# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 13:03:01 2016

@author: jesusluque
"""
    
from flask import Flask,render_template,request,redirect
app_mp = Flask(__name__)

#app_mp.vars={}
#
#app_mp.questions={}
#app_mp.questions['How many eyes do you have?']=('1','2','3')
#app_mp.questions['Which fruit do you like best?']=('banana','mango','pineapple')
#app_mp.questions['Do you like cupcakes?']=('yes','no','maybe')
#
#app_mp.nquestions=len(app_mp.questions)
## should be 3

@app_mp.route('/index_mp',methods=['GET','POST'])
def index_mp():
#    nquestions=app_mp.nquestions
    curve = "Twitter Inc (TWTR) Prices, Dividends, Splits and Trading Volume"
    
    if request.method == 'GET':
#        return render_template('userinfo_mp.html',num=nquestions)
        return render_template('userinfo_mp.html', curv1=curve)
    else:
        # request was a POST
#        app_mp.vars['name'] = request.form['name_mp']
#        app_mp.vars['age'] = request.form['age_mp']
#
#        f = open('%s_%s.txt'%(app_mp.vars['name'],app_mp.vars['age']),'w')
#        f.write('Name: %s\n'%(app_mp.vars['name']))
#        f.write('Age: %s\n\n'%(app_mp.vars['age']))
#        f.close()

        temp1=request.form['answer']
#        temp2=request.form['answer2']
#        temp3=request.form['answer3']
        f = open('prueba.txt','w')
#        f.write('%s %s %s\n'%(temp1, temp2, temp3))
        f.write('%s %s %s\n'%(type(temp1), len(temp1), temp1))
        f.close()
        
        
        import pandas as pd
        from bokeh.plotting import figure, output_file, save
        import requests
        
        r=requests.get('https://www.quandl.com/api/v3/datasets/WIKI/TWTR.json?api_key=yNFoy4S_sDhN3-k-SUNL', 
                       auth=('jesushluque', 'TDIreplydata2017'))
        my_info = r.json()
        my_data=pd.DataFrame(my_info['dataset']['data'][:][:])
        
        column_names = my_info['dataset']['column_names']
        my_data.columns = column_names
        my_data=my_data.set_index('Date')
        
        output_file("templates/lines.html")
        
        # create a new plot with a title and axis labels
        p = figure(title="Title", x_axis_label='x', y_axis_label='y')
        
        # add a line renderer with legend and line thickness
#        for i in range(1,4):
        #    p.line(my_data.index, my_data[column_names[i+1]])#, legend=column_names[i])
#            p.line(range(len(my_data)), my_data[column_names[i+1]], legend=column_names[i+1])
        p.line(range(len(my_data)), my_data[column_names[int(temp1)]], legend=column_names[int(temp1)])        
        # show the results
        save(p)

        return redirect('/main_mp')

@app_mp.route('/main_mp')
def main_mp2():
#    if len(app_mp.questions)==0 : return render_template('lines.html')
#    return redirect('/next_mp')
    return render_template('lines.html')

#####################################
## IMPORTANT: I have separated /next_mp INTO GET AND POST
## You can also do this in one function, with If and Else
## The attribute that contains GET and POST is: request.method
#####################################

#@app_mp.route('/next_mp',methods=['GET'])
#def next_mp(): #remember the function name does not need to match the URL
#    # for clarity (temp variables)
#    n = app_mp.nquestions - len(app_mp.questions) + 1
#    q = app_mp.questions.keys()[0] #python indexes at 0
#    a1, a2, a3 = app_mp.questions.values()[0] #this will return the answers corresponding to q
#
#    # save the current question key
#    app_mp.currentq = q
#
#    return render_template('layout_mp.html',num=n,question=q,ans1=a1,ans2=a2,ans3=a3)
#
#@app_mp.route('/next_mp',methods=['POST'])
#def next_mp2():  #can't have two functions with the same name
#    # Here, we will collect data from the user.
#    # Then, we return to the main function, so it can tell us whether to
#    # display another question page, or to show the end page.
#
#    f = open('%s_%s.txt'%(app_mp.vars['name'],app_mp.vars['age']),'a') #a is for append
#    f.write('%s\n'%(app_mp.currentq))
#    f.write('%s\n\n'%(request.form['answer_from_layout_mp'])) #this was the 'name' on layout.html!
#    f.close()
#
#    # Remove question from dictionary
#    del app_mp.questions[app_mp.currentq]
#
#    return redirect('/main_mp')

if __name__ == "__main__":
    app_mp.run(debug=True)