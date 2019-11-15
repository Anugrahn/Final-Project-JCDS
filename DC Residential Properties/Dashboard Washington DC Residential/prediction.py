import pickle
import pandas as pd
from pandas import DataFrame,get_dummies

model = pickle.load(open('finalized_model.sav','rb'))
encoder_features = pickle.load(open('encoder_features.sav','rb'))
scaller_features = pickle.load(open('scaller_features.sav','rb'))

def applyGRADE(x):
    if x.GRADE == 'Fair Quality':
        return 0
    elif x.GRADE == 'Low Quality':
        return 1
    elif x.GRADE == 'Average':
        return 2
    elif x.GRADE == 'Above Average':
        return 3
    elif x.GRADE == 'Good Quality':
        return 4
    elif x.GRADE == 'Very Good':
        return 5
    elif x.GRADE == 'Exceptional-C':
        return 6
    elif x.GRADE == 'Exceptional-B':
        return 7
    elif x.GRADE == 'Exceptional-A':
        return 8
    elif x.GRADE == 'Excellent':
        return 9
    elif x.GRADE == 'Superior':
        return 10

def applyCNDTN(x):
    if x.CNDTN == 'Poor':
        return 0
    elif x.CNDTN == 'Fair':
        return 1
    elif x.CNDTN == 'Average':
        return 2
    elif x.CNDTN == 'Good':
        return 3
    elif x.CNDTN == 'Very Good':
        return 4
    elif x.CNDTN == 'Excellent':
        return 5

def prediction(data):
    df = DataFrame(data,index=[0])
    df.CNDTN = df.apply(applyCNDTN,axis=1)
    df.GRADE = df.apply(applyGRADE,axis=1)
    import category_encoders as ce
    df_temp = encoder_features.transform(df.drop(['GRADE','CNDTN'],axis=1)).drop(['HEAT_0','AC_0','STYLE_0','STRUCT_0',
            'EXTWALL_0','QUALIFIED_0','ROOF_0','INTWALL_0','ASSESSMENT_NBHD_0','WARD_0','QUADRANT_0'], axis=1)
    df = pd.concat([df_temp,df[['GRADE','CNDTN']]],axis=1)
    df_scaled = scaller_features.transform(df[['YR_RMDL','GBA','LANDAREA']])
    df_scaled = pd.DataFrame(df_scaled,columns=['YR_RMDL','GBA','LANDAREA'])
    df = pd.concat([df.drop(['YR_RMDL','GBA','LANDAREA'],axis=1),df_scaled],axis=1)
    df = df[['BATHRM', 'HF_BATHRM', 'HEAT_1', 'HEAT_2', 'HEAT_3', 'HEAT_4', 'AC_1',
       'NUM_UNITS', 'ROOMS', 'BEDRM', 'QUALIFIED_1', 'BLDG_NUM', 'STYLE_1',
       'STYLE_2', 'STYLE_3', 'STYLE_4', 'STYLE_5', 'STRUCT_1', 'STRUCT_2',
       'STRUCT_3', 'EXTWALL_1', 'EXTWALL_2', 'EXTWALL_3', 'EXTWALL_4',
       'EXTWALL_5', 'ROOF_1', 'ROOF_2', 'ROOF_3', 'ROOF_4', 'INTWALL_1',
       'INTWALL_2', 'INTWALL_3', 'INTWALL_4', 'KITCHENS', 'FIREPLACES',
       'ASSESSMENT_NBHD_1', 'ASSESSMENT_NBHD_2', 'ASSESSMENT_NBHD_3',
       'ASSESSMENT_NBHD_4', 'ASSESSMENT_NBHD_5', 'ASSESSMENT_NBHD_6', 'WARD_1',
       'WARD_2', 'WARD_3', 'QUADRANT_1', 'QUADRANT_2', 'GRADE', 'CNDTN',
       'YR_RMDL', 'GBA', 'LANDAREA']]
    hasil = model.predict(df)
    hasil_fix = int(hasil[0])
    return hasil_fix

def hasil_table(data):
    df = DataFrame(data,index=[0])
    return df