-- https://www.codewars.com/kata/are-the-numbers-in-order/train/haskell
-- My solution
module NumbersInOrder (isAscOrder) where 
    isAscOrder :: [Int] -> Bool
    isAscOrder [] = True
    isAscOrder [x] = True
    isAscOrder (x:y:xs) = if x <= y then isAscOrder (y:xs) else False
-- ...
module NumbersInOrder where 
    import Data.List
    
    isAscOrder :: [Int] -> Bool 
    isAscOrder xs = sort xs == xs
-- ...
module NumbersInOrder where 

    isAscOrder :: [Int] -> Bool 
    isAscOrder = and . (zipWith (<=) <*> tail)
-- ...
module NumbersInOrder where 

    import Data.List (sort)
    
    isAscOrder :: [Int] -> Bool 
    isAscOrder = (==) <*> sort
-- ...
module NumbersInOrder (isAscOrder) where 

    import Data.List
    
    isAscOrder :: [Int] -> Bool
    isAscOrder = sort >>= (==)
-- ...
module NumbersInOrder where 

    isAscOrder :: [Int] -> Bool
    isAscOrder (a:b:xs)
      | a <= b = isAscOrder (b:xs)
      | otherwise = False
    isAscOrder _ = True
-- ...
module NumbersInOrder where 

    isAscOrder :: [Int] -> Bool 
    isAscOrder xs = and $ zipWith (<=) xs (tail xs)
-- ...
module NumbersInOrder where 

    isAscOrder :: [Int] -> Bool 
    isAscOrder []  = True
    isAscOrder [_] = True
    isAscOrder (a:b:c)
      | a > b      = False
      | otherwise  = isAscOrder (b:c)
-- ...
module NumbersInOrder where 

    isAscOrder :: [Int] -> Bool
    isAscOrder [] = True
    isAscOrder (x:[]) = True
    isAscOrder (x:y:xs) = (x <= y) && isAscOrder (y:xs);
-- ...
module NumbersInOrder (isAscOrder) where 

    isAscOrder :: [Int] -> Bool
    isAscOrder (x:xs)
      |length (x:xs) == 1 = True
      |x <= head xs = isAscOrder xs
      |otherwise = False
-- ...
module NumbersInOrder (isAscOrder) where 

    isAscOrder :: [Int] -> Bool
    isAscOrder = \x -> sort x == x
      where
      sort [] = []
      sort (x:xs) = let great = [ y | y <- xs , x <= y];
                        lesser = [ y | y <- xs , x > y ]
                    in (sort lesser) ++ [x] ++ (sort great) 
-- ...
module NumbersInOrder (isAscOrder) where 

    isAscOrder :: [Int] -> Bool
    isAscOrder lst = all pairInOrder pairs
      where
        pairInOrder (a, b) = a <= b
        pairs = zip lst (drop 1 lst)
-- ...
module NumbersInOrder (isAscOrder) where 

    isAscOrder :: [Int] -> Bool
    isAscOrder [x] = True
    isAscOrder xs  = all (uncurry (<=)) . zip xs $ tail xs
-- ...
