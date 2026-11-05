# Description

This is a simple python script for looking up Chinese sentences in GoldenDict-ng.

It's intended to reinforce the options of sentence mining for the program.

<img width="775" height="1029" alt="image" src="https://github.com/user-attachments/assets/54b82414-829a-4a59-b9ab-d699ff62664f" />

## Operation
It uses jieba to parse the sentence, and make all the parsed sentence clickable, then display the result on the program. 


## Features
- Accurate mode **default** | (similar to usual sentence splitting)
- Search engine mode ```-i``` | (similar to accurate but it includes splitting the long words into fragments)
- Has a mono character option ```-m``` | (for looking up single characters only. useful for Classical Chinese)

To learn more about those features: [About segmentation mode](https://github.com/fxsjy/jieba/tree/master#main-functions)

## Dictionary
By default, it's already using a big dictionary from jieba's repo to support all characters.

Main dictionary source: [dict.txt.big](https://github.com/fxsjy/jieba/blob/master/extra_dict/dict.txt.big)

It is possible to change the main dictionary with the ```-d ``` flag. User dictionary is possible with a ``-u`` flag.

## Setup for GoldenDict-ng
1. Go to Preferences => Sources => Programs and make an external program using the script (you can add command line flags for it)
   
<img width="836" height="49" alt="image" src="https://github.com/user-attachments/assets/ae7e0b23-e7b3-41b1-8d07-98797ceeb18f" /> 


2. Go to Groups then make sure the external program (/w jieba-gd-lookup) is at the top

<img width="426" height="207" alt="image" src="https://github.com/user-attachments/assets/5d445d85-d2c4-4046-964a-8c9ad4669ec8" />


## Credits
* [gd-mandarin](https://github.com/Ajatt-Tools/gd-tools#gd-mandarin) - Provided the design inspiration for this project.
* [Jieba](https://github.com/fxsjy/jieba) - The core text-segmentation program powering this script.
