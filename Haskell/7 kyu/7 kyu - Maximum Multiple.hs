-- https://www.codewars.com/kata/5aba780a6a176b029800041c/train/haskell
-- My solution
module MaxMult where

maxMultiple :: Int -> Int -> Int
maxMultiple x n = (n `div` x) * x
-- ...
module MaxMult where

maxMultiple :: Int -> Int -> Int
maxMultiple d b = d * quot b d
-- ...
module MaxMult where

import Data.Functor

maxMultiple :: Int -> Int -> Int
maxMultiple = fmap (.) (*) <*> flip div
-- ...
module MaxMult where

maxMultiple :: Int -> Int -> Int
maxMultiple d b = head $ filter (\x -> x `mod` d ==0) [b, b-1..1]
-- ...
module MaxMult where

maxMultiple :: Int -> Int -> Int
maxMultiple d b = head $ dropWhile (\x -> x `mod` d /= 0) [b, b-1..]
