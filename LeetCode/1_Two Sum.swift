class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var numToIndex = [Int: Int]()   // Num: Index
        
        for (index, num) in nums.enumerated() {
            if let complementIndex = numToIndex[target-num] {
                return [complementIndex, index]
            }
            numToIndex[num] = index
        }
        
        return []
    }
}
