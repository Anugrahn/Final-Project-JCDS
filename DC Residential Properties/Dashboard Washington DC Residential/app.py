from flask import Flask,render_template,request
from datas import quadrant,property_type,ward,neighborhood,style,structure,extwall,intwall,roof,qualified,condition,grade,ac,heat
from prediction import prediction,hasil_table
from plots import quadrant_plots,ward_plots
app = Flask(__name__)

@app.route('/',methods= ['GET','POST'])
def index():
    if request.method == 'POST':
        data = request.form
        data = data.to_dict()
        data['NUM_UNITS'] = int(data['NUM_UNITS'])
        data['BLDG_NUM'] = int(data['BLDG_NUM'])
        data['ROOMS'] = int(data['ROOMS'])
        data['BEDRM'] = int(data['BEDRM'])
        data['BATHRM'] = int(data['BATHRM'])
        data['HF_BATHRM'] = int(data['HF_BATHRM'])
        data['KITCHENS'] = int(data['KITCHENS'])
        data['FIREPLACES'] = int(data['FIREPLACES'])
        data['LANDAREA'] = int(data['LANDAREA'])
        data['GBA'] = int(data['GBA'])
        data['YR_RMDL'] =int(data['YR_RMDL'])
        hasil = prediction(data)
        return render_template('result.html' , hasil_pred=hasil)
        # return render_template('result.html',hasil_pred=hasil)
        # kita jalanin function predict
        # Render reulst.html
    return render_template('prediction.html',data_quadrant = sorted(quadrant), 
    data_ward = sorted(ward), data_neighborhood = sorted(neighborhood), data_style= sorted(style),
    data_struct= sorted(structure), data_ext = sorted(extwall), data_int= sorted(intwall), data_roof=sorted(roof),
    data_qualified = sorted(qualified), data_condition = sorted(condition), data_grade=sorted(grade), data_ac=sorted(ac),
    data_heat=sorted(heat),
    data_property = sorted(property_type))

@app.route('/data')
def login():
    data = quadrant_plots()
    data2 = ward_plots()
    return render_template('plots.html',data=data,data2=data2)

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)