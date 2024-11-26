# Results vs. 3.10.4

- fork: faster-cpython
- ref: load_const_return_re
- machine: linux-x86_64
- commit hash: 031f320
- commit date: 2024-10-23
- overall geometric mean: 1.281x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: 1.34x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 317 ms: 1.10x faster                                                                   |
| docutils       | 3.41 sec                                                     | 3.19 sec: 1.07x faster                                                                 |
| html5lib       | 94.6 ms                                                      | 71.8 ms: 1.32x faster                                                                  |
| tornado_http   | 157 ms                                                       | 123 ms: 1.28x faster                                                                   |
| Geometric mean | (ref)                                                        | 1.19x faster                                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320 |
|-------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 337 ms: 2.05x faster                                                                   |
| async_tree_memoization  | 819 ms                                                       | 409 ms: 2.00x faster                                                                   |
| async_tree_io           | 1.60 sec                                                     | 819 ms: 1.95x faster                                                                   |
| async_tree_cpu_io_mixed | 936 ms                                                       | 575 ms: 1.63x faster                                                                   |
| Geometric mean          | (ref)                                                        | 1.90x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 85.3 ms: 1.57x faster                                                                  |
| float          | 111 ms                                                       | 80.7 ms: 1.38x faster                                                                  |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                                   |
| Geometric mean | (ref)                                                        | 1.33x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 147 ms: 1.29x faster                                                                   |
| regex_dna      | 261 ms                                                       | 234 ms: 1.12x faster                                                                   |
| regex_v8       | 27.2 ms                                                      | 24.8 ms: 1.09x faster                                                                  |
| regex_effbot   | 3.09 ms                                                      | 3.60 ms: 1.17x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 222 us: 1.41x faster                                                                   |
| tomli_loads          | 2.92 sec                                                     | 2.13 sec: 1.37x faster                                                                 |
| pickle_pure_python   | 455 us                                                       | 340 us: 1.34x faster                                                                   |
| xml_etree_process    | 75.9 ms                                                      | 56.9 ms: 1.33x faster                                                                  |
| json_dumps           | 14.5 ms                                                      | 10.9 ms: 1.33x faster                                                                  |
| json_loads           | 30.3 us                                                      | 24.6 us: 1.23x faster                                                                  |
| xml_etree_generate   | 92.3 ms                                                      | 80.0 ms: 1.15x faster                                                                  |
| xml_etree_iterparse  | 110 ms                                                       | 101 ms: 1.09x faster                                                                   |
| xml_etree_parse      | 160 ms                                                       | 147 ms: 1.09x faster                                                                   |
| Geometric mean       | (ref)                                                        | 1.25x faster                                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.11 ms: 1.24x slower                                                                  |
| python_startup         | 11.5 ms                                                      | 15.1 ms: 1.31x slower                                                                  |
| Geometric mean         | (ref)                                                        | 1.28x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.44 ms: 1.56x faster                                                                  |
| django_template | 50.2 ms                                                      | 43.8 ms: 1.15x faster                                                                  |
| genshi_text     | 31.4 ms                                                      | 29.9 ms: 1.05x faster                                                                  |
| genshi_xml      | 63.3 ms                                                      | 66.9 ms: 1.06x slower                                                                  |
| Geometric mean  | (ref)                                                        | 1.15x faster                                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320 |
|--------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 182 us: 2.95x faster                                                                   |
| deltablue                | 7.50 ms                                                      | 3.29 ms: 2.28x faster                                                                  |
| async_tree_none          | 692 ms                                                       | 337 ms: 2.05x faster                                                                   |
| async_tree_memoization   | 819 ms                                                       | 409 ms: 2.00x faster                                                                   |
| async_tree_io            | 1.60 sec                                                     | 819 ms: 1.95x faster                                                                   |
| scimark_sor              | 180 ms                                                       | 104 ms: 1.73x faster                                                                   |
| scimark_lu               | 167 ms                                                       | 97.2 ms: 1.72x faster                                                                  |
| go                       | 262 ms                                                       | 157 ms: 1.66x faster                                                                   |
| richards_super           | 90.6 ms                                                      | 54.6 ms: 1.66x faster                                                                  |
| deepcopy_memo            | 49.8 us                                                      | 30.3 us: 1.64x faster                                                                  |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 575 ms: 1.63x faster                                                                   |
| crypto_pyaes             | 119 ms                                                       | 73.2 ms: 1.63x faster                                                                  |
| logging_silent           | 167 ns                                                       | 103 ns: 1.62x faster                                                                   |
| pyflate                  | 733 ms                                                       | 456 ms: 1.61x faster                                                                   |
| chaos                    | 109 ms                                                       | 67.7 ms: 1.60x faster                                                                  |
| nbody                    | 134 ms                                                       | 85.3 ms: 1.57x faster                                                                  |
| mako                     | 14.7 ms                                                      | 9.44 ms: 1.56x faster                                                                  |
| richards                 | 75.1 ms                                                      | 48.3 ms: 1.56x faster                                                                  |
| scimark_monte_carlo      | 107 ms                                                       | 70.3 ms: 1.53x faster                                                                  |
| raytrace                 | 489 ms                                                       | 323 ms: 1.51x faster                                                                   |
| spectral_norm            | 139 ms                                                       | 93.3 ms: 1.49x faster                                                                  |
| coroutines               | 30.3 ms                                                      | 20.4 ms: 1.49x faster                                                                  |
| deepcopy                 | 468 us                                                       | 316 us: 1.48x faster                                                                   |
| sqlglot_parse            | 2.24 ms                                                      | 1.52 ms: 1.48x faster                                                                  |
| generators               | 57.3 ms                                                      | 38.9 ms: 1.47x faster                                                                  |
| comprehensions           | 26.7 us                                                      | 18.9 us: 1.41x faster                                                                  |
| unpickle_pure_python     | 312 us                                                       | 222 us: 1.41x faster                                                                   |
| float                    | 111 ms                                                       | 80.7 ms: 1.38x faster                                                                  |
| tomli_loads              | 2.92 sec                                                     | 2.13 sec: 1.37x faster                                                                 |
| pylint                   | 566 ms                                                       | 415 ms: 1.36x faster                                                                   |
| sqlglot_transpile        | 2.68 ms                                                      | 1.99 ms: 1.35x faster                                                                  |
| logging_format           | 9.64 us                                                      | 7.18 us: 1.34x faster                                                                  |
| pprint_safe_repr         | 1.05 sec                                                     | 784 ms: 1.34x faster                                                                   |
| pickle_pure_python       | 455 us                                                       | 340 us: 1.34x faster                                                                   |
| pathlib                  | 21.4 ms                                                      | 16.0 ms: 1.34x faster                                                                  |
| xml_etree_process        | 75.9 ms                                                      | 56.9 ms: 1.33x faster                                                                  |
| json_dumps               | 14.5 ms                                                      | 10.9 ms: 1.33x faster                                                                  |
| pprint_pformat           | 2.15 sec                                                     | 1.62 sec: 1.33x faster                                                                 |
| logging_simple           | 8.88 us                                                      | 6.69 us: 1.33x faster                                                                  |
| thrift                   | 1.18 ms                                                      | 887 us: 1.33x faster                                                                   |
| html5lib                 | 94.6 ms                                                      | 71.8 ms: 1.32x faster                                                                  |
| deepcopy_reduce          | 4.01 us                                                      | 3.04 us: 1.32x faster                                                                  |
| hexiom                   | 9.42 ms                                                      | 7.20 ms: 1.31x faster                                                                  |
| regex_compile            | 190 ms                                                       | 147 ms: 1.29x faster                                                                   |
| pycparser                | 1.67 sec                                                     | 1.30 sec: 1.29x faster                                                                 |
| fannkuch                 | 483 ms                                                       | 375 ms: 1.29x faster                                                                   |
| tornado_http             | 157 ms                                                       | 123 ms: 1.28x faster                                                                   |
| dulwich_log              | 81.1 ms                                                      | 63.8 ms: 1.27x faster                                                                  |
| scimark_fft              | 361 ms                                                       | 288 ms: 1.26x faster                                                                   |
| json_loads               | 30.3 us                                                      | 24.6 us: 1.23x faster                                                                  |
| bench_thread_pool        | 1.14 ms                                                      | 954 us: 1.20x faster                                                                   |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.25 ms: 1.19x faster                                                                  |
| mdp                      | 3.01 sec                                                     | 2.60 sec: 1.16x faster                                                                 |
| nqueens                  | 115 ms                                                       | 99.5 ms: 1.16x faster                                                                  |
| xml_etree_generate       | 92.3 ms                                                      | 80.0 ms: 1.15x faster                                                                  |
| django_template          | 50.2 ms                                                      | 43.8 ms: 1.15x faster                                                                  |
| sympy_expand             | 600 ms                                                       | 533 ms: 1.13x faster                                                                   |
| json                     | 5.86 ms                                                      | 5.21 ms: 1.13x faster                                                                  |
| sympy_str                | 360 ms                                                       | 321 ms: 1.12x faster                                                                   |
| regex_dna                | 261 ms                                                       | 234 ms: 1.12x faster                                                                   |
| async_generators         | 421 ms                                                       | 380 ms: 1.11x faster                                                                   |
| 2to3                     | 350 ms                                                       | 317 ms: 1.10x faster                                                                   |
| sympy_sum                | 193 ms                                                       | 175 ms: 1.10x faster                                                                   |
| regex_v8                 | 27.2 ms                                                      | 24.8 ms: 1.09x faster                                                                  |
| xml_etree_iterparse      | 110 ms                                                       | 101 ms: 1.09x faster                                                                   |
| xml_etree_parse          | 160 ms                                                       | 147 ms: 1.09x faster                                                                   |
| pidigits                 | 271 ms                                                       | 251 ms: 1.08x faster                                                                   |
| docutils                 | 3.41 sec                                                     | 3.19 sec: 1.07x faster                                                                 |
| sqlglot_normalize        | 144 ms                                                       | 135 ms: 1.07x faster                                                                   |
| meteor_contest           | 138 ms                                                       | 130 ms: 1.06x faster                                                                   |
| genshi_text              | 31.4 ms                                                      | 29.9 ms: 1.05x faster                                                                  |
| sympy_integrate          | 28.2 ms                                                      | 27.3 ms: 1.03x faster                                                                  |
| asyncio_websockets       | 390 ms                                                       | 385 ms: 1.01x faster                                                                   |
| sqlglot_optimize         | 70.1 ms                                                      | 69.7 ms: 1.01x faster                                                                  |
| genshi_xml               | 63.3 ms                                                      | 66.9 ms: 1.06x slower                                                                  |
| telco                    | 7.23 ms                                                      | 7.69 ms: 1.06x slower                                                                  |
| regex_effbot             | 3.09 ms                                                      | 3.60 ms: 1.17x slower                                                                  |
| python_startup_no_site   | 7.33 ms                                                      | 9.11 ms: 1.24x slower                                                                  |
| coverage                 | 63.3 ms                                                      | 79.3 ms: 1.25x slower                                                                  |
| python_startup           | 11.5 ms                                                      | 15.1 ms: 1.31x slower                                                                  |
| create_gc_cycles         | 1.76 ms                                                      | 2.92 ms: 1.66x slower                                                                  |
| gc_traversal             | 3.42 ms                                                      | 5.80 ms: 1.70x slower                                                                  |
| bench_mp_pool            | 6.37 ms                                                      | 2.57 sec: 403.30x slower                                                               |
| Geometric mean           | (ref)                                                        | 1.19x faster                                                                           |
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241023-3.14.0a1+-031f320-JIT/bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.281x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: 1.34x