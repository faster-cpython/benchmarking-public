
# Results vs. 3.11.0

- fork: python
- ref: 3.12
- machine: windows-amd64
- commit hash: 60ade0c
- commit date: 2023-07-08
- overall geometric mean: 1.05x faster
- HPT reliability: 99.95%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230708-pythonperf1-amd64-python-3.12-3.12.0b3+-60ade0c |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 215 ms: 1.03x slower                                        |
| tornado_http   | 91.8 ms                                                     | 96.2 ms: 1.05x slower                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230708-pythonperf1-amd64-python-3.12-3.12.0b3+-60ade0c |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 54.6 ms                                                     | 53.0 ms: 1.03x faster                                       |
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                        |
| Geometric mean | (ref)                                                       | 1.01x faster                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230708-pythonperf1-amd64-python-3.12-3.12.0b3+-60ade0c |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 85.6 ms: 1.06x faster                                       |
| regex_v8       | 13.8 ms                                                     | 13.9 ms: 1.00x slower                                       |
| regex_dna      | 115 ms                                                      | 124 ms: 1.07x slower                                        |
| regex_effbot   | 1.50 ms                                                     | 1.61 ms: 1.07x slower                                       |
| Geometric mean | (ref)                                                       | 1.02x slower                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230708-pythonperf1-amd64-python-3.12-3.12.0b3+-60ade0c |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.63 ms: 1.34x faster                                       |
| unpickle_pure_python | 152 us                                                      | 131 us: 1.16x faster                                        |
| xml_etree_parse      | 95.9 ms                                                     | 89.7 ms: 1.07x faster                                       |
| pickle_pure_python   | 200 us                                                      | 190 us: 1.05x faster                                        |
| tomli_loads          | 1.41 sec                                                    | 1.37 sec: 1.03x faster                                      |
| pickle_dict          | 18.5 us                                                     | 18.1 us: 1.02x faster                                       |
| xml_etree_process    | 37.1 ms                                                     | 37.7 ms: 1.02x slower                                       |
| unpickle             | 8.09 us                                                     | 8.42 us: 1.04x slower                                       |
| json_loads           | 12.9 us                                                     | 13.5 us: 1.05x slower                                       |
| xml_etree_generate   | 52.2 ms                                                     | 55.0 ms: 1.05x slower                                       |
| pickle_list          | 2.68 us                                                     | 2.83 us: 1.05x slower                                       |
| pickle               | 6.61 us                                                     | 7.13 us: 1.08x slower                                       |
| unpickle_list        | 2.55 us                                                     | 2.96 us: 1.16x slower                                       |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230708-pythonperf1-amd64-python-3.12-3.12.0b3+-60ade0c |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 18.7 ms                                                     | 20.4 ms: 1.09x slower                                       |
| python_startup_no_site | 15.9 ms                                                     | 17.6 ms: 1.11x slower                                       |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230708-pythonperf1-amd64-python-3.12-3.12.0b3+-60ade0c |
|-----------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 6.86 ms: 1.06x faster                                       |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230708-pythonperf1-amd64-python-3.12-3.12.0b3+-60ade0c |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 93.4 us: 3.45x faster                                       |
| generators               | 33.8 ms                                                     | 21.6 ms: 1.56x faster                                       |
| json_dumps               | 7.56 ms                                                     | 5.63 ms: 1.34x faster                                       |
| asyncio_tcp              | 699 ms                                                      | 542 ms: 1.29x faster                                        |
| richards_super           | 37.5 ms                                                     | 29.6 ms: 1.27x faster                                       |
| deltablue                | 2.61 ms                                                     | 2.07 ms: 1.26x faster                                       |
| sqlglot_parse            | 952 us                                                      | 787 us: 1.21x faster                                        |
| richards                 | 30.6 ms                                                     | 25.6 ms: 1.19x faster                                       |
| logging_silent           | 69.8 ns                                                     | 58.7 ns: 1.19x faster                                       |
| mdp                      | 1.67 sec                                                    | 1.42 sec: 1.18x faster                                      |
| unpack_sequence          | 46.1 ns                                                     | 39.2 ns: 1.17x faster                                       |
| sqlglot_transpile        | 1.16 ms                                                     | 998 us: 1.17x faster                                        |
| unpickle_pure_python     | 152 us                                                      | 131 us: 1.16x faster                                        |
| raytrace                 | 211 ms                                                      | 185 ms: 1.14x faster                                        |
| comprehensions           | 15.9 us                                                     | 14.0 us: 1.14x faster                                       |
| hexiom                   | 4.55 ms                                                     | 4.01 ms: 1.14x faster                                       |
| scimark_lu               | 63.5 ms                                                     | 56.0 ms: 1.13x faster                                       |
| go                       | 97.3 ms                                                     | 86.9 ms: 1.12x faster                                       |
| async_tree_none          | 320 ms                                                      | 288 ms: 1.11x faster                                        |
| async_tree_io            | 779 ms                                                      | 700 ms: 1.11x faster                                        |
| async_tree_memoization   | 371 ms                                                      | 334 ms: 1.11x faster                                        |
| chaos                    | 47.1 ms                                                     | 42.4 ms: 1.11x faster                                       |
| mypy2                    | 229 ms                                                      | 209 ms: 1.10x faster                                        |
| coverage                 | 55.9 ms                                                     | 51.1 ms: 1.09x faster                                       |
| json                     | 3.25 ms                                                     | 2.97 ms: 1.09x faster                                       |
| deepcopy_memo            | 25.2 us                                                     | 23.3 us: 1.08x faster                                       |
| xml_etree_parse          | 95.9 ms                                                     | 89.7 ms: 1.07x faster                                       |
| spectral_norm            | 67.9 ms                                                     | 63.7 ms: 1.07x faster                                       |
| nqueens                  | 64.9 ms                                                     | 61.0 ms: 1.06x faster                                       |
| sqlglot_normalize        | 190 ms                                                      | 179 ms: 1.06x faster                                        |
| coroutines               | 14.6 ms                                                     | 13.8 ms: 1.06x faster                                       |
| mako                     | 7.26 ms                                                     | 6.86 ms: 1.06x faster                                       |
| regex_compile            | 90.6 ms                                                     | 85.6 ms: 1.06x faster                                       |
| async_tree_cpu_io_mixed  | 501 ms                                                      | 475 ms: 1.05x faster                                        |
| deepcopy                 | 246 us                                                      | 234 us: 1.05x faster                                        |
| scimark_monte_carlo      | 44.6 ms                                                     | 42.5 ms: 1.05x faster                                       |
| pickle_pure_python       | 200 us                                                      | 190 us: 1.05x faster                                        |
| logging_simple           | 6.61 us                                                     | 6.32 us: 1.05x faster                                       |
| pyflate                  | 304 ms                                                      | 291 ms: 1.05x faster                                        |
| sqlglot_optimize         | 34.9 ms                                                     | 33.4 ms: 1.04x faster                                       |
| fannkuch                 | 252 ms                                                      | 243 ms: 1.04x faster                                        |
| logging_format           | 7.01 us                                                     | 6.75 us: 1.04x faster                                       |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.48 ms: 1.04x faster                                       |
| dulwich_log              | 44.5 ms                                                     | 42.9 ms: 1.04x faster                                       |
| meteor_contest           | 74.7 ms                                                     | 72.2 ms: 1.04x faster                                       |
| tomli_loads              | 1.41 sec                                                    | 1.37 sec: 1.03x faster                                      |
| float                    | 54.6 ms                                                     | 53.0 ms: 1.03x faster                                       |
| pprint_safe_repr         | 512 ms                                                      | 498 ms: 1.03x faster                                        |
| crypto_pyaes             | 47.6 ms                                                     | 46.4 ms: 1.02x faster                                       |
| pickle_dict              | 18.5 us                                                     | 18.1 us: 1.02x faster                                       |
| pprint_pformat           | 1.04 sec                                                    | 1.02 sec: 1.02x faster                                      |
| pycparser                | 691 ms                                                      | 678 ms: 1.02x faster                                        |
| regex_v8                 | 13.8 ms                                                     | 13.9 ms: 1.00x slower                                       |
| pidigits                 | 148 ms                                                      | 150 ms: 1.01x slower                                        |
| gc_traversal             | 1.46 ms                                                     | 1.48 ms: 1.02x slower                                       |
| xml_etree_process        | 37.1 ms                                                     | 37.7 ms: 1.02x slower                                       |
| scimark_fft              | 178 ms                                                      | 183 ms: 1.03x slower                                        |
| 2to3                     | 209 ms                                                      | 215 ms: 1.03x slower                                        |
| sqlite_synth             | 1.68 us                                                     | 1.75 us: 1.04x slower                                       |
| unpickle                 | 8.09 us                                                     | 8.42 us: 1.04x slower                                       |
| telco                    | 3.90 ms                                                     | 4.06 ms: 1.04x slower                                       |
| create_gc_cycles         | 693 us                                                      | 722 us: 1.04x slower                                        |
| tornado_http             | 91.8 ms                                                     | 96.2 ms: 1.05x slower                                       |
| scimark_sor              | 75.6 ms                                                     | 79.2 ms: 1.05x slower                                       |
| json_loads               | 12.9 us                                                     | 13.5 us: 1.05x slower                                       |
| xml_etree_generate       | 52.2 ms                                                     | 55.0 ms: 1.05x slower                                       |
| pickle_list              | 2.68 us                                                     | 2.83 us: 1.05x slower                                       |
| regex_dna                | 115 ms                                                      | 124 ms: 1.07x slower                                        |
| regex_effbot             | 1.50 ms                                                     | 1.61 ms: 1.07x slower                                       |
| pickle                   | 6.61 us                                                     | 7.13 us: 1.08x slower                                       |
| python_startup           | 18.7 ms                                                     | 20.4 ms: 1.09x slower                                       |
| python_startup_no_site   | 15.9 ms                                                     | 17.6 ms: 1.11x slower                                       |
| bench_mp_pool            | 62.5 ms                                                     | 70.5 ms: 1.13x slower                                       |
| pathlib                  | 71.4 ms                                                     | 81.5 ms: 1.14x slower                                       |
| unpickle_list            | 2.55 us                                                     | 2.96 us: 1.16x slower                                       |
| async_generators         | 178 ms                                                      | 233 ms: 1.31x slower                                        |
| dask                     | 264 ms                                                      | 366 ms: 1.39x slower                                        |
| Geometric mean           | (ref)                                                       | 1.05x faster                                                |

Benchmark hidden because not significant (7): asyncio_tcp_ssl, aiohttp, nbody, xml_etree_iterparse, bench_thread_pool, deepcopy_reduce, docutils
Ignored benchmarks (14) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 99.95% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
