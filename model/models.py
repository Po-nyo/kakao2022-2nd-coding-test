class WaitingUser:

    def __init__(self, info):
        self.id = info['id']
        self.fr = info['from']

    def __str__(self):
        return f'[id: {self.id}, fr: {self.fr}]'


class GameResult:

    def __init__(self, game_result):
        self.win = game_result['win']
        self.lose = game_result['lose']
        self.taken = game_result['taken']

    def __str__(self):
        return f'[win: {self.win}, lose: {self.lose}, taken: {self.taken}]'


class UserInfo:

    def __init__(self, info):
        self.id = info['id']
        self.grade = info['grade']

    def __str__(self):
        return f'[id: {self.id}, grade: {self.grade}]'


class Match:

    def __init__(self):
        self.pairs = []

    def match(self, user1, user2):
        self.pairs.append([user1, user2])

    def get_match_request(self):
        return {'pairs': self.pairs}


class ChangeGrade:

    def __init__(self):
        self.commands = []

    def change_grade(self, user_id, grade):
        self.commands.append({'id': user_id, 'grade': grade})

    def get_change_grade_request(self):
        return {'commands': self.commands}
