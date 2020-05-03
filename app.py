from flask import Flask, render_template, request, json
import logging
import socket
if "RPI" in socket.gethostname().upper():
    from libs.servocontrol import servocontroller as sc


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
 
    left_right = request.args.get('left_right') # if request.args.get('left_right') else None
    up_down = request.args.get('up_down') #if request.args.get('up_down') else None
    click = request.args.get('click')

    logging.info(f"left_right: {left_right}")
    logging.info(f"up_down: {up_down}")
    logging.info(f"click: {click}")

    servo_positions = {'left_right':left_right,
                       'up_down':up_down, 
                       'click':click
                       }
    
    logging.info(servo_positions)

    #try:
    sc.set_servo(servo_positions)
    #except Exception as error:
    #    logging.ERROR(error.args())


    return json.dumps({'status':'OK'})


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', filename='app.log')
    logger = logging.getLogger(__name__)
    app.run(debug=True,port=1080,host="0.0.0.0")
