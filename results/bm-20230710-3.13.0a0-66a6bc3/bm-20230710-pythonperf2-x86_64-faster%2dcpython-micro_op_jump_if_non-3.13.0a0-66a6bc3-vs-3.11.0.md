
# Results vs. 3.11.0

- fork: faster-cpython
- ref: micro_op_jump_if_non
- machine: linux-x86_64
- commit hash: 66a6bc3
- commit date: 2023-07-10
- overall geometric mean: 1.04x faster
- HPT reliability: 72.53%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230710-pythonperf2-x86_64-faster%2dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| docutils       | 2.86 sec                                                     | 2.93 sec: 1.02x slower                                                                |
| tornado_http   | 122 ms                                                       | 124 ms: 1.02x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230710-pythonperf2-x86_64-faster%2dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 92.7 ms: 1.02x slower                                                                 |
| pidigits       | 251 ms                                                       | 261 ms: 1.04x slower                                                                  |
| float          | 74.2 ms                                                      | 82.2 ms: 1.11x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230710-pythonperf2-x86_64-faster%2dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 152 ms: 1.04x faster                                                                  |
| regex_v8       | 23.9 ms                                                      | 23.8 ms: 1.00x faster                                                                 |
| regex_effbot   | 3.50 ms                                                      | 3.56 ms: 1.02x slower                                                                 |
| regex_dna      | 227 ms                                                       | 242 ms: 1.06x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230710-pythonperf2-x86_64-faster%2dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.3 ms: 1.30x faster                                                                 |
| json_loads           | 28.7 us                                                      | 25.6 us: 1.12x faster                                                                 |
| unpickle_pure_python | 241 us                                                       | 224 us: 1.07x faster                                                                  |
| xml_etree_parse      | 158 ms                                                       | 150 ms: 1.05x faster                                                                  |
| xml_etree_iterparse  | 104 ms                                                       | 107 ms: 1.03x slower                                                                  |
| tomli_loads          | 2.26 sec                                                     | 2.33 sec: 1.03x slower                                                                |
| unpickle_list        | 4.53 us                                                      | 4.71 us: 1.04x slower                                                                 |
| xml_etree_process    | 56.5 ms                                                      | 59.2 ms: 1.05x slower                                                                 |
| pickle_dict          | 30.8 us                                                      | 32.7 us: 1.06x slower                                                                 |
| unpickle             | 13.4 us                                                      | 14.4 us: 1.07x slower                                                                 |
| pickle               | 9.64 us                                                      | 10.4 us: 1.08x slower                                                                 |
| xml_etree_generate   | 80.5 ms                                                      | 87.1 ms: 1.08x slower                                                                 |
| pickle_list          | 3.83 us                                                      | 4.38 us: 1.15x slower                                                                 |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                          |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230710-pythonperf2-x86_64-faster%2dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.3 ms: 1.05x slower                                                                 |
| python_startup_no_site | 7.76 ms                                                      | 8.38 ms: 1.08x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230710-pythonperf2-x86_64-faster%2dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3 |
|-----------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 10.2 ms: 1.08x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230710-pythonperf2-x86_64-faster%2dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3 |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 155 us: 3.37x faster                                                                  |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.57 sec: 1.96x faster                                                                |
| asyncio_tcp              | 753 ms                                                       | 385 ms: 1.95x faster                                                                  |
| generators               | 56.0 ms                                                      | 35.9 ms: 1.56x faster                                                                 |
| json_dumps               | 13.4 ms                                                      | 10.3 ms: 1.30x faster                                                                 |
| chaos                    | 80.9 ms                                                      | 62.8 ms: 1.29x faster                                                                 |
| mypy2                    | 451 ms                                                       | 372 ms: 1.21x faster                                                                  |
| coroutines               | 27.6 ms                                                      | 22.9 ms: 1.20x faster                                                                 |
| scimark_lu               | 115 ms                                                       | 97.9 ms: 1.17x faster                                                                 |
| json_loads               | 28.7 us                                                      | 25.6 us: 1.12x faster                                                                 |
| async_tree_none          | 519 ms                                                       | 465 ms: 1.12x faster                                                                  |
| async_tree_memoization   | 630 ms                                                       | 564 ms: 1.12x faster                                                                  |
| raytrace                 | 317 ms                                                       | 284 ms: 1.11x faster                                                                  |
| comprehensions           | 24.6 us                                                      | 22.1 us: 1.11x faster                                                                 |
| crypto_pyaes             | 83.4 ms                                                      | 75.8 ms: 1.10x faster                                                                 |
| nqueens                  | 103 ms                                                       | 93.9 ms: 1.10x faster                                                                 |
| json                     | 5.65 ms                                                      | 5.19 ms: 1.09x faster                                                                 |
| async_tree_io            | 1.17 sec                                                     | 1.08 sec: 1.09x faster                                                                |
| sqlglot_normalize        | 126 ms                                                       | 116 ms: 1.09x faster                                                                  |
| hexiom                   | 7.13 ms                                                      | 6.58 ms: 1.08x faster                                                                 |
| gc_traversal             | 3.85 ms                                                      | 3.57 ms: 1.08x faster                                                                 |
| deltablue                | 4.00 ms                                                      | 3.71 ms: 1.08x faster                                                                 |
| mako                     | 11.0 ms                                                      | 10.2 ms: 1.08x faster                                                                 |
| fannkuch                 | 429 ms                                                       | 399 ms: 1.08x faster                                                                  |
| logging_format           | 8.11 us                                                      | 7.55 us: 1.07x faster                                                                 |
| unpickle_pure_python     | 241 us                                                       | 224 us: 1.07x faster                                                                  |
| mdp                      | 2.75 sec                                                     | 2.56 sec: 1.07x faster                                                                |
| bench_thread_pool        | 1.01 ms                                                      | 951 us: 1.06x faster                                                                  |
| xml_etree_parse          | 158 ms                                                       | 150 ms: 1.05x faster                                                                  |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 716 ms: 1.05x faster                                                                  |
| deepcopy                 | 399 us                                                       | 384 us: 1.04x faster                                                                  |
| deepcopy_memo            | 38.8 us                                                      | 37.3 us: 1.04x faster                                                                 |
| regex_compile            | 158 ms                                                       | 152 ms: 1.04x faster                                                                  |
| sqlglot_parse            | 1.53 ms                                                      | 1.48 ms: 1.04x faster                                                                 |
| logging_simple           | 7.19 us                                                      | 6.96 us: 1.03x faster                                                                 |
| logging_silent           | 101 ns                                                       | 98.2 ns: 1.03x faster                                                                 |
| deepcopy_reduce          | 3.51 us                                                      | 3.46 us: 1.02x faster                                                                 |
| sqlglot_optimize         | 59.8 ms                                                      | 58.9 ms: 1.02x faster                                                                 |
| sqlglot_transpile        | 1.92 ms                                                      | 1.89 ms: 1.02x faster                                                                 |
| meteor_contest           | 131 ms                                                       | 129 ms: 1.01x faster                                                                  |
| regex_v8                 | 23.9 ms                                                      | 23.8 ms: 1.00x faster                                                                 |
| regex_effbot             | 3.50 ms                                                      | 3.56 ms: 1.02x slower                                                                 |
| spectral_norm            | 93.3 ms                                                      | 95.3 ms: 1.02x slower                                                                 |
| tornado_http             | 122 ms                                                       | 124 ms: 1.02x slower                                                                  |
| nbody                    | 90.7 ms                                                      | 92.7 ms: 1.02x slower                                                                 |
| docutils                 | 2.86 sec                                                     | 2.93 sec: 1.02x slower                                                                |
| coverage                 | 84.8 ms                                                      | 86.9 ms: 1.03x slower                                                                 |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 4.16 ms: 1.03x slower                                                                 |
| xml_etree_iterparse      | 104 ms                                                       | 107 ms: 1.03x slower                                                                  |
| pathlib                  | 19.1 ms                                                      | 19.6 ms: 1.03x slower                                                                 |
| tomli_loads              | 2.26 sec                                                     | 2.33 sec: 1.03x slower                                                                |
| unpickle_list            | 4.53 us                                                      | 4.71 us: 1.04x slower                                                                 |
| pidigits                 | 251 ms                                                       | 261 ms: 1.04x slower                                                                  |
| xml_etree_process        | 56.5 ms                                                      | 59.2 ms: 1.05x slower                                                                 |
| python_startup           | 10.8 ms                                                      | 11.3 ms: 1.05x slower                                                                 |
| pprint_pformat           | 1.63 sec                                                     | 1.72 sec: 1.06x slower                                                                |
| regex_dna                | 227 ms                                                       | 242 ms: 1.06x slower                                                                  |
| pickle_dict              | 30.8 us                                                      | 32.7 us: 1.06x slower                                                                 |
| unpickle                 | 13.4 us                                                      | 14.4 us: 1.07x slower                                                                 |
| scimark_monte_carlo      | 68.2 ms                                                      | 73.1 ms: 1.07x slower                                                                 |
| pprint_safe_repr         | 784 ms                                                       | 846 ms: 1.08x slower                                                                  |
| pickle                   | 9.64 us                                                      | 10.4 us: 1.08x slower                                                                 |
| python_startup_no_site   | 7.76 ms                                                      | 8.38 ms: 1.08x slower                                                                 |
| go                       | 164 ms                                                       | 177 ms: 1.08x slower                                                                  |
| xml_etree_generate       | 80.5 ms                                                      | 87.1 ms: 1.08x slower                                                                 |
| scimark_fft              | 285 ms                                                       | 313 ms: 1.10x slower                                                                  |
| float                    | 74.2 ms                                                      | 82.2 ms: 1.11x slower                                                                 |
| sqlite_synth             | 2.50 us                                                      | 2.77 us: 1.11x slower                                                                 |
| telco                    | 6.86 ms                                                      | 7.76 ms: 1.13x slower                                                                 |
| richards                 | 48.3 ms                                                      | 55.0 ms: 1.14x slower                                                                 |
| pickle_list              | 3.83 us                                                      | 4.38 us: 1.15x slower                                                                 |
| unpack_sequence          | 45.6 ns                                                      | 52.5 ns: 1.15x slower                                                                 |
| pyflate                  | 449 ms                                                       | 518 ms: 1.15x slower                                                                  |
| async_generators         | 316 ms                                                       | 393 ms: 1.24x slower                                                                  |
| scimark_sor              | 111 ms                                                       | 146 ms: 1.32x slower                                                                  |
| dask                     | 410 ms                                                       | 592 ms: 1.44x slower                                                                  |
| Geometric mean           | (ref)                                                        | 1.04x faster                                                                          |

Benchmark hidden because not significant (6): dulwich_log, richards_super, pycparser, pickle_pure_python, create_gc_cycles, bench_mp_pool
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 72.53% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
