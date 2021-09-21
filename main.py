import logging

from flask import jsonify, render_template

from app import create_app

log = logging.getLogger('app_logs')

application = create_app()

@application.route("/")
def index_information():
    return render_template('documentation.html')

@application.errorhandler(404)
def page_not_found(error):
    response = jsonify({"message": "ATENTION: System does not recognize this request."})
    log.debug(error)
    return response, 404

   
if __name__ == "__main__":  
    import logging
    logging.basicConfig(filename='log.log',level=logging.DEBUG)
    application.run(debug=True)

