package hello.aop.order

import lombok.extern.slf4j.Slf4j
import org.slf4j.LoggerFactory
import org.springframework.stereotype.Repository

@Slf4j
@Repository
class OrderRepository {

    private val log = LoggerFactory.getLogger(OrderRepository::class.java)

    fun save(itemId: String): String {
        log.info("[orderRepository] executed.")

        if (itemId == "ex")  {
            throw IllegalArgumentException("Ex is occurred.")
        }

        return "ok"
    }
}