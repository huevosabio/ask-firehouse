from app import app
import time
from flask import Flask, request, jsonify, Response
import flask

@app.route('/api/test',methods=['POST','GET'])
def test():
	return flask.jsonify(result={'result':time.time()})




@app.route('/echo',methods=['POST','GET'])
def respond():
	req = request.json
	print req
	response = {"version": "1.0",
	"sessionAttributes": {
    	"supportedHoriscopePeriods": {
    	"daily": True,
    	"weekly": False,
    	"monthly": False}},
	"response": {
    "outputSpeech": {
      "type": "PlainText",
      "text": "Well, people that suck, suck"
    },
    "card": {
      "type": "PlainText",
      "title": "Rikel Says",
      "subtitle": "PlainText",
      "content": "Well, people that suck, suck"
    },"shouldEndSession": False}}

	if req['request']['type'] == 'LaunchRequest':
		response['response']['outputSpeech']['text'] = 'Ahm, yes? How may I help you?'
	elif req['request']['type'] == 'IntentRequest':
		response['response']['outputSpeech']['text'] = "Well, people that suck, suck"
	elif req['request']['type'] == 'SessionEndedRequest':
		response['response']['outputSpeech']['text'] = 'Ok, that was $20.'
		response['shouldEndSession'] = True
	else:
		pass

	js = flask.jsonify(response)
	js.headers['Content-Type'] = 'application/json;charset=UTF-8'
	print type(js.headers)
	print js.headers

	return js