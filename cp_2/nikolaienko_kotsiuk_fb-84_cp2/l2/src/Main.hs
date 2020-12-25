module Main where

import Data.Char (chr, ord, toLower)
import Data.Function ((&))
import Data.Functor ((<&>))
import Data.Map (Map, (!))
import qualified Data.Map as Map
import Control.Monad (replicateM)
import Data.List (isPrefixOf, sortBy)

main :: IO ()
main =  index

out = do
  text <- readFile "encrypted"
  let prep = filter (/= '\n') text
  print $ (vigenereCipherDecrypt "человеквфутляре" prep) <&> PChar


type Shifter = (Char, Char) -> Char




-- shifts given char ignoring out of range chars
unsafeShift :: Int -> Int -> Shifter
unsafeShift first last (offset, char) =
  let num = ord char
      out = num + (ord offset - first)
   in if num < first || num > last
        then char
        else
          chr $
            if out > last
              then out - (last - first) - 1
              else out


unsafeReverseShift first last (offset, char) =
  let num = ord char
      out = num - (ord offset - first)
   in if num < first || num > last
        then char
        else
          chr $
            if out < first
              then last - (first - out) + 1
              else out


vigenereCipherDecrypt key text = vigenereCipher key text $ unsafeReverseShift 1072 1103


vigenereCipher key text shifter = cycle key `zip` text <&> shifter

vigenereCipherRus key text = vigenereCipher key text $ unsafeShift 1072 1103

newtype PChar = PChar {unwrap :: Char} deriving (Eq, Ord)

instance Show PChar where
  show s = [unwrap s]
  showList lst = lst <&> show & concat & (++)

occurences text = Map.fromListWith (+) [(c, 1) | c <- text]

i :: Ord a => [a] -> Float
i text =
  Map.keys occs
    <&> (\t -> ((occs ! t) * (occs ! t - 1)) / (n * (n - 1)))
    & sum
  where
    occs = occurences text
    n = fromIntegral $ length text

each n [] = []
each n as = head as : each n (drop n as)

blocks r text= [0 .. r-1] <&> \n -> drop n text & each r

iSplitted r text =
  blocks r text <&> i & sum & (/ fromIntegral r)
 


encrypt = do
  text <- readFile "lem_fiasko"
  wf "fiasko_2_ад" "ад" text
  wf "fiasko_3_наш" "наш" text
  wf "fiasko_4_квас" "квас" text
  wf "fiasko_5_каноэ" "каноэ" text
  wf "fiasko_14_рациональность" "рациональность" text
  where
    wf path key text = writeFile path $ vigenereCipherRus key text

index = do
  rf "lem_fiasko" 
  rf "fiasko_2_ад" 
  rf "fiasko_3_наш" 
  rf "fiasko_4_квас" 
  rf "fiasko_5_каноэ" 
  rf "fiasko_14_рациональность" 
  where
    rf name = do
      text <- readFile name
      putStr (name ++ ": ")
      print $ i text

encrypted = do
  text <- readFile "encrypted" <&> filter (/= '\n')
  [1 .. 60] <&> (\r -> (iSplitted r text, r)) & mapM_ print





decrypt = do
  text <- readFile "encrypted"
  let 
    often = text 
      & filter (\x -> x /= '\n') 
      & blocks 15
      <&> occurences 
      <&> Map.toList 
      <&> sortBy (\(_, v) (_,v') -> compare v' v) 
      <&> (<&> (\(l, _) -> l)) 
      <&> (!!0)
    oftenRus = replicateM 15 ['о', 'е', 'а', 'н', 'т']
    keys = oftenRus <&> (\lst -> lst `zip` often) <&> (<&> unsafeReverseShift 1072 1103) & (filter $ isPrefixOf "человек") <&> (<&> PChar)
    in
      print $ take 100 $ keys 


