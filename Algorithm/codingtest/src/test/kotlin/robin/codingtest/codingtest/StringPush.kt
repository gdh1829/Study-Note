import org.assertj.core.api.Assertions
import org.junit.jupiter.api.Test

/**
 * 문자열 밀기.
 * https://school.programmers.co.kr/learn/courses/30/lessons/120921
 */
class StringPush {
    /**
     * A의 첫 letter가 시작되는 B의 index를 먼저 서치 후,
     * 서치된 시작점들을 내에서 가장 먼저 발견되는 동일 지점을 찾아 얼리 리턴.
     */
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
                    result = move
                    false
                } else {
                    true
                }
            }

        return result
    }

    /**
     * StringBuilder를 이용하여, 한번씩 letter를 이동시켜 동일시 되는 지점을 찾아 얼리 리턴.
     * Good) StringBuilder라는 적절한 클래스를 이용하여 문자열 내에서의 이동이 아주 간결해졌다.
     */
    fun solution_ver2(A: String, B: String): Int {
        if (A ==  B) return 0

        val sb = StringBuilder(A)
        for (index in B.indices) {
            sb.insert(0, sb[sb.length - 1])
            sb.deleteCharAt(sb.length - 1)
            if (sb.toString() == B) return index + 1
        }

        return -1
    }

    /**
     * 문제의 조건을 100% 활용한 초심플 솔루션..
     */
    fun solution_ver3(A: String, B: String): Int {
        return (B + B).indexOf(A)
    }

    @Test
    fun execute() {
        Assertions.assertThat(solution("hello", "ohell")).isEqualTo(1)
        Assertions.assertThat(solution("apple", "elppa")).isEqualTo(-1)
        Assertions.assertThat(solution("atat", "tata")).isEqualTo(1)
        Assertions.assertThat(solution("abc", "abc")).isEqualTo(0)
        Assertions.assertThat(solution("apaph", "aphap")).isEqualTo(3)

        Assertions.assertThat(solution_ver2("hello", "ohell")).isEqualTo(1)
        Assertions.assertThat(solution_ver2("apple", "elppa")).isEqualTo(-1)
        Assertions.assertThat(solution_ver2("atat", "tata")).isEqualTo(1)
        Assertions.assertThat(solution_ver2("abc", "abc")).isEqualTo(0)
        Assertions.assertThat(solution_ver2("apaph", "aphap")).isEqualTo(3)

        Assertions.assertThat(solution_ver3("hello", "ohell")).isEqualTo(1)
        Assertions.assertThat(solution_ver3("apple", "elppa")).isEqualTo(-1)
        Assertions.assertThat(solution_ver3("atat", "tata")).isEqualTo(1)
        Assertions.assertThat(solution_ver3("abc", "abc")).isEqualTo(0)
        Assertions.assertThat(solution_ver3("apaph", "aphap")).isEqualTo(3)
    }
}
