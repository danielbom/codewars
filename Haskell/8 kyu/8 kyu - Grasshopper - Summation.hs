-- https://www.codewars.com/kata/55d24f55d7dd296eb9000030/train/haskell
-- My solution
module Summation where 

summation :: Integer -> Integer 
summation n = sum [1..n]
-- ...
module Summation where 

summation :: Integer -> Integer 
summation n = div (n*(n + 1)) 2
-- ...
module Summation where 

summation :: Integer -> Integer 
summation n = n * (n+1) `quot` 2
