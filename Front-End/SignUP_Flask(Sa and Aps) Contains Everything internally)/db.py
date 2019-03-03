from flask import Flask,request,render_template
import MySQLdb
app = Flask(__name__, template_folder='templates')
def connection():
    hostname = "localhost"
    username = "adithya"
    password = "Adithya98"
    database = "BucketList"

    return MySQLdb.connect(host = hostname, user = username, passwd = password, db = database)

@app.route('/')
def get_data():
 return render_template("login.html")

@app.route('/update',methods=['GET','POST'])
def login():
	pno = request.form['number']
	pas = request.form['pass']
	
	conn = connection()
	cursor = conn.cursor()

	sql_query = " SELECT pno FROM signup WHERE pno=\"{U}\" AND pwd=\"{P}\"; ".format(U=pno, P=pas)

	try:
		cursor.execute(sql_query)
		conn.close()
		return "logged in"
		
	except:

		conn.close()

	for pno in cursor.fetchall():
		if pno[0] == pno:			
			return True

	return False
# conn.close()    
    

if __name__ == '__main__':
    app.run(debug=True)
