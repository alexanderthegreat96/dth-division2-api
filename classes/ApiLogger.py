from classes.DatabaseWrapper import DatabaseWrapper

class ApiLogger:
    def logData(self, api_key,endpoint,method,result):
        db = DatabaseWrapper()
        query = 'INSERT into logs (`api_key`,`endpoint`,`method`,`result`,`created_at`,`updated_at`) VALUES (%s,%s,%s,%s,%s,%s)'
        queryVals = (api_key,endpoint,method,result,db.now,db.now)
        db.cursor.execute(query,queryVals)
        db.connection.commit()
        db.connection.close()