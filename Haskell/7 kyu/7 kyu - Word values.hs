-- https://www.codewars.com/kata/word-values/train/haskell
-- My solution
module Haskell.Codewars.WordValues where

    import Data.Char
    import Data.List
    
    chAlphaValue :: Char -> Int
    chAlphaValue ch = if isAlpha ch then (ord (toLower ch)) - 96 else 0
    
    sumCharsAlphaValue :: [Char] -> Int
    sumCharsAlphaValue str = sum (map chAlphaValue str)
    
    wordValue :: [[Char]] -> [Int]
    wordValue xs = [ i*sum | [sum, i] <- transpose [map sumCharsAlphaValue xs, [1..length xs]]]
    -- wordValue xs [ i*sum | (i, sum) <- zip [0..] map sumCharsAlphaValue xs ]
-- ...
module Haskell.Codewars.WordValues where

    import Data.Char (isAsciiLower)
    
    wordValue :: [String] -> [Int]
    wordValue = zipWith (*) [1..] . map (sum . map ((+ a') . fromEnum) . filter isAsciiLower)
        where a' = negate . pred . fromEnum $ 'a'
-- ...
module Haskell.Codewars.WordValues where

    import Data.Char (isLetter, ord)
    
    wordValue :: [[Char]] -> [Int]
    wordValue = zipWith (*) [1..] . map sum . map (map conv)
      where conv x = if isLetter x then ord x - 96 else 0