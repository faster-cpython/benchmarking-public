
# Results vs. 3.11.0

- fork: python
- ref: v3.12.0b3
- machine: windows-amd64
- commit hash: f992a60
- commit date: 2023-06-19
- overall geometric mean: 1.05x faster
- HPT reliability: 99.16%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230619-pythonperf1-amd64-python-v3.12.0b3-3.12.0b3-f992a60 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 217 ms: 1.04x slower                                            |
| docutils       | 1.60 sec                                                    | 1.66 sec: 1.03x slower                                          |
| tornado_http   | 91.8 ms                                                     | 90.2 ms: 1.02x faster                                           |
| Geometric mean | (ref)                                                       | 1.02x slower                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230619-pythonperf1-amd64-python-v3.12.0b3-3.12.0b3-f992a60 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 67.6 ms: 1.04x faster                                           |
| float          | 54.6 ms                                                     | 54.0 ms: 1.01x faster                                           |
| pidigits       | 148 ms                                                      | 154 ms: 1.04x slower                                            |
| Geometric mean | (ref)                                                       | 1.00x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230619-pythonperf1-amd64-python-v3.12.0b3-3.12.0b3-f992a60 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 87.5 ms: 1.04x faster                                           |
| regex_v8       | 13.8 ms                                                     | 14.0 ms: 1.01x slower                                           |
| regex_dna      | 115 ms                                                      | 122 ms: 1.05x slower                                            |
| regex_effbot   | 1.50 ms                                                     | 1.61 ms: 1.08x slower                                           |
| Geometric mean | (ref)                                                       | 1.03x slower                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230619-pythonperf1-amd64-python-v3.12.0b3-3.12.0b3-f992a60 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.79 ms: 1.31x faster                                           |
| unpickle_pure_python | 152 us                                                      | 132 us: 1.15x faster                                            |
| xml_etree_parse      | 95.9 ms                                                     | 92.7 ms: 1.03x faster                                           |
| pickle_pure_python   | 200 us                                                      | 194 us: 1.03x faster                                            |
| tomli_loads          | 1.41 sec                                                    | 1.38 sec: 1.02x faster                                          |
| pickle_dict          | 18.5 us                                                     | 18.1 us: 1.02x faster                                           |
| unpickle             | 8.09 us                                                     | 8.28 us: 1.02x slower                                           |
| xml_etree_process    | 37.1 ms                                                     | 38.1 ms: 1.03x slower                                           |
| xml_etree_iterparse  | 62.6 ms                                                     | 64.6 ms: 1.03x slower                                           |
| pickle               | 6.61 us                                                     | 6.86 us: 1.04x slower                                           |
| json_loads           | 12.9 us                                                     | 13.5 us: 1.05x slower                                           |
| pickle_list          | 2.68 us                                                     | 2.84 us: 1.06x slower                                           |
| xml_etree_generate   | 52.2 ms                                                     | 56.2 ms: 1.08x slower                                           |
| unpickle_list        | 2.55 us                                                     | 2.83 us: 1.11x slower                                           |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230619-pythonperf1-amd64-python-v3.12.0b3-3.12.0b3-f992a60 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 17.1 ms: 1.08x slower                                           |
| python_startup         | 18.7 ms                                                     | 20.4 ms: 1.09x slower                                           |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230619-pythonperf1-amd64-python-v3.12.0b3-3.12.0b3-f992a60 |
|-----------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 6.88 ms: 1.06x faster                                           |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230619-pythonperf1-amd64-python-v3.12.0b3-3.12.0b3-f992a60 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 94.6 us: 3.40x faster                                           |
| generators               | 33.8 ms                                                     | 22.0 ms: 1.53x faster                                           |
| asyncio_tcp              | 699 ms                                                      | 498 ms: 1.40x faster                                            |
| json_dumps               | 7.56 ms                                                     | 5.79 ms: 1.31x faster                                           |
| deltablue                | 2.61 ms                                                     | 2.07 ms: 1.26x faster                                           |
| richards_super           | 37.5 ms                                                     | 29.7 ms: 1.26x faster                                           |
| unpack_sequence          | 46.1 ns                                                     | 38.8 ns: 1.19x faster                                           |
| sqlglot_parse            | 952 us                                                      | 802 us: 1.19x faster                                            |
| logging_silent           | 69.8 ns                                                     | 59.3 ns: 1.18x faster                                           |
| richards                 | 30.6 ms                                                     | 26.1 ms: 1.17x faster                                           |
| mdp                      | 1.67 sec                                                    | 1.43 sec: 1.16x faster                                          |
| unpickle_pure_python     | 152 us                                                      | 132 us: 1.15x faster                                            |
| sqlglot_transpile        | 1.16 ms                                                     | 1.01 ms: 1.15x faster                                           |
| raytrace                 | 211 ms                                                      | 184 ms: 1.14x faster                                            |
| hexiom                   | 4.55 ms                                                     | 3.99 ms: 1.14x faster                                           |
| comprehensions           | 15.9 us                                                     | 14.0 us: 1.14x faster                                           |
| scimark_lu               | 63.5 ms                                                     | 56.6 ms: 1.12x faster                                           |
| go                       | 97.3 ms                                                     | 88.3 ms: 1.10x faster                                           |
| chaos                    | 47.1 ms                                                     | 42.8 ms: 1.10x faster                                           |
| async_tree_none          | 320 ms                                                      | 292 ms: 1.10x faster                                            |
| deepcopy_memo            | 25.2 us                                                     | 23.3 us: 1.08x faster                                           |
| json                     | 3.25 ms                                                     | 3.01 ms: 1.08x faster                                           |
| mypy2                    | 229 ms                                                      | 215 ms: 1.06x faster                                            |
| nqueens                  | 64.9 ms                                                     | 61.1 ms: 1.06x faster                                           |
| coverage                 | 55.9 ms                                                     | 52.8 ms: 1.06x faster                                           |
| mako                     | 7.26 ms                                                     | 6.88 ms: 1.06x faster                                           |
| async_tree_memoization   | 371 ms                                                      | 352 ms: 1.05x faster                                            |
| spectral_norm            | 67.9 ms                                                     | 64.6 ms: 1.05x faster                                           |
| deepcopy                 | 246 us                                                      | 234 us: 1.05x faster                                            |
| scimark_monte_carlo      | 44.6 ms                                                     | 42.6 ms: 1.05x faster                                           |
| async_tree_io            | 779 ms                                                      | 744 ms: 1.05x faster                                            |
| coroutines               | 14.6 ms                                                     | 14.0 ms: 1.04x faster                                           |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.47 ms: 1.04x faster                                           |
| fannkuch                 | 252 ms                                                      | 243 ms: 1.04x faster                                            |
| regex_compile            | 90.6 ms                                                     | 87.5 ms: 1.04x faster                                           |
| nbody                    | 70.0 ms                                                     | 67.6 ms: 1.04x faster                                           |
| xml_etree_parse          | 95.9 ms                                                     | 92.7 ms: 1.03x faster                                           |
| sqlglot_normalize        | 190 ms                                                      | 184 ms: 1.03x faster                                            |
| pickle_pure_python       | 200 us                                                      | 194 us: 1.03x faster                                            |
| sqlglot_optimize         | 34.9 ms                                                     | 33.9 ms: 1.03x faster                                           |
| logging_simple           | 6.61 us                                                     | 6.44 us: 1.03x faster                                           |
| pyflate                  | 304 ms                                                      | 297 ms: 1.02x faster                                            |
| tomli_loads              | 1.41 sec                                                    | 1.38 sec: 1.02x faster                                          |
| scimark_fft              | 178 ms                                                      | 175 ms: 1.02x faster                                            |
| pickle_dict              | 18.5 us                                                     | 18.1 us: 1.02x faster                                           |
| tornado_http             | 91.8 ms                                                     | 90.2 ms: 1.02x faster                                           |
| logging_format           | 7.01 us                                                     | 6.91 us: 1.02x faster                                           |
| aiohttp                  | 899 us                                                      | 887 us: 1.01x faster                                            |
| meteor_contest           | 74.7 ms                                                     | 73.9 ms: 1.01x faster                                           |
| float                    | 54.6 ms                                                     | 54.0 ms: 1.01x faster                                           |
| dulwich_log              | 44.5 ms                                                     | 44.1 ms: 1.01x faster                                           |
| regex_v8                 | 13.8 ms                                                     | 14.0 ms: 1.01x slower                                           |
| bench_thread_pool        | 852 us                                                      | 866 us: 1.02x slower                                            |
| unpickle                 | 8.09 us                                                     | 8.28 us: 1.02x slower                                           |
| xml_etree_process        | 37.1 ms                                                     | 38.1 ms: 1.03x slower                                           |
| xml_etree_iterparse      | 62.6 ms                                                     | 64.6 ms: 1.03x slower                                           |
| docutils                 | 1.60 sec                                                    | 1.66 sec: 1.03x slower                                          |
| scimark_sor              | 75.6 ms                                                     | 78.1 ms: 1.03x slower                                           |
| 2to3                     | 209 ms                                                      | 217 ms: 1.04x slower                                            |
| pidigits                 | 148 ms                                                      | 154 ms: 1.04x slower                                            |
| pickle                   | 6.61 us                                                     | 6.86 us: 1.04x slower                                           |
| json_loads               | 12.9 us                                                     | 13.5 us: 1.05x slower                                           |
| gc_traversal             | 1.46 ms                                                     | 1.53 ms: 1.05x slower                                           |
| telco                    | 3.90 ms                                                     | 4.11 ms: 1.05x slower                                           |
| regex_dna                | 115 ms                                                      | 122 ms: 1.05x slower                                            |
| pickle_list              | 2.68 us                                                     | 2.84 us: 1.06x slower                                           |
| create_gc_cycles         | 693 us                                                      | 744 us: 1.07x slower                                            |
| python_startup_no_site   | 15.9 ms                                                     | 17.1 ms: 1.08x slower                                           |
| regex_effbot             | 1.50 ms                                                     | 1.61 ms: 1.08x slower                                           |
| xml_etree_generate       | 52.2 ms                                                     | 56.2 ms: 1.08x slower                                           |
| bench_mp_pool            | 62.5 ms                                                     | 67.9 ms: 1.09x slower                                           |
| python_startup           | 18.7 ms                                                     | 20.4 ms: 1.09x slower                                           |
| sqlite_synth             | 1.68 us                                                     | 1.86 us: 1.10x slower                                           |
| unpickle_list            | 2.55 us                                                     | 2.83 us: 1.11x slower                                           |
| pathlib                  | 71.4 ms                                                     | 82.8 ms: 1.16x slower                                           |
| async_generators         | 178 ms                                                      | 234 ms: 1.32x slower                                            |
| dask                     | 264 ms                                                      | 370 ms: 1.40x slower                                            |
| Geometric mean           | (ref)                                                       | 1.05x faster                                                    |

Benchmark hidden because not significant (7): asyncio_tcp_ssl, async_tree_cpu_io_mixed, pprint_pformat, pprint_safe_repr, crypto_pyaes, deepcopy_reduce, pycparser
Ignored benchmarks (14) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 99.16% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
