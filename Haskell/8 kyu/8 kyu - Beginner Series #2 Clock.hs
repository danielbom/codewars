-- https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a/train/haskell
-- My solution
module Kata (past) where

past :: Int -> Int -> Int -> Int
past h m s = (s + m * 60 + h * 3600) * 1000
