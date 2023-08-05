
# Results vs. 3.11.0

- fork: faster-cpython
- ref: gc_scan_roots
- machine: linux-x86_64
- commit hash: fb9e869
- commit date: 2023-08-04
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230804-pythonperf2-x86_64-faster%2dcpython-gc_scan_roots-3.13.0a0-fb9e869 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| docutils       | 2.86 sec                                                     | 2.98 sec: 1.04x slower                                                         |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230804-pythonperf2-x86_64-faster%2dcpython-gc_scan_roots-3.13.0a0-fb9e869 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 251 ms                                                       | 260 ms: 1.03x slower                                                           |
| float          | 74.2 ms                                                      | 81.9 ms: 1.10x slower                                                          |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                   |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230804-pythonperf2-x86_64-faster%2dcpython-gc_scan_roots-3.13.0a0-fb9e869 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 150 ms: 1.05x faster                                                           |
| regex_effbot   | 3.50 ms                                                      | 3.47 ms: 1.01x faster                                                          |
| regex_v8       | 23.9 ms                                                      | 24.3 ms: 1.02x slower                                                          |
| regex_dna      | 227 ms                                                       | 245 ms: 1.08x slower                                                           |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230804-pythonperf2-x86_64-faster%2dcpython-gc_scan_roots-3.13.0a0-fb9e869 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.3 ms: 1.30x faster                                                          |
| json_loads           | 28.7 us                                                      | 25.2 us: 1.14x faster                                                          |
| xml_etree_parse      | 158 ms                                                       | 146 ms: 1.08x faster                                                           |
| unpickle_pure_python | 241 us                                                       | 234 us: 1.03x faster                                                           |
| pickle_pure_python   | 319 us                                                       | 318 us: 1.00x faster                                                           |
| xml_etree_iterparse  | 104 ms                                                       | 107 ms: 1.02x slower                                                           |
| unpickle_list        | 4.53 us                                                      | 4.67 us: 1.03x slower                                                          |
| tomli_loads          | 2.26 sec                                                     | 2.34 sec: 1.03x slower                                                         |
| pickle               | 9.64 us                                                      | 10.1 us: 1.05x slower                                                          |
| pickle_dict          | 30.8 us                                                      | 32.9 us: 1.07x slower                                                          |
| xml_etree_process    | 56.5 ms                                                      | 60.4 ms: 1.07x slower                                                          |
| unpickle             | 13.4 us                                                      | 14.5 us: 1.08x slower                                                          |
| xml_etree_generate   | 80.5 ms                                                      | 87.2 ms: 1.08x slower                                                          |
| pickle_list          | 3.83 us                                                      | 4.53 us: 1.18x slower                                                          |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230804-pythonperf2-x86_64-faster%2dcpython-gc_scan_roots-3.13.0a0-fb9e869 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.6 ms: 1.08x slower                                                          |
| python_startup_no_site | 7.76 ms                                                      | 8.68 ms: 1.12x slower                                                          |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230804-pythonperf2-x86_64-faster%2dcpython-gc_scan_roots-3.13.0a0-fb9e869 |
|-----------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 10.3 ms: 1.07x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230804-pythonperf2-x86_64-faster%2dcpython-gc_scan_roots-3.13.0a0-fb9e869 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 156 us: 3.34x faster                                                           |
| asyncio_tcp              | 753 ms                                                       | 369 ms: 2.04x faster                                                           |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.58 sec: 1.95x faster                                                         |
| generators               | 56.0 ms                                                      | 37.1 ms: 1.51x faster                                                          |
| chaos                    | 80.9 ms                                                      | 62.0 ms: 1.30x faster                                                          |
| json_dumps               | 13.4 ms                                                      | 10.3 ms: 1.30x faster                                                          |
| mypy2                    | 451 ms                                                       | 373 ms: 1.21x faster                                                           |
| scimark_lu               | 115 ms                                                       | 97.9 ms: 1.17x faster                                                          |
| coroutines               | 27.6 ms                                                      | 23.7 ms: 1.17x faster                                                          |
| crypto_pyaes             | 83.4 ms                                                      | 72.9 ms: 1.14x faster                                                          |
| json_loads               | 28.7 us                                                      | 25.2 us: 1.14x faster                                                          |
| raytrace                 | 317 ms                                                       | 282 ms: 1.12x faster                                                           |
| nqueens                  | 103 ms                                                       | 92.3 ms: 1.11x faster                                                          |
| logging_format           | 8.11 us                                                      | 7.40 us: 1.10x faster                                                          |
| comprehensions           | 24.6 us                                                      | 22.5 us: 1.10x faster                                                          |
| hexiom                   | 7.13 ms                                                      | 6.51 ms: 1.10x faster                                                          |
| async_tree_memoization   | 630 ms                                                       | 575 ms: 1.09x faster                                                           |
| fannkuch                 | 429 ms                                                       | 393 ms: 1.09x faster                                                           |
| async_tree_none          | 519 ms                                                       | 479 ms: 1.08x faster                                                           |
| mdp                      | 2.75 sec                                                     | 2.55 sec: 1.08x faster                                                         |
| xml_etree_parse          | 158 ms                                                       | 146 ms: 1.08x faster                                                           |
| deltablue                | 4.00 ms                                                      | 3.72 ms: 1.08x faster                                                          |
| json                     | 5.65 ms                                                      | 5.26 ms: 1.07x faster                                                          |
| sqlglot_normalize        | 126 ms                                                       | 118 ms: 1.07x faster                                                           |
| mako                     | 11.0 ms                                                      | 10.3 ms: 1.07x faster                                                          |
| logging_simple           | 7.19 us                                                      | 6.76 us: 1.06x faster                                                          |
| sqlglot_parse            | 1.53 ms                                                      | 1.44 ms: 1.06x faster                                                          |
| bench_thread_pool        | 1.01 ms                                                      | 952 us: 1.06x faster                                                           |
| async_tree_io            | 1.17 sec                                                     | 1.11 sec: 1.06x faster                                                         |
| regex_compile            | 158 ms                                                       | 150 ms: 1.05x faster                                                           |
| deepcopy                 | 399 us                                                       | 385 us: 1.04x faster                                                           |
| sqlglot_transpile        | 1.92 ms                                                      | 1.85 ms: 1.04x faster                                                          |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 723 ms: 1.04x faster                                                           |
| unpickle_pure_python     | 241 us                                                       | 234 us: 1.03x faster                                                           |
| logging_silent           | 101 ns                                                       | 98.3 ns: 1.03x faster                                                          |
| sqlglot_optimize         | 59.8 ms                                                      | 58.9 ms: 1.01x faster                                                          |
| deepcopy_memo            | 38.8 us                                                      | 38.3 us: 1.01x faster                                                          |
| meteor_contest           | 131 ms                                                       | 129 ms: 1.01x faster                                                           |
| regex_effbot             | 3.50 ms                                                      | 3.47 ms: 1.01x faster                                                          |
| pickle_pure_python       | 319 us                                                       | 318 us: 1.00x faster                                                           |
| scimark_monte_carlo      | 68.2 ms                                                      | 68.9 ms: 1.01x slower                                                          |
| pycparser                | 1.32 sec                                                     | 1.34 sec: 1.01x slower                                                         |
| regex_v8                 | 23.9 ms                                                      | 24.3 ms: 1.02x slower                                                          |
| richards_super           | 61.0 ms                                                      | 62.2 ms: 1.02x slower                                                          |
| xml_etree_iterparse      | 104 ms                                                       | 107 ms: 1.02x slower                                                           |
| pathlib                  | 19.1 ms                                                      | 19.6 ms: 1.03x slower                                                          |
| unpickle_list            | 4.53 us                                                      | 4.67 us: 1.03x slower                                                          |
| coverage                 | 84.8 ms                                                      | 87.5 ms: 1.03x slower                                                          |
| pidigits                 | 251 ms                                                       | 260 ms: 1.03x slower                                                           |
| tomli_loads              | 2.26 sec                                                     | 2.34 sec: 1.03x slower                                                         |
| pprint_pformat           | 1.63 sec                                                     | 1.69 sec: 1.04x slower                                                         |
| spectral_norm            | 93.3 ms                                                      | 96.9 ms: 1.04x slower                                                          |
| bench_mp_pool            | 4.62 ms                                                      | 4.82 ms: 1.04x slower                                                          |
| docutils                 | 2.86 sec                                                     | 2.98 sec: 1.04x slower                                                         |
| pickle                   | 9.64 us                                                      | 10.1 us: 1.05x slower                                                          |
| pprint_safe_repr         | 784 ms                                                       | 825 ms: 1.05x slower                                                           |
| gc_traversal             | 3.85 ms                                                      | 4.08 ms: 1.06x slower                                                          |
| pickle_dict              | 30.8 us                                                      | 32.9 us: 1.07x slower                                                          |
| xml_etree_process        | 56.5 ms                                                      | 60.4 ms: 1.07x slower                                                          |
| create_gc_cycles         | 1.61 ms                                                      | 1.73 ms: 1.07x slower                                                          |
| scimark_fft              | 285 ms                                                       | 306 ms: 1.07x slower                                                           |
| go                       | 164 ms                                                       | 177 ms: 1.08x slower                                                           |
| regex_dna                | 227 ms                                                       | 245 ms: 1.08x slower                                                           |
| sqlite_synth             | 2.50 us                                                      | 2.70 us: 1.08x slower                                                          |
| unpickle                 | 13.4 us                                                      | 14.5 us: 1.08x slower                                                          |
| xml_etree_generate       | 80.5 ms                                                      | 87.2 ms: 1.08x slower                                                          |
| python_startup           | 10.8 ms                                                      | 11.6 ms: 1.08x slower                                                          |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 4.41 ms: 1.09x slower                                                          |
| float                    | 74.2 ms                                                      | 81.9 ms: 1.10x slower                                                          |
| python_startup_no_site   | 7.76 ms                                                      | 8.68 ms: 1.12x slower                                                          |
| richards                 | 48.3 ms                                                      | 54.9 ms: 1.14x slower                                                          |
| pyflate                  | 449 ms                                                       | 514 ms: 1.15x slower                                                           |
| telco                    | 6.86 ms                                                      | 8.00 ms: 1.17x slower                                                          |
| pickle_list              | 3.83 us                                                      | 4.53 us: 1.18x slower                                                          |
| async_generators         | 316 ms                                                       | 396 ms: 1.26x slower                                                           |
| unpack_sequence          | 45.6 ns                                                      | 59.7 ns: 1.31x slower                                                          |
| scimark_sor              | 111 ms                                                       | 146 ms: 1.31x slower                                                           |
| dask                     | 410 ms                                                       | 594 ms: 1.45x slower                                                           |
| Geometric mean           | (ref)                                                        | 1.03x faster                                                                   |

Benchmark hidden because not significant (4): tornado_http, deepcopy_reduce, nbody, dulwich_log
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
