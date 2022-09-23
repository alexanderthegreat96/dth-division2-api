import json

class ApiConfig:
    def __init__(self):
        f = open('config.json')
        data = json.load(f)
        self.mysql_host = data['database']['host']
        self.mysql_user = data['database']['user']
        self.mysql_pass = data['database']['password']
        self.mysql_db = data['database']['database']
        f.close()

    def mysqlHost(self):
        return self.mysql_host
    def mysqlUser(self):
        return self.mysql_user
    def mysqlPass(self):
        return self.mysql_pass
    def mysqlDb(self):
        return self.mysql_db