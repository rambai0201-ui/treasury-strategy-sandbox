import streamlit as st

st.set_page_config(
    page_title="Treasury Strategy Sandbox",
    page_icon="💰",
    layout="wide",
)

# Sidebar: starting assumptions
with st.sidebar:
    st.header("Model setup")
    st.caption("Fictional demonstration inputs only.")

    st.selectbox(
        "Currency",
        options=["AUD"],
        help="All monetary inputs use this currency.",
    )

    st.number_input(
        "Forecast horizon (months)",
        value=24,
        disabled=True,
    )

    opening_cash = st.number_input(
        "Opening available cash",
        min_value=0.0,
        value=10_000_000.0,
        step=100_000.0,
        format="%.2f",
        help="Cash available at the start of the forecast.",
    )

    liquidity_buffer = st.number_input(
        "Minimum liquidity buffer",
        min_value=0.0,
        value=2_000_000.0,
        step=100_000.0,
        format="%.2f",
        help="The minimum available cash balance you want to maintain.",
    )

    st.info(
        "These inputs are not connected to a forecast yet."
    )

# Main heading
st.title("Treasury Strategy Sandbox")
st.write(
    "Explore treasury decisions, test assumptions, "
    "and understand the trade-offs."
)
st.caption(
    "A demonstration decision-support tool, not financial advice "
    "or a transaction-processing system."
)

# Main workspace
position_tab, forecast_tab, strategy_tab = st.tabs(
    [
        "1. Starting position",
        "2. Cash-flow forecast",
        "3. Strategy lab",
    ]
)

with position_tab:
    st.subheader("Your starting position")
    st.write(
        "Define the financial position before exploring "
        "what happens next."
    )

    cash_column, buffer_column = st.columns(2)

    with cash_column:
        st.metric(
            "Opening available cash",
            f"AUD {opening_cash:,.0f}",
        )

    with buffer_column:
        st.metric(
            "Minimum liquidity buffer",
            f"AUD {liquidity_buffer:,.0f}",
        )

    st.divider()

    st.markdown("#### Building blocks")
    st.markdown(
        """
        - **Operating cash flows:** monthly receipts and payments.
        - **Investments:** placements, maturities and interest received.
        - **Debt:** borrowings, repayments and interest paid.
        - **Liquidity:** available cash compared with the minimum buffer.
        """
    )

    st.caption(
        "Only opening cash and the liquidity buffer are editable "
        "at this stage. The other building blocks come next."
    )

with forecast_tab:
    st.subheader("Understand the baseline")
    st.write(
        "What happens over the next 24 months "
        "before you introduce a new strategy?"
    )

    st.info(
        "Coming next: monthly cash-flow inputs, "
        "an explainable forecast table, and a liquidity chart."
    )

with strategy_tab:
    st.subheader("Explore a treasury decision")
    st.write(
        "The forecast will support experiments, "
        "rather than being the final product."
    )

    st.markdown(
        """
        Possible future experiments:

        - **Fix or float?** Compare borrowing-rate strategies.
        - **Invest short or longer?** Explore return versus liquidity.
        - **Repay debt or retain cash?** Examine the trade-offs.
        - **What if your market view is wrong?** Stress-test a strategy.
        """
    )

    st.warning(
        "Not implemented yet. Strategy comparisons will be added "
        "after the baseline forecast is validated."
    )