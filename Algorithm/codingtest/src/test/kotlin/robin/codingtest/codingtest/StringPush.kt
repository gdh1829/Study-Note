import org.assertj.core.api.Assertions
import org.junit.jupiter.api.Test

/**
 * 문자열 밀기.
 * https://school.programmers.co.kr/learn/courses/30/lessons/120921
 */
class StringPush {
    @Test
    fun execute() {
        Assertions.assertThat(solution("hello", "ohell")).isEqualTo(1)
        Assertions.assertThat(solution("apple", "elppa")).isEqualTo(-1)
        Assertions.assertThat(solution("atat", "tata")).isEqualTo(1)
        Assertions.assertThat(solution("abc", "abc")).isEqualTo(0)
        Assertions.assertThat(solution("apaph", "aphap")).isEqualTo(3)
    }

    fun solution(A: String, B: String): Int {
        var result = -1

        if (A == B) {
            return 0
        }

        B.mapIndexedNotNull { index, c -> if (c == A.first()) index else null }
            .takeWhile { move ->
                val arr = Array<String?>(A.length) { null }
                
                A.forEachIndexed { index, c ->
                    var loc = index + move
                    if (loc >= A.length) {
                        loc -= A.length
                    }
                    arr[loc] = "$c"
                }

                if (arr.filterNotNull().joinToString("") == B) {
                    println(arr.filterNotNull().joinToString(""))
                    result = move
                    false
                } else {
                    true
                }
            }

        return result
    }
}
