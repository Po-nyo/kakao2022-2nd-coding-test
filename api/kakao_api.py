from . import base_requester
from config import app_properties
from model.models import *


class KakaoApiRequester:

    headers = {'Content-Type': 'application/json; charset=utf-8'}

    def __init__(self):
        headers = self.headers.copy()
        headers['X-Auth-Token'] = app_properties.X_AUTH_TOKEN
        data = {'problem': app_properties.PROBLEM}
        res = base_requester.post('/start', headers=headers, data=data)
        print('==================== start ====================')
        print(f'{res}')
        print('===============================================')
        self.headers['Authorization'] = res['auth_key']

    def waiting_line(self):
        waiting_line = base_requester.get('/waiting_line', headers=self.headers)['waiting_line']
        return [WaitingUser(info) for info in waiting_line]

    def game_result(self):
        game_result = base_requester.get('/game_result', headers=self.headers)['game_result']
        return [GameResult(info) for info in game_result]

    def user_info(self):
        user_info = base_requester.get('/user_info', headers=self.headers)['user_info']
        return [UserInfo(info) for info in user_info]

    def match(self, data):
        return base_requester.put('/match', headers=self.headers, data=data)

    def change_grade(self, data):
        return base_requester.put('/change_grade', headers=self.headers, data=data)

    def score(self):
        return base_requester.get('/score', headers=self.headers)
