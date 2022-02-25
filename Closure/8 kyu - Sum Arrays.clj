; https://www.codewars.com/kata/53dc54212259ed3d4f00071c/train/clojure
; My solution
(ns Sum)

(defn sum [a] (reduce + a))

; ...
(ns Sum)

(def sum (partial reduce +))

; ...
(ns Sum)

(defn sum [a] (apply + a))

; ...
(ns Sum)

(defn sum [a]
  (if (empty? a) 0 
    (+' (first a)
      (sum (rest a)))))

; ...
(ns Sum)
(require '[clojure.core.reducers :as r])

(defn sum [a] (r/fold + a))
