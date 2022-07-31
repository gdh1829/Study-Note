package hello.aop

<<<<<<< Updated upstream
import hello.aop.order.OrderRepository
import hello.aop.order.OrderService
import hello.aop.order.aop.AspectV1
import hello.aop.order.aop.AspectV2
import org.assertj.core.api.Assertions
import org.junit.jupiter.api.DisplayName
import org.junit.jupiter.api.Test
import org.slf4j.LoggerFactory
import org.springframework.aop.support.AopUtils
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.boot.test.context.SpringBootTest
import org.springframework.context.annotation.Import

// @Import(AspectV1::class)
@Import(AspectV2::class)
@SpringBootTest
class AopTest {

    @Autowired
    private lateinit var orderService: OrderService

    @Autowired
    private lateinit var orderRepository: OrderRepository

    private val log = LoggerFactory.getLogger(AopTest::class.java)

    @DisplayName("aopInfo")
    @Test
    fun aopInfo() {
        log.info("isAopProxy, orderService=${AopUtils.isAopProxy(orderService)}")
        log.info("isAopProxy, orderRepository=${AopUtils.isAopProxy(orderRepository)}")
    }

    @DisplayName("success")
    @Test
    fun success() {
        orderService.orderItem("itemA")
    }

    @DisplayName("exception")
    @Test
    fun exception() {
        Assertions.assertThatThrownBy { orderService.orderItem("ex") }
            .isInstanceOf(IllegalArgumentException::class.java)
    }
=======
class AopTest {
>>>>>>> Stashed changes
}