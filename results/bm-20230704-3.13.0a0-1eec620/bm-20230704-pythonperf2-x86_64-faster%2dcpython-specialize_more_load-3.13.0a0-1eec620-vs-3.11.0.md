
# Results vs. 3.11.0

- fork: faster-cpython
- ref: specialize_more_load
- machine: linux-x86_64
- commit hash: 1eec620
- commit date: 2023-07-04
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230704-pythonperf2-x86_64-faster%2dcpython-specialize_more_load-3.13.0a0-1eec620 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| docutils       | 2.86 sec                                                     | 2.93 sec: 1.02x slower                                                                |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230704-pythonperf2-x86_64-faster%2dcpython-specialize_more_load-3.13.0a0-1eec620 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| pidigits       | 251 ms                                                       | 260 ms: 1.03x slower                                                                  |
| float          | 74.2 ms                                                      | 80.3 ms: 1.08x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230704-pythonperf2-x86_64-faster%2dcpython-specialize_more_load-3.13.0a0-1eec620 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 149 ms: 1.06x faster                                                                  |
| regex_v8       | 23.9 ms                                                      | 24.9 ms: 1.04x slower                                                                 |
| regex_effbot   | 3.50 ms                                                      | 3.65 ms: 1.04x slower                                                                 |
| regex_dna      | 227 ms                                                       | 246 ms: 1.08x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230704-pythonperf2-x86_64-faster%2dcpython-specialize_more_load-3.13.0a0-1eec620 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.0 ms: 1.33x faster                                                                 |
| json_loads           | 28.7 us                                                      | 24.7 us: 1.16x faster                                                                 |
| unpickle_pure_python | 241 us                                                       | 220 us: 1.10x faster                                                                  |
| xml_etree_parse      | 158 ms                                                       | 146 ms: 1.08x faster                                                                  |
| pickle_pure_python   | 319 us                                                       | 314 us: 1.02x faster                                                                  |
| xml_etree_iterparse  | 104 ms                                                       | 106 ms: 1.02x slower                                                                  |
| unpickle_list        | 4.53 us                                                      | 4.65 us: 1.02x slower                                                                 |
| tomli_loads          | 2.26 sec                                                     | 2.34 sec: 1.03x slower                                                                |
| xml_etree_process    | 56.5 ms                                                      | 58.4 ms: 1.03x slower                                                                 |
| pickle_dict          | 30.8 us                                                      | 31.9 us: 1.04x slower                                                                 |
| pickle               | 9.64 us                                                      | 10.2 us: 1.06x slower                                                                 |
| xml_etree_generate   | 80.5 ms                                                      | 85.8 ms: 1.07x slower                                                                 |
| unpickle             | 13.4 us                                                      | 14.6 us: 1.09x slower                                                                 |
| pickle_list          | 3.83 us                                                      | 4.36 us: 1.14x slower                                                                 |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230704-pythonperf2-x86_64-faster%2dcpython-specialize_more_load-3.13.0a0-1eec620 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.3 ms: 1.05x slower                                                                 |
| python_startup_no_site | 7.76 ms                                                      | 8.37 ms: 1.08x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230704-pythonperf2-x86_64-faster%2dcpython-specialize_more_load-3.13.0a0-1eec620 |
|-----------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 10.1 ms: 1.09x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230704-pythonperf2-x86_64-faster%2dcpython-specialize_more_load-3.13.0a0-1eec620 |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 151 us: 3.47x faster                                                                  |
| asyncio_tcp              | 753 ms                                                       | 383 ms: 1.96x faster                                                                  |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.57 sec: 1.96x faster                                                                |
| generators               | 56.0 ms                                                      | 37.6 ms: 1.49x faster                                                                 |
| json_dumps               | 13.4 ms                                                      | 10.0 ms: 1.33x faster                                                                 |
| chaos                    | 80.9 ms                                                      | 61.7 ms: 1.31x faster                                                                 |
| mypy2                    | 451 ms                                                       | 371 ms: 1.22x faster                                                                  |
| coroutines               | 27.6 ms                                                      | 23.2 ms: 1.19x faster                                                                 |
| json_loads               | 28.7 us                                                      | 24.7 us: 1.16x faster                                                                 |
| scimark_lu               | 115 ms                                                       | 98.8 ms: 1.16x faster                                                                 |
| raytrace                 | 317 ms                                                       | 275 ms: 1.15x faster                                                                  |
| crypto_pyaes             | 83.4 ms                                                      | 73.6 ms: 1.13x faster                                                                 |
| deltablue                | 4.00 ms                                                      | 3.57 ms: 1.12x faster                                                                 |
| async_tree_memoization   | 630 ms                                                       | 562 ms: 1.12x faster                                                                  |
| comprehensions           | 24.6 us                                                      | 22.0 us: 1.12x faster                                                                 |
| async_tree_none          | 519 ms                                                       | 466 ms: 1.11x faster                                                                  |
| nqueens                  | 103 ms                                                       | 92.9 ms: 1.11x faster                                                                 |
| hexiom                   | 7.13 ms                                                      | 6.49 ms: 1.10x faster                                                                 |
| unpickle_pure_python     | 241 us                                                       | 220 us: 1.10x faster                                                                  |
| json                     | 5.65 ms                                                      | 5.17 ms: 1.09x faster                                                                 |
| async_tree_io            | 1.17 sec                                                     | 1.08 sec: 1.09x faster                                                                |
| mako                     | 11.0 ms                                                      | 10.1 ms: 1.09x faster                                                                 |
| xml_etree_parse          | 158 ms                                                       | 146 ms: 1.08x faster                                                                  |
| fannkuch                 | 429 ms                                                       | 397 ms: 1.08x faster                                                                  |
| mdp                      | 2.75 sec                                                     | 2.55 sec: 1.08x faster                                                                |
| sqlglot_normalize        | 126 ms                                                       | 118 ms: 1.07x faster                                                                  |
| deepcopy                 | 399 us                                                       | 373 us: 1.07x faster                                                                  |
| sqlglot_parse            | 1.53 ms                                                      | 1.43 ms: 1.07x faster                                                                 |
| logging_format           | 8.11 us                                                      | 7.59 us: 1.07x faster                                                                 |
| regex_compile            | 158 ms                                                       | 149 ms: 1.06x faster                                                                  |
| bench_thread_pool        | 1.01 ms                                                      | 956 us: 1.06x faster                                                                  |
| deepcopy_memo            | 38.8 us                                                      | 36.8 us: 1.05x faster                                                                 |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 713 ms: 1.05x faster                                                                  |
| sqlglot_transpile        | 1.92 ms                                                      | 1.85 ms: 1.04x faster                                                                 |
| logging_simple           | 7.19 us                                                      | 6.94 us: 1.04x faster                                                                 |
| logging_silent           | 101 ns                                                       | 97.5 ns: 1.03x faster                                                                 |
| deepcopy_reduce          | 3.51 us                                                      | 3.42 us: 1.03x faster                                                                 |
| richards_super           | 61.0 ms                                                      | 59.7 ms: 1.02x faster                                                                 |
| gc_traversal             | 3.85 ms                                                      | 3.77 ms: 1.02x faster                                                                 |
| pickle_pure_python       | 319 us                                                       | 314 us: 1.02x faster                                                                  |
| dulwich_log              | 68.4 ms                                                      | 67.6 ms: 1.01x faster                                                                 |
| sqlglot_optimize         | 59.8 ms                                                      | 59.2 ms: 1.01x faster                                                                 |
| meteor_contest           | 131 ms                                                       | 131 ms: 1.00x slower                                                                  |
| spectral_norm            | 93.3 ms                                                      | 94.5 ms: 1.01x slower                                                                 |
| xml_etree_iterparse      | 104 ms                                                       | 106 ms: 1.02x slower                                                                  |
| pathlib                  | 19.1 ms                                                      | 19.4 ms: 1.02x slower                                                                 |
| docutils                 | 2.86 sec                                                     | 2.93 sec: 1.02x slower                                                                |
| unpickle_list            | 4.53 us                                                      | 4.65 us: 1.02x slower                                                                 |
| unpack_sequence          | 45.6 ns                                                      | 46.9 ns: 1.03x slower                                                                 |
| tomli_loads              | 2.26 sec                                                     | 2.34 sec: 1.03x slower                                                                |
| create_gc_cycles         | 1.61 ms                                                      | 1.66 ms: 1.03x slower                                                                 |
| pidigits                 | 251 ms                                                       | 260 ms: 1.03x slower                                                                  |
| xml_etree_process        | 56.5 ms                                                      | 58.4 ms: 1.03x slower                                                                 |
| pickle_dict              | 30.8 us                                                      | 31.9 us: 1.04x slower                                                                 |
| regex_v8                 | 23.9 ms                                                      | 24.9 ms: 1.04x slower                                                                 |
| regex_effbot             | 3.50 ms                                                      | 3.65 ms: 1.04x slower                                                                 |
| scimark_monte_carlo      | 68.2 ms                                                      | 71.5 ms: 1.05x slower                                                                 |
| go                       | 164 ms                                                       | 172 ms: 1.05x slower                                                                  |
| pprint_pformat           | 1.63 sec                                                     | 1.71 sec: 1.05x slower                                                                |
| python_startup           | 10.8 ms                                                      | 11.3 ms: 1.05x slower                                                                 |
| pickle                   | 9.64 us                                                      | 10.2 us: 1.06x slower                                                                 |
| xml_etree_generate       | 80.5 ms                                                      | 85.8 ms: 1.07x slower                                                                 |
| pprint_safe_repr         | 784 ms                                                       | 840 ms: 1.07x slower                                                                  |
| python_startup_no_site   | 7.76 ms                                                      | 8.37 ms: 1.08x slower                                                                 |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 4.37 ms: 1.08x slower                                                                 |
| float                    | 74.2 ms                                                      | 80.3 ms: 1.08x slower                                                                 |
| regex_dna                | 227 ms                                                       | 246 ms: 1.08x slower                                                                  |
| unpickle                 | 13.4 us                                                      | 14.6 us: 1.09x slower                                                                 |
| sqlite_synth             | 2.50 us                                                      | 2.72 us: 1.09x slower                                                                 |
| coverage                 | 84.8 ms                                                      | 92.8 ms: 1.09x slower                                                                 |
| telco                    | 6.86 ms                                                      | 7.57 ms: 1.10x slower                                                                 |
| richards                 | 48.3 ms                                                      | 53.5 ms: 1.11x slower                                                                 |
| scimark_fft              | 285 ms                                                       | 317 ms: 1.11x slower                                                                  |
| pickle_list              | 3.83 us                                                      | 4.36 us: 1.14x slower                                                                 |
| pyflate                  | 449 ms                                                       | 513 ms: 1.14x slower                                                                  |
| async_generators         | 316 ms                                                       | 392 ms: 1.24x slower                                                                  |
| bench_mp_pool            | 4.62 ms                                                      | 5.86 ms: 1.27x slower                                                                 |
| scimark_sor              | 111 ms                                                       | 145 ms: 1.31x slower                                                                  |
| dask                     | 410 ms                                                       | 588 ms: 1.43x slower                                                                  |
| Geometric mean           | (ref)                                                        | 1.04x faster                                                                          |

Benchmark hidden because not significant (3): nbody, tornado_http, pycparser
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
