(defun fizzbuzz (limit)
  (loop for x from 1 to limit do
    (princ (cond ((zerop (mod x 15)) "FizzBuzz")
                 ((zerop (mod x 3))  "Fizz")
                 ((zerop (mod x 5))  "Buzz")
                 (t                  x)))
    (terpri)))
