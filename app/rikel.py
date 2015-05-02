from app import app
import time
import flask

@app.route('/api/test',methods=['POST','GET'])
def test():
	return flask.jsonify(result={'result':time.time()})