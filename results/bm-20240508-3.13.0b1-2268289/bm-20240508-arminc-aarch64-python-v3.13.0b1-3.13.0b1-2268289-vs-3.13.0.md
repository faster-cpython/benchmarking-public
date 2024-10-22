# Results vs. 3.13.0

- fork: python
- ref: v3.13.0b1
- machine: linux-aarch64
- commit hash: 2268289
- commit date: 2024-05-08
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| chameleon      | 9.02 ms                                                  | 9.23 ms: 1.02x slower                                        |
| docutils       | 2.91 sec                                                 | 3.12 sec: 1.07x slower                                       |
| html5lib       | 64.3 ms                                                  | 66.6 ms: 1.03x slower                                        |
| Geometric mean | (ref)                                                    | 1.02x slower                                                 |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| asyncio_tcp                | 568 ms                                                   | 545 ms: 1.04x faster                                         |
| async_tree_memoization_tg  | 649 ms                                                   | 628 ms: 1.03x faster                                         |
| async_generators           | 496 ms                                                   | 488 ms: 1.02x faster                                         |
| asyncio_websockets         | 656 ms                                                   | 666 ms: 1.02x slower                                         |
| async_tree_memoization     | 626 ms                                                   | 645 ms: 1.03x slower                                         |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 799 ms: 1.05x slower                                         |
| coroutines                 | 28.2 ms                                                  | 29.7 ms: 1.05x slower                                        |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 795 ms: 1.08x slower                                         |
| async_tree_io              | 1.11 sec                                                 | 1.21 sec: 1.10x slower                                       |
| async_tree_io_tg           | 1.09 sec                                                 | 1.23 sec: 1.13x slower                                       |
| Geometric mean             | (ref)                                                    | 1.03x slower                                                 |

Benchmark hidden because not significant (3): async_tree_none, asyncio_tcp_ssl, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 90.7 ms: 1.04x faster                                        |
| nbody          | 114 ms                                                   | 110 ms: 1.03x faster                                         |
| Geometric mean | (ref)                                                    | 1.02x faster                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 128 ms                                                   | 130 ms: 1.01x slower                                         |
| regex_dna      | 246 ms                                                   | 257 ms: 1.04x slower                                         |
| Geometric mean | (ref)                                                    | 1.02x slower                                                 |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle_list       | 6.65 us                                                  | 6.31 us: 1.05x faster                                        |
| unpickle            | 20.2 us                                                  | 19.5 us: 1.03x faster                                        |
| pickle_list         | 5.34 us                                                  | 5.26 us: 1.01x faster                                        |
| pickle_pure_python  | 359 us                                                   | 363 us: 1.01x slower                                         |
| pickle              | 13.5 us                                                  | 13.7 us: 1.02x slower                                        |
| xml_etree_iterparse | 147 ms                                                   | 150 ms: 1.03x slower                                         |
| json_loads          | 31.4 us                                                  | 32.3 us: 1.03x slower                                        |
| tomli_loads         | 2.53 sec                                                 | 2.64 sec: 1.04x slower                                       |
| xml_etree_parse     | 188 ms                                                   | 199 ms: 1.06x slower                                         |
| Geometric mean      | (ref)                                                    | 1.01x slower                                                 |

