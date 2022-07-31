package hello.aop.order

import org.slf4j.LoggerFactory
import org.springframework.stereotype.Service

@Service
class OrderService(
    private val orderRepository: OrderRepository
) {
    private val log = LoggerFactory.getLogger(OrderService::class.java)

    fun orderItem(itemId: String) {
        log.info("[orderService] executed.")
        orderRepository.save(itemId)
    }
}