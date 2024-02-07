import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(layout='wide')
new_col = ['active', 'enter_year',
              '2024f', '2024d', '2024m',  # R06
              '2023f', '2023d', '2023m',  # R05
              '2022f', '2022d', '2022m',  # R04
              '2021f', '2021d', '2021m',  # R03
              '2020f', '2020d', '2020m',  # R02
              '2019f', '2019d', '2019m',  # R01
              '2018f', '2018d', '2018m',  # H30
              '2017f', '2017d', '2017m',  # H29
              '2016f', '2016d',  # H28
              '2015f', '2015d',  # H27
              '2014f', '2014d',  # H26
              '2013f', '2013d',  # H25
              '2012f', '2012d',  # H24
              '2011f', '2011d',  # H23
              '2010f',  # H22
              '2009f',  # H21
              '2008f',  # H20
              '2007f',  # H19
              '2006f',  # H18
              '2005f',  # H17
              '2004f', '2004d', # H16
              '2003f', '2003d',  # H15
              '2002f',  # H14
              '2001f',  # H13
              ]

def pre_proc(df):
    df.columns = new_col

    for i in range (2024, 2000, -1):
        fee = str(i) +'f'
        donate = str(i) +'d'
        meth = str(i) + 'm'
        if donate in new_col:
            df[f'{i}'] = df[fee] + df[donate]
            df = df.drop(columns=[donate, fee])
        else:
            df[f'{i}'] = df[fee]
            df = df.drop(columns=[fee])
        if meth in new_col:
            df = df.drop(columns=[meth]) 
    df = df.drop(columns='active')
    df = df.drop(columns='2024')
    return df

def enter_corr(sum_df):
    enter_list = [str(i) for i in range(1998, 2020, 1)]
    df_list = []



def main():
    #
    df = pd.read_csv('payment.csv', encoding='shift-jis')
    df = pre_proc(df)
    sum_df = df.groupby('enter_year').count().T
    sum_df.columns = sum_df.columns.map(lambda x: str(x))

    shift_df_list = []
    year_list = [str(i) for i in range(1998, 2021, 1)]
    for i, y in enumerate(year_list):
        tmp = sum_df.loc[:, y].shift(i)
        shift_df_list.append(tmp)
    shift_df = pd.concat(shift_df_list, axis=1)
    
    # for col in shift_df.columns[0:10]:
        

    

    s1, s2,s3 = st.columns(3)
    # s3, s4, s5, s6 = st.columns(6)
    with s1:
        data = []
        for col in sum_df.columns[0:10]:
            data.append(go.Scatter(x=sum_df.index, y=sum_df[col], name=col))
        fig = go.Figure(data)
        st.plotly_chart(fig, use_container_width=True)
    with s2: 
        data = []
        for col in sum_df.columns[10:20]:
            data.append(go.Scatter(x=sum_df.index, y=sum_df[col], name=col))
        fig = go.Figure(data)
        st.plotly_chart(fig, use_container_width=True)
    
    with s3:
        data = []
        for col in sum_df.columns[20:30]:
            data.append(go.Scatter(x=sum_df.index, y=sum_df[col], name=col))
        fig = go.Figure(data)
        st.plotly_chart(fig, use_container_width=True)
    
    s4, s5,s6 = st.columns(3)
    
    with s4:
        data = []
        for col in sum_df.columns[30:40]:
            data.append(go.Scatter(x=sum_df.index, y=sum_df[col], name=col))
        fig = go.Figure(data)
        st.plotly_chart(fig, use_container_width=True)
    
    with s5:
        data = []
        for col in sum_df.columns[40:50]:
            data.append(go.Scatter(x=sum_df.index, y=sum_df[col], name=col))
        fig = go.Figure(data)
        st.plotly_chart(fig, use_container_width=True)
    
    with s6:
        data = []
        for col in sum_df.columns[50:]:
            data.append(go.Scatter(x=sum_df.index, y=sum_df[col], name=col))
        fig = go.Figure(data)
        st.plotly_chart(fig, use_container_width=True)

    # 入学してからの
if __name__ == '__main__':
    main()
