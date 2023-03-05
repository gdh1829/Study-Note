import kotlin.math.pow

/**
 * 이진수 더하기.
 * https://school.programmers.co.kr/learn/courses/30/lessons/120885
 */
fun main() {
    /**
     * 십진수와 이진수 변환을 구현하여 해결하기.
     */
    fun solution(bin1: String, bin2: String): String {

        // 주어진 입력값을 십진수로 변환.
        fun toInt(bin: String, radix: Int =  2): Int {
            var result = 0.0
            bin.reversed().forEachIndexed { index, c -> result += ((radix.toDouble()).pow(index) * c.digitToInt()) }

            return result.toInt()
        }

        // 주어진 십진수를 이진수로 변환.
        fun toBin(decimal: Int): String {
            var result = ""
            var share = decimal

            do {
                result += share % 2
                share = share / 2
            } while (share > 0)

            return result.reversed()
        }

        return (toInt(bin1) + toInt(bin2)).let { toBin(it) }
    }

    /**
     * 코틀린 내장 함수를 사용하여 간단하게 해결하기.
     */
    fun solution2(bin1: String, bin2: String): String {
        return Integer.toBinaryString(bin1.toInt(2) + bin2.toInt(2))
    }

    println(solution("10", "11").also { println(it) }.let { it == "101" })
    println(solution("1001", "1111").also { println(it) }.let { it == "11000" })

    println(solution2("10", "11").also { println(it) }.let { it == "101" })
    println(solution2("1001", "1111").also { println(it) }.let { it == "11000" })
}

main()
