
# Results vs. 3.11.0

- fork: faster-cpython
- ref: specialize_more_load
- machine: linux-x86_64
- commit hash: 16a2718
- commit date: 2023-07-05
- overall geometric mean: 1.04x faster
- HPT reliability: 89.19%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230705-pythonperf2-x86_64-faster%2dcpython-specialize_more_load-3.13.0a0-16a2718 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| docutils       | 2.86 sec                                                     | 2.92 sec: 1.02x slower                                                                |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230705-pythonperf2-x86_64-faster%2dcpython-specialize_more_load-3.13.0a0-16a2718 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 89.1 ms: 1.02x faster                                                                 |
| pidigits       | 251 ms                                                       | 261 ms: 1.04x slower                                                                  |
| float          | 74.2 ms                                                      | 81.3 ms: 1.10x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230705-pythonperf2-x86_64-faster%2dcpython-specialize_more_load-3.13.0a0-16a2718 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 151 ms: 1.04x faster                                                                  |
| regex_v8       | 23.9 ms                                                      | 24.2 ms: 1.01x slower                                                                 |
| regex_effbot   | 3.50 ms                                                      | 3.58 ms: 1.02x slower                                                                 |
| regex_dna      | 227 ms                                                       | 241 ms: 1.06x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230705-pythonperf2-x86_64-faster%2dcpython-specialize_more_load-3.13.0a0-16a2718 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.1 ms: 1.33x faster                                                                 |
| json_loads           | 28.7 us                                                      | 24.9 us: 1.15x faster                                                                 |
| unpickle_pure_python | 241 us                                                       | 219 us: 1.10x faster                                                                  |
| xml_etree_parse      | 158 ms                                                       | 145 ms: 1.08x faster                                                                  |
| pickle_pure_python   | 319 us                                                       | 316 us: 1.01x faster                                                                  |
| unpickle_list        | 4.53 us                                                      | 4.61 us: 1.02x slower                                                                 |
| pickle_dict          | 30.8 us                                                      | 31.4 us: 1.02x slower                                                                 |
| xml_etree_process    | 56.5 ms                                                      | 58.8 ms: 1.04x slower                                                                 |
| xml_etree_generate   | 80.5 ms                                                      | 85.4 ms: 1.06x slower                                                                 |
| tomli_loads          | 2.26 sec                                                     | 2.40 sec: 1.06x slower                                                                |
| pickle               | 9.64 us                                                      | 10.2 us: 1.06x slower                                                                 |
| unpickle             | 13.4 us                                                      | 14.6 us: 1.09x slower                                                                 |
| pickle_list          | 3.83 us                                                      | 4.34 us: 1.13x slower                                                                 |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                          |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230705-pythonperf2-x86_64-faster%2dcpython-specialize_more_load-3.13.0a0-16a2718 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.3 ms: 1.05x slower                                                                 |
| python_startup_no_site | 7.76 ms                                                      | 8.39 ms: 1.08x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230705-pythonperf2-x86_64-faster%2dcpython-specialize_more_load-3.13.0a0-16a2718 |
|-----------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 10.1 ms: 1.09x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230705-pythonperf2-x86_64-faster%2dcpython-specialize_more_load-3.13.0a0-16a2718 |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 154 us: 3.39x faster                                                                  |
| asyncio_tcp              | 753 ms                                                       | 382 ms: 1.97x faster                                                                  |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.57 sec: 1.96x faster                                                                |
| generators               | 56.0 ms                                                      | 37.1 ms: 1.51x faster                                                                 |
| json_dumps               | 13.4 ms                                                      | 10.1 ms: 1.33x faster                                                                 |
| chaos                    | 80.9 ms                                                      | 61.4 ms: 1.32x faster                                                                 |
| mypy2                    | 451 ms                                                       | 371 ms: 1.22x faster                                                                  |
| coroutines               | 27.6 ms                                                      | 23.2 ms: 1.19x faster                                                                 |
| scimark_lu               | 115 ms                                                       | 98.8 ms: 1.16x faster                                                                 |
| json_loads               | 28.7 us                                                      | 24.9 us: 1.15x faster                                                                 |
| raytrace                 | 317 ms                                                       | 275 ms: 1.15x faster                                                                  |
| crypto_pyaes             | 83.4 ms                                                      | 74.1 ms: 1.13x faster                                                                 |
| comprehensions           | 24.6 us                                                      | 22.0 us: 1.12x faster                                                                 |
| async_tree_memoization   | 630 ms                                                       | 565 ms: 1.12x faster                                                                  |
| async_tree_none          | 519 ms                                                       | 469 ms: 1.11x faster                                                                  |
| deltablue                | 4.00 ms                                                      | 3.61 ms: 1.11x faster                                                                 |
| nqueens                  | 103 ms                                                       | 93.2 ms: 1.10x faster                                                                 |
| hexiom                   | 7.13 ms                                                      | 6.48 ms: 1.10x faster                                                                 |
| unpickle_pure_python     | 241 us                                                       | 219 us: 1.10x faster                                                                  |
| logging_format           | 8.11 us                                                      | 7.41 us: 1.09x faster                                                                 |
| mako                     | 11.0 ms                                                      | 10.1 ms: 1.09x faster                                                                 |
| json                     | 5.65 ms                                                      | 5.18 ms: 1.09x faster                                                                 |
| gc_traversal             | 3.85 ms                                                      | 3.53 ms: 1.09x faster                                                                 |
| xml_etree_parse          | 158 ms                                                       | 145 ms: 1.08x faster                                                                  |
| async_tree_io            | 1.17 sec                                                     | 1.08 sec: 1.08x faster                                                                |
| mdp                      | 2.75 sec                                                     | 2.57 sec: 1.07x faster                                                                |
| fannkuch                 | 429 ms                                                       | 401 ms: 1.07x faster                                                                  |
| sqlglot_normalize        | 126 ms                                                       | 118 ms: 1.06x faster                                                                  |
| sqlglot_parse            | 1.53 ms                                                      | 1.45 ms: 1.06x faster                                                                 |
| logging_simple           | 7.19 us                                                      | 6.83 us: 1.05x faster                                                                 |
| deepcopy                 | 399 us                                                       | 381 us: 1.05x faster                                                                  |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 716 ms: 1.05x faster                                                                  |
| logging_silent           | 101 ns                                                       | 96.5 ns: 1.04x faster                                                                 |
| regex_compile            | 158 ms                                                       | 151 ms: 1.04x faster                                                                  |
| richards_super           | 61.0 ms                                                      | 58.9 ms: 1.04x faster                                                                 |
| sqlglot_transpile        | 1.92 ms                                                      | 1.85 ms: 1.04x faster                                                                 |
| bench_thread_pool        | 1.01 ms                                                      | 979 us: 1.03x faster                                                                  |
| deepcopy_reduce          | 3.51 us                                                      | 3.45 us: 1.02x faster                                                                 |
| deepcopy_memo            | 38.8 us                                                      | 38.1 us: 1.02x faster                                                                 |
| nbody                    | 90.7 ms                                                      | 89.1 ms: 1.02x faster                                                                 |
| dulwich_log              | 68.4 ms                                                      | 67.7 ms: 1.01x faster                                                                 |
| sqlglot_optimize         | 59.8 ms                                                      | 59.2 ms: 1.01x faster                                                                 |
| pickle_pure_python       | 319 us                                                       | 316 us: 1.01x faster                                                                  |
| meteor_contest           | 131 ms                                                       | 130 ms: 1.01x faster                                                                  |
| scimark_monte_carlo      | 68.2 ms                                                      | 67.9 ms: 1.00x faster                                                                 |
| regex_v8                 | 23.9 ms                                                      | 24.2 ms: 1.01x slower                                                                 |
| unpickle_list            | 4.53 us                                                      | 4.61 us: 1.02x slower                                                                 |
| docutils                 | 2.86 sec                                                     | 2.92 sec: 1.02x slower                                                                |
| pickle_dict              | 30.8 us                                                      | 31.4 us: 1.02x slower                                                                 |
| regex_effbot             | 3.50 ms                                                      | 3.58 ms: 1.02x slower                                                                 |
| unpack_sequence          | 45.6 ns                                                      | 46.8 ns: 1.03x slower                                                                 |
| pathlib                  | 19.1 ms                                                      | 19.6 ms: 1.03x slower                                                                 |
| spectral_norm            | 93.3 ms                                                      | 96.1 ms: 1.03x slower                                                                 |
| pidigits                 | 251 ms                                                       | 261 ms: 1.04x slower                                                                  |
| xml_etree_process        | 56.5 ms                                                      | 58.8 ms: 1.04x slower                                                                 |
| create_gc_cycles         | 1.61 ms                                                      | 1.68 ms: 1.04x slower                                                                 |
| pprint_pformat           | 1.63 sec                                                     | 1.70 sec: 1.04x slower                                                                |
| coverage                 | 84.8 ms                                                      | 89.2 ms: 1.05x slower                                                                 |
| python_startup           | 10.8 ms                                                      | 11.3 ms: 1.05x slower                                                                 |
| regex_dna                | 227 ms                                                       | 241 ms: 1.06x slower                                                                  |
| go                       | 164 ms                                                       | 174 ms: 1.06x slower                                                                  |
| xml_etree_generate       | 80.5 ms                                                      | 85.4 ms: 1.06x slower                                                                 |
| tomli_loads              | 2.26 sec                                                     | 2.40 sec: 1.06x slower                                                                |
| pickle                   | 9.64 us                                                      | 10.2 us: 1.06x slower                                                                 |
| pprint_safe_repr         | 784 ms                                                       | 841 ms: 1.07x slower                                                                  |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 4.37 ms: 1.08x slower                                                                 |
| python_startup_no_site   | 7.76 ms                                                      | 8.39 ms: 1.08x slower                                                                 |
| unpickle                 | 13.4 us                                                      | 14.6 us: 1.09x slower                                                                 |
| sqlite_synth             | 2.50 us                                                      | 2.73 us: 1.09x slower                                                                 |
| float                    | 74.2 ms                                                      | 81.3 ms: 1.10x slower                                                                 |
| richards                 | 48.3 ms                                                      | 53.0 ms: 1.10x slower                                                                 |
| scimark_fft              | 285 ms                                                       | 315 ms: 1.11x slower                                                                  |
| pickle_list              | 3.83 us                                                      | 4.34 us: 1.13x slower                                                                 |
| pyflate                  | 449 ms                                                       | 514 ms: 1.15x slower                                                                  |
| telco                    | 6.86 ms                                                      | 7.96 ms: 1.16x slower                                                                 |
| async_generators         | 316 ms                                                       | 391 ms: 1.24x slower                                                                  |
| bench_mp_pool            | 4.62 ms                                                      | 5.93 ms: 1.28x slower                                                                 |
| scimark_sor              | 111 ms                                                       | 147 ms: 1.32x slower                                                                  |
| dask                     | 410 ms                                                       | 590 ms: 1.44x slower                                                                  |
| Geometric mean           | (ref)                                                        | 1.04x faster                                                                          |

Benchmark hidden because not significant (3): pycparser, tornado_http, xml_etree_iterparse
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 89.19% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
