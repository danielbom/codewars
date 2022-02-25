-- https://www.codewars.com/kata/remove-string-spaces/train/haskell
-- My solution
module Kata (noSpace) where

    noSpace :: String -> String
    noSpace str = [x | x <- str, not (x `elem` " ")]
-- ...
module Kata (noSpace) where

    noSpace :: String -> String
    noSpace = filter (/=' ')
-- ...
module Kata (noSpace) where

    import Data.Char (isSpace)
    
    noSpace :: String -> String
    noSpace = filter (not . isSpace)
-- ...
module Kata (noSpace) where

    noSpace :: String -> String
    noSpace = concat.words
-- ...
module Kata (noSpace) where

    noSpace :: String -> String
    noSpace str = concat (words str)
-- ...
module Kata (noSpace) where

    noSpace :: String -> String
    noSpace s = [x | x <- s, x /= ' ']
-- ...
module Kata (noSpace) where

    noSpace :: String -> String
    noSpace = filter (`notElem` " ")
-- ...
module Kata (noSpace) where

    noSpace :: String -> String
    noSpace str = concat $ words str
-- ...
module Kata (noSpace) where

    noSpace :: String -> String
    noSpace [] = []
    noSpace (x:xs)
      | x /= ' '  = x : noSpace xs
      | otherwise = noSpace xs
-- ...
module Kata (noSpace) where

    noSpace :: String -> String
    noSpace = foldl (\x y -> if [y] == " " then x else x ++ [y]) ""
-- ...
module Kata (noSpace) where

    noSpace :: String -> String
    noSpace str = foldr (++) "" (words str)
-- ...
module Kata (noSpace) where

    noSpace :: String -> String
    noSpace str
     | str == "" = ""
     | (head str) == ' ' = (noSpace (tail str))
     | otherwise = (head str) : (noSpace (tail str))
-- ...
module Kata (noSpace) where

    noSpace :: String -> String
    noSpace [] = []
    noSpace (x:xs) 
      | x == ' ' = noSpace(xs)
      | otherwise = [x] ++ noSpace(xs)
-- ...
module Kata (noSpace) where

    noSpace :: String -> String
    noSpace []=[]
    noSpace cs=filter func cs
      where func c=c/=' '
