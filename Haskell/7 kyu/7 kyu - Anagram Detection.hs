-- https://www.codewars.com/kata/529eef7a9194e0cbc1000255/train/haskell
-- My solution
module Codewars.Anagram where

import Data.Char (toLower)
import Data.List (sort)

isAnagramOf :: String -> String -> Bool
isAnagramOf test original = f test == f original
  where f = sort . map toLower

-- ...
module Codewars.Anagram where

import Data.Function (on)
import Data.List (sort)
import Data.Char (toLower)

isAnagramOf :: String -> String -> Bool
isAnagramOf = (==) `on` (sort . map toLower)

-- ...
module Codewars.Anagram where

import Data.Char
import Data.Map (insertWith, empty)
import Data.Function

-- A solution that doesn't use Data.List.sort. Why not.

isAnagramOf :: String -> String -> Bool
isAnagramOf = (==) `on` foldr (\x acc -> insertWith (+) (toLower x) 1 acc) empty

-- ...
{-# LANGUAGE TupleSections #-}
module Codewars.Anagram where
import qualified Data.Map as M
import Data.Char
import Data.Function
isAnagramOf :: String -> String -> Bool
isAnagramOf = (==) `on` charMap

charMap = M.fromListWith (+) . map (,1) . map toLower
