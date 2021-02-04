from flask import Flask, render_template, request
import pickle


app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return render_template("index.html")

@app.route('/predict', methods = ['GET', 'POST'])
def result():
    if request.method == "POST":
        pos_dict = {'F': 0, 'G': 1, 'PF': 2, 'PG': 3, 'SF': 4, 'SG': 5}
        age = float(request.form['age'])
        G = float(request.form['g'])
        GS = float(request.form['gs'])
        MP = float(request.form['mp'])
        FG = float(request.form['fg'])
        FGA = float(request.form['fga'])
        X3P = float(request.form['x3p'])
        X3PA = float(request.form['x3pa'])
        X2P = float(request.form['x2p'])
        X2PA = float(request.form['x2pa'])
        FT = float(request.form['ft'])
        FTA = float(request.form['fta'])
        ORB = float(request.form['orb'])
        DRB = float(request.form['drb'])
        REB = ORB + DRB
        AST = float(request.form['ast'])
        STL = float(request.form['stl'])
        BLK = float(request.form['blk'])
        TOV = float(request.form['tov'])
        PF = float(request.form['pf'])
        pos = request.form['pos']

        pos_list = [0, 0, 0, 0, 0, 0]

        if pos == 'C':
            p0, p1, p2, p3, p4, p5 = pos_list
        else:
            pos_list[pos_dict[pos]] = 1
            p0, p1, p2, p3, p4, p5 = pos_list

        model = pickle.load(open('final_knn_model_v1.pkl', 'rb'))
        scale = pickle.load(open('final_knn_scale.pkl', 'rb'))

        predicted = model.predict(scale.transform([[age, G, GS, MP, FG, FGA, X3P, X3PA, X2P, X2PA, FT,
                                                   FTA, REB, AST, STL, BLK, TOV, PF, p0, p1, p2, p3, p4, p5]]))[0]

        print(predicted)
        return render_template("result.html", prediction=round(predicted))


if __name__ == '__main__':
    app.run(debug=True)