; https://www.codewars.com/kata/54dc6f5a224c26032800005c/train/clojure
; My solution
(ns bookseller.core
  (:require [clojure.string :as str] ))

(defn stock-list [list-of-books list-of-cat]
  (if (or (empty? list-of-cat) (empty? list-of-books)) [] 
    (let [category (first list-of-cat)]
    (concat
      [[category
        (reduce + 
        (map (comp read-string #(str/replace-first % #"^0*" "") #(nth % 1) #(str/split % #" "))
        (filter #(str/starts-with? % category)
        list-of-books)))]]
      (stock-list list-of-books (rest list-of-cat))))))

; ...
(ns bookseller.core
  (:require [clojure.string :as s]))

(defrecord Book [category stock])

(defn book [entry]
  (let [sp (s/split entry #" ")]
    (Book. (-> sp first first str)
           (-> sp second Integer/parseInt))))

(defn category? [category book]
  (= (:category book) category))

(defn stocks [category books]
  (->> books
       (filter (partial category? category))
       (map :stock)
       (reduce + 0)))

(defn stocks-by-category [categories books]
  (for [category categories]
    [category (stocks category books)]))

(defn stock-list [booklist categories]
  (if (every? seq [booklist categories])
    (stocks-by-category categories (map book booklist))
    (vector)))
