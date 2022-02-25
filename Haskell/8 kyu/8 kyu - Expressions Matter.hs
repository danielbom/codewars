-- https://www.codewars.com/kata/5ae62fcf252e66d44d00008e/train/haskell
-- My solution
module Expression where

expression :: Int -> Int -> Int -> Int 
expression a b c = foldl1 max [
    a + b + c,
    a * b * c,
    a * (b + c),
    a * b + c,
    a + b * c,
    (a + b) * c
    ]
-- ...
module Expression where
import Data.List

expression :: Int -> Int -> Int -> Int
expression a b c = maximum [a+b+c, a*(b+c), a*b*c, a+(b*c), (a+b)*c]
-- ...
module Expression where

expression :: Int -> Int -> Int -> Int
expression a b c =
    maximum [
          (a + b) + c
        , (a * b) + c
        , (a + b) * c
        , (a * b) * c
        , a + (b * c)
        , a * (b + c)
    ]
