-- https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/haskell
-- My solution
module Initials where

import Data.Char (toUpper)
import Data.List (intersperse)

getInitials :: String -> String
getInitials
  = intersperse '.'
  . map (toUpper . head)
  . words
