# Results vs. 3.13.0

- fork: faster-cpython
- ref: bound_method_instrum
- machine: linux-x86_64
- commit hash: 5787d3e
- commit date: 2024-07-23
- overall geometric mean: 1.02x faster
- HPT reliability: 96.36%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-pythonperf2-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 287 ms: 1.01x faster                                                                  |
| docutils       | 2.81 sec                                                     | 2.97 sec: 1.06x slower                                                                |
| html5lib       | 71.9 ms                                                      | 74.1 ms: 1.03x slower                                                                 |
| tornado_http   | 120 ms                                                       | 117 ms: 1.02x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-pythonperf2-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 386 ms: 1.19x faster                                                                  |
| async_tree_memoization     | 452 ms                                                       | 405 ms: 1.12x faster                                                                  |
| async_tree_none            | 372 ms                                                       | 335 ms: 1.11x faster                                                                  |
| async_tree_none_tg         | 340 ms                                                       | 306 ms: 1.11x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 542 ms: 1.06x faster                                                                  |
| async_tree_io_tg           | 819 ms                                                       | 775 ms: 1.06x faster                                                                  |
| async_tree_io              | 847 ms                                                       | 817 ms: 1.04x faster                                                                  |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 580 ms: 1.03x faster                                                                  |
| asyncio_tcp                | 380 ms                                                       | 374 ms: 1.01x faster                                                                  |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x faster                                                                |
| coroutines                 | 21.6 ms                                                      | 21.9 ms: 1.01x slower                                                                 |
| asyncio_websockets         | 382 ms                                                       | 392 ms: 1.02x slower                                                                  |
| async_generators           | 359 ms                                                       | 368 ms: 1.02x slower                                                                  |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-pythonperf2-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 85.1 ms: 1.03x faster                                                                 |
| float          | 81.9 ms                                                      | 80.6 ms: 1.02x faster                                                                 |
| pidigits       | 253 ms                                                       | 253 ms: 1.00x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-pythonperf2-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                      | 25.5 ms: 1.03x faster                                                                 |
| regex_compile  | 144 ms                                                       | 141 ms: 1.02x faster                                                                  |
| regex_dna      | 244 ms                                                       | 245 ms: 1.01x slower                                                                  |
| regex_effbot   | 3.37 ms                                                      | 3.40 ms: 1.01x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-pythonperf2-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| xml_etree_process    | 60.9 ms                                                      | 59.7 ms: 1.02x faster                                                                 |
| json_dumps           | 11.0 ms                                                      | 10.8 ms: 1.02x faster                                                                 |
| unpickle_pure_python | 214 us                                                       | 216 us: 1.01x slower                                                                  |
| tomli_loads          | 2.41 sec                                                     | 2.45 sec: 1.02x slower                                                                |
| json_loads           | 24.0 us                                                      | 24.9 us: 1.04x slower                                                                 |
| xml_etree_iterparse  | 100 ms                                                       | 104 ms: 1.04x slower                                                                  |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                          |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_generate, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-pythonperf2-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                                 |
| python_startup_no_site | 8.94 ms                                                      | 9.06 ms: 1.01x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-pythonperf2-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| genshi_text     | 26.6 ms                                                      | 25.0 ms: 1.07x faster                                                                 |
| genshi_xml      | 57.3 ms                                                      | 54.0 ms: 1.06x faster                                                                 |
| django_template | 38.9 ms                                                      | 40.2 ms: 1.03x slower                                                                 |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                                          |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-pythonperf2-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 289 us: 1.38x faster                                                                  |
| deepcopy_memo              | 39.5 us                                                      | 30.7 us: 1.29x faster                                                                 |
| deepcopy_reduce            | 3.54 us                                                      | 2.90 us: 1.22x faster                                                                 |
| async_tree_memoization_tg  | 461 ms                                                       | 386 ms: 1.19x faster                                                                  |
| generators                 | 33.5 ms                                                      | 29.0 ms: 1.16x faster                                                                 |
| async_tree_memoization     | 452 ms                                                       | 405 ms: 1.12x faster                                                                  |
| async_tree_none            | 372 ms                                                       | 335 ms: 1.11x faster                                                                  |
| async_tree_none_tg         | 340 ms                                                       | 306 ms: 1.11x faster                                                                  |
| pathlib                    | 17.4 ms                                                      | 15.9 ms: 1.09x faster                                                                 |
| telco                      | 8.58 ms                                                      | 7.89 ms: 1.09x faster                                                                 |
| genshi_text                | 26.6 ms                                                      | 25.0 ms: 1.07x faster                                                                 |
| genshi_xml                 | 57.3 ms                                                      | 54.0 ms: 1.06x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 542 ms: 1.06x faster                                                                  |
| scimark_fft                | 314 ms                                                       | 297 ms: 1.06x faster                                                                  |
| async_tree_io_tg           | 819 ms                                                       | 775 ms: 1.06x faster                                                                  |
| raytrace                   | 289 ms                                                       | 275 ms: 1.05x faster                                                                  |
| scimark_sor                | 126 ms                                                       | 120 ms: 1.05x faster                                                                  |
| async_tree_io              | 847 ms                                                       | 817 ms: 1.04x faster                                                                  |
| pycparser                  | 1.26 sec                                                     | 1.21 sec: 1.04x faster                                                                |
| nbody                      | 88.0 ms                                                      | 85.1 ms: 1.03x faster                                                                 |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 580 ms: 1.03x faster                                                                  |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.15 ms: 1.03x faster                                                                 |
| bpe_tokeniser              | 5.10 sec                                                     | 4.94 sec: 1.03x faster                                                                |
| logging_format             | 7.07 us                                                      | 6.86 us: 1.03x faster                                                                 |
| bench_thread_pool          | 901 us                                                       | 874 us: 1.03x faster                                                                  |
| logging_simple             | 6.40 us                                                      | 6.23 us: 1.03x faster                                                                 |
| regex_v8                   | 26.2 ms                                                      | 25.5 ms: 1.03x faster                                                                 |
| regex_compile              | 144 ms                                                       | 141 ms: 1.02x faster                                                                  |
| spectral_norm              | 97.4 ms                                                      | 95.2 ms: 1.02x faster                                                                 |
| tornado_http               | 120 ms                                                       | 117 ms: 1.02x faster                                                                  |
| crypto_pyaes               | 72.8 ms                                                      | 71.3 ms: 1.02x faster                                                                 |
| xml_etree_process          | 60.9 ms                                                      | 59.7 ms: 1.02x faster                                                                 |
| sqlglot_optimize           | 59.7 ms                                                      | 58.6 ms: 1.02x faster                                                                 |
| meteor_contest             | 128 ms                                                       | 126 ms: 1.02x faster                                                                  |
| json_dumps                 | 11.0 ms                                                      | 10.8 ms: 1.02x faster                                                                 |
| float                      | 81.9 ms                                                      | 80.6 ms: 1.02x faster                                                                 |
| asyncio_tcp                | 380 ms                                                       | 374 ms: 1.01x faster                                                                  |
| pyflate                    | 492 ms                                                       | 485 ms: 1.01x faster                                                                  |
| 2to3                       | 291 ms                                                       | 287 ms: 1.01x faster                                                                  |
| nqueens                    | 88.2 ms                                                      | 87.2 ms: 1.01x faster                                                                 |
| richards                   | 52.7 ms                                                      | 52.1 ms: 1.01x faster                                                                 |
| typing_runtime_protocols   | 174 us                                                       | 173 us: 1.01x faster                                                                  |
| sympy_str                  | 296 ms                                                       | 294 ms: 1.01x faster                                                                  |
| sympy_integrate            | 23.3 ms                                                      | 23.2 ms: 1.01x faster                                                                 |
| richards_super             | 59.8 ms                                                      | 59.5 ms: 1.01x faster                                                                 |
| sympy_expand               | 505 ms                                                       | 503 ms: 1.00x faster                                                                  |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x faster                                                                |
| pidigits                   | 253 ms                                                       | 253 ms: 1.00x slower                                                                  |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                                 |
| deltablue                  | 3.41 ms                                                      | 3.43 ms: 1.00x slower                                                                 |
| regex_dna                  | 244 ms                                                       | 245 ms: 1.01x slower                                                                  |
| comprehensions             | 17.3 us                                                      | 17.4 us: 1.01x slower                                                                 |
| pprint_safe_repr           | 812 ms                                                       | 818 ms: 1.01x slower                                                                  |
| regex_effbot               | 3.37 ms                                                      | 3.40 ms: 1.01x slower                                                                 |
| unpickle_pure_python       | 214 us                                                       | 216 us: 1.01x slower                                                                  |
| sqlglot_parse              | 1.38 ms                                                      | 1.39 ms: 1.01x slower                                                                 |
| mdp                        | 2.52 sec                                                     | 2.55 sec: 1.01x slower                                                                |
| dulwich_log                | 65.5 ms                                                      | 66.2 ms: 1.01x slower                                                                 |
| python_startup_no_site     | 8.94 ms                                                      | 9.06 ms: 1.01x slower                                                                 |
| coroutines                 | 21.6 ms                                                      | 21.9 ms: 1.01x slower                                                                 |
| dask                       | 379 ms                                                       | 384 ms: 1.01x slower                                                                  |
| go                         | 160 ms                                                       | 163 ms: 1.02x slower                                                                  |
| tomli_loads                | 2.41 sec                                                     | 2.45 sec: 1.02x slower                                                                |
| pprint_pformat             | 1.65 sec                                                     | 1.68 sec: 1.02x slower                                                                |
| chaos                      | 61.7 ms                                                      | 62.9 ms: 1.02x slower                                                                 |
| fannkuch                   | 365 ms                                                       | 373 ms: 1.02x slower                                                                  |
| asyncio_websockets         | 382 ms                                                       | 392 ms: 1.02x slower                                                                  |
| async_generators           | 359 ms                                                       | 368 ms: 1.02x slower                                                                  |
| html5lib                   | 71.9 ms                                                      | 74.1 ms: 1.03x slower                                                                 |
| django_template            | 38.9 ms                                                      | 40.2 ms: 1.03x slower                                                                 |
| coverage                   | 81.1 ms                                                      | 84.2 ms: 1.04x slower                                                                 |
| json_loads                 | 24.0 us                                                      | 24.9 us: 1.04x slower                                                                 |
| json                       | 5.22 ms                                                      | 5.43 ms: 1.04x slower                                                                 |
| xml_etree_iterparse        | 100 ms                                                       | 104 ms: 1.04x slower                                                                  |
| scimark_monte_carlo        | 64.9 ms                                                      | 68.3 ms: 1.05x slower                                                                 |
| docutils                   | 2.81 sec                                                     | 2.97 sec: 1.06x slower                                                                |
| gc_traversal               | 4.11 ms                                                      | 4.49 ms: 1.09x slower                                                                 |
| create_gc_cycles           | 1.76 ms                                                      | 2.00 ms: 1.14x slower                                                                 |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                          |

Benchmark hidden because not significant (13): bench_mp_pool, xml_etree_parse, sqlglot_transpile, sqlglot_normalize, sympy_sum, xml_etree_generate, scimark_lu, thrift, hexiom, pickle_pure_python, logging_silent, pylint, mako
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 96.36% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x