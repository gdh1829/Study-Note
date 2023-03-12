import org.assertj.core.api.Assertions
import org.junit.jupiter.api.Test

/**
 * 다음에 올 숫자.
 * https://school.programmers.co.kr/learn/courses/30/lessons/120924
 */
class NextNumber {
    /**
     * 등차수열과 등비수열의 특징 이용.
     */
    fun solution(common: IntArray): Int {
        val first = common.first()
        val second = common.component2()

        return if (isArithmeticSequence(common)) {
            common.last() + (second - first)
        } else  {
            common.last() * (second / first)
        }
    }

    private fun isArithmeticSequence(sequence: IntArray): Boolean =
        // 문제에서 common의 길이 3 이상을 보장하므로.
        sequence.first() - sequence.component2() == sequence.component2() - sequence.component3()

    @Test
    fun execute() {
        Assertions.assertThat(solution(intArrayOf(1, 2, 3, 4))).isEqualTo(5)
        Assertions.assertThat(solution(intArrayOf(2, 4, 8))).isEqualTo(16)
    }
}
