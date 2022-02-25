; https://www.codewars.com/kata/57a0e5c372292dd76d000d7e/train/clojure
; My solution
(ns clojure.string-repeat)

(defn repeat-str [n string]
  (if (<= n 1) string
    (apply str
      (concat [string]
        (repeat-str (- n 1) string)))))

; ...
(ns clojure.string-repeat)

(defn repeat-str [n s]
  (apply str (repeat n s)))

; ...
(ns clojure.string-repeat)

(defn repeat-str [n strng]
  (loop [count n s strng]
    (if (= count 1) s
      (recur (dec count) (str s strng)))))

; ...
(ns clojure.string-repeat)

(def repeat-str #(apply str (repeat %1 %2)))

; ...
(ns clojure.string-repeat
  (require [clojure.string :as string]))

(def repeat-str (comp string/join repeat))

; ...
(ns clojure.string-repeat)

(defn repeat-str [n strng]
  (reduce str 
    (take n
      (repeat strng))))

; ...
(ns clojure.string-repeat)

(defn repeat-str [n strng]
  (if (== n 0) ""
    (str strng
      (repeat-str (- n 1) strng))))
