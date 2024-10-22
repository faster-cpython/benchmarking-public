# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a4
- machine: linux-aarch64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.00x slower
- HPT reliability: 59.86%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.96x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| html5lib       | 64.3 ms                                                  | 66.1 ms: 1.03x slower                                        |
| Geometric mean | (ref)                                                    | 1.01x slower                                                 |

Benchmark hidden because not significant (4): 2to3, chameleon, docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| asyncio_tcp                | 568 ms                                                   | 553 ms: 1.03x faster                                         |
| async_generators           | 496 ms                                                   | 487 ms: 1.02x faster                                         |
| asyncio_websockets         | 656 ms                                                   | 660 ms: 1.01x slower                                         |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.20 sec: 1.01x slower                                       |
| coroutines                 | 28.2 ms                                                  | 29.2 ms: 1.03x slower                                        |
| async_tree_memoization_tg  | 649 ms                                                   | 728 ms: 1.12x slower                                         |
| async_tree_none            | 493 ms                                                   | 564 ms: 1.14x slower                                         |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 880 ms: 1.15x slower                                         |
| async_tree_memoization     | 626 ms                                                   | 737 ms: 1.18x slower                                         |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 887 ms: 1.20x slower                                         |
| async_tree_none_tg         | 467 ms                                                   | 567 ms: 1.21x slower                                         |
| async_tree_io              | 1.11 sec                                                 | 1.42 sec: 1.29x slower                                       |
| async_tree_io_tg           | 1.09 sec                                                 | 1.43 sec: 1.31x slower                                       |
| Geometric mean             | (ref)                                                    | 1.12x slower                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 106 ms: 1.08x faster                                         |
| float          | 94.4 ms                                                  | 93.1 ms: 1.01x faster                                        |
| Geometric mean | (ref)                                                    | 1.03x faster                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.2 ms: 1.04x faster                                        |
| regex_compile  | 128 ms                                                   | 125 ms: 1.03x faster                                         |
| regex_dna      | 246 ms                                                   | 253 ms: 1.03x slower                                         |
| Geometric mean | (ref)                                                    | 1.01x faster                                                 |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle_list       | 6.65 us                                                  | 6.46 us: 1.03x faster                                        |
| pickle_pure_python  | 359 us                                                   | 351 us: 1.02x faster                                         |
| unpickle            | 20.2 us                                                  | 19.7 us: 1.02x faster                                        |
| pickle_list         | 5.34 us                                                  | 5.22 us: 1.02x faster                                        |
| xml_etree_iterparse | 147 ms                                                   | 149 ms: 1.02x slower                                         |
| tomli_loads         | 2.53 sec                                                 | 2.58 sec: 1.02x slower                                       |
| json_loads          | 31.4 us                                                  | 32.2 us: 1.03x slower                                        |
| xml_etree_parse     | 188 ms                                                   | 198 ms: 1.05x slower                                         |
| Geometric mean      | (ref)                                                    | 1.00x faster                                                 |

