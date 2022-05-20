import pandas as pd
import json
import plotly
import plotly.express as px
from flask import Flask, render_template, request
from joblib import load
app = Flask(__name__)

df = pd.read_csv('Mumbai1.csv')

model = load('model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/facilities')
def facilities():
    sp = df.groupby(df['Swimming Pool'])['Unnamed: 0'].count()
    fig1 = px.bar(sp,x=['No','Yes'],y=sp.values,color=['No','Yes'],title='Swimming Pool Availability',
            labels={'x':'status','y':'No. of houses'})
    graph1 = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

    jt = df.groupby(df['Jogging Track'])['Unnamed: 0'].count()
    fig2 = px.bar(jt,x=['No','Yes'],y=jt.values,color=['No','Yes'],title='Jogging Track Availability',
            labels={'x':'status','y':'No. of houses'})
    graph2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)

    gc = df.groupby(df['Gas Connection'])['Unnamed: 0'].count()
    fig3 = px.bar(gc,x=['No','Yes'],y=gc.values,color=['No','Yes'],title='Gas Connection Availability',
            labels={'x':'status','y':'No. of houses'})
    graph3 = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)

    ig = df.groupby(df['Indoor Games'])['Unnamed: 0'].count()
    fig4 = px.bar(ig,x=['No','Yes'],y=ig.values,color=['No','Yes'],title='Indoor Games Availability',
            labels={'x':'status','y':'No. of houses'})
    graph4 = json.dumps(fig4, cls=plotly.utils.PlotlyJSONEncoder)

    lg = df.groupby(df['Landscaped Gardens'])['Unnamed: 0'].count()
    fig5 = px.bar(lg,x=['No','Yes'],y=lg.values,color=['No','Yes'],title='Landscaped Gardens',
            labels={'x':'status','y':'No. of houses'})
    graph5 = json.dumps(fig5, cls=plotly.utils.PlotlyJSONEncoder)

    ic = df.groupby(df['Intercom'])['Unnamed: 0'].count()
    fig6 = px.bar(ic,x=['No','Yes'],y=ic.values,color=['No','Yes'],title='Intercom Availability',
            labels={'x':'status','y':'No. of houses'})
    graph6 = json.dumps(fig6, cls=plotly.utils.PlotlyJSONEncoder)

    ch = df.groupby(df['Clubhouse'])['Unnamed: 0'].count()
    fig7 = px.bar(ch,x=['No','Yes'],y=ch.values,color=['No','Yes'],title='Clubhouse Availability',
            labels={'x':'status','y':'No. of houses'})
    graph7 = json.dumps(fig7, cls=plotly.utils.PlotlyJSONEncoder)

    sec = df.groupby(df['24x7 Security'])['Unnamed: 0'].count()
    fig8 = px.bar(sec,x=['No','Yes'],y=sec.values,color=['No','Yes'],title='24x7 Security',
            labels={'x':'status','y':'No. of houses'})
    graph8 = json.dumps(fig8, cls=plotly.utils.PlotlyJSONEncoder)

    ms = df.groupby(df['Maintenance Staff'])['Unnamed: 0'].count()
    fig9 = px.bar(ms,x=['No','Yes'],y=ms.values,color=['No','Yes'],title='Maintenance Staff',
            labels={'x':'status','y':'No. of houses'})
    graph9 = json.dumps(fig9, cls=plotly.utils.PlotlyJSONEncoder)

    cp = df.groupby(df['Car Parking'])['Unnamed: 0'].count()
    fig10 = px.bar(cp,x=['No','Yes'],y=cp.values,color=['No','Yes'],title='Car Parking',
            labels={'x':'status','y':'No. of houses'})
    graph10 = json.dumps(fig10, cls=plotly.utils.PlotlyJSONEncoder)

    la = df.groupby(df['Lift Available'])['Unnamed: 0'].count()
    fig11 = px.bar(la,x=['No','Yes'],y=la.values,color=['No','Yes'],title='Lift Available',
            labels={'x':'status','y':'No. of houses'})
    graph11 = json.dumps(fig11, cls=plotly.utils.PlotlyJSONEncoder)

    gym = df.groupby(df['Gymnasium'])['Unnamed: 0'].count()
    fig12 = px.bar(gym,x=['No','Yes'],y=gym.values,color=['No','Yes'],title='Gym Availability',
            labels={'x':'status','y':'No. of houses'})
    graph12 = json.dumps(fig12, cls=plotly.utils.PlotlyJSONEncoder)

    nr = df.groupby(df['New/Resale'])['Unnamed: 0'].count()
    fig13 = px.bar(nr,x=['New','Resale'],y=nr.values,color=['New','Resale'],title='New or Resale',
            labels={'x':'status','y':'No. of houses'})
    graph13 = json.dumps(fig13, cls=plotly.utils.PlotlyJSONEncoder)

    bed = df.groupby(df['No. of Bedrooms'])['Unnamed: 0'].count()
    fig14 = px.bar(bed,x=bed.index,y=bed.values,color=bed.index,title='No. of Bedrooms',
            labels={'x':'No. of bedrooms','y':'No. of houses'})
    graph14 = json.dumps(fig14, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('facilities.html',graph1=graph1,graph2=graph2,graph3=graph3,graph4=graph4,
                            graph5=graph5,graph6=graph6,graph7=graph7,graph8=graph8,graph9=graph9,
                            graph10=graph10,graph11=graph11,graph12=graph12,graph13=graph13,graph14=graph14)

@app.route('/price')
def price():
    fig15 = px.scatter(df,x="Area", y="Price", title='Area-size vs Price',color='Area',
            labels={
                'x':'Area',
                'y':'Price'
            })
    graph15 = json.dumps(fig15, cls=plotly.utils.PlotlyJSONEncoder)

    fig16 = px.histogram(df,x="No. of Bedrooms", y="Price",color="No. of Bedrooms",
                            title='Bedrooms vs Price')
    graph16 = json.dumps(fig16, cls=plotly.utils.PlotlyJSONEncoder)

    fig17 = px.scatter(df,x="Location", y="Price",color="Location",
                            title='Location vs Price')
    graph17 = json.dumps(fig17, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('price.html',graph15=graph15,graph16=graph16,graph17=graph17)

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method=="POST":
        form = request.form
        area = int(form.get('area'))
        bed = int(form.get('bed'))
        new = int(form.get('new'))
        gym = int(form.get('gym'))
        lift = int(form.get('lift'))
        car = int(form.get('car'))
        maintain = int(form.get('maintain'))
        sec = int(form.get('sec'))
        club = int(form.get('club'))
        intercom = int(form.get('intercom'))
        garden = int(form.get('garden'))
        games = form.get('games')
        gas = int(form.get('gas'))
        jog = float(form.get('jog'))
        swim = int(form.get('swim'))
        userinp = [[area,bed,new,gym,lift,car,maintain,sec,club,intercom,garden,games,gas,jog,swim]]
        prediction = model.predict(userinp)
        output = round(prediction[0], 2)
        return render_template('predict.html',area=area,bed=bed,new=new,gym=gym,lift=lift,car=car,
                                maintain=maintain,sec=sec,club=club,intercom=intercom,
                                garden=garden,games=games,gas=gas,jog=jog,swim=swim,output=output)
    return render_template('predict.html')
if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 