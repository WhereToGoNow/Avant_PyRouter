"""Test for router.py."""

import random

from router import Path, Graph, Router


def test_random():
    """Randomize all the things. We just see whether the algorithm works
    without error.
    """
    num_nodes = 100
    v_start, v_end = 0, num_nodes - 1
    length_max, time_max = 10, 31

    graph = Graph(num_nodes)
    router = Router(graph, verbose=True)

    print('Find the best path from %d to %d... (Time <= %.3f, Length <= %.3f)'
          % (v_start, v_end, time_max, length_max))

    for v in range(num_nodes):
        graph.time_nodes[v] = random.uniform(1, 3)
        graph.eval_nodes[v] = random.uniform(1, 10)

        for v_next in range(num_nodes):
            graph.time_edges[v][v_next] = random.uniform(1, 5)

    path = router.find_best_path(v_start, v_end, length_max, time_max)

    print('Best path: %s' % path)


def test_unique():
    """The unique best path is 0 -> 3 -> 6 -> ... -> 30. Let's see
    whether our algorithm gets close to this path.
    """
    num_nodes = 31
    v_start, v_end = 0, num_nodes - num_nodes % 3
    length_max = int(num_nodes / 3) + 1
    time_max = 10000

    graph = Graph(num_nodes)
    router = Router(graph, verbose=True)

    print('Find the best path from %d to %d... (Time <= %.3f, Length <= %.3f)'
          % (v_start, v_end, time_max, length_max))

    for v in range(num_nodes):
        graph.time_nodes[v] = random.uniform(4, 6)
        graph.eval_nodes[v] = random.uniform(1, 3)

        for v_next in range(num_nodes):
            graph.time_edges[v][v_next] = random.uniform(4, 6)

    # let 0 -> 3 -> ... -> 30 be the best path
    for v in range(0, num_nodes, 3):
        graph.time_nodes[v] = random.uniform(1, 4)
        graph.eval_nodes[v] = random.uniform(3, 5)

        if v + 3 < num_nodes:
            graph.time_edges[v][v + 3] = random.uniform(1, 4)

    # real best path 0 -> 3 -> ... -> 30
    path_real = Path(graph, [v_start, v_end])

    for i in range(length_max - 2):
        path_real.add_node(i + 1, (i + 1) * 3)

    # path guessed by the algorithm
    path_guess = router.find_best_path(v_start, v_end, length_max, time_max)

    # compare them
    print('Best path (guess): %s (Point: %.3f)'
          % (path_guess, path_guess.point))

    print('Best path (real): %s (Point: %.3f)'
          % (path_real, path_real.point))


if __name__ == '__main__':
    print('[Test_random]')
    test_random()

    print('\n[Test_unique]')
    test_unique()
