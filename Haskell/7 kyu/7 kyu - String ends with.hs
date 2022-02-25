-- https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/train/haskell
-- My solution
module StringsEndsWith (solution) where

solution :: String -> String -> Bool
solution s sub = drop n s == sub
  where n = length s - length sub
-- ...
module StringsEndsWith (solution) where

import Data.List

solution :: String -> String -> Bool
solution = flip isSuffixOf
