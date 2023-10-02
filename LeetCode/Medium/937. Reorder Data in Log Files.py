def reorderLogFiles(self, logs: List[str]) -> List[str]:
    # 문자로그와 숫자로그를 구분
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
     
    # 문자로그 정렬
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits
