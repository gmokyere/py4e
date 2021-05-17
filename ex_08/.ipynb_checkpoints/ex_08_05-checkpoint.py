{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hola welcome to ex8, pg106\n",
      "\n",
      "stephen.marquard@uct.ac.za\n",
      "louis@media.berkeley.edu\n",
      "zqian@umich.edu\n",
      "rjlowe@iupui.edu\n",
      "zqian@umich.edu\n",
      "rjlowe@iupui.edu\n",
      "cwen@iupui.edu\n",
      "cwen@iupui.edu\n",
      "gsilver@umich.edu\n",
      "gsilver@umich.edu\n",
      "zqian@umich.edu\n",
      "gsilver@umich.edu\n",
      "wagnermr@iupui.edu\n",
      "zqian@umich.edu\n",
      "antranig@caret.cam.ac.uk\n",
      "gopal.ramasammycook@gmail.com\n",
      "david.horwitz@uct.ac.za\n",
      "david.horwitz@uct.ac.za\n",
      "david.horwitz@uct.ac.za\n",
      "david.horwitz@uct.ac.za\n",
      "stephen.marquard@uct.ac.za\n",
      "louis@media.berkeley.edu\n",
      "louis@media.berkeley.edu\n",
      "ray@media.berkeley.edu\n",
      "cwen@iupui.edu\n",
      "cwen@iupui.edu\n",
      "cwen@iupui.edu\n"
     ]
    }
   ],
   "source": [
    "print(\"Hola welcome to ex8, pg106\\n\")\n",
    "\n",
    "fh = open('mbox-short.txt')\n",
    "for line in fh:\n",
    "    line = line.rstrip() #delete right side white space\n",
    "    \n",
    "    #Gaurdian\n",
    "    if len(line) <3:\n",
    "        continue\n",
    "        \n",
    "    if not line.startswith(\"From \"): #skip lines that do not start from \"from\"\n",
    "        continue\n",
    "    word = line.split()\n",
    "    print(word[1])\n",
    "            \n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
