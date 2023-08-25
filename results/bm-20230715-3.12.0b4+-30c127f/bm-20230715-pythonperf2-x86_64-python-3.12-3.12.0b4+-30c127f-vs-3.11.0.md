
# Results vs. 3.11.0

- fork: python
- ref: 3.12
- machine: linux-x86_64
- commit hash: 30c127f
- commit date: 2023-07-15
- overall geometric mean: 1.06x faster
- HPT reliability: 99.70%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230715-pythonperf2-x86_64-python-3.12-3.12.0b4+-30c127f |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 285 ms: 1.01x faster                                         |
| docutils       | 2.86 sec                                                     | 2.91 sec: 1.02x slower                                       |
| Geometric mean | (ref)                                                        | 1.00x slower                                                 |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230715-pythonperf2-x86_64-python-3.12-3.12.0b4+-30c127f |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| pidigits       | 251 ms                                                       | 260 ms: 1.04x slower                                         |
| float          | 74.2 ms                                                      | 78.6 ms: 1.06x slower                                        |
| Geometric mean | (ref)                                                        | 1.03x slower                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230715-pythonperf2-x86_64-python-3.12-3.12.0b4+-30c127f |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 145 ms: 1.09x faster                                         |
| regex_v8       | 23.9 ms                                                      | 24.0 ms: 1.00x slower                                        |
| regex_dna      | 227 ms                                                       | 240 ms: 1.06x slower                                         |
| Geometric mean | (ref)                                                        | 1.01x faster                                                 |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230715-pythonperf2-x86_64-python-3.12-3.12.0b4+-30c127f |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.3 ms: 1.31x faster                                        |
| json_loads           | 28.7 us                                                      | 24.9 us: 1.15x faster                                        |
| unpickle_pure_python | 241 us                                                       | 210 us: 1.14x faster                                         |
| xml_etree_parse      | 158 ms                                                       | 149 ms: 1.06x faster                                         |
| tomli_loads          | 2.26 sec                                                     | 2.19 sec: 1.03x faster                                       |
| pickle_pure_python   | 319 us                                                       | 323 us: 1.01x slower                                         |
| xml_etree_process    | 56.5 ms                                                      | 59.1 ms: 1.05x slower                                        |
| pickle               | 9.64 us                                                      | 10.2 us: 1.06x slower                                        |
| xml_etree_generate   | 80.5 ms                                                      | 85.7 ms: 1.06x slower                                        |
| unpickle             | 13.4 us                                                      | 14.6 us: 1.09x slower                                        |
| pickle_dict          | 30.8 us                                                      | 33.5 us: 1.09x slower                                        |
| unpickle_list        | 4.53 us                                                      | 4.95 us: 1.09x slower                                        |
| pickle_list          | 3.83 us                                                      | 4.41 us: 1.15x slower                                        |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                 |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230715-pythonperf2-x86_64-python-3.12-3.12.0b4+-30c127f |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.5 ms: 1.07x slower                                        |
| python_startup_no_site | 7.76 ms                                                      | 8.52 ms: 1.10x slower                                        |
| Geometric mean         | (ref)                                                        | 1.08x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230715-pythonperf2-x86_64-python-3.12-3.12.0b4+-30c127f |
|-----------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 10.0 ms: 1.10x faster                                        |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230715-pythonperf2-x86_64-python-3.12-3.12.0b4+-30c127f |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 153 us: 3.42x faster                                         |
| asyncio_tcp              | 753 ms                                                       | 378 ms: 1.99x faster                                         |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.57 sec: 1.96x faster                                       |
| generators               | 56.0 ms                                                      | 36.1 ms: 1.55x faster                                        |
| json_dumps               | 13.4 ms                                                      | 10.3 ms: 1.31x faster                                        |
| chaos                    | 80.9 ms                                                      | 63.2 ms: 1.28x faster                                        |
| fannkuch                 | 429 ms                                                       | 345 ms: 1.24x faster                                         |
| deltablue                | 4.00 ms                                                      | 3.24 ms: 1.23x faster                                        |
| mypy2                    | 451 ms                                                       | 368 ms: 1.23x faster                                         |
| hexiom                   | 7.13 ms                                                      | 5.87 ms: 1.22x faster                                        |
| coroutines               | 27.6 ms                                                      | 22.7 ms: 1.21x faster                                        |
| richards_super           | 61.0 ms                                                      | 51.5 ms: 1.19x faster                                        |
| scimark_lu               | 115 ms                                                       | 99.4 ms: 1.15x faster                                        |
| json_loads               | 28.7 us                                                      | 24.9 us: 1.15x faster                                        |
| unpickle_pure_python     | 241 us                                                       | 210 us: 1.14x faster                                         |
| nqueens                  | 103 ms                                                       | 90.3 ms: 1.14x faster                                        |
| async_tree_memoization   | 630 ms                                                       | 555 ms: 1.13x faster                                         |
| comprehensions           | 24.6 us                                                      | 21.9 us: 1.12x faster                                        |
| async_tree_none          | 519 ms                                                       | 464 ms: 1.12x faster                                         |
| go                       | 164 ms                                                       | 148 ms: 1.11x faster                                         |
| async_tree_io            | 1.17 sec                                                     | 1.06 sec: 1.11x faster                                       |
| sqlglot_parse            | 1.53 ms                                                      | 1.39 ms: 1.10x faster                                        |
| sqlglot_normalize        | 126 ms                                                       | 115 ms: 1.10x faster                                         |
| mako                     | 11.0 ms                                                      | 10.0 ms: 1.10x faster                                        |
| json                     | 5.65 ms                                                      | 5.18 ms: 1.09x faster                                        |
| logging_format           | 8.11 us                                                      | 7.44 us: 1.09x faster                                        |
| regex_compile            | 158 ms                                                       | 145 ms: 1.09x faster                                         |
| richards                 | 48.3 ms                                                      | 44.4 ms: 1.09x faster                                        |
| deepcopy                 | 399 us                                                       | 374 us: 1.07x faster                                         |
| mdp                      | 2.75 sec                                                     | 2.57 sec: 1.07x faster                                       |
| sqlglot_transpile        | 1.92 ms                                                      | 1.80 ms: 1.07x faster                                        |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 707 ms: 1.06x faster                                         |
| xml_etree_parse          | 158 ms                                                       | 149 ms: 1.06x faster                                         |
| bench_thread_pool        | 1.01 ms                                                      | 961 us: 1.05x faster                                         |
| logging_simple           | 7.19 us                                                      | 6.85 us: 1.05x faster                                        |
| sqlglot_optimize         | 59.8 ms                                                      | 57.5 ms: 1.04x faster                                        |
| deepcopy_reduce          | 3.51 us                                                      | 3.39 us: 1.04x faster                                        |
| tomli_loads              | 2.26 sec                                                     | 2.19 sec: 1.03x faster                                       |
| logging_silent           | 101 ns                                                       | 97.7 ns: 1.03x faster                                        |
| deepcopy_memo            | 38.8 us                                                      | 37.6 us: 1.03x faster                                        |
| dulwich_log              | 68.4 ms                                                      | 66.4 ms: 1.03x faster                                        |
| pycparser                | 1.32 sec                                                     | 1.28 sec: 1.03x faster                                       |
| meteor_contest           | 131 ms                                                       | 128 ms: 1.02x faster                                         |
| raytrace                 | 317 ms                                                       | 311 ms: 1.02x faster                                         |
| crypto_pyaes             | 83.4 ms                                                      | 82.1 ms: 1.02x faster                                        |
| scimark_sor              | 111 ms                                                       | 109 ms: 1.02x faster                                         |
| pyflate                  | 449 ms                                                       | 442 ms: 1.01x faster                                         |
| 2to3                     | 288 ms                                                       | 285 ms: 1.01x faster                                         |
| spectral_norm            | 93.3 ms                                                      | 92.7 ms: 1.01x faster                                        |
| scimark_monte_carlo      | 68.2 ms                                                      | 67.9 ms: 1.01x faster                                        |
| regex_v8                 | 23.9 ms                                                      | 24.0 ms: 1.00x slower                                        |
| pathlib                  | 19.1 ms                                                      | 19.2 ms: 1.01x slower                                        |
| pickle_pure_python       | 319 us                                                       | 323 us: 1.01x slower                                         |
| docutils                 | 2.86 sec                                                     | 2.91 sec: 1.02x slower                                       |
| telco                    | 6.86 ms                                                      | 7.01 ms: 1.02x slower                                        |
| pprint_safe_repr         | 784 ms                                                       | 801 ms: 1.02x slower                                         |
| pidigits                 | 251 ms                                                       | 260 ms: 1.04x slower                                         |
| create_gc_cycles         | 1.61 ms                                                      | 1.67 ms: 1.04x slower                                        |
| xml_etree_process        | 56.5 ms                                                      | 59.1 ms: 1.05x slower                                        |
| bench_mp_pool            | 4.62 ms                                                      | 4.87 ms: 1.05x slower                                        |
| regex_dna                | 227 ms                                                       | 240 ms: 1.06x slower                                         |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 4.28 ms: 1.06x slower                                        |
| float                    | 74.2 ms                                                      | 78.6 ms: 1.06x slower                                        |
| pickle                   | 9.64 us                                                      | 10.2 us: 1.06x slower                                        |
| scimark_fft              | 285 ms                                                       | 302 ms: 1.06x slower                                         |
| coverage                 | 84.8 ms                                                      | 90.1 ms: 1.06x slower                                        |
| xml_etree_generate       | 80.5 ms                                                      | 85.7 ms: 1.06x slower                                        |
| python_startup           | 10.8 ms                                                      | 11.5 ms: 1.07x slower                                        |
| unpack_sequence          | 45.6 ns                                                      | 49.0 ns: 1.07x slower                                        |
| sqlite_synth             | 2.50 us                                                      | 2.71 us: 1.08x slower                                        |
| unpickle                 | 13.4 us                                                      | 14.6 us: 1.09x slower                                        |
| pickle_dict              | 30.8 us                                                      | 33.5 us: 1.09x slower                                        |
| unpickle_list            | 4.53 us                                                      | 4.95 us: 1.09x slower                                        |
| gc_traversal             | 3.85 ms                                                      | 4.20 ms: 1.09x slower                                        |
| python_startup_no_site   | 7.76 ms                                                      | 8.52 ms: 1.10x slower                                        |
| pickle_list              | 3.83 us                                                      | 4.41 us: 1.15x slower                                        |
| async_generators         | 316 ms                                                       | 388 ms: 1.23x slower                                         |
| dask                     | 410 ms                                                       | 564 ms: 1.38x slower                                         |
| Geometric mean           | (ref)                                                        | 1.06x faster                                                 |

Benchmark hidden because not significant (5): nbody, regex_effbot, pprint_pformat, tornado_http, xml_etree_iterparse
Ignored benchmarks (16) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 99.70% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x
