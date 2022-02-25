-- https://www.codewars.com/kata/ones-and-zeros/train/haskell
-- My solution
module OnesAndZeroes (toNumber) where

    _toNumber :: [Int] -> Int -> Int
    _toNumber [] n = 0
    _toNumber (x:xs) n = x * n + (_toNumber xs n*2)
    
    
    toNumber :: [Int] -> Int
    toNumber ns = _toNumber (reverse ns) 1

-- ...
module OnesAndZeroes (toNumber) where

    toNumber :: [Int] -> Int
    toNumber = foldl (\acc b -> 2*acc + b) 0 

-- ...
module OnesAndZeroes (toNumber) where

    toNumber :: [Int] -> Int
    toNumber s = sum $ map (\t -> fst t * 2 ^ snd t) $ zip s p
        where 
            l = length s
            p = reverse [0..l - 1]

-- ...
module OnesAndZeroes (toNumber) where

    toNumber :: [Int] -> Int
    toNumber = foldl1 (\acc x -> acc * 2 + x)

-- ...
module OnesAndZeroes (toNumber) where

    import Data.Foldable (foldl')
    
    toNumber :: [Int] -> Int
    toNumber = foldl' go 0
      where
        go x 0 = 2 * x
        go x 1 = 2 * x + 1
        go x _ = error "unreachable"

-- ...
module OnesAndZeroes (toNumber) where

    toNumber :: [Int] -> Int
    toNumber [] = 0
    toNumber [x] = x
    toNumber (x:xs) = (x * 2 ^(length xs)) + toNumber xs

-- ...
module OnesAndZeroes (toNumber) where

    toNumber :: [Int] -> Int
    toNumber =snd . foldr (\x (n,s) -> (n + 1 , s + x*2^n)) (0,0)

-- ...
module OnesAndZeroes (toNumber) where

    toNumber :: [Int] -> Int
    toNumber = sum . map (\(i,n) -> n * 2 ^ i) . zip [0..] . reverse

-- ...
module OnesAndZeroes (toNumber) where

    toNumber :: [Int] -> Int
    toNumber = go 0
      where
        go :: Int -> [Int] -> Int
        go acc [] = acc
        go acc (x:xs) = go (2 * acc + x) xs

-- ...
module OnesAndZeroes (toNumber) where

    toNumber :: [Int] -> Int
    toNumber z = foldr step 0 $ reverse z
      where step x y = (+) x ( (*) y 2 )