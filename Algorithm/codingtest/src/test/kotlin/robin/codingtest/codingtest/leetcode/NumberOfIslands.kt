package robin.codingtest.codingtest.leetcode

import org.assertj.core.api.Assertions
import org.junit.jupiter.api.Test

/**
 * https://leetcode.com/problems/number-of-islands/
 *
 * 그래프탐색: DFS
 */
class NumberOfIslands {

    fun solution(grid: Array<CharArray>): Int {
        val xSize = grid.size
        val ySize = grid.first().size

        fun checkIfIsland(x:Int, y:Int, grid: Array<CharArray>): Boolean {
            // 좌표 범위 초과
            if (x < 0 || x >= xSize || y < 0 || y >= ySize) {
                return false
            }

            if (grid[x][y] == '0') {
                return false
            }

            // 방문 처리
            grid[x][y] = '0'

            checkIfIsland(x+1, y, grid)
            checkIfIsland(x-1, y, grid)
            checkIfIsland(x, y+1, grid)
            checkIfIsland(x, y-1, grid)

            return true
        }

        var count = 0
        for (x in grid.indices) {
            for (y in grid.first().indices) {
                if (checkIfIsland(x, y, grid)) {
                    count++
                }
            }
        }

        return count
    }

    /**
     * 1 is land
     * 0 is sea
     *
     * 연결되어 있는 1 덩어리의 수.
     */
    @Test
    fun doTest() {
        val tc1 = arrayOf(
            charArrayOf('1','1','1','1','0'),
            charArrayOf('1','1','0','1','0'),
            charArrayOf('1','1','0','0','0'),
            charArrayOf('0','0','0','0','0')
        )
        Assertions.assertThat(solution(tc1)).isEqualTo(1)

        val tc2 = arrayOf(
            charArrayOf('1','1','0','0','0'),
            charArrayOf('1','1','0','0','0'),
            charArrayOf('0','0','1','0','0'),
            charArrayOf('0','0','0','1','1')
        )
        Assertions.assertThat(solution(tc2)).isEqualTo(3)

        val tc3 = arrayOf(
            charArrayOf('1','1','1'),
            charArrayOf('0','1','0'),
            charArrayOf('1','1','1')
        )
        Assertions.assertThat(solution(tc3)).isEqualTo(1)
    }
}