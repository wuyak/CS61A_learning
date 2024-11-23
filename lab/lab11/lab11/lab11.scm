(define (if-program condition if-true if-false)
  `(if ,condition ,if-true ,if-false))

(define (square n) (* n n))

(define (pow-expr base exp)
    (cond ((= base 0) 0)
          ((= exp 0) 1)
          ((= (remainder exp 2) 0) `(square ,(pow-expr base (quotient exp 2))))
          (else `(* ,base ,(pow-expr base (- exp 1))))))

(define-macro (repeat n expr)
  `(repeated-call ,n (lambda () ,expr)))

; Call zero-argument procedure f n times and return the final result.
(define (repeated-call n f)
  (if (> n 0)
      (begin (f) (repeated-call (- n 1) f))))
