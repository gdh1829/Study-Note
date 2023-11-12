package robin.codingtest.codingtest.leetcode

import org.assertj.core.api.Assertions
import org.junit.jupiter.api.Test
import java.util.Deque

/**
 * https://leetcode.com/problems/permutations/
 *
 * 198ms
 */
class Permutations {

    fun permute(nums: IntArray): List<List<Int>> {
        val result = mutableListOf<List<Int>>()

        fun dfs(nums: MutableList<Int>, path: MutableList<Int> = mutableListOf()) {
            if (nums.isEmpty()) {
//            println("add result => $result")
                result.add(path.toList())
                return
            }

            for (num in nums) {
                // 선택 숫자 append
                path.add(num)

                // 선택된 숫자를 제거 후 남은 선택지 구성을 위한 딥카피.
                // 그렇지 않을 경우, nums looping 데이터를 수정하기 때문에 ConcurrentModificationEx.
                val copied = nums.toMutableList()
                copied.remove(num)

                dfs(copied, path)

                // dfs가 끝 N 리프노드에 다다르고 다시 이전 N-1 노드 path로 회귀.
                path.removeLast()
            }
        }

        dfs(nums.toMutableList())

        return result
    }

    @Test
    fun run() {
        Assertions.assertThat(permute(intArrayOf(1,2,3)))
            .isEqualTo(
                listOf(
                    listOf(1,2,3),listOf(1,3,2),listOf(2,1,3),
                    listOf(2,3,1),listOf(3,1,2),listOf(3,2,1)
                )
            )

        Assertions.assertThat(permute(intArrayOf(0,1)))
            .isEqualTo(listOf(listOf(0,1),listOf(1,0)))

        Assertions.assertThat(permute(intArrayOf(1)))
            .isEqualTo(listOf(listOf(1)))
    }
}
