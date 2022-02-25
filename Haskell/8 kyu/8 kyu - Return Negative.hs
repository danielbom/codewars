-- https://www.codewars.com/kata/return-negative/train/haskell
-- My solution
module Codewars.Kata.Negative where

    makeNegative :: (Num a, Ord a) => a -> a
    makeNegative a
          | a < 0 = a
          | otherwise = negate a
-- ...
module Codewars.Kata.Negative where

    makeNegative :: Num a => a -> a
    makeNegative = negate . abs
-- ...
module Codewars.Kata.Negative where

    makeNegative :: Num a => a -> a
    makeNegative n = - abs n
-- ...
module Codewars.Kata.Negative where

    makeNegative :: (Num a, Ord a) => a -> a
    makeNegative x = if x > 0 then (-x) else x
-- ...
module Codewars.Kata.Negative where

    makeNegative :: (Num a, Ord a) => a -> a
    makeNegative number | number < 0 = number
                        | otherwise = number * (-1)
-- ...
module Codewars.Kata.Negative where

    makeNegative :: (Num a, Ord a) => a -> a
    makeNegative a = min (-a) a
-- ...
module Codewars.Kata.Negative where

    makeNegative :: (Num a, Ord a) => a -> a
    makeNegative n = negate $ abs n
-- ...
module Codewars.Kata.Negative where

    makeNegative :: (Num a, Ord a) => a -> a
    makeNegative n = negate(abs(n))
-- ...
