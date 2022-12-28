# Programming Exercize: Translator Application

Due to her lack of proficiency in English, Nima has to attend international competitions with a translator. Since bringing someone else to translate would be too expensive, Nima decides to look for an alternative solution. Now you have to help Nima and write a translator app that reads the dictionary and the corresponding sentence from the input and translates the sentence according to the language in which it is expressed. In the translation process, if there is no word in the dictionary, print the word itself in the output.

In the first line of the input, there is a number n, which represents the number of words that are available in the translation dictionary. Each of the next n lines contains four words, the second to fourth words being the translation of the first word. Each word is translated in three different languages. The second word is the English translation, the third word is the French translation, and the fourth word is the German translation of the first word. The last line contains a sentence that needs to be translated from English, French or German to the language of the first word. A sentence consists of several words separated by spaces. See example input and example output for more information. (If the translation of the desired word included two parts, consider it without a space. For example, the word laprogrammation in the input of the example below is in the form of la programmation, which has saved the space between its two parts.)

The final sentence may be a combination of words from three languages.

Example input:
```
4
man I je ich
kheili very très sehr
alaghemand interested intéressé interessiert 
barnamenevisi programming laprogrammation Programmierung
I am very interested in programming
```

Example output:
```
man am kheili alaghemand in barnamenevisi
```
