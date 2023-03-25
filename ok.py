print("ok")
import yaml

@app.route('/', methods=['GET'])
  def index():
  user = request.cookies.get('username')
  # Insecure example
  return "Hey there, {}!".format(yaml.unsafe_load(user))

import subprocess
# ...
@app.route("secure-command-execution-arg")
def a():
  arg = flask.request.args.get("arg")
  # Secure example for passing and argument to a command
  subprocess.run(["ping", "-c1", arg])
# ...
@app.route("secure-command-execution-cmd")
def b():
  cmd = flask.request.args.get("cmd")
  arg = flask.request.args.get("arg")
  allowed = {'p': "ping", 'l': "ls"}
