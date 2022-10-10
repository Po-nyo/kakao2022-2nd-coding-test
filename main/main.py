from solution import *
from api.kakao_api import KakaoApiRequester

if __name__ == '__main__':
    kakao = KakaoApiRequester()
    strategy1(kakao)
    print(kakao.score())

# 시나리오 1번 레코드 (strategy1)
# {'status': 'finished',
# 'efficiency_score': '95.9259',
# 'accuracy_score1': '79.7778',
# 'accuracy_score2': '61.7019',
# 'score': '246.5164'}

# 시나리오 2번 레코드 (strategy1)
# {'status': 'finished',
# 'efficiency_score': '98.7742',
# 'accuracy_score1': '70.9267',
# 'accuracy_score2': '58.8217',
# 'score': '234.7174'}
