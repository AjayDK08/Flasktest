from flask import Flask,render_template,request,redirect,url_for
import sqlite3

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html");


@app.route("/add")
def add():
    return render_template("add.html")


@app.route("/savedetails", methods=["POST", "GET"])
def saveDetails():
    msg = "msg"
    if request.method == "POST":
        try:
            Ambid= request.form["Ambid"]
            Queueid= request.form["Queueid"]
            Amount= request.form["Amount"]
            Taskcount = request.form["Taskcount"]
            State= request.form["State"]
            Reason = request.form["Reason"]

            with sqlite3.connect("queue.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into Queues (Ambid, Queueid, Amount,Taskcount,State,Reason) values (?,?,?,?,?,?)", (Ambid, Queueid, Amount,Taskcount,State,Reason))
                con.commit()
                msg = "Queue successfully Added"
        except:
            con.rollback()
            msg = "Queue can not be added to the list"
        finally:
            return render_template("success.html", msg=msg)
            con.close()


@app.route("/view")
def view():
    con = sqlite3.connect("queue.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from Queues")
    rows = cur.fetchall()
    return render_template("view.html", rows=rows)


@app.route("/delete")
def delete():
    return render_template("delete.html")


@app.route("/delete_record", methods=["POST"])
def deleterecord():
    Queueid = request.form["Queueid"]
    Ambid =request.form["Ambid"]
    with sqlite3.connect("queue.db") as con:
        try:
            cur = con.cursor()
            if Queueid and Ambid:
                cur.execute("delete from Queues where Queueid = ?", (Queueid,))
                cur.execute("delete from Queues where Ambid = ?", (Ambid,))
                msg = "Record deleted successfully"
        except:
            msg = "can't be deleted ids not matching"
        finally:
            return render_template("delete_record.html", msg=msg)


# @app.route("/display/update/<int:uid>", methods=["GET", "POST"])
# def update(Ambid):
#     con = sqlite3.connect("queue.db")
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#     cur.execute("SELECT * from test where id = ?", (Ambid,))
#     get_rows = cur.fetchall()
#
#     if request.method == "POST":
#
#         try:
#             amb = request.form["Ambid"]
#             queue = request.form["Queueid"]
#             amount = request.form["Amount"]
#             task = request.form["Taskcount"]
#             state = request.form["State"]
#             reason = request.form["Reason"]
#
#             with sqlite3.connect("queue.db") as con:
#                 cur = con.cursor()
#                 cur.execute("update test set Ambid=?, Queueid=?,Amount=?,Taskcount=?,State=?,Reason=? where id=?",
#                             (Ambid, Queueid, Amount, Taskcount, State, Reason, uid))
#
#                 con.commit()
#             return redirect(url_for('display'))
#         except TypeError:
#             con.rollback()
#             msg = "Database error"
#
#     return render_template('update.html', data=get_rows)


if __name__ == "__main__":
    app.run(debug=True)