/**
 * https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
 */
class Solution {
    /**
     * time complexity O(n^2)
     */
    fun maxProfit(prices: IntArray): Int {
        var result = 0

        var buyPrices = mutableListOf<Int>()
        for (sellDay in prices.indices) {
            if (sellDay > 0) {
                val profit = prices[sellDay] - buyPrices.min()!!

                if (result < profit) {
                    result = profit
                }
            }
            buyPrices.add(prices[sellDay])
        }

        return result
    }

    /**
     * time complexity O(n)
     */
    fun maxProfitV2(prices: IntArray): Int {
        var minPrice = Int.MAX_VALUE
        var maxProfit = 0

        for (index in prices.indices) {
            // 가장 낮은 값을 먼저 찾아보고
            if (prices[index] < minPrice) {
                minPrice = prices[index]
            // 그렇지 않을 경우 profit 비교
            } else if (prices[index] - minPrice > maxProfit) {
                maxProfit = prices[index] - minPrice
            }
        }

        return maxProfit
    }
}

println(Solution().maxProfit(intArrayOf(7,1,5,3,6,4)))
println(Solution().maxProfit(intArrayOf(7,6,4,3,1)))

println(Solution().maxProfitV2(intArrayOf(7,1,5,3,6,4)))
println(Solution().maxProfitV2(intArrayOf(7,6,4,3,1)))
