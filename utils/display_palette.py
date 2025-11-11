import streamlit as st

def display_palette(hex_colors):
    st.markdown("<div style='display:flex;justify-content:center;flex-wrap:wrap;margin-top:10px'>", unsafe_allow_html=True)
    for color in hex_colors:
        st.markdown(
            f"""
            <div style='background-color:{color};
                        width:100px;height:100px;
                        border-radius:12px;
                        margin:6px;
                        box-shadow:0 0 8px rgba(0,0,0,0.25);
                        text-align:center;
                        line-height:100px;
                        color:#fff;
                        font-weight:bold;
                        cursor:pointer'
                 title='{color}'>{color}</div>
            """,
            unsafe_allow_html=True
        )
    st.markdown("</div>", unsafe_allow_html=True)
