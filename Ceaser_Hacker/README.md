# Caesar Cipher Decryptor

This Python script allows you to decrypt a message that has been encoded using a Caesar cipher. It will attempt all possible shift values (from 1 to 26) and print the results for each one. This is useful for breaking Caesar ciphers without knowing the shift key.

## Features

- Takes a message as input from the user.
- Tries all shift values (1 to 26).
- Outputs all possible decrypted messages for each shift.

## How It Works

1. The script accepts a message you want to decrypt.
2. It then iterates through all shift values (from 1 to 26).
3. For each shift, it tries to decrypt the message by shifting each letter backwards.
4. It prints out the possible decrypted messages for each shift.
5. The correct message will be the one that makes sense in natural language.

## Usage

1. Run the script.
2. Enter the encrypted message when prompted.
3. The script will display the decrypted message for all shift values from 1 to 26.

## Example

```bash
Enter the message you want ot decrypt: qiwweki
```


### Output

```bash
1: phvvdjh
2: oguucig
3: nfttbhf
4: message    <---
5: ldrr`fd
6: kcqq_ec
7: jbpp^db
8: iaoo]ca
9: h`nn\b`
10: g_mm[a_
11: f^llZ`^
12: e]kkY_]
13: d\jjX^\
14: c[iiW][
15: bZhhV\Z
16: aYggU[Y
17: `XffTZX
18: _WeeSYW
19: ^VddRXV
20: ]UccQWU
21: \TbbPVT
22: [SaaOUS
23: ZR``NTR
24: YQ__MSQ
25: XP^^LRP
26: WO]]KQO
```


## Requirements

- Python 3.x

## Inspiration 

This was inspired from the book The Big Book Of Small Python Projects 

