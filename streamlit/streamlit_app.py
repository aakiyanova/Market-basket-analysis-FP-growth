import streamlit as st
import pandas as pd
import numpy as np
from fpgrowth_py import fpgrowth
import pyfpgrowth
import base64
import markdown
import streamlit.components.v1 as components
import plotly.express as px


# read in the datasets
rules = pd.read_csv('../../data/rules_app.csv')
all_orders = pd.read_csv('../../data/all_orders.csv')

# Use the full page instead of a narrow central column
st.beta_set_page_config(layout="wide")

# add a static header
st.write('<style>body { margin: 0; font-family: Arial, Helvetica, sans-serif;} .header{padding: 40px 540px; background: #465; color: #20c997; position:fixed;top:0;} .sticky { position: fixed; top: 0; width: 100%;} </style><div class="header" id="myHeader">', unsafe_allow_html=True)

# set title of the page
st.title('**Market Basket Analysis**')

# create a sidebar
st.sidebar.header('Dataset at a Glance')
st.sidebar.write('2017 Instacart Data')
st.sidebar.write('3.4M orders \n')
st.sidebar.write('206k unique customer IDs \n')
st.sidebar.write('34M rows \n')
st.sidebar.write('50k unique products \n')

 # Add project details, number of orders, number of unique users, top products, busy and slow days etc.

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
"Choose an item from the dropdown menu and click the 'See Basket' button to see products most frequently purchased together.")

#ask user to select a product
product_choice = st.selectbox(
    ('Select Item'),
    rules['antecedent']
)

filter_strawberries = rules['antecedent'] == 'organic strawberries'
filter_raspberries = rules['antecedent'] == 'organic raspberries'
filter_avocado = rules['antecedent'] == 'organic hass avocado'
filter_spinach = rules['antecedent'] == 'organic baby spinach'

# t = st.text_input("Pick an item from the list")
if st.button('See Basket'):

# #apply filters to the dataframe
        if product_choice == 'organic raspberries':
            st.write(rules[filter_raspberries])
        if product_choice == 'organic strawberries':
            st.write(rules[filter_strawberries])
        if product_choice == 'organic hass avocado':
            st.write(rules[filter_avocado])
        if product_choice == 'organic baby spinach':
            st.write(rules[filter_spinach])


st.image('../assets/background.jpg')



# def main():
#     html_temp = """<div class='tableauPlaceholder' id='viz1614371486793' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ma&#47;MarketBasketAnalysis_Departments&#47;DepartmentAnalysis&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='MarketBasketAnalysis_Departments&#47;DepartmentAnalysis' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ma&#47;MarketBasketAnalysis_Departments&#47;DepartmentAnalysis&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1614371486793');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='1416px';vizElement.style.height='991px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
#     components.html(html_temp)
#
# if __name__ == "__main__":
#     main()
