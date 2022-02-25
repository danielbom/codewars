; https://www.codewars.com/kata/5672a98bdbdd995fad00000f/train/clojure
; My solution
(ns rock-paper-scissors)

(defn rps-win [hand1 hand2]
  (or 
    (and (= hand1 "scissors") (= hand2 "paper"))
    (and (= hand1 "paper") (= hand2 "rock"))
    (and (= hand1 "rock") (= hand2 "scissors"))))

(defn rps [p1 p2]
  (if (rps-win p1 p2) "Player 1 won!"
  (if (rps-win p2 p1) "Player 2 won!" "Draw!")))

; And
(ns rock-paper-scissors)

(defn rps [p1 p2]
  (let [oppos-win-move {"scissors" "paper", "paper" "rock", "rock" "scissors"}]
    (if (= (oppos-win-move p1) p2) "Player 1 won!"
    (if (= (oppos-win-move p2) p1) "Player 2 won!" "Draw!"))))

; ...
(ns rock-paper-scissors)

(def wins #{["rock" "scissors"] ["scissors" "paper"] ["paper" "rock"]})

(defn rps [p1 p2]
  (cond
    (= p1 p2) "Draw!"
    (wins [p1 p2]) "Player 1 won!"
    :else "Player 2 won!"))

; ...
(ns rock-paper-scissors)

(defn rps [p1 p2]
  (cond
    (= p1 p2) "Draw!"
    (case [p1 p2]
      ["scissors" "paper"] true
      ["paper" "rock"] true
      ["rock" "scissors"] true
      false) "Player 1 won!"
      :else "Player 2 won!"))

; ...
(ns rock-paper-scissors)

(def rps-game-map {
  "scissors" {
    "paper" "Player 1 won!"
    "rock" "Player 2 won!"
  }
  "paper"    {
    "scissors" "Player 2 won!"
    "rock" "Player 1 won!"
  }
  "rock"     {
    "scissors" "Player 1 won!"
    "paper" "Player 2 won!"
  }
})

(defn rps [p1 p2]
  ((rps-game-map p1) p2 "Draw!"))

; ...
(ns rock-paper-scissors)

(defn rps [p1 p2]
  (case [p1 p2]
    ["scissors", "paper"] "Player 1 won!"
    ["paper", "scissors"] "Player 2 won!"
    ["rock", "scissors"] "Player 1 won!"
    ["scissors", "rock"] "Player 2 won!"
    ["paper", "rock"] "Player 1 won!"
    ["rock", "paper"] "Player 2 won!"
    "Draw!"))
