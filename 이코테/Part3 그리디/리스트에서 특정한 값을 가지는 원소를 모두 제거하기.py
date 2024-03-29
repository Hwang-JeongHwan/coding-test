a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5} # 집합 자료형 (집합 자료형은 추후에 다시 다룹니다.)
# 특정한 값의 존재유무만 판단할때 유용하게 사용

# remove_list에 포함되지 않은 값만을 저장
result = [i for i in a if i not in remove_set]
# a라는 리스트를 i라는 변수가 하나씩 확인하면서 i 라는 변수가 remove_set에 포함되지 않은경우만
# result라는 리스트에 추가 
print(result)


# 튜플은 한 번 선언된 값을 변경할수 없음 -> 문자열과 같음
# 리스트는 대괄호([])를 이용하지만 튜플은 소괄호(())를 이용함
# 튜플은 리스트에 비해 상대적으로 공간 효율적임

a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# 네 번째 원소만 출력
print(a[3])

# 두번째 원소부터 네번째 원소까지
print(a[1 : 4])

# 서로 다른 성질의 데이터를 묶어서 관리해야 할 때
# 최단 경로 알고리즘에서는 (비용(실수값), 노드 번호(정수형태))의 형태로 튜플 자료형을 자주 사용함
# 학생 정보라고 하면 학번, 성적등을 하나로 묶어서 관리할 수 있음

# 데이터의 나열을 해싱(hashing)의 키값으로 사용해야 할 때
# 튜플은 변경이 불가능하므로 리스트와 다르게 키 값으로 사용될수 있음 -> 리스트는 변경이 가능한 객체이기
# 때문에 키 값으로 사용할수 없음
# 리스트 보다 메모리를 효율적으로 사용해야 할 때 사용

# 사전 자료형 (dictionary)
# 사전 자료형은 키(key)와 값(value)의 쌍을 데이터로 가지는 자료형
# 앞서 다루었던 리스트나 튜플이 값을 순차적으로 저장하는 것과는 대비됨
# 리스트의 경우 값이 앞에서부터  뒤쪽까지 차례대로 저장이 되어있기 떄문에 몇번째 원소에 접근할때
# 인덱싱을 이용 <-> 반면에 사전자료형은 키와 값의 쌍을 데이터로 가지며 임의의 변경불가능한 자료형을 키로 사용
# 할수있음 파이썬의 사전 자료형은 해시 테이블을 이용하므로 데이터의 조회 및 수정에 있어서 O(1)상수 시간에 처리 가능

data = dict()
# 키           value
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)
if '사과' in data:
    print('사과를 키로 가지는 데이터가 존재함')

#  사전 자료형에서는 키와 값을 별도로 뽑아내기 위한 메서드를 지원
# 키 데이터만 뽑아서 리스트로 이용할때는 keys()함수를 이용
# 값 데이터만 뽑아서 리스트로 이용할 때는 values()함수를 이용 


# 키 데이터만 담은 리스트
key_list = data.keys()

# 값 데이터만 담은 리스트
value_list = data.values()

print(key_list)
print(value_list)

# 각 키에 따른 값을 하나씩 출력
for key in key_list:
    print(data[key])

# for value in value_list:
#     print(data[value]) 이건 안되네..
for i in data:
    print(i)
# 특정한 키에 맵핑되는 값에 접근
print(data['사과'])
b = {
    '홍길동' : 97,
    '이순신' : 98
}
print(b)