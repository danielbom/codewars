; https://www.codewars.com/kata/50654ddff44f800200000004/train/clojure
; My solution
(ns multiply.bug.fix)

(defn multiply [a b] (* a b))

; ...
(ns multiply.bug.fix)

(def multiply *)

; ...
(ns multiply.bug.fix)

(defn multiply 
 "A simple multiplication test"
  [& args] (apply * args))

; ...
(ns multiply.bug.fix)

(defn multiply [& args]
  (reduce * args))

; ...
