module Main where

import qualified Data.Char as Char
import Data.Function ((&))
import Data.Functor ((<&>))
import qualified Data.Map as Map
import Lib
import Data.List (sortBy)

main = do
  mytext_with_spaces <- readFile "mytext_with_spaces" <&> (<&> PChar)
  putStrLn "Text with spaces: "
  freqAndEntropy mytext_with_spaces
  mytext_without_spaces <- readFile "mytext_without_spaces" <&> (<&> PChar)
  putStrLn "Text without spaces: "
  freqAndEntropy mytext_without_spaces


freqAndEntropy :: [PChar] -> IO ()
freqAndEntropy text = do
  let f1 = text & countFrequencies
  putStrLn "Frequencies of letters: "
  f1 & Map.toList & sortBy (\(_, v) (_,v') -> compare v' v) <&> (<&> toPercents) & mapM_ print
  putStr "H1: "
  print $ (hn f1 1)

  let f2 = text & chunked 2 & countFrequencies
  putStrLn "Frequencies of bigrams: "
  print $ (f2 <&> toPercents & asMatrix)
  putStr "H2: "
  print $ (hn f2 2)

  let f2Over = text & grouped 2 & countFrequencies
  putStrLn "Frequencies of bigrams(overlapped): "
  print $ f2Over <&> toPercents & asMatrix
  putStr "H2(overlapped): "
  print $ (hn f2Over 2)

textPreparer path npath withSpaces = do
  text <- readFile path
  text
    & transform withSpaces
    & writeFile npath

transform withSpaces text =
  text
    <&> Char.toLower
      & words
    <&> filter isSmallRus
      & filter (not . null)
      & (if withSpaces then unwords else concat)
  where
    isSmallRus c =
      let ord = Char.ord c
       in (ord >= 1072 && ord <= 1103)
