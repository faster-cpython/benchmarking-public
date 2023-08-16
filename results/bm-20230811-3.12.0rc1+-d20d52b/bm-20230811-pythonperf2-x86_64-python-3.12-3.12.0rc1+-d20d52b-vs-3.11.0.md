
# Results vs. 3.11.0

- fork: python
- ref: 3.12
- machine: linux-x86_64
- commit hash: d20d52b
- commit date: 2023-08-11
- overall geometric mean: 1.07x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-pythonperf2-x86_64-python-3.12-3.12.0rc1+-d20d52b |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 283 ms: 1.01x faster                                          |
| docutils       | 2.86 sec                                                     | 2.90 sec: 1.01x slower                                        |
| tornado_http   | 122 ms                                                       | 119 ms: 1.02x faster                                          |
| Geometric mean | (ref)                                                        | 1.01x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-pythonperf2-x86_64-python-3.12-3.12.0rc1+-d20d52b |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------:|
| pidigits       | 251 ms                                                       | 260 ms: 1.03x slower                                          |
| float          | 74.2 ms                                                      | 78.1 ms: 1.05x slower                                         |
| Geometric mean | (ref)                                                        | 1.02x slower                                                  |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-pythonperf2-x86_64-python-3.12-3.12.0rc1+-d20d52b |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 144 ms: 1.09x faster                                          |
| regex_v8       | 23.9 ms                                                      | 23.1 ms: 1.04x faster                                         |
| regex_effbot   | 3.50 ms                                                      | 3.63 ms: 1.04x slower                                         |
| regex_dna      | 227 ms                                                       | 238 ms: 1.05x slower                                          |
| Geometric mean | (ref)                                                        | 1.01x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-pythonperf2-x86_64-python-3.12-3.12.0rc1+-d20d52b |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.4 ms: 1.29x faster                                         |
| json_loads           | 28.7 us                                                      | 24.2 us: 1.19x faster                                         |
| unpickle_pure_python | 241 us                                                       | 203 us: 1.18x faster                                          |
| xml_etree_parse      | 158 ms                                                       | 148 ms: 1.06x faster                                          |
| tomli_loads          | 2.26 sec                                                     | 2.15 sec: 1.05x faster                                        |
| pickle_pure_python   | 319 us                                                       | 318 us: 1.00x faster                                          |
| xml_etree_iterparse  | 104 ms                                                       | 106 ms: 1.01x slower                                          |
| xml_etree_process    | 56.5 ms                                                      | 57.9 ms: 1.02x slower                                         |
| unpickle_list        | 4.53 us                                                      | 4.68 us: 1.03x slower                                         |
| pickle_dict          | 30.8 us                                                      | 31.9 us: 1.04x slower                                         |
| pickle               | 9.64 us                                                      | 10.0 us: 1.04x slower                                         |
| xml_etree_generate   | 80.5 ms                                                      | 84.6 ms: 1.05x slower                                         |
| unpickle             | 13.4 us                                                      | 15.0 us: 1.12x slower                                         |
| pickle_list          | 3.83 us                                                      | 4.41 us: 1.15x slower                                         |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-pythonperf2-x86_64-python-3.12-3.12.0rc1+-d20d52b |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.5 ms: 1.07x slower                                         |
| python_startup_no_site | 7.76 ms                                                      | 8.50 ms: 1.10x slower                                         |
| Geometric mean         | (ref)                                                        | 1.08x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-pythonperf2-x86_64-python-3.12-3.12.0rc1+-d20d52b |
|-----------|:------------------------------------------------------------:|:-------------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 9.95 ms: 1.10x faster                                         |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-pythonperf2-x86_64-python-3.12-3.12.0rc1+-d20d52b |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 151 us: 3.47x faster                                          |
| asyncio_tcp              | 753 ms                                                       | 380 ms: 1.98x faster                                          |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.57 sec: 1.96x faster                                        |
| generators               | 56.0 ms                                                      | 36.4 ms: 1.54x faster                                         |
| chaos                    | 80.9 ms                                                      | 62.3 ms: 1.30x faster                                         |
| json_dumps               | 13.4 ms                                                      | 10.4 ms: 1.29x faster                                         |
| deltablue                | 4.00 ms                                                      | 3.22 ms: 1.24x faster                                         |
| hexiom                   | 7.13 ms                                                      | 5.80 ms: 1.23x faster                                         |
| mypy2                    | 451 ms                                                       | 367 ms: 1.23x faster                                          |
| coroutines               | 27.6 ms                                                      | 22.5 ms: 1.22x faster                                         |
| fannkuch                 | 429 ms                                                       | 360 ms: 1.19x faster                                          |
| json_loads               | 28.7 us                                                      | 24.2 us: 1.19x faster                                         |
| unpickle_pure_python     | 241 us                                                       | 203 us: 1.18x faster                                          |
| scimark_lu               | 115 ms                                                       | 98.4 ms: 1.16x faster                                         |
| nqueens                  | 103 ms                                                       | 88.3 ms: 1.16x faster                                         |
| richards_super           | 61.0 ms                                                      | 53.2 ms: 1.15x faster                                         |
| async_tree_memoization   | 630 ms                                                       | 549 ms: 1.15x faster                                          |
| async_tree_none          | 519 ms                                                       | 456 ms: 1.14x faster                                          |
| comprehensions           | 24.6 us                                                      | 21.7 us: 1.14x faster                                         |
| async_tree_io            | 1.17 sec                                                     | 1.05 sec: 1.12x faster                                        |
| go                       | 164 ms                                                       | 147 ms: 1.12x faster                                          |
| sqlglot_parse            | 1.53 ms                                                      | 1.39 ms: 1.11x faster                                         |
| logging_format           | 8.11 us                                                      | 7.35 us: 1.10x faster                                         |
| mako                     | 11.0 ms                                                      | 9.95 ms: 1.10x faster                                         |
| json                     | 5.65 ms                                                      | 5.16 ms: 1.09x faster                                         |
| regex_compile            | 158 ms                                                       | 144 ms: 1.09x faster                                          |
| logging_silent           | 101 ns                                                       | 92.6 ns: 1.09x faster                                         |
| mdp                      | 2.75 sec                                                     | 2.52 sec: 1.09x faster                                        |
| richards                 | 48.3 ms                                                      | 44.7 ms: 1.08x faster                                         |
| sqlglot_normalize        | 126 ms                                                       | 116 ms: 1.08x faster                                          |
| deepcopy                 | 399 us                                                       | 370 us: 1.08x faster                                          |
| deepcopy_memo            | 38.8 us                                                      | 36.0 us: 1.08x faster                                         |
| gc_traversal             | 3.85 ms                                                      | 3.57 ms: 1.08x faster                                         |
| logging_simple           | 7.19 us                                                      | 6.69 us: 1.08x faster                                         |
| raytrace                 | 317 ms                                                       | 295 ms: 1.07x faster                                          |
| sqlglot_transpile        | 1.92 ms                                                      | 1.79 ms: 1.07x faster                                         |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 701 ms: 1.07x faster                                          |
| bench_thread_pool        | 1.01 ms                                                      | 947 us: 1.07x faster                                          |
| xml_etree_parse          | 158 ms                                                       | 148 ms: 1.06x faster                                          |
| tomli_loads              | 2.26 sec                                                     | 2.15 sec: 1.05x faster                                        |
| dulwich_log              | 68.4 ms                                                      | 65.8 ms: 1.04x faster                                         |
| meteor_contest           | 131 ms                                                       | 126 ms: 1.04x faster                                          |
| pycparser                | 1.32 sec                                                     | 1.27 sec: 1.04x faster                                        |
| sqlglot_optimize         | 59.8 ms                                                      | 57.6 ms: 1.04x faster                                         |
| regex_v8                 | 23.9 ms                                                      | 23.1 ms: 1.04x faster                                         |
| spectral_norm            | 93.3 ms                                                      | 90.2 ms: 1.04x faster                                         |
| deepcopy_reduce          | 3.51 us                                                      | 3.41 us: 1.03x faster                                         |
| crypto_pyaes             | 83.4 ms                                                      | 81.6 ms: 1.02x faster                                         |
| tornado_http             | 122 ms                                                       | 119 ms: 1.02x faster                                          |
| scimark_sor              | 111 ms                                                       | 109 ms: 1.02x faster                                          |
| pyflate                  | 449 ms                                                       | 442 ms: 1.02x faster                                          |
| 2to3                     | 288 ms                                                       | 283 ms: 1.01x faster                                          |
| pickle_pure_python       | 319 us                                                       | 318 us: 1.00x faster                                          |
| scimark_monte_carlo      | 68.2 ms                                                      | 68.7 ms: 1.01x slower                                         |
| pathlib                  | 19.1 ms                                                      | 19.2 ms: 1.01x slower                                         |
| docutils                 | 2.86 sec                                                     | 2.90 sec: 1.01x slower                                        |
| xml_etree_iterparse      | 104 ms                                                       | 106 ms: 1.01x slower                                          |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 4.14 ms: 1.02x slower                                         |
| pprint_safe_repr         | 784 ms                                                       | 803 ms: 1.02x slower                                          |
| xml_etree_process        | 56.5 ms                                                      | 57.9 ms: 1.02x slower                                         |
| create_gc_cycles         | 1.61 ms                                                      | 1.65 ms: 1.03x slower                                         |
| telco                    | 6.86 ms                                                      | 7.07 ms: 1.03x slower                                         |
| unpickle_list            | 4.53 us                                                      | 4.68 us: 1.03x slower                                         |
| pidigits                 | 251 ms                                                       | 260 ms: 1.03x slower                                          |
| pickle_dict              | 30.8 us                                                      | 31.9 us: 1.04x slower                                         |
| regex_effbot             | 3.50 ms                                                      | 3.63 ms: 1.04x slower                                         |
| pickle                   | 9.64 us                                                      | 10.0 us: 1.04x slower                                         |
| scimark_fft              | 285 ms                                                       | 297 ms: 1.04x slower                                          |
| regex_dna                | 227 ms                                                       | 238 ms: 1.05x slower                                          |
| xml_etree_generate       | 80.5 ms                                                      | 84.6 ms: 1.05x slower                                         |
| float                    | 74.2 ms                                                      | 78.1 ms: 1.05x slower                                         |
| coverage                 | 84.8 ms                                                      | 89.8 ms: 1.06x slower                                         |
| python_startup           | 10.8 ms                                                      | 11.5 ms: 1.07x slower                                         |
| sqlite_synth             | 2.50 us                                                      | 2.74 us: 1.09x slower                                         |
| python_startup_no_site   | 7.76 ms                                                      | 8.50 ms: 1.10x slower                                         |
| unpickle                 | 13.4 us                                                      | 15.0 us: 1.12x slower                                         |
| unpack_sequence          | 45.6 ns                                                      | 52.2 ns: 1.14x slower                                         |
| pickle_list              | 3.83 us                                                      | 4.41 us: 1.15x slower                                         |
| async_generators         | 316 ms                                                       | 383 ms: 1.21x slower                                          |
| dask                     | 410 ms                                                       | 564 ms: 1.37x slower                                          |
| bench_mp_pool            | 4.62 ms                                                      | 6.66 ms: 1.44x slower                                         |
| Geometric mean           | (ref)                                                        | 1.07x faster                                                  |

Benchmark hidden because not significant (2): nbody, pprint_pformat
Ignored benchmarks (16) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
