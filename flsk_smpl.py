import datetime
import createFigure_last as cf
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    #f= open(r"/home/glowbyte/ulitin_temp/file_for_test","w+")
    #f.write(str(datetime.datetime.now()))
    #f.close()
    #cf.plotMain()

    return "Test connection to web-service successfull!"

@app.route('/plots')
def buildPlot():
    cf.plotMain()	
    return 'Plots created'

@app.errorhandler(Exception)
def server_error(err):
    app.logger.error(f"App error: {err}")
    return "Forbidden", 403

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4567)
