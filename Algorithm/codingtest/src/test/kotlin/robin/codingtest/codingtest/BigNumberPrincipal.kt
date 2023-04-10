import org.assertj.core.api.Assertions
import org.junit.jupiter.api.Test

/**
 * 큰 수의 법칙.
 * numbers array가 주어지고, 최대 M 횟수만큼 더하여 가장 큰 수를 만들어라.
 * 단, 배열의 특정한 인덱에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 특징.
 * 서로 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른 것으로 간주.
 * 시간 제한 1초.
 *
 * N(2 <= N <= 1000), M(1 <= N <= 10000), K(1 <= K <= 10000)
 */
class BigNumberPrincipal {

    fun solution_v1(numbers: IntArray, N: Int, M: Int, K: Int): Int {
        val (firstBig, secondBig) = numbers.sortedDescending().let { Pair(it.component1(), it.component2()) }
        val total = mutableListOf<Int>()

        while (true) {
            repeat(K) {
                if (total.size >= M) {
                    return@repeat
                }
                total.add(firstBig)
            }

            if (total.size >= M) {
                break
            }
            total.add(secondBig)
        }

        return total.sum()
    }

    /**
     * M이 100억 이상인 경우, v1의 방식은 시간초과이므로 개선 버전 v2.
     */
    fun solution_v2(numbers: IntArray, N: Int, M: Int, K: Int): Int {
        val (firstBig, secondBig) = numbers.sortedDescending().let { Pair(it.component1(), it.component2()) }

        // 가장 큰 수가 더해지는 횟수
        var plusableCount = (M / (K + 1)) * K
        plusableCount += M % (K + 1)

        var result = 0
        // 가장 큰 수 더하기
        result += plusableCount * firstBig
        // 두번째로 큰 수 더하기
        result += (M - plusableCount) * secondBig

        return result
    }

    @Test
    fun execute() {
        Assertions.assertThat(solution_v1(intArrayOf(2, 4, 5, 4, 6), 5, 8, 3)).isEqualTo(46)
        Assertions.assertThat(solution_v2(intArrayOf(2, 4, 5, 4, 6), 5, 8, 3)).isEqualTo(46)
    }
}
