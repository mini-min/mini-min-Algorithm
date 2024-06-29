class Solution {
    func reorderLogFiles(_ logs: [String]) -> [String] {
        var letterLogs = [String]()
        var digitLogs = [String]()

        // letterLog와 digitLog 분리해서 Array에 담기
        for log in logs {
            guard let check = log.split(separator: " ")[1].first as? Character else { continue }
            check.isLetter ? letterLogs.append(log) : digitLogs.append(log)
        }

        // letterLog 정렬하기
        letterLogs.sort { log1, log2 in
            let log1Split = log1.split(separator: " ")
            let log2Split = log2.split(separator: " ")
            let log1NoId = log1Split[1...].joined(separator: " ")
            let log2NoId = log2Split[1...].joined(separator: " ")
            return log1NoId==log2NoId ? log1Split[0]<log2Split[0] : log1NoId < log2NoId
        }

        return letterLogs+digitLogs
    }
}
