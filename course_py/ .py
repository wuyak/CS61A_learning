(define (check expr)
  (list 'if expr ''passed
        (list 'quote (list 'failed: expr))))
