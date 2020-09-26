import random
from flask import jsonify
from flask import Flask
from flask import request
from flask import abort
# from flask_restful import Api, Resource, reqparse
# from make_requests import *
from flask_cors import CORS
from vaccine_blueprint import vaccine_blueprint
import login
import logout
import register
import patient_home
# import hospital_home


from db_module import db_main
# import db_module

db_main.init_db()
db_main.print_metadata()



app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.secret_key = str.encode('_5#y2L"F4Q8z\n\xec]/' + str(random.random))
app.register_blueprint(vaccine_blueprint)
# parser = reqparse.RequestParser()

@app.route("/")
def hello():
    return jsonify("<h1>Hello Worldnnnnn!</h1>")


@app.route('/train_list', methods=['POST'])
def flask_train_list():
    imp_tags = ["origin", "dest", "day", "month", "year"]

    if not request.json:
        abort(400)
    for key in imp_tags:
        if key not in request.json.keys():
            abort(400)
    # trains_list = get_trains(request.json["origin"], request.json["dest"], request.json["day"], request.json["month"], request.json["year"])

    # return jsonify({'trains_list': trains_list}), 201

@app.route('/getapplications', methods=['GET'])
def getapplications():
    data = {}
    data["id"] = 1
    data["companyName"]="Google";
    data["role"]="Software Engineer";
    data["location"]="NY";
    data["a_status"]="DECLINED";

    return jsonify(data), 200
@app.route('/station_list', methods=['GET'])
def flask_station_list():
    stations_list = get_station_names()

    return jsonify({'stations_list': stations_list}), 201

@app.route('/station_location', methods=['POST'])
def flask_station_location():
    imp_tags = ["station"]

    if not request.json:
        abort(400)
    for key in imp_tags:
        if key not in request.json.keys():
            abort(400)
    # station_location = get_station_location(request.json["station"])

    # return jsonify({'station_location': station_location}), 201

@app.route('/train_density', methods=['POST'])
def flask_train_density():
    imp_tags = ["DateAsString","Destination","Origin","OriginTime","TrainName","TrainNameConn1","TrainNameConn2"]

    if not request.json:
        abort(400)
    for key in imp_tags:
        if key not in request.json.keys():
            abort(400)
    # train_density = get_train_density(request.json)

    return jsonify({'train_density': train_density}), 201

@app.route('/train_station_density', methods=['POST'])
def flask_train_station_density():
    imp_tags = ["DateAsString","Destination","Origin","OriginTime","TrainName","TrainNameConn1","TrainNameConn2"]

    if not request.json:
        abort(400)
    for key in imp_tags:
        if key not in request.json.keys():
            abort(400)
    # train_density = get_train_station_density(request.json)

    # return jsonify({'train_station_density': train_density}), 201


if __name__== "__main__":


    # print(get_trains_arriveby("1", "33", "17", "07", "2020", time="0000"))

    # print(get_trains("GREYSTONE", "GREENWICH", "17", "07", "2020"))

    app.run(debug=True)
    aa=1