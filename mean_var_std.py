{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "e976b5bb-66fb-499c-95e3-341d76a7d1bf",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "bbd05548-d41c-4b77-8376-635ffee622c3",
   "metadata": {},
   "outputs": [],
   "source": [
    "input_list = [2, 1, 4, 6, 8, 5, 7, 9, 3] "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d739ac43-c246-49fb-9bbe-572298e2a54f",
   "metadata": {},
   "outputs": [],
   "source": [
    "matrix=np.array(input_list).reshape (3,3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "04619bde-6592-4c15-b531-75a42ac4cc2e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def calculate(input_list):\n",
    "    if len(input_list) !=9:\n",
    "        raise ValueError(\"List must contain nine numbers.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "53da869c-a23e-4a06-8b73-b0a3b10d3887",
   "metadata": {},
   "outputs": [],
   "source": [
    "#matrix=np.array(input_list).reshape (3,3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "b6e60b23-b2ab-410c-bc31-9d56ebaadde9",
   "metadata": {},
   "outputs": [],
   "source": [
    "work ={\n",
    "    'mean': [\n",
    "        matrix.mean(axis=0).tolist(), \n",
    "        matrix.mean(axis=1).tolist(),  \n",
    "        matrix.mean().tolist()   \n",
    "    ],\n",
    "    'variance': [\n",
    "        matrix.var(axis=0).tolist(),\n",
    "        matrix.var(axis=1).tolist(),\n",
    "        matrix.var().tolist()\n",
    "    ],\n",
    "    'standard deviation': [\n",
    "        matrix.std(axis=0).tolist(),\n",
    "        matrix.std(axis=1).tolist(),\n",
    "        matrix.std().tolist()\n",
    "    ],\n",
    "    'max': [\n",
    "        matrix.max(axis=0).tolist(),\n",
    "        matrix.max(axis=1).tolist(),\n",
    "        matrix.max().tolist()\n",
    "    ],\n",
    "    'min': [\n",
    "        matrix.min(axis=0).tolist(),\n",
    "        matrix.min(axis=1).tolist(),\n",
    "        matrix.min().tolist()\n",
    "    ],\n",
    "    'sum': [\n",
    "        matrix.sum(axis=0).tolist(),  \n",
    "        matrix.sum(axis=1).tolist(),\n",
    "        matrix.sum().tolist()\n",
    "    ]\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "a3f11bd0-52b6-4b3c-be75-e5244286f950",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'mean': [[5.0, 6.0, 4.0],\n",
       "  [2.3333333333333335, 6.333333333333333, 6.333333333333333],\n",
       "  5.0],\n",
       " 'variance': [[4.666666666666667, 12.666666666666666, 0.6666666666666666],\n",
       "  [1.5555555555555554, 1.5555555555555554, 6.222222222222221],\n",
       "  6.666666666666667],\n",
       " 'standard deviation': [[2.160246899469287,\n",
       "   3.559026084010437,\n",
       "   0.816496580927726],\n",
       "  [1.247219128924647, 1.247219128924647, 2.494438257849294],\n",
       "  2.581988897471611],\n",
       " 'max': [[7, 9, 5], [4, 8, 9], 9],\n",
       " 'min': [[2, 1, 3], [1, 5, 3], 1],\n",
       " 'sum': [[15, 18, 12], [7, 19, 19], 45]}"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "work"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "112e5cfd-6785-47e8-aa4d-9d287d59719d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "anaconda-2024.02-py310",
   "language": "python",
   "name": "conda-env-anaconda-2024.02-py310-py"
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
   "version": "3.10.14"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
