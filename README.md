### Project Name: Secret Message Decoder

#### Overview:
This project aims to decode a secret message from a list of words provided in a text file. The method of decoding involves arranging these words in a pyramid-like structure and retrieving the last word of each line. For instance, given words numbered from 1 to n, the result is obtained by forming a sentence from the last words of each line in the pyramid. 

#### Usage:
1. Provide a text file containing words, where each line consists of a number followed by a word. The numbers indicate the order of appearance in the message.
2. Execute the decoding function, which arranges the words into a pyramid and extracts the last word of each line.
3. The decoded message will be the sentence formed by these last words.

#### Example:
Given the words:
```
1-i
2-hello 3-love
4-world 5-cat 6-coding
```
The resulting decoded message is: "i love coding".

#### Note:
While the example provided may seem straightforward, the complexity arises when dealing with a large number of words (e.g., more than 300). Without the decoding function and this explanation, deciphering the text file becomes challenging.

#### Testing:
Included in the repository is a sample text file to test the decoding function. Upon execution, the expected result is the phrase: "in the shadowy depths of the ancient forest whispers of forgotten secrets linger concealed beneath the moss covered stones of time guarding ancient mysteries".

"Hope this project helps you level up your Python skills!"
