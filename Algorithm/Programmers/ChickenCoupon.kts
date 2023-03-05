// 치킨 쿠폰
// https://school.programmers.co.kr/learn/courses/30/lessons/120884

fun main() {
    fun solution(chicken: Int): Int {
        val freeChickenCriterion = 10
        var freeChickens = chicken / freeChickenCriterion
        var coupons = freeChickens + (chicken % freeChickenCriterion)
        while (true) {
            // 남은 쿠폰으로 무료 치킨 추가 주문 가능 여부.
            if (coupons < freeChickenCriterion) {
                break
            }

            val newChickens = coupons / freeChickenCriterion
            // 남은 쿠폰으로 추가 주문시 보완되는 남은 쿠폰.
            coupons = (newChickens + coupons % freeChickenCriterion)
            freeChickens += newChickens
        }

        return freeChickens
    }

    // 재귀풀이.
    fun solution2(chicken: Int): Int {
        return if (chicken < 10) 0 else chicken / 10 + solution2(chicken / 10 + chicken % 10)
    }

    println(solution(100) == 11)
    println(solution(1081) == 120)

    println(solution2(100) == 11)
    println(solution2(1081) == 120)
}

main()
