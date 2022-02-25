-- https://www.codewars.com/kata/570a6a46455d08ff8d001002/train/haskell
-- My solution
module Codewars.G964.NoZeros where

noBoringZeros :: Int -> Int
noBoringZeros 0 = 0
noBoringZeros n = read $ reverse $ dropWhile (=='0') $ reverse $ show n
-- ...
module Codewars.G964.NoZeros where

noBoringZeros :: Int -> Int
noBoringZeros 0 = 0
noBoringZeros n = read . reverse . dropWhile (== '0') . reverse $ show n
-- ...
module Codewars.G964.NoZeros where

noBoringZeros :: Int -> Int
noBoringZeros n
  | n == 0          = 0
  | n `mod` 10 == 0 = noBoringZeros (n `div` 10)
  | otherwise       = n
-- ...
module Codewars.G964.NoZeros where

noBoringZeros :: Int -> Int
noBoringZeros 0 = 0
noBoringZeros n = until ((/=0) . (`mod`10)) (`div`10) n
-- ...
module Codewars.G964.NoZeros where

noBoringZeros :: Int -> Int
noBoringZeros 0 = 0
noBoringZeros n = 
  let (d, m) = divMod n 10
  in if m == 0 then noBoringZeros d else n
-- ...
module Codewars.G964.NoZeros where
import Data.Bool

noBoringZeros :: Int -> Int
noBoringZeros = bool 0 . until ((/=0) . (`mod`10)) (`div`10) <*> (/=0)
-- ...
module Codewars.G964.NoZeros where
import Data.List (dropWhileEnd)

noBoringZeros :: Int -> Int
noBoringZeros 0 = 0
noBoringZeros x = read . dropWhileEnd (=='0') . show $ x
-- ...
module Codewars.G964.NoZeros where

noBoringZeros :: Int -> Int
noBoringZeros = until ((||) <$> (== 0) <*> (/= 0) . (`mod` 10)) (`div` 10)