module Lib where

import Data.Function ((&))
import Data.Functor ((<&>))
import Data.List (nub)
import Data.Map (Map)
import qualified Data.Map as Map
import Data.Matrix (Matrix)
import qualified Data.Matrix as Matrix
import Text.Printf (printf)

type Splitter a = Int -> [a] -> [[a]]

newtype PChar = PChar {unwrap :: Char} deriving (Eq, Ord)

instance Show PChar where
  show s =
    let c = unwrap s
     in case c of
          ' ' -> "_"
          '\n' -> "\\n"
          e -> [e]
  showList lst = lst <&> show & concat & (++)

grouped :: Splitter a
grouped _ [] = []
grouped n lst = case take n lst of
  l | length l == n -> l : (grouped n $ drop 1 lst)
  _ -> []

-- >>> grouped 2 "abcde"
-- ["ab","bc","cd","de"]

chunked :: Splitter a
chunked _ [] = []
chunked n lst = case take n lst of
  l | length l == n -> l : (grouped n $ drop n lst)
  _ -> []

countFrequencies :: (Fractional b, Ord k) => [k] -> Map k b
countFrequencies text = occurrences <&> (/ all)
  where
    occurrences = Map.fromListWith (+) [(c, 1) | c <- text]
    all = length text & fromIntegral

entropy :: (Foldable t, Functor t, Floating f) => t f -> f
entropy frequencies = - (sum $ (\p -> p * (logBase 2 p)) <$> frequencies)

hn :: (Foldable t, Functor t) => t Double -> Int -> Double
hn frequencies n =
  frequencies & entropy & (* (1.0 / fromIntegral n))

toPercents :: Double -> [PChar]
toPercents f = (f * 100) & printf "%.3f" <&> PChar

asMatrix :: Map [PChar] [PChar] -> Matrix [PChar]
asMatrix m =
  let keys = Map.keys m
      f = keys <&> (!! 0) & nub
      s = keys <&> (!! 1) & nub
      lF = length f
      lS = length s
      all = [(i, j) | i <- [2 .. lF + 1], j <- [2 .. lS + 1]]
      init = Matrix.matrix (lF + 1) (lS + 1) (\_ -> [PChar '0'])
      withFirst = foldl (\acc i -> Matrix.setElem [f !! (i -2)] (i, 1) acc) init [2 .. lF + 1]
      withSecond = foldl (\acc i -> Matrix.setElem [s !! (i -2)] (1, i) acc) withFirst [2 .. lS + 1]
      getOrZero i j =
        case Map.lookup [(f !! (i -2)), (s !! (j -2))] m of
          Just x -> x
          Nothing -> [PChar '0']
   in foldl (\acc (i, j) -> Matrix.setElem (getOrZero i j) (i, j) acc) withSecond all
