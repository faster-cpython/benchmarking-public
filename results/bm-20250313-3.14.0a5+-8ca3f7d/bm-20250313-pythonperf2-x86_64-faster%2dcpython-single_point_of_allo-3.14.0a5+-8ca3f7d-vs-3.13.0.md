# Results vs. 3.13.0

- fork: faster-cpython
- ref: single_point_of_allo
- machine: linux-x86_64
- commit hash: 8ca3f7d
- commit date: 2025-03-13
- overall geometric mean: 1.017x slower
- HPT reliability: 97.45%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250313-pythonperf2-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-8ca3f7d |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 309 ms: 1.06x slower                                                                   |
| docutils       | 2.83 sec                                                     | 3.05 sec: 1.08x slower                                                                 |
| html5lib       | 73.5 ms                                                      | 72.1 ms: 1.02x faster                                                                  |
| sphinx         | 1.12 sec                                                     | 1.18 sec: 1.05x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250313-pythonperf2-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-8ca3f7d |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 366 ms: 1.27x faster                                                                   |
| async_tree_io              | 843 ms                                                       | 665 ms: 1.27x faster                                                                   |
| async_tree_none            | 376 ms                                                       | 297 ms: 1.26x faster                                                                   |
| async_tree_io_tg           | 831 ms                                                       | 673 ms: 1.23x faster                                                                   |
| async_tree_none_tg         | 346 ms                                                       | 287 ms: 1.21x faster                                                                   |
| async_tree_memoization     | 453 ms                                                       | 377 ms: 1.20x faster                                                                   |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 541 ms: 1.12x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 528 ms: 1.10x faster                                                                   |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                                  |
| async_generators           | 457 ms                                                       | 491 ms: 1.08x slower                                                                   |
| Geometric mean             | (ref)                                                        | 1.14x faster                                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250313-pythonperf2-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-8ca3f7d |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 76.5 ms: 1.06x faster                                                                  |
| pidigits       | 252 ms                                                       | 255 ms: 1.01x slower                                                                   |
| nbody          | 89.3 ms                                                      | 119 ms: 1.33x slower                                                                   |
| Geometric mean | (ref)                                                        | 1.08x slower                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250313-pythonperf2-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-8ca3f7d |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.10 ms: 1.18x faster                                                                  |
| regex_v8       | 26.1 ms                                                      | 23.9 ms: 1.09x faster                                                                  |
| regex_dna      | 247 ms                                                       | 236 ms: 1.05x faster                                                                   |
| regex_compile  | 143 ms                                                       | 148 ms: 1.03x slower                                                                   |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250313-pythonperf2-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-8ca3f7d |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| xml_etree_parse      | 150 ms                                                       | 139 ms: 1.08x faster                                                                   |
| tomli_loads          | 2.46 sec                                                     | 2.41 sec: 1.02x faster                                                                 |
| xml_etree_process    | 61.2 ms                                                      | 61.7 ms: 1.01x slower                                                                  |
| unpickle_pure_python | 217 us                                                       | 222 us: 1.02x slower                                                                   |
| xml_etree_generate   | 86.5 ms                                                      | 89.2 ms: 1.03x slower                                                                  |
| pickle_pure_python   | 323 us                                                       | 345 us: 1.07x slower                                                                   |
| json_dumps           | 11.1 ms                                                      | 12.2 ms: 1.09x slower                                                                  |
| json_loads           | 24.7 us                                                      | 29.1 us: 1.18x slower                                                                  |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                                           |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250313-pythonperf2-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-8ca3f7d |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 16.5 ms: 1.04x slower                                                                  |
| python_startup_no_site | 8.96 ms                                                      | 10.6 ms: 1.18x slower                                                                  |
| Geometric mean         | (ref)                                                        | 1.11x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250313-pythonperf2-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-8ca3f7d |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 26.9 ms: 1.02x slower                                                                  |
| genshi_xml      | 57.1 ms                                                      | 60.3 ms: 1.06x slower                                                                  |
| mako            | 10.4 ms                                                      | 11.1 ms: 1.07x slower                                                                  |
| django_template | 36.4 ms                                                      | 39.2 ms: 1.08x slower                                                                  |
| Geometric mean  | (ref)                                                        | 1.06x slower                                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250313-pythonperf2-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-8ca3f7d |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.6 us                                                      | 29.7 us: 1.30x faster                                                                  |
| deepcopy                   | 392 us                                                       | 306 us: 1.28x faster                                                                   |
| async_tree_memoization_tg  | 466 ms                                                       | 366 ms: 1.27x faster                                                                   |
| async_tree_io              | 843 ms                                                       | 665 ms: 1.27x faster                                                                   |
| async_tree_none            | 376 ms                                                       | 297 ms: 1.26x faster                                                                   |
| async_tree_io_tg           | 831 ms                                                       | 673 ms: 1.23x faster                                                                   |
| async_tree_none_tg         | 346 ms                                                       | 287 ms: 1.21x faster                                                                   |
| async_tree_memoization     | 453 ms                                                       | 377 ms: 1.20x faster                                                                   |
| generators                 | 33.6 ms                                                      | 28.4 ms: 1.19x faster                                                                  |
| go                         | 162 ms                                                       | 137 ms: 1.18x faster                                                                   |
| regex_effbot               | 3.67 ms                                                      | 3.10 ms: 1.18x faster                                                                  |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 541 ms: 1.12x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 528 ms: 1.10x faster                                                                   |
| richards                   | 52.9 ms                                                      | 48.3 ms: 1.10x faster                                                                  |
| regex_v8                   | 26.1 ms                                                      | 23.9 ms: 1.09x faster                                                                  |
| richards_super             | 59.6 ms                                                      | 54.7 ms: 1.09x faster                                                                  |
| xml_etree_parse            | 150 ms                                                       | 139 ms: 1.08x faster                                                                   |
| deepcopy_reduce            | 3.54 us                                                      | 3.29 us: 1.08x faster                                                                  |
| float                      | 81.3 ms                                                      | 76.5 ms: 1.06x faster                                                                  |
| telco                      | 8.79 ms                                                      | 8.39 ms: 1.05x faster                                                                  |
| regex_dna                  | 247 ms                                                       | 236 ms: 1.05x faster                                                                   |
| dulwich_log                | 68.2 ms                                                      | 65.1 ms: 1.05x faster                                                                  |
| hexiom                     | 6.55 ms                                                      | 6.40 ms: 1.02x faster                                                                  |
| tomli_loads                | 2.46 sec                                                     | 2.41 sec: 1.02x faster                                                                 |
| html5lib                   | 73.5 ms                                                      | 72.1 ms: 1.02x faster                                                                  |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                                  |
| connected_components       | 432 ms                                                       | 432 ms: 1.00x faster                                                                   |
| meteor_contest             | 130 ms                                                       | 130 ms: 1.00x slower                                                                   |
| pprint_safe_repr           | 843 ms                                                       | 848 ms: 1.01x slower                                                                   |
| xml_etree_process          | 61.2 ms                                                      | 61.7 ms: 1.01x slower                                                                  |
| coverage                   | 80.0 ms                                                      | 80.7 ms: 1.01x slower                                                                  |
| pidigits                   | 252 ms                                                       | 255 ms: 1.01x slower                                                                   |
| shortest_path              | 460 ms                                                       | 468 ms: 1.02x slower                                                                   |
| create_gc_cycles           | 2.68 ms                                                      | 2.73 ms: 1.02x slower                                                                  |
| unpickle_pure_python       | 217 us                                                       | 222 us: 1.02x slower                                                                   |
| json                       | 5.69 ms                                                      | 5.81 ms: 1.02x slower                                                                  |
| pathlib                    | 17.5 ms                                                      | 17.9 ms: 1.02x slower                                                                  |
| genshi_text                | 26.2 ms                                                      | 26.9 ms: 1.02x slower                                                                  |
| mdp                        | 2.54 sec                                                     | 2.61 sec: 1.03x slower                                                                 |
| xml_etree_generate         | 86.5 ms                                                      | 89.2 ms: 1.03x slower                                                                  |
| sqlite_synth               | 2.91 us                                                      | 3.00 us: 1.03x slower                                                                  |
| regex_compile              | 143 ms                                                       | 148 ms: 1.03x slower                                                                   |
| python_startup             | 15.9 ms                                                      | 16.5 ms: 1.04x slower                                                                  |
| scimark_fft                | 328 ms                                                       | 340 ms: 1.04x slower                                                                   |
| sqlalchemy_declarative     | 148 ms                                                       | 155 ms: 1.04x slower                                                                   |
| scimark_lu                 | 98.7 ms                                                      | 103 ms: 1.04x slower                                                                   |
| thrift                     | 901 us                                                       | 940 us: 1.04x slower                                                                   |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.99 ms: 1.04x slower                                                                  |
| sympy_integrate            | 23.6 ms                                                      | 24.6 ms: 1.04x slower                                                                  |
| deltablue                  | 3.42 ms                                                      | 3.58 ms: 1.05x slower                                                                  |
| sphinx                     | 1.12 sec                                                     | 1.18 sec: 1.05x slower                                                                 |
| 2to3                       | 293 ms                                                       | 309 ms: 1.06x slower                                                                   |
| genshi_xml                 | 57.1 ms                                                      | 60.3 ms: 1.06x slower                                                                  |
| scimark_monte_carlo        | 66.1 ms                                                      | 70.3 ms: 1.06x slower                                                                  |
| bench_thread_pool          | 942 us                                                       | 1.00 ms: 1.07x slower                                                                  |
| sqlalchemy_imperative      | 18.3 ms                                                      | 19.5 ms: 1.07x slower                                                                  |
| pycparser                  | 1.24 sec                                                     | 1.33 sec: 1.07x slower                                                                 |
| pickle_pure_python         | 323 us                                                       | 345 us: 1.07x slower                                                                   |
| spectral_norm              | 97.0 ms                                                      | 104 ms: 1.07x slower                                                                   |
| sympy_sum                  | 155 ms                                                       | 166 ms: 1.07x slower                                                                   |
| mako                       | 10.4 ms                                                      | 11.1 ms: 1.07x slower                                                                  |
| async_generators           | 457 ms                                                       | 491 ms: 1.08x slower                                                                   |
| django_template            | 36.4 ms                                                      | 39.2 ms: 1.08x slower                                                                  |
| docutils                   | 2.83 sec                                                     | 3.05 sec: 1.08x slower                                                                 |
| sympy_str                  | 298 ms                                                       | 324 ms: 1.09x slower                                                                   |
| logging_silent             | 97.9 ns                                                      | 107 ns: 1.09x slower                                                                   |
| json_dumps                 | 11.1 ms                                                      | 12.2 ms: 1.09x slower                                                                  |
| logging_simple             | 6.39 us                                                      | 7.00 us: 1.10x slower                                                                  |
| logging_format             | 6.94 us                                                      | 7.66 us: 1.10x slower                                                                  |
| sympy_expand               | 509 ms                                                       | 566 ms: 1.11x slower                                                                   |
| bpe_tokeniser              | 5.09 sec                                                     | 5.66 sec: 1.11x slower                                                                 |
| comprehensions             | 17.0 us                                                      | 19.1 us: 1.12x slower                                                                  |
| nqueens                    | 90.7 ms                                                      | 104 ms: 1.14x slower                                                                   |
| crypto_pyaes               | 73.3 ms                                                      | 85.9 ms: 1.17x slower                                                                  |
| python_startup_no_site     | 8.96 ms                                                      | 10.6 ms: 1.18x slower                                                                  |
| json_loads                 | 24.7 us                                                      | 29.1 us: 1.18x slower                                                                  |
| chaos                      | 60.2 ms                                                      | 71.1 ms: 1.18x slower                                                                  |
| raytrace                   | 273 ms                                                       | 324 ms: 1.19x slower                                                                   |
| many_optionals             | 930 us                                                       | 1.12 ms: 1.20x slower                                                                  |
| typing_runtime_protocols   | 169 us                                                       | 205 us: 1.21x slower                                                                   |
| fannkuch                   | 363 ms                                                       | 453 ms: 1.25x slower                                                                   |
| nbody                      | 89.3 ms                                                      | 119 ms: 1.33x slower                                                                   |
| gc_traversal               | 4.74 ms                                                      | 6.32 ms: 1.33x slower                                                                  |
| subparsers                 | 17.5 ms                                                      | 24.9 ms: 1.43x slower                                                                  |
| bench_mp_pool              | 5.12 ms                                                      | 1.57 sec: 306.73x slower                                                               |
| Geometric mean             | (ref)                                                        | 1.08x slower                                                                           |

Benchmark hidden because not significant (7): pylint, k_core, asyncio_websockets, pyflate, scimark_sor, pprint_pformat, xml_etree_iterparse
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250313-3.14.0a5+-8ca3f7d/bm-20250313-pythonperf2-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-8ca3f7d.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.017x slower

# HPT report

- Reliability score: 97.45% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.03x