from solution import *
from api.kakao_api import KakaoApiRequester

if __name__ == '__main__':
    kakao = KakaoApiRequester()
    strategy1(kakao)
    print(kakao.score())

# 시나리오 1번 레코드 (strategy1)
# {'status': 'finished',
# 'efficiency_score': '98.3533',
# 'accuracy_score1': '68.6667',
# 'accuracy_score2': '57.921',
# 'score': '230.5879'}

# 시나리오 2번 레코드 (strategy1)
# {'status': 'finished',
# 'efficiency_score': '98.7742',
# 'accuracy_score1': '70.9267',
# 'accuracy_score2': '58.8217',
# 'score': '234.7174'}
