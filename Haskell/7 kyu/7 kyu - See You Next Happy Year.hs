-- https://www.codewars.com/kata/5ae7e3f068e6445bc8000046/train/haskell
-- My solution
module NextHappyYear where

import Data.List (nub)

nextHappyYear :: Int -> Int
nextHappyYear = until ((==4) . length . nub . show) succ . succ
-- ...
module NextHappyYear where

import Data.List

nextHappyYear :: Int -> Int
nextHappyYear = until (isUnique . show) succ . succ where
  isUnique = nub >>= (==)
-- ...
module NextHappyYear where

import Data.List (nub)

nextHappyYear :: Int -> Int
nextHappyYear = head . filter ((==) <*> nub <$> show) . enumFrom . succ
-- ...
module NextHappyYear where

import Data.List

nextHappyYear :: Int -> Int
nextHappyYear n = head $ dropWhile ((/=)<$>nub.show<*>show) [(n+1)..]
-- ...
module NextHappyYear where

import Data.List (nub)
import Control.Arrow ((>>>), (&&&))

nextHappyYear :: Int -> Int
nextHappyYear = enumFrom.(+1)
            >>> dropWhile (show >>> id &&& nub >>> uncurry (/=))
            >>> head