# Results vs. 3.13.0

- fork: faster-cpython
- ref: bound_method_instrum
- machine: linux-aarch64
- commit hash: 5787d3e
- commit date: 2024-07-23
- overall geometric mean: 1.02x faster
- HPT reliability: 97.62%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-arminc-aarch64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 301 ms: 1.02x faster                                                              |
| docutils       | 2.91 sec                                                 | 3.05 sec: 1.05x slower                                                            |
| html5lib       | 64.3 ms                                                  | 67.4 ms: 1.05x slower                                                             |
| tornado_http   | 131 ms                                                   | 126 ms: 1.04x faster                                                              |
| Geometric mean | (ref)                                                    | 1.01x slower                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-arminc-aarch64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 540 ms: 1.20x faster                                                              |
| async_tree_none_tg         | 467 ms                                                   | 405 ms: 1.15x faster                                                              |
| async_tree_memoization     | 626 ms                                                   | 552 ms: 1.13x faster                                                              |
| async_tree_none            | 493 ms                                                   | 439 ms: 1.12x faster                                                              |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 725 ms: 1.05x faster                                                              |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 707 ms: 1.04x faster                                                              |
| asyncio_websockets         | 656 ms                                                   | 660 ms: 1.01x slower                                                              |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.22 sec: 1.02x slower                                                            |
| async_tree_io_tg           | 1.09 sec                                                 | 1.12 sec: 1.03x slower                                                            |
| Geometric mean             | (ref)                                                    | 1.05x faster                                                                      |

Benchmark hidden because not significant (4): async_tree_io, async_generators, coroutines, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-arminc-aarch64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 112 ms: 1.02x faster                                                              |
| float          | 94.4 ms                                                  | 92.3 ms: 1.02x faster                                                             |
| Geometric mean | (ref)                                                    | 1.01x faster                                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-arminc-aarch64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_dna      | 246 ms                                                   | 249 ms: 1.01x slower                                                              |
| Geometric mean | (ref)                                                    | 1.00x faster                                                                      |

Benchmark hidden because not significant (3): regex_v8, regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-arminc-aarch64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|--------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python | 359 us                                                   | 355 us: 1.01x faster                                                              |
| json_loads         | 31.4 us                                                  | 32.4 us: 1.03x slower                                                             |
| Geometric mean     | (ref)                                                    | 1.00x slower                                                                      |

