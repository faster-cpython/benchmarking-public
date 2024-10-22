# Results vs. 3.13.0

- fork: python
- ref: v3.14.0a1
- machine: linux-aarch64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.06x slower
- HPT reliability: 99.64%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 293 ms: 1.04x faster                                         |
| docutils       | 2.91 sec                                                 | 3.01 sec: 1.03x slower                                       |
| tornado_http   | 131 ms                                                   | 125 ms: 1.05x faster                                         |
| Geometric mean | (ref)                                                    | 1.01x faster                                                 |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 538 ms: 1.21x faster                                         |
| async_tree_none            | 493 ms                                                   | 438 ms: 1.13x faster                                         |
| async_tree_memoization     | 626 ms                                                   | 563 ms: 1.11x faster                                         |
| async_tree_none_tg         | 467 ms                                                   | 447 ms: 1.05x faster                                         |
| async_generators           | 496 ms                                                   | 479 ms: 1.04x faster                                         |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 743 ms: 1.03x faster                                         |
| asyncio_tcp                | 568 ms                                                   | 554 ms: 1.03x faster                                         |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 724 ms: 1.02x faster                                         |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.21 sec: 1.02x slower                                       |
| coroutines                 | 28.2 ms                                                  | 28.8 ms: 1.02x slower                                        |
| async_tree_io              | 1.11 sec                                                 | 1.18 sec: 1.07x slower                                       |
| async_tree_io_tg           | 1.09 sec                                                 | 1.21 sec: 1.11x slower                                       |
| Geometric mean             | (ref)                                                    | 1.03x faster                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 95.4 ms: 1.01x slower                                        |
| Geometric mean | (ref)                                                    | 1.00x slower                                                 |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 128 ms                                                   | 125 ms: 1.03x faster                                         |
| regex_v8       | 31.5 ms                                                  | 31.1 ms: 1.01x faster                                        |
| regex_dna      | 246 ms                                                   | 243 ms: 1.01x faster                                         |
| Geometric mean | (ref)                                                    | 1.01x faster                                                 |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle            | 20.2 us                                                  | 19.1 us: 1.05x faster                                        |
| pickle_list         | 5.34 us                                                  | 5.22 us: 1.02x faster                                        |
| json_loads          | 31.4 us                                                  | 31.2 us: 1.01x faster                                        |
| pickle_pure_python  | 359 us                                                   | 365 us: 1.02x slower                                         |
| xml_etree_parse     | 188 ms                                                   | 191 ms: 1.02x slower                                         |
| xml_etree_iterparse | 147 ms                                                   | 150 ms: 1.02x slower                                         |
| pickle              | 13.5 us                                                  | 13.9 us: 1.03x slower                                        |
| tomli_loads         | 2.53 sec                                                 | 2.63 sec: 1.04x slower                                       |
| json_dumps          | 13.4 ms                                                  | 14.1 ms: 1.06x slower                                        |
| Geometric mean      | (ref)                                                    | 1.01x slower                                                 |

