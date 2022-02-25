-- https://www.codewars.com/kata/square-n-sum/train/haskell
-- My solution
module SquareSum where

    squareSum :: [Integer] -> Integer
    squareSum list = sum [x*x | x <- list]
-- ...
module SquareSum where

    squareSum :: [Integer] -> Integer
    squareSum = sum . map (^2)
-- ...
module SquareSum where

    squareSum :: [Integer] -> Integer
    squareSum [] = 0
    squareSum (x:xs) = x ^ 2 + squareSum xs
-- ...
module SquareSum where

    squareSum :: [Integer] -> Integer
    squareSum = foldr (\x s -> x*x + s) 0
-- ...
module SquareSum where

    squareSum :: [Integer] -> Integer
    squareSum = foldr ((+) . (^2)) 0
-- ...
module SquareSum where

    squareSum :: [Integer] -> Integer
    squareSum xs = sum (map (^2) xs) 
-- ...
module SquareSum where

    import Control.Monad
    
    squareSum :: [Integer] -> Integer
    squareSum = sum . map (join (*))
-- ...