Benchmark hidden because not significant (7): xml_etree_generate, unpickle_pure_python, json_dumps, tomli_loads, xml_etree_iterparse, xml_etree_process, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-arminc-aarch64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                             |
| Geometric mean | (ref)                                                    | 1.00x faster                                                                      |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-arminc-aarch64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|-----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| django_template | 42.3 ms                                                  | 41.5 ms: 1.02x faster                                                             |
| genshi_xml      | 60.2 ms                                                  | 60.0 ms: 1.00x faster                                                             |
| mako            | 13.3 ms                                                  | 13.4 ms: 1.00x slower                                                             |
| Geometric mean  | (ref)                                                    | 1.01x faster                                                                      |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-arminc-aarch64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| deepcopy                   | 451 us                                                   | 328 us: 1.38x faster                                                              |
| deepcopy_memo              | 51.0 us                                                  | 38.9 us: 1.31x faster                                                             |
| async_tree_memoization_tg  | 649 ms                                                   | 540 ms: 1.20x faster                                                              |
| deepcopy_reduce            | 4.07 us                                                  | 3.42 us: 1.19x faster                                                             |
| async_tree_none_tg         | 467 ms                                                   | 405 ms: 1.15x faster                                                              |
| async_tree_memoization     | 626 ms                                                   | 552 ms: 1.13x faster                                                              |
| async_tree_none            | 493 ms                                                   | 439 ms: 1.12x faster                                                              |
| generators                 | 37.8 ms                                                  | 35.0 ms: 1.08x faster                                                             |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 725 ms: 1.05x faster                                                              |
| pathlib                    | 22.4 ms                                                  | 21.4 ms: 1.04x faster                                                             |
| tornado_http               | 131 ms                                                   | 126 ms: 1.04x faster                                                              |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 707 ms: 1.04x faster                                                              |
| logging_silent             | 135 ns                                                   | 130 ns: 1.04x faster                                                              |
| pycparser                  | 1.26 sec                                                 | 1.22 sec: 1.04x faster                                                            |
| bench_thread_pool          | 1.28 ms                                                  | 1.23 ms: 1.04x faster                                                             |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.38 ms: 1.03x faster                                                             |
| richards                   | 53.5 ms                                                  | 52.1 ms: 1.03x faster                                                             |
| bench_mp_pool              | 7.30 ms                                                  | 7.12 ms: 1.02x faster                                                             |
| scimark_monte_carlo        | 83.8 ms                                                  | 81.9 ms: 1.02x faster                                                             |
| richards_super             | 60.3 ms                                                  | 58.9 ms: 1.02x faster                                                             |
| go                         | 163 ms                                                   | 159 ms: 1.02x faster                                                              |
| nbody                      | 114 ms                                                   | 112 ms: 1.02x faster                                                              |
| float                      | 94.4 ms                                                  | 92.3 ms: 1.02x faster                                                             |
| scimark_lu                 | 139 ms                                                   | 137 ms: 1.02x faster                                                              |
| python_startup             | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                             |
| django_template            | 42.3 ms                                                  | 41.5 ms: 1.02x faster                                                             |
| meteor_contest             | 113 ms                                                   | 111 ms: 1.02x faster                                                              |
| scimark_fft                | 447 ms                                                   | 440 ms: 1.02x faster                                                              |
| sqlglot_normalize          | 128 ms                                                   | 126 ms: 1.02x faster                                                              |
| chaos                      | 68.8 ms                                                  | 67.7 ms: 1.02x faster                                                             |
| 2to3                       | 306 ms                                                   | 301 ms: 1.02x faster                                                              |
| telco                      | 9.73 ms                                                  | 9.60 ms: 1.01x faster                                                             |
| pickle_pure_python         | 359 us                                                   | 355 us: 1.01x faster                                                              |
| bpe_tokeniser              | 5.90 sec                                                 | 5.86 sec: 1.01x faster                                                            |
| genshi_xml                 | 60.2 ms                                                  | 60.0 ms: 1.00x faster                                                             |
| mako                       | 13.3 ms                                                  | 13.4 ms: 1.00x slower                                                             |
| asyncio_websockets         | 656 ms                                                   | 660 ms: 1.01x slower                                                              |
| coverage                   | 98.5 ms                                                  | 99.3 ms: 1.01x slower                                                             |
| sympy_expand               | 455 ms                                                   | 458 ms: 1.01x slower                                                              |
| regex_dna                  | 246 ms                                                   | 249 ms: 1.01x slower                                                              |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.22 sec: 1.02x slower                                                            |
| sympy_str                  | 264 ms                                                   | 268 ms: 1.02x slower                                                              |
| json                       | 5.61 ms                                                  | 5.73 ms: 1.02x slower                                                             |
| pprint_pformat             | 1.90 sec                                                 | 1.94 sec: 1.02x slower                                                            |
| comprehensions             | 20.4 us                                                  | 20.9 us: 1.03x slower                                                             |
| fannkuch                   | 452 ms                                                   | 463 ms: 1.03x slower                                                              |
| async_tree_io_tg           | 1.09 sec                                                 | 1.12 sec: 1.03x slower                                                            |
| pprint_safe_repr           | 926 ms                                                   | 952 ms: 1.03x slower                                                              |
| typing_runtime_protocols   | 192 us                                                   | 198 us: 1.03x slower                                                              |
| sqlglot_parse              | 1.38 ms                                                  | 1.42 ms: 1.03x slower                                                             |
| json_loads                 | 31.4 us                                                  | 32.4 us: 1.03x slower                                                             |
| pyflate                    | 556 ms                                                   | 576 ms: 1.04x slower                                                              |
| dask                       | 350 ms                                                   | 365 ms: 1.04x slower                                                              |
| html5lib                   | 64.3 ms                                                  | 67.4 ms: 1.05x slower                                                             |
| docutils                   | 2.91 sec                                                 | 3.05 sec: 1.05x slower                                                            |
| gc_traversal               | 4.53 ms                                                  | 4.88 ms: 1.08x slower                                                             |
| create_gc_cycles           | 2.12 ms                                                  | 2.28 ms: 1.08x slower                                                             |
| Geometric mean             | (ref)                                                    | 1.02x faster                                                                      |

Benchmark hidden because not significant (33): xml_etree_generate, async_tree_io, regex_v8, logging_simple, hexiom, logging_format, unpickle_pure_python, crypto_pyaes, async_generators, scimark_sor, sqlglot_transpile, genshi_text, regex_compile, sqlglot_optimize, sympy_integrate, json_dumps, spectral_norm, coroutines, pidigits, regex_effbot, tomli_loads, mdp, raytrace, asyncio_tcp, xml_etree_iterparse, deltablue, sympy_sum, nqueens, thrift, xml_etree_process, python_startup_no_site, xml_etree_parse, pylint
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240723-3.14.0a0-5787d3e/bm-20240723-arminc-aarch64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e.json: dulwich_log

# HPT report

- Reliability score: 97.62% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x