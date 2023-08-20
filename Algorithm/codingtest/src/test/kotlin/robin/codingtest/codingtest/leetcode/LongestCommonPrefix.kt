package robin.codingtest.codingtest.leetcode

import org.assertj.core.api.Assertions
import org.junit.jupiter.api.Test

/**
 * https://leetcode.com/problems/longest-common-prefix/
 */
class LongestCommonPrefix {

    /**
     * time complexity O(N^M) 200ms
     * 매칭된다는 전제로 char를 입력 후 비교 대상과 매칭되지 않는 경우 가장 최신 appended char를 제거 후 반환.
     */
    fun solution_a(strs: Array<String>): String {
        var result = ""
        val target = strs.first()
        val criteria = strs.drop(1)

        target.forEachIndexed { index, c ->
            result += c

            criteria.forEach { str ->
                if (str.getOrNull(index) != c) {
                    result = result.dropLast(1)
                    return result
                }
            }
        }

        return result
    }

    /**
     * time complexity O(Log(N) + M) 179ms
     * 정렬 후 첫번째와 마지막 element만 비교한다.
     * 문자열은 알파벳(사전순)으로 정렬되므로 중간 elements와는 비교가 불요하고 마지막 element와 비교만 하면 된다.
     * ex. flower, flow, flight -> flight, flow, flower. 즉 flight와 flower만 비교하면 common prefix를 찾을 수 있다.
     *
     * 참고로 Kotlin에서는 내장함수로 CharSequence.commonPrefixWith(other: CharSequence, ignoreCase: Boolean = false): String을 지원한다.
     */
    fun solution_b(strs: Array<String>): String {
        strs.sort()
        val first = strs.first()
        val last = strs.last()

        var result = ""
        first.forEachIndexed { index, c ->
            if (last.getOrNull(index) != c) {
                return result
            }

            result += c
        }

        return result
    }

    @Test
    fun execution() {
        // Assertions.assertThat(solution_a(arrayOf("flower","flow","flight"))).isEqualTo("fl")
        // Assertions.assertThat(solution_a(arrayOf("dog","racecar","car"))).isEqualTo("")
        // Assertions.assertThat(solution_a(arrayOf("cir","car"))).isEqualTo("c")

        Assertions.assertThat(solution_b(arrayOf("flower","flow","flight"))).isEqualTo("fl")
        Assertions.assertThat(solution_b(arrayOf("dog","racecar","car"))).isEqualTo("")
        Assertions.assertThat(solution_b(arrayOf("cir","car"))).isEqualTo("c")
    }
}