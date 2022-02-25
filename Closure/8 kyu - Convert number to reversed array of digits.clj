; https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/clojure
; My solution
(ns digitizer.core)

(defn digitize [n]
  (if (< n 10) [n]
    (concat [(mod n 10)]
      (digitize (quot n 10)))))

; ...
(ns digitizer.core)

(defn digitize [n]
  (->> n
       str
       reverse
       (map #(Character/digit % 10))))

; ...
(ns digitizer.core)

(defn digitize [n]
  (reverse (map #(Integer/parseInt (str %)) (str n))))

; ...
(ns digitizer.core)

(defn digitize [n]
  (->> (str n)
       (reverse)
       (map str)
       (map read-string)))

; ...
(ns digitizer.core)

(defn char-to-int [c] (- (int c) (int \0)))

(defn digitize [n]
  (map char-to-int (reverse (str n))))

; ...
(ns digitizer.core)

(defn digitize [n] 
  (reverse 
    (for [x (str n)] (read-string (str x)))))
  