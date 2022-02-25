-- https://www.codewars.com/kata/calculate-average/train/haskell
-- My solution
module Average where

    avg :: [Float] -> Float
    avg l = (sum l) / fromIntegral (length l)
-- ...
module Average where

    import Data.List (genericLength)

    avg :: [Float] -> Float
    avg l = sum l / genericLength l
-- ...
module Average where

    avg :: [Float] -> Float
    avg [] = error "Cannot get average of empty list of values."
    avg l = (sum l) / (fromIntegral $ length l)
-- ...
module Average where

    avg :: [Float] -> Float
    avg  = pure (/) <*> sum <*> fromIntegral . length
-- ...
module Average where

    import Control.Monad (liftM2)
    import Data.List (genericLength)
    
    avg :: [Float] -> Float
    avg = liftM2 (/) sum genericLength
-- ...

