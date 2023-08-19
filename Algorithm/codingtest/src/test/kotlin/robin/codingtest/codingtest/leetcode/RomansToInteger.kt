package robin.codingtest.codingtest.leetcode

import org.assertj.core.api.Assertions
import org.junit.jupiter.api.Test

/**
 * https://leetcode.com/problems/roman-to-integer/
 */
class RomansToInteger {

    /**
     * time complexity O(N + 6) 334ms
     * 제한된 예외 케이스를 치환 후 합계 계산.
     */
    fun romanToInt_A(s: String): Int {
        var input = s + ""
        val dict = mapOf('I' to 1, 'V' to 5, 'X' to 10, 'L' to 50, 'C' to 100, 'D' to 500, 'M' to 1000)
        val exceptions = mapOf(
            "IV" to "IIII", "IX" to "VIIII", "XL" to "XXXX", "XC" to "LXXXX", "CD" to "CCCC", "CM" to "DCCCC"
        )

        exceptions.forEach { (k, v) -> input = input.replace(k, v) }

        return input.sumOf { dict.getOrDefault(it, 0) }
    }

    /**
     * time complexity O(N) 210ms
     * subtraction을 발생시키는 I,X,C인 경우, 다음 char를 확인하여 subraction에 해당시 자기 자신만큼 마이너스하며
     * 한 번의 순환 과정에서 보합을 일으킬 수 있도록 한다.
     */
    fun romanToInt_B(s: String): Int {
        return s.mapIndexed { index, c ->
            when (c) {
                'I' -> if ("VX".contains(s.getOrNull(index+1) ?: '_')) -1 else 1
                'V' -> 5
                'X' -> if ("LC".contains(s.getOrNull(index+1) ?: '_')) -10 else 10
                'L' -> 50
                'C' -> if ("DM".contains(s.getOrNull(index+1) ?: '_')) -100 else 100
                'D' -> 500
                'M' -> 1000
                else -> 0
            }
        }.sum()
    }

    @Test
    fun execute() {
        Assertions.assertThat(romanToInt_B("LVIII")).isEqualTo(58)
        Assertions.assertThat(romanToInt_B("MCMXCIV")).isEqualTo(1994)
        Assertions.assertThat(romanToInt_B("IX")).isEqualTo(9)
    }
}