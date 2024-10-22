# Results vs. 3.10.4

- fork: faster-cpython
- ref: variable_offset_inli
- machine: linux-x86_64
- commit hash: a3e6464
- commit date: 2024-08-20
- overall geometric mean: 1.35x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240820-pythonperf2-x86_64-faster%2dcpython-variable_offset_inli-3.14.0a0-a3e6464 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 288 ms: 1.21x faster                                                                  |
| docutils       | 3.41 sec                                                     | 2.94 sec: 1.16x faster                                                                |
| html5lib       | 94.6 ms                                                      | 73.8 ms: 1.28x faster                                                                 |
| tornado_http   | 157 ms                                                       | 118 ms: 1.33x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.24x faster                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240820-pythonperf2-x86_64-faster%2dcpython-variable_offset_inli-3.14.0a0-a3e6464 |
|-------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 320 ms: 2.16x faster                                                                  |
| async_tree_memoization  | 819 ms                                                       | 399 ms: 2.05x faster                                                                  |
| async_tree_io           | 1.60 sec                                                     | 806 ms: 1.98x faster                                                                  |
| async_tree_cpu_io_mixed | 936 ms                                                       | 573 ms: 1.63x faster                                                                  |
| Geometric mean          | (ref)                                                        | 1.95x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240820-pythonperf2-x86_64-faster%2dcpython-variable_offset_inli-3.14.0a0-a3e6464 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 87.7 ms: 1.53x faster                                                                 |
| float          | 111 ms                                                       | 79.7 ms: 1.39x faster                                                                 |
| pidigits       | 271 ms                                                       | 256 ms: 1.06x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.31x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240820-pythonperf2-x86_64-faster%2dcpython-variable_offset_inli-3.14.0a0-a3e6464 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 139 ms: 1.36x faster                                                                  |
| regex_dna      | 261 ms                                                       | 255 ms: 1.03x faster                                                                  |
| regex_v8       | 27.2 ms                                                      | 27.6 ms: 1.02x slower                                                                 |
| regex_effbot   | 3.09 ms                                                      | 3.52 ms: 1.14x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240820-pythonperf2-x86_64-faster%2dcpython-variable_offset_inli-3.14.0a0-a3e6464 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 318 us: 1.43x faster                                                                  |
| unpickle_pure_python | 312 us                                                       | 218 us: 1.43x faster                                                                  |
| json_dumps           | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                                 |
| tomli_loads          | 2.92 sec                                                     | 2.24 sec: 1.30x faster                                                                |
| xml_etree_process    | 75.9 ms                                                      | 58.4 ms: 1.30x faster                                                                 |
| json_loads           | 30.3 us                                                      | 25.0 us: 1.21x faster                                                                 |
| xml_etree_parse      | 160 ms                                                       | 144 ms: 1.12x faster                                                                  |
| xml_etree_generate   | 92.3 ms                                                      | 84.3 ms: 1.09x faster                                                                 |
| xml_etree_iterparse  | 110 ms                                                       | 103 ms: 1.07x faster                                                                  |
| Geometric mean       | (ref)                                                        | 1.25x faster                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240820-pythonperf2-x86_64-faster%2dcpython-variable_offset_inli-3.14.0a0-a3e6464 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                                 |
| python_startup_no_site | 7.33 ms                                                      | 9.07 ms: 1.24x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240820-pythonperf2-x86_64-faster%2dcpython-variable_offset_inli-3.14.0a0-a3e6464 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.4 ms: 1.41x faster                                                                 |
| django_template | 50.2 ms                                                      | 39.4 ms: 1.27x faster                                                                 |
| genshi_text     | 31.4 ms                                                      | 25.9 ms: 1.21x faster                                                                 |
| genshi_xml      | 63.3 ms                                                      | 54.9 ms: 1.15x faster                                                                 |
| Geometric mean  | (ref)                                                        | 1.26x faster                                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240820-pythonperf2-x86_64-faster%2dcpython-variable_offset_inli-3.14.0a0-a3e6464 |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 173 us: 3.11x faster                                                                  |
| deltablue                | 7.50 ms                                                      | 3.46 ms: 2.17x faster                                                                 |
| async_tree_none          | 692 ms                                                       | 320 ms: 2.16x faster                                                                  |
| asyncio_tcp              | 779 ms                                                       | 368 ms: 2.12x faster                                                                  |
| async_tree_memoization   | 819 ms                                                       | 399 ms: 2.05x faster                                                                  |
| async_tree_io            | 1.60 sec                                                     | 806 ms: 1.98x faster                                                                  |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.97x faster                                                                |
| generators               | 57.3 ms                                                      | 30.2 ms: 1.90x faster                                                                 |
| scimark_lu               | 167 ms                                                       | 95.3 ms: 1.75x faster                                                                 |
| deepcopy_memo            | 49.8 us                                                      | 29.2 us: 1.70x faster                                                                 |
| chaos                    | 109 ms                                                       | 63.8 ms: 1.70x faster                                                                 |
| raytrace                 | 489 ms                                                       | 291 ms: 1.68x faster                                                                  |
| go                       | 262 ms                                                       | 160 ms: 1.64x faster                                                                  |
| deepcopy                 | 468 us                                                       | 286 us: 1.63x faster                                                                  |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 573 ms: 1.63x faster                                                                  |
| pylint                   | 566 ms                                                       | 349 ms: 1.62x faster                                                                  |
| logging_silent           | 167 ns                                                       | 103 ns: 1.62x faster                                                                  |
| crypto_pyaes             | 119 ms                                                       | 73.6 ms: 1.62x faster                                                                 |
| sqlglot_parse            | 2.24 ms                                                      | 1.39 ms: 1.61x faster                                                                 |
| richards_super           | 90.6 ms                                                      | 56.5 ms: 1.60x faster                                                                 |
| scimark_monte_carlo      | 107 ms                                                       | 68.2 ms: 1.58x faster                                                                 |
| comprehensions           | 26.7 us                                                      | 17.3 us: 1.55x faster                                                                 |
| scimark_sor              | 180 ms                                                       | 117 ms: 1.54x faster                                                                  |
| nbody                    | 134 ms                                                       | 87.7 ms: 1.53x faster                                                                 |
| sqlglot_transpile        | 2.68 ms                                                      | 1.76 ms: 1.52x faster                                                                 |
| pyflate                  | 733 ms                                                       | 487 ms: 1.51x faster                                                                  |
| richards                 | 75.1 ms                                                      | 50.1 ms: 1.50x faster                                                                 |
| hexiom                   | 9.42 ms                                                      | 6.34 ms: 1.48x faster                                                                 |
| spectral_norm            | 139 ms                                                       | 96.1 ms: 1.45x faster                                                                 |
| pickle_pure_python       | 455 us                                                       | 318 us: 1.43x faster                                                                  |
| unpickle_pure_python     | 312 us                                                       | 218 us: 1.43x faster                                                                  |
| coroutines               | 30.3 ms                                                      | 21.4 ms: 1.42x faster                                                                 |
| mako                     | 14.7 ms                                                      | 10.4 ms: 1.41x faster                                                                 |
| float                    | 111 ms                                                       | 79.7 ms: 1.39x faster                                                                 |
| logging_format           | 9.64 us                                                      | 6.95 us: 1.39x faster                                                                 |
| bench_mp_pool            | 6.37 ms                                                      | 4.59 ms: 1.39x faster                                                                 |
| deepcopy_reduce          | 4.01 us                                                      | 2.91 us: 1.38x faster                                                                 |
| logging_simple           | 8.88 us                                                      | 6.44 us: 1.38x faster                                                                 |
| fannkuch                 | 483 ms                                                       | 353 ms: 1.37x faster                                                                  |
| regex_compile            | 190 ms                                                       | 139 ms: 1.36x faster                                                                  |
| pycparser                | 1.67 sec                                                     | 1.23 sec: 1.36x faster                                                                |
| json_dumps               | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                                 |
| thrift                   | 1.18 ms                                                      | 864 us: 1.36x faster                                                                  |
| bench_thread_pool        | 1.14 ms                                                      | 854 us: 1.34x faster                                                                  |
| pathlib                  | 21.4 ms                                                      | 16.0 ms: 1.33x faster                                                                 |
| tornado_http             | 157 ms                                                       | 118 ms: 1.33x faster                                                                  |
| tomli_loads              | 2.92 sec                                                     | 2.24 sec: 1.30x faster                                                                |
| xml_etree_process        | 75.9 ms                                                      | 58.4 ms: 1.30x faster                                                                 |
| nqueens                  | 115 ms                                                       | 88.6 ms: 1.30x faster                                                                 |
| html5lib                 | 94.6 ms                                                      | 73.8 ms: 1.28x faster                                                                 |
| django_template          | 50.2 ms                                                      | 39.4 ms: 1.27x faster                                                                 |
| sympy_sum                | 193 ms                                                       | 152 ms: 1.27x faster                                                                  |
| pprint_pformat           | 2.15 sec                                                     | 1.70 sec: 1.26x faster                                                                |
| pprint_safe_repr         | 1.05 sec                                                     | 834 ms: 1.26x faster                                                                  |
| sympy_str                | 360 ms                                                       | 290 ms: 1.24x faster                                                                  |
| sympy_integrate          | 28.2 ms                                                      | 22.9 ms: 1.23x faster                                                                 |
| json_loads               | 30.3 us                                                      | 25.0 us: 1.21x faster                                                                 |
| genshi_text              | 31.4 ms                                                      | 25.9 ms: 1.21x faster                                                                 |
| 2to3                     | 350 ms                                                       | 288 ms: 1.21x faster                                                                  |
| sqlglot_normalize        | 144 ms                                                       | 119 ms: 1.21x faster                                                                  |
| sympy_expand             | 600 ms                                                       | 497 ms: 1.21x faster                                                                  |
| mdp                      | 3.01 sec                                                     | 2.49 sec: 1.21x faster                                                                |
| sqlglot_optimize         | 70.1 ms                                                      | 58.4 ms: 1.20x faster                                                                 |
| scimark_fft              | 361 ms                                                       | 301 ms: 1.20x faster                                                                  |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.28 ms: 1.19x faster                                                                 |
| docutils                 | 3.41 sec                                                     | 2.94 sec: 1.16x faster                                                                |
| genshi_xml               | 63.3 ms                                                      | 54.9 ms: 1.15x faster                                                                 |
| async_generators         | 421 ms                                                       | 368 ms: 1.14x faster                                                                  |
| xml_etree_parse          | 160 ms                                                       | 144 ms: 1.12x faster                                                                  |
| meteor_contest           | 138 ms                                                       | 126 ms: 1.10x faster                                                                  |
| json                     | 5.86 ms                                                      | 5.34 ms: 1.10x faster                                                                 |
| xml_etree_generate       | 92.3 ms                                                      | 84.3 ms: 1.09x faster                                                                 |
| xml_etree_iterparse      | 110 ms                                                       | 103 ms: 1.07x faster                                                                  |
| pidigits                 | 271 ms                                                       | 256 ms: 1.06x faster                                                                  |
| regex_dna                | 261 ms                                                       | 255 ms: 1.03x faster                                                                  |
| asyncio_websockets       | 390 ms                                                       | 384 ms: 1.02x faster                                                                  |
| regex_v8                 | 27.2 ms                                                      | 27.6 ms: 1.02x slower                                                                 |
| telco                    | 7.23 ms                                                      | 7.95 ms: 1.10x slower                                                                 |
| regex_effbot             | 3.09 ms                                                      | 3.52 ms: 1.14x slower                                                                 |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                                 |
| create_gc_cycles         | 1.76 ms                                                      | 2.05 ms: 1.16x slower                                                                 |
| python_startup_no_site   | 7.33 ms                                                      | 9.07 ms: 1.24x slower                                                                 |
| coverage                 | 63.3 ms                                                      | 78.4 ms: 1.24x slower                                                                 |
| gc_traversal             | 3.42 ms                                                      | 4.58 ms: 1.34x slower                                                                 |
| Geometric mean           | (ref)                                                        | 1.35x faster                                                                          |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240820-3.14.0a0-a3e6464/bm-20240820-pythonperf2-x86_64-faster%2dcpython-variable_offset_inli-3.14.0a0-a3e6464.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.13x