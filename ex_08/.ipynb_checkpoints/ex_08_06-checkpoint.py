{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hola welcome to ex8, pg106\n",
      "\n",
      "Enter a number, Enter done if finished  -1\n",
      "Enter a number, Enter done if finished  4\n",
      "Enter a number, Enter done if finished  200\n",
      "Enter a number, Enter done if finished  100000\n",
      "Enter a number, Enter done if finished  done\n",
      "\n",
      "Max is: 100000.0 \n",
      "Min is: -1.0\n"
     ]
    }
   ],
   "source": [
    "print(\"Hola welcome to ex8, pg106\\n\")\n",
    "\n",
    "num = list()\n",
    "\n",
    "while True:\n",
    "    inp = input(\"Enter a number, Enter done if finished  \")\n",
    "    if inp == \"done\":\n",
    "        break\n",
    "    try:\n",
    "        inp = float(inp)\n",
    "    except:\n",
    "            print(\"Enter a valid number\")\n",
    "            continue\n",
    "    num.append(inp)\n",
    "    \n",
    "    \n",
    "\n",
    "print(\"\\nMax is:\", max(num), \"\\nMin is:\", min(num) )"
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
