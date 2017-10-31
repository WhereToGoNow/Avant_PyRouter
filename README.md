# PyRouter

Implementation of Ryu's routing algorithm in python.

### Requirements
- Python 2.X or 3.X
- Tested on python 2.7, python 3.6, pypy 5.7.1

### TODO
- Connect the router with the evaluator.
- Test with some real-world data.

### How to test
Run `test.py`.

### Example output
```
[Test_random]
Find the best path from 0 to 99... (Time <= 31.000, Length <= 10.000)
> [0 -> 99]
  (Point: 10.493, Time: 6.734)
> [0 -> 94 -> 99]
  (Point: 19.860, Time: 8.522)
> [0 -> 94 -> 90 -> 99]
  (Point: 29.229, Time: 12.976)
> [0 -> 94 -> 90 -> 68 -> 99]
  (Point: 38.575, Time: 18.864)
> [0 -> 94 -> 90 -> 28 -> 68 -> 99]
  (Point: 47.880, Time: 21.285)
> [0 -> 94 -> 90 -> 28 -> 32 -> 68 -> 99]
  (Point: 57.146, Time: 24.620)
> [0 -> 94 -> 90 -> 21 -> 28 -> 32 -> 68 -> 99]
  (Point: 66.365, Time: 26.833)
> [0 -> 94 -> 90 -> 72 -> 21 -> 28 -> 32 -> 68 -> 99]
  (Point: 75.622, Time: 29.081)
> [0 -> 94 -> 90 -> 72 -> 21 -> 28 -> 32 -> 39 -> 68 -> 99]
  (Point: 84.358, Time: 30.926)
Best path: [0 -> 94 -> 90 -> 72 -> 21 -> 28 -> 32 -> 39 -> 68 -> 99]

[Test_unique]
Find the best path from 0 to 30... (Time <= 10000.000, Length <= 11.000)
> [0 -> 30]
  (Point: 6.659, Time: 12.280)
> [0 -> 27 -> 30]
  (Point: 10.889, Time: 17.026)
> [0 -> 18 -> 27 -> 30]
  (Point: 14.865, Time: 23.083)
> [0 -> 3 -> 18 -> 27 -> 30]
  (Point: 18.682, Time: 30.469)
> [0 -> 3 -> 18 -> 24 -> 27 -> 30]
  (Point: 22.497, Time: 38.050)
> [0 -> 3 -> 18 -> 12 -> 24 -> 27 -> 30]
  (Point: 26.193, Time: 44.614)
> [0 -> 3 -> 18 -> 12 -> 15 -> 24 -> 27 -> 30]
  (Point: 29.903, Time: 46.529)
> [0 -> 3 -> 18 -> 12 -> 15 -> 21 -> 24 -> 27 -> 30]
  (Point: 33.191, Time: 51.415)
> [0 -> 3 -> 6 -> 18 -> 12 -> 15 -> 21 -> 24 -> 27 -> 30]
  (Point: 36.385, Time: 57.167)
> [0 -> 3 -> 6 -> 9 -> 18 -> 12 -> 15 -> 21 -> 24 -> 27 -> 30]
  (Point: 39.587, Time: 60.971)
Best path (guess): [0 -> 3 -> 6 -> 9 -> 18 -> 12 -> 15 -> 21 -> 24 -> 27 -> 30] (Point: 39.587)
Best path (real): [0 -> 3 -> 6 -> 9 -> 12 -> 15 -> 18 -> 21 -> 24 -> 27 -> 30] (Point: 39.761)
```
