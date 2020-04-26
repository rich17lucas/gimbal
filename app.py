from flask import Flask, render_template, request, json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello' )
def hello():
    return render_template('hello.html')


@app.route('/gimbal')
def try_boot_strap():
    return render_template('gimbalcontrol.html')


@app.route('/postValues')
def post_values():
    print(f"request.args: {request.args}")
    #print(f"request.args.get('left_right'): {request.args.get('left_right')}")
    #print(f"request.args.get('up_down'): {request.args.get('up_down')}")

    left_right = request.args.get('left_right') # if request.args.get('left_right') else None
    up_down = request.args.get('up_down') #if request.args.get('up_down') else None
    click = request.args.get('click')

    print(f"left_right: {left_right}")
    print(f"up_down: {up_down}")
    print(f"click: {click}")

    return json.dumps({'status':'OK'})


if __name__ == '__main__':
    app.run(debug=True,port=1080,host="0.0.0.0")
