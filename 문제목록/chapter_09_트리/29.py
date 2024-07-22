"""
문제 29 다단계 칫솔 판매

난이도: ⭐️⭐️
저자 권장 시간: 60분
권장 시간 복잡도: O(N*M)
출제: 2021 Dev-Matching 웹 백엔드 개발자(상반기)
정답률: 39%
날짜: 2024-07-21 일요일

제약조건:
    - enroll의 길이는 1 이상 10,000 이하입니다.
        - enroll에 민호의 이름은 없습니다. 따라서 enroll의 길이는 민호를 제외한 조직 구성원의 총 수입니다.
    - referral의 길이는 enroll의 길이와 같습니다.
        - referral 내에서 i 번째에 있는 이름은 배열 enroll 내에서 i 번째에 있는 판매원을 조직에 참여시킨 사람의 이름입니다.
        - 어느 누구의 추천도 없이 조직에 참여한 사람에 대해서는 referral 배열 내에 추천인의 이름이 기입되지 않고 “-“ 가 기입됩니다. 위 예제에서는 john 과 mary 가 이러한 예에 해당합니다.
        - enroll 에 등장하는 이름은 조직에 참여한 순서에 따릅니다.
        - 즉, 어느 판매원의 이름이 enroll 의 i 번째에 등장한다면, 이 판매원을 조직에 참여시킨 사람의 이름, 즉 referral 의 i 번째 원소는 이미 배열 enroll 의 j 번째 (j < i) 에 등장했음이 보장됩니다.
    - seller의 길이는 1 이상 100,000 이하입니다.
        - seller 내의 i 번째에 있는 이름은 i 번째 판매 집계 데이터가 어느 판매원에 의한 것인지를 나타냅니다.
        - seller 에는 같은 이름이 중복해서 들어있을 수 있습니다.
    - amount의 길이는 seller의 길이와 같습니다.
        - amount 내의 i 번째에 있는 수는 i 번째 판매 집계 데이터의 판매량을 나타냅니다.
        - 판매량의 범위, 즉 amount 의 원소들의 범위는 1 이상 100 이하인 자연수입니다.
    - 칫솔 한 개를 판매하여 얻어지는 이익은 100 원으로 정해져 있습니다.
    - 모든 조직 구성원들의 이름은 10 글자 이내의 영문 알파벳 소문자들로만 이루어져 있습니다.

입출력의 예:
    - enroll ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
    - referral ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
    - seller ["young", "john", "tod", "emily", "mary"]
    - amount [12, 4, 2, 5, 10]
    - result [360, 958, 108, 0, 450, 18, 180, 1080]
"""


# 저자 풀이
# 시간 복잡도 O(N*M)
def solution(enroll, referral, seller, amount):
    referral_dict = dict(zip(enroll, referral))  # 전체 판매원들의 추천인이 누군지 알 수 있는 딕셔너리

    result = {name: 0 for name in enroll}  # 각 판매원들의 이득 총액을 구하기 위해 초기화

    for i in range(len(seller)):
        total_revenue = amount[i] * 100  # 칫솔1개 판매하면 수익이 100원, 총 판매 수익 계산
        cur_name = seller[i]  # 판매원의 이름이 담겨 있음

        while total_revenue > 0 and cur_name != '-':
            result[cur_name] += total_revenue - total_revenue // 10  # 판매원은 판매수익에서 이익의 10%를 주고 남은 금액을 가짐
            cur_name = referral_dict[cur_name]  # 판매원의 추천인을 찾는 과정
            total_revenue //= 10  # 10%를 주고 남은 금액

    return [result[name] for name in enroll]


# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
result = [360, 958, 108, 0, 450, 18, 180, 1080]
print(solution(enroll, referral, seller, amount)) # 반환값 : [360, 958, 108, 0, 450, 18, 180, 1080]


"""
Note:
- 문제 읽고 고민한 내용
    - enroll, referral의 길이가 같으니 zip함수를 써서 직원의 추천인을 찾으면 되겠다 싶었다.
    - 코드는 크게 어려운것 같진 않은데, 고민하다 잘 안되서 저자 풀이보고 공부했다.
- 저자의 풀이와 비교해봤을 때 배울 점
    - 판매원의 추천인을 찾기 위해 while문으로 cur_name이라는 변수에 추천인을 담는다.
    - 판매원은 총 이익의 10%를 주고 남은 금액을 갖고
    - 판매원의 추천인들은 이익의 10%에서 10%를 주고 남은 금액을 반복해서 나눠 갖는다. 이 금액들을 초기화해둔 result에 계속 더한다.
"""
