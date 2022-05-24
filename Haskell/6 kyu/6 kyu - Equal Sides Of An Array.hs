-- https://www.codewars.com/kata/5679aa472b8f57fb8c000047/train/haskell
-- My solution
module Codewars.G964.FindEven where

findEvenIndex :: [Int] -> Int
findEvenIndex arr = head $ go 0 (sum arr) 0 arr
  where
    go _ _ _ [] = [-1]
    go left right index (x:xs)
      | left == right' = index:rest
      | otherwise           = rest
      where right' = right - x
            rest = go (left + x) right' (index + 1) xs

-- And
module Codewars.G964.FindEven where

import Data.List (scanl')
import Data.Maybe

data EvenIdx = EvenIdx
  { left  :: Int
  , right :: Int
  , index :: Int
  , lastLeft :: Maybe Int
  }

evenIdxFromList :: [Int] -> EvenIdx
evenIdxFromList xs = EvenIdx 0 (sum xs) (-1) Nothing

nextEvenIdx :: EvenIdx -> Int -> EvenIdx
nextEvenIdx (EvenIdx left right index _) x = 
  EvenIdx (left + x) (right - x) (index + 1) (Just left)

evenIdxValid :: EvenIdx -> Bool
evenIdxValid (EvenIdx _ right _ lastLeft) = maybe True (right ==) lastLeft

findEvenIndex :: [Int] -> Int
findEvenIndex arr =
  case result of
    (x1:x2:xs) -> index x2
    _          -> -1
  where result = filter evenIdxValid
          $ scanl' nextEvenIdx (evenIdxFromList arr) arr

-- ...
module Codewars.G964.FindEven where

import Control.Applicative ((<$>), (<*>))
import Data.List (elemIndex)
import Data.Maybe (fromMaybe)

findEvenIndex :: [Int] -> Int
findEvenIndex = fromMaybe (-1) . elemIndex True .
  (zipWith (==) <$> scanl1 (+) <*> scanr1 (+))
