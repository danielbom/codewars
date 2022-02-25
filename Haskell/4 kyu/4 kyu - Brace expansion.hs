-- https://www.codewars.com/kata/597f11f61fe82a80c200002c/train/haskell
-- My solution
module Kata.BraceExpansion (expandBraces) where

indexOf :: Char -> String -> Int
indexOf = go 0
  where 
    go n ch [] = -1
    go n ch (x:xs)
      | x == ch   = n
      | otherwise = go (n + 1) ch xs

findEnd :: String -> Int
findEnd str = go str 0 0
  where
    go ('{':xs) n ctr = go xs (n + 1) (ctr + 1)
    go ('}':xs) n 0   = n
    go ('}':xs) n ctr = go xs (n + 1) (ctr - 1)
    go (_:xs) n ctr   = go xs (n + 1) ctr
    go _ _ _ = -1

splitCh :: Char -> String -> [String]
splitCh ch str = go ch str [] []
  where
    go _ [] ys rs = rs ++ [ys]
    go ch (x:xs) ys rs 
      | ch == x   = go ch xs [] (rs ++ [ys])
      | otherwise = go ch xs (ys ++ [x]) rs

mapCommaTopLevel :: String -> String
mapCommaTopLevel = go 0 []
  where 
    go _ rs [] = rs
    go 0 rs (',':xs) = go 0 (rs ++ [';']) xs
    go ctr rs (x:xs) = case x of
      '{' -> go (ctr + 1) (rs ++ [x]) xs
      '}' -> go (ctr - 1) (rs ++ [x]) xs
      _   -> go ctr (rs ++ [x]) xs

expandBraces :: String -> [String]
expandBraces str = 
  if start < 0 
  then [str]
  else
    concatMap (expandBraces . joinStr)
    $ splitCh ';' 
    $ mapCommaTopLevel
    $ take end
    $ drop (start + 1) str
  where
    joinStr s = take start str ++ s ++ drop (start + end + 2) str
    start = indexOf '{' str
    end = findEnd $ drop (start + 1) str

-- ...
module Kata.BraceExpansion (expandBraces) where

import Text.Parsec
import Text.Parsec.String
import Text.Parsec.Char
import Control.Applicative (liftA2)

expandBraces :: String -> [String]
expandBraces input = case parse path "" input of
    Left _ -> []
    Right output -> output

path :: Parser [String]
path = simplePath (pure . pure <$> anyChar)
  where
    expand = foldr (liftA2 (++)) [""]
    simplePath p = expand <$> many (try text <|> try expansion <|> p)
    pathToExpand = simplePath (pure . pure <$> noneOf ",}")
    expansion = between (char '{') (char '}') (concat <$> sepBy1 pathToExpand (char ','))
    text = (: []) <$> many1 (noneOf "{},")

-- ...
{-# LANGUAGE ViewPatterns #-}

module Kata.BraceExpansion (expandBraces) where

brace :: String -> ([String], String)
brace (comma -> (a, b, s)) = (a ++ b, s)

comma :: String -> ([String], [String], String)
comma "" = ([""], [], "")
comma ('{':(brace -> (a, '}':(comma -> (b, c, s))))) = ((++) <$> a <*> b, c, s)
comma (',':(brace -> (a, s))) = ([""], a, s)
comma ('}':s) = ([""], [], '}' : s)
comma (a:(comma -> (b, c, s))) = ((a :) <$> b, c, s)

expandBraces :: String -> [String]
expandBraces "" = [""]
expandBraces ('{':(brace -> (a, '}':(expandBraces -> b)))) = (++) <$> a <*> b
expandBraces (c:(expandBraces -> a)) = (c :) <$> a

-- ...
module Kata.BraceExpansion (expandBraces) where

import Text.ParserCombinators.ReadP

expandBraces :: String -> [String]
expandBraces = fst . head . filter (null . snd) . readP_to_S expr where
    
    brace :: ReadP a -> ReadP a
    brace str = between (char '{') (char '}') str

    expr = foldr union [[]] <$> many singl where
        singl = expand +++ simpl <++ (many1 $ string ",")
        simpl = fmap (: []) . munch1 $ flip notElem "{,}"
        expand = concat <$> brace (sepBy expr $ char ',')
        
        union :: [String] -> [String] -> [String]
        union as = concat . zipWith (map . (++)) as . repeat 
  
-- ...
module Kata.BraceExpansion (expandBraces) where

import Text.Parsec
import Control.Monad (join)

type P a = Parsec String () a

stringP :: P String
stringP = many1 $ noneOf "{},"
topStringP = many1 $ noneOf "{}"

termP :: P String -> P [String]
termP sp = return <$> sp
    <|> between (char '{') (char '}') subtermP
  where subtermP = join <$> termsP stringP `sepBy` (char ',')

termsP :: P String -> P [String]
termsP sp = map concat . sequence <$> many (termP sp)

expandBraces :: String -> [String]
expandBraces = either (error . show) id . parse (termsP topStringP) ""

-- ...
module Kata.BraceExpansion (expandBraces) where

import           Control.Applicative
import           Control.Arrow

expandBraces :: String -> [String]
expandBraces = map reverse . fst . expandBraces1 False [[]]
expandBraces1 :: Bool -> [String] -> String -> ([String], String)
expandBraces1 _ r [] = (r, [])
expandBraces1 b r ('{' : xs) =
  uncurry (expandBraces1 b) $ first (liftA2 (flip (++)) r) $ expandBraces1 True [[]] xs
expandBraces1 _    r ('}' : xs) = (r, xs)
expandBraces1 True r (',' : xs) = first (r ++) $ expandBraces1 True [[]] xs
expandBraces1 b    r (x   : xs) = expandBraces1 b (map (x :) r) xs

-- ...
module Kata.BraceExpansion (expandBraces) where
import Control.Applicative (liftA2)
import Text.Parsec

expandBraces :: String -> [String]
expandBraces = either (const []) id . parse parser "" where
    parser = expand <$> many (try alts <|> pure . pure <$> anyChar)
    alts = concat <$> between (char '{') (char '}') (alt `sepBy1` char ',')
    alt = expand <$> many (try alts <|> pure . pure <$> noneOf ",}")
    expand = foldr (liftA2 (++)) [""]

-- ...
module Kata.BraceExpansion (expandBraces) where
import Text.Parsec
data S = S String [([S],String)] deriving Show

parseS = (S <$> many (noneOf "{}") <*> many parsePair)
parseSNoComa = (S <$> many (noneOf "{,}") <*> many parsePairNoComa)
parsePair = (,) <$> (char '{' *> (parseSNoComa `sepBy` (char ',')) <* char '}') <*>  many (noneOf "{}")
parsePairNoComa = (,) <$> (char '{' *> (parseSNoComa `sepBy` (char ',')) <* char '}') <*>  many (noneOf "{,}")

expandBraces :: String -> [String]
expandBraces s = case (parse parseS " " s) of
    Left st -> error "Impossible"
    Right st -> expandBracesS  st

expandBracesS :: S -> [String]
expandBracesS (S s l) = map (s++) (foldl f [""] l) where
    f b (l2,s2) = (++) <$> b <*> (map (++s2) (concatMap expandBracesS l2))