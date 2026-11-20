from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3, os
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app=Flask(__name__)
app.secret_key="cinebook-demo-secret"
DB=os.path.join(os.path.dirname(__file__),"movie_booking.db")

MOVIES=[
{"id":1,"title":"Jailer 2","language":"Tamil","genre":"Action","rating":8.2,"duration":"2h 45m","emoji":"🔥"},
{"id":2,"title":"Jana Nayagan","language":"Tamil","genre":"Action","rating":8.0,"duration":"2h 35m","emoji":"⭐"},
{"id":3,"title":"Vinnaithaandi Varuvaayaa","language":"Tamil","genre":"Romance","rating":8.5,"duration":"2h 37m","emoji":"💖"},
{"id":4,"title":"Meesaya Murukku","language":"Tamil","genre":"Comedy","rating":7.5,"duration":"2h 25m","emoji":"🎵"},
{"id":5,"title":"Mookuthi Amman 2","language":"Tamil","genre":"Comedy","rating":7.8,"duration":"2h 20m","emoji":"✨"},
{"id":6,"title":"Premalu","language":"Malayalam","genre":"Romance","rating":8.0,"duration":"2h 36m","emoji":"💕"},
{"id":7,"title":"Pushpa 2","language":"Telugu","genre":"Action","rating":8.1,"duration":"3h 15m","emoji":"🌿"},
{"id":8,"title":"The Avengers","language":"English","genre":"Action","rating":8.0,"duration":"2h 23m","emoji":"🦸"},
{"id":9,"title":"Spider-Man: No Way Home","language":"English","genre":"Action","rating":8.3,"duration":"2h 28m","emoji":"🕷️"},
{"id":10,"title":"Interstellar","language":"English","genre":"Sci-Fi","rating":8.7,"duration":"2h 49m","emoji":"🚀"},
{"id":11,"title":"Inception","language":"English","genre":"Sci-Fi","rating":8.6,"duration":"2h 28m","emoji":"🌀"},
{"id":12,"title":"The Dark Knight","language":"English","genre":"Action","rating":9.0,"duration":"2h 32m","emoji":"🦇"},
{"id":13,"title":"Inside Out 2","language":"English","genre":"Animation","rating":8.0,"duration":"1h 40m","emoji":"🌈"},
{"id":14,"title":"Mufasa: The Lion King","language":"English","genre":"Adventure","rating":7.8,"duration":"1h 58m","emoji":"🦁"},
{"id":15,"title":"Lilo & Stitch","language":"English","genre":"Family","rating":7.9,"duration":"1h 48m","emoji":"🌺"},
{"id":16,"title":"The Odyssey","language":"English","genre":"Adventure","rating":8.1,"duration":"2h 40m","emoji":"⚔️"}]
CINEMAS=["PVR Cinemas - Madurai","INOX - Madurai","Vetri Cinemas - Madurai","Cinepolis - Chennai","PVR Cinemas - Chennai"]
SHOW_TIMES=["10:00 AM","1:30 PM","4:30 PM","7:30 PM","10:00 PM"]

def db():
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; return c
def init_db():
    c=db()
    c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,email TEXT UNIQUE NOT NULL,password TEXT NOT NULL,preferred_language TEXT DEFAULT 'Tamil')")
    c.execute("CREATE TABLE IF NOT EXISTS bookings(id INTEGER PRIMARY KEY AUTOINCREMENT,user_id INTEGER,movie_id INTEGER,movie_title TEXT,cinema TEXT,show_time TEXT,seats TEXT,total REAL,payment_method TEXT,booked_at TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS reviews(id INTEGER PRIMARY KEY AUTOINCREMENT,user_id INTEGER,movie_id INTEGER,rating INTEGER,comment TEXT,created_at TEXT)")
    c.commit(); c.close()
def movie(mid): return next((m for m in MOVIES if m["id"]==mid),None)
def recs():
    lang="Tamil"
    if session.get("user_id"):
        c=db(); u=c.execute("SELECT preferred_language FROM users WHERE id=?",(session["user_id"],)).fetchone()
        liked=c.execute("SELECT movie_id FROM reviews WHERE user_id=? AND rating>=4 ORDER BY id DESC LIMIT 5",(session["user_id"],)).fetchall(); c.close()
        if u: lang=u["preferred_language"]
        genres=[movie(x["movie_id"])["genre"] for x in liked if movie(x["movie_id"])]
        if genres:
            r=[m for m in MOVIES if m["language"]==lang and m["genre"] in genres]
            if r:return r[:6]
    return [m for m in MOVIES if m["language"]==lang][:6]

