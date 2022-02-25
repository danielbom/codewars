-- https://www.codewars.com/kata/reversed-sequence/train/haskell
-- My solution
module RevSeq where 
    reverseSeq :: Int -> [Int] 
    reverseSeq n = reverse [1..n]
-- ...
module RevSeq where 
    reverseSeq :: Int -> [Int] 
    reverseSeq n = [n,n-1..1]
-- ...
module RevSeq where 
    reverseSeq :: Int -> [Int] 
    reverseSeq 0 = []
    reverseSeq n = n : reverseSeq (n-1)
-- ...
module RevSeq where 
    reverseSeq :: Int -> [Int] 
    reverseSeq = reverse . flip take [1..]
-- ...
module RevSeq where 
    reverseSeq :: Int -> [Int] 
    reverseSeq = enumFromThenTo <*> pred <*> const 1
-- ...
module RevSeq where 
    reverseSeq :: Int -> [Int] 
    reverseSeq n = [n - x | x <- [0..n-1]]
-- ...
module RevSeq (reverseSeq) where

    reverseSeq :: Int -> [Int] 
    reverseSeq = flip (enumFromThenTo <*> pred) 1
-- ...
module RevSeq where 
    reverseSeq :: Int -> [Int] 
    reverseSeq = (reverse .) . flip take $ iterate (+ 1) 1
-- ...
module RevSeq where 

    reverseSeq :: Int -> [Int]
    reverseSeq n = takeWhile (>= 1) $ iterate (\a -> a - 1) n
-- ...
module RevSeq where 
    reverseSeq :: Int -> [Int] 
    reverseSeq n =
      if n > 0
        then n : reverseSeq (n - 1)
      else []
-- ...
module RevSeq where 
    reverseSeq :: Int -> [Int] 
    reverseSeq n = foldl (\acc x -> x : acc) [] [1..n]
-- ...
module RevSeq where 
    reverseSeq :: Int -> [Int]
    reverseSeq n = enumFromThenTo n (n-1) 1
-- ...
module RevSeq where 
    reverseSeq :: Int -> [Int] 
    reverseSeq n | n == 0 = []
                 | otherwise = n : reverseSeq (n - 1)
-- ...
module RevSeq where 
    reverseSeq :: Int -> [Int] 
    reverseSeq n | n == 0 = []
                 | otherwise = [n] ++ reverseSeq (n - 1)
-- ...
module RevSeq where 
    reverseSeq :: Int -> [Int] 
    reverseSeq n
      | n > 0     = n : reverseSeq (n - 1)
      | n == 0    = []
      | otherwise = error "The number needs to be positive"
-- ...
module RevSeq where 
    reverseSeq :: Int -> [Int] 
    reverseSeq n = if n == 0 then [] else n:reverseSeq (n-1)
-- ...
module RevSeq where 
    reverseSeq :: Int -> [Int] 
    reverseSeq n = reverse (take n [1..])
-- ...
module RevSeq where 
    reverseSeq :: Int -> [Int] 
    reverseSeq n = [n, pred n .. 1]
-- ...
module RevSeq where 
    reverseSeq :: Int -> [Int]
    reverseSeq 0 = []
    reverseSeq n | n < 0 = map (\x -> -x) $ reverseSeq (-n) 
    reverseSeq n = n : reverseSeq (n - 1)
-- ...
module RevSeq where 
    reverseSeq :: Int -> [Int] 
    reverseSeq = reverse . enumFromTo 1