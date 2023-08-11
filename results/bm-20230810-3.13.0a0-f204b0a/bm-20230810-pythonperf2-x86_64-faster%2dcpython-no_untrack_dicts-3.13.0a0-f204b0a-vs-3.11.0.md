
# Results vs. 3.11.0

- fork: faster-cpython
- ref: no_untrack_dicts
- machine: linux-x86_64
- commit hash: f204b0a
- commit date: 2023-08-10
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230810-pythonperf2-x86_64-faster%2dcpython-no_untrack_dicts-3.13.0a0-f204b0a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| docutils       | 2.86 sec                                                     | 2.93 sec: 1.02x slower                                                            |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                      |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230810-pythonperf2-x86_64-faster%2dcpython-no_untrack_dicts-3.13.0a0-f204b0a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 87.8 ms: 1.03x faster                                                             |
| pidigits       | 251 ms                                                       | 259 ms: 1.03x slower                                                              |
| float          | 74.2 ms                                                      | 81.3 ms: 1.10x slower                                                             |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230810-pythonperf2-x86_64-faster%2dcpython-no_untrack_dicts-3.13.0a0-f204b0a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 149 ms: 1.06x faster                                                              |
| regex_v8       | 23.9 ms                                                      | 24.2 ms: 1.01x slower                                                             |
| regex_effbot   | 3.50 ms                                                      | 3.62 ms: 1.03x slower                                                             |
| regex_dna      | 227 ms                                                       | 252 ms: 1.11x slower                                                              |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230810-pythonperf2-x86_64-faster%2dcpython-no_untrack_dicts-3.13.0a0-f204b0a |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.2 ms: 1.31x faster                                                             |
| json_loads           | 28.7 us                                                      | 25.5 us: 1.13x faster                                                             |
| unpickle_pure_python | 241 us                                                       | 220 us: 1.09x faster                                                              |
| xml_etree_parse      | 158 ms                                                       | 147 ms: 1.07x faster                                                              |
| pickle_pure_python   | 319 us                                                       | 315 us: 1.01x faster                                                              |
| tomli_loads          | 2.26 sec                                                     | 2.29 sec: 1.01x slower                                                            |
| xml_etree_iterparse  | 104 ms                                                       | 107 ms: 1.02x slower                                                              |
| pickle_dict          | 30.8 us                                                      | 32.0 us: 1.04x slower                                                             |
| unpickle_list        | 4.53 us                                                      | 4.75 us: 1.05x slower                                                             |
| pickle               | 9.64 us                                                      | 10.2 us: 1.05x slower                                                             |
| xml_etree_process    | 56.5 ms                                                      | 60.4 ms: 1.07x slower                                                             |
| xml_etree_generate   | 80.5 ms                                                      | 87.1 ms: 1.08x slower                                                             |
| unpickle             | 13.4 us                                                      | 14.7 us: 1.09x slower                                                             |
| pickle_list          | 3.83 us                                                      | 4.52 us: 1.18x slower                                                             |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230810-pythonperf2-x86_64-faster%2dcpython-no_untrack_dicts-3.13.0a0-f204b0a |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.5 ms: 1.07x slower                                                             |
| python_startup_no_site | 7.76 ms                                                      | 8.55 ms: 1.10x slower                                                             |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230810-pythonperf2-x86_64-faster%2dcpython-no_untrack_dicts-3.13.0a0-f204b0a |
|-----------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 10.3 ms: 1.06x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230810-pythonperf2-x86_64-faster%2dcpython-no_untrack_dicts-3.13.0a0-f204b0a |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 153 us: 3.42x faster                                                              |
| asyncio_tcp              | 753 ms                                                       | 369 ms: 2.04x faster                                                              |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.58 sec: 1.95x faster                                                            |
| generators               | 56.0 ms                                                      | 36.4 ms: 1.54x faster                                                             |
| json_dumps               | 13.4 ms                                                      | 10.2 ms: 1.31x faster                                                             |
| chaos                    | 80.9 ms                                                      | 62.1 ms: 1.30x faster                                                             |
| async_tree_memoization   | 630 ms                                                       | 535 ms: 1.18x faster                                                              |
| async_tree_none          | 519 ms                                                       | 453 ms: 1.15x faster                                                              |
| coroutines               | 27.6 ms                                                      | 24.1 ms: 1.14x faster                                                             |
| nqueens                  | 103 ms                                                       | 90.6 ms: 1.13x faster                                                             |
| async_tree_io            | 1.17 sec                                                     | 1.04 sec: 1.13x faster                                                            |
| json_loads               | 28.7 us                                                      | 25.5 us: 1.13x faster                                                             |
| crypto_pyaes             | 83.4 ms                                                      | 74.3 ms: 1.12x faster                                                             |
| scimark_lu               | 115 ms                                                       | 104 ms: 1.11x faster                                                              |
| logging_format           | 8.11 us                                                      | 7.36 us: 1.10x faster                                                             |
| fannkuch                 | 429 ms                                                       | 389 ms: 1.10x faster                                                              |
| comprehensions           | 24.6 us                                                      | 22.3 us: 1.10x faster                                                             |
| raytrace                 | 317 ms                                                       | 288 ms: 1.10x faster                                                              |
| create_gc_cycles         | 1.61 ms                                                      | 1.47 ms: 1.10x faster                                                             |
| unpickle_pure_python     | 241 us                                                       | 220 us: 1.09x faster                                                              |
| hexiom                   | 7.13 ms                                                      | 6.57 ms: 1.09x faster                                                             |
| json                     | 5.65 ms                                                      | 5.20 ms: 1.09x faster                                                             |
| sqlglot_normalize        | 126 ms                                                       | 117 ms: 1.07x faster                                                              |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 698 ms: 1.07x faster                                                              |
| xml_etree_parse          | 158 ms                                                       | 147 ms: 1.07x faster                                                              |
| logging_simple           | 7.19 us                                                      | 6.73 us: 1.07x faster                                                             |
| sqlglot_parse            | 1.53 ms                                                      | 1.44 ms: 1.07x faster                                                             |
| mdp                      | 2.75 sec                                                     | 2.58 sec: 1.06x faster                                                            |
| mako                     | 11.0 ms                                                      | 10.3 ms: 1.06x faster                                                             |
| regex_compile            | 158 ms                                                       | 149 ms: 1.06x faster                                                              |
| deltablue                | 4.00 ms                                                      | 3.78 ms: 1.06x faster                                                             |
| bench_thread_pool        | 1.01 ms                                                      | 958 us: 1.05x faster                                                              |
| coverage                 | 84.8 ms                                                      | 81.5 ms: 1.04x faster                                                             |
| sqlglot_transpile        | 1.92 ms                                                      | 1.85 ms: 1.04x faster                                                             |
| nbody                    | 90.7 ms                                                      | 87.8 ms: 1.03x faster                                                             |
| deepcopy                 | 399 us                                                       | 389 us: 1.03x faster                                                              |
| logging_silent           | 101 ns                                                       | 98.4 ns: 1.02x faster                                                             |
| deepcopy_memo            | 38.8 us                                                      | 37.9 us: 1.02x faster                                                             |
| deepcopy_reduce          | 3.51 us                                                      | 3.45 us: 1.02x faster                                                             |
| gc_traversal             | 3.85 ms                                                      | 3.80 ms: 1.01x faster                                                             |
| pickle_pure_python       | 319 us                                                       | 315 us: 1.01x faster                                                              |
| meteor_contest           | 131 ms                                                       | 129 ms: 1.01x faster                                                              |
| richards_super           | 61.0 ms                                                      | 60.4 ms: 1.01x faster                                                             |
| sqlglot_optimize         | 59.8 ms                                                      | 59.4 ms: 1.01x faster                                                             |
| spectral_norm            | 93.3 ms                                                      | 93.0 ms: 1.00x faster                                                             |
| regex_v8                 | 23.9 ms                                                      | 24.2 ms: 1.01x slower                                                             |
| tomli_loads              | 2.26 sec                                                     | 2.29 sec: 1.01x slower                                                            |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 4.10 ms: 1.01x slower                                                             |
| xml_etree_iterparse      | 104 ms                                                       | 107 ms: 1.02x slower                                                              |
| docutils                 | 2.86 sec                                                     | 2.93 sec: 1.02x slower                                                            |
| pprint_pformat           | 1.63 sec                                                     | 1.68 sec: 1.03x slower                                                            |
| pidigits                 | 251 ms                                                       | 259 ms: 1.03x slower                                                              |
| pathlib                  | 19.1 ms                                                      | 19.7 ms: 1.03x slower                                                             |
| regex_effbot             | 3.50 ms                                                      | 3.62 ms: 1.03x slower                                                             |
| pickle_dict              | 30.8 us                                                      | 32.0 us: 1.04x slower                                                             |
| pprint_safe_repr         | 784 ms                                                       | 820 ms: 1.05x slower                                                              |
| unpickle_list            | 4.53 us                                                      | 4.75 us: 1.05x slower                                                             |
| pickle                   | 9.64 us                                                      | 10.2 us: 1.05x slower                                                             |
| go                       | 164 ms                                                       | 173 ms: 1.05x slower                                                              |
| scimark_fft              | 285 ms                                                       | 301 ms: 1.06x slower                                                              |
| scimark_monte_carlo      | 68.2 ms                                                      | 72.4 ms: 1.06x slower                                                             |
| xml_etree_process        | 56.5 ms                                                      | 60.4 ms: 1.07x slower                                                             |
| python_startup           | 10.8 ms                                                      | 11.5 ms: 1.07x slower                                                             |
| xml_etree_generate       | 80.5 ms                                                      | 87.1 ms: 1.08x slower                                                             |
| sqlite_synth             | 2.50 us                                                      | 2.71 us: 1.09x slower                                                             |
| unpickle                 | 13.4 us                                                      | 14.7 us: 1.09x slower                                                             |
| float                    | 74.2 ms                                                      | 81.3 ms: 1.10x slower                                                             |
| python_startup_no_site   | 7.76 ms                                                      | 8.55 ms: 1.10x slower                                                             |
| richards                 | 48.3 ms                                                      | 53.5 ms: 1.11x slower                                                             |
| regex_dna                | 227 ms                                                       | 252 ms: 1.11x slower                                                              |
| pyflate                  | 449 ms                                                       | 512 ms: 1.14x slower                                                              |
| telco                    | 6.86 ms                                                      | 8.08 ms: 1.18x slower                                                             |
| pickle_list              | 3.83 us                                                      | 4.52 us: 1.18x slower                                                             |
| async_generators         | 316 ms                                                       | 392 ms: 1.24x slower                                                              |
| unpack_sequence          | 45.6 ns                                                      | 60.1 ns: 1.32x slower                                                             |
| scimark_sor              | 111 ms                                                       | 150 ms: 1.35x slower                                                              |
| dask                     | 410 ms                                                       | 587 ms: 1.43x slower                                                              |
| Geometric mean           | (ref)                                                        | 1.04x faster                                                                      |

Benchmark hidden because not significant (5): tornado_http, dulwich_log, pycparser, bench_mp_pool, mypy2
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
