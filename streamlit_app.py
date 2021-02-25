import streamlit as st
import pandas as pd
import numpy as np
from fpgrowth_py import fpgrowth
import pyfpgrowth
import base64
import markdown
import streamlit.components.v1 as components

# read in the dataset
patterns = pd.read_csv('../data/patterns.csv')
rules = pd.read_csv('../data/rules.csv')

# Use the full page instead of a narrow central column
st.beta_set_page_config(layout="wide")

# add a static header
st.write('<style>body { margin: 0; font-family: Arial, Helvetica, sans-serif;} .header{padding: 40px 540px; background: #465; color: #20c997; position:fixed;top:0;} .sticky { position: fixed; top: 0; width: 100%;} </style><div class="header" id="myHeader">', unsafe_allow_html=True)

# set title of the page
st.title('**Frequent Item Analysis**')

# create a sidebar
st.sidebar.header('Dataset at a Glance')
st.sidebar.markdown('3.4M orders') # Add project details, number of orders, number of unique users, top products, busy and slow days etc.

# reduce sidebar width
st.markdown(
    f'''
        <style>
            .sidebar .sidebar-content {{
                width: 200px;
            }}
        </style>
    ''',
    unsafe_allow_html=True
)

# App Header
st.header('What Will Your Customer Buy Next?')

# Brief Instructions on how to use the app
st.write(
"Choose an item from the dropdown menu and click the 'Get Pair' button to see a product most frequently purchased together.")

#ask user to select a product
product_choice = st.selectbox(
    ('Select Item'),
    rules['antecedent_1']
)
# t = st.text_input("Pick an item from the list")
start = st.button(
    ('Get Pair'),
    rules['consequent']
)
# for loop to run through the algorithm results
if start:
    for item in rules['antecedent_1']:
            print(f"Most Frequently Bought together item is {rules['consequent']} with {rules['confidence_level']} confident level.")

st.image('./assets/background.jpg')

def main():
    html_temp = """<div class='tableauPlaceholder' id='viz1614215722694' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;al&#47;all_orders_dashboard&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='all_orders_dashboard&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;al&#47;all_orders_dashboard&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1614215722694');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='650px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='887px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='650px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='887px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
    components.html(html_temp)
    
if __name__ == "__main__":
    main()
