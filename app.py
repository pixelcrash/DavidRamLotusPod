from flask import Flask, render_template
import subprocess
import os
import signal

app = Flask(__name__)

running_process = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update', methods=['POST'])  # Use POST for security reasons
def update_application():
    result = subprocess.run(['./update_script.sh'], capture_output=True, text=True)
    if result.returncode == 0:
        return {"success": True, "message": "Update initiated"}, 202
    else:
        return {"success": False, "message": "Update failed"}, 500


@app.route('/task/<taskname>', methods=['POST'])
def runtask(taskname):
    global running_process

    if running_process is not None:
        try:
            # Terminate the running process
            os.kill(running_process.pid, signal.SIGTERM)
        except Exception as e:
            # Handle errors if the process could not be terminated
            print(f"Error terminating process: {e}")
        finally:
            running_process = None

    # Replace 'your_script.py' with the path to your Python script
    process = subprocess.Popen(['python', f'{taskname}.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    running_process = process
    return "runtask"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
    