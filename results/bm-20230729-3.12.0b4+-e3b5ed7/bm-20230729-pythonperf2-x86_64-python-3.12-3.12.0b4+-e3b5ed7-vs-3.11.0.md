
# Results vs. 3.11.0

- fork: python
- ref: 3.12
- machine: linux-x86_64
- commit hash: e3b5ed7
- commit date: 2023-07-29
- overall geometric mean: 1.06x faster
- HPT reliability: 99.95%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-pythonperf2-x86_64-python-3.12-3.12.0b4+-e3b5ed7 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 284 ms: 1.01x faster                                         |
| docutils       | 2.86 sec                                                     | 2.90 sec: 1.02x slower                                       |
| Geometric mean | (ref)                                                        | 1.00x slower                                                 |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-pythonperf2-x86_64-python-3.12-3.12.0b4+-e3b5ed7 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| pidigits       | 251 ms                                                       | 260 ms: 1.03x slower                                         |
| float          | 74.2 ms                                                      | 78.6 ms: 1.06x slower                                        |
| Geometric mean | (ref)                                                        | 1.03x slower                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-pythonperf2-x86_64-python-3.12-3.12.0b4+-e3b5ed7 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 144 ms: 1.10x faster                                         |
| regex_v8       | 23.9 ms                                                      | 23.2 ms: 1.03x faster                                        |
| regex_effbot   | 3.50 ms                                                      | 3.75 ms: 1.07x slower                                        |
| regex_dna      | 227 ms                                                       | 247 ms: 1.09x slower                                         |
| Geometric mean | (ref)                                                        | 1.01x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-pythonperf2-x86_64-python-3.12-3.12.0b4+-e3b5ed7 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.2 ms: 1.31x faster                                        |
| unpickle_pure_python | 241 us                                                       | 207 us: 1.16x faster                                         |
| json_loads           | 28.7 us                                                      | 25.6 us: 1.12x faster                                        |
| xml_etree_parse      | 158 ms                                                       | 147 ms: 1.07x faster                                         |
| tomli_loads          | 2.26 sec                                                     | 2.18 sec: 1.04x faster                                       |
| pickle_pure_python   | 319 us                                                       | 321 us: 1.01x slower                                         |
| xml_etree_iterparse  | 104 ms                                                       | 105 ms: 1.01x slower                                         |
| xml_etree_process    | 56.5 ms                                                      | 57.8 ms: 1.02x slower                                        |
| unpickle_list        | 4.53 us                                                      | 4.68 us: 1.03x slower                                        |
| pickle               | 9.64 us                                                      | 10.0 us: 1.04x slower                                        |
| xml_etree_generate   | 80.5 ms                                                      | 85.1 ms: 1.06x slower                                        |
| pickle_dict          | 30.8 us                                                      | 33.2 us: 1.08x slower                                        |
| unpickle             | 13.4 us                                                      | 14.7 us: 1.09x slower                                        |
| pickle_list          | 3.83 us                                                      | 4.52 us: 1.18x slower                                        |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-pythonperf2-x86_64-python-3.12-3.12.0b4+-e3b5ed7 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.5 ms: 1.07x slower                                        |
| python_startup_no_site | 7.76 ms                                                      | 8.47 ms: 1.09x slower                                        |
| Geometric mean         | (ref)                                                        | 1.08x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-pythonperf2-x86_64-python-3.12-3.12.0b4+-e3b5ed7 |
|-----------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 9.89 ms: 1.11x faster                                        |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-pythonperf2-x86_64-python-3.12-3.12.0b4+-e3b5ed7 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 152 us: 3.44x faster                                         |
| asyncio_tcp              | 753 ms                                                       | 381 ms: 1.98x faster                                         |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.57 sec: 1.96x faster                                       |
| generators               | 56.0 ms                                                      | 35.8 ms: 1.57x faster                                        |
| json_dumps               | 13.4 ms                                                      | 10.2 ms: 1.31x faster                                        |
| chaos                    | 80.9 ms                                                      | 63.8 ms: 1.27x faster                                        |
| fannkuch                 | 429 ms                                                       | 342 ms: 1.26x faster                                         |
| mypy2                    | 451 ms                                                       | 366 ms: 1.23x faster                                         |
| coroutines               | 27.6 ms                                                      | 22.4 ms: 1.23x faster                                        |
| deltablue                | 4.00 ms                                                      | 3.27 ms: 1.22x faster                                        |
| hexiom                   | 7.13 ms                                                      | 5.88 ms: 1.21x faster                                        |
| scimark_lu               | 115 ms                                                       | 97.4 ms: 1.18x faster                                        |
| unpickle_pure_python     | 241 us                                                       | 207 us: 1.16x faster                                         |
| nqueens                  | 103 ms                                                       | 89.1 ms: 1.15x faster                                        |
| async_tree_memoization   | 630 ms                                                       | 551 ms: 1.14x faster                                         |
| richards_super           | 61.0 ms                                                      | 53.8 ms: 1.14x faster                                        |
| async_tree_none          | 519 ms                                                       | 459 ms: 1.13x faster                                         |
| comprehensions           | 24.6 us                                                      | 21.8 us: 1.13x faster                                        |
| json_loads               | 28.7 us                                                      | 25.6 us: 1.12x faster                                        |
| mako                     | 11.0 ms                                                      | 9.89 ms: 1.11x faster                                        |
| logging_format           | 8.11 us                                                      | 7.32 us: 1.11x faster                                        |
| async_tree_io            | 1.17 sec                                                     | 1.06 sec: 1.11x faster                                       |
| sqlglot_parse            | 1.53 ms                                                      | 1.39 ms: 1.10x faster                                        |
| logging_silent           | 101 ns                                                       | 91.7 ns: 1.10x faster                                        |
| regex_compile            | 158 ms                                                       | 144 ms: 1.10x faster                                         |
| json                     | 5.65 ms                                                      | 5.18 ms: 1.09x faster                                        |
| logging_simple           | 7.19 us                                                      | 6.60 us: 1.09x faster                                        |
| mdp                      | 2.75 sec                                                     | 2.52 sec: 1.09x faster                                       |
| sqlglot_transpile        | 1.92 ms                                                      | 1.78 ms: 1.08x faster                                        |
| xml_etree_parse          | 158 ms                                                       | 147 ms: 1.07x faster                                         |
| go                       | 164 ms                                                       | 153 ms: 1.07x faster                                         |
| pycparser                | 1.32 sec                                                     | 1.24 sec: 1.06x faster                                       |
| deepcopy                 | 399 us                                                       | 375 us: 1.06x faster                                         |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 705 ms: 1.06x faster                                         |
| sqlglot_normalize        | 126 ms                                                       | 119 ms: 1.06x faster                                         |
| bench_thread_pool        | 1.01 ms                                                      | 964 us: 1.05x faster                                         |
| dulwich_log              | 68.4 ms                                                      | 65.8 ms: 1.04x faster                                        |
| spectral_norm            | 93.3 ms                                                      | 89.9 ms: 1.04x faster                                        |
| tomli_loads              | 2.26 sec                                                     | 2.18 sec: 1.04x faster                                       |
| deepcopy_memo            | 38.8 us                                                      | 37.5 us: 1.04x faster                                        |
| meteor_contest           | 131 ms                                                       | 126 ms: 1.03x faster                                         |
| richards                 | 48.3 ms                                                      | 46.8 ms: 1.03x faster                                        |
| crypto_pyaes             | 83.4 ms                                                      | 80.9 ms: 1.03x faster                                        |
| regex_v8                 | 23.9 ms                                                      | 23.2 ms: 1.03x faster                                        |
| raytrace                 | 317 ms                                                       | 308 ms: 1.03x faster                                         |
| sqlglot_optimize         | 59.8 ms                                                      | 58.3 ms: 1.02x faster                                        |
| scimark_sor              | 111 ms                                                       | 109 ms: 1.02x faster                                         |
| gc_traversal             | 3.85 ms                                                      | 3.76 ms: 1.02x faster                                        |
| deepcopy_reduce          | 3.51 us                                                      | 3.44 us: 1.02x faster                                        |
| scimark_monte_carlo      | 68.2 ms                                                      | 66.9 ms: 1.02x faster                                        |
| 2to3                     | 288 ms                                                       | 284 ms: 1.01x faster                                         |
| pprint_pformat           | 1.63 sec                                                     | 1.62 sec: 1.01x faster                                       |
| pathlib                  | 19.1 ms                                                      | 19.0 ms: 1.00x faster                                        |
| pickle_pure_python       | 319 us                                                       | 321 us: 1.01x slower                                         |
| xml_etree_iterparse      | 104 ms                                                       | 105 ms: 1.01x slower                                         |
| pprint_safe_repr         | 784 ms                                                       | 794 ms: 1.01x slower                                         |
| docutils                 | 2.86 sec                                                     | 2.90 sec: 1.02x slower                                       |
| xml_etree_process        | 56.5 ms                                                      | 57.8 ms: 1.02x slower                                        |
| create_gc_cycles         | 1.61 ms                                                      | 1.66 ms: 1.03x slower                                        |
| pidigits                 | 251 ms                                                       | 260 ms: 1.03x slower                                         |
| unpickle_list            | 4.53 us                                                      | 4.68 us: 1.03x slower                                        |
| pickle                   | 9.64 us                                                      | 10.0 us: 1.04x slower                                        |
| scimark_fft              | 285 ms                                                       | 300 ms: 1.05x slower                                         |
| telco                    | 6.86 ms                                                      | 7.22 ms: 1.05x slower                                        |
| xml_etree_generate       | 80.5 ms                                                      | 85.1 ms: 1.06x slower                                        |
| float                    | 74.2 ms                                                      | 78.6 ms: 1.06x slower                                        |
| python_startup           | 10.8 ms                                                      | 11.5 ms: 1.07x slower                                        |
| regex_effbot             | 3.50 ms                                                      | 3.75 ms: 1.07x slower                                        |
| coverage                 | 84.8 ms                                                      | 91.2 ms: 1.08x slower                                        |
| pickle_dict              | 30.8 us                                                      | 33.2 us: 1.08x slower                                        |
| regex_dna                | 227 ms                                                       | 247 ms: 1.09x slower                                         |
| python_startup_no_site   | 7.76 ms                                                      | 8.47 ms: 1.09x slower                                        |
| unpickle                 | 13.4 us                                                      | 14.7 us: 1.09x slower                                        |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 4.44 ms: 1.10x slower                                        |
| sqlite_synth             | 2.50 us                                                      | 2.75 us: 1.10x slower                                        |
| unpack_sequence          | 45.6 ns                                                      | 50.9 ns: 1.12x slower                                        |
| pickle_list              | 3.83 us                                                      | 4.52 us: 1.18x slower                                        |
| async_generators         | 316 ms                                                       | 389 ms: 1.23x slower                                         |
| dask                     | 410 ms                                                       | 568 ms: 1.38x slower                                         |
| bench_mp_pool            | 4.62 ms                                                      | 7.08 ms: 1.53x slower                                        |
| Geometric mean           | (ref)                                                        | 1.06x faster                                                 |

Benchmark hidden because not significant (3): nbody, pyflate, tornado_http
Ignored benchmarks (16) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 99.95% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
