package robin.codingtest.codingtest.leetcode

import org.assertj.core.api.Assertions
import org.junit.jupiter.api.Test

/**
 * https://leetcode.com/problems/letter-combinations-of-a-phone-number/
 */
class LetterCombinationsOfPhoneNumber {

    private val numAndLettersMapping = mapOf(
        "1" to arrayOf(),
        "2" to arrayOf("a", "b", "c"),
        "3" to arrayOf("d", "e", "f"),
        "4" to arrayOf("g", "h", "i"),
        "5" to arrayOf("j", "k", "l"),
        "6" to arrayOf("m", "n", "o"),
        "7" to arrayOf("p", "q", "r", "s"),
        "8" to arrayOf("t", "u", "v"),
        "9" to arrayOf("w", "x", "y", "z")
    )

    // 완전 탐색 조합.
    fun letterCombinations(digits: String): List<String> {
        if (digits.isEmpty()) {
            return emptyList()
        }

        var memo = mutableListOf<String>()
        digits.toCharArray().map { "$it" }.forEach { digit ->
            // 첫번째 digit의 문자 단순 append
            if (memo.isEmpty()) {
                numAndLettersMapping[digit]!!.forEach { memo.add(it) }
                return@forEach
            }

            // 첫번째 이후 이전 digit 알파벳 조합으로부터 새 digit 알파벳들과의 완전 탐색 조합 append
            val nextMemo = mutableListOf<String>()
            memo.forEach { m ->
                numAndLettersMapping[digit]!!.forEach { nextMemo.add(m + it) }
            }

            memo = nextMemo
        }

        return memo
    }

    @Test
    fun runTest() {
        Assertions.assertThat(letterCombinations("23"))
            .isEqualTo(listOf("ad","ae","af","bd","be","bf","cd","ce","cf"))

        Assertions.assertThat(letterCombinations(""))
            .isEqualTo(emptyList<String>())

        Assertions.assertThat(letterCombinations("2"))
            .isEqualTo(listOf("a", "b", "c"))
    }
}