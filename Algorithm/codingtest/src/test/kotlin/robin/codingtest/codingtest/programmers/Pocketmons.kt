package robin.codingtest.codingtest.programmers

import org.assertj.core.api.Assertions
import org.junit.jupiter.api.Test

/**
 * https://school.programmers.co.kr/learn/courses/30/lessons/1845
 * Level:1
 */
class Pocketmons {

    fun solution(nums: Array<Int>): Int {
        return nums.distinct().size.coerceAtMost(nums.size / 2)
    }

    @Test
    fun run() {
        Assertions.assertThat(solution(arrayOf(3, 1, 2, 3))).isEqualTo(2)
        Assertions.assertThat(solution(arrayOf(3, 3, 3, 2, 2, 4))).isEqualTo(3)
        Assertions.assertThat(solution(arrayOf(3, 3, 3, 2, 2, 2))).isEqualTo(2)
    }
}
