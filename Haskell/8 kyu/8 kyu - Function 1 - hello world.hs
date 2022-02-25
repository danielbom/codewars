-- https://www.codewars.com/kata/function-1-hello-world/train/haskell
-- My solution
module Codewars.Kata.HelloWorld where

    greet :: String
    greet = "hello world!"
-- ...
module Codewars.Kata.HelloWorld where

    greet :: String
    greet = reverse "!dlrow olleh"
-- ...
module Codewars.Kata.HelloWorld where

    greet :: String
    greet = map succ "gdkkn\USvnqkc "
-- ...
module Codewars.Kata.HelloWorld where

    greet :: String
    greet = take 12 "hello world! by zamcl"
-- ...
module Codewars.Kata.HelloWorld where

    greet :: String
    greet = filter ((`elem` [32,33,100,101,104,108,111,114,119]) . fromEnum) "hazey-llama-oats won't-ram-lazy-danny!"
-- ...
module Codewars.Kata.HelloWorld where

    greet :: String
    greet = id "hello world!"
-- ...
module Codewars.Kata.HelloWorld where

    greet :: String
    greet = ['h','e','l','l','o',' ','w','o','r','l','d','!']
-- ...
module Codewars.Kata.HelloWorld where
    import Data.Char
    
    greet :: String
    greet = map chr [104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100, 33]
-- ...
module Codewars.Kata.HelloWorld where

    [greeting, space, earth, exclamation] = ["hello", " ", "world", "!"]
    
    greet :: String
    greet = greeting ++ space ++ earth ++ exclamation
-- ...
module Codewars.Kata.HelloWorld where

    greet :: String
    greet = ldlof snoc "" "!dlrow olleh"
      where ldlof = foldl
            snoc acc x  =  x : acc
-- ...
module Codewars.Kata.HelloWorld where

    greet :: String
    greet = reverse $ unwords ["!dlrow","olleh"]
-- ...
module Codewars.Kata.HelloWorld where

    greet :: String
    greet = [ c | c <- "hello world!"]
-- ...
