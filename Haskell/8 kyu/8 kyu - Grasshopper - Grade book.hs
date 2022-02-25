-- https://www.codewars.com/kata/55cbd4ba903825f7970000f5/train/haskell
-- My solution
module GradeBook (getGrade) where

getGrade :: Double -> Double -> Double -> Char
getGrade x y z
  | score >= 90 = 'A'
  | score >= 80 = 'B'
  | score >= 70 = 'C'
  | score >= 60 = 'D'
  | otherwise = 'F'
  where score = (x + y + z) / 3
-- ...
module GradeBook (getGrade) where

toGrade :: Double -> Char
toGrade d 
  |  0 <= d && d < 60 = 'F'
  | 60 <= d && d < 70 = 'D'
  | 70 <= d && d < 80 = 'C'
  | 80 <= d && d < 90 = 'B'
  | 90 <= d && d <= 100 = 'A'

getGrade :: Double -> Double -> Double -> Char
getGrade x y z = toGrade $ (x+y+z)/3