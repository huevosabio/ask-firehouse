from app import app
import time
from flask import Flask, request, jsonify
import flask

@app.route('/api/test',methods=['POST','GET'])
def test():
	return flask.jsonify(result={'result':time.time()})




@app.route('/echo',methods=['POST','GET'])
def respond():
	req = request.json
	response = {"version": "1.0",
	"response": {
    "outputSpeech": {
      "type": "string",
      "text": "Well, people that suck, suck"
    },
    "card": {
      "type": "string",
      "title": "Rikel Says",
      "subtitle": "string",
      "content": "Well, people that suck, suck"
    },
    "shouldEndSession": False}}

	if req['request']['type'] == 'LaunchRequest':
		response['text'] = 'Ahm, yes? How may I help you?'
	elif req['request']['type'] == 'IntentRequest':
		response['text'] = "Well, people that suck, suck"
	elif req['request']['type'] == 'SessionEndedRequest':
		response['text'] = 'Ok, that was $20.'
		response['shouldEndSession'] = True
	else:
		pass

	return flask.jsonify(response)