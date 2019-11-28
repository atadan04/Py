def secintime(sec):
    day = 0
    hou = 0
    min = 0
    if sec<0:
        return "Error"
    if sec // 86400 > 0:
        day = sec // 86400
    sec = sec % 86400
    if sec // 3600 > 0:
        hou = sec // 3600
    sec = sec % 3600
    if sec // 60 > 0:
        min = sec // 60
    sec = sec % 60
    return str(str(day) + "day " + str(hou) + "hou " + str(min) + "min " + str(sec) + "sec ")
sec = int(input("Enter the number of seconds:\n"))
print(secintime(sec))

