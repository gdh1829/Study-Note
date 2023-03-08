import org.assertj.core.api.Assertions
import org.junit.jupiter.api.Test

/**
 * 종이 자르기.
 * https://school.programmers.co.kr/learn/courses/30/lessons/120922
 */
class PaperCutting {
    /**
     * 세로컷 후에, 세로컷으로 늘어난 가로 페이퍼를 그 수만큼 다시 컷.
     */
    fun solution(M: Int, N: Int): Int {
        val verticalCuttingCount = M - 1
        val horizonCut = M * (N - 1)

        return verticalCuttingCount + horizonCut
    }

    @Test
    fun execute() {
        Assertions.assertThat(solution(2, 2)).isEqualTo(3)
        Assertions.assertThat(solution(2, 5)).isEqualTo(9)
        Assertions.assertThat(solution(1, 1)).isEqualTo(0)
    }
}
