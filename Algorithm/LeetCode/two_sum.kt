/**
 * https://leetcode.com/problems/two-sum/
 */
class Solution {
    /**
     * time complexity O(n^2)
     */
    fun twoSum_solution_a(nums: IntArray, target: Int): IntArray {
        val result = IntArray(2)
        for (leftPoint in nums.indices) {
            for (rightPoint in IntRange(leftPoint + 1, nums.lastIndex))
                if ((nums[leftPoint] + nums[rightPoint]) == target) {
                    result[0] = leftPoint
                    result[1] = rightPoint
                    break
                }
        }
        return result
    }

    /**
     * time complexity O(n)
     * 어레이 인덱스가 이동하면서 타겟 숫자에 대하여 현재 자신의 숫자의 차를 갖는 수가 지나온 길에 있었는지 함께 체크하는 방법.
     * 솔루션 a 대비 한 번의 루프로 해결이 가능.
     */
    fun twoSum_solution_b(nums: IntArray, target: Int): IntArray {
        val result = IntArray(2)
        
        val map = mutableMapOf<Int, Int>()
        for (index in nums.indices) {
            val complement = target - nums[index]
            
            if (map.containsKey(complement)) {
                result[0] = index
                result[1] = map[complement]!!
                return result
            }
            map.put(nums[index], index)
        }
        return result
    }

    /**
     * time complexity O(n)
     * 솔루션b 대비 코틀린 함수를 이용하여 더욱 간결하게.
     */
    fun twoSum_solution_c(nums: IntArray, target: Int): IntArray {
        val diffMap = mutableMapOf<Int, Int>()

        nums.forEachIndexed { index, num ->
            diffMap[num]?.run { return intArrayOf(diffMap[num], index) }
            diffMap[target - num] = index
        }

        return intArrayOf()
    }
}
