-- https://www.codewars.com/kata/5af15a37de4c7f223e00012d/train/haskell
-- My solution
module MenBoys where

import Data.List (nub,sort)

menFromBoys :: [Int] -> [Int]
menFromBoys xs = sort men ++ reverse (sort boys)
  where
    unique = nub xs
    men = filter even unique
    boys = filter odd unique
-- ...
module MenBoys where

import Data.List

menFromBoys :: [Int] -> [Int]
menFromBoys = sortOn (\n -> (odd n, if even n then n else -n)) . nub
-- ...
module MenBoys where

import Data.List (nub,sort)

menFromBoys :: [Int] -> [Int]
menFromBoys xs =  nub $ [x | x<- sort xs, even x] ++ [x | x<-reverse $ sort xs, odd x] 
-- ...
module MenBoys where

import Data.List (nub,sort,partition,sortBy)
import Data.Bifoldable ( biconcat, bifoldMap )

menFromBoys :: [Int] -> [Int]
menFromBoys = bifoldMap sort (sortBy $ flip compare) . partition even . nub
-- ...
module MenBoys where
import Data.List (partition)
import Data.Bifunctor (bimap)

import Data.List (nub,sort)

menFromBoys :: [Int] -> [Int]
menFromBoys = nub . uncurry (++) . bimap sort (reverse . sort) . partition even