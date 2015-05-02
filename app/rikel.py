from app import app

@app.route('/api/test',methods=['POST','GET'])
def test():
	return flask.jsonify(result={'result':time.time()})