Benchmark hidden because not significant (5): pickle_dict, unpickle_pure_python, json_dumps, xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                  | 12.6 ms: 1.05x faster                                        |
| python_startup_no_site | 8.75 ms                                                  | 8.49 ms: 1.03x faster                                        |
| Geometric mean         | (ref)                                                    | 1.04x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| mako           | 13.3 ms                                                  | 13.2 ms: 1.01x faster                                        |
| genshi_xml     | 60.2 ms                                                  | 61.7 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                    | 1.01x slower                                                 |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| mypy2                      | 1.18 sec                                                 | 771 ms: 1.54x faster                                         |
| python_startup             | 13.3 ms                                                  | 12.6 ms: 1.05x faster                                        |
| unpickle_list              | 6.65 us                                                  | 6.31 us: 1.05x faster                                        |
| asyncio_tcp                | 568 ms                                                   | 545 ms: 1.04x faster                                         |
| float                      | 94.4 ms                                                  | 90.7 ms: 1.04x faster                                        |
| bench_mp_pool              | 7.30 ms                                                  | 7.04 ms: 1.04x faster                                        |
| chaos                      | 68.8 ms                                                  | 66.5 ms: 1.03x faster                                        |
| async_tree_memoization_tg  | 649 ms                                                   | 628 ms: 1.03x faster                                         |
| nbody                      | 114 ms                                                   | 110 ms: 1.03x faster                                         |
| unpickle                   | 20.2 us                                                  | 19.5 us: 1.03x faster                                        |
| python_startup_no_site     | 8.75 ms                                                  | 8.49 ms: 1.03x faster                                        |
| pycparser                  | 1.26 sec                                                 | 1.23 sec: 1.02x faster                                       |
| go                         | 163 ms                                                   | 160 ms: 1.02x faster                                         |
| async_generators           | 496 ms                                                   | 488 ms: 1.02x faster                                         |
| pickle_list                | 5.34 us                                                  | 5.26 us: 1.01x faster                                        |
| generators                 | 37.8 ms                                                  | 37.3 ms: 1.01x faster                                        |
| scimark_fft                | 447 ms                                                   | 442 ms: 1.01x faster                                         |
| mako                       | 13.3 ms                                                  | 13.2 ms: 1.01x faster                                        |
| mdp                        | 3.36 sec                                                 | 3.34 sec: 1.01x faster                                       |
| pickle_pure_python         | 359 us                                                   | 363 us: 1.01x slower                                         |
| regex_compile              | 128 ms                                                   | 130 ms: 1.01x slower                                         |
| sqlite_synth               | 3.84 us                                                  | 3.89 us: 1.01x slower                                        |
| logging_simple             | 7.04 us                                                  | 7.15 us: 1.02x slower                                        |
| asyncio_websockets         | 656 ms                                                   | 666 ms: 1.02x slower                                         |
| sympy_sum                  | 143 ms                                                   | 146 ms: 1.02x slower                                         |
| pickle                     | 13.5 us                                                  | 13.7 us: 1.02x slower                                        |
| sympy_integrate            | 21.0 ms                                                  | 21.4 ms: 1.02x slower                                        |
| pprint_pformat             | 1.90 sec                                                 | 1.94 sec: 1.02x slower                                       |
| chameleon                  | 9.02 ms                                                  | 9.23 ms: 1.02x slower                                        |
| pprint_safe_repr           | 926 ms                                                   | 948 ms: 1.02x slower                                         |
| nqueens                    | 98.7 ms                                                  | 101 ms: 1.02x slower                                         |
| genshi_xml                 | 60.2 ms                                                  | 61.7 ms: 1.02x slower                                        |
| sympy_str                  | 264 ms                                                   | 270 ms: 1.03x slower                                         |
| xml_etree_iterparse        | 147 ms                                                   | 150 ms: 1.03x slower                                         |
| json_loads                 | 31.4 us                                                  | 32.3 us: 1.03x slower                                        |
| fannkuch                   | 452 ms                                                   | 465 ms: 1.03x slower                                         |
| pathlib                    | 22.4 ms                                                  | 23.1 ms: 1.03x slower                                        |
| sqlglot_parse              | 1.38 ms                                                  | 1.42 ms: 1.03x slower                                        |
| async_tree_memoization     | 626 ms                                                   | 645 ms: 1.03x slower                                         |
| sympy_expand               | 455 ms                                                   | 470 ms: 1.03x slower                                         |
| html5lib                   | 64.3 ms                                                  | 66.6 ms: 1.03x slower                                        |
| richards_super             | 60.3 ms                                                  | 62.8 ms: 1.04x slower                                        |
| regex_dna                  | 246 ms                                                   | 257 ms: 1.04x slower                                         |
| tomli_loads                | 2.53 sec                                                 | 2.64 sec: 1.04x slower                                       |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 799 ms: 1.05x slower                                         |
| coroutines                 | 28.2 ms                                                  | 29.7 ms: 1.05x slower                                        |
| richards                   | 53.5 ms                                                  | 56.3 ms: 1.05x slower                                        |
| flaskblogging              | 4.60 ms                                                  | 4.84 ms: 1.05x slower                                        |
| typing_runtime_protocols   | 192 us                                                   | 203 us: 1.06x slower                                         |
| xml_etree_parse            | 188 ms                                                   | 199 ms: 1.06x slower                                         |
| pyflate                    | 556 ms                                                   | 595 ms: 1.07x slower                                         |
| docutils                   | 2.91 sec                                                 | 3.12 sec: 1.07x slower                                       |
| dask                       | 350 ms                                                   | 378 ms: 1.08x slower                                         |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 795 ms: 1.08x slower                                         |
| async_tree_io              | 1.11 sec                                                 | 1.21 sec: 1.10x slower                                       |
| gc_traversal               | 4.53 ms                                                  | 5.09 ms: 1.12x slower                                        |
| async_tree_io_tg           | 1.09 sec                                                 | 1.23 sec: 1.13x slower                                       |
| create_gc_cycles           | 2.12 ms                                                  | 2.43 ms: 1.15x slower                                        |
| telco                      | 9.73 ms                                                  | 167 ms: 17.20x slower                                        |
| Geometric mean             | (ref)                                                    | 1.04x slower                                                 |

Benchmark hidden because not significant (41): spectral_norm, scimark_monte_carlo, hexiom, tornado_http, logging_format, logging_silent, async_tree_none, raytrace, asyncio_tcp_ssl, crypto_pyaes, pickle_dict, scimark_sparse_mat_mult, comprehensions, regex_v8, deepcopy_memo, meteor_contest, scimark_lu, thrift, 2to3, sqlglot_transpile, coverage, pylint, unpickle_pure_python, bench_thread_pool, scimark_sor, json_dumps, sqlglot_normalize, deepcopy_reduce, deepcopy, aiohttp, pidigits, django_template, json, gunicorn, async_tree_none_tg, regex_effbot, genshi_text, deltablue, sqlglot_optimize, xml_etree_process, xml_etree_generate
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, unpack_sequence
Ignored benchmarks (1) of results/bm-20240508-3.13.0b1-2268289/bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289.json: dulwich_log

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x