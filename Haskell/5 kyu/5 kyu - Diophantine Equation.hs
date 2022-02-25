-- https://www.codewars.com/kata/554f76dca89983cc400000bb/train/haskell
-- My solution
module Codewars.Kata.Dioph where

equation :: Integer -> Integer -> Integer
equation x y = (x - 2*y) * (x + 2*y)

solequaRec :: Integer -> Integer -> [(Integer, Integer)]
solequaRec a n = 
  if x < 0 || y < 0
  then []
  else if isIntegers && isValid
    then (x, y):rec
    else rec
  where 
    b = n `div` a
    isIntegers = a * b == n
    
    a2 = a * a
    x = (n + a2) `div` (2 * a)
    y = (n - a2) `div` (4 * a)
    isValid = equation x y == n

    rec = solequaRec (succ a) n
    
solequa :: Integer -> [(Integer, Integer)]
solequa = solequaRec 1

-- ...
module Codewars.Kata.Dioph where

solequa :: Integer -> [(Integer, Integer)]
solequa n = [(f a b,g a b)| a <- [1..u], let b = div n a, check a b] where
    f p q = div (p+q) 2
    g p q = div (q-p) 4
    check p q = p*q == n && rem (p+q) 2 == 0 && rem (q-p) 4 == 0
    u = floor.sqrt.fromIntegral $ n

-- ...
module Codewars.Kata.Dioph
    ( solequa
    ) where

import Control.Monad (forM, guard)
import Data.List     (group, sortBy)

solequa :: Integer -> [(Integer, Integer)]
solequa n = sortBy (\x y -> compare y x) $ do
    f <- factors n
    let g  = div n f
        x2 = g + f
        y4 = g - f
    guard $ g >= f && mod x2 2 == 0 && mod y4 4 == 0
    return (div x2 2, div y4 4)

smallestPrimeDivisorFrom :: Integer -> Integer -> Integer
smallestPrimeDivisorFrom n i
    | i * i > n    = n
    | mod n i == 0 = i
    | otherwise    = smallestPrimeDivisorFrom n $ i + 1

primeDecomposition :: Integer -> [(Integer, Int)]
primeDecomposition n = [(p, length ps) | ps@(p : _) <- group $ go n 2]
  where
    go 1 _ = []
    go m i = let p = smallestPrimeDivisorFrom m i in p : go (div m p) p

factors :: Integer -> [Integer]
factors n = map product $ forM (primeDecomposition n) $ \(p, e) -> [p ^ i | i <- [0 .. e]]