import org.assertj.core.api.Assertions
import org.junit.jupiter.api.Test

/**
 * 연속된 수의 함.
 * https://school.programmers.co.kr/learn/courses/30/lessons/120923
 */
class SumOfSequence {
    /**
     * 슬라이딩윈도우 활용.
     */
    fun solution(num: Int, total: Int): IntArray {
        // 연속된 수의 합이므로 불필요한 탐색 범위를 제거하기 위한 근접 시작점.
        val mid = total / num

        // 더 큰 수일 가능성은 없으므로 작은수로 범위를 좁혀 슬라이딩 윈도우 탐색.
        val deque = ArrayDeque((mid until mid + num).toSet().reversed())
        while (deque.isNotEmpty()) {
            if (deque.sum() == total) {
                return deque.sorted().toIntArray()
            }

            deque.removeFirst()
            deque.addLast(deque.last() - 1)
        }

        return intArrayOf()
    }

    @Test
    fun execute_solution() {
        Assertions.assertThat(solution(3, 12)).isEqualTo(intArrayOf(3, 4, 5))
        Assertions.assertThat(solution(5, 15)).isEqualTo(intArrayOf(1, 2, 3, 4, 5))
        Assertions.assertThat(solution(4, 14)).isEqualTo(intArrayOf(2, 3, 4, 5))
        Assertions.assertThat(solution(5, 5)).isEqualTo(intArrayOf(-1, 0, 1, 2, 3))
        Assertions.assertThat(solution(1, 10)).isEqualTo(intArrayOf(10))
        Assertions.assertThat(solution(3, -3)).isEqualTo(intArrayOf(-2, -1, 0))
        Assertions.assertThat(solution(3, 21)).isEqualTo(intArrayOf(6, 7, 8))
    }
}
