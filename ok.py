print("ok")
import yaml

@app.route('/', methods=['GET'])
  def index():
  user = request.cookies.get('username')
  # Insecure example
  return "Hey there, {}!".format(yaml.unsafe_load(user))
