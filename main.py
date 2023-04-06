import flask, aiohttp, urllib, urllib3, subprocess
from flask import Flask, request
from ai import GetResponse

s = Flask('important-server')

@s.route('/ai')
def ai():
  return flask.render_template('ai.html')

@s.route('/terminal')
def terminal():
  return flask.render_template('terminal.html')

@s.route('/get-response/ai')
def get_response_ai():
  #lastKeywords = request.headers.get('lastkwords')
  q = request.headers.get('question')
  response = GetResponse(str(q))
  return response

@s.route('/get-response/terminal')
def get_response_terminal():
  result = subprocess.run(request.headers["cmd"], stdout=subprocess.PIPE, shell=True)
  return result.stdout

s.run(host="0.0.0.0", port=8008, debug=True)