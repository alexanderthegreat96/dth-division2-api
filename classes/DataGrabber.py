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
        self.chrome.get('https://api.tracker.gg/api/v2/division-2/standard/profile/xbl/' + self.playername)
        soup = BeautifulSoup(self.chrome.page_source, features="html.parser")
        bodyText = soup.find("body").text

        if (bodyText):
            jsonBody = bodyText
            response = json.loads(jsonBody)

            if ("errors" in response):
                dataArray['error'] = response['errors'][0]['message']
            else:

                platformInfo = response['data']['platformInfo']
                playerStats = response['data']['segments'][0]['stats']
                avatarUrl = platformInfo['avatarUrl']

                dataArray['data'] = []
                dataArray['data'].append({'platformSlug' : platformInfo['platformSlug']})
                dataArray['data'].append({'platformUserId' : platformInfo['platformUserId']})
                dataArray['data'].append({'avatarUrl':avatarUrl})

                for i in playerStats:
                    dataArray['data'].append({i:playerStats[i]})

        else:
            dataArray['error'] = 'Unexpected error. Could not get an input from server.'

        return dataArray

    def getPCData(self):

        dataArray = dict()
        self.chrome.get('https://api.tracker.gg/api/v2/division-2/standard/profile/uplay/' + self.playername)
        soup = BeautifulSoup(self.chrome.page_source, features="html.parser")
        bodyText = soup.find("body").text

        if (bodyText):
            jsonBody = bodyText
            response = json.loads(jsonBody)

            if ("errors" in response):
                dataArray['error'] = response['errors'][0]['message']
            else:

                platformInfo = response['data']['platformInfo']
                playerStats = response['data']['segments'][0]['stats']
                avatarUrl = platformInfo['avatarUrl']

                dataArray['data'] = []
                dataArray['data'].append({'platformSlug': platformInfo['platformSlug']})
                dataArray['data'].append({'platformUserId': platformInfo['platformUserId']})
                dataArray['data'].append({'avatarUrl': avatarUrl})

                for i in playerStats:
                    dataArray['data'].append({i: playerStats[i]})

        else:
            dataArray['error'] = 'Unexpected error. Could not get an input from server.'

        return dataArray


    def getPSNData(self):
        dataArray = dict()
        self.chrome.get('https://api.tracker.gg/api/v2/division-2/standard/profile/psn/' + self.playername)
        soup = BeautifulSoup(self.chrome.page_source, features="html.parser")
        bodyText = soup.find("body").text

        if (bodyText):
            jsonBody = bodyText
            response = json.loads(jsonBody)

            if ("errors" in response):
                dataArray['error'] = response['errors'][0]['message']
            else:

                platformInfo = response['data']['platformInfo']
                playerStats = response['data']['segments'][0]['stats']
                avatarUrl = platformInfo['avatarUrl']

                dataArray['data'] = []
                dataArray['data'].append({'platformSlug': platformInfo['platformSlug']})
                dataArray['data'].append({'platformUserId': platformInfo['platformUserId']})
                dataArray['data'].append({'avatarUrl': avatarUrl})

                for i in playerStats:
                    dataArray['data'].append({i: playerStats[i]})

        else:
            dataArray['error'] = 'Unexpected error. Could not get an input from server.'

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