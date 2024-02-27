# Pycaret 
> *PyCaret simplifies and accelerates the Machine Learning workflow, 
allowing data scientists to **focus on the interpretation and implementation of models rather than the underlying technical processes.***  



    
PyCaret은 python용 low-code open-source  ML 라이브러리이다. 
기본적으로 sklearn 및 다른 라이브러리들을 포함하고 있어, 다양한 모델을 시도하고, 교차 검증과 앙상블까지 간단한 코드로 수행할 수 있는 Auto ML이다. 
머신러닝에 익숙하지 않는 사람도 아주 쉽고 간편하게 머신러닝을 돌릴 수 있다.

------
## AutoML 언제 사용하면 좋을까?
프로젝트를 진행하면서 어떤 알고리즘으로 먼저 테스트해봐야 할지 감이 안잡힐 때 Auto ML을 사용하면 편하다.   
PyCaret은 인코딩, 대치, 스케일링 등 수동으로 수행할 때 상당한 시간과 노력이 필요한 다양한 전처리 문제에 대한 자동화된 솔루션을 제공한다.   
포함된 알고리즘의 다양성을 통해 사용자는 최상의 모델을 신속하게 비교하고 선택할 수 있다.  

------
## AutoML using PyCaret - `Classification`
PyCaret으로 분류 머신러닝 모델을 만드는 단계는 다음과 같다. 

**1. 분석 환경 만들기(Setup)**
- 분류 패키지의 모든 모듈을 임포트한다.
from pycaret.classification import *
 
- 환경 설정
`setup()`  
분석 환경을 설정하는 것으로, 샘플링, 결측치 보정, 인코딩 등 데이터 셋에 대한 전처리가 포함된다. 파라미터가 정말 많다. 

setup 파라미터 설명 : 
  https://pycaret.readthedocs.io/en/stable/api/classification.html#pycaret.classification.setup
    
     
**2. 모델 비교하기 `compare_model()`**  
처음 단계로 setup설정에 맞춰 여러 모델을 놓고 점수를 비교한다.   
우수한 모델부터 순차적으로 보여준다.   

   
**3. 모델 생성하기 `create_model()`**  
estimator에 생성할 모델 약어(ex: 'rf', 'catboost')를 적어 모델을 생성한다.   
    
  
**4. 모델 튜닝 `tune_model()`**  
sklearn의 gridsearch와 같은 기능을 수행하는 메소드이다.   
optimize 매개변수에 튜닝을 통해 최적화하고자 하는 매트릭를 적는다.     

  
**5. 시각화 - 모델 분석**  
Pycaret은 모델 분석을 위한 다양한 시각화 자료도 제공한다.   
    
5.1 `plot_model()`  
모델의 특성 중요도, auc Curve. 혼동행렬등을 보여준다.
- plot 매개변수 종류 : 'auc' / 'thereshold' / 'pr' / 'class_report' / 'feature' 등
  
5.2 `interpret_model()`  
shap 시각화를 보여주며, shap 패키지가 설치되어 있어야 한다.   
imterpret_model(model, plot='summary')    
  
5.3 `evaluate_model()`    
인터렉티브 대시보드처럼 클릭하여 위의 기능들을 실행할 수 있게 해준다.   
  


#시각화 -SHAP 
https://www.kaggle.com/code/dansbecker/shap-values/tutorial
