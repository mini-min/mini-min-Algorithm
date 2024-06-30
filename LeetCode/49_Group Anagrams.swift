class Solution {
    func groupAnagrams(_ strs: [String]) -> [[String]] {
        var anagrams = [String: [String]]()         // Anagram을 판단하기 위한 딕셔너리 
        
        for str in strs {
            let sortedStr = String(str.sorted())    // 정렬된 단어를 Key값으로 가짐 -> 애너그램 단어는 정렬해도 단어가 같음

            if var anagram = anagrams[sortedStr] {  // 딕셔너리에 key 값이 있는 경우 -> 기존 Value에 append한 후, 갈아 끼우기
                anagram.append(str)
                anagrams[sortedStr] = anagram
            } else {                                // 딕셔너리에 key 값이 없는 경우 -> Key 값에 해당하는 새로운 Array 추가
                anagrams[sortedStr] = [str]
            }
        }
        
        return Array(anagrams.values)
    }
}
