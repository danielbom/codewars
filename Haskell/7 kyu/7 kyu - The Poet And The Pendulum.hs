-- https://www.codewars.com/kata/5bd776533a7e2720c40000e5
-- My solution
module Poet where

import Data.List

extract cmp xs = [x | (x, index) <- zip xs [1 ..], cmp index]
left = reverse . extract even
right = extract odd

createPendulum :: [Int] -> [Int]
createPendulum (x:xs) = left xs ++ [x] ++ right xs

pendulum :: [Int] -> [Int]
pendulum = createPendulum . sort

-- And
module Poet where

import Data.List

extract cmp = map snd . filter (cmp . (`mod` 2) . fst) . zip [1 ..]
left = reverse . extract (==0)
right = extract (/=0)

createPendulum :: [Int] -> [Int]
createPendulum (x:xs) = left xs ++ [x] ++ right xs

pendulum :: [Int] -> [Int]
pendulum = createPendulum . sort

-- ...
module Poet where

import Data.List
import qualified Data.Sequence as Seq

pendulum :: [Int] -> [Int]
pendulum xs = map (Seq.index sorted) indices where
  l = length xs - 1
  indices = reverse [0,2..l] ++ [1,3..l]
  sorted = Seq.fromList $ sort xs

-- ...
module Poet (pendulum) where

import Data.List (sort)

pendulum :: [Int] -> [Int]
pendulum xs = go [] [] (sort xs) where
  go left right (l:r:middle) = go (l:left) (r:right) middle
  go left right [x] = x : left ++ reverse right
  go left right [] = left ++ reverse right

-- ...
module Poet where

import Data.List

pendulum :: [Int] -> [Int]
pendulum xs = reverse l ++ r
  where
    split a ~(bs, as) = (a:as, bs)
    (l, r) = foldr split ([],[]) (sort xs)
    
-- ...
module Poet where

import Data.List (partition, sort)

pendulum :: [Int] -> [Int]
pendulum = (\(o, e) -> (reverse . snd . unzip) o ++ (snd . unzip) e) . partition (even . fst) . zip [0..] . sort

-- ...
module Poet where
import Data.List

pendulum :: [Int] -> [Int]
pendulum = (\xs -> reverse (h (xs)) ++ h (tail xs)) . sort
  where
    h (x:y:ys) = x:(h ys)
    h xs = xs
