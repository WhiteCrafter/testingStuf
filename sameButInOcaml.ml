let rec factorial x = match x with 
  | 1 -> 1
  | x -> x * (factorial (x-1))