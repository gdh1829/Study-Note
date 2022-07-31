package hello.aop.order.aop

import org.aspectj.lang.ProceedingJoinPoint
import org.aspectj.lang.annotation.Around
import org.aspectj.lang.annotation.Aspect
import org.slf4j.LoggerFactory

@Aspect
class AspectV1 {

    private val log = LoggerFactory.getLogger(AspectV1::class.java)

    @Around("execution(* hello.aop.order..*(..))")
    fun doLog(joinPoint: ProceedingJoinPoint): Any? {
        log.info("[log] ${joinPoint.signature}")
        return joinPoint.proceed()
    }
}