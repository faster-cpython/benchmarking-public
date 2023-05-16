
# Results vs. base

- fork: faster-cpython
- ref: no_local_eval_breake
- machine: linux-x86_64
- commit hash: 4d1b4d4
- commit date: 2023-05-12
- overall geometric mean: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230515-pythonperf2-x86_64-python-b378d991f8cd41c33416-3.12.0a7+-b378d99 | bm-20230512-pythonperf2-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a7+-4d1b4d4 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                                       | 283 ms: 1.01x faster                                                                   |
| docutils       | 2.88 sec                                                                     | 2.87 sec: 1.00x faster                                                                 |
| Geometric mean | (ref)                                                                        | 1.01x faster                                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230515-pythonperf2-x86_64-python-b378d991f8cd41c33416-3.12.0a7+-b378d99 | bm-20230512-pythonperf2-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a7+-4d1b4d4 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| float          | 79.2 ms                                                                      | 77.7 ms: 1.02x faster                                                                  |
| Geometric mean | (ref)                                                                        | 1.01x faster                                                                           |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230515-pythonperf2-x86_64-python-b378d991f8cd41c33416-3.12.0a7+-b378d99 | bm-20230512-pythonperf2-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a7+-4d1b4d4 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_v8       | 24.4 ms                                                                      | 23.5 ms: 1.04x faster                                                                  |
| regex_dna      | 235 ms                                                                       | 230 ms: 1.02x faster                                                                   |
| regex_compile  | 145 ms                                                                       | 143 ms: 1.01x faster                                                                   |
| regex_effbot   | 3.47 ms                                                                      | 3.52 ms: 1.01x slower                                                                  |
| Geometric mean | (ref)                                                                        | 1.01x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230515-pythonperf2-x86_64-python-b378d991f8cd41c33416-3.12.0a7+-b378d99 | bm-20230512-pythonperf2-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a7+-4d1b4d4 |
|----------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                                      | 85.3 ms: 1.02x faster                                                                  |
| xml_etree_process    | 59.8 ms                                                                      | 58.7 ms: 1.02x faster                                                                  |
| xml_etree_parse      | 149 ms                                                                       | 147 ms: 1.02x faster                                                                   |
| tomli_loads          | 2.19 sec                                                                     | 2.16 sec: 1.01x faster                                                                 |
| pickle_pure_python   | 325 us                                                                       | 321 us: 1.01x faster                                                                   |
| unpickle_pure_python | 206 us                                                                       | 204 us: 1.01x faster                                                                   |
| pickle               | 10.0 us                                                                      | 10.1 us: 1.00x slower                                                                  |
| pickle_dict          | 31.8 us                                                                      | 32.0 us: 1.01x slower                                                                  |
| pickle_list          | 4.24 us                                                                      | 4.32 us: 1.02x slower                                                                  |
| unpickle_list        | 4.67 us                                                                      | 4.88 us: 1.04x slower                                                                  |
| Geometric mean       | (ref)                                                                        | 1.00x faster                                                                           |