@app.context_processor
def globals(): return {"current_user":session.get("user_name")}
@app.route("/")
def home(): return render_template("index.html",recommendations=recs(),featured=sorted(MOVIES,key=lambda x:x["rating"],reverse=True)[:6])
@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=="POST":
        n=request.form.get("name","").strip(); e=request.form.get("email","").strip().lower(); p=request.form.get("password",""); l=request.form.get("preferred_language","Tamil")
        if not n or not e or len(p)<6: flash("Enter all details. Password must be at least 6 characters.","error"); return render_template("register.html")
        c=db()
        try:
            c.execute("INSERT INTO users(name,email,password,preferred_language) VALUES(?,?,?,?)",(n,e,generate_password_hash(p),l)); c.commit(); flash("Registration successful. Please login.","success"); return redirect(url_for("login"))
        except sqlite3.IntegrityError: flash("Email already registered.","error")
        finally:c.close()
    return render_template("register.html")
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        e=request.form.get("email","").strip().lower(); p=request.form.get("password",""); c=db(); u=c.execute("SELECT * FROM users WHERE email=?",(e,)).fetchone(); c.close()
        if u and check_password_hash(u["password"],p): session["user_id"]=u["id"]; session["user_name"]=u["name"]; flash("Welcome back!","success"); return redirect(url_for("home"))
        flash("Invalid email or password.","error")
    return render_template("login.html")
@app.route("/logout")
def logout(): session.clear(); flash("Logged out successfully.","success"); return redirect(url_for("home"))
@app.route("/movies")
def movies():
    q=request.args.get("q","").lower().strip(); l=request.args.get("language","All"); g=request.args.get("genre","All"); r=MOVIES
    if q:r=[m for m in r if q in m["title"].lower() or q in m["language"].lower()]
    if l!="All":r=[m for m in r if m["language"]==l]
    if g!="All":r=[m for m in r if m["genre"]==g]
    return render_template("movies.html",movies=r,languages=sorted(set(m["language"] for m in MOVIES)),genres=sorted(set(m["genre"] for m in MOVIES)),selected_language=l,selected_genre=g,q=q)
@app.route("/book/<int:mid>",methods=["GET","POST"])
def book(mid):
    if not session.get("user_id"): flash("Please login before booking.","error"); return redirect(url_for("login"))
    m=movie(mid)
    if request.method=="POST":
        seats=request.form.getlist("seats"); cinema=request.form.get("cinema"); time=request.form.get("show_time")
        if not seats or len(seats)>8 or cinema not in CINEMAS or time not in SHOW_TIMES: flash("Select valid cinema, time and 1-8 seats.","error"); return redirect(url_for("book",mid=mid))
        session["cart"]={"movie_id":mid,"movie_title":m["title"],"cinema":cinema,"show_time":time,"seats":seats,"total":len(seats)*180}; return redirect(url_for("checkout"))
    return render_template("book.html",movie=m,cinemas=CINEMAS,show_times=SHOW_TIMES)
@app.route("/checkout",methods=["GET","POST"])
def checkout():
    cart=session.get("cart")
    if not session.get("user_id"): return redirect(url_for("login"))
    if not cart: return redirect(url_for("movies"))
    if request.method=="POST":
        method=request.form.get("payment_method")
        if method not in ["UPI","Card","Net Banking"]: flash("Choose a valid payment method.","error"); return render_template("checkout.html",cart=cart)
        c=db(); cur=c.execute("INSERT INTO bookings(user_id,movie_id,movie_title,cinema,show_time,seats,total,payment_method,booked_at) VALUES(?,?,?,?,?,?,?,?,?)",(session["user_id"],cart["movie_id"],cart["movie_title"],cart["cinema"],cart["show_time"],", ".join(cart["seats"]),cart["total"],method,datetime.now().strftime("%Y-%m-%d %H:%M"))); bid=cur.lastrowid; c.commit(); c.close(); session.pop("cart"); return redirect(url_for("ticket",bid=bid))
    return render_template("checkout.html",cart=cart)
@app.route("/ticket/<int:bid>")
def ticket(bid):
    c=db(); b=c.execute("SELECT * FROM bookings WHERE id=? AND user_id=?",(bid,session.get("user_id"))).fetchone(); c.close()
    if not b:return redirect(url_for("history"))
    return render_template("ticket.html",booking=b)
@app.route("/history")
def history():
    if not session.get("user_id"):return redirect(url_for("login"))
    c=db(); b=c.execute("SELECT * FROM bookings WHERE user_id=? ORDER BY id DESC",(session["user_id"],)).fetchall(); c.close(); return render_template("history.html",bookings=b)
@app.route("/reviews",methods=["GET","POST"])
def reviews():
    if not session.get("user_id"):return redirect(url_for("login"))
    if request.method=="POST":
        c=db(); c.execute("INSERT INTO reviews(user_id,movie_id,rating,comment,created_at) VALUES(?,?,?,?,?)",(session["user_id"],int(request.form["movie_id"]),int(request.form["rating"]),request.form.get("comment",""),datetime.now().strftime("%Y-%m-%d %H:%M"))); c.commit(); c.close(); flash("Review saved. Your recommendations are updated.","success")
    c=db(); r=c.execute("SELECT * FROM reviews WHERE user_id=? ORDER BY id DESC",(session["user_id"],)).fetchall(); c.close(); return render_template("reviews.html",movies=MOVIES,reviews=r)
@app.route("/recommendations")
def recommendations(): return render_template("recommendations.html",recommendations=recs())
if __name__=="__main__": init_db(); app.run(debug=True)
