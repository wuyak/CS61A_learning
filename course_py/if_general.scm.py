"""
(begin
 (define (f x total)
  (if (< (* x x) 50)
   (f (+ x 1) (+ total x))
    total))
 (f 1 0))
"""

(define (sum-while initial-x condition  add_to_total update-x)
 ;      (sum-while  1       '(< (* x x) 50  'x      '(+ x 1)
`(begin
 (define (f x total)
  (if ,condition
   (f ,update-x (+ total ,add_to_total))
    total))
 (f initial-x 0)))
