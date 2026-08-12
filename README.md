<!-- 
<!--
Color palette: 
#fb8500 -> vibrant, fiery orange 
#219ebc -> cool, mid-tone cerulean blue 

Not much to say really. It's my first domain-specific language, 
hopefully I defined it well enough and added appropriate syntax highlighting. 
Nevertheless, I think it's a very good domain-specific language. 

Hope you think the same,
— William Bowley, 13th of August, 2026

P.S: Thanks for downloading the UnitValues repository `▽`ʃ♡
-->

<p align="center"><img src="logos/logo.png" alt="UnitValues" style="max-width:600px;"> </p>
<p align="center">A typed language for numerical quantities.</p>

# Overview
 
![License](https://img.shields.io/badge/License-MIT-219ebc?style=flat-square)
![DSL](https://img.shields.io/badge/Domain-DSL-fb8500?style=flat-square&labelColor)

Unit-Informed Values (`.uiv`) and Unit Types (`.ut`) are domain-specific languages for computational engineering. Unlike general-purpose formats, 
`.uiv` and `.ut` allow users to encode values with dimensional constraints.
## Local Installation

To install the Unit-Informed Values (`UIV`) language extension locally for Visual Studio Code:

### Windows

```powershell
Copy-Item -Recurse -Force $PWD "$HOME\.vscode\extensions\uiv-0.0.6"
```

### Linux/MacOs
```bash
cp -r . "$HOME/.vscode/extensions/uiv-0.0.6"
```