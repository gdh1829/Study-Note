package robin.codingtest.codingtest.programmers

import org.assertj.core.api.Assertions
import org.junit.jupiter.api.Test

/**
 * https://school.programmers.co.kr/learn/courses/30/lessons/42578?language=kotlin
 */
class ClothesCombination {

    /**
     * 조합의 수만 파악하면 되는 문제.
     */
    fun solution(clothes: List<List<String>>): Int {
        return clothes.groupBy { it[1] } // 신체 부위별 재묶음 처리.
            .also { println("groupBy => $it") }
            .values   // 불필요한 부위를 나타내는 키 날리기
            .also { println("values => $it") }
            .map { it.size + 1 }  // 각 파츠별 옷 개수와 선택하지 않았을 경우 포함
            .also { println("map => $it") }
            .reduce(Int::times)   // 각 신체 부위별 개수 조합
            .also { println("times => $it") }
            .minus(1)  // 모든 신체 부위에서 선택하지 않았을 경우 제외.
            .also { println("minus => $it") }
    }

    @Test
    fun run() {
        val case1 = listOf(listOf("yellow_hat", "headgear"), listOf("blue_sunglasses", "eyewear"), listOf("green_turban", "headgear"))
        val case2 = listOf(listOf("crow_mask", "face"), listOf("crow_mask", "face"), listOf("smoky_makeup", "face"))

        Assertions.assertThat(solution(case1)).isEqualTo(5)
        Assertions.assertThat(solution(case2)).isEqualTo(3)
    }
}