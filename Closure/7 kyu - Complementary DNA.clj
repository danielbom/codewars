; https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/clojure
; My solution
(ns complementary-dna)

(defn dna-compl [base]
  (if (= base "A") "T"
  (if (= base "T") "A"
  (if (= base "G") "C"
  (if (= base "C") "G" "")))))

(defn dna-strand [dna]
  (apply str
    (map (comp dna-compl str) dna)))

; ...
(ns complementary-dna)

(defn dna-strand [dna]
    (apply str (map {\A \T \C \G \G \C \T \A} dna)))

; ...
(ns complementary-dna)

(require '[clojure.string :refer [replace]])

(defn dna-strand [dna]
  (replace dna #"\S" {"A" "T" "C" "G" "T" "A" "G" "C"}))

; ...
(ns complementary-dna)

(defn dna-strand [dna]
  (apply str (map #(case % \A \T \T \A \C \G \G \C) dna)))

; ...
(ns complementary-dna
  (:require [clojure.string :as string]))

(defn dna-strand [n]
  (string/join (replace {"A" "T", "T" "A", "C" "G", "G", "C"}
                        (string/split n #""))))

; ...
