-- https://www.codewars.com/kata/55192f4ecd82ff826900089e/train/haskell
-- My solution
module Codewars.Kata.Watermelon where

divide :: Integer -> Bool
divide w = (even w) && (w >= 4)
-- ...
module Codewars.Kata.Watermelon where

divide :: Integer -> Bool
divide 2 = False
divide x = even x
-- ...
module Codewars.Kata.Watermelon where

divide :: Integer -> Bool
divide = (&&) <$> even <*> (>= 4)
