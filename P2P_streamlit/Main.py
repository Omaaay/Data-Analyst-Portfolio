import numpy as np
import pandas as pd
import streamlit as st





# 네비게이션 구성 설정
st.set_page_config(initial_sidebar_state='collapsed', layout='wide')







# csv 캐싱, 변수 할당
@st.cache_data
def load_data():
    accept = pd.read_csv("P2P_streamlit/data/dashboard_data2.csv", low_memory=False)
    target = "loan_status"
    X, y = accept.loc[:, [column for column in accept.columns if column != target]], accept[target]
    data = pd.concat((X, y ), axis=1).reset_index(drop=True)
    data['sub_grade'] = pd.Categorical(data['sub_grade'], categories=sorted(data.sub_grade.unique()), ordered=True)
    numric_features = data.select_dtypes(include=np.number).columns.tolist()
    categorical = data.select_dtypes(exclude=np.number).columns.tolist()[:-1]
    return numric_features, categorical, target, data

numric_features, categorical, target, data = load_data()
colors = ['#66b3ff','#ff9999']

# 페이지 전역 변수 설정
st.session_state.numric_features = numric_features
st.session_state.categorical = categorical
st.session_state.target = target
st.session_state.data = data
st.session_state.colors = colors





centered_button_style = """
<style>
    .stButton>button {
        display: block;
        margin: auto;
        border: None;
        width: 6em; 
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
    }
    .stButton>button:hover {
        background-color: whiteblue !important;
        color: red !important;
        border: 0.2px solid #E5E5E5 !important;
        box-shadow: None !important;
        font-weight: bold;
        transition: box-shadow 0.3s ease;
    }

    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-uf99v8.ea3mdgi8 > div.block-container.st-emotion-cache-z5fcl4.ea3mdgi5 > div > div > div > div:nth-child(6){
         position: fixed;
         top: 2.9em;
         width: 92%;
         z-index: 9999;
         background-color: white;
    }

    # #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-uf99v8.ea3mdgi8 > div.block-container.st-emotion-cache-z5fcl4.ea3mdgi5 > div > div > div:nth-child(1) > div > div{
    # background-color: red;
    # }

    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-uf99v8.ea3mdgi8 > div.block-container.st-emotion-cache-z5fcl4.ea3mdgi5 > div > div > div > div:nth-child(7) > div:nth-child(1) > div > div > div > div > div > button{
        width: 8em;
        margin-left: 0em;
    }
    
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-uf99v8.ea3mdgi8 > div.block-container.st-emotion-cache-z5fcl4.ea3mdgi5 > div > div > div > div:nth-child(7) > div:nth-child(2) > div > div > div > div > div > button{
        width: 75%;
        margin-right: 0em;
        position: absolute;
        right: 0em;
    }
    
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-uf99v8.ea3mdgi8 > div.block-container.st-emotion-cache-z5fcl4.ea3mdgi5 > div > div > div > div:nth-child(7) > div:nth-child(3) > div > div > div > div > div > button{
        width: 75%;
        margin-right: 0em;
    }


    
</style>
"""
###
# 사용자 정의 스타일을 포함한 HTML 문자열
custom_css = """
<style>
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-uf99v8.ea3mdgi8 > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div.st-emotion-cache-0.eqpbllx5 > details {
        border: None;
    }
    
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-uf99v8.ea3mdgi8 > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi5 > div > div > div > div:nth-child(5) > div:nth-child(1) > div > div > div > div > div > button{
         margin-left: 1em;
    }
    
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-uf99v8.ea3mdgi8 > div.block-container.st-emotion-cache-z5fcl4.ea3mdgi5 > div > div > div > div:nth-child(6) > div:nth-child(1) > div > div > div > div > div > button{
        width: 8em;
        margin-left: 0em;
    }
    
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-uf99v8.ea3mdgi8 > div.block-container.st-emotion-cache-z5fcl4.ea3mdgi5 > div > div > div > div:nth-child(6) > div:nth-child(2) > div > div > div > div > div > button{
        width: 75%;
        margin-right: 0em;
        position: absolute;
        right: 0em;
    }
    
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-uf99v8.ea3mdgi8 > div.block-container.st-emotion-cache-z5fcl4.ea3mdgi5 > div > div > div > div:nth-child(6) > div:nth-child(3) > div > div > div > div > div > button{
        width: 75%;
        margin-right: 0em;
    }
</style>
"""
###
# 사용자 정의 스타일을 포함한 HTML 문자열
expander_css = """
<style>
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-uf99v8.ea3mdgi8 > div.block-container.st-emotion-cache-z5fcl4.ea3mdgi5 > div > div > div > div:nth-child(8) > details{
        border: 0px solid #E5E5E5;
        heigh: 2px;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-uf99v8.ea3mdgi8 > div.block-container.st-emotion-cache-z5fcl4.ea3mdgi5 > div > div > div > div:nth-child(8) > details > summary > svg.eyeqlp51.st-emotion-cache-1pbsqtx.ex0cdmw0{
        width: 3em;
        heigh: 3em !important;
        color: red;
    }
</style>
"""
###
# 특성 설명 버튼 HTML 문자열
page_button_style = """
<style>
    
    
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-uf99v8.ea3mdgi8 > div.block-container.st-emotion-cache-z5fcl4.ea3mdgi5 > div > div > div > div:nth-child(11) > div:nth-child(1) > div > div > div > div > div > button{
        width: 400px;
        height:300px;
        margin-left: 150px;
    }
      #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-uf99v8.ea3mdgi8 > div.block-container.st-emotion-cache-z5fcl4.ea3mdgi5 > div > div > div > div:nth-child(11) > div:nth-child(1) > div > div > div > div > div > p{
        font-size: 1.4rem;
        font-weight: bold;
    }
    
   #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-uf99v8.ea3mdgi8 > div.block-container.st-emotion-cache-z5fcl4.ea3mdgi5 > div > div > div > div:nth-child(11) > div:nth-child(2) > div > div > div > div > div > button{
        width: 400px;
        height:300px;
        margin-right: 300px;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-uf99v8.ea3mdgi8 > div.block-container.st-emotion-cache-z5fcl4.ea3mdgi5 > div > div > div > div:nth-child(11) > div:nth-child(2) > div > div > div > div > div > p{
        font-size: 1.4rem;
        font-weight: bold;
    }
    
</style>
"""


