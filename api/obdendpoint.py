from flask_restful import Resource, reqparse
import obd

class connect(Resource):
    def get(self):
        connection = obd.OBD()
        if (connection.status() == OBDStatus.CAR_CONNECTED):
            return {'msg': 'connected'}, 200
        else:
            return {'error': 'Error connecting to OBD'}, 500

class status(Resource):
    def get(self):
        return {'OBDStatus': obd.OBDStatus}
        
