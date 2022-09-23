from classes.DatabaseWrapper import DatabaseWrapper

class AuthenticateRequest:

    def authenticate(self, apikey):
        db = DatabaseWrapper()

        db.cursor.execute('SELECT id FROM users WHERE api_key = "'+apikey+'" LIMIT 1')
        result = db.cursor.fetchone()

        if(result):
            return 'authenticated'
        else:
            return 'not_authenticated'