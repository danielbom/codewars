-- https://www.codewars.com/kata/jennys-secret-message/train/haskell
-- My solution
module Codewars.Kata.Jenny where

    greet :: String -> String
    greet "Johnny" = "Hello, my love!"
    greet name     = "Hello, " ++ name ++ "!"
-- ...
module Codewars.Kata.Jenny where

    greet :: String -> String
    greet name 
        |(name=="Johnny") = "Hello, my love!"
        |otherwise      = "Hello, " ++ name ++ "!"
-- ...
module Codewars.Kata.Jenny where

    greet :: String -> String
    greet name = "Hello, " ++ (if name == "Johnny" then "my love!" else name ++ "!")
-- ...
module Codewars.Kata.Jenny where

    greet :: String -> String
    greet h = "Hello, "++(if h=="Johnny"then"my love"else h)++"!"

-- ...
module Codewars.Kata.Jenny where

    greet :: String -> String
    greet name
        | name /= "Johnny" = "Hello, " ++ name ++ "!"
        | otherwise        = "Hello, my love!"
