-- https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/haskell
-- My solution
module Codewars.Kata.DNA where
import Codewars.Kata.DNA.Types

-- data Base = A | T | G | C
type DNA = [Base]

dnaStrand :: DNA -> DNA
dnaStrand = map compl
  where 
    compl :: Base -> Base
    compl A = T
    compl T = A
    compl G = C
    compl C = G

-- ...
module Codewars.Kata.DNA where
import Codewars.Kata.DNA.Types

import Data.Maybe (fromJust)

-- data Base = A | T | G | C
type DNA = [Base]

dnaStrand :: DNA -> DNA
dnaStrand = map (fromJust . flip lookup [(A,T),(T,A),(G,C),(C,G)])

-- ...
module Codewars.Kata.DNA where
import Codewars.Kata.DNA.Types

-- data Base = A | T | G | C
type DNA = [Base]

dnaStrand :: DNA -> DNA
dnaStrand = foldr (\b acc -> (comp b) : acc) []
  where
    comp b = case b of 
      A -> T
      C -> G
      G -> C
      T -> A
