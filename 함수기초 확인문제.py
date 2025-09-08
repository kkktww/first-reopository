def GetMinMax(data):
    min_val = data[0]
    max_val = data[0]

    for num in data:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    return min_val, max_val

# 함수 사용 예시
min_value, max_value = GetMinMax([5, 6, 3, 9, 8, 1, 4])

print(f"최소값 : {min_value}")
print(f"최대값 : {max_value}")
