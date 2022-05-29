-- https://www.codewars.com/kata/5544c7a5cb454edb3c000047/train/haskell
-- My solution
module Codewars.Kata.BouncingBall where

bouncingBall :: Double -> Double -> Double -> Integer
bouncingBall height bounce window
  | height <= 0 = -1
  | bounce <= 0 || 1 <= bounce = -1
  | window <= 0 || window >= height = -1
  | otherwise = 
    let n = toInteger
          $ length 
          $ takeWhile (> window) 
          $ iterate (* bounce) height
    in (n - 1) * 2 + 1

-- ...
module Codewars.Kata.BouncingBall where

bouncingBall :: Double -> Double -> Double -> Integer
bouncingBall h b w 
  | h > 0 && 0 < b && b < 1 && w < h = 2 + (bouncingBall (h * b) b w)
  | otherwise = -1

-- ...
module Codewars.Kata.BouncingBall where

bouncingBall :: Double -> Double -> Double -> Integer
bouncingBall h b w
  | not (h > 0 && 0 < b && b < 1 && w < h) = -1
  | otherwise = (truncate $ fromIntegral $ ceiling $ logBase b $ w / h) * 2 - 1

-- ...
module Codewars.Kata.BouncingBall where

bouncingBall :: Double -> Double -> Double -> Integer
bouncingBall h b w
  | h <= 0 || b <= 0 || b >= 1 || w >= h = -1
  | otherwise = 1 + 2 * (ceiling (logBase b (w / h)) - 1)