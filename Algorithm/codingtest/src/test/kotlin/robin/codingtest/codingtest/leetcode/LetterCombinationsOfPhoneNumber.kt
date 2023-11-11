package robin.codingtest.codingtest.leetcode

import org.assertj.core.api.Assertions
import org.junit.jupiter.api.Test

/**
 * https://leetcode.com/problems/letter-combinations-of-a-phone-number/
 *
 * leet code 성능 테스트시,
 * 버전1(173ms)이 버전2(205ms)보다 성능이 더 좋았고, 메모리 차이는 1mb 정도.
 * 성능은 떨어지나 dfs+backtracking 조합의 코드가 더 완성도 있어보인다.
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

    // DFS + 백트래킹 활용
    // dfs로서 자릿수의 가장 깊숙히 N자리까지 들어가 순환하며 N-1로 거꾸로 거슬러 올라오면 자릿수가 맞을때마다 output을 result에 넣게된다.
    fun letterCombinationsVer2(digits: String): List<String> {
        val result = mutableListOf<String>()

        fun dfs(index: Int, path: String) {
            println("1. dfs: index $index, path $path")
            // 입력 자리수만큼 문자열 조합 확보 완료 => DFS 끝까지 탐색 완료, 백트래킹
            if (path.length == digits.length) {
                result.add(path)
                println("1. add result: $path")
                return
            }

            // 입력한 자릿수 단위 반복
            for (i in (index until digits.length)) {
                for (j in numAndLettersMapping["${digits[i]}"]!!) {
                    println("i: $i, j: $j")
                    dfs(i + 1, path + j)
                }
            }
        }

        if (digits.isBlank()) {
            return emptyList()
        }

        dfs(0, "")

        return result
    }

    @Test
    fun runVersion1() {
        Assertions.assertThat(letterCombinations("23"))
            .isEqualTo(listOf("ad","ae","af","bd","be","bf","cd","ce","cf"))

        Assertions.assertThat(letterCombinations(""))
            .isEqualTo(emptyList<String>())

        Assertions.assertThat(letterCombinations("2"))
            .isEqualTo(listOf("a", "b", "c"))
    }

    @Test
    fun runVersion2() {
        Assertions.assertThat(letterCombinationsVer2("23"))
            .isEqualTo(listOf("ad","ae","af","bd","be","bf","cd","ce","cf"))

        Assertions.assertThat(letterCombinationsVer2(""))
            .isEqualTo(emptyList<String>())

        Assertions.assertThat(letterCombinationsVer2("2"))
            .isEqualTo(listOf("a", "b", "c"))
    }
}
