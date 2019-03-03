from flask import Flask,request,render_template
import MySQLdb
app = Flask(__name__)
def connection():
    hostname = "localhost"
    username = "adithya"
    password = "Adithya98"
    database = "BucketList"

    return MySQLdb.connect(host = hostname, user = username, passwd = password, db = database)

@app.route('/')
def get_data():
 return render_template("signup.html")

@app.route('/update',methods=['GET','POST'])
def update_data():
 if request.method=='POST':
    nm=request.form['nname']
    ph=request.form['number']
    em=request.form['email']
    pw=request.form['pass']
    
    conn = connection()
    cursor = conn.cursor()
    sql_query="INSERT INTO names_tbl VALUES ('{a}','{b}','{c}','{d}');".format(a=nm,b=ph,c=em,d=pw)
    try:
        cursor.execute(sql_query)
        conn.commit()
        return "inserted"
    except Exception as e:
        print(e)
        return e
          
        
    conn.close()    
    

if __name__ == '__main__':
    app.run(debug=True)
