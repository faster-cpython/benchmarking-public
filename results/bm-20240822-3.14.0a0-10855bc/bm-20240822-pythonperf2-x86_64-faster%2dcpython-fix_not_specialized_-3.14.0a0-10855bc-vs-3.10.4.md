# Results vs. 3.10.4

- fork: faster-cpython
- ref: fix_not_specialized_
- machine: linux-x86_64
- commit hash: 10855bc
- commit date: 2024-08-22
- overall geometric mean: 1.35x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240822-pythonperf2-x86_64-faster%2dcpython-fix_not_specialized_-3.14.0a0-10855bc |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 287 ms: 1.22x faster                                                                  |
| docutils       | 3.41 sec                                                     | 2.94 sec: 1.16x faster                                                                |
| html5lib       | 94.6 ms                                                      | 72.8 ms: 1.30x faster                                                                 |
| tornado_http   | 157 ms                                                       | 117 ms: 1.34x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.25x faster                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240822-pythonperf2-x86_64-faster%2dcpython-fix_not_specialized_-3.14.0a0-10855bc |
|-------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 318 ms: 2.17x faster                                                                  |
| async_tree_memoization  | 819 ms                                                       | 398 ms: 2.06x faster                                                                  |
| async_tree_io           | 1.60 sec                                                     | 797 ms: 2.00x faster                                                                  |
| async_tree_cpu_io_mixed | 936 ms                                                       | 568 ms: 1.65x faster                                                                  |
| Geometric mean          | (ref)                                                        | 1.96x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240822-pythonperf2-x86_64-faster%2dcpython-fix_not_specialized_-3.14.0a0-10855bc |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 86.9 ms: 1.54x faster                                                                 |
| float          | 111 ms                                                       | 79.3 ms: 1.40x faster                                                                 |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.32x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240822-pythonperf2-x86_64-faster%2dcpython-fix_not_specialized_-3.14.0a0-10855bc |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 138 ms: 1.37x faster                                                                  |
| regex_dna      | 261 ms                                                       | 240 ms: 1.09x faster                                                                  |
| regex_v8       | 27.2 ms                                                      | 26.1 ms: 1.04x faster                                                                 |
| regex_effbot   | 3.09 ms                                                      | 3.62 ms: 1.17x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240822-pythonperf2-x86_64-faster%2dcpython-fix_not_specialized_-3.14.0a0-10855bc |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 212 us: 1.47x faster                                                                  |
| pickle_pure_python   | 455 us                                                       | 321 us: 1.42x faster                                                                  |
| json_dumps           | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                                 |
| xml_etree_process    | 75.9 ms                                                      | 59.3 ms: 1.28x faster                                                                 |
| tomli_loads          | 2.92 sec                                                     | 2.30 sec: 1.27x faster                                                                |
| json_loads           | 30.3 us                                                      | 24.9 us: 1.22x faster                                                                 |
| xml_etree_parse      | 160 ms                                                       | 142 ms: 1.13x faster                                                                  |
| xml_etree_generate   | 92.3 ms                                                      | 84.2 ms: 1.10x faster                                                                 |
| xml_etree_iterparse  | 110 ms                                                       | 101 ms: 1.10x faster                                                                  |
| Geometric mean       | (ref)                                                        | 1.25x faster                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240822-pythonperf2-x86_64-faster%2dcpython-fix_not_specialized_-3.14.0a0-10855bc |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                                 |
| python_startup_no_site | 7.33 ms                                                      | 9.04 ms: 1.23x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240822-pythonperf2-x86_64-faster%2dcpython-fix_not_specialized_-3.14.0a0-10855bc |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                                                 |
| django_template | 50.2 ms                                                      | 39.7 ms: 1.26x faster                                                                 |
| genshi_text     | 31.4 ms                                                      | 25.8 ms: 1.22x faster                                                                 |
| genshi_xml      | 63.3 ms                                                      | 55.5 ms: 1.14x faster                                                                 |
| Geometric mean  | (ref)                                                        | 1.26x faster                                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240822-pythonperf2-x86_64-faster%2dcpython-fix_not_specialized_-3.14.0a0-10855bc |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 176 us: 3.05x faster                                                                  |
| deltablue                | 7.50 ms                                                      | 3.43 ms: 2.19x faster                                                                 |
| async_tree_none          | 692 ms                                                       | 318 ms: 2.17x faster                                                                  |
| asyncio_tcp              | 779 ms                                                       | 368 ms: 2.12x faster                                                                  |
| async_tree_memoization   | 819 ms                                                       | 398 ms: 2.06x faster                                                                  |
| generators               | 57.3 ms                                                      | 28.4 ms: 2.02x faster                                                                 |
| async_tree_io            | 1.60 sec                                                     | 797 ms: 2.00x faster                                                                  |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.97x faster                                                                |
| raytrace                 | 489 ms                                                       | 267 ms: 1.83x faster                                                                  |
| chaos                    | 109 ms                                                       | 61.1 ms: 1.78x faster                                                                 |
| scimark_lu               | 167 ms                                                       | 94.7 ms: 1.76x faster                                                                 |
| logging_silent           | 167 ns                                                       | 98.5 ns: 1.70x faster                                                                 |
| deepcopy_memo            | 49.8 us                                                      | 29.9 us: 1.66x faster                                                                 |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 568 ms: 1.65x faster                                                                  |
| richards_super           | 90.6 ms                                                      | 55.1 ms: 1.64x faster                                                                 |
| crypto_pyaes             | 119 ms                                                       | 72.6 ms: 1.64x faster                                                                 |
| deepcopy                 | 468 us                                                       | 287 us: 1.63x faster                                                                  |
| pylint                   | 566 ms                                                       | 347 ms: 1.63x faster                                                                  |
| scimark_monte_carlo      | 107 ms                                                       | 66.0 ms: 1.63x faster                                                                 |
| sqlglot_parse            | 2.24 ms                                                      | 1.41 ms: 1.59x faster                                                                 |
| go                       | 262 ms                                                       | 166 ms: 1.57x faster                                                                  |
| pyflate                  | 733 ms                                                       | 471 ms: 1.56x faster                                                                  |
| nbody                    | 134 ms                                                       | 86.9 ms: 1.54x faster                                                                 |
| richards                 | 75.1 ms                                                      | 49.0 ms: 1.53x faster                                                                 |
| sqlglot_transpile        | 2.68 ms                                                      | 1.78 ms: 1.51x faster                                                                 |
| comprehensions           | 26.7 us                                                      | 17.8 us: 1.50x faster                                                                 |
| hexiom                   | 9.42 ms                                                      | 6.36 ms: 1.48x faster                                                                 |
| unpickle_pure_python     | 312 us                                                       | 212 us: 1.47x faster                                                                  |
| scimark_sor              | 180 ms                                                       | 126 ms: 1.43x faster                                                                  |
| spectral_norm            | 139 ms                                                       | 97.2 ms: 1.43x faster                                                                 |
| pickle_pure_python       | 455 us                                                       | 321 us: 1.42x faster                                                                  |
| mako                     | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                                                 |
| float                    | 111 ms                                                       | 79.3 ms: 1.40x faster                                                                 |
| logging_simple           | 8.88 us                                                      | 6.34 us: 1.40x faster                                                                 |
| coroutines               | 30.3 ms                                                      | 21.7 ms: 1.40x faster                                                                 |
| bench_mp_pool            | 6.37 ms                                                      | 4.61 ms: 1.38x faster                                                                 |
| logging_format           | 9.64 us                                                      | 7.01 us: 1.38x faster                                                                 |
| regex_compile            | 190 ms                                                       | 138 ms: 1.37x faster                                                                  |
| deepcopy_reduce          | 4.01 us                                                      | 2.94 us: 1.36x faster                                                                 |
| json_dumps               | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                                 |
| thrift                   | 1.18 ms                                                      | 864 us: 1.36x faster                                                                  |
| tornado_http             | 157 ms                                                       | 117 ms: 1.34x faster                                                                  |
| pathlib                  | 21.4 ms                                                      | 15.9 ms: 1.34x faster                                                                 |
| bench_thread_pool        | 1.14 ms                                                      | 862 us: 1.32x faster                                                                  |
| pycparser                | 1.67 sec                                                     | 1.27 sec: 1.32x faster                                                                |
| fannkuch                 | 483 ms                                                       | 371 ms: 1.30x faster                                                                  |
| html5lib                 | 94.6 ms                                                      | 72.8 ms: 1.30x faster                                                                 |
| nqueens                  | 115 ms                                                       | 88.5 ms: 1.30x faster                                                                 |
| pprint_pformat           | 2.15 sec                                                     | 1.68 sec: 1.28x faster                                                                |
| xml_etree_process        | 75.9 ms                                                      | 59.3 ms: 1.28x faster                                                                 |
| sympy_sum                | 193 ms                                                       | 151 ms: 1.28x faster                                                                  |
| pprint_safe_repr         | 1.05 sec                                                     | 827 ms: 1.27x faster                                                                  |
| tomli_loads              | 2.92 sec                                                     | 2.30 sec: 1.27x faster                                                                |
| django_template          | 50.2 ms                                                      | 39.7 ms: 1.26x faster                                                                 |
| sympy_str                | 360 ms                                                       | 291 ms: 1.24x faster                                                                  |
| sympy_integrate          | 28.2 ms                                                      | 22.9 ms: 1.23x faster                                                                 |
| 2to3                     | 350 ms                                                       | 287 ms: 1.22x faster                                                                  |
| json_loads               | 30.3 us                                                      | 24.9 us: 1.22x faster                                                                 |
| genshi_text              | 31.4 ms                                                      | 25.8 ms: 1.22x faster                                                                 |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.18 ms: 1.22x faster                                                                 |
| sqlglot_optimize         | 70.1 ms                                                      | 58.5 ms: 1.20x faster                                                                 |
| sympy_expand             | 600 ms                                                       | 501 ms: 1.20x faster                                                                  |
| sqlglot_normalize        | 144 ms                                                       | 121 ms: 1.19x faster                                                                  |
| mdp                      | 3.01 sec                                                     | 2.53 sec: 1.19x faster                                                                |
| scimark_fft              | 361 ms                                                       | 305 ms: 1.19x faster                                                                  |
| async_generators         | 421 ms                                                       | 362 ms: 1.16x faster                                                                  |
| docutils                 | 3.41 sec                                                     | 2.94 sec: 1.16x faster                                                                |
| genshi_xml               | 63.3 ms                                                      | 55.5 ms: 1.14x faster                                                                 |
| xml_etree_parse          | 160 ms                                                       | 142 ms: 1.13x faster                                                                  |
| json                     | 5.86 ms                                                      | 5.33 ms: 1.10x faster                                                                 |
| xml_etree_generate       | 92.3 ms                                                      | 84.2 ms: 1.10x faster                                                                 |
| xml_etree_iterparse      | 110 ms                                                       | 101 ms: 1.10x faster                                                                  |
| regex_dna                | 261 ms                                                       | 240 ms: 1.09x faster                                                                  |
| meteor_contest           | 138 ms                                                       | 128 ms: 1.08x faster                                                                  |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                                  |
| regex_v8                 | 27.2 ms                                                      | 26.1 ms: 1.04x faster                                                                 |
| telco                    | 7.23 ms                                                      | 7.98 ms: 1.10x slower                                                                 |
| create_gc_cycles         | 1.76 ms                                                      | 2.01 ms: 1.14x slower                                                                 |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                                 |
| regex_effbot             | 3.09 ms                                                      | 3.62 ms: 1.17x slower                                                                 |
| coverage                 | 63.3 ms                                                      | 78.0 ms: 1.23x slower                                                                 |
| python_startup_no_site   | 7.33 ms                                                      | 9.04 ms: 1.23x slower                                                                 |
| gc_traversal             | 3.42 ms                                                      | 4.50 ms: 1.32x slower                                                                 |
| Geometric mean           | (ref)                                                        | 1.35x faster                                                                          |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240822-3.14.0a0-10855bc/bm-20240822-pythonperf2-x86_64-faster%2dcpython-fix_not_specialized_-3.14.0a0-10855bc.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.13x