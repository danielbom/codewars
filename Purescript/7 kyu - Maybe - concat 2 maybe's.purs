-- https://www.codewars.com/kata/57da675dfa96908b16000040/train/purescript
-- My solution
module MaybeConcat (concatMaybe) where

import Prelude

import Preloaded (undefined)
import Data.Maybe (Maybe)
import Control.Apply (lift2)

concatMaybe :: Maybe String -> Maybe String -> Maybe String
concatMaybe = lift2 (\x y -> x <> " " <> y)
