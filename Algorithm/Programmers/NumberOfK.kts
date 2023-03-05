/**
 * K의 개수.
 * https://school.programmers.co.kr/learn/courses/30/lessons/120887
 */
fun solution(i: Int, j: Int, k: Int): Int {
    return (i..j).sumOf { num -> "$num".toCharArray().count { it.digitToInt() == k } }
}

solution(1, 13, 1).also { println(it) }.also { check(it == 6) }
solution(10, 50, 5).also { println(it) }.also { check(it == 5) }
solution(3, 10, 2).also { println(it) }.also { check(it == 0) }

/**
 * 개선 솔루션.
 *
 * k의 자릿수가 1자리로 고정이며 한자리수 개별 숫자의 카운트이므로,
 * solution과 같이 별도 계산할 필요가 없어 모든 숫자를 하나로 합쳐 카운트만 새어주면 되었다.
 */
fun solution2(i: Int, j: Int, k: Int): Int {
    return (i..j).joinToString("").count { it.digitToInt() == k }
}

solution2(1, 13, 1).also { println(it) }.also { check(it == 6) }
solution2(10, 50, 5).also { println(it) }.also { check(it == 5) }
solution2(3, 10, 2).also { println(it) }.also { check(it == 0) }
