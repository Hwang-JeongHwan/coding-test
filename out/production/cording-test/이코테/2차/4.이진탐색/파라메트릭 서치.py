# 파라메트릭 서치란 최적화 문제를 결정 문제(예 혹은 아니오)로 바꾸어 해결하는 기법임
# ex) 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제

# 일반적으로 코딩테스트에서 파라메트릭 서치 문제는 이진 탐색을 이용하여 해결할 수 있음

# def binary_search(array, target, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
#     if array[mid] == target:
#         return mid

#     if array[mid] > target:
#         return binary_search(array, target, start, mid - 1)
    
#     else:
#         return binary_search(array, target, mid + 1, end)
