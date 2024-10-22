# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: adf0b94
- commit date: 2024-07-19
- overall geometric mean: 1.14x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240719-pythonperf2-x86_64-python-main-3.14.0a0-adf0b94 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 342 ms: 1.02x faster                                        |
| docutils       | 3.41 sec                                                     | 3.43 sec: 1.00x slower                                      |
| html5lib       | 94.6 ms                                                      | 83.0 ms: 1.14x faster                                       |
| tornado_http   | 157 ms                                                       | 127 ms: 1.24x faster                                        |
| Geometric mean | (ref)                                                        | 1.09x faster                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240719-pythonperf2-x86_64-python-main-3.14.0a0-adf0b94 |
|-------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 356 ms: 1.94x faster                                        |
| async_tree_memoization  | 819 ms                                                       | 425 ms: 1.93x faster                                        |
| async_tree_io           | 1.60 sec                                                     | 838 ms: 1.91x faster                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 599 ms: 1.56x faster                                        |
| Geometric mean          | (ref)                                                        | 1.83x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240719-pythonperf2-x86_64-python-main-3.14.0a0-adf0b94 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 111 ms                                                       | 91.6 ms: 1.21x faster                                       |
| pidigits       | 271 ms                                                       | 254 ms: 1.07x faster                                        |
| nbody          | 134 ms                                                       | 127 ms: 1.06x faster                                        |
| Geometric mean | (ref)                                                        | 1.11x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240719-pythonperf2-x86_64-python-main-3.14.0a0-adf0b94 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_dna      | 261 ms                                                       | 243 ms: 1.07x faster                                        |
| regex_v8       | 27.2 ms                                                      | 25.9 ms: 1.05x faster                                       |
| regex_compile  | 190 ms                                                       | 213 ms: 1.12x slower                                        |
| regex_effbot   | 3.09 ms                                                      | 3.65 ms: 1.18x slower                                       |
| Geometric mean | (ref)                                                        | 1.04x slower                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240719-pythonperf2-x86_64-python-main-3.14.0a0-adf0b94 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 14.5 ms                                                      | 11.4 ms: 1.28x faster                                       |
| json_loads           | 30.3 us                                                      | 25.5 us: 1.19x faster                                       |
| xml_etree_parse      | 160 ms                                                       | 144 ms: 1.11x faster                                        |
| xml_etree_process    | 75.9 ms                                                      | 68.7 ms: 1.11x faster                                       |
| pickle_pure_python   | 455 us                                                       | 427 us: 1.07x faster                                        |
| unpickle_pure_python | 312 us                                                       | 301 us: 1.04x faster                                        |
| tomli_loads          | 2.92 sec                                                     | 2.90 sec: 1.00x faster                                      |
| xml_etree_iterparse  | 110 ms                                                       | 114 ms: 1.04x slower                                        |
| xml_etree_generate   | 92.3 ms                                                      | 97.8 ms: 1.06x slower                                       |
| Geometric mean       | (ref)                                                        | 1.07x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240719-pythonperf2-x86_64-python-main-3.14.0a0-adf0b94 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.17x slower                                       |
| python_startup_no_site | 7.33 ms                                                      | 9.14 ms: 1.25x slower                                       |
| Geometric mean         | (ref)                                                        | 1.21x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240719-pythonperf2-x86_64-python-main-3.14.0a0-adf0b94 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 46.3 ms: 1.09x faster                                       |
| mako            | 14.7 ms                                                      | 14.5 ms: 1.01x faster                                       |
| genshi_text     | 31.4 ms                                                      | 32.8 ms: 1.05x slower                                       |
| genshi_xml      | 63.3 ms                                                      | 66.8 ms: 1.05x slower                                       |
| Geometric mean  | (ref)                                                        | 1.00x slower                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240719-pythonperf2-x86_64-python-main-3.14.0a0-adf0b94 |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 203 us: 2.64x faster                                        |
| asyncio_tcp              | 779 ms                                                       | 392 ms: 1.99x faster                                        |
| async_tree_none          | 692 ms                                                       | 356 ms: 1.94x faster                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.61 sec: 1.93x faster                                      |
| async_tree_memoization   | 819 ms                                                       | 425 ms: 1.93x faster                                        |
| async_tree_io            | 1.60 sec                                                     | 838 ms: 1.91x faster                                        |
| generators               | 57.3 ms                                                      | 30.2 ms: 1.90x faster                                       |
| deltablue                | 7.50 ms                                                      | 4.25 ms: 1.77x faster                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 599 ms: 1.56x faster                                        |
| raytrace                 | 489 ms                                                       | 322 ms: 1.52x faster                                        |
| pylint                   | 566 ms                                                       | 383 ms: 1.48x faster                                        |
| richards_super           | 90.6 ms                                                      | 65.2 ms: 1.39x faster                                       |
| chaos                    | 109 ms                                                       | 79.5 ms: 1.37x faster                                       |
| logging_simple           | 8.88 us                                                      | 6.65 us: 1.33x faster                                       |
| deepcopy                 | 468 us                                                       | 351 us: 1.33x faster                                        |
| bench_mp_pool            | 6.37 ms                                                      | 4.82 ms: 1.32x faster                                       |
| logging_format           | 9.64 us                                                      | 7.33 us: 1.32x faster                                       |
| coroutines               | 30.3 ms                                                      | 23.1 ms: 1.31x faster                                       |
| thrift                   | 1.18 ms                                                      | 905 us: 1.30x faster                                        |
| richards                 | 75.1 ms                                                      | 57.9 ms: 1.30x faster                                       |
| go                       | 262 ms                                                       | 202 ms: 1.30x faster                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.73 ms: 1.29x faster                                       |
| pathlib                  | 21.4 ms                                                      | 16.7 ms: 1.28x faster                                       |
| crypto_pyaes             | 119 ms                                                       | 93.4 ms: 1.28x faster                                       |
| json_dumps               | 14.5 ms                                                      | 11.4 ms: 1.28x faster                                       |
| tornado_http             | 157 ms                                                       | 127 ms: 1.24x faster                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 2.19 ms: 1.23x faster                                       |
| float                    | 111 ms                                                       | 91.6 ms: 1.21x faster                                       |
| json_loads               | 30.3 us                                                      | 25.5 us: 1.19x faster                                       |
| pyflate                  | 733 ms                                                       | 616 ms: 1.19x faster                                        |
| scimark_lu               | 167 ms                                                       | 144 ms: 1.16x faster                                        |
| bench_thread_pool        | 1.14 ms                                                      | 987 us: 1.16x faster                                        |
| deepcopy_reduce          | 4.01 us                                                      | 3.47 us: 1.16x faster                                       |
| pycparser                | 1.67 sec                                                     | 1.45 sec: 1.15x faster                                      |
| html5lib                 | 94.6 ms                                                      | 83.0 ms: 1.14x faster                                       |
| scimark_monte_carlo      | 107 ms                                                       | 94.4 ms: 1.14x faster                                       |
| dask                     | 472 ms                                                       | 421 ms: 1.12x faster                                        |
| scimark_sor              | 180 ms                                                       | 161 ms: 1.12x faster                                        |
| xml_etree_parse          | 160 ms                                                       | 144 ms: 1.11x faster                                        |
| xml_etree_process        | 75.9 ms                                                      | 68.7 ms: 1.11x faster                                       |
| mdp                      | 3.01 sec                                                     | 2.74 sec: 1.10x faster                                      |
| django_template          | 50.2 ms                                                      | 46.3 ms: 1.09x faster                                       |
| async_generators         | 421 ms                                                       | 388 ms: 1.08x faster                                        |
| regex_dna                | 261 ms                                                       | 243 ms: 1.07x faster                                        |
| pidigits                 | 271 ms                                                       | 254 ms: 1.07x faster                                        |
| logging_silent           | 167 ns                                                       | 157 ns: 1.07x faster                                        |
| pickle_pure_python       | 455 us                                                       | 427 us: 1.07x faster                                        |
| nbody                    | 134 ms                                                       | 127 ms: 1.06x faster                                        |
| regex_v8                 | 27.2 ms                                                      | 25.9 ms: 1.05x faster                                       |
| dulwich_log              | 81.1 ms                                                      | 77.8 ms: 1.04x faster                                       |
| unpickle_pure_python     | 312 us                                                       | 301 us: 1.04x faster                                        |
| sqlglot_normalize        | 144 ms                                                       | 140 ms: 1.02x faster                                        |
| 2to3                     | 350 ms                                                       | 342 ms: 1.02x faster                                        |
| sympy_sum                | 193 ms                                                       | 190 ms: 1.01x faster                                        |
| json                     | 5.86 ms                                                      | 5.78 ms: 1.01x faster                                       |
| mako                     | 14.7 ms                                                      | 14.5 ms: 1.01x faster                                       |
| pprint_pformat           | 2.15 sec                                                     | 2.13 sec: 1.01x faster                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 1.04 sec: 1.01x faster                                      |
| nqueens                  | 115 ms                                                       | 114 ms: 1.01x faster                                        |
| tomli_loads              | 2.92 sec                                                     | 2.90 sec: 1.00x faster                                      |
| sympy_integrate          | 28.2 ms                                                      | 28.1 ms: 1.00x faster                                       |
| deepcopy_memo            | 49.8 us                                                      | 50.0 us: 1.00x slower                                       |
| docutils                 | 3.41 sec                                                     | 3.43 sec: 1.00x slower                                      |
| sqlglot_optimize         | 70.1 ms                                                      | 70.6 ms: 1.01x slower                                       |
| sympy_str                | 360 ms                                                       | 370 ms: 1.03x slower                                        |
| comprehensions           | 26.7 us                                                      | 27.6 us: 1.03x slower                                       |
| xml_etree_iterparse      | 110 ms                                                       | 114 ms: 1.04x slower                                        |
| fannkuch                 | 483 ms                                                       | 500 ms: 1.04x slower                                        |
| genshi_text              | 31.4 ms                                                      | 32.8 ms: 1.05x slower                                       |
| sympy_expand             | 600 ms                                                       | 628 ms: 1.05x slower                                        |
| meteor_contest           | 138 ms                                                       | 145 ms: 1.05x slower                                        |
| genshi_xml               | 63.3 ms                                                      | 66.8 ms: 1.05x slower                                       |
| xml_etree_generate       | 92.3 ms                                                      | 97.8 ms: 1.06x slower                                       |
| spectral_norm            | 139 ms                                                       | 150 ms: 1.08x slower                                        |
| hexiom                   | 9.42 ms                                                      | 10.5 ms: 1.11x slower                                       |
| regex_compile            | 190 ms                                                       | 213 ms: 1.12x slower                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.02 ms: 1.15x slower                                       |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.17x slower                                       |
| regex_effbot             | 3.09 ms                                                      | 3.65 ms: 1.18x slower                                       |
| scimark_fft              | 361 ms                                                       | 433 ms: 1.20x slower                                        |
| python_startup_no_site   | 7.33 ms                                                      | 9.14 ms: 1.25x slower                                       |
| coverage                 | 63.3 ms                                                      | 80.0 ms: 1.26x slower                                       |
| telco                    | 7.23 ms                                                      | 9.17 ms: 1.27x slower                                       |
| gc_traversal             | 3.42 ms                                                      | 4.49 ms: 1.31x slower                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 6.81 ms: 1.34x slower                                       |
| Geometric mean           | (ref)                                                        | 1.14x faster                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240719-3.14.0a0-adf0b94-PYTHON_UOPS/bm-20240719-pythonperf2-x86_64-python-main-3.14.0a0-adf0b94.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.15x