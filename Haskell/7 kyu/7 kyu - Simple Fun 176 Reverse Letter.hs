-- https://www.codewars.com/kata/58b8c94b7df3f116eb00005b/train/haskell
-- My solution
module SF176 where

import Data.Char (isLetter)

reverseLetter :: String -> String
reverseLetter = reverse . filter isLetter 

-- ...
module SF176 where

import Data.Char (isAlpha)

reverseLetter :: String -> String
reverseLetter = reverse . filter isAlpha

-- ...
module SF176 where

reverseLetter :: String -> String
reverseLetter str = reverse [x | x <- str, x `elem` ['a'..'z']]