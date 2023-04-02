from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__,template_folder = 'template')

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/submit',methods = ['POST'])
def submit():
  
    rollno = request.form.get('rollno')
    name = request.form.get('name')
    email = request.form.get('email')
    
    # Connect to the PostgreSQL database on another computer
    conn = psycopg2.connect(
        database="test",
        user="postgres",
        password="kali",
        host="192.168.56.103",
        port="5432"
    )
    cur = conn.cursor()
    
    # Insert the student details into the PostgreSQL database
    cur.execute(
        "INSERT INTO data (rollno, name, email) VALUES (%s, %s, %s)",
        (rollno, name, email)
    )
    conn.commit()
    conn.close()
    
    return "Student details added successfully"

@app.route('/find',methods=['POST'])
def find():
    rollno = request.form.get('rollno')
    
    conn = psycopg2.connect(dbname = "test",user = "postgres",password = "kali",host = "192.168.56.103",port = "5432")
    cur = conn.cursor()

    cur.execute("select * from data where rollno = '{}'".format(rollno))
    result = cur.fetchall()
    conn.commit()
    conn.close()
    return result

if __name__ == '__main__':
    #ip address of VM1 is 192.168.56.102
    app.run(host="192.168.56.102",port=5000,debug=True)
