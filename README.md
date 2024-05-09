# goit-algo-hw-05

Analysis:

Based on the time measurements:

For pattern1 in text1:
•⁠  ⁠Boyer-Moore: 0.04595
•⁠  ⁠KMP: 0.22225
•⁠  ⁠Rabin-Karp: 0.54741

For pattern2 in text2:
•⁠  ⁠Boyer-Moore: 0.09667
•⁠  ⁠KMP: 0.79143
•⁠  ⁠Rabin-Karp: 2.03721

Boyer-Moore generally performs the best, followed by KMP, and then Rabin-Karp, especially evident in longer texts and patterns.

For no_pattern:

•⁠  ⁠Boyer-Moore: 
  - text1: 0.07427
  - text2: 0.08982

•⁠  ⁠KMP: 
  - text1: 0.86506
  - text2: 1.41747

•⁠  ⁠Rabin-Karp: 
  - text1: 2.51801
  - text2: 3.73805

Boyer-Moore still maintains the best performance, followed by KMP and then Rabin-Karp, with Rabin-Karp showing the slowest performance in both cases.