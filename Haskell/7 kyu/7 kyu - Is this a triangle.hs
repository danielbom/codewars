-- https://www.codewars.com/kata/is-this-a-triangle/train/haskell
-- My solution
module Codewars.Triangles where

    import Data.List (sort)
    
    isTriangle :: Int -> Int -> Int -> Bool
    isTriangle a b c = a + b > c && a + c > b && b + c > a
-- ...
module Codewars.Triangles where

    import Data.List (sort)
    
    isTriangle :: Int -> Int -> Int -> Bool
    isTriangle a b c =
      case sort [a,b,c] of
         [min, middle, max] -> (min + middle) > max
-- ...
module Codewars.Triangles where

    isTriangle :: Int -> Int -> Int -> Bool
    isTriangle a b c = and [ a < b + c
                           , b < c + a
                           , c < a + b
                           ]
-- ...
module Codewars.Triangles where

    import Data.List (sort)
    
    isTriangle :: Int -> Int -> Int -> Bool
    isTriangle a b c = head sorted < sum (tail sorted)
      where
        sorted = reverse(sort [a, b, c])
-- ...
module Codewars.Triangles where

    import Data.List (sort)
    
    isTriangle :: Int -> Int -> Int -> Bool
    isTriangle a b c = let [minn,middlen,maxn] = sort [a,b,c] in minn + middlen > maxn
-- ...
module Codewars.Triangles where

    import Data.List (sort)
    
    isTriangle :: Int -> Int -> Int -> Bool
    isTriangle a b c = maximum [a,b,c] < sum [a,b,c] - maximum [a,b,c]
-- ...
module Codewars.Triangles where

    import Data.List
    
    isTriangle :: Int -> Int -> Int -> Bool
    isTriangle a b c = x + y > z
      where [x, y, z] = sort [a, b, c]
-- ...
module Codewars.Triangles where

    import Data.List (sort)
    
    isTriangle :: Int -> Int -> Int -> Bool
    isTriangle a b c = check $ sort [a, b, c]
      where 
        check (a:b:c:[]) = (a + b) > c
-- ...
module Codewars.Triangles where

    import Data.List (sort, permutations)
    
    isValidTriangle (a:b:c:[]) = (a+b)> c
    isTriangle :: Int -> Int -> Int -> Bool
    isTriangle a b c = all isValidTriangle (permutations [a,b,c])
-- ...
module Codewars.Triangles where

    import Data.List (sort)
    
    isTriangle :: Int -> Int -> Int -> Bool
    isTriangle a b c
      | (\e -> e > 0)`all` (a:b:c:[]) = case (sort (a:b:c:[])) of f:s:t:[] -> (t < f + s)
      | otherwise = False
-- ...
module Codewars.Triangles where

    import Data.List (sort)
    
    isTriangle :: Int -> Int -> Int -> Bool
    isTriangle a b c = 
      let x = a + b > c
          y = b + c > a
          z = a + c > b
      in x && y && z
-- ...
module Codewars.Triangles where

    import Data.List (sort)
    
    isTriangle :: Int -> Int -> Int -> Bool
    isTriangle a b c = xPlusYGreaterZ a b c && xPlusYGreaterZ a c b && xPlusYGreaterZ b c a
      where xPlusYGreaterZ x y z = (x + y) > z
-- ...
module Codewars.Triangles where

    import Data.List (sort)
    
    isTriangle :: Int -> Int -> Int -> Bool
    isTriangle a b c
      | a < 0 = False
      | b < 0 = False
      | c < 0 = False
      | a+b <= c = False
      | a+c <= b = False
      | b+c <= a = False
      | otherwise = True