
# Results vs. 3.11.0

- fork: faster-cpython
- ref: tweak_ints_monitorin
- machine: linux-x86_64
- commit hash: 83ffca9
- commit date: 2023-08-05
- overall geometric mean: 1.04x faster
- HPT reliability: 83.24%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-pythonperf2-x86_64-faster%2dcpython-tweak_ints_monitorin-3.13.0a0-83ffca9 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| docutils       | 2.86 sec                                                     | 2.93 sec: 1.03x slower                                                                |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-pythonperf2-x86_64-faster%2dcpython-tweak_ints_monitorin-3.13.0a0-83ffca9 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 88.9 ms: 1.02x faster                                                                 |
| pidigits       | 251 ms                                                       | 261 ms: 1.04x slower                                                                  |
| float          | 74.2 ms                                                      | 81.3 ms: 1.10x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-pythonperf2-x86_64-faster%2dcpython-tweak_ints_monitorin-3.13.0a0-83ffca9 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 151 ms: 1.04x faster                                                                  |
| regex_dna      | 227 ms                                                       | 237 ms: 1.04x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                          |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-pythonperf2-x86_64-faster%2dcpython-tweak_ints_monitorin-3.13.0a0-83ffca9 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.3 ms: 1.31x faster                                                                 |
| json_loads           | 28.7 us                                                      | 25.5 us: 1.12x faster                                                                 |
| unpickle_pure_python | 241 us                                                       | 223 us: 1.08x faster                                                                  |
| xml_etree_parse      | 158 ms                                                       | 148 ms: 1.06x faster                                                                  |
| xml_etree_iterparse  | 104 ms                                                       | 106 ms: 1.02x slower                                                                  |
| pickle_pure_python   | 319 us                                                       | 326 us: 1.02x slower                                                                  |
| pickle               | 9.64 us                                                      | 9.99 us: 1.04x slower                                                                 |
| pickle_dict          | 30.8 us                                                      | 31.9 us: 1.04x slower                                                                 |
| xml_etree_generate   | 80.5 ms                                                      | 85.8 ms: 1.07x slower                                                                 |
| tomli_loads          | 2.26 sec                                                     | 2.42 sec: 1.07x slower                                                                |
| unpickle_list        | 4.53 us                                                      | 4.85 us: 1.07x slower                                                                 |
| xml_etree_process    | 56.5 ms                                                      | 60.8 ms: 1.08x slower                                                                 |
| unpickle             | 13.4 us                                                      | 14.7 us: 1.09x slower                                                                 |
| pickle_list          | 3.83 us                                                      | 4.34 us: 1.13x slower                                                                 |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-pythonperf2-x86_64-faster%2dcpython-tweak_ints_monitorin-3.13.0a0-83ffca9 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.6 ms: 1.08x slower                                                                 |
| python_startup_no_site | 7.76 ms                                                      | 8.64 ms: 1.11x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-pythonperf2-x86_64-faster%2dcpython-tweak_ints_monitorin-3.13.0a0-83ffca9 |
|-----------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 10.4 ms: 1.06x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-pythonperf2-x86_64-faster%2dcpython-tweak_ints_monitorin-3.13.0a0-83ffca9 |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 155 us: 3.38x faster                                                                  |
| asyncio_tcp              | 753 ms                                                       | 368 ms: 2.05x faster                                                                  |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.58 sec: 1.95x faster                                                                |
| generators               | 56.0 ms                                                      | 37.4 ms: 1.50x faster                                                                 |
| json_dumps               | 13.4 ms                                                      | 10.3 ms: 1.31x faster                                                                 |
| chaos                    | 80.9 ms                                                      | 62.8 ms: 1.29x faster                                                                 |
| mypy2                    | 451 ms                                                       | 372 ms: 1.21x faster                                                                  |
| coroutines               | 27.6 ms                                                      | 23.3 ms: 1.18x faster                                                                 |
| scimark_lu               | 115 ms                                                       | 100 ms: 1.14x faster                                                                  |
| raytrace                 | 317 ms                                                       | 280 ms: 1.13x faster                                                                  |
| nqueens                  | 103 ms                                                       | 91.3 ms: 1.13x faster                                                                 |
| json_loads               | 28.7 us                                                      | 25.5 us: 1.12x faster                                                                 |
| crypto_pyaes             | 83.4 ms                                                      | 74.3 ms: 1.12x faster                                                                 |
| async_tree_memoization   | 630 ms                                                       | 569 ms: 1.11x faster                                                                  |
| comprehensions           | 24.6 us                                                      | 22.3 us: 1.11x faster                                                                 |
| async_tree_none          | 519 ms                                                       | 471 ms: 1.10x faster                                                                  |
| fannkuch                 | 429 ms                                                       | 389 ms: 1.10x faster                                                                  |
| deltablue                | 4.00 ms                                                      | 3.64 ms: 1.10x faster                                                                 |
| logging_format           | 8.11 us                                                      | 7.40 us: 1.10x faster                                                                 |
| json                     | 5.65 ms                                                      | 5.15 ms: 1.10x faster                                                                 |
| hexiom                   | 7.13 ms                                                      | 6.58 ms: 1.08x faster                                                                 |
| async_tree_io            | 1.17 sec                                                     | 1.08 sec: 1.08x faster                                                                |
| gc_traversal             | 3.85 ms                                                      | 3.56 ms: 1.08x faster                                                                 |
| unpickle_pure_python     | 241 us                                                       | 223 us: 1.08x faster                                                                  |
| sqlglot_normalize        | 126 ms                                                       | 118 ms: 1.07x faster                                                                  |
| mdp                      | 2.75 sec                                                     | 2.57 sec: 1.07x faster                                                                |
| sqlglot_parse            | 1.53 ms                                                      | 1.44 ms: 1.06x faster                                                                 |
| xml_etree_parse          | 158 ms                                                       | 148 ms: 1.06x faster                                                                  |
| bench_thread_pool        | 1.01 ms                                                      | 953 us: 1.06x faster                                                                  |
| mako                     | 11.0 ms                                                      | 10.4 ms: 1.06x faster                                                                 |
| logging_simple           | 7.19 us                                                      | 6.85 us: 1.05x faster                                                                 |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 717 ms: 1.04x faster                                                                  |
| regex_compile            | 158 ms                                                       | 151 ms: 1.04x faster                                                                  |
| deepcopy                 | 399 us                                                       | 384 us: 1.04x faster                                                                  |
| logging_silent           | 101 ns                                                       | 97.2 ns: 1.04x faster                                                                 |
| sqlglot_transpile        | 1.92 ms                                                      | 1.85 ms: 1.04x faster                                                                 |
| nbody                    | 90.7 ms                                                      | 88.9 ms: 1.02x faster                                                                 |
| deepcopy_memo            | 38.8 us                                                      | 38.2 us: 1.02x faster                                                                 |
| meteor_contest           | 131 ms                                                       | 129 ms: 1.01x faster                                                                  |
| coverage                 | 84.8 ms                                                      | 83.9 ms: 1.01x faster                                                                 |
| deepcopy_reduce          | 3.51 us                                                      | 3.47 us: 1.01x faster                                                                 |
| sqlglot_optimize         | 59.8 ms                                                      | 59.4 ms: 1.01x faster                                                                 |
| scimark_monte_carlo      | 68.2 ms                                                      | 69.0 ms: 1.01x slower                                                                 |
| xml_etree_iterparse      | 104 ms                                                       | 106 ms: 1.02x slower                                                                  |
| pickle_pure_python       | 319 us                                                       | 326 us: 1.02x slower                                                                  |
| pycparser                | 1.32 sec                                                     | 1.35 sec: 1.02x slower                                                                |
| docutils                 | 2.86 sec                                                     | 2.93 sec: 1.03x slower                                                                |
| create_gc_cycles         | 1.61 ms                                                      | 1.66 ms: 1.03x slower                                                                 |
| pidigits                 | 251 ms                                                       | 261 ms: 1.04x slower                                                                  |
| pickle                   | 9.64 us                                                      | 9.99 us: 1.04x slower                                                                 |
| pprint_pformat           | 1.63 sec                                                     | 1.69 sec: 1.04x slower                                                                |
| pathlib                  | 19.1 ms                                                      | 19.8 ms: 1.04x slower                                                                 |
| pickle_dict              | 30.8 us                                                      | 31.9 us: 1.04x slower                                                                 |
| regex_dna                | 227 ms                                                       | 237 ms: 1.04x slower                                                                  |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 4.23 ms: 1.05x slower                                                                 |
| bench_mp_pool            | 4.62 ms                                                      | 4.84 ms: 1.05x slower                                                                 |
| pprint_safe_repr         | 784 ms                                                       | 826 ms: 1.05x slower                                                                  |
| scimark_fft              | 285 ms                                                       | 301 ms: 1.06x slower                                                                  |
| xml_etree_generate       | 80.5 ms                                                      | 85.8 ms: 1.07x slower                                                                 |
| tomli_loads              | 2.26 sec                                                     | 2.42 sec: 1.07x slower                                                                |
| unpickle_list            | 4.53 us                                                      | 4.85 us: 1.07x slower                                                                 |
| xml_etree_process        | 56.5 ms                                                      | 60.8 ms: 1.08x slower                                                                 |
| python_startup           | 10.8 ms                                                      | 11.6 ms: 1.08x slower                                                                 |
| unpack_sequence          | 45.6 ns                                                      | 49.6 ns: 1.09x slower                                                                 |
| sqlite_synth             | 2.50 us                                                      | 2.71 us: 1.09x slower                                                                 |
| unpickle                 | 13.4 us                                                      | 14.7 us: 1.09x slower                                                                 |
| go                       | 164 ms                                                       | 179 ms: 1.09x slower                                                                  |
| float                    | 74.2 ms                                                      | 81.3 ms: 1.10x slower                                                                 |
| richards                 | 48.3 ms                                                      | 53.7 ms: 1.11x slower                                                                 |
| python_startup_no_site   | 7.76 ms                                                      | 8.64 ms: 1.11x slower                                                                 |
| pickle_list              | 3.83 us                                                      | 4.34 us: 1.13x slower                                                                 |
| pyflate                  | 449 ms                                                       | 514 ms: 1.15x slower                                                                  |
| telco                    | 6.86 ms                                                      | 8.05 ms: 1.17x slower                                                                 |
| async_generators         | 316 ms                                                       | 397 ms: 1.26x slower                                                                  |
| scimark_sor              | 111 ms                                                       | 146 ms: 1.31x slower                                                                  |
| dask                     | 410 ms                                                       | 591 ms: 1.44x slower                                                                  |
| Geometric mean           | (ref)                                                        | 1.04x faster                                                                          |

Benchmark hidden because not significant (6): regex_effbot, richards_super, regex_v8, dulwich_log, spectral_norm, tornado_http
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 83.24% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
