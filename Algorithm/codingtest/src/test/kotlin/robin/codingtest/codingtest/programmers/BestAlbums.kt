package robin.codingtest.codingtest.programmers

import org.junit.jupiter.api.Test

/**
 * https://school.programmers.co.kr/learn/courses/30/lessons/42579
 *
 * 개인평>
 * 같은 인덱스의 순서로 여럿으로 분리된 리스트에 대하여, 개별 리스트의 순환하면서 계산치를 쌓고 분류하는 것이 아닌
 * 그룹핑을 통해 하나의 리스트로 효율적으로 묶어 그 안에서 간단한 연산 과정을 통해 답을 만들어가야하는 문제.
 * 핵심은 두 리스트를 어떻게 그룹으로 묶어 연산을 이어가는지. key-value 맵에 대한 적극적 응용 필요.
 */
class BestAlbums {

    fun solution(genres: Array<String>, plays: IntArray): IntArray {
        val indicesByGenre = genres.indices.groupBy { genres[it] }
            .also { println("indicesByGenre: $it") }

        val genrePairList = indicesByGenre.toList()
            .also { println("genrePairList: $it") }

        val sortedByEachGenrePlayCountDesc = genrePairList
            .sortedByDescending { (genre, indices) -> indices.sumOf { plays[it] } }
            .also { println("sortedByEachGenrePlayCountDesc: $it") }

        val tookTopTwoOfEachGenre = sortedByEachGenrePlayCountDesc
            .map { it.second.sortedByDescending { plays[it] }.take(2) }
            .also { println("tookTopTwoOfEachGenre: $it") }

        return tookTopTwoOfEachGenre
            .flatten()
            .also { println("flatten: $it") }
            .toIntArray()
    }

    @Test
    fun run() {
        val result = solution(arrayOf("classic", "pop", "classic", "classic", "pop"), intArrayOf(500, 600, 150, 800, 2500))
        println(result)
    }
}
