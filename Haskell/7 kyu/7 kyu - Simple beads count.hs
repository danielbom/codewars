-- https://www.codewars.com/kata/58712dfa5c538b6fc7000569/train/haskell
-- My solution
module Kata (countRedBeads) where

countRedBeads :: Int -> Int
countRedBeads blueBeads
  | blueBeads < 2 = 0
  | otherwise     = 2 * (blueBeads - 1)

-- ...
module Kata (countRedBeads) where

countRedBeads :: Int -> Int
countRedBeads = max 0 . (2 *) . pred

-- ...
module Kata (countRedBeads) where

countRedBeads :: Int -> Int
countRedBeads 0 = 0
countRedBeads n = 2 * (n - 1)

-- ...
module Kata (countRedBeads) where

countRedBeads :: Int -> Int
countRedBeads = (<*>) ((*) . fromEnum . (> 1)) ((2 *) . subtract 1)

-- ...
module Kata (countRedBeads) where

countRedBeads :: Int -> Int
countRedBeads = (*) . fromEnum . (> 1) <*> (2 *) . subtract 1
