# PyRouter

Implementation of Ryu's routing algorithm in python.

### Requirements
- Python 2.X or 3.X
- Tested on python 2.7, python 3.6, pypy 5.7.1

### How to use
```python
from router import Graph, Router

def do_work():
    # configurations
    num_nodes = ...
    v_start, v_end = ..., ...
    time_max, length_max = ..., ...
    
    # initialize the graph
    graph = Graph(num_nodes)
    router = Router(graph, verbose=False)
    
    for v in range(num_nodes):
        graph.time_nodes[v] = ...
        graph.eval_nodes[v] = ...
        
        for v_next in range(num_nodes):
            graph.time_edges[v][v_next] = ...
    
    # generate the path
    path = router.find_best_path(v_start, v_end, length_max, time_max)
    
    # play with the generated path
    # ...
```

### How to test
Run `test.py`.

### TODO
- Connect the router with the evaluator.
- Test with some real-world data.

### Example output
```
[Test_random]
Find the best path from 0 to 99... (Time <= 31.000, Length <= 10.000)
> [0 -> 99]
  (Point: 4.218, Time: 5.809)
> [0 -> 27 -> 99]
  (Point: 13.738, Time: 11.077)
> [0 -> 23 -> 27 -> 99]
  (Point: 23.127, Time: 14.545)
> [0 -> 55 -> 23 -> 27 -> 99]
  (Point: 32.436, Time: 15.242)
> [0 -> 55 -> 23 -> 84 -> 27 -> 99]
  (Point: 41.715, Time: 18.490)
> [0 -> 55 -> 23 -> 84 -> 25 -> 27 -> 99]
  (Point: 50.961, Time: 21.911)
> [0 -> 55 -> 9 -> 23 -> 84 -> 25 -> 27 -> 99]
  (Point: 60.038, Time: 26.551)
> [0 -> 46 -> 55 -> 9 -> 23 -> 84 -> 25 -> 27 -> 99]
  (Point: 69.026, Time: 30.444)
> [0 -> 46 -> 55 -> 9 -> 23 -> 84 -> 25 -> 27 -> 99]
  (Point: 69.026, Time: 30.444)
Best path: [0 -> 46 -> 55 -> 9 -> 23 -> 84 -> 25 -> 27 -> 99]

[Test_unique]
Find the best path from 0 to 30... (Time <= 10000.000, Length <= 11.000)
> [0 -> 30]
  (Point: 6.293, Time: 8.213)
> [0 -> 24 -> 30]
  (Point: 10.555, Time: 15.788)
> [0 -> 9 -> 24 -> 30]
  (Point: 14.726, Time: 22.028)
> [0 -> 9 -> 12 -> 24 -> 30]
  (Point: 18.506, Time: 28.222)
> [0 -> 9 -> 12 -> 24 -> 6 -> 30]
  (Point: 22.266, Time: 33.710)
> [0 -> 9 -> 12 -> 18 -> 24 -> 6 -> 30]
  (Point: 25.979, Time: 43.121)
> [0 -> 9 -> 12 -> 18 -> 24 -> 6 -> 27 -> 30]
  (Point: 29.482, Time: 48.795)
> [0 -> 9 -> 12 -> 15 -> 18 -> 24 -> 6 -> 27 -> 30]
  (Point: 32.567, Time: 49.919)
> [0 -> 9 -> 12 -> 15 -> 18 -> 24 -> 3 -> 6 -> 27 -> 30]
  (Point: 35.599, Time: 54.087)
> [0 -> 9 -> 12 -> 15 -> 18 -> 21 -> 24 -> 3 -> 6 -> 27 -> 30]
  (Point: 38.145, Time: 55.685)
Best path (guess): [0 -> 9 -> 12 -> 15 -> 18 -> 21 -> 24 -> 3 -> 6 -> 27 -> 30] (Point: 38.145)
Best path (real): [0 -> 3 -> 6 -> 9 -> 12 -> 15 -> 18 -> 21 -> 24 -> 27 -> 30] (Point: 38.291)
```
