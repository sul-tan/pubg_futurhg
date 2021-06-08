from flask import Flask , render_template
app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")
@app.route('/fee', methods=["POST"])   
def fee():
    return render_template("fee.html") 
@app.route('/details',methods=["post"])  
def details():
    return render_template("form.html")  
if __name__ == "__main__":
    main()
