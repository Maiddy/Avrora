# Output/Input

## Avrora.ui.prints *
### mprint(text, vmargin=0, hmargin=0, fill=" ", wrap=None,
###		speed=-1, char="",  _end="\n")

text - Text itself to output.
	   Make sure text does not contains escape chars,
	   if you do not want text looks like shi... shiny sun.

vmargin - Vertical indent from the top.
		  Set to int to indent in lines,
		  set to str like "45%" to indent,
		  as percentage of the entire height.

hmargin - Same as vmargin above, but it is
		  horizontal indent.

fill - I do not recommend to touch it for a while.

wrap - Length of text wrapping.(i dunno how to explain it,
		just try)

speed - Text appearance speed.

char - Same as fill for a while.

_end - A char to print after printing of the text.
	   (default '\n' - new line)


### minput(text="", text_margin=0, vmargin=0, hmargin=0)

text - Text to print before input.(same as usual *input()* with text)

text_margin - Text indent to the left.(Looks more nice sometimes)

vmargin - Same as *vmargin* in *mprint()*

hmargin - Same as *hmargin* in *mprint()*


## Avrora.ui.effects *
### hack()
