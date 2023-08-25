
# Results vs. 3.11.0

- fork: python
- ref: 3.12
- machine: windows-amd64
- commit hash: d20d52b
- commit date: 2023-08-11
- overall geometric mean: 1.04x faster
- HPT reliability: 98.49%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-pythonperf1-amd64-python-3.12-3.12.0rc1+-d20d52b |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 214 ms: 1.02x slower                                         |
| tornado_http   | 91.8 ms                                                     | 87.3 ms: 1.05x faster                                        |
| Geometric mean | (ref)                                                       | 1.01x faster                                                 |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-pythonperf1-amd64-python-3.12-3.12.0rc1+-d20d52b |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 147 ms: 1.01x faster                                         |
| nbody          | 70.0 ms                                                     | 71.8 ms: 1.03x slower                                        |
| Geometric mean | (ref)                                                       | 1.00x slower                                                 |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-pythonperf1-amd64-python-3.12-3.12.0rc1+-d20d52b |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 89.7 ms: 1.01x faster                                        |
| regex_v8       | 13.8 ms                                                     | 13.8 ms: 1.00x faster                                        |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                         |
| regex_effbot   | 1.50 ms                                                     | 1.61 ms: 1.08x slower                                        |
| Geometric mean | (ref)                                                       | 1.03x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-pythonperf1-amd64-python-3.12-3.12.0rc1+-d20d52b |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.86 ms: 1.29x faster                                        |
| unpickle_pure_python | 152 us                                                      | 139 us: 1.09x faster                                         |
| xml_etree_parse      | 95.9 ms                                                     | 90.4 ms: 1.06x faster                                        |
| pickle_dict          | 18.5 us                                                     | 18.1 us: 1.02x faster                                        |
| pickle_pure_python   | 200 us                                                      | 202 us: 1.01x slower                                         |
| unpickle             | 8.09 us                                                     | 8.18 us: 1.01x slower                                        |
| xml_etree_iterparse  | 62.6 ms                                                     | 64.3 ms: 1.03x slower                                        |
| json_loads           | 12.9 us                                                     | 13.6 us: 1.05x slower                                        |
| xml_etree_process    | 37.1 ms                                                     | 39.1 ms: 1.06x slower                                        |
| pickle_list          | 2.68 us                                                     | 2.86 us: 1.07x slower                                        |
| xml_etree_generate   | 52.2 ms                                                     | 56.7 ms: 1.09x slower                                        |
| pickle               | 6.61 us                                                     | 7.25 us: 1.10x slower                                        |
| unpickle_list        | 2.55 us                                                     | 2.82 us: 1.11x slower                                        |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                 |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-pythonperf1-amd64-python-3.12-3.12.0rc1+-d20d52b |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 16.6 ms: 1.04x slower                                        |
| python_startup         | 18.7 ms                                                     | 19.6 ms: 1.05x slower                                        |
| Geometric mean         | (ref)                                                       | 1.04x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-pythonperf1-amd64-python-3.12-3.12.0rc1+-d20d52b |
|-----------|:-----------------------------------------------------------:|:------------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 6.94 ms: 1.05x faster                                        |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-pythonperf1-amd64-python-3.12-3.12.0rc1+-d20d52b |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 95.1 us: 3.38x faster                                        |
| asyncio_tcp              | 699 ms                                                      | 472 ms: 1.48x faster                                         |
| generators               | 33.8 ms                                                     | 23.0 ms: 1.47x faster                                        |
| json_dumps               | 7.56 ms                                                     | 5.86 ms: 1.29x faster                                        |
| richards_super           | 37.5 ms                                                     | 30.0 ms: 1.25x faster                                        |
| unpack_sequence          | 46.1 ns                                                     | 38.2 ns: 1.21x faster                                        |
| deltablue                | 2.61 ms                                                     | 2.18 ms: 1.20x faster                                        |
| richards                 | 30.6 ms                                                     | 26.5 ms: 1.16x faster                                        |
| sqlglot_parse            | 952 us                                                      | 825 us: 1.15x faster                                         |
| logging_silent           | 69.8 ns                                                     | 60.7 ns: 1.15x faster                                        |
| mdp                      | 1.67 sec                                                    | 1.47 sec: 1.14x faster                                       |
| sqlglot_transpile        | 1.16 ms                                                     | 1.04 ms: 1.12x faster                                        |
| async_tree_none          | 320 ms                                                      | 290 ms: 1.11x faster                                         |
| json                     | 3.25 ms                                                     | 2.95 ms: 1.10x faster                                        |
| async_tree_memoization   | 371 ms                                                      | 337 ms: 1.10x faster                                         |
| coverage                 | 55.9 ms                                                     | 51.0 ms: 1.10x faster                                        |
| mypy2                    | 229 ms                                                      | 209 ms: 1.10x faster                                         |
| go                       | 97.3 ms                                                     | 89.0 ms: 1.09x faster                                        |
| unpickle_pure_python     | 152 us                                                      | 139 us: 1.09x faster                                         |
| raytrace                 | 211 ms                                                      | 193 ms: 1.09x faster                                         |
| comprehensions           | 15.9 us                                                     | 14.7 us: 1.09x faster                                        |
| hexiom                   | 4.55 ms                                                     | 4.21 ms: 1.08x faster                                        |
| async_tree_io            | 779 ms                                                      | 720 ms: 1.08x faster                                         |
| dulwich_log              | 44.5 ms                                                     | 41.3 ms: 1.08x faster                                        |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.96 sec: 1.08x faster                                       |
| chaos                    | 47.1 ms                                                     | 44.2 ms: 1.07x faster                                        |
| xml_etree_parse          | 95.9 ms                                                     | 90.4 ms: 1.06x faster                                        |
| scimark_lu               | 63.5 ms                                                     | 59.9 ms: 1.06x faster                                        |
| tornado_http             | 91.8 ms                                                     | 87.3 ms: 1.05x faster                                        |
| async_tree_cpu_io_mixed  | 501 ms                                                      | 477 ms: 1.05x faster                                         |
| aiohttp                  | 899 us                                                      | 856 us: 1.05x faster                                         |
| mako                     | 7.26 ms                                                     | 6.94 ms: 1.05x faster                                        |
| nqueens                  | 64.9 ms                                                     | 62.1 ms: 1.04x faster                                        |
| fannkuch                 | 252 ms                                                      | 244 ms: 1.03x faster                                         |
| coroutines               | 14.6 ms                                                     | 14.2 ms: 1.03x faster                                        |
| spectral_norm            | 67.9 ms                                                     | 66.4 ms: 1.02x faster                                        |
| pickle_dict              | 18.5 us                                                     | 18.1 us: 1.02x faster                                        |
| sqlglot_normalize        | 190 ms                                                      | 187 ms: 1.02x faster                                         |
| meteor_contest           | 74.7 ms                                                     | 73.4 ms: 1.02x faster                                        |
| scimark_monte_carlo      | 44.6 ms                                                     | 43.9 ms: 1.02x faster                                        |
| pyflate                  | 304 ms                                                      | 299 ms: 1.02x faster                                         |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.53 ms: 1.02x faster                                        |
| sqlglot_optimize         | 34.9 ms                                                     | 34.5 ms: 1.01x faster                                        |
| regex_compile            | 90.6 ms                                                     | 89.7 ms: 1.01x faster                                        |
| pidigits                 | 148 ms                                                      | 147 ms: 1.01x faster                                         |
| logging_simple           | 6.61 us                                                     | 6.56 us: 1.01x faster                                        |
| deepcopy                 | 246 us                                                      | 244 us: 1.01x faster                                         |
| regex_v8                 | 13.8 ms                                                     | 13.8 ms: 1.00x faster                                        |
| pickle_pure_python       | 200 us                                                      | 202 us: 1.01x slower                                         |
| deepcopy_memo            | 25.2 us                                                     | 25.5 us: 1.01x slower                                        |
| unpickle                 | 8.09 us                                                     | 8.18 us: 1.01x slower                                        |
| 2to3                     | 209 ms                                                      | 214 ms: 1.02x slower                                         |
| nbody                    | 70.0 ms                                                     | 71.8 ms: 1.03x slower                                        |
| xml_etree_iterparse      | 62.6 ms                                                     | 64.3 ms: 1.03x slower                                        |
| scimark_fft              | 178 ms                                                      | 184 ms: 1.03x slower                                         |
| gc_traversal             | 1.46 ms                                                     | 1.51 ms: 1.03x slower                                        |
| pprint_pformat           | 1.04 sec                                                    | 1.07 sec: 1.03x slower                                       |
| pprint_safe_repr         | 512 ms                                                      | 530 ms: 1.04x slower                                         |
| create_gc_cycles         | 693 us                                                      | 719 us: 1.04x slower                                         |
| python_startup_no_site   | 15.9 ms                                                     | 16.6 ms: 1.04x slower                                        |
| sqlite_synth             | 1.68 us                                                     | 1.76 us: 1.04x slower                                        |
| python_startup           | 18.7 ms                                                     | 19.6 ms: 1.05x slower                                        |
| regex_dna                | 115 ms                                                      | 121 ms: 1.05x slower                                         |
| deepcopy_reduce          | 2.07 us                                                     | 2.18 us: 1.05x slower                                        |
| telco                    | 3.90 ms                                                     | 4.11 ms: 1.05x slower                                        |
| json_loads               | 12.9 us                                                     | 13.6 us: 1.05x slower                                        |
| xml_etree_process        | 37.1 ms                                                     | 39.1 ms: 1.06x slower                                        |
| bench_mp_pool            | 62.5 ms                                                     | 66.5 ms: 1.06x slower                                        |
| pickle_list              | 2.68 us                                                     | 2.86 us: 1.07x slower                                        |
| regex_effbot             | 1.50 ms                                                     | 1.61 ms: 1.08x slower                                        |
| xml_etree_generate       | 52.2 ms                                                     | 56.7 ms: 1.09x slower                                        |
| pathlib                  | 71.4 ms                                                     | 78.1 ms: 1.09x slower                                        |
| pickle                   | 6.61 us                                                     | 7.25 us: 1.10x slower                                        |
| scimark_sor              | 75.6 ms                                                     | 83.7 ms: 1.11x slower                                        |
| unpickle_list            | 2.55 us                                                     | 2.82 us: 1.11x slower                                        |
| async_generators         | 178 ms                                                      | 233 ms: 1.31x slower                                         |
| dask                     | 264 ms                                                      | 367 ms: 1.39x slower                                         |
| Geometric mean           | (ref)                                                       | 1.04x faster                                                 |

Benchmark hidden because not significant (7): bench_thread_pool, float, pycparser, logging_format, crypto_pyaes, tomli_loads, docutils
Ignored benchmarks (14) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 98.49% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
