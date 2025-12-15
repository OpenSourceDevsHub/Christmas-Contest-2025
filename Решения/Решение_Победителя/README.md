# Crypto Quest #1 — Solution

https://github.com/zart227/crypto-quest-1

This repository contains a solution to the first New Year crypto quest.

## Ciphertext
Length: 84 symbols  
Important property: 84 ≡ 4 (mod 5)

## Step-by-step solution

### 1. Noise removal
Every 5th symbol is noise.
We remove each 5th character from the ciphertext.

### 2. Base-36 decoding
The cleaned string is split into pairs.
Each pair is interpreted as a base-36 number.

### 3. Quadratic offset
For each decoded number we subtract a growing quadratic offset:
2², 3², 4², ...

### 4. Caesar shift
The intermediate text is shifted by -3 (Caesar cipher).

## Result
OpenSourceyChat0whoissoeea0gift
Open Source Chat — whoissoeeA — gift
