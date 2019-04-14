# Folder-Maker

Folder Maker is a simple desktop application designed specifically for making directories for **Movies** and **TV Shows**.
Executable file for current version is found [here.](https://drive.google.com/open?id=10RHfafooz7Rzosroyq1FQoCPpilAaNIJ)

## Creating Directories For TV Shows

There are two modes of operation. 

#### - Sub Directory Per Episode

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sub directory per epsiode mode creates a folder structure like the one shown below.
```
Silicon Valley
│
└───Season 01
│   │
│   └─── 01
│   │
│   └─── 02
│   │   ...
│   └─── 08
│   
└─── Season 02
    │
    └─── 01
    │
    └─── 02
    │   ...
    └─── 08   
```

#### - Directory Per Season Only

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Directory per season only mode creates a folder structure like the one shown below.
```
Silicon Valley
│
└───Season 01
│   │
│   └─── Subtitles
│   
└─── Season 02
    │
    └─── Subtitles
```
## Creating Directories For Movies

Multiple movie directories can be created with or without Subtitles sub directory using Folder Maker. Simply add as much as movie titles to the list and press create button.

There are several Keyboard shortcuts added for convinience. 
- <kbd>A</kbd> = Add a movie for the list
- <kbd>E</kbd> = Edit a movie in the list
- <kbd>R</kbd> = Remove a movie from the list
- <kbd>C</kbd> = Create the directories for the movie list

## Setting up the project
Run 
`pip install -r requirements.txt`
from the repository directory.


## To Do

- UI improvements.
- At the moment, sub directory per episode mode can only create seasons with same number of episodes.
- Writing a shell extension for the program.

## Dependencies

- PyQt 5
