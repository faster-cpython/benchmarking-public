
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: bef1c87
- commit date: 2023-06-25
- overall geometric mean: 1.07x faster
- HPT reliability: 99.45%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230625-pythonperf2-x86_64-python-main-3.13.0a0-bef1c87 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| docutils       | 2.86 sec                                                     | 2.89 sec: 1.01x slower                                      |
| Geometric mean | (ref)                                                        | 1.00x slower                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230625-pythonperf2-x86_64-python-main-3.13.0a0-bef1c87 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 92.5 ms: 1.02x slower                                       |
| pidigits       | 251 ms                                                       | 260 ms: 1.04x slower                                        |
| float          | 74.2 ms                                                      | 79.0 ms: 1.06x slower                                       |
| Geometric mean | (ref)                                                        | 1.04x slower                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230625-pythonperf2-x86_64-python-main-3.13.0a0-bef1c87 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 144 ms: 1.09x faster                                        |
| regex_effbot   | 3.50 ms                                                      | 3.56 ms: 1.02x slower                                       |
| regex_v8       | 23.9 ms                                                      | 24.4 ms: 1.02x slower                                       |
| regex_dna      | 227 ms                                                       | 249 ms: 1.10x slower                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230625-pythonperf2-x86_64-python-main-3.13.0a0-bef1c87 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.2 ms: 1.31x faster                                       |
| json_loads           | 28.7 us                                                      | 24.2 us: 1.19x faster                                       |
| unpickle_pure_python | 241 us                                                       | 216 us: 1.12x faster                                        |
| xml_etree_parse      | 158 ms                                                       | 152 ms: 1.03x faster                                        |
| tomli_loads          | 2.26 sec                                                     | 2.25 sec: 1.01x faster                                      |
| pickle_pure_python   | 319 us                                                       | 323 us: 1.01x slower                                        |
| xml_etree_iterparse  | 104 ms                                                       | 106 ms: 1.02x slower                                        |
| pickle_dict          | 30.8 us                                                      | 31.7 us: 1.03x slower                                       |
| pickle               | 9.64 us                                                      | 10.0 us: 1.04x slower                                       |
| xml_etree_process    | 56.5 ms                                                      | 59.2 ms: 1.05x slower                                       |
| unpickle_list        | 4.53 us                                                      | 4.86 us: 1.07x slower                                       |
| xml_etree_generate   | 80.5 ms                                                      | 86.3 ms: 1.07x slower                                       |
| unpickle             | 13.4 us                                                      | 14.5 us: 1.08x slower                                       |
| pickle_list          | 3.83 us                                                      | 4.45 us: 1.16x slower                                       |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230625-pythonperf2-x86_64-python-main-3.13.0a0-bef1c87 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.2 ms: 1.04x slower                                       |
| python_startup_no_site | 7.76 ms                                                      | 8.33 ms: 1.07x slower                                       |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230625-pythonperf2-x86_64-python-main-3.13.0a0-bef1c87 |
|-----------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 10.3 ms: 1.06x faster                                       |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230625-pythonperf2-x86_64-python-main-3.13.0a0-bef1c87 |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 153 us: 3.42x faster                                        |
| asyncio_tcp              | 753 ms                                                       | 379 ms: 1.98x faster                                        |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.57 sec: 1.96x faster                                      |
| generators               | 56.0 ms                                                      | 37.0 ms: 1.52x faster                                       |
| chaos                    | 80.9 ms                                                      | 60.6 ms: 1.33x faster                                       |
| json_dumps               | 13.4 ms                                                      | 10.2 ms: 1.31x faster                                       |
| coroutines               | 27.6 ms                                                      | 21.9 ms: 1.26x faster                                       |
| deltablue                | 4.00 ms                                                      | 3.22 ms: 1.24x faster                                       |
| scimark_lu               | 115 ms                                                       | 93.0 ms: 1.23x faster                                       |
| hexiom                   | 7.13 ms                                                      | 5.81 ms: 1.23x faster                                       |
| mypy2                    | 451 ms                                                       | 369 ms: 1.22x faster                                        |
| fannkuch                 | 429 ms                                                       | 353 ms: 1.21x faster                                        |
| json_loads               | 28.7 us                                                      | 24.2 us: 1.19x faster                                       |
| raytrace                 | 317 ms                                                       | 270 ms: 1.17x faster                                        |
| richards_super           | 61.0 ms                                                      | 52.2 ms: 1.17x faster                                       |
| nqueens                  | 103 ms                                                       | 89.8 ms: 1.14x faster                                       |
| comprehensions           | 24.6 us                                                      | 21.7 us: 1.13x faster                                       |
| logging_format           | 8.11 us                                                      | 7.24 us: 1.12x faster                                       |
| async_tree_memoization   | 630 ms                                                       | 563 ms: 1.12x faster                                        |
| json                     | 5.65 ms                                                      | 5.06 ms: 1.12x faster                                       |
| unpickle_pure_python     | 241 us                                                       | 216 us: 1.12x faster                                        |
| go                       | 164 ms                                                       | 147 ms: 1.11x faster                                        |
| async_tree_none          | 519 ms                                                       | 469 ms: 1.11x faster                                        |
| regex_compile            | 158 ms                                                       | 144 ms: 1.09x faster                                        |
| mdp                      | 2.75 sec                                                     | 2.52 sec: 1.09x faster                                      |
| async_tree_io            | 1.17 sec                                                     | 1.08 sec: 1.09x faster                                      |
| sqlglot_normalize        | 126 ms                                                       | 116 ms: 1.09x faster                                        |
| sqlglot_parse            | 1.53 ms                                                      | 1.41 ms: 1.09x faster                                       |
| gc_traversal             | 3.85 ms                                                      | 3.54 ms: 1.09x faster                                       |
| logging_simple           | 7.19 us                                                      | 6.65 us: 1.08x faster                                       |
| logging_silent           | 101 ns                                                       | 93.9 ns: 1.07x faster                                       |
| richards                 | 48.3 ms                                                      | 45.4 ms: 1.06x faster                                       |
| sqlglot_transpile        | 1.92 ms                                                      | 1.81 ms: 1.06x faster                                       |
| mako                     | 11.0 ms                                                      | 10.3 ms: 1.06x faster                                       |
| spectral_norm            | 93.3 ms                                                      | 88.1 ms: 1.06x faster                                       |
| bench_thread_pool        | 1.01 ms                                                      | 955 us: 1.06x faster                                        |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 713 ms: 1.05x faster                                        |
| deepcopy                 | 399 us                                                       | 382 us: 1.05x faster                                        |
| scimark_sor              | 111 ms                                                       | 107 ms: 1.04x faster                                        |
| xml_etree_parse          | 158 ms                                                       | 152 ms: 1.03x faster                                        |
| sqlglot_optimize         | 59.8 ms                                                      | 57.9 ms: 1.03x faster                                       |
| meteor_contest           | 131 ms                                                       | 127 ms: 1.03x faster                                        |
| pycparser                | 1.32 sec                                                     | 1.28 sec: 1.03x faster                                      |
| deepcopy_reduce          | 3.51 us                                                      | 3.44 us: 1.02x faster                                       |
| deepcopy_memo            | 38.8 us                                                      | 38.1 us: 1.02x faster                                       |
| crypto_pyaes             | 83.4 ms                                                      | 82.0 ms: 1.02x faster                                       |
| dulwich_log              | 68.4 ms                                                      | 67.3 ms: 1.02x faster                                       |
| tomli_loads              | 2.26 sec                                                     | 2.25 sec: 1.01x faster                                      |
| pickle_pure_python       | 319 us                                                       | 323 us: 1.01x slower                                        |
| docutils                 | 2.86 sec                                                     | 2.89 sec: 1.01x slower                                      |
| xml_etree_iterparse      | 104 ms                                                       | 106 ms: 1.02x slower                                        |
| regex_effbot             | 3.50 ms                                                      | 3.56 ms: 1.02x slower                                       |
| regex_v8                 | 23.9 ms                                                      | 24.4 ms: 1.02x slower                                       |
| nbody                    | 90.7 ms                                                      | 92.5 ms: 1.02x slower                                       |
| scimark_monte_carlo      | 68.2 ms                                                      | 69.7 ms: 1.02x slower                                       |
| pprint_pformat           | 1.63 sec                                                     | 1.67 sec: 1.02x slower                                      |
| pickle_dict              | 30.8 us                                                      | 31.7 us: 1.03x slower                                       |
| pathlib                  | 19.1 ms                                                      | 19.7 ms: 1.03x slower                                       |
| pidigits                 | 251 ms                                                       | 260 ms: 1.04x slower                                        |
| scimark_fft              | 285 ms                                                       | 296 ms: 1.04x slower                                        |
| pickle                   | 9.64 us                                                      | 10.0 us: 1.04x slower                                       |
| python_startup           | 10.8 ms                                                      | 11.2 ms: 1.04x slower                                       |
| pprint_safe_repr         | 784 ms                                                       | 820 ms: 1.05x slower                                        |
| xml_etree_process        | 56.5 ms                                                      | 59.2 ms: 1.05x slower                                       |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 4.29 ms: 1.06x slower                                       |
| telco                    | 6.86 ms                                                      | 7.28 ms: 1.06x slower                                       |
| float                    | 74.2 ms                                                      | 79.0 ms: 1.06x slower                                       |
| unpickle_list            | 4.53 us                                                      | 4.86 us: 1.07x slower                                       |
| xml_etree_generate       | 80.5 ms                                                      | 86.3 ms: 1.07x slower                                       |
| python_startup_no_site   | 7.76 ms                                                      | 8.33 ms: 1.07x slower                                       |
| coverage                 | 84.8 ms                                                      | 91.2 ms: 1.08x slower                                       |
| unpickle                 | 13.4 us                                                      | 14.5 us: 1.08x slower                                       |
| sqlite_synth             | 2.50 us                                                      | 2.73 us: 1.09x slower                                       |
| regex_dna                | 227 ms                                                       | 249 ms: 1.10x slower                                        |
| unpack_sequence          | 45.6 ns                                                      | 50.3 ns: 1.10x slower                                       |
| pickle_list              | 3.83 us                                                      | 4.45 us: 1.16x slower                                       |
| async_generators         | 316 ms                                                       | 389 ms: 1.23x slower                                        |
| bench_mp_pool            | 4.62 ms                                                      | 6.83 ms: 1.48x slower                                       |
| Geometric mean           | (ref)                                                        | 1.07x faster                                                |

Benchmark hidden because not significant (3): pyflate, tornado_http, create_gc_cycles
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, dask, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 99.45% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x
