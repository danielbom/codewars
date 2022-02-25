-- https://www.codewars.com/kata/55f73be6e12baaa5900000d4/train/haskell
-- My solution
module MessiGoals where

goals :: Int -> Int -> Int -> Int
goals x y z = x + y + z
-- ...
module MessiGoals where

goals :: Int -> Int -> Int -> Int
goals = ((+) .) . (+)
-- ...
module MessiGoals where

goals :: Int -> Int -> Int -> Int
goals = (. (+)) ((+) .)
-- ...
module MessiGoals where
import Data.Function (on)

goals :: Int -> Int -> Int -> Int
goals = (.) `on` (+)
-- ...
module MessiGoals where

goals :: Int -> Int -> Int -> Int
goals laliga copa champions = laliga + copa + champions
-- ...
module MessiGoals where
import Data.Function

goals :: Int -> Int -> Int -> Int
goals = on (.) (+)