Benchmark hidden because not significant (6): json_dumps, pickle_dict, xml_etree_process, xml_etree_generate, unpickle_pure_python, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                  | 12.1 ms: 1.09x faster                                        |
| python_startup_no_site | 8.75 ms                                                  | 10.5 ms: 1.20x slower                                        |
| Geometric mean         | (ref)                                                    | 1.05x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 42.3 ms                                                  | 40.3 ms: 1.05x faster                                        |
| genshi_text     | 27.7 ms                                                  | 27.1 ms: 1.02x faster                                        |
| mako            | 13.3 ms                                                  | 13.2 ms: 1.01x faster                                        |
| genshi_xml      | 60.2 ms                                                  | 59.7 ms: 1.01x faster                                        |
| Geometric mean  | (ref)                                                    | 1.02x faster                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols   | 192 us                                                   | 133 us: 1.45x faster                                         |
| mypy2                      | 1.18 sec                                                 | 915 ms: 1.29x faster                                         |
| python_startup             | 13.3 ms                                                  | 12.1 ms: 1.09x faster                                        |
| create_gc_cycles           | 2.12 ms                                                  | 1.96 ms: 1.08x faster                                        |
| nbody                      | 114 ms                                                   | 106 ms: 1.08x faster                                         |
| logging_silent             | 135 ns                                                   | 126 ns: 1.07x faster                                         |
| deepcopy_memo              | 51.0 us                                                  | 48.5 us: 1.05x faster                                        |
| bench_mp_pool              | 7.30 ms                                                  | 6.96 ms: 1.05x faster                                        |
| django_template            | 42.3 ms                                                  | 40.3 ms: 1.05x faster                                        |
| crypto_pyaes               | 82.7 ms                                                  | 78.8 ms: 1.05x faster                                        |
| generators                 | 37.8 ms                                                  | 36.2 ms: 1.05x faster                                        |
| regex_v8                   | 31.5 ms                                                  | 30.2 ms: 1.04x faster                                        |
| spectral_norm              | 141 ms                                                   | 135 ms: 1.04x faster                                         |
| deepcopy                   | 451 us                                                   | 434 us: 1.04x faster                                         |
| deepcopy_reduce            | 4.07 us                                                  | 3.94 us: 1.03x faster                                        |
| gc_traversal               | 4.53 ms                                                  | 4.39 ms: 1.03x faster                                        |
| sympy_sum                  | 143 ms                                                   | 139 ms: 1.03x faster                                         |
| unpickle_list              | 6.65 us                                                  | 6.46 us: 1.03x faster                                        |
| sqlglot_normalize          | 128 ms                                                   | 125 ms: 1.03x faster                                         |
| regex_compile              | 128 ms                                                   | 125 ms: 1.03x faster                                         |
| asyncio_tcp                | 568 ms                                                   | 553 ms: 1.03x faster                                         |
| pprint_safe_repr           | 926 ms                                                   | 903 ms: 1.03x faster                                         |
| chaos                      | 68.8 ms                                                  | 67.1 ms: 1.03x faster                                        |
| pickle_pure_python         | 359 us                                                   | 351 us: 1.02x faster                                         |
| sympy_str                  | 264 ms                                                   | 257 ms: 1.02x faster                                         |
| unpickle                   | 20.2 us                                                  | 19.7 us: 1.02x faster                                        |
| pickle_list                | 5.34 us                                                  | 5.22 us: 1.02x faster                                        |
| sqlglot_optimize           | 62.4 ms                                                  | 61.0 ms: 1.02x faster                                        |
| hexiom                     | 7.13 ms                                                  | 6.98 ms: 1.02x faster                                        |
| genshi_text                | 27.7 ms                                                  | 27.1 ms: 1.02x faster                                        |
| thrift                     | 946 us                                                   | 926 us: 1.02x faster                                         |
| nqueens                    | 98.7 ms                                                  | 96.6 ms: 1.02x faster                                        |
| pprint_pformat             | 1.90 sec                                                 | 1.86 sec: 1.02x faster                                       |
| async_generators           | 496 ms                                                   | 487 ms: 1.02x faster                                         |
| telco                      | 9.73 ms                                                  | 9.57 ms: 1.02x faster                                        |
| sympy_expand               | 455 ms                                                   | 448 ms: 1.02x faster                                         |
| go                         | 163 ms                                                   | 160 ms: 1.01x faster                                         |
| sympy_integrate            | 21.0 ms                                                  | 20.7 ms: 1.01x faster                                        |
| float                      | 94.4 ms                                                  | 93.1 ms: 1.01x faster                                        |
| mako                       | 13.3 ms                                                  | 13.2 ms: 1.01x faster                                        |
| scimark_fft                | 447 ms                                                   | 442 ms: 1.01x faster                                         |
| genshi_xml                 | 60.2 ms                                                  | 59.7 ms: 1.01x faster                                        |
| mdp                        | 3.36 sec                                                 | 3.34 sec: 1.01x faster                                       |
| asyncio_websockets         | 656 ms                                                   | 660 ms: 1.01x slower                                         |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.20 sec: 1.01x slower                                       |
| pycparser                  | 1.26 sec                                                 | 1.28 sec: 1.01x slower                                       |
| richards                   | 53.5 ms                                                  | 54.2 ms: 1.01x slower                                        |
| xml_etree_iterparse        | 147 ms                                                   | 149 ms: 1.02x slower                                         |
| bench_thread_pool          | 1.28 ms                                                  | 1.30 ms: 1.02x slower                                        |
| fannkuch                   | 452 ms                                                   | 461 ms: 1.02x slower                                         |
| tomli_loads                | 2.53 sec                                                 | 2.58 sec: 1.02x slower                                       |
| json_loads                 | 31.4 us                                                  | 32.2 us: 1.03x slower                                        |
| html5lib                   | 64.3 ms                                                  | 66.1 ms: 1.03x slower                                        |
| regex_dna                  | 246 ms                                                   | 253 ms: 1.03x slower                                         |
| logging_simple             | 7.04 us                                                  | 7.26 us: 1.03x slower                                        |
| coverage                   | 98.5 ms                                                  | 102 ms: 1.03x slower                                         |
| coroutines                 | 28.2 ms                                                  | 29.2 ms: 1.03x slower                                        |
| scimark_sor                | 159 ms                                                   | 166 ms: 1.04x slower                                         |
| deltablue                  | 3.85 ms                                                  | 4.03 ms: 1.05x slower                                        |
| xml_etree_parse            | 188 ms                                                   | 198 ms: 1.05x slower                                         |
| pathlib                    | 22.4 ms                                                  | 23.7 ms: 1.06x slower                                        |
| pyflate                    | 556 ms                                                   | 597 ms: 1.07x slower                                         |
| async_tree_memoization_tg  | 649 ms                                                   | 728 ms: 1.12x slower                                         |
| async_tree_none            | 493 ms                                                   | 564 ms: 1.14x slower                                         |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 880 ms: 1.15x slower                                         |
| async_tree_memoization     | 626 ms                                                   | 737 ms: 1.18x slower                                         |
| python_startup_no_site     | 8.75 ms                                                  | 10.5 ms: 1.20x slower                                        |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 887 ms: 1.20x slower                                         |
| async_tree_none_tg         | 467 ms                                                   | 567 ms: 1.21x slower                                         |
| async_tree_io              | 1.11 sec                                                 | 1.42 sec: 1.29x slower                                       |
| async_tree_io_tg           | 1.09 sec                                                 | 1.43 sec: 1.31x slower                                       |
| Geometric mean             | (ref)                                                    | 1.00x slower                                                 |

Benchmark hidden because not significant (28): pylint, json_dumps, pickle_dict, scimark_lu, sqlglot_parse, xml_etree_process, chameleon, raytrace, scimark_sparse_mat_mult, comprehensions, sqlglot_transpile, aiohttp, sqlite_synth, 2to3, docutils, pidigits, xml_etree_generate, unpickle_pure_python, scimark_monte_carlo, richards_super, pickle, regex_effbot, meteor_contest, logging_format, gunicorn, tornado_http, json, flaskblogging
Ignored benchmarks (3) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, dask, unpack_sequence
Ignored benchmarks (1) of results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60.json: dulwich_log

# HPT report

- Reliability score: 59.86% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.96x