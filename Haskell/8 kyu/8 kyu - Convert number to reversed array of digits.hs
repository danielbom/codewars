-- https://www.codewars.com/kata/convert-number-to-reversed-array-of-digits/train/haskell
-- My solution
module Codewars.Kata.Convert where
    import Data.Char(digitToInt)
    
    digitize :: Int -> [Int]
    digitize s = map (read . pure :: Char -> Int) $ reverse $ show s

-- ...
module Codewars.Kata.Convert where
    import Data.Char
    
    digitize :: Int -> [Int]
    digitize = reverse . map digitToInt . show

-- ...
module Codewars.Kata.Convert where

    digitize :: Int -> [Int]
    digitize = map (read . return) . reverse . show
