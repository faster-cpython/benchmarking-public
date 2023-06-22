
# Results vs. 3.11.0

- fork: python
- ref: v3.12.0b3
- machine: linux-x86_64
- commit hash: f992a60
- commit date: 2023-06-19
- overall geometric mean: 1.07x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230619-pythonperf2-x86_64-python-v3.12.0b3-3.12.0b3-f992a60 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 283 ms: 1.02x faster                                             |
| docutils       | 2.86 sec                                                     | 2.87 sec: 1.00x slower                                           |
| tornado_http   | 122 ms                                                       | 118 ms: 1.03x faster                                             |
| Geometric mean | (ref)                                                        | 1.01x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230619-pythonperf2-x86_64-python-v3.12.0b3-3.12.0b3-f992a60 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 84.2 ms: 1.08x faster                                            |
| pidigits       | 251 ms                                                       | 260 ms: 1.03x slower                                             |
| float          | 74.2 ms                                                      | 78.8 ms: 1.06x slower                                            |
| Geometric mean | (ref)                                                        | 1.01x slower                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230619-pythonperf2-x86_64-python-v3.12.0b3-3.12.0b3-f992a60 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 144 ms: 1.10x faster                                             |
| regex_effbot   | 3.50 ms                                                      | 3.48 ms: 1.01x faster                                            |
| regex_v8       | 23.9 ms                                                      | 23.9 ms: 1.00x faster                                            |
| regex_dna      | 227 ms                                                       | 238 ms: 1.05x slower                                             |
| Geometric mean | (ref)                                                        | 1.01x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230619-pythonperf2-x86_64-python-v3.12.0b3-3.12.0b3-f992a60 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.4 ms: 1.29x faster                                            |
| json_loads           | 28.7 us                                                      | 24.7 us: 1.16x faster                                            |
| unpickle_pure_python | 241 us                                                       | 209 us: 1.15x faster                                             |
| xml_etree_parse      | 158 ms                                                       | 150 ms: 1.05x faster                                             |
| tomli_loads          | 2.26 sec                                                     | 2.17 sec: 1.04x faster                                           |
| xml_etree_iterparse  | 104 ms                                                       | 106 ms: 1.02x slower                                             |
| pickle_pure_python   | 319 us                                                       | 326 us: 1.02x slower                                             |
| unpickle_list        | 4.53 us                                                      | 4.65 us: 1.03x slower                                            |
| xml_etree_process    | 56.5 ms                                                      | 58.2 ms: 1.03x slower                                            |
| xml_etree_generate   | 80.5 ms                                                      | 85.3 ms: 1.06x slower                                            |
| pickle               | 9.64 us                                                      | 10.3 us: 1.07x slower                                            |
| unpickle             | 13.4 us                                                      | 14.6 us: 1.09x slower                                            |
| pickle_dict          | 30.8 us                                                      | 33.6 us: 1.09x slower                                            |
| pickle_list          | 3.83 us                                                      | 4.43 us: 1.16x slower                                            |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230619-pythonperf2-x86_64-python-v3.12.0b3-3.12.0b3-f992a60 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.4 ms: 1.06x slower                                            |
| python_startup_no_site | 7.76 ms                                                      | 8.43 ms: 1.09x slower                                            |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230619-pythonperf2-x86_64-python-v3.12.0b3-3.12.0b3-f992a60 |
|-----------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 10.0 ms: 1.09x faster                                            |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230619-pythonperf2-x86_64-python-v3.12.0b3-3.12.0b3-f992a60 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 152 us: 3.44x faster                                             |
| asyncio_tcp              | 753 ms                                                       | 377 ms: 2.00x faster                                             |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.56 sec: 1.97x faster                                           |
| generators               | 56.0 ms                                                      | 36.7 ms: 1.53x faster                                            |
| json_dumps               | 13.4 ms                                                      | 10.4 ms: 1.29x faster                                            |
| chaos                    | 80.9 ms                                                      | 63.4 ms: 1.28x faster                                            |
| fannkuch                 | 429 ms                                                       | 343 ms: 1.25x faster                                             |
| deltablue                | 4.00 ms                                                      | 3.21 ms: 1.24x faster                                            |
| hexiom                   | 7.13 ms                                                      | 5.79 ms: 1.23x faster                                            |
| coroutines               | 27.6 ms                                                      | 22.4 ms: 1.23x faster                                            |
| richards_super           | 61.0 ms                                                      | 50.8 ms: 1.20x faster                                            |
| scimark_lu               | 115 ms                                                       | 96.7 ms: 1.18x faster                                            |
| json_loads               | 28.7 us                                                      | 24.7 us: 1.16x faster                                            |
| unpickle_pure_python     | 241 us                                                       | 209 us: 1.15x faster                                             |
| async_tree_memoization   | 630 ms                                                       | 551 ms: 1.14x faster                                             |
| nqueens                  | 103 ms                                                       | 90.2 ms: 1.14x faster                                            |
| logging_format           | 8.11 us                                                      | 7.13 us: 1.14x faster                                            |
| comprehensions           | 24.6 us                                                      | 21.7 us: 1.14x faster                                            |
| async_tree_none          | 519 ms                                                       | 457 ms: 1.14x faster                                             |
| go                       | 164 ms                                                       | 145 ms: 1.13x faster                                             |
| async_tree_io            | 1.17 sec                                                     | 1.06 sec: 1.11x faster                                           |
| logging_simple           | 7.19 us                                                      | 6.49 us: 1.11x faster                                            |
| sqlglot_parse            | 1.53 ms                                                      | 1.39 ms: 1.10x faster                                            |
| mdp                      | 2.75 sec                                                     | 2.49 sec: 1.10x faster                                           |
| logging_silent           | 101 ns                                                       | 91.8 ns: 1.10x faster                                            |
| regex_compile            | 158 ms                                                       | 144 ms: 1.10x faster                                             |
| mako                     | 11.0 ms                                                      | 10.0 ms: 1.09x faster                                            |
| json                     | 5.65 ms                                                      | 5.18 ms: 1.09x faster                                            |
| sqlglot_normalize        | 126 ms                                                       | 116 ms: 1.08x faster                                             |
| richards                 | 48.3 ms                                                      | 44.7 ms: 1.08x faster                                            |
| nbody                    | 90.7 ms                                                      | 84.2 ms: 1.08x faster                                            |
| sqlglot_transpile        | 1.92 ms                                                      | 1.80 ms: 1.07x faster                                            |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 704 ms: 1.06x faster                                             |
| deepcopy                 | 399 us                                                       | 376 us: 1.06x faster                                             |
| bench_thread_pool        | 1.01 ms                                                      | 953 us: 1.06x faster                                             |
| raytrace                 | 317 ms                                                       | 300 ms: 1.06x faster                                             |
| xml_etree_parse          | 158 ms                                                       | 150 ms: 1.05x faster                                             |
| meteor_contest           | 131 ms                                                       | 125 ms: 1.05x faster                                             |
| tomli_loads              | 2.26 sec                                                     | 2.17 sec: 1.04x faster                                           |
| sqlglot_optimize         | 59.8 ms                                                      | 57.4 ms: 1.04x faster                                            |
| pycparser                | 1.32 sec                                                     | 1.27 sec: 1.04x faster                                           |
| scimark_sor              | 111 ms                                                       | 107 ms: 1.04x faster                                             |
| deepcopy_memo            | 38.8 us                                                      | 37.4 us: 1.04x faster                                            |
| dulwich_log              | 68.4 ms                                                      | 66.1 ms: 1.04x faster                                            |
| crypto_pyaes             | 83.4 ms                                                      | 80.9 ms: 1.03x faster                                            |
| deepcopy_reduce          | 3.51 us                                                      | 3.41 us: 1.03x faster                                            |
| tornado_http             | 122 ms                                                       | 118 ms: 1.03x faster                                             |
| pyflate                  | 449 ms                                                       | 439 ms: 1.02x faster                                             |
| 2to3                     | 288 ms                                                       | 283 ms: 1.02x faster                                             |
| scimark_monte_carlo      | 68.2 ms                                                      | 67.8 ms: 1.01x faster                                            |
| regex_effbot             | 3.50 ms                                                      | 3.48 ms: 1.01x faster                                            |
| regex_v8                 | 23.9 ms                                                      | 23.9 ms: 1.00x faster                                            |
| docutils                 | 2.86 sec                                                     | 2.87 sec: 1.00x slower                                           |
| pathlib                  | 19.1 ms                                                      | 19.2 ms: 1.01x slower                                            |
| xml_etree_iterparse      | 104 ms                                                       | 106 ms: 1.02x slower                                             |
| create_gc_cycles         | 1.61 ms                                                      | 1.64 ms: 1.02x slower                                            |
| pprint_safe_repr         | 784 ms                                                       | 799 ms: 1.02x slower                                             |
| pickle_pure_python       | 319 us                                                       | 326 us: 1.02x slower                                             |
| unpickle_list            | 4.53 us                                                      | 4.65 us: 1.03x slower                                            |
| telco                    | 6.86 ms                                                      | 7.07 ms: 1.03x slower                                            |
| xml_etree_process        | 56.5 ms                                                      | 58.2 ms: 1.03x slower                                            |
| pidigits                 | 251 ms                                                       | 260 ms: 1.03x slower                                             |
| regex_dna                | 227 ms                                                       | 238 ms: 1.05x slower                                             |
| coverage                 | 84.8 ms                                                      | 89.0 ms: 1.05x slower                                            |
| gc_traversal             | 3.85 ms                                                      | 4.06 ms: 1.06x slower                                            |
| xml_etree_generate       | 80.5 ms                                                      | 85.3 ms: 1.06x slower                                            |
| python_startup           | 10.8 ms                                                      | 11.4 ms: 1.06x slower                                            |
| float                    | 74.2 ms                                                      | 78.8 ms: 1.06x slower                                            |
| scimark_fft              | 285 ms                                                       | 304 ms: 1.07x slower                                             |
| pickle                   | 9.64 us                                                      | 10.3 us: 1.07x slower                                            |
| unpack_sequence          | 45.6 ns                                                      | 49.4 ns: 1.08x slower                                            |
| unpickle                 | 13.4 us                                                      | 14.6 us: 1.09x slower                                            |
| python_startup_no_site   | 7.76 ms                                                      | 8.43 ms: 1.09x slower                                            |
| sqlite_synth             | 2.50 us                                                      | 2.72 us: 1.09x slower                                            |
| bench_mp_pool            | 4.62 ms                                                      | 5.05 ms: 1.09x slower                                            |
| pickle_dict              | 30.8 us                                                      | 33.6 us: 1.09x slower                                            |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 4.43 ms: 1.10x slower                                            |
| pickle_list              | 3.83 us                                                      | 4.43 us: 1.16x slower                                            |
| async_generators         | 316 ms                                                       | 382 ms: 1.21x slower                                             |
| dask                     | 410 ms                                                       | 562 ms: 1.37x slower                                             |
| Geometric mean           | (ref)                                                        | 1.07x faster                                                     |

Benchmark hidden because not significant (3): pprint_pformat, spectral_norm, mypy2
Ignored benchmarks (16) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
