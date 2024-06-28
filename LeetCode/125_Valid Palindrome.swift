class Solution {
    func isPalindrome(_ s: String) -> Bool {
        // 반복하면서 담을 문자열 선언
        var newString: String = ""  

        // 입력 String을 반복하면서 문자와 숫자만 남기기 + 소문자로 변환
        s.forEach {
            if ($0.isLetter || $0.isNumber) { 
                newString.append($0.lowercased()) 
            }
        }

        // 최종 팰린드롬 비교
        return newString == String(newString.reversed())
    }
}
