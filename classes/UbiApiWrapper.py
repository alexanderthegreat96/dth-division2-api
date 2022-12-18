import requests
import json
from base64 import b64encode
from requests.auth import HTTPBasicAuth
from requests.structures import CaseInsensitiveDict
import datetime
from datetime import datetime as dt
from pathlib import Path

class UbiApiWrapper:
    def __init__(self):
        f = open('../config.json')
        data = json.load(f)

        self.username = data['dummy-account']['username']
        self.password = data['dummy-account']['password']
        self.ubiappid = data['app-id']
        self.sessionid = data['session-id']
        self.user_agent = data['user-agent']

        userpass = self.username + ':' + self.password
        self.encoded_u = b64encode(userpass.encode()).decode()



    def login(self):
        headers = CaseInsensitiveDict()
        headers['Content-Type'] = "application/json; charset=utf-8"
        headers['Ubi-AppId'] = self.ubiappid
        headers['Ubi-RequestedPlatformType'] = 'uplay'
        headers['X-Requested-With'] = 'XMLHttpRequest'
        headers['Referer'] = 'https://connect.ubisoft.com'
        headers['Origin'] = 'https://connect.ubisoft.com'
        headers['Accept-Language'] = 'en-US'
        headers['Accept-Encoding'] = 'deflate, br'
        headers['User-Agent'] = self.user_agent
        headers['Host'] = 'public-ubiservices.ubi.com'
        headers['Cache-Control'] = 'no-cache'
        headers['Accept'] = "*/*"
        headers['Authorization'] = "Basic %s" %self.encoded_u

        request_url = "https://public-ubiservices.ubi.com/v3/profiles/sessions"

        data = requests.post(request_url, headers=headers)

        systemOutput  = dict()
        if(data.status_code != 301):
            output = json.loads(data.text)
            if("errorCode" in output):
                systemOutput['error'] = output['message']
            else:
                systemOutput['output'] = 'Saving user data to cache/user.json'
                self.save_user(data.text)
        else:
            systemOutput['error'] = "System is trying to redirect. Aborting!"

        return systemOutput

    ##saves the user data to json in cache/user.json
    def save_user(self, json_output = ""):
        try:
            with open('../cache/user.json', 'w') as file:
                file.write(json_output)
                file.close()
        except(FileNotFoundError, PermissionError, OSError):
            print('File not found | Permission Error | Operating system error')

    ## checks if the input json is an actual json
    def is_json(self,myjson):
        try:
            json.loads(myjson)
        except ValueError as e:
            return False
        return True


    def refresh_ticket(self):
        login = self.login()
        if("error" not in login):
            with open('../cache/user.json', 'r') as file:
                json_output = file.read()
                if (json_output != "" and self.is_json(json_output)):
                    user_data = json.loads(json_output)
                    ticket = user_data['ticket']
                    return "Ubi_v1 t=" + ticket
                else:
                    raise Exception('There was a problem parsing the file cache/user.json')
        else:
            raise Exception(login['error'])

    def uplay_ticket(self):
        with open('../cache/user.json', 'r') as file:
            json_output = file.read()
            if(json_output != "" and self.is_json(json_output)):

                user_data = json.loads(json_output)
                ticket = user_data['ticket']
                expiration = user_data['expiration']
                session_id = user_data['sessionId']
                session_key = user_data['sessionKey']
                user_id = user_data['userId']
                profile_id = user_data['profileId']
                expiration = expiration[:-4]
                time = datetime.datetime.strptime(expiration,'%Y-%m-%dT%H:%M:%S.%f')
                if (dt.now() < time):
                    pass
                else:
                    try:
                        return self.refresh_ticket()
                    except Exception as error:
                        #return error
                        pass

                return "Ubi_v1 t=" + ticket
            else:
                try:
                    return self.refresh_ticket()
                except Exception as error:
                    return error


    def uplay_session(self):
        with open('../cache/user.json', 'r') as file:
            json_output = file.read()
            if(json_output != "" and self.is_json(json_output)):
                user_data = json.loads(json_output)
                session_id = user_data['sessionId']
                session_key = user_data['sessionKey']
                return session_id

    # def save_ticket(self,save, ticket=""):
    #     if(save) :
    #         with open('cache/user.json', 'w') as f:
    #             f.write(ticket)
    #     else:
    #         with open('cache/user.json','r') as f:
    #             return f.read()
    #
    #
    # def uplay_ticket(self, check = True):
    #     ticket = json.loads(self.save_ticket(False))
    #     if("expiration" not in ticket or "error" in ticket and ticket['error'] == True or  "errorCode" in ticket and check):
    #         self.login()
    #         return self.uplay_ticket(False)
    #     elif check:
    #         expiration  = ticket['expiration']
    #         expiration = expiration[:-4]
    #         time = datetime.datetime.strptime(expiration,'%Y-%m-%dT%H:%M:%S.%f')
    #         if(time < dt.now()):
    #             self.login()
    #             return self.uplay_ticket(False)
    #
    #     else:
    #         pass
    #
    #     if("ticket" not in ticket):
    #         return ''
    #
    #     ticket_string = ticket['ticket']
    #
    #     return "Ubi_v1 t=" + ticket_string
    #
    #
    # def save_session(self,save = True, session = ""):
    #     if (save):
    #         with open('cache/session_id', 'w') as f:
    #            if(json.loads(session)):
    #                session = json.loads(session)
    #                session_id = session['sessionId']
    #                f.write(session_id)
    #            else:
    #                session_id = self.sessionid
    #                f.write(session_id)
    #
    #         return session_id
    #     else:
    #         with open('cache/session_id', 'r') as f:
    #             return f.read()
    #
    # def uplay_session(self,session = ""):
    #     sessionPath = Path('cache/session_id')
    #     if(sessionPath.is_file()):
    #         with open('cache/session_id', 'r') as f:
    #             data = f.read()
    #             if(data != ""):
    #                 return data
    #             else:
    #                 data = self.login()
    #                 return self.save_session(True,data)
    #     else:
    #         self.save_session(True,session)


    def findPlayer(self,username):
        url = "https://public-ubiservices.ubi.com/v2/profiles?nameOnPlatform="+username+"&platformType=uplay"
        headers = CaseInsensitiveDict()
        headers["Authorization"] = self.uplay_ticket()
        headers["Accept-Language"] = "en-US,en;q=0.9"
        headers["Ubi-AppId"] = '314d4fef-e568-454a-ae06-43e3bece12a6'
        headers["Ubi-SessionId"] = self.uplay_session()
        headers["Accept"] = "*/*"
        headers["Origin"] = "https://connect.ubisoft.com"
        headers["Referer"] = "https://connect.ubisoft.com"
        headers["User-Agent"] = self.user_agent

        profile = dict()
        try:
            data = requests.get(url, headers=headers)
            if (data.status_code != 301):
                output = json.loads(data.text)

                if ("errorCode" in output):
                    profile['error'] = output['message']
                else:
                    profile['data'] = output['profiles'][0]
            else:
                profile['error'] = 'Error has occurred'
        except Exception as e:
            profile['error'] = 'Unable to access resource. Resource not found.'

        return profile

    def getDivision2StatsByIdentifier(self, uplayId = "43fe181a-d92a-408f-9f84-c43042197baf"):
        url = 'https://public-ubiservices.ubi.com/v1/profiles/' + uplayId +'/statscard?spaceId=60859c37-949d-49e2-8fc8-6d8dc40f1a9e'
        headers = CaseInsensitiveDict()
        headers["Authorization"] = self.uplay_ticket()
        headers["Origin"] = "https://connect.ubisoft.com"
        headers["Host"] = "public-ubiservices.ubi.com"
        headers["Accept-Language"] = "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7"
        headers["User-Agent"] = self.user_agent
        headers["Accept"] = "application/json, text/plain, */*"
        headers["Ubi-AppId"] = self.ubiappid
        headers["Ubi-SessionId"] = self.uplay_session()
        headers["Ubi-LocaleCode"] = "en-US"
        headers["Referer"] = "https://connect.ubisoft.com/"
        headers["Connection"] =  "keep-alive"

        stats = dict()

        try:
            data = requests.get(url, headers=headers)

            if (data.status_code != 301):
                output = json.loads(data.text)
                if ("errorCode" in output):
                    stats['error'] = output['message']
                else:
                    returns = dict()
                    cards = json.loads(data.text)
                    for item in cards['Statscards']:
                        returns[item['statName']] = item['value']
                    stats['output'] = returns
            else:
                stats['error'] = 'Error has occured'

        except Exception as e:
            stats['error'] = "Unable to access resource."

        return stats

