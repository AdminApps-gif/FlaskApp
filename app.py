from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask (__name__)
app.config.from_object('config.Config')

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM master_file")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', data=data)
    

@app.route('/add', methods=['GET', 'POST'])
def add_company():
    if request.method == 'POST':
        bn = request.form['BN']
        team = request.form['Team']
        company = request.form['Company_Name']
        owner = request.form['Owner_Name']
        ye = request.form['YE']
        gst = request.form['GST']
        bk = request.form['BK']
        status = request.form['Status']
        cur = mysql.connection.cursor()
        cur.execute("""
                    INSERT INTO master_file (BN, Team, Company_Name, Owner_Name, YE, GST, BK, Status)
                    VALUE (%s, %s, %s, %s, %s, %s, %s, %s)
                    """ , (bn, team, company, owner, ye, gst, bk, status))
        mysql.connection.commit()
        cur.close()
        return render_template('success.html')
    return render_template('add.html')

if __name__ == '__main__':
    app.run (debug=True)