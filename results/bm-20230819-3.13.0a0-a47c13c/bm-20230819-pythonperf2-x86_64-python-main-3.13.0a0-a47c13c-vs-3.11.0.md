
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: a47c13c
- commit date: 2023-08-19
- overall geometric mean: 1.04x faster
- HPT reliability: 94.74%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230819-pythonperf2-x86_64-python-main-3.13.0a0-a47c13c |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| docutils       | 2.86 sec                                                     | 2.87 sec: 1.00x slower                                      |
| Geometric mean | (ref)                                                        | 1.00x faster                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230819-pythonperf2-x86_64-python-main-3.13.0a0-a47c13c |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 84.9 ms: 1.07x faster                                       |
| pidigits       | 251 ms                                                       | 260 ms: 1.03x slower                                        |
| float          | 74.2 ms                                                      | 77.4 ms: 1.04x slower                                       |
| Geometric mean | (ref)                                                        | 1.00x slower                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230819-pythonperf2-x86_64-python-main-3.13.0a0-a47c13c |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 148 ms: 1.06x faster                                        |
| regex_effbot   | 3.50 ms                                                      | 3.71 ms: 1.06x slower                                       |
| regex_dna      | 227 ms                                                       | 248 ms: 1.09x slower                                        |
| regex_v8       | 23.9 ms                                                      | 26.3 ms: 1.10x slower                                       |
| Geometric mean | (ref)                                                        | 1.05x slower                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230819-pythonperf2-x86_64-python-main-3.13.0a0-a47c13c |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.3 ms: 1.30x faster                                       |
| json_loads           | 28.7 us                                                      | 25.2 us: 1.14x faster                                       |
| xml_etree_parse      | 158 ms                                                       | 145 ms: 1.09x faster                                        |
| unpickle_pure_python | 241 us                                                       | 228 us: 1.05x faster                                        |
| tomli_loads          | 2.26 sec                                                     | 2.23 sec: 1.01x faster                                      |
| pickle_pure_python   | 319 us                                                       | 317 us: 1.00x faster                                        |
| xml_etree_iterparse  | 104 ms                                                       | 106 ms: 1.01x slower                                        |
| unpickle_list        | 4.53 us                                                      | 4.60 us: 1.02x slower                                       |
| xml_etree_process    | 56.5 ms                                                      | 58.8 ms: 1.04x slower                                       |
| pickle               | 9.64 us                                                      | 10.1 us: 1.05x slower                                       |
| pickle_dict          | 30.8 us                                                      | 32.5 us: 1.06x slower                                       |
| unpickle             | 13.4 us                                                      | 14.4 us: 1.07x slower                                       |
| xml_etree_generate   | 80.5 ms                                                      | 86.6 ms: 1.08x slower                                       |
| pickle_list          | 3.83 us                                                      | 4.38 us: 1.14x slower                                       |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230819-pythonperf2-x86_64-python-main-3.13.0a0-a47c13c |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.6 ms: 1.08x slower                                       |
| python_startup_no_site | 7.76 ms                                                      | 8.64 ms: 1.11x slower                                       |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230819-pythonperf2-x86_64-python-main-3.13.0a0-a47c13c |
|-----------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 10.4 ms: 1.06x faster                                       |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230819-pythonperf2-x86_64-python-main-3.13.0a0-a47c13c |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 150 us: 3.49x faster                                        |
| asyncio_tcp              | 753 ms                                                       | 372 ms: 2.02x faster                                        |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.58 sec: 1.95x faster                                      |
| generators               | 56.0 ms                                                      | 36.2 ms: 1.55x faster                                       |
| json_dumps               | 13.4 ms                                                      | 10.3 ms: 1.30x faster                                       |
| chaos                    | 80.9 ms                                                      | 62.4 ms: 1.30x faster                                       |
| coroutines               | 27.6 ms                                                      | 22.9 ms: 1.20x faster                                       |
| async_tree_none          | 519 ms                                                       | 441 ms: 1.18x faster                                        |
| raytrace                 | 317 ms                                                       | 274 ms: 1.15x faster                                        |
| nqueens                  | 103 ms                                                       | 89.9 ms: 1.14x faster                                       |
| json_loads               | 28.7 us                                                      | 25.2 us: 1.14x faster                                       |
| crypto_pyaes             | 83.4 ms                                                      | 73.2 ms: 1.14x faster                                       |
| scimark_lu               | 115 ms                                                       | 101 ms: 1.14x faster                                        |
| async_tree_memoization   | 630 ms                                                       | 555 ms: 1.14x faster                                        |
| comprehensions           | 24.6 us                                                      | 22.2 us: 1.11x faster                                       |
| hexiom                   | 7.13 ms                                                      | 6.52 ms: 1.09x faster                                       |
| logging_format           | 8.11 us                                                      | 7.45 us: 1.09x faster                                       |
| xml_etree_parse          | 158 ms                                                       | 145 ms: 1.09x faster                                        |
| json                     | 5.65 ms                                                      | 5.20 ms: 1.09x faster                                       |
| sqlglot_normalize        | 126 ms                                                       | 116 ms: 1.08x faster                                        |
| mdp                      | 2.75 sec                                                     | 2.54 sec: 1.08x faster                                      |
| deltablue                | 4.00 ms                                                      | 3.71 ms: 1.08x faster                                       |
| fannkuch                 | 429 ms                                                       | 399 ms: 1.07x faster                                        |
| async_tree_io            | 1.17 sec                                                     | 1.09 sec: 1.07x faster                                      |
| sqlglot_parse            | 1.53 ms                                                      | 1.43 ms: 1.07x faster                                       |
| nbody                    | 90.7 ms                                                      | 84.9 ms: 1.07x faster                                       |
| logging_simple           | 7.19 us                                                      | 6.74 us: 1.07x faster                                       |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 704 ms: 1.06x faster                                        |
| regex_compile            | 158 ms                                                       | 148 ms: 1.06x faster                                        |
| mako                     | 11.0 ms                                                      | 10.4 ms: 1.06x faster                                       |
| unpickle_pure_python     | 241 us                                                       | 228 us: 1.05x faster                                        |
| deepcopy                 | 399 us                                                       | 381 us: 1.05x faster                                        |
| deepcopy_reduce          | 3.51 us                                                      | 3.38 us: 1.04x faster                                       |
| sqlglot_transpile        | 1.92 ms                                                      | 1.85 ms: 1.04x faster                                       |
| bench_thread_pool        | 1.01 ms                                                      | 978 us: 1.03x faster                                        |
| bench_mp_pool            | 4.62 ms                                                      | 4.48 ms: 1.03x faster                                       |
| gc_traversal             | 3.85 ms                                                      | 3.75 ms: 1.03x faster                                       |
| sqlglot_optimize         | 59.8 ms                                                      | 58.3 ms: 1.03x faster                                       |
| deepcopy_memo            | 38.8 us                                                      | 38.1 us: 1.02x faster                                       |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 3.99 ms: 1.02x faster                                       |
| tomli_loads              | 2.26 sec                                                     | 2.23 sec: 1.01x faster                                      |
| coverage                 | 84.8 ms                                                      | 84.0 ms: 1.01x faster                                       |
| richards_super           | 61.0 ms                                                      | 60.6 ms: 1.01x faster                                       |
| logging_silent           | 101 ns                                                       | 100 ns: 1.01x faster                                        |
| pickle_pure_python       | 319 us                                                       | 317 us: 1.00x faster                                        |
| scimark_monte_carlo      | 68.2 ms                                                      | 68.5 ms: 1.00x slower                                       |
| docutils                 | 2.86 sec                                                     | 2.87 sec: 1.00x slower                                      |
| dulwich_log              | 68.4 ms                                                      | 68.9 ms: 1.01x slower                                       |
| xml_etree_iterparse      | 104 ms                                                       | 106 ms: 1.01x slower                                        |
| pathlib                  | 19.1 ms                                                      | 19.3 ms: 1.01x slower                                       |
| pycparser                | 1.32 sec                                                     | 1.34 sec: 1.01x slower                                      |
| unpickle_list            | 4.53 us                                                      | 4.60 us: 1.02x slower                                       |
| pprint_pformat           | 1.63 sec                                                     | 1.67 sec: 1.02x slower                                      |
| scimark_fft              | 285 ms                                                       | 294 ms: 1.03x slower                                        |
| pidigits                 | 251 ms                                                       | 260 ms: 1.03x slower                                        |
| go                       | 164 ms                                                       | 170 ms: 1.04x slower                                        |
| xml_etree_process        | 56.5 ms                                                      | 58.8 ms: 1.04x slower                                       |
| float                    | 74.2 ms                                                      | 77.4 ms: 1.04x slower                                       |
| pprint_safe_repr         | 784 ms                                                       | 819 ms: 1.05x slower                                        |
| pickle                   | 9.64 us                                                      | 10.1 us: 1.05x slower                                       |
| pickle_dict              | 30.8 us                                                      | 32.5 us: 1.06x slower                                       |
| regex_effbot             | 3.50 ms                                                      | 3.71 ms: 1.06x slower                                       |
| unpickle                 | 13.4 us                                                      | 14.4 us: 1.07x slower                                       |
| xml_etree_generate       | 80.5 ms                                                      | 86.6 ms: 1.08x slower                                       |
| python_startup           | 10.8 ms                                                      | 11.6 ms: 1.08x slower                                       |
| spectral_norm            | 93.3 ms                                                      | 101 ms: 1.09x slower                                        |
| sqlite_synth             | 2.50 us                                                      | 2.72 us: 1.09x slower                                       |
| regex_dna                | 227 ms                                                       | 248 ms: 1.09x slower                                        |
| regex_v8                 | 23.9 ms                                                      | 26.3 ms: 1.10x slower                                       |
| richards                 | 48.3 ms                                                      | 53.8 ms: 1.11x slower                                       |
| python_startup_no_site   | 7.76 ms                                                      | 8.64 ms: 1.11x slower                                       |
| pyflate                  | 449 ms                                                       | 509 ms: 1.13x slower                                        |
| pickle_list              | 3.83 us                                                      | 4.38 us: 1.14x slower                                       |
| telco                    | 6.86 ms                                                      | 7.94 ms: 1.16x slower                                       |
| async_generators         | 316 ms                                                       | 392 ms: 1.24x slower                                        |
| scimark_sor              | 111 ms                                                       | 147 ms: 1.32x slower                                        |
| unpack_sequence          | 45.6 ns                                                      | 62.6 ns: 1.37x slower                                       |
| dask                     | 410 ms                                                       | 589 ms: 1.44x slower                                        |
| Geometric mean           | (ref)                                                        | 1.04x faster                                                |

Benchmark hidden because not significant (4): tornado_http, create_gc_cycles, meteor_contest, mypy2
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 94.74% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
