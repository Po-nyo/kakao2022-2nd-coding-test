# 2022 카카오 신입공채 2차 온라인 테스트
## 게임 매칭 알고리즘 설계하기
https://school.programmers.co.kr/skill_check_assignments/265

개인 풀이 코드 입니다.

<br>

## 기본 전략

Elo 레이팅 전략 사용
1. 모든 유저의 점수를 일정 값으로 초기화
2. 경기 결과에 따라 k * (gameResult - 이길 확률) 만큼 점수 변경. (k는 가중치, gameResult 는 승리: 1, 무승부: 0.5, 패배: 0)
3. 가중치 k는 경기 시간에 따라 다르게 설정
4. A가 B에게 이길 확률은 1 / (10 ^ ((B의 점수 - A의 점수) / 400) + 1)
5. 게임 매칭시, 기다린 시간이 많은 유저가 먼저 상대를 찾는 우선순위가 높음
6. 기다린 시간이 길수록 승률이 50% 와 더 멀어지는 상대와 매칭 가능
7. 시나리오 2번의 경우, 경기 시간이 10분 이하인 경기는 무시

## 시나리오 1번 레코드

efficiency_score: 98.3533

accuracy_score1: 68.6667

accuracy_score2: 57.921

score: 230.5879

## 시나리오 2번 레코드
status: finished

efficiency_score: 98.7742

accuracy_score1: 70.9267

accuracy_score2: 58.8217

score: 234.7174
