package robin.codingtest.codingtest.leetcode

import org.assertj.core.api.Assertions
import org.junit.jupiter.api.Test
import java.util.Deque

/**
 * https://leetcode.com/problems/combination-sum/
 */
class CombinationSum {

    fun combinationSum(candidates: IntArray, target: Int): List<List<Int>> {
        val result = mutableListOf<List<Int>>()

        fun dfs(targetSum: Int, index: Int, path: MutableList<Int>) {
            if (targetSum < 0) {
                return
            }

            if (targetSum == 0) {
                result.add(path.toList())
                return
            }

            for (i in (index until candidates.size)) {
                path.add(candidates[i])
                dfs(targetSum - candidates[i], i, path)
                path.removeLastOrNull()
            }
        }

        dfs(target, 0, mutableListOf())

        return result
    }

    @Test
    fun run() {
        Assertions.assertThat(combinationSum(intArrayOf(2,3,6,7), 7))
            .isEqualTo(listOf(listOf(2,2,3), listOf(7)))

        Assertions.assertThat(combinationSum(intArrayOf(2,3,5), 8))
            .isEqualTo(listOf(listOf(2,2,2,2), listOf(2,3,3), listOf(3,5)))

        Assertions.assertThat(combinationSum(intArrayOf(2), 1))
            .isEqualTo(emptyList<Int>())
    }
}
