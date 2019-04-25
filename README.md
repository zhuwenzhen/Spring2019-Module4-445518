# CSE 330: Module 4
Author: Wenzhen Zhu
Date: 02/27/2017
---
## Part 1. Regular Expressions
+ Match the string "hello world" in a sentence
```
\b(.*)(hello world)+(.*)\b
```

+ Find all words in an input string that contain a triple vowel
```
 \b\w*[aeiou]{3}\w*\b
```

+ Match an input string that is entirely a flight code, of the format AA####, where AA is a two-letter uppercase airline code, and #### is a three- or four-digit flight number
```
(^AA)\d{3,4}$
```
## Part2. Baseball Stats Counter (35 Points):
See ```module4.py```