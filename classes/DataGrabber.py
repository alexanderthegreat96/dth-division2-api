from bs4 import BeautifulSoup
import json
import math
import locale


class Datagrabber:

    def __init__(self, playername, platform,chrome):
        self.playername = playername
        self.platform = platform
        self.chrome = chrome

    def getXboxData(self):
        dataArray = dict()
        try:
            self.chrome.get('https://api.tracker.gg/api/v2/division-2/standard/profile/xbl/' + self.playername)
            try:
                soup = BeautifulSoup(self.chrome.page_source, features="html.parser")
                bodyText = soup.find("body").text

                if (bodyText):
                    jsonBody = bodyText
                    try:
                        response = json.loads(jsonBody)

                        if ("errors" in response):
                            dataArray['error'] = response['errors'][0]['message']
                        else:

                            platformInfo = response['data']['platformInfo']
                            playerStats = response['data']['segments'][0]['stats']
                            avatarUrl = platformInfo['avatarUrl']

                            data = dict()

                            data['platformSlug'] = platformInfo['platformSlug']
                            data['platformUserId'] = platformInfo['platformUserId']
                            data['username'] = platformInfo['platformUserIdentifier']
                            data['avatarUrl'] = avatarUrl

                            for i in playerStats:
                                data[i] = playerStats[i]

                            dataArray['data'] = data
                    except Exception as e:
                        dataArray['error'] = 'There was an error. System was unable to parse JSON output. ' + e.message

                else:
                    dataArray['error'] = 'Unexpected error. Could not get an input from server.'
            except Exception as e:
                dataArray['error'] = 'There was a parsing error: ' + e.message
        except Exception as e:
            dataArray['error'] = "There was en error: " + e.message

        return dataArray

    def getPCData(self):

        dataArray = dict()
        try:

            self.chrome.get('https://api.tracker.gg/api/v2/division-2/standard/profile/uplay/' + self.playername)
            try:
                soup = BeautifulSoup(self.chrome.page_source, features="html.parser")
                bodyText = soup.find("body").text

                if (bodyText):
                    jsonBody = bodyText
                    try:
                        response = json.loads(jsonBody)

                        if ("errors" in response):
                            dataArray['error'] = response['errors'][0]['message']
                        else:

                            platformInfo = response['data']['platformInfo']
                            playerStats = response['data']['segments'][0]['stats']
                            avatarUrl = platformInfo['avatarUrl']

                            data = dict()

                            data['platformSlug'] = platformInfo['platformSlug']
                            data['platformUserId'] = platformInfo['platformUserId']
                            data['username'] = platformInfo['platformUserIdentifier']
                            data['avatarUrl'] = avatarUrl


                            for i in playerStats:
                                data[i] = playerStats[i]

                            dataArray['data'] = data
                    except Exception as e:
                        dataArray['error'] = 'There was an error. System was unable to parse JSON output. ' + e.message

                else:
                    dataArray['error'] = 'Unexpected error. Could not get an input from server.'
            except Exception as e:
                dataArray['error'] = 'There was a parsing error: ' + e.message
        except Exception as e:
            dataArray['error'] = "There was en error: " + e.message

        return dataArray


    def getPSNData(self):
        dataArray = dict()
        try:

            self.chrome.get('https://api.tracker.gg/api/v2/division-2/standard/profile/psn/' + self.playername)
            try:
                soup = BeautifulSoup(self.chrome.page_source, features="html.parser")
                bodyText = soup.find("body").text

                if (bodyText):
                    jsonBody = bodyText
                    try:
                        response = json.loads(jsonBody)

                        if ("errors" in response):
                            dataArray['error'] = response['errors'][0]['message']
                        else:

                            platformInfo = response['data']['platformInfo']
                            playerStats = response['data']['segments'][0]['stats']
                            avatarUrl = platformInfo['avatarUrl']

                            data = dict()

                            data['platformSlug'] = platformInfo['platformSlug']
                            data['platformUserId'] = platformInfo['platformUserId']
                            data['username'] = platformInfo['platformUserIdentifier']
                            data['avatarUrl'] = avatarUrl

                            for i in playerStats:
                                data[i] = playerStats[i]

                            dataArray['data'] = data
                    except Exception as e:
                        dataArray['error'] = 'There was an error. System was unable to parse JSON output. ' + e.message

                else:
                    dataArray['error'] = 'Unexpected error. Could not get an input from server.'
            except Exception as e:
                dataArray['error'] = 'There was a parsing error: ' + e.message
        except Exception as e:
            dataArray['error'] = "There was en error: " + e.message

        return dataArray


    def fetchPlayerData(self):
        if(self.platform == 'psn'):
            return self.getPSNData()
        elif(self.platform == 'xbox'):
            return self.getXboxData()
        elif(self.platform == 'uplay'):
            return self.getPCData()
        else:
            return self.getPCData()