/**
 * A로 B 만들기.
 * https://school.programmers.co.kr/learn/courses/30/lessons/120886
 */
fun solution(before: String, after: String): Int {
    var tmp = before
    after.forEach { tmp = tmp.replaceFirst("$it", "") }

    return tmp.takeIf { it.isBlank() }?.let { 1 } ?: 0
}

solution("olleh", "hello").also { println(it == 1) }
solution("allpe", "apple").also { println(it == 0) }

/** 개선 솔루션. */
fun solution2(before: String, after: String): Int {
    return if (before.toList().sorted() == after.toList().sorted()) 1 else 0
}

solution2("olleh", "hello").also { println(it == 1) }
solution2("allpe", "apple").also { println(it == 0) }
