# Results vs. 3.13.0

- fork: kumaraditya303
- ref: per_thread_tasks
- machine: linux-x86_64
- commit hash: 4014e70
- commit date: 2025-01-29
- overall geometric mean: 1.053x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-pythonperf2-x86_64-kumaraditya303-per_thread_tasks-3.14.0a4+-4014e70 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 282 ms: 1.04x faster                                                             |
| docutils       | 2.83 sec                                                     | 2.88 sec: 1.02x slower                                                           |
| html5lib       | 73.5 ms                                                      | 66.5 ms: 1.10x faster                                                            |
| sphinx         | 1.12 sec                                                     | 1.11 sec: 1.01x faster                                                           |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-pythonperf2-x86_64-kumaraditya303-per_thread_tasks-3.14.0a4+-4014e70 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 335 ms: 1.39x faster                                                             |
| async_tree_io              | 843 ms                                                       | 644 ms: 1.31x faster                                                             |
| async_tree_none            | 376 ms                                                       | 289 ms: 1.30x faster                                                             |
| async_tree_memoization     | 453 ms                                                       | 350 ms: 1.30x faster                                                             |
| async_tree_io_tg           | 831 ms                                                       | 648 ms: 1.28x faster                                                             |
| async_tree_none_tg         | 346 ms                                                       | 277 ms: 1.25x faster                                                             |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 516 ms: 1.17x faster                                                             |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 504 ms: 1.15x faster                                                             |
| async_generators           | 457 ms                                                       | 413 ms: 1.11x faster                                                             |
| coroutines                 | 21.6 ms                                                      | 20.8 ms: 1.04x faster                                                            |
| Geometric mean             | (ref)                                                        | 1.20x faster                                                                     |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-pythonperf2-x86_64-kumaraditya303-per_thread_tasks-3.14.0a4+-4014e70 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 69.6 ms: 1.17x faster                                                            |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                     |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-pythonperf2-x86_64-kumaraditya303-per_thread_tasks-3.14.0a4+-4014e70 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.17 ms: 1.16x faster                                                            |
| regex_compile  | 143 ms                                                       | 134 ms: 1.06x faster                                                             |
| regex_v8       | 26.1 ms                                                      | 25.5 ms: 1.02x faster                                                            |
| regex_dna      | 247 ms                                                       | 249 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-pythonperf2-x86_64-kumaraditya303-per_thread_tasks-3.14.0a4+-4014e70 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.05 sec: 1.20x faster                                                           |
| xml_etree_parse      | 150 ms                                                       | 136 ms: 1.10x faster                                                             |
| unpickle_pure_python | 217 us                                                       | 207 us: 1.05x faster                                                             |
| xml_etree_process    | 61.2 ms                                                      | 58.4 ms: 1.05x faster                                                            |
| xml_etree_generate   | 86.5 ms                                                      | 82.9 ms: 1.04x faster                                                            |
| xml_etree_iterparse  | 103 ms                                                       | 106 ms: 1.03x slower                                                             |
| json_dumps           | 11.1 ms                                                      | 11.6 ms: 1.05x slower                                                            |
| json_loads           | 24.7 us                                                      | 37.8 us: 1.53x slower                                                            |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                     |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-pythonperf2-x86_64-kumaraditya303-per_thread_tasks-3.14.0a4+-4014e70 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup | 15.9 ms                                                      | 16.0 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                     |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-pythonperf2-x86_64-kumaraditya303-per_thread_tasks-3.14.0a4+-4014e70 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.0 ms: 1.14x faster                                                            |
| genshi_xml      | 57.1 ms                                                      | 53.0 ms: 1.08x faster                                                            |
| django_template | 36.4 ms                                                      | 36.8 ms: 1.01x slower                                                            |
| mako            | 10.4 ms                                                      | 10.9 ms: 1.06x slower                                                            |
| Geometric mean  | (ref)                                                        | 1.04x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-pythonperf2-x86_64-kumaraditya303-per_thread_tasks-3.14.0a4+-4014e70 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| deepcopy                   | 392 us                                                       | 280 us: 1.40x faster                                                             |
| async_tree_memoization_tg  | 466 ms                                                       | 335 ms: 1.39x faster                                                             |
| async_tree_io              | 843 ms                                                       | 644 ms: 1.31x faster                                                             |
| deepcopy_memo              | 38.6 us                                                      | 29.5 us: 1.31x faster                                                            |
| async_tree_none            | 376 ms                                                       | 289 ms: 1.30x faster                                                             |
| async_tree_memoization     | 453 ms                                                       | 350 ms: 1.30x faster                                                             |
| async_tree_io_tg           | 831 ms                                                       | 648 ms: 1.28x faster                                                             |
| go                         | 162 ms                                                       | 129 ms: 1.26x faster                                                             |
| async_tree_none_tg         | 346 ms                                                       | 277 ms: 1.25x faster                                                             |
| deepcopy_reduce            | 3.54 us                                                      | 2.91 us: 1.22x faster                                                            |
| tomli_loads                | 2.46 sec                                                     | 2.05 sec: 1.20x faster                                                           |
| generators                 | 33.6 ms                                                      | 28.6 ms: 1.18x faster                                                            |
| pyflate                    | 503 ms                                                       | 429 ms: 1.17x faster                                                             |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 516 ms: 1.17x faster                                                             |
| float                      | 81.3 ms                                                      | 69.6 ms: 1.17x faster                                                            |
| regex_effbot               | 3.67 ms                                                      | 3.17 ms: 1.16x faster                                                            |
| spectral_norm              | 97.0 ms                                                      | 84.0 ms: 1.15x faster                                                            |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 504 ms: 1.15x faster                                                             |
| genshi_text                | 26.2 ms                                                      | 23.0 ms: 1.14x faster                                                            |
| telco                      | 8.79 ms                                                      | 7.75 ms: 1.13x faster                                                            |
| pathlib                    | 17.5 ms                                                      | 15.5 ms: 1.13x faster                                                            |
| richards_super             | 59.6 ms                                                      | 53.1 ms: 1.12x faster                                                            |
| richards                   | 52.9 ms                                                      | 47.9 ms: 1.11x faster                                                            |
| async_generators           | 457 ms                                                       | 413 ms: 1.11x faster                                                             |
| html5lib                   | 73.5 ms                                                      | 66.5 ms: 1.10x faster                                                            |
| xml_etree_parse            | 150 ms                                                       | 136 ms: 1.10x faster                                                             |
| scimark_sor                | 123 ms                                                       | 112 ms: 1.10x faster                                                             |
| bpe_tokeniser              | 5.09 sec                                                     | 4.64 sec: 1.10x faster                                                           |
| pylint                     | 347 ms                                                       | 317 ms: 1.09x faster                                                             |
| hexiom                     | 6.55 ms                                                      | 6.06 ms: 1.08x faster                                                            |
| scimark_fft                | 328 ms                                                       | 303 ms: 1.08x faster                                                             |
| pprint_pformat             | 1.72 sec                                                     | 1.59 sec: 1.08x faster                                                           |
| genshi_xml                 | 57.1 ms                                                      | 53.0 ms: 1.08x faster                                                            |
| pprint_safe_repr           | 843 ms                                                       | 786 ms: 1.07x faster                                                             |
| thrift                     | 901 us                                                       | 846 us: 1.07x faster                                                             |
| regex_compile              | 143 ms                                                       | 134 ms: 1.06x faster                                                             |
| unpickle_pure_python       | 217 us                                                       | 207 us: 1.05x faster                                                             |
| logging_simple             | 6.39 us                                                      | 6.09 us: 1.05x faster                                                            |
| sqlglot_parse              | 1.40 ms                                                      | 1.33 ms: 1.05x faster                                                            |
| xml_etree_process          | 61.2 ms                                                      | 58.4 ms: 1.05x faster                                                            |
| k_core                     | 2.17 sec                                                     | 2.07 sec: 1.05x faster                                                           |
| meteor_contest             | 130 ms                                                       | 124 ms: 1.05x faster                                                             |
| xml_etree_generate         | 86.5 ms                                                      | 82.9 ms: 1.04x faster                                                            |
| sqlalchemy_imperative      | 18.3 ms                                                      | 17.5 ms: 1.04x faster                                                            |
| sqlalchemy_declarative     | 148 ms                                                       | 142 ms: 1.04x faster                                                             |
| mdp                        | 2.54 sec                                                     | 2.45 sec: 1.04x faster                                                           |
| coroutines                 | 21.6 ms                                                      | 20.8 ms: 1.04x faster                                                            |
| sqlglot_transpile          | 1.79 ms                                                      | 1.72 ms: 1.04x faster                                                            |
| 2to3                       | 293 ms                                                       | 282 ms: 1.04x faster                                                             |
| sqlglot_normalize          | 119 ms                                                       | 115 ms: 1.04x faster                                                             |
| connected_components       | 432 ms                                                       | 417 ms: 1.04x faster                                                             |
| scimark_lu                 | 98.7 ms                                                      | 95.4 ms: 1.03x faster                                                            |
| nqueens                    | 90.7 ms                                                      | 87.9 ms: 1.03x faster                                                            |
| sympy_str                  | 298 ms                                                       | 290 ms: 1.03x faster                                                             |
| sympy_expand               | 509 ms                                                       | 495 ms: 1.03x faster                                                             |
| sqlite_synth               | 2.91 us                                                      | 2.82 us: 1.03x faster                                                            |
| shortest_path              | 460 ms                                                       | 447 ms: 1.03x faster                                                             |
| coverage                   | 80.0 ms                                                      | 77.8 ms: 1.03x faster                                                            |
| sqlglot_optimize           | 59.3 ms                                                      | 57.7 ms: 1.03x faster                                                            |
| chaos                      | 60.2 ms                                                      | 58.7 ms: 1.03x faster                                                            |
| logging_format             | 6.94 us                                                      | 6.77 us: 1.03x faster                                                            |
| regex_v8                   | 26.1 ms                                                      | 25.5 ms: 1.02x faster                                                            |
| bench_thread_pool          | 942 us                                                       | 921 us: 1.02x faster                                                             |
| dulwich_log                | 68.2 ms                                                      | 66.8 ms: 1.02x faster                                                            |
| scimark_monte_carlo        | 66.1 ms                                                      | 64.9 ms: 1.02x faster                                                            |
| sympy_sum                  | 155 ms                                                       | 152 ms: 1.02x faster                                                             |
| sympy_integrate            | 23.6 ms                                                      | 23.2 ms: 1.02x faster                                                            |
| deltablue                  | 3.42 ms                                                      | 3.37 ms: 1.01x faster                                                            |
| sphinx                     | 1.12 sec                                                     | 1.11 sec: 1.01x faster                                                           |
| python_startup             | 15.9 ms                                                      | 16.0 ms: 1.00x slower                                                            |
| pidigits                   | 252 ms                                                       | 254 ms: 1.01x slower                                                             |
| regex_dna                  | 247 ms                                                       | 249 ms: 1.01x slower                                                             |
| django_template            | 36.4 ms                                                      | 36.8 ms: 1.01x slower                                                            |
| pycparser                  | 1.24 sec                                                     | 1.26 sec: 1.01x slower                                                           |
| fannkuch                   | 363 ms                                                       | 368 ms: 1.01x slower                                                             |
| docutils                   | 2.83 sec                                                     | 2.88 sec: 1.02x slower                                                           |
| typing_runtime_protocols   | 169 us                                                       | 172 us: 1.02x slower                                                             |
| xml_etree_iterparse        | 103 ms                                                       | 106 ms: 1.03x slower                                                             |
| comprehensions             | 17.0 us                                                      | 17.5 us: 1.03x slower                                                            |
| json_dumps                 | 11.1 ms                                                      | 11.6 ms: 1.05x slower                                                            |
| create_gc_cycles           | 2.68 ms                                                      | 2.81 ms: 1.05x slower                                                            |
| mako                       | 10.4 ms                                                      | 10.9 ms: 1.06x slower                                                            |
| many_optionals             | 930 us                                                       | 1.01 ms: 1.08x slower                                                            |
| json                       | 5.69 ms                                                      | 6.88 ms: 1.21x slower                                                            |
| subparsers                 | 17.5 ms                                                      | 22.5 ms: 1.29x slower                                                            |
| gc_traversal               | 4.74 ms                                                      | 6.58 ms: 1.39x slower                                                            |
| json_loads                 | 24.7 us                                                      | 37.8 us: 1.53x slower                                                            |
| bench_mp_pool              | 5.12 ms                                                      | 929 ms: 181.40x slower                                                           |
| Geometric mean             | (ref)                                                        | 1.00x slower                                                                     |

Benchmark hidden because not significant (8): logging_silent, pickle_pure_python, asyncio_websockets, python_startup_no_site, crypto_pyaes, nbody, raytrace, scimark_sparse_mat_mult
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.053x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.27x