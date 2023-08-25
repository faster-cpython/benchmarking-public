
# Results vs. 3.10.4

- fork: faster-cpython
- ref: incremental_gc
- machine: linux-x86_64
- commit hash: 82d43ba
- commit date: 2023-08-11
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-pythonperf2-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-82d43ba |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| docutils       | 3.40 sec                                                     | 2.78 sec: 1.22x faster                                                          |
| tornado_http   | 152 ms                                                       | 129 ms: 1.18x faster                                                            |
| Geometric mean | (ref)                                                        | 1.20x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-pythonperf2-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-82d43ba |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 85.8 ms: 1.60x faster                                                           |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                                            |
| float          | 110 ms                                                       | 116 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                        | 1.17x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-pythonperf2-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-82d43ba |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 151 ms: 1.28x faster                                                            |
| regex_v8       | 26.6 ms                                                      | 23.8 ms: 1.12x faster                                                           |
| regex_dna      | 259 ms                                                       | 236 ms: 1.10x faster                                                            |
| regex_effbot   | 2.99 ms                                                      | 3.37 ms: 1.13x slower                                                           |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-pythonperf2-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-82d43ba |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 218 us: 1.47x faster                                                            |
| pickle_pure_python   | 457 us                                                       | 315 us: 1.45x faster                                                            |
| json_dumps           | 14.2 ms                                                      | 10.2 ms: 1.39x faster                                                           |
| xml_etree_process    | 76.0 ms                                                      | 59.7 ms: 1.27x faster                                                           |
| tomli_loads          | 2.97 sec                                                     | 2.38 sec: 1.25x faster                                                          |
| json_loads           | 30.0 us                                                      | 26.0 us: 1.15x faster                                                           |
| pickle               | 9.94 us                                                      | 9.78 us: 1.02x faster                                                           |
| pickle_list          | 4.11 us                                                      | 4.22 us: 1.03x slower                                                           |
| unpickle_list        | 4.49 us                                                      | 4.64 us: 1.03x slower                                                           |
| unpickle             | 14.2 us                                                      | 15.0 us: 1.06x slower                                                           |
| pickle_dict          | 30.0 us                                                      | 31.8 us: 1.06x slower                                                           |
| xml_etree_parse      | 162 ms                                                       | 543 ms: 3.36x slower                                                            |
| xml_etree_iterparse  | 110 ms                                                       | 515 ms: 4.67x slower                                                            |
| Geometric mean       | (ref)                                                        | 1.09x slower                                                                    |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-pythonperf2-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-82d43ba |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.8 ms: 1.03x slower                                                           |
| python_startup_no_site | 7.32 ms                                                      | 8.75 ms: 1.19x slower                                                           |
| Geometric mean         | (ref)                                                        | 1.11x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-pythonperf2-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-82d43ba |
|-----------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 10.3 ms: 1.43x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-pythonperf2-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-82d43ba |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 156 us: 3.35x faster                                                            |
| async_tree_io            | 1.61 sec                                                     | 726 ms: 2.21x faster                                                            |
| asyncio_tcp              | 782 ms                                                       | 369 ms: 2.12x faster                                                            |
| async_tree_none          | 700 ms                                                       | 352 ms: 1.99x faster                                                            |
| deltablue                | 7.47 ms                                                      | 3.80 ms: 1.97x faster                                                           |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.58 sec: 1.96x faster                                                          |
| async_tree_memoization   | 824 ms                                                       | 434 ms: 1.90x faster                                                            |
| raytrace                 | 488 ms                                                       | 280 ms: 1.74x faster                                                            |
| chaos                    | 107 ms                                                       | 61.7 ms: 1.74x faster                                                           |
| logging_silent           | 166 ns                                                       | 97.4 ns: 1.70x faster                                                           |
| scimark_lu               | 164 ms                                                       | 101 ms: 1.62x faster                                                            |
| scimark_monte_carlo      | 109 ms                                                       | 68.0 ms: 1.61x faster                                                           |
| crypto_pyaes             | 118 ms                                                       | 73.5 ms: 1.61x faster                                                           |
| nbody                    | 137 ms                                                       | 85.8 ms: 1.60x faster                                                           |
| generators               | 58.0 ms                                                      | 36.7 ms: 1.58x faster                                                           |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 611 ms: 1.56x faster                                                            |
| richards_super           | 90.8 ms                                                      | 59.5 ms: 1.53x faster                                                           |
| sqlglot_parse            | 2.26 ms                                                      | 1.48 ms: 1.52x faster                                                           |
| go                       | 259 ms                                                       | 175 ms: 1.48x faster                                                            |
| unpickle_pure_python     | 321 us                                                       | 218 us: 1.47x faster                                                            |
| spectral_norm            | 136 ms                                                       | 93.2 ms: 1.46x faster                                                           |
| pickle_pure_python       | 457 us                                                       | 315 us: 1.45x faster                                                            |
| hexiom                   | 9.52 ms                                                      | 6.58 ms: 1.45x faster                                                           |
| mako                     | 14.7 ms                                                      | 10.3 ms: 1.43x faster                                                           |
| richards                 | 74.1 ms                                                      | 53.0 ms: 1.40x faster                                                           |
| bench_mp_pool            | 7.18 ms                                                      | 5.14 ms: 1.40x faster                                                           |
| json_dumps               | 14.2 ms                                                      | 10.2 ms: 1.39x faster                                                           |
| sqlglot_transpile        | 2.71 ms                                                      | 1.95 ms: 1.39x faster                                                           |
| pyflate                  | 697 ms                                                       | 511 ms: 1.36x faster                                                            |
| deepcopy_memo            | 48.9 us                                                      | 37.0 us: 1.32x faster                                                           |
| pprint_pformat           | 2.15 sec                                                     | 1.64 sec: 1.31x faster                                                          |
| pprint_safe_repr         | 1.05 sec                                                     | 803 ms: 1.31x faster                                                            |
| pycparser                | 1.66 sec                                                     | 1.27 sec: 1.30x faster                                                          |
| logging_simple           | 8.90 us                                                      | 6.87 us: 1.29x faster                                                           |
| coroutines               | 30.4 ms                                                      | 23.5 ms: 1.29x faster                                                           |
| regex_compile            | 194 ms                                                       | 151 ms: 1.28x faster                                                            |
| fannkuch                 | 496 ms                                                       | 387 ms: 1.28x faster                                                            |
| logging_format           | 9.57 us                                                      | 7.48 us: 1.28x faster                                                           |
| xml_etree_process        | 76.0 ms                                                      | 59.7 ms: 1.27x faster                                                           |
| tomli_loads              | 2.97 sec                                                     | 2.38 sec: 1.25x faster                                                          |
| scimark_sor              | 177 ms                                                       | 142 ms: 1.25x faster                                                            |
| unpack_sequence          | 59.5 ns                                                      | 47.8 ns: 1.25x faster                                                           |
| nqueens                  | 112 ms                                                       | 91.4 ms: 1.23x faster                                                           |
| comprehensions           | 26.9 us                                                      | 22.0 us: 1.23x faster                                                           |
| docutils                 | 3.40 sec                                                     | 2.78 sec: 1.22x faster                                                          |
| sqlglot_normalize        | 144 ms                                                       | 119 ms: 1.21x faster                                                            |
| deepcopy                 | 454 us                                                       | 380 us: 1.19x faster                                                            |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 4.38 ms: 1.19x faster                                                           |
| tornado_http             | 152 ms                                                       | 129 ms: 1.18x faster                                                            |
| sqlglot_optimize         | 70.3 ms                                                      | 59.9 ms: 1.17x faster                                                           |
| bench_thread_pool        | 1.14 ms                                                      | 971 us: 1.17x faster                                                            |
| scimark_fft              | 359 ms                                                       | 308 ms: 1.17x faster                                                            |
| dulwich_log              | 80.1 ms                                                      | 68.6 ms: 1.17x faster                                                           |
| mdp                      | 3.03 sec                                                     | 2.60 sec: 1.17x faster                                                          |
| deepcopy_reduce          | 4.03 us                                                      | 3.46 us: 1.16x faster                                                           |
| json_loads               | 30.0 us                                                      | 26.0 us: 1.15x faster                                                           |
| json                     | 5.96 ms                                                      | 5.19 ms: 1.15x faster                                                           |
| regex_v8                 | 26.6 ms                                                      | 23.8 ms: 1.12x faster                                                           |
| pathlib                  | 21.7 ms                                                      | 19.6 ms: 1.11x faster                                                           |
| sqlite_synth             | 2.97 us                                                      | 2.70 us: 1.10x faster                                                           |
| regex_dna                | 259 ms                                                       | 236 ms: 1.10x faster                                                            |
| create_gc_cycles         | 1.82 ms                                                      | 1.67 ms: 1.09x faster                                                           |
| meteor_contest           | 137 ms                                                       | 127 ms: 1.08x faster                                                            |
| async_generators         | 422 ms                                                       | 405 ms: 1.04x faster                                                            |
| pidigits                 | 271 ms                                                       | 260 ms: 1.04x faster                                                            |
| mypy2                    | 466 ms                                                       | 457 ms: 1.02x faster                                                            |
| pickle                   | 9.94 us                                                      | 9.78 us: 1.02x faster                                                           |
| pickle_list              | 4.11 us                                                      | 4.22 us: 1.03x slower                                                           |
| python_startup           | 11.5 ms                                                      | 11.8 ms: 1.03x slower                                                           |
| unpickle_list            | 4.49 us                                                      | 4.64 us: 1.03x slower                                                           |
| float                    | 110 ms                                                       | 116 ms: 1.05x slower                                                            |
| unpickle                 | 14.2 us                                                      | 15.0 us: 1.06x slower                                                           |
| pickle_dict              | 30.0 us                                                      | 31.8 us: 1.06x slower                                                           |
| regex_effbot             | 2.99 ms                                                      | 3.37 ms: 1.13x slower                                                           |
| telco                    | 7.14 ms                                                      | 8.16 ms: 1.14x slower                                                           |
| python_startup_no_site   | 7.32 ms                                                      | 8.75 ms: 1.19x slower                                                           |
| gc_traversal             | 3.45 ms                                                      | 4.37 ms: 1.27x slower                                                           |
| dask                     | 463 ms                                                       | 593 ms: 1.28x slower                                                            |
| coverage                 | 64.0 ms                                                      | 95.1 ms: 1.49x slower                                                           |
| xml_etree_parse          | 162 ms                                                       | 543 ms: 3.36x slower                                                            |
| xml_etree_iterparse      | 110 ms                                                       | 515 ms: 4.67x slower                                                            |
| Geometric mean           | (ref)                                                        | 1.23x faster                                                                    |

Benchmark hidden because not significant (1): xml_etree_generate
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x
