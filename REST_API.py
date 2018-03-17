from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request,jsonify
import secrets
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/harsh/Desktop/Assignment2/REST_DB.db'
db = SQLAlchemy(app)

class wallets(db.Model):
	srNo1 = db.Column(db.Integer,primary_key=True)
	wall_id = db.Column(db.Integer)
	balance = db.Column(db.Integer)
	coin_symbol = db.Column(db.String(50))

class transfer(db.Model):
	srNo2 = db.Column(db.Integer,primary_key=True)
	status = db.Column(db.String(25))
	from_wallet = db.Column(db.Integer)
	to_wallet = db.Column(db.Integer)
	amount = db.Column(db.Integer)
	time_stamp = db.Column(db.String(50))
	txn_hash = db.Column(db.String(50))


@app.route('/wallets/<id_no>', methods = ['GET'])
def walletGET(id_no):
	see_wall = wallets.query.filter_by(wall_id=int(id_no)).first()

	if not see_wall:
		return jsonify({"message" : "Data not available for the ID you have entered"})

	get_wallet = {}
	get_wallet['id'] = see_wall.wall_id
	get_wallet['balance'] = see_wall.balance
	get_wallet['coin_symbol'] = see_wall.coin_symbol

	return jsonify(get_wallet)


@app.route('/wallets', methods = ['POST'])
def walletPOST():
	data_wallet = request.get_json()
	print('wallet :'+ str(data_wallet))
	add_in_wallet = wallets(wall_id = data_wallet['id'], balance = data_wallet['balance'], coin_symbol = data_wallet['coin_symbol'])
	db.session.add(add_in_wallet)
	db.session.commit()

	return jsonify({"message" : "New Wallet Data Saved!"})


@app.route('/wallets/<id_no>', methods = ['DELETE'])
def walletDELETE(id_no):
	del_wallet = wallets.query.filter_by(wall_id=int(id_no)).first()

	if not del_wallet:
		return jsonify({"message" : "Data not available for the ID you have entered"})

	db.session.delete(del_wallet)
	db.session.commit()

	return jsonify({"message" : "Selected Wallet has been successfully deleted!"})


@app.route('/txns', methods = ['POST'])
def txnPOST():
	data_txn = request.get_json()

	check1 = wallets.query.filter_by(wall_id=data_txn['to_wallet']).first()
	check2 = wallets.query.filter_by(wall_id=data_txn['from_wallet']).first()
	if not check1 and not check2:
		return jsonify({"message" : "Entered both entries are not available in Wallet Table!"})

	if not check1 or not check2:
		return jsonify({"message" : "One of the entries is not available in Wallet Table!"})

	add_in_txns = transfer(status = "pending", from_wallet = data_txn['from_wallet'], to_wallet = data_txn['to_wallet'],
		amount = data_txn['amount'], time_stamp = datetime.datetime.now(), txn_hash = secrets.token_hex(nbytes=32))

	db.session.add(add_in_txns)
	db.session.commit()

	return jsonify({"message" : "Transfer Completed!"})


@app.route('/txns/<id_no>', methods = ['GET'])
def txnsGET(id_no):
	see_txns = transfer.query.filter_by(txn_hash=id_no).first()

	if not see_txns:
		return jsonify({"message" : "Data not available for the Transaction Hash you have entered"})

	get_txns = {}
	get_txns['status'] = see_txns.status
	get_txns['from_wallet'] = see_txns.from_wallet
	get_txns['to_wallet'] = see_txns.to_wallet
	get_txns['amount'] = see_txns.amount
	get_txns['time_stamp'] = see_txns.time_stamp
	get_txns['txn_hash'] = see_txns.txn_hash

	return jsonify(get_txns)


if __name__ == '__main__':
    app.run(debug=True)

# Reference : https://www.youtube.com/watch?v=WxGBoY5iNXY
