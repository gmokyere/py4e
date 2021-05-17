{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hola welcome to ex8, pg105\n",
      "['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']\n"
     ]
    }
   ],
   "source": [
    "print(\"Hola welcome to ex8, pg105\")\n",
    "\n",
    "fh = open('romeo.txt')\n",
    "words = list()\n",
    "for line in fh:\n",
    "    wrd = line.rstrip()\n",
    "    wrd = wrd.split()\n",
    "    for word in wrd:\n",
    "        if word not in words:\n",
    "            words.append(word)\n",
    "            \n",
    "print(sorted(words))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "26\n"
     ]
    }
   ],
   "source": [
    "print(len(words))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'sort' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-24-307db9cb83bb>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0msort\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mwords\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m: name 'sort' is not defined"
     ]
    }
   ],
   "source": [
    "sort(words)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Arise',\n",
       " 'But',\n",
       " 'It',\n",
       " 'Juliet',\n",
       " 'Who',\n",
       " 'already',\n",
       " 'and',\n",
       " 'breaks',\n",
       " 'east',\n",
       " 'envious',\n",
       " 'fair',\n",
       " 'grief',\n",
       " 'is',\n",
       " 'kill',\n",
       " 'light',\n",
       " 'moon',\n",
       " 'pale',\n",
       " 'sick',\n",
       " 'soft',\n",
       " 'sun',\n",
       " 'the',\n",
       " 'through',\n",
       " 'what',\n",
       " 'window',\n",
       " 'with',\n",
       " 'yonder']"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
