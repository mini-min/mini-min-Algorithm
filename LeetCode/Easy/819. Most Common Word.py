def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    paragraph = paragraph.lower()  # 소문자로 변경
    words = re.sub('[\'?!;",.]',' ',paragraph).split()      # 구두점 제거 + 공란 기준으로 split
    words = [word for word in words if word not in banned]  # banned 단어 필터링
    words = collections.Counter(words)  # Counter 객체로 최빈값 계산
    return words.most_common(1)[0][0]   # 최빈값 리턴
