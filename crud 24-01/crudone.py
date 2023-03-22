from flask import Flask,render_template,request,url_for,redirect
import sqlite3 as sql

app=Flask(__name__)

@app.route("/")
def home():
    con=sql.connect("user.db")
    con.row_factory=sql.Row
    res=con.cursor()
    res.execute("select * from node")
    dot=res.fetchall()
    con.commit()
    return render_template("home.html",data=dot)

@app.route("/add",methods=["post","get"])
def add():
    if request.form.get("id")!=None:
        id=request.form.get("id")
        name=request.form.get("name")
        course=request.form.get("course")
        con=sql.connect("user.db")
        res=con.cursor()
        res.execute("insert into node(ID,NAME,COURSE)values(?,?,?)",(int(id),name,course))
        con.commit()
    return render_template("add.html")

@app.route("/update/<id>",methods=["post","get"])
def edit(id):
    if request.form.get("id")!=None:
        id=request.form.get("id")
        name=request.form.get("name")
        course=request.form.get("course")
        con=sql.connect("user.db") 
        res=con.cursor()
        res.execute("update node set name=?, course=? where id=?",(name,course,int(id)))  
        con.commit()
        return render_template("home.html")
    con=sql.connect("user.db")
    con.row_factory=sql.Row
    res=con.cursor()
    res.execute("select * from node where ID=?",(int(id),))
    a=res.fetchone()
    print(a)
    return render_template("edit.html",data=a)

@app.route("/delete/<id>", methods=["post","get"])
def deletedata(id):
    con=sql.connect("user.db")
    con.row_factory=sql.Row
    res=con.cursor()
    res.execute("delete from node where id=?",(int(id)))
    con.commit()
    return "DELETE SUCESSFULLY"


if __name__=="__main__":
    app.run(debug=True)
