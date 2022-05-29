-- https://www.codewars.com/kata/55ab4f980f2d576c070000f4/train/haskell
-- My solution
module Codewars.G964.Suite2 where

game :: Integer -> Either Integer (Integer, Integer)
game k = 
  let k' = (k * k)
  in if even k' 
    then Left $ k' `div` 2 
    else Right $ (k', 2)

-- ...
module Codewars.G964.Suite2 where

divide :: Integer -> Integer -> (Integer, Integer)
divide x y
    | x `rem` y == 0 = (x `div` y, 1)
    | otherwise      = (x, y)

asPair :: (Integer, Integer) -> Either Integer (Integer, Integer)
asPair (x, 1) = Left x
asPair (x, y) = Right (x, y)

game :: Integer -> Either Integer (Integer, Integer)
game n = asPair $ (n * n) `divide` 2

-- ...
module Codewars.G964.Suite2 where

game :: Integer -> Either Integer (Integer, Integer)
game n | even n = Left (n * n `div` 2) | True = Right (n * n, 2)

-- ...
module Codewars.G964.Suite2 where

import Data.Ratio ((%), Ratio)
import GHC.Real   (Ratio ((:%)))

{-|
 a 3x3 board
 1/2 + 2/3 + 3/4 + 1/3 + 2/4 + 3/5 + 1/4 + 2/5 + 3/6
 which can be rearranged as
 1/2 + (1/3 + 2/3) + (1/4 + 2/4 + 3/4) + (2/5 + 3/5) + 3/6
 1/2 +  3/3        +  6/4              +  5/5        + 3/6
 1/2 +  1          +  3/2              +  1          + 1/2
 rearranged again
 (1/2 + 1/2) + (1 + 1) + 3/2
  1          +  2      + 3/2
 we find that the sum of a board of size n has the pattern
 1 + 2 + 3 + ... + (n-1) + n/2 
 ∵ sum of first (n - 1) consecutive numbers plus  n/2 (i)
 sum of n consecutive numbers starting at 1 is  n * (n + 1)/2 
 ∵ (i) =>  (n - 1) * (n - 1 + 1)/2 + n/2
       => ((n - 1) * n + n) / 2 = n^2 / 2
 if our board length is even we reduce the sum of n^2/2 else
 we write our fraction (n^2, 2) 
-}

game :: Integer -> Either Integer (Integer, Integer)
game n = case n^2 % 2 of
          v :% 1 -> Left   v
          v :% _ -> Right (v,2)
          