Benchmark hidden because not significant (4): unpickle, json_loads, json_dumps, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230515-pythonperf2-x86_64-python-b378d991f8cd41c33416-3.12.0a7+-b378d99 | bm-20230512-pythonperf2-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a7+-4d1b4d4 |
|------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.42 ms                                                                      | 8.39 ms: 1.00x faster                                                                  |
| python_startup         | 11.4 ms                                                                      | 11.4 ms: 1.00x faster                                                                  |
| Geometric mean         | (ref)                                                                        | 1.00x faster                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230515-pythonperf2-x86_64-python-b378d991f8cd41c33416-3.12.0a7+-b378d99 | bm-20230512-pythonperf2-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a7+-4d1b4d4 |
|-----------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| mako      | 10.1 ms                                                                      | 9.89 ms: 1.03x faster                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20230515-pythonperf2-x86_64-python-b378d991f8cd41c33416-3.12.0a7+-b378d99 | bm-20230512-pythonperf2-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a7+-4d1b4d4 |
|--------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| gc_traversal             | 4.20 ms                                                                      | 3.80 ms: 1.11x faster                                                                  |
| scimark_sor              | 113 ms                                                                       | 107 ms: 1.06x faster                                                                   |
| pyflate                  | 463 ms                                                                       | 441 ms: 1.05x faster                                                                   |
| logging_silent           | 94.5 ns                                                                      | 90.5 ns: 1.04x faster                                                                  |
| richards                 | 45.4 ms                                                                      | 43.5 ms: 1.04x faster                                                                  |
| pycparser                | 1.28 sec                                                                     | 1.23 sec: 1.04x faster                                                                 |
| regex_v8                 | 24.4 ms                                                                      | 23.5 ms: 1.04x faster                                                                  |
| deepcopy_memo            | 37.2 us                                                                      | 35.9 us: 1.04x faster                                                                  |
| pprint_safe_repr         | 815 ms                                                                       | 788 ms: 1.04x faster                                                                   |
| unpack_sequence          | 53.4 ns                                                                      | 51.6 ns: 1.03x faster                                                                  |
| pprint_pformat           | 1.66 sec                                                                     | 1.61 sec: 1.03x faster                                                                 |
| scimark_lu               | 101 ms                                                                       | 98.0 ms: 1.03x faster                                                                  |
| go                       | 148 ms                                                                       | 144 ms: 1.03x faster                                                                   |
| richards_super           | 51.5 ms                                                                      | 50.1 ms: 1.03x faster                                                                  |
| create_gc_cycles         | 1.68 ms                                                                      | 1.63 ms: 1.03x faster                                                                  |
| mako                     | 10.1 ms                                                                      | 9.89 ms: 1.03x faster                                                                  |
| sqlite_synth             | 2.71 us                                                                      | 2.65 us: 1.02x faster                                                                  |
| typing_runtime_protocols | 155 us                                                                       | 151 us: 1.02x faster                                                                   |
| crypto_pyaes             | 81.4 ms                                                                      | 79.5 ms: 1.02x faster                                                                  |
| float                    | 79.2 ms                                                                      | 77.7 ms: 1.02x faster                                                                  |
| scimark_monte_carlo      | 69.9 ms                                                                      | 68.5 ms: 1.02x faster                                                                  |
| regex_dna                | 235 ms                                                                       | 230 ms: 1.02x faster                                                                   |
| xml_etree_generate       | 87.0 ms                                                                      | 85.3 ms: 1.02x faster                                                                  |
| xml_etree_process        | 59.8 ms                                                                      | 58.7 ms: 1.02x faster                                                                  |
| xml_etree_parse          | 149 ms                                                                       | 147 ms: 1.02x faster                                                                   |
| async_tree_cpu_io_mixed  | 711 ms                                                                       | 698 ms: 1.02x faster                                                                   |
| scimark_fft              | 305 ms                                                                       | 300 ms: 1.02x faster                                                                   |
| async_generators         | 392 ms                                                                       | 386 ms: 1.02x faster                                                                   |
| coroutines               | 22.7 ms                                                                      | 22.4 ms: 1.02x faster                                                                  |
| generators               | 36.3 ms                                                                      | 35.7 ms: 1.01x faster                                                                  |
| async_tree_none          | 465 ms                                                                       | 458 ms: 1.01x faster                                                                   |
| mdp                      | 2.56 sec                                                                     | 2.52 sec: 1.01x faster                                                                 |
| tomli_loads              | 2.19 sec                                                                     | 2.16 sec: 1.01x faster                                                                 |
| regex_compile            | 145 ms                                                                       | 143 ms: 1.01x faster                                                                   |
| pickle_pure_python       | 325 us                                                                       | 321 us: 1.01x faster                                                                   |
| async_tree_memoization   | 558 ms                                                                       | 550 ms: 1.01x faster                                                                   |
| asyncio_tcp              | 385 ms                                                                       | 380 ms: 1.01x faster                                                                   |
| deltablue                | 3.23 ms                                                                      | 3.20 ms: 1.01x faster                                                                  |
| sqlglot_parse            | 1.40 ms                                                                      | 1.38 ms: 1.01x faster                                                                  |
| async_tree_io            | 1.06 sec                                                                     | 1.05 sec: 1.01x faster                                                                 |
| 2to3                     | 285 ms                                                                       | 283 ms: 1.01x faster                                                                   |
| unpickle_pure_python     | 206 us                                                                       | 204 us: 1.01x faster                                                                   |
| chaos                    | 64.1 ms                                                                      | 63.6 ms: 1.01x faster                                                                  |
| hexiom                   | 5.83 ms                                                                      | 5.79 ms: 1.01x faster                                                                  |
| spectral_norm            | 90.1 ms                                                                      | 89.5 ms: 1.01x faster                                                                  |
| dask                     | 559 ms                                                                       | 556 ms: 1.01x faster                                                                   |
| comprehensions           | 21.8 us                                                                      | 21.7 us: 1.01x faster                                                                  |
| docutils                 | 2.88 sec                                                                     | 2.87 sec: 1.00x faster                                                                 |
| python_startup_no_site   | 8.42 ms                                                                      | 8.39 ms: 1.00x faster                                                                  |
| dulwich_log              | 65.5 ms                                                                      | 65.3 ms: 1.00x faster                                                                  |
| python_startup           | 11.4 ms                                                                      | 11.4 ms: 1.00x faster                                                                  |
| sqlglot_optimize         | 58.0 ms                                                                      | 58.2 ms: 1.00x slower                                                                  |
| pickle                   | 10.0 us                                                                      | 10.1 us: 1.00x slower                                                                  |
| pickle_dict              | 31.8 us                                                                      | 32.0 us: 1.01x slower                                                                  |
| deepcopy_reduce          | 3.37 us                                                                      | 3.39 us: 1.01x slower                                                                  |
| regex_effbot             | 3.47 ms                                                                      | 3.52 ms: 1.01x slower                                                                  |
| fannkuch                 | 349 ms                                                                       | 356 ms: 1.02x slower                                                                   |
| pickle_list              | 4.24 us                                                                      | 4.32 us: 1.02x slower                                                                  |
| meteor_contest           | 127 ms                                                                       | 130 ms: 1.02x slower                                                                   |
| coverage                 | 86.8 ms                                                                      | 90.5 ms: 1.04x slower                                                                  |
| unpickle_list            | 4.67 us                                                                      | 4.88 us: 1.04x slower                                                                  |
| Geometric mean           | (ref)                                                                        | 1.01x faster                                                                           |

Benchmark hidden because not significant (22): telco, tornado_http, unpickle, sqlglot_transpile, pathlib, sqlglot_normalize, raytrace, json_loads, bench_mp_pool, logging_format, asyncio_tcp_ssl, nqueens, nbody, logging_simple, json_dumps, pidigits, mypy2, deepcopy, json, xml_etree_iterparse, bench_thread_pool, scimark_sparse_mat_mult
