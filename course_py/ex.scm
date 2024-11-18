(define (check expr)
  (list 'if expr ''passed
        (list 'quote (list 'failed: expr))))

(define (square-expr term) `(* ,term ,term))
`(+ ,(square-expr 'a), (square-expr 'b))

(define (twice expr)
              (list 'begin expr expr))

(define (map fn vals)
  (if (null? vals)
    ()
    (cons (fn (car vals))
          (map fn (cdr vals)))))

(define (for sym vals expr)
  `(map (lambda (,sym) ,expr) ',vals))

(for 'x '(2 3 4 5) '(* x x))
(eval (for 'x '(2 3 4 5) '(* x x)))

(define fact (lambda (n)
               (if (zero? n) 1
                 (* n (fact (- n 1))))))

(define-macro (twice expr)
  (list 'begin expr expr))

(define (trace expr)
  (define operator (car expr))
    `(begin
       (define original ,operator)
       (define ,operator (lambda (n)
                  (print (list ,operator n))
                  (original n)))
       (let result ,expr)
         (define ,operator original)
         result))


(eval (trace '(fact 5)))
(fact 5)