# 버튼의 기본값 설정
st.markdown(centered_button_style, unsafe_allow_html=True)

# 커스텀 CSS 적용
st.markdown(custom_css, unsafe_allow_html=True)

# 커스텀 CSS st.expander
st.markdown(expander_css, unsafe_allow_html=True)

# 커스텀 특성 소개 버튼
st.markdown(page_button_style, unsafe_allow_html=True)
################################################################################




# 페이지 구성
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Main"):
        st.switch_page("Main.py")
with col2:
    if st.button("Analyst"):
        st.switch_page("pages/Analyst.py")
with col3:
    if st.button("Investor"):
        st.switch_page("pages/Investor.py")


####
st.markdown('## Lending Club P2P대출 상환 예측')
st.markdown('Analyst는 분석가를 위한 예측 모델링 변수간의 EDA를 간편하게 확인할 수 있습니다')
st.markdown('Investor는 투자자의 투자 결정을 돕기 위한 대출신청자의 상환 확률을 확인할 수 있습니다')
st.divider()
####
col1, col2 = st.columns(2)
with col1:
    if st.button("Analyst",key=1, use_container_width=True):
        st.switch_page("pages/Analyst.py")
with col2:
    if st.button("Investor",key=2, use_container_width=True):
        st.switch_page("pages/Investor.py")

####
st.divider()
####







