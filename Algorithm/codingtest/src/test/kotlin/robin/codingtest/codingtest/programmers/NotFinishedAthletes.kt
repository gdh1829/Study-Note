package robin.codingtest.codingtest.programmers

import org.assertj.core.api.Assertions
import org.junit.jupiter.api.Test

/**
 * https://school.programmers.co.kr/learn/courses/30/lessons/42576
 * Level:2
 */
class NotFinishedAthletes {

    fun solution(participant: Array<String>, completion: Array<String>): String {
        val completerAgg = completion.groupingBy { it }.eachCount().toMutableMap()

        participant.forEach { p ->
            completerAgg[p] = completerAgg[p]?.takeIf { it > 0 }?.minus(1) ?: return p
        }

        return ""
    }

    @Test
    fun run() {
        Assertions.assertThat(solution(arrayOf("leo", "kiki", "eden"), arrayOf("eden", "kiki"))).isEqualTo("leo")
        Assertions.assertThat(solution(arrayOf("marina", "josipa", "nikola", "vinko", "filipa"), arrayOf("josipa", "filipa", "marina", "nikola"))).isEqualTo("vinko")
        Assertions.assertThat(solution(arrayOf("mislav", "stanko", "mislav", "ana"), arrayOf("stanko", "ana", "mislav"))).isEqualTo("mislav")
    }
}
