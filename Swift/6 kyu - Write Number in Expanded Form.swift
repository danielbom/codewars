// https://www.codewars.com/kata/write-number-in-expanded-form/train/swift
// My solution
func expandedForm(_ num: Int) -> String {
    if (num == 0) {
        return "0"
    }
    var sb: [String] = []
    var number = num
    for i in 0..<String(num).count {
        var k = number % 10
        number = Int(number / 10)
        if (k != 0) {
            var p = Int(pow(Double(10), Double(i)))
            sb.insert(String(k * p), at: 0)
        }
    }
    return sb.joined(separator: " + ")
}

// ...
func expandedForm(_ num: Int) -> String {
    let digits = String(num).characters
    let maxZeros = digits.count - 1
    
    let parts = digits
        .enumerated()
        .filter { $0.element != "0" }
        .map {
            String($0.element) +
            String(repeating: "0", count: maxZeros - $0.offset)
        }
    
    return parts.joined(separator: " + ")
}

// ...
func expandedForm(_ num: Int) -> String {
    let digits = String(num).characters
    return digits.enumerated()
        .flatMap { $1 == "0"
            ? nil
            : "\($1)" + String(
                    repeating: "0", count: digits.count - $0 - 1
                )
            }
            .joined(separator: " + ")
}
// ...

func expandedForm(_ num: Int) -> String {
    var result: [String] = []
    for (index, str) in "\(num)".characters.reversed().enumerated() {
        let res = (Int("\(str)") ?? 0) *
            Int(pow(10.0, Double(index) ?? 0))
        if res != 0 {
            result.append("\(res)")
        }
    }
    return result.reversed().joined(separator: " + ")
}