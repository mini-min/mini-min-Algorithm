class Solution {
    func mostCommonWord(_ paragraph: String, _ banned: [String]) -> String {
        var wordCheckDict = [String: Int]()

        // 단어 처리(소문자 + 공백 변환) & 구분(공백 기준)
        let words = paragraph.lowercased().replacingOccurrences(of: ",", with: " ").split(separator: " ")

        // 단어 반복하면서 갯수 체크
        for word in words {
            var newWord = word.components(separatedBy: ["!", "?", "'", ",", ";", "."]).joined()
            // 딕셔너리에 등록된 word가 아닌 경우 + banned 단어가 아닌 경우 -> 새롭게 딕셔너리 카운트 추가
            if (wordCheckDict[newWord] == nil && !banned.contains(newWord)) { 
                wordCheckDict[newWord] = 1 
            } else {
                if let count = wordCheckDict[newWord] { wordCheckDict[newWord] = count + 1 }
            }
        }

        // 가장 자주 등장하는 단어 찾기
        var mostCommonWord = ""
        var maxCount = 0
        for (word, count) in wordCheckDict {
            if count > maxCount {
                mostCommonWord = word
                maxCount = count
            }
        }
        
        return mostCommonWord
    }
}
