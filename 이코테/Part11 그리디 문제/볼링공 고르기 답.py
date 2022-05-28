# 무게마다 볼링공이 몇 개 있는지를 계산 => A가 특정한 무게의 공을 선택 했을대 이어서 B가 볼링공을 선택하는 경우를 차례대로 계산하여
# 문제 해결 가능
# A 를 기 준으로 무게가 낮은 볼링공부터 무게가 높은 볼링공까지 순서대로 하나씩 확인
# 무게가 1인공 1개 2인공 2개 3인공 2개가 있다고 가정
# A가 1인공을 선택할때의 경우의 수:
# 1(무게가 1인 공의 개수) x 4(B가 선택하는 경우의 수) = 4가지 경우
# 
# A가 2인 공을 선택할 때의 경우의 수 
# 2(무게가 2인 공의 개수) x 2(B가 선택하는 경우의 수) = 4가지 경우
# 
# A가 무게가 3인 공을 선택할 때의 경우의수
# 2(무게가 3인 공의 개수) x 0(B가 선택하는 경우의 수) = 0가지 경우  
# 이미 계산 했던 경우(조합)는 제외 하기 때문에 단계가 진행 됨에 따라 B가 선택하는 경우의 수는 줄어듬
n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for i in data:
    array[i] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
    n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += array[i] * n # B가 선택하는 경우의 수와 곱하기 

print(result)

