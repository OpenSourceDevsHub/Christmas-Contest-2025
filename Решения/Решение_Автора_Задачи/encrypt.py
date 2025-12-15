import re
from itertools import accumulate, cycle

BASE36_RE = re.compile(r"^[0-9A-Z]+$")


def encrypt(plaintext: str, decoy_stream: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") -> str: 
    
    shifts = accumulate((7, *((i * 2 + 5) for i in range(len(plaintext) - 1))))
    d = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decoys = cycle(decoy_stream)
    
    clean = "".join(
        d[v // 36] + d[v % 36] 
        if 0 < (v := ord(c) + s) < 36 * 36 
        else (_ for _ in ()).throw(ValueError(f"value {v} overflow at index {i}"))
        for i, (c, s) in enumerate(zip(plaintext, shifts))
    )
    
    return "".join(
        ch + (next(decoys) if idx % 4 == 3 else "")
        for idx, ch in enumerate(clean)
    )


if __name__ == "__main__":
    msg = "OpenSource_Chat-whoissoeea-gift"
    cipher = encrypt(msg)
    print("plaintext:", msg)
    print("ciphertext:", cipher)

