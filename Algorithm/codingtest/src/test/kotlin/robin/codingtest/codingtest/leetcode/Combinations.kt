package robin.codingtest.codingtest.leetcode

import org.assertj.core.api.Assertions
import org.junit.jupiter.api.Test
import java.util.Deque

/**
 * https://leetcode.com/problems/combinations/
 */
class Combinations {

    fun combine(n: Int, k: Int): List<List<Int>> {
        val result = mutableListOf<List<Int>>()

        /**
         * @param elements 조합
         * @param start 시작숫자
         * @param k 조합을 위해 앞으로 필요한 숫자 수
         */
        fun dfs(elements: MutableList<Int>, start: Int, k: Int) {
//            println("start $start, k $k, elements: $elements")

            // 조합의 개수 만족시, 결과 저장
            if (k == 0) {
//                println("add result: $elements")
                result.add(elements.toList())
                return
            }

            // 1~N까지의 숫자 중 앞서 쓰인 숫자를 제외하고 다음 숫자부터 재귀 1~N -> 2~N -> 3~N ... (N-1)~N 재귀.
            // K 남은 추가적 필요 숫자 개수.
            for (num in IntRange(start, n)) {
                elements.add(num)
                dfs(elements, num + 1, k - 1)
                // 리프 노드 방문 후 1노드 백트랙
                elements.removeLast()
            }
        }

        dfs(mutableListOf(), 1, k)

        return result
    }

    @Test
    fun run() {
        Assertions.assertThat(combine(4, 2))
            .isEqualTo(
                listOf(
                    listOf(1,2),listOf(1,3),listOf(1,4),
                    listOf(2,3),listOf(2,4),listOf(3,4)
                )
            )

        Assertions.assertThat(combine(1, 1))
            .isEqualTo(listOf(listOf(1)))

        Assertions.assertThat(combine(5, 3))
            .isEqualTo(
                listOf(
                    listOf(1,2,3),listOf(1,2,4),listOf(1,2,5),
                    listOf(1,3,4),listOf(1,3,5),listOf(1,4,5),
                    listOf(2,3,4),listOf(2,3,5),listOf(2,4,5),
                    listOf(3,4,5)
                )
            )
    }
}
