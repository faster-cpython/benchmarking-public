# Results vs. 3.13.0

- fork: python
- ref: v3.13.0b4
- machine: linux-x86_64
- commit hash: 567c38b
- commit date: 2024-07-18
- overall geometric mean: 1.00x faster
- HPT reliability: 85.98%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 290 ms: 1.00x faster                                             |
| chameleon      | 7.42 ms                                                      | 7.20 ms: 1.03x faster                                            |
| docutils       | 2.81 sec                                                     | 2.99 sec: 1.06x slower                                           |
| html5lib       | 71.9 ms                                                      | 74.1 ms: 1.03x slower                                            |
| Geometric mean | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|---------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg | 461 ms                                                       | 427 ms: 1.08x faster                                             |
| async_tree_none           | 372 ms                                                       | 367 ms: 1.01x faster                                             |
| asyncio_tcp               | 380 ms                                                       | 375 ms: 1.01x faster                                             |
| asyncio_tcp_ssl           | 1.58 sec                                                     | 1.58 sec: 1.00x faster                                           |
| async_generators          | 359 ms                                                       | 362 ms: 1.01x slower                                             |
| asyncio_websockets        | 382 ms                                                       | 387 ms: 1.01x slower                                             |
| async_tree_none_tg        | 340 ms                                                       | 347 ms: 1.02x slower                                             |
| async_tree_cpu_io_mixed   | 600 ms                                                       | 614 ms: 1.02x slower                                             |
| coroutines                | 21.6 ms                                                      | 22.2 ms: 1.03x slower                                            |
| async_tree_memoization    | 452 ms                                                       | 464 ms: 1.03x slower                                             |
| async_tree_io             | 847 ms                                                       | 875 ms: 1.03x slower                                             |
| async_tree_io_tg          | 819 ms                                                       | 905 ms: 1.11x slower                                             |
| Geometric mean            | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 80.0 ms: 1.02x faster                                            |
| pidigits       | 253 ms                                                       | 253 ms: 1.00x slower                                             |
| Geometric mean | (ref)                                                        | 1.00x faster                                                     |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                      | 25.0 ms: 1.05x faster                                            |
| regex_compile  | 144 ms                                                       | 143 ms: 1.01x faster                                             |
| regex_dna      | 244 ms                                                       | 251 ms: 1.03x slower                                             |
| regex_effbot   | 3.37 ms                                                      | 3.54 ms: 1.05x slower                                            |
| Geometric mean | (ref)                                                        | 1.01x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_pure_python   | 318 us                                                       | 315 us: 1.01x faster                                             |
| unpickle_pure_python | 214 us                                                       | 214 us: 1.00x faster                                             |
| xml_etree_process    | 60.9 ms                                                      | 61.5 ms: 1.01x slower                                            |
| tomli_loads          | 2.41 sec                                                     | 2.44 sec: 1.01x slower                                           |
| xml_etree_generate   | 85.3 ms                                                      | 86.9 ms: 1.02x slower                                            |
| xml_etree_parse      | 145 ms                                                       | 149 ms: 1.03x slower                                             |
| json_loads           | 24.0 us                                                      | 25.0 us: 1.04x slower                                            |
| xml_etree_iterparse  | 100 ms                                                       | 106 ms: 1.06x slower                                             |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                     |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                            |
| python_startup_no_site | 8.94 ms                                                      | 9.02 ms: 1.01x slower                                            |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_text     | 26.6 ms                                                      | 26.2 ms: 1.02x faster                                            |
| genshi_xml      | 57.3 ms                                                      | 56.8 ms: 1.01x faster                                            |
| django_template | 38.9 ms                                                      | 39.1 ms: 1.01x slower                                            |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                     |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|---------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mypy2                     | 1.05 sec                                                     | 768 ms: 1.36x faster                                             |
| raytrace                  | 289 ms                                                       | 263 ms: 1.10x faster                                             |
| async_tree_memoization_tg | 461 ms                                                       | 427 ms: 1.08x faster                                             |
| scimark_sor               | 126 ms                                                       | 116 ms: 1.08x faster                                             |
| deepcopy                  | 397 us                                                       | 377 us: 1.05x faster                                             |
| deepcopy_memo             | 39.5 us                                                      | 37.5 us: 1.05x faster                                            |
| regex_v8                  | 26.2 ms                                                      | 25.0 ms: 1.05x faster                                            |
| scimark_fft               | 314 ms                                                       | 302 ms: 1.04x faster                                             |
| telco                     | 8.58 ms                                                      | 8.29 ms: 1.03x faster                                            |
| chameleon                 | 7.42 ms                                                      | 7.20 ms: 1.03x faster                                            |
| deepcopy_reduce           | 3.54 us                                                      | 3.44 us: 1.03x faster                                            |
| scimark_sparse_mat_mult   | 4.29 ms                                                      | 4.16 ms: 1.03x faster                                            |
| pycparser                 | 1.26 sec                                                     | 1.23 sec: 1.02x faster                                           |
| float                     | 81.9 ms                                                      | 80.0 ms: 1.02x faster                                            |
| pathlib                   | 17.4 ms                                                      | 17.1 ms: 1.02x faster                                            |
| coverage                  | 81.1 ms                                                      | 79.6 ms: 1.02x faster                                            |
| logging_silent            | 97.7 ns                                                      | 95.9 ns: 1.02x faster                                            |
| genshi_text               | 26.6 ms                                                      | 26.2 ms: 1.02x faster                                            |
| scimark_lu                | 97.8 ms                                                      | 96.2 ms: 1.02x faster                                            |
| comprehensions            | 17.3 us                                                      | 17.0 us: 1.02x faster                                            |
| meteor_contest            | 128 ms                                                       | 126 ms: 1.02x faster                                             |
| sqlglot_optimize          | 59.7 ms                                                      | 58.9 ms: 1.01x faster                                            |
| richards_super            | 59.8 ms                                                      | 59.0 ms: 1.01x faster                                            |
| async_tree_none           | 372 ms                                                       | 367 ms: 1.01x faster                                             |
| typing_runtime_protocols  | 174 us                                                       | 172 us: 1.01x faster                                             |
| pickle_pure_python        | 318 us                                                       | 315 us: 1.01x faster                                             |
| chaos                     | 61.7 ms                                                      | 60.9 ms: 1.01x faster                                            |
| asyncio_tcp               | 380 ms                                                       | 375 ms: 1.01x faster                                             |
| genshi_xml                | 57.3 ms                                                      | 56.8 ms: 1.01x faster                                            |
| logging_format            | 7.07 us                                                      | 7.01 us: 1.01x faster                                            |
| sympy_expand              | 505 ms                                                       | 500 ms: 1.01x faster                                             |
| regex_compile             | 144 ms                                                       | 143 ms: 1.01x faster                                             |
| deltablue                 | 3.41 ms                                                      | 3.38 ms: 1.01x faster                                            |
| sympy_sum                 | 154 ms                                                       | 153 ms: 1.01x faster                                             |
| sqlglot_transpile         | 1.78 ms                                                      | 1.77 ms: 1.00x faster                                            |
| unpickle_pure_python      | 214 us                                                       | 214 us: 1.00x faster                                             |
| 2to3                      | 291 ms                                                       | 290 ms: 1.00x faster                                             |
| asyncio_tcp_ssl           | 1.58 sec                                                     | 1.58 sec: 1.00x faster                                           |
| sympy_str                 | 296 ms                                                       | 295 ms: 1.00x faster                                             |
| spectral_norm             | 97.4 ms                                                      | 97.6 ms: 1.00x slower                                            |
| pidigits                  | 253 ms                                                       | 253 ms: 1.00x slower                                             |
| nqueens                   | 88.2 ms                                                      | 88.6 ms: 1.00x slower                                            |
| richards                  | 52.7 ms                                                      | 53.0 ms: 1.00x slower                                            |
| python_startup            | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                            |
| sqlglot_normalize         | 118 ms                                                       | 119 ms: 1.00x slower                                             |
| bpe_tokeniser             | 5.10 sec                                                     | 5.13 sec: 1.01x slower                                           |
| mdp                       | 2.52 sec                                                     | 2.54 sec: 1.01x slower                                           |
| async_generators          | 359 ms                                                       | 362 ms: 1.01x slower                                             |
| django_template           | 38.9 ms                                                      | 39.1 ms: 1.01x slower                                            |
| hexiom                    | 6.33 ms                                                      | 6.38 ms: 1.01x slower                                            |
| python_startup_no_site    | 8.94 ms                                                      | 9.02 ms: 1.01x slower                                            |
| pprint_pformat            | 1.65 sec                                                     | 1.66 sec: 1.01x slower                                           |
| xml_etree_process         | 60.9 ms                                                      | 61.5 ms: 1.01x slower                                            |
| logging_simple            | 6.40 us                                                      | 6.47 us: 1.01x slower                                            |
| dulwich_log               | 65.5 ms                                                      | 66.3 ms: 1.01x slower                                            |
| asyncio_websockets        | 382 ms                                                       | 387 ms: 1.01x slower                                             |
| tomli_loads               | 2.41 sec                                                     | 2.44 sec: 1.01x slower                                           |
| sqlglot_parse             | 1.38 ms                                                      | 1.40 ms: 1.01x slower                                            |
| json                      | 5.22 ms                                                      | 5.31 ms: 1.02x slower                                            |
| go                        | 160 ms                                                       | 163 ms: 1.02x slower                                             |
| scimark_monte_carlo       | 64.9 ms                                                      | 66.1 ms: 1.02x slower                                            |
| xml_etree_generate        | 85.3 ms                                                      | 86.9 ms: 1.02x slower                                            |
| async_tree_none_tg        | 340 ms                                                       | 347 ms: 1.02x slower                                             |
| async_tree_cpu_io_mixed   | 600 ms                                                       | 614 ms: 1.02x slower                                             |
| crypto_pyaes              | 72.8 ms                                                      | 74.6 ms: 1.02x slower                                            |
| coroutines                | 21.6 ms                                                      | 22.2 ms: 1.03x slower                                            |
| xml_etree_parse           | 145 ms                                                       | 149 ms: 1.03x slower                                             |
| async_tree_memoization    | 452 ms                                                       | 464 ms: 1.03x slower                                             |
| regex_dna                 | 244 ms                                                       | 251 ms: 1.03x slower                                             |
| thrift                    | 877 us                                                       | 903 us: 1.03x slower                                             |
| html5lib                  | 71.9 ms                                                      | 74.1 ms: 1.03x slower                                            |
| async_tree_io             | 847 ms                                                       | 875 ms: 1.03x slower                                             |
| dask                      | 379 ms                                                       | 394 ms: 1.04x slower                                             |
| json_loads                | 24.0 us                                                      | 25.0 us: 1.04x slower                                            |
| regex_effbot              | 3.37 ms                                                      | 3.54 ms: 1.05x slower                                            |
| docutils                  | 2.81 sec                                                     | 2.99 sec: 1.06x slower                                           |
| xml_etree_iterparse       | 100 ms                                                       | 106 ms: 1.06x slower                                             |
| async_tree_io_tg          | 819 ms                                                       | 905 ms: 1.11x slower                                             |
| gc_traversal              | 4.11 ms                                                      | 4.60 ms: 1.12x slower                                            |
| create_gc_cycles          | 1.76 ms                                                      | 2.02 ms: 1.15x slower                                            |
| Geometric mean            | (ref)                                                        | 1.00x faster                                                     |

Benchmark hidden because not significant (13): pylint, mako, tornado_http, bench_mp_pool, json_dumps, generators, sympy_integrate, pyflate, bench_thread_pool, fannkuch, pprint_safe_repr, nbody, async_tree_cpu_io_mixed_tg
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 85.98% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x