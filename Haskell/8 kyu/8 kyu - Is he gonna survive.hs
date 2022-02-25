-- https://www.codewars.com/kata/is-he-gonna-survive/train/haskell
-- My solution
module Survive where

    hero :: Int -> Int -> Bool
    hero bullet dragons = bullet - dragons * 2 >= 0
-- ..
module Survive where

    hero :: Int -> Int -> Bool
    hero = (>=) . (`div` 2)
-- ...
module Survive where

    hero :: Int -> Int -> Bool
    hero bullets dragons = bullets >= 2 * dragons
-- ...
module Survive where

    hero :: Int -> Int -> Bool
    hero b d = b `div` 2 >= d
-- ...
module Survive where

    hero :: Int -> Int -> Bool
    hero bullets dragons         -- using guards
        | bullets >= dragons*2 = True    -- if the number of bullets are greater than or equal to the number of dragons then True
        | otherwise            = False   -- otherwise, False
-- ...
