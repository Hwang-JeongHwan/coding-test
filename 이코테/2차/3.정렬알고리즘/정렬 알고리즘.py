# 정렬이란 데이터를 특정한 기준에 따라 순서대로 나열하는 것을 말함
# 일반적으로 문제 상황에 따라서 적절한 정렬 알고리즘이 공식처럼 사용됨 

# 선택정렬: 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해
# 맨앞에 있는 데이터와 바꾸는것을 반복함
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(array))
