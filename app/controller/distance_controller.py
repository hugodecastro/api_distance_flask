from app.model.distance_model import Distance
from flask import jsonify, render_template


def doc():
    f1 = "<pre>" + index.__doc__ + "</pre>"

    html = """
        <h3>Request: INDEX GEOLOCATOR</h3>{}
    """.format(f1)
    return html

def index(destination):
    """     
    Link: http://.../distance/g/&lt;<i>destination</i>&gt;

    <b>Method</b>: GET 
    
    <b>Description</b>:
        Returns the difference between the entered location and Moscow Ring Road. If the location is within the MKAD, the distance will not be calculated.

    <b>Data request</b>:
        The expected format is a json that contains the "destination" field. 
        request = {
            "destination": "string"
        }
        <b>NOTE:</b> &lt;<i>destination</i>&gt; is a string.
        
    <b>Returns</b>: JSON
        point_one = {
            "lat": float,
            "long": float
        }
        point_two = {
            "lat": float,
            "long": float
        }

        200: SUCCES (HTTP_200_OK).
        500: INTERNAL ERROR (HTTP_500_INTERNAL_SERVER_ERROR).  
    """
    try:
        int(destination) # prevent numeric input
    except Exception:
        if 'Moscow' in destination:
            # when point_two=None then map will display initial configuration
            return render_template("distance.html", result=0, point_two=None), 200

        distance = Distance.get_destination(dest=destination)

        if len(distance) == 2:
            # given destination is within MKAD range
            return render_template("distance.html", result=0, point_two=None), 200
            

        return render_template("distance.html",
                                result=distance[0],
                                point_one=distance[1],
                                point_two=distance[2]), 200
                                
    return render_template("distance.html", result="Invalid input.",
                                            point_two=None), 500

    
