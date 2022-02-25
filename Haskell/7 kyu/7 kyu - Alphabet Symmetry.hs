-- https://www.codewars.com/kata/59d9ff9f7905dfeed50000b0/train/haskell
-- My solution
module AlphabetSymm where

import Data.Char (toLower)

countSymmetry :: String -> Int
countSymmetry = length . filter (uncurry (==)) . zip ['a' .. 'z'] . map toLower

solve :: [String] -> [Int]
solve = map countSymmetry

-- ...
module AlphabetSymm where
import Data.Char (toLower)

solve :: [String] -> [Int]
solve = map (length . filter id . zipWith (==) ['a'..'z'] . map toLower)

-- ...
module AlphabetSymm where

import Data.Char (toLower)

solve :: [String] -> [Int]
solve = map $ length . filter id . zipWith (==) ['a'..'z'] . map toLower

-- ...
module AlphabetSymm where

import           Data.Char (ord, toLower)

solve :: [String] -> [Int]
solve = map (foldl (\cnt (i, c) -> if i == ord (toLower c) - 96 then cnt + 1 else cnt) 0 . zip [1..])

