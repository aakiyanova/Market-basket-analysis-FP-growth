import streamlit as st
import pandas as pd
import numpy as np
from fpgrowth_py import fpgrowth
import pyfpgrowth
import base64
import markdown
import streamlit.components.v1 as components
import plotly.express as px
import plotly.graph_objects as go
from plotly import tools
import plotly.offline as py


# read in the datasets
rules = pd.read_csv('../../data/rules_50_percent_app.csv')
all_orders = pd.read_csv('../../data/all_orders.csv')

# Use the full page instead of a narrow central column
st.beta_set_page_config(layout="wide")

# add a static header
st.write('<style>body { margin: 0; font-family: Arial, Helvetica, sans-serif;} .header{padding: 40px 540px; background: #465; color: #20c997; position:fixed;top:0;} .sticky { position: fixed; top: 0; width: 100%;} </style><div class="header" id="myHeader">', unsafe_allow_html=True)

# set title of the page
st.title('**Market Basket Analysis**')

# create a sidebar
st.sidebar.header('Dataset at a Glance')

# add data details to the sidebar
st.sidebar.write('2017 Instacart Data')
st.sidebar.write('3.4M orders \n')
st.sidebar.write('206k unique customer IDs \n')
st.sidebar.write('34M rows \n')
st.sidebar.write('50k unique products \n')

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

# create df filters on the antecedent column
filter_strawberries = rules['antecedent'] == "'organic_strawberries'"
filter__hass_avocado = rules['antecedent'] == "'organic hass avocado'"
filter_garlic = rules['antecedent'] == "'organic garlic'"
filter_bag_bananas = rules['antecedent'] == "'bag of organic bananas'"
filter_yogurt = rules['antecedent'] == "'icelandic style skyr blueberry non-fat yogurt'"
filter_soda = rules['antecedent'] == "'soda'"
filter_banana = rules['antecedent'] == "'banana'"
filter_zucchini = rules['antecedent'] == "'organic zucchini'"
filter_lemon = rules['antecedent'] == "'large lemon'"
filter_spinach = rules['antecedent'] == "'organic baby spinach'"
filter_lemon = rules['antecedent'] == "'large lemon'"
filter_avocado = rules['antecedent'] == "'organic avocado'"


# button to showcase the results
if st.button('See Basket'):
        # apply filters
        if product_choice == "'strawberries'":
            st.write(rules[filter_strawberries])
        if product_choice == "'organic hass avocado'":
            st.write(rules[filter_hass_avocado])
        if product_choice == "'organic garlic'":
            st.write(rules[filter_garlic])
        if product_choice == "'bag of organic bananas'":
            st.write(rules[filter_bag_bananas])
        if product_choice == "'icelandic style skyr blueberry non-fat yogurt'":
            st.write(rules[filter_yogurt])
        if product_choice == "'soda'":
            st.write(rules[filter_soda])
        if product_choice == "'banana'":
            st.write(rules[filter_banana])
        if product_choice == "'organic zucchini'":
            st.write(rules[filter_zucchini])
        if product_choice == "'large lemon'":
            st.write(rules[filter_lemon])
        if product_choice == "'organic baby spinach'":
            st.write(rules[filter_spinach])
        if product_choice == "'organic avocado'":
            st.write(rules[filter_avocado])

st.image('../assets/background.jpg')

@st.cache
def load_data():
    """Function to load the data"""
    df = pd.read_csv('../../data/all_orders.csv')

    numeric_df = df.select_dtypes(['float64', 'int64'])
    numeric_cols = numeric_df.columns

    text_df = df.select_dtypes(['object'])
    text_cols = text_df.columns

    aisle_column = df['aisle']

    unique_aisle = aisle_column.unique()

    return df, numeric_cols, text_cols, unique_aisle

df, numeric_cols, text_cols, unique_aisle = load_data()

# header of Dashboard + explanation
st.header("**Data Dashboard**")
st.write("The dashboard allows to interactively explore the Instacart order data")

# give sidebar a heading
st.sidebar.header('Settings')
# st.sidebar.subheader('Product Breakdown')

# add checknob to sidebar
check_box = st.sidebar.checkbox(label = 'Display dataset')

# if checked, display full all_orders df
if check_box:
    st.write(df)

# sidebar: select numeric columns for the dashboard
feature_selection = st.sidebar.multiselect(label='Features to plot', options=numeric_cols)

# sidebar: select aisles
aisle_dropdown = st.sidebar.selectbox(label='Aisles', options=unique_aisle)

print(feature_selection)
# filter df by aisles
df = df[df['aisle'] == aisle_dropdown]
df_features = df[feature_selection]

# bar plot the dashboard results
plotly_figure = px.bar(data_frame=df_features, x=df_features.index, y=feature_selection, title=(str.capitalize(aisle_dropdown) + ' ' + 'sales'))
# print the bar plot
st.plotly_chart(plotly_figure)
