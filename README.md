# password-generator.py

>Make a password generator that generates a random password of desired length specified by user input.
For example:
Enter desired password length>> 7
hY@rSdA

[Prompt](https://www.reddit.com/r/ProgrammingPrompts/comments/4cegdt/easy_make_a_simple_password_generator/)

## Help
```
usage: password-generator.py [-h] [--uppercase_ascii] [--lowercase_ascii]
                             [--numerical] [--punctuation] [--length LENGTH]
                             [--count COUNT]

Generate passwords

optional arguments:
  -h, --help            show this help message and exit
  --uppercase_ascii, -A
                        Use uppercase ASCII
  --lowercase_ascii, -a
                        Use lowercase ASCII
  --numerical, -n       Use numerical characters
  --punctuation, -p     Use punctuation characters
  --length LENGTH, -l LENGTH
                        Generate a password of this length
  --count COUNT, -c COUNT
                        How many passwords to generate
```

## Example
```
> python password-generator.py -npAa -c 5 -l30
```
```
8yP&@r'T~ew<I$eE~8;"N}ZuETUdYH
{l]?[*-)U<z&"@*E0M2gF2qU[K3-l-
Ax@w^=P\%YD~f`>{Z50S[i0h$B7xTu
y!z5)X'({*tP{>DqotV|Wj,2-QAV2*
*+\Zj/hn(*22-ReGAY>)fS6VRc@kRg
```
