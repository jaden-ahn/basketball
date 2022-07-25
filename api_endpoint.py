from flask import Flask,jsonify



app=Flask(__name__)
message={"message":"hello world"}



@app.route("/")
def index():
    return "Welcome to our API"



@app.route("/predict/<int:freethrows>/<int:twopointer>/<int:threepointer>/<int:missedfreethrows>/<int:missedtwos>/<int:missedthrees>",methods=["GET"])
def predict(freethrows,twopointer,threepointer,missedfreethrows,missedtwos,missedthrees):
    arr=[freethrows,twopointer,threepointer,missedfreethrows,missedtwos,missedthrees]
    if (freethrows)/(missedfreethrows + freethrows) > 0.5 and twopointer/(missedtwos + twopointer) > 0.5 and threepointer/(missedthrees + threepointer) > 0.5:
        return jsonify({"result":True})
    else:
        return jsonify({"result":False})





if __name__ == "__main__":
    app.run(debug=True)
