import streamlit as st
import streamlit.components.v1 as components

if st.button("Open"):
    components.html(
        f'''
        <script type="text/javascript">
        window.open("{st.secrets["URL"]}", "_blank").focus();
        </script>
        ''',
        height=300,
    )
