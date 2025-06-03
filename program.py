import streamlit as st
import pandas as pd
import numpy as np

data = pd.DataFrame(
    np.random.randn(10, 2),
    columns=["A", "B"]
)

st.line_chart(data)

