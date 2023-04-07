from flask import Flask,render_template,request;
import pymysql;
import json
db = pymysql.connect("127.0.0.1", "root", "root", "baldb")
app=Flask(__name__);
name="Swarnali"
@app.route('/')
def bal_delivery_automation():
    return render_template("bal_delivery_automation.html")
@app.route('/bal_delivery_window.html')
def bal_delivery_window():
        return render_template("bal_delivery_window.html")
@app.route('/showtab',methods = ['POST', 'GET'])
def showtable():
    if request.method=='POST':
         rl = request.form['Release']
         sp = request.form['Sprint']
         res = request.form['opt1']
         cursor = db.cursor()
        #sql = "select concat('[',GROUP_CONCAT(JSON_OBJECT('Resource Name', Resource_Name,'Story Ref', Story_Ref,'Area', Area)SEPARATOR ','),']')from bal_resource_task;"
        #sql="SELECT concat("{",CONCAT('"Resource Name":'   , '"', Resource_Name   , '"', ',' '"Story Ref":', '"', Story_Ref, '"', ',''"Area":'  , Area),"}")"FROM bal_resource_task;"

         sql="select * from bal_resource_task where Resource_Name = %s and Rel=%s and Sprint=%s"
         adr = (res,rl,sp)
         cursor.execute(sql,adr)
         rows = cursor.fetchall()
         print (json.dumps(rows,indent=4))
    return render_template("showtable.html",rows = rows)





if __name__=="__main__" :
    app.run(debug=True);
