{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0f44fdac",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the radius of circle: 1.1\n",
      "3.8013271108436504\n"
     ]
    }
   ],
   "source": [
    "#Program to find Area of Circle\n",
    "rad=float(input(\"Enter the radius of circle: \"))\n",
    "from math import pi\n",
    "area=(pi*rad**2)\n",
    "print(area)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "fa774a9f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Input the Filename: abc.py\n",
      "The extension of the file is : 'py'\n"
     ]
    }
   ],
   "source": [
    "#Program to find Extension Checker\n",
    "filename = input(\"Input the Filename: \")\n",
    "f_extns = filename.split(\".\")\n",
    "print (\"The extension of the file is : \" + repr(f_extns[-1]))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bbb3d024",
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
