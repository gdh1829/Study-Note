package robin.codingtest.codingtest.leetcode

import org.assertj.core.api.Assertions
import org.junit.jupiter.api.Test
import java.util.Deque

/**
 * https://leetcode.com/problems/subsets/
 */
class Subsets {

    fun subsets(nums: IntArray): List<List<Int>> {
        val result = mutableListOf<List<Int>>()

        fun dfs(index: Int, path: MutableList<Int>) {
            result.add(path.toList())
            for (i in (index until nums.size)) {
                path.add(nums[i])
                dfs(i+1, path)
                path.removeLastOrNull()
            }
        }

        dfs(0, mutableListOf())

        // 경로보기
//        for (ele  in result) {
//            println(ele)
//        }

        return result
    }

    @Test
    fun run() {
        Assertions.assertThat(subsets(intArrayOf(1,2,3)))
            .containsExactlyInAnyOrderElementsOf(
                listOf(
                    emptyList(), listOf(1), listOf(2), listOf(1,2),
                    listOf(3), listOf(1,3), listOf(2,3), listOf(1,2,3)
                )
            )

        Assertions.assertThat(subsets(intArrayOf(0)))
            .containsExactlyInAnyOrderElementsOf(
                listOf(
                    emptyList(), listOf(0)
                )
            )
    }
}
