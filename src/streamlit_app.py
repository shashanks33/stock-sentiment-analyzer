# streamlit_app.py

import streamlit as st
import pandas as pd

from reddit_sentiment import RedditSentimentAnalyzer
from stock_data      import StockDataFetcher

analyzer = RedditSentimentAnalyzer()
fetcher = StockDataFetcher()

st.title("📰📈 Stock Sentiment Analyzer")

stock_symbol = st.text_input(
    "Ticker symbol", 
    value="", 
    placeholder="e.g. AAPL, GOOGL, MSFT"
).upper()

if st.button("Analyze"):
    with st.spinner("Fetching data…"):
        result = analyzer.analyze_sentiment(stock_symbol)

        if not result['success']:
            st.error(result['error'])
        else:
            avg     = result['average_sentiment']
            verdict = "Bullish" if avg > 0 else ("Bearish" if avg < 0 else "Neutral")
            st.metric("Avg Sentiment", f"{avg:.3f}", verdict)

            # ---------------------
        # fetch current price via your fetcher instance
        stock_res = fetcher.get_stock_data(stock_symbol)
        if stock_res['success']:
            cp  = stock_res['data']['current_price']
            cur = stock_res['data']['currency']
            st.metric("Current Price", f"{cp:.2f} {cur}")
        else:
            st.error(stock_res['error'])
            # ---------------------

            # top posts table
            df_top = pd.DataFrame(result['top_posts'])
            df_top['sentiment'] = df_top['sentiment'].map(lambda x: f"{x:.3f}")
            st.subheader("Top 5 Reddit Posts")

            for post in result['top_posts']:
                # Container for visual spacing (optional)
                with st.container():
                    # Clickable title
                    st.markdown(
                        f"**[{post['title']}]({post['url']})**",
                        unsafe_allow_html=True
                    )
                    # Key metadata
                    st.write(
                        f"Score: **{post['score']}**   |   "
                        f"Sentiment: **{post['sentiment']:.3f}**   |   "
                        f"Posted: **{post['created_utc']}**"
                    )
                    # Expander for the full body
                    with st.expander("▶️ Show full post"):
                        if post['text'].strip():
                            st.write(post['text'])
                        else:
                            st.write("_No body text available_")


