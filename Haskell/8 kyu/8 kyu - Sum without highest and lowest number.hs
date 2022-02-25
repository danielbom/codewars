-- https://www.codewars.com/kata/sum-without-highest-and-lowest-number/train/haskell
-- My solution
module Kata where

    sumArray :: Maybe [Int] -> Int
    sumArray list = case list of
        Nothing -> 0
        Just list -> if length list == 0
            then 0
            else if length list == 1
                then 0
                else sum list - maximum list - minimum list
-- ...
module Kata where
    import Data.List 
    import Data.Maybe
    sumArray :: Maybe [Int] -> Int
    sumArray xs = sum $ drop 1 $ reverse $ drop 1 $ sort $ concat $ maybeToList xs
-- ...
module Kata where
    import Data.List
    sumArray :: Maybe [Int] -> Int
    sumArray (Just (x:x1:x2:xs)) = sum $ init $ tail $ sort $ x:x1:x2:xs
    sumArray _ = 0
-- ...
module Kata where

    import Data.List
    
    sumArray :: Maybe [Int] -> Int
    sumArray (Nothing) = 0 :: Int 
    sumArray (Just []) = 0 :: Int 
    sumArray (Just [_]) = 0 :: Int 
    sumArray (Just xs) = sum $ tail $ init $ sort xs
-- ...
module Kata where

    sumArray :: Maybe [Int] -> Int
    sumArray (Just xs@(_:_:_)) = sum xs - maximum xs - minimum xs
    sumArray _ = 0
-- ...
module Kata where
    import Data.List
    
    sumArray :: Maybe [Int] -> Int
    sumArray xs = case xs of 
                    Just [a] -> 0
                    Just [] -> 0
                    Just ar -> sum $ init $ tail $ sort ar
                    _ -> 0
-- ...
module Kata where

    sumArray :: Maybe [Int] -> Int
    sumArray (Just xs) = if (length xs) <= 1 then 0 else sum xs - minimum xs - maximum xs
    sumArray _ = 0
-- ...
module Kata where

    sumArray :: Maybe [Int] -> Int
    sumArray Nothing = 0
    sumArray (Just []) = 0
    sumArray (Just (x:[])) = 0
    sumArray (Just (x:y)) =
        let
            max = maximum (x:y)
            min = minimum (x:y)
            sum [] = 0
            sum (x:y) =
                x + sum y
        in
            sum (x:y) - max - min
