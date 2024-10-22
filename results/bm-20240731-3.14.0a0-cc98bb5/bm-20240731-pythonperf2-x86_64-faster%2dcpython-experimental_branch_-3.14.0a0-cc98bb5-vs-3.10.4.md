# Results vs. 3.10.4

- fork: faster-cpython
- ref: experimental_branch_
- machine: linux-x86_64
- commit hash: cc98bb5
- commit date: 2024-07-31
- overall geometric mean: 1.36x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 283 ms: 1.24x faster                                                                  |
| docutils       | 3.41 sec                                                     | 2.98 sec: 1.15x faster                                                                |
| html5lib       | 94.6 ms                                                      | 71.7 ms: 1.32x faster                                                                 |
| tornado_http   | 157 ms                                                       | 117 ms: 1.34x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.26x faster                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|-------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 331 ms: 2.09x faster                                                                  |
| async_tree_memoization  | 819 ms                                                       | 401 ms: 2.04x faster                                                                  |
| async_tree_io           | 1.60 sec                                                     | 788 ms: 2.03x faster                                                                  |
| async_tree_cpu_io_mixed | 936 ms                                                       | 572 ms: 1.64x faster                                                                  |
| Geometric mean          | (ref)                                                        | 1.94x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 85.7 ms: 1.57x faster                                                                 |
| float          | 111 ms                                                       | 76.8 ms: 1.45x faster                                                                 |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.34x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 139 ms: 1.37x faster                                                                  |
| regex_dna      | 261 ms                                                       | 238 ms: 1.10x faster                                                                  |
| regex_v8       | 27.2 ms                                                      | 25.3 ms: 1.07x faster                                                                 |
| regex_effbot   | 3.09 ms                                                      | 3.51 ms: 1.14x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 205 us: 1.52x faster                                                                  |
| pickle_pure_python   | 455 us                                                       | 319 us: 1.43x faster                                                                  |
| json_dumps           | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                                 |
| tomli_loads          | 2.92 sec                                                     | 2.16 sec: 1.35x faster                                                                |
| xml_etree_process    | 75.9 ms                                                      | 58.8 ms: 1.29x faster                                                                 |
| json_loads           | 30.3 us                                                      | 25.7 us: 1.18x faster                                                                 |
| xml_etree_parse      | 160 ms                                                       | 142 ms: 1.13x faster                                                                  |
| xml_etree_iterparse  | 110 ms                                                       | 101 ms: 1.10x faster                                                                  |
| xml_etree_generate   | 92.3 ms                                                      | 84.4 ms: 1.09x faster                                                                 |
| Geometric mean       | (ref)                                                        | 1.26x faster                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                                 |
| python_startup_no_site | 7.33 ms                                                      | 9.06 ms: 1.24x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.5 ms: 1.40x faster                                                                 |
| django_template | 50.2 ms                                                      | 39.1 ms: 1.28x faster                                                                 |
| genshi_text     | 31.4 ms                                                      | 25.7 ms: 1.22x faster                                                                 |
| genshi_xml      | 63.3 ms                                                      | 55.0 ms: 1.15x faster                                                                 |
| Geometric mean  | (ref)                                                        | 1.26x faster                                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 180 us: 2.98x faster                                                                  |
| deltablue                | 7.50 ms                                                      | 3.38 ms: 2.22x faster                                                                 |
| async_tree_none          | 692 ms                                                       | 331 ms: 2.09x faster                                                                  |
| asyncio_tcp              | 779 ms                                                       | 376 ms: 2.07x faster                                                                  |
| async_tree_memoization   | 819 ms                                                       | 401 ms: 2.04x faster                                                                  |
| generators               | 57.3 ms                                                      | 28.1 ms: 2.04x faster                                                                 |
| async_tree_io            | 1.60 sec                                                     | 788 ms: 2.03x faster                                                                  |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                                |
| raytrace                 | 489 ms                                                       | 267 ms: 1.83x faster                                                                  |
| chaos                    | 109 ms                                                       | 61.4 ms: 1.77x faster                                                                 |
| scimark_lu               | 167 ms                                                       | 95.0 ms: 1.76x faster                                                                 |
| logging_silent           | 167 ns                                                       | 95.6 ns: 1.75x faster                                                                 |
| go                       | 262 ms                                                       | 158 ms: 1.66x faster                                                                  |
| richards_super           | 90.6 ms                                                      | 54.7 ms: 1.66x faster                                                                 |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 572 ms: 1.64x faster                                                                  |
| deepcopy_memo            | 49.8 us                                                      | 30.5 us: 1.63x faster                                                                 |
| pylint                   | 566 ms                                                       | 348 ms: 1.63x faster                                                                  |
| scimark_monte_carlo      | 107 ms                                                       | 66.1 ms: 1.63x faster                                                                 |
| sqlglot_parse            | 2.24 ms                                                      | 1.39 ms: 1.61x faster                                                                 |
| deepcopy                 | 468 us                                                       | 292 us: 1.60x faster                                                                  |
| pyflate                  | 733 ms                                                       | 458 ms: 1.60x faster                                                                  |
| crypto_pyaes             | 119 ms                                                       | 74.7 ms: 1.60x faster                                                                 |
| nbody                    | 134 ms                                                       | 85.7 ms: 1.57x faster                                                                 |
| richards                 | 75.1 ms                                                      | 48.4 ms: 1.55x faster                                                                 |
| comprehensions           | 26.7 us                                                      | 17.4 us: 1.54x faster                                                                 |
| unpickle_pure_python     | 312 us                                                       | 205 us: 1.52x faster                                                                  |
| hexiom                   | 9.42 ms                                                      | 6.22 ms: 1.51x faster                                                                 |
| scimark_sor              | 180 ms                                                       | 119 ms: 1.51x faster                                                                  |
| sqlglot_transpile        | 2.68 ms                                                      | 1.77 ms: 1.51x faster                                                                 |
| float                    | 111 ms                                                       | 76.8 ms: 1.45x faster                                                                 |
| spectral_norm            | 139 ms                                                       | 96.7 ms: 1.44x faster                                                                 |
| logging_simple           | 8.88 us                                                      | 6.18 us: 1.44x faster                                                                 |
| pickle_pure_python       | 455 us                                                       | 319 us: 1.43x faster                                                                  |
| coroutines               | 30.3 ms                                                      | 21.4 ms: 1.42x faster                                                                 |
| logging_format           | 9.64 us                                                      | 6.80 us: 1.42x faster                                                                 |
| mako                     | 14.7 ms                                                      | 10.5 ms: 1.40x faster                                                                 |
| regex_compile            | 190 ms                                                       | 139 ms: 1.37x faster                                                                  |
| bench_mp_pool            | 6.37 ms                                                      | 4.67 ms: 1.36x faster                                                                 |
| json_dumps               | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                                 |
| tomli_loads              | 2.92 sec                                                     | 2.16 sec: 1.35x faster                                                                |
| deepcopy_reduce          | 4.01 us                                                      | 2.97 us: 1.35x faster                                                                 |
| tornado_http             | 157 ms                                                       | 117 ms: 1.34x faster                                                                  |
| bench_thread_pool        | 1.14 ms                                                      | 853 us: 1.34x faster                                                                  |
| thrift                   | 1.18 ms                                                      | 878 us: 1.34x faster                                                                  |
| pycparser                | 1.67 sec                                                     | 1.26 sec: 1.33x faster                                                                |
| pathlib                  | 21.4 ms                                                      | 16.1 ms: 1.33x faster                                                                 |
| fannkuch                 | 483 ms                                                       | 365 ms: 1.32x faster                                                                  |
| html5lib                 | 94.6 ms                                                      | 71.7 ms: 1.32x faster                                                                 |
| xml_etree_process        | 75.9 ms                                                      | 58.8 ms: 1.29x faster                                                                 |
| pprint_pformat           | 2.15 sec                                                     | 1.67 sec: 1.29x faster                                                                |
| django_template          | 50.2 ms                                                      | 39.1 ms: 1.28x faster                                                                 |
| pprint_safe_repr         | 1.05 sec                                                     | 817 ms: 1.28x faster                                                                  |
| nqueens                  | 115 ms                                                       | 91.1 ms: 1.26x faster                                                                 |
| sympy_sum                | 193 ms                                                       | 153 ms: 1.26x faster                                                                  |
| dask                     | 472 ms                                                       | 376 ms: 1.26x faster                                                                  |
| 2to3                     | 350 ms                                                       | 283 ms: 1.24x faster                                                                  |
| sympy_str                | 360 ms                                                       | 291 ms: 1.24x faster                                                                  |
| genshi_text              | 31.4 ms                                                      | 25.7 ms: 1.22x faster                                                                 |
| sympy_expand             | 600 ms                                                       | 496 ms: 1.21x faster                                                                  |
| sqlglot_normalize        | 144 ms                                                       | 119 ms: 1.21x faster                                                                  |
| sympy_integrate          | 28.2 ms                                                      | 23.4 ms: 1.20x faster                                                                 |
| async_generators         | 421 ms                                                       | 351 ms: 1.20x faster                                                                  |
| sqlglot_optimize         | 70.1 ms                                                      | 59.0 ms: 1.19x faster                                                                 |
| json_loads               | 30.3 us                                                      | 25.7 us: 1.18x faster                                                                 |
| scimark_fft              | 361 ms                                                       | 309 ms: 1.17x faster                                                                  |
| mdp                      | 3.01 sec                                                     | 2.58 sec: 1.17x faster                                                                |
| genshi_xml               | 63.3 ms                                                      | 55.0 ms: 1.15x faster                                                                 |
| docutils                 | 3.41 sec                                                     | 2.98 sec: 1.15x faster                                                                |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.49 ms: 1.13x faster                                                                 |
| xml_etree_parse          | 160 ms                                                       | 142 ms: 1.13x faster                                                                  |
| xml_etree_iterparse      | 110 ms                                                       | 101 ms: 1.10x faster                                                                  |
| regex_dna                | 261 ms                                                       | 238 ms: 1.10x faster                                                                  |
| xml_etree_generate       | 92.3 ms                                                      | 84.4 ms: 1.09x faster                                                                 |
| meteor_contest           | 138 ms                                                       | 127 ms: 1.09x faster                                                                  |
| json                     | 5.86 ms                                                      | 5.45 ms: 1.08x faster                                                                 |
| regex_v8                 | 27.2 ms                                                      | 25.3 ms: 1.07x faster                                                                 |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                                  |
| telco                    | 7.23 ms                                                      | 7.97 ms: 1.10x slower                                                                 |
| create_gc_cycles         | 1.76 ms                                                      | 1.94 ms: 1.10x slower                                                                 |
| regex_effbot             | 3.09 ms                                                      | 3.51 ms: 1.14x slower                                                                 |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                                 |
| python_startup_no_site   | 7.33 ms                                                      | 9.06 ms: 1.24x slower                                                                 |
| coverage                 | 63.3 ms                                                      | 78.7 ms: 1.24x slower                                                                 |
| gc_traversal             | 3.42 ms                                                      | 4.49 ms: 1.31x slower                                                                 |
| Geometric mean           | (ref)                                                        | 1.36x faster                                                                          |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240731-3.14.0a0-cc98bb5/bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.13x