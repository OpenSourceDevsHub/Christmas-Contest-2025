import re
from itertools import accumulate

BASE36_RE = re.compile(r"^[0-9A-Z]+$")


def decrypt(ciphertext: str) -> str: 
    if not BASE36_RE.fullmatch(ciphertext):
        raise ValueError("expects Base36 characters only")
    
    f = "".join(c for i, c in enumerate(ciphertext, 1) if i % 5)
    pairs = [f[i:i+2] for i in range(0, len(f), 2)]
    
    return "".join(
        (lambda p, s, i: chr(code) if 0 < (code := int(p, 36) - s) < 256 
         else (_ for _ in ()).throw(ValueError(f"Invalid ascii {code} at index {i}"))
        )(p, s, i) 
        for i, (p, s) in enumerate(zip(pairs, accumulate((7, *((i * 2 + 5) for i in range(len(pairs) - 1))))))
    )


if __name__ == "__main__":
    print("decode:", decrypt(
        "2E3GX3C3U93E4JK545I35M69L6Q6N78F91PAF9D0CED0GEAF91GQHZRJ6K95LON1TN4QB2S0TMVVR"
    ))
