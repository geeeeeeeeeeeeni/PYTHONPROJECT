'''
Dictionary
    key:value로 이루어져 쌍으로 데이터 값을 저장하는데 사용
    키값 중복 불가.
'''

#값 가져오기
thisdict = {
        "brand" : "꾸찌",
        "model" : "g001",
        "year" : 2022
}

print(thisdict["brand"])
print(thisdict.get("brand"))


# 키 목록 가져오기
print(thisdict.keys())

#추가하기
thisdict = {
        "brand" : "Ford",
        "model" : "Mustang",
        "year" : 1964
}

thisdict["color"] = "red"
print(thisdict)
thisdict.update({"bgColor" : "Black"})
print(thisdict)

#변경하기 -> 원래 없었으면 추가되고, 있었으면 수정됩니다.
thisdict["color"] = "yellow"
print(thisdict)
thisdict.update({"bgColor" : "blue"})
print(thisdict)

#제거하기
thisdict.pop("model")
print(thisdict)

#마지막 삽입된 항목 제거하기
thisdict.popitem()
print(thisdict)