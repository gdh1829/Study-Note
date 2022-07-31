package hello.aop.order.aop

import org.aspectj.lang.ProceedingJoinPoint
import org.aspectj.lang.annotation.Around
import org.aspectj.lang.annotation.Aspect
import org.aspectj.lang.annotation.Pointcut
import org.slf4j.LoggerFactory

@Aspect
class AspectV2 {

    private val log = LoggerFactory.getLogger(AspectV2::class.java)

    // hello.aop.order 패키지와 하위 모든 패키지를 대상으로 한다.
    @Pointcut("execution(* hello.aop.order..*(..))")
    private fun doLogPointCut() {} // 포인트컷 시그니처라 함.

    @Around("doLogPointCut()")
    fun doLog(joinPoint: ProceedingJoinPoint): Any? {
        log.info("[log] ${joinPoint.signature}") // 조인포인트 시그니처
        return joinPoint.proceed()
    }
}