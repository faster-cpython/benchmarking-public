# Results vs. 3.10.4

- fork: faster-cpython
- ref: bound_method_instrum
- machine: linux-x86_64
- commit hash: 5787d3e
- commit date: 2024-07-23
- overall geometric mean: 1.34x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-pythonperf2-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 287 ms: 1.22x faster                                                                  |
| docutils       | 3.41 sec                                                     | 2.97 sec: 1.15x faster                                                                |
| html5lib       | 94.6 ms                                                      | 74.1 ms: 1.28x faster                                                                 |
| tornado_http   | 157 ms                                                       | 117 ms: 1.34x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.24x faster                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-pythonperf2-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|-------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 335 ms: 2.06x faster                                                                  |
| async_tree_memoization  | 819 ms                                                       | 405 ms: 2.02x faster                                                                  |
| async_tree_io           | 1.60 sec                                                     | 817 ms: 1.96x faster                                                                  |
| async_tree_cpu_io_mixed | 936 ms                                                       | 580 ms: 1.61x faster                                                                  |
| Geometric mean          | (ref)                                                        | 1.91x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-pythonperf2-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 85.1 ms: 1.58x faster                                                                 |
| float          | 111 ms                                                       | 80.6 ms: 1.38x faster                                                                 |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.32x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-pythonperf2-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 141 ms: 1.35x faster                                                                  |
| regex_dna      | 261 ms                                                       | 245 ms: 1.07x faster                                                                  |
| regex_v8       | 27.2 ms                                                      | 25.5 ms: 1.06x faster                                                                 |
| regex_effbot   | 3.09 ms                                                      | 3.40 ms: 1.10x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-pythonperf2-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 216 us: 1.44x faster                                                                  |
| pickle_pure_python   | 455 us                                                       | 319 us: 1.43x faster                                                                  |
| json_dumps           | 14.5 ms                                                      | 10.8 ms: 1.35x faster                                                                 |
| xml_etree_process    | 75.9 ms                                                      | 59.7 ms: 1.27x faster                                                                 |
| json_loads           | 30.3 us                                                      | 24.9 us: 1.22x faster                                                                 |
| tomli_loads          | 2.92 sec                                                     | 2.45 sec: 1.19x faster                                                                |
| xml_etree_parse      | 160 ms                                                       | 144 ms: 1.11x faster                                                                  |
| xml_etree_generate   | 92.3 ms                                                      | 85.4 ms: 1.08x faster                                                                 |
| xml_etree_iterparse  | 110 ms                                                       | 104 ms: 1.06x faster                                                                  |
| Geometric mean       | (ref)                                                        | 1.23x faster                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-pythonperf2-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                                 |
| python_startup_no_site | 7.33 ms                                                      | 9.06 ms: 1.24x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-pythonperf2-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.5 ms: 1.40x faster                                                                 |
| genshi_text     | 31.4 ms                                                      | 25.0 ms: 1.26x faster                                                                 |
| django_template | 50.2 ms                                                      | 40.2 ms: 1.25x faster                                                                 |
| genshi_xml      | 63.3 ms                                                      | 54.0 ms: 1.17x faster                                                                 |
| Geometric mean  | (ref)                                                        | 1.27x faster                                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-pythonperf2-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 173 us: 3.11x faster                                                                  |
| deltablue                | 7.50 ms                                                      | 3.43 ms: 2.19x faster                                                                 |
| asyncio_tcp              | 779 ms                                                       | 374 ms: 2.08x faster                                                                  |
| async_tree_none          | 692 ms                                                       | 335 ms: 2.06x faster                                                                  |
| async_tree_memoization   | 819 ms                                                       | 405 ms: 2.02x faster                                                                  |
| generators               | 57.3 ms                                                      | 29.0 ms: 1.98x faster                                                                 |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.97x faster                                                                |
| async_tree_io            | 1.60 sec                                                     | 817 ms: 1.96x faster                                                                  |
| raytrace                 | 489 ms                                                       | 275 ms: 1.78x faster                                                                  |
| chaos                    | 109 ms                                                       | 62.9 ms: 1.73x faster                                                                 |
| logging_silent           | 167 ns                                                       | 98.1 ns: 1.71x faster                                                                 |
| scimark_lu               | 167 ms                                                       | 97.9 ms: 1.71x faster                                                                 |
| crypto_pyaes             | 119 ms                                                       | 71.3 ms: 1.67x faster                                                                 |
| pylint                   | 566 ms                                                       | 349 ms: 1.62x faster                                                                  |
| deepcopy_memo            | 49.8 us                                                      | 30.7 us: 1.62x faster                                                                 |
| deepcopy                 | 468 us                                                       | 289 us: 1.62x faster                                                                  |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 580 ms: 1.61x faster                                                                  |
| sqlglot_parse            | 2.24 ms                                                      | 1.39 ms: 1.61x faster                                                                 |
| go                       | 262 ms                                                       | 163 ms: 1.61x faster                                                                  |
| nbody                    | 134 ms                                                       | 85.1 ms: 1.58x faster                                                                 |
| scimark_monte_carlo      | 107 ms                                                       | 68.3 ms: 1.57x faster                                                                 |
| comprehensions           | 26.7 us                                                      | 17.4 us: 1.54x faster                                                                 |
| richards_super           | 90.6 ms                                                      | 59.5 ms: 1.52x faster                                                                 |
| pyflate                  | 733 ms                                                       | 485 ms: 1.51x faster                                                                  |
| sqlglot_transpile        | 2.68 ms                                                      | 1.78 ms: 1.51x faster                                                                 |
| scimark_sor              | 180 ms                                                       | 120 ms: 1.51x faster                                                                  |
| hexiom                   | 9.42 ms                                                      | 6.34 ms: 1.48x faster                                                                 |
| spectral_norm            | 139 ms                                                       | 95.2 ms: 1.46x faster                                                                 |
| unpickle_pure_python     | 312 us                                                       | 216 us: 1.44x faster                                                                  |
| richards                 | 75.1 ms                                                      | 52.1 ms: 1.44x faster                                                                 |
| pickle_pure_python       | 455 us                                                       | 319 us: 1.43x faster                                                                  |
| logging_simple           | 8.88 us                                                      | 6.23 us: 1.43x faster                                                                 |
| logging_format           | 9.64 us                                                      | 6.86 us: 1.41x faster                                                                 |
| mako                     | 14.7 ms                                                      | 10.5 ms: 1.40x faster                                                                 |
| bench_mp_pool            | 6.37 ms                                                      | 4.57 ms: 1.40x faster                                                                 |
| coroutines               | 30.3 ms                                                      | 21.9 ms: 1.38x faster                                                                 |
| deepcopy_reduce          | 4.01 us                                                      | 2.90 us: 1.38x faster                                                                 |
| float                    | 111 ms                                                       | 80.6 ms: 1.38x faster                                                                 |
| pycparser                | 1.67 sec                                                     | 1.21 sec: 1.38x faster                                                                |
| json_dumps               | 14.5 ms                                                      | 10.8 ms: 1.35x faster                                                                 |
| regex_compile            | 190 ms                                                       | 141 ms: 1.35x faster                                                                  |
| pathlib                  | 21.4 ms                                                      | 15.9 ms: 1.34x faster                                                                 |
| thrift                   | 1.18 ms                                                      | 877 us: 1.34x faster                                                                  |
| tornado_http             | 157 ms                                                       | 117 ms: 1.34x faster                                                                  |
| nqueens                  | 115 ms                                                       | 87.2 ms: 1.32x faster                                                                 |
| bench_thread_pool        | 1.14 ms                                                      | 874 us: 1.31x faster                                                                  |
| fannkuch                 | 483 ms                                                       | 373 ms: 1.29x faster                                                                  |
| pprint_safe_repr         | 1.05 sec                                                     | 818 ms: 1.28x faster                                                                  |
| pprint_pformat           | 2.15 sec                                                     | 1.68 sec: 1.28x faster                                                                |
| html5lib                 | 94.6 ms                                                      | 74.1 ms: 1.28x faster                                                                 |
| xml_etree_process        | 75.9 ms                                                      | 59.7 ms: 1.27x faster                                                                 |
| genshi_text              | 31.4 ms                                                      | 25.0 ms: 1.26x faster                                                                 |
| sympy_sum                | 193 ms                                                       | 154 ms: 1.25x faster                                                                  |
| django_template          | 50.2 ms                                                      | 40.2 ms: 1.25x faster                                                                 |
| dask                     | 472 ms                                                       | 384 ms: 1.23x faster                                                                  |
| sympy_str                | 360 ms                                                       | 294 ms: 1.23x faster                                                                  |
| dulwich_log              | 81.1 ms                                                      | 66.2 ms: 1.22x faster                                                                 |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.15 ms: 1.22x faster                                                                 |
| 2to3                     | 350 ms                                                       | 287 ms: 1.22x faster                                                                  |
| json_loads               | 30.3 us                                                      | 24.9 us: 1.22x faster                                                                 |
| scimark_fft              | 361 ms                                                       | 297 ms: 1.22x faster                                                                  |
| sqlglot_normalize        | 144 ms                                                       | 118 ms: 1.22x faster                                                                  |
| sympy_integrate          | 28.2 ms                                                      | 23.2 ms: 1.21x faster                                                                 |
| sqlglot_optimize         | 70.1 ms                                                      | 58.6 ms: 1.20x faster                                                                 |
| sympy_expand             | 600 ms                                                       | 503 ms: 1.19x faster                                                                  |
| tomli_loads              | 2.92 sec                                                     | 2.45 sec: 1.19x faster                                                                |
| mdp                      | 3.01 sec                                                     | 2.55 sec: 1.18x faster                                                                |
| genshi_xml               | 63.3 ms                                                      | 54.0 ms: 1.17x faster                                                                 |
| docutils                 | 3.41 sec                                                     | 2.97 sec: 1.15x faster                                                                |
| async_generators         | 421 ms                                                       | 368 ms: 1.14x faster                                                                  |
| xml_etree_parse          | 160 ms                                                       | 144 ms: 1.11x faster                                                                  |
| meteor_contest           | 138 ms                                                       | 126 ms: 1.10x faster                                                                  |
| xml_etree_generate       | 92.3 ms                                                      | 85.4 ms: 1.08x faster                                                                 |
| json                     | 5.86 ms                                                      | 5.43 ms: 1.08x faster                                                                 |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                                  |
| regex_dna                | 261 ms                                                       | 245 ms: 1.07x faster                                                                  |
| regex_v8                 | 27.2 ms                                                      | 25.5 ms: 1.06x faster                                                                 |
| xml_etree_iterparse      | 110 ms                                                       | 104 ms: 1.06x faster                                                                  |
| telco                    | 7.23 ms                                                      | 7.89 ms: 1.09x slower                                                                 |
| regex_effbot             | 3.09 ms                                                      | 3.40 ms: 1.10x slower                                                                 |
| create_gc_cycles         | 1.76 ms                                                      | 2.00 ms: 1.13x slower                                                                 |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                                 |
| python_startup_no_site   | 7.33 ms                                                      | 9.06 ms: 1.24x slower                                                                 |
| gc_traversal             | 3.42 ms                                                      | 4.49 ms: 1.31x slower                                                                 |
| coverage                 | 63.3 ms                                                      | 84.2 ms: 1.33x slower                                                                 |
| Geometric mean           | (ref)                                                        | 1.34x faster                                                                          |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240723-3.14.0a0-5787d3e/bm-20240723-pythonperf2-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.13x