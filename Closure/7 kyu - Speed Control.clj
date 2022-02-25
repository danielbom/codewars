; https://www.codewars.com/kata/56484848ba95170a8000004d/train/clojure
; My solution
(ns gps.core)

(defn gps [seconds [f & r]]
  (if (empty? r) 0
    (max (gps seconds r)
      (int (quot (* 3600 (- (first r) f)) seconds)))))

; ...
(ns gps.core)

(defn gps [s x]
  (->> (partition 2 1 x)
    (map (fn [[p c]] (- c p)))
    (map #(* % 3600.0))
    (map #(/ % s))
    (reduce max 0)
    long))

; ...
(ns gps.core)

(defn gps [s x]
  (->> (partition 2 1 x)
       (map (fn [[x y]] (/ (* 3600 (- y x)) s)))
       (reduce max 0)
       int))

; ...
(ns gps.core)

(defn gps [s x]
  (if (< 1 (count x))
    (let [hourly-speed #(/ (* 3600 %) s)
          distances (map - (rest x) x)
          speeds (map hourly-speed distances)
          max-speed (apply max speeds)]
      (int max-speed))
    0))

; ...
(ns gps.core)

(defn gps [s x]
  (if (<= (count x) 1)
    0
    (int (apply max (map #(/ (* % 3600) (float s)) (map - (rest x) x))))))

; ...
(ns gps.core)

(defn gps [s x]
  (if (> 0 (count x)) 0
    (let [hourly-speed #(/ (* 3600 %) s)
          distances (map - (rest x) x)
          speeds (map hourly-speed distances)
          max-speed (apply max speeds)]
      (int max-speed))))

; ...
(ns gps.core)

(defn gps [time-interval distances]
 (if (< (count distances) 2)
   0
   (let [distance-pairs (partition 2 (interleave (rest distances) (butlast distances)))
         pairwise-difference (fn [[a b]] (- a b))
         distances-per-interval (map pairwise-difference distance-pairs)
         seconds-in-an-hour 3600
         distance->velocity (fn [d] (/ (* seconds-in-an-hour d) time-interval))
         avg-velocities (map distance->velocity distances-per-interval)
         largest-avg-velocity (apply max avg-velocities)]
     (int largest-avg-velocity))))