Benchmark hidden because not significant (5): pickle_dict, unpickle_list, unpickle_pure_python, xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 8.75 ms                                                  | 8.63 ms: 1.01x faster                                        |
| python_startup         | 13.3 ms                                                  | 14.5 ms: 1.09x slower                                        |
| Geometric mean         | (ref)                                                    | 1.04x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_xml     | 60.2 ms                                                  | 61.6 ms: 1.02x slower                                        |
| mako           | 13.3 ms                                                  | 13.7 ms: 1.03x slower                                        |
| Geometric mean | (ref)                                                    | 1.01x slower                                                 |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| deepcopy                   | 451 us                                                   | 333 us: 1.36x faster                                         |
| deepcopy_memo              | 51.0 us                                                  | 38.2 us: 1.33x faster                                        |
| async_tree_memoization_tg  | 649 ms                                                   | 538 ms: 1.21x faster                                         |
| go                         | 163 ms                                                   | 136 ms: 1.20x faster                                         |
| deepcopy_reduce            | 4.07 us                                                  | 3.56 us: 1.14x faster                                        |
| async_tree_none            | 493 ms                                                   | 438 ms: 1.13x faster                                         |
| async_tree_memoization     | 626 ms                                                   | 563 ms: 1.11x faster                                         |
| generators                 | 37.8 ms                                                  | 34.8 ms: 1.09x faster                                        |
| pathlib                    | 22.4 ms                                                  | 21.2 ms: 1.06x faster                                        |
| unpickle                   | 20.2 us                                                  | 19.1 us: 1.05x faster                                        |
| scimark_lu                 | 139 ms                                                   | 133 ms: 1.05x faster                                         |
| tornado_http               | 131 ms                                                   | 125 ms: 1.05x faster                                         |
| async_tree_none_tg         | 467 ms                                                   | 447 ms: 1.05x faster                                         |
| logging_format             | 7.83 us                                                  | 7.51 us: 1.04x faster                                        |
| 2to3                       | 306 ms                                                   | 293 ms: 1.04x faster                                         |
| pycparser                  | 1.26 sec                                                 | 1.21 sec: 1.04x faster                                       |
| sympy_sum                  | 143 ms                                                   | 138 ms: 1.04x faster                                         |
| async_generators           | 496 ms                                                   | 479 ms: 1.04x faster                                         |
| scimark_fft                | 447 ms                                                   | 433 ms: 1.03x faster                                         |
| logging_simple             | 7.04 us                                                  | 6.82 us: 1.03x faster                                        |
| meteor_contest             | 113 ms                                                   | 110 ms: 1.03x faster                                         |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 743 ms: 1.03x faster                                         |
| json                       | 5.61 ms                                                  | 5.46 ms: 1.03x faster                                        |
| regex_compile              | 128 ms                                                   | 125 ms: 1.03x faster                                         |
| asyncio_tcp                | 568 ms                                                   | 554 ms: 1.03x faster                                         |
| hexiom                     | 7.13 ms                                                  | 6.97 ms: 1.02x faster                                        |
| logging_silent             | 135 ns                                                   | 132 ns: 1.02x faster                                         |
| bpe_tokeniser              | 5.90 sec                                                 | 5.76 sec: 1.02x faster                                       |
| pickle_list                | 5.34 us                                                  | 5.22 us: 1.02x faster                                        |
| crypto_pyaes               | 82.7 ms                                                  | 80.9 ms: 1.02x faster                                        |
| telco                      | 9.73 ms                                                  | 9.54 ms: 1.02x faster                                        |
| pprint_safe_repr           | 926 ms                                                   | 909 ms: 1.02x faster                                         |
| thrift                     | 946 us                                                   | 929 us: 1.02x faster                                         |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.46 ms: 1.02x faster                                        |
| sqlglot_normalize          | 128 ms                                                   | 126 ms: 1.02x faster                                         |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 724 ms: 1.02x faster                                         |
| pprint_pformat             | 1.90 sec                                                 | 1.87 sec: 1.01x faster                                       |
| python_startup_no_site     | 8.75 ms                                                  | 8.63 ms: 1.01x faster                                        |
| regex_v8                   | 31.5 ms                                                  | 31.1 ms: 1.01x faster                                        |
| scimark_sor                | 159 ms                                                   | 157 ms: 1.01x faster                                         |
| regex_dna                  | 246 ms                                                   | 243 ms: 1.01x faster                                         |
| sympy_str                  | 264 ms                                                   | 261 ms: 1.01x faster                                         |
| coverage                   | 98.5 ms                                                  | 97.6 ms: 1.01x faster                                        |
| sqlglot_optimize           | 62.4 ms                                                  | 61.8 ms: 1.01x faster                                        |
| json_loads                 | 31.4 us                                                  | 31.2 us: 1.01x faster                                        |
| float                      | 94.4 ms                                                  | 95.4 ms: 1.01x slower                                        |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.21 sec: 1.02x slower                                       |
| pickle_pure_python         | 359 us                                                   | 365 us: 1.02x slower                                         |
| xml_etree_parse            | 188 ms                                                   | 191 ms: 1.02x slower                                         |
| coroutines                 | 28.2 ms                                                  | 28.8 ms: 1.02x slower                                        |
| sqlglot_parse              | 1.38 ms                                                  | 1.41 ms: 1.02x slower                                        |
| bench_thread_pool          | 1.28 ms                                                  | 1.30 ms: 1.02x slower                                        |
| xml_etree_iterparse        | 147 ms                                                   | 150 ms: 1.02x slower                                         |
| genshi_xml                 | 60.2 ms                                                  | 61.6 ms: 1.02x slower                                        |
| deltablue                  | 3.85 ms                                                  | 3.95 ms: 1.03x slower                                        |
| mako                       | 13.3 ms                                                  | 13.7 ms: 1.03x slower                                        |
| pickle                     | 13.5 us                                                  | 13.9 us: 1.03x slower                                        |
| docutils                   | 2.91 sec                                                 | 3.01 sec: 1.03x slower                                       |
| fannkuch                   | 452 ms                                                   | 469 ms: 1.04x slower                                         |
| tomli_loads                | 2.53 sec                                                 | 2.63 sec: 1.04x slower                                       |
| raytrace                   | 298 ms                                                   | 311 ms: 1.04x slower                                         |
| pyflate                    | 556 ms                                                   | 585 ms: 1.05x slower                                         |
| json_dumps                 | 13.4 ms                                                  | 14.1 ms: 1.06x slower                                        |
| async_tree_io              | 1.11 sec                                                 | 1.18 sec: 1.07x slower                                       |
| python_startup             | 13.3 ms                                                  | 14.5 ms: 1.09x slower                                        |
| async_tree_io_tg           | 1.09 sec                                                 | 1.21 sec: 1.11x slower                                       |
| gc_traversal               | 4.53 ms                                                  | 6.25 ms: 1.38x slower                                        |
| create_gc_cycles           | 2.12 ms                                                  | 3.67 ms: 1.73x slower                                        |
| bench_mp_pool              | 7.30 ms                                                  | 4.94 sec: 676.99x slower                                     |
| Geometric mean             | (ref)                                                    | 1.06x slower                                                 |

Benchmark hidden because not significant (27): pickle_dict, unpickle_list, genshi_text, richards_super, nbody, django_template, mdp, nqueens, sympy_integrate, scimark_monte_carlo, richards, pidigits, unpickle_pure_python, regex_effbot, asyncio_websockets, html5lib, unpack_sequence, sqlite_synth, spectral_norm, sympy_expand, xml_etree_process, chaos, xml_etree_generate, typing_runtime_protocols, comprehensions, sqlglot_transpile, pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (2) of results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: dulwich_log, sphinx

# HPT report

- Reliability score: 99.64% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.13x