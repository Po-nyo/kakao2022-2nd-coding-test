from model.models import *
from config import app_properties


# id: power (default: 1000)
user_power = {}


def init():
    global user_power
    user_count = 30 if app_properties.PROBLEM == 1 else 900
    user_power = {i: 1000 for i in range(1, user_count + 1)}


def determine_grade(kakao):
    change_grade = ChangeGrade()
    users = dict(sorted(user_power.items(), key=lambda info: info[1], reverse=True)).keys()
    for idx, user in enumerate(users):
        change_grade.change_grade(user, 9999 - idx)
    kakao.change_grade(change_grade.get_change_grade_request())


def win_rate(user1_id, user2_id):
    return 1 / (1 + 10 ** ((user_power[user2_id] - user_power[user1_id]) / 400))


def modify_user_power(game_result):
    k = 50 - game_result.taken
    rate = win_rate(game_result.win, game_result.lose)
    user_power[game_result.win] += k * (1 - rate)
    user_power[game_result.lose] += k * (rate - 1)


# 아무것도 안하기
def do_nothing(kakao):
    for _ in range(595):
        print(kakao.match(Match().get_match_request()))


# 단순하게 매칭한 순서대로 매치 잡아주기
def asap(kakao):
    for i in range(595):
        waiting_users = kakao.waiting_line()
        waiting_users = sorted(waiting_users, key=lambda elem: elem.fr, reverse=True)
        match = Match()
        while len(waiting_users) >= 2:
            user1, user2 = waiting_users.pop(), waiting_users.pop()
            match.match(user1.id, user2.id)

        print(kakao.match(match.get_match_request()))
        game_result = kakao.game_result()
        # print(list(map(str, game_result)))
        for r in game_result:
            winner, loser, taken = r.win, r.lose, r.taken
            user_power[winner] = user_power.get(winner, 1000) + 20
            user_power[loser] = user_power.get(loser, 1000) - 20

        if i == 594:
            determine_grade(kakao)

    # 종료
    kakao.match(Match().get_match_request())
    # 최종 결과
    print(user_power)
    print(list(map(str, kakao.user_info())))


# Elo 레이팅 적용 전략
# 모든 유저의 점수를 일정 값으로 초기화
# (가중치) * (경기 결과 - 이길 확률) 만큼 점수 변화
# (경기 결과)는 이겼을 경우 1, 무승부 경우 0.5, 졌을 경우 0으로 설정
# 유저 A가 (이길 확률)은 1 / (1 + 10^(B의 점수 - A의 점수) / 400)
def strategy1(kakao):
    global user_power
    init()

    for i in range(595):
        waiting_users = kakao.waiting_line()
        game_result = kakao.game_result()

        for result in game_result:
            if app_properties.PROBLEM == 2 and result.taken <= 10:
                continue
            modify_user_power(result)

        waiting_users = sorted(waiting_users, key=lambda elem: elem.fr - i)
        match, matched = Match(), set()

        # 기다린 시간: 실력차 허용치
        allowed_range = {5: 0.1, 10: 0.2, 15: 0.3}
        for idx, user1 in enumerate(waiting_users):
            if user1.id in matched:
                continue

            allowed = allowed_range[5]
            for wait, value in allowed_range.items():
                if user1.fr - i <= wait:
                    allowed = value
                    break

            another_user = None
            for idx2 in range(idx + 1, len(waiting_users)):
                user2 = waiting_users[idx2]
                if user2.id in matched or idx == idx2:
                    continue

                diff = abs(win_rate(user1.id, user2.id) - 0.5)
                if diff <= allowed:
                    another_user = user2
                    break

            if another_user:
                # print(f'{user_power[user1.id]} {user_power[another_user.id]} {win_rate(user1.id, another_user.id)}')
                match.match(user1.id, another_user.id)
                matched.add(user1.id)
                matched.add(another_user.id)

        print(kakao.match(match.get_match_request()))

        if i == 594:
            determine_grade(kakao)

    # 종료
    kakao.match(Match().get_match_request())
    # 최종 결과
    print(user_power)
    print(list(map(str, kakao.user_info())))
