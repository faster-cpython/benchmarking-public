# Results vs. 3.13.0

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-aarch64
- commit hash: 2fa7b0e
- commit date: 2024-09-04
- overall geometric mean: 1.02x faster
- HPT reliability: 98.34%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 294 ms: 1.04x faster                                                    |
| docutils       | 2.91 sec                                                 | 3.01 sec: 1.04x slower                                                  |
| tornado_http   | 131 ms                                                   | 126 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg | 649 ms                                                   | 553 ms: 1.17x faster                                                    |
| async_tree_none           | 493 ms                                                   | 437 ms: 1.13x faster                                                    |
| async_tree_none_tg        | 467 ms                                                   | 419 ms: 1.11x faster                                                    |
| async_tree_memoization    | 626 ms                                                   | 568 ms: 1.10x faster                                                    |
| async_generators          | 496 ms                                                   | 479 ms: 1.04x faster                                                    |
| async_tree_cpu_io_mixed   | 764 ms                                                   | 739 ms: 1.03x faster                                                    |
| coroutines                | 28.2 ms                                                  | 28.3 ms: 1.00x slower                                                   |
| asyncio_websockets        | 656 ms                                                   | 662 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl           | 2.18 sec                                                 | 2.20 sec: 1.01x slower                                                  |
| async_tree_io             | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                  |
| async_tree_io_tg          | 1.09 sec                                                 | 1.17 sec: 1.08x slower                                                  |
| Geometric mean            | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 109 ms: 1.04x faster                                                    |
| float          | 94.4 ms                                                  | 92.6 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.5 ms: 1.03x faster                                                   |
| regex_compile  | 128 ms                                                   | 127 ms: 1.01x faster                                                    |
| regex_effbot   | 4.87 ms                                                  | 4.94 ms: 1.01x slower                                                   |
| regex_dna      | 246 ms                                                   | 254 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                    | 1.00x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse | 147 ms                                                   | 146 ms: 1.01x faster                                                    |
| tomli_loads         | 2.53 sec                                                 | 2.63 sec: 1.04x slower                                                  |
| json_loads          | 31.4 us                                                  | 32.7 us: 1.04x slower                                                   |
| Geometric mean      | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (6): xml_etree_generate, unpickle_pure_python, pickle_pure_python, xml_etree_parse, xml_etree_process, json_dumps

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 27.7 ms                                                  | 27.1 ms: 1.02x faster                                                   |
| mako           | 13.3 ms                                                  | 13.5 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                  | 451 us                                                   | 329 us: 1.37x faster                                                    |
| deepcopy_memo             | 51.0 us                                                  | 38.4 us: 1.33x faster                                                   |
| go                        | 163 ms                                                   | 136 ms: 1.20x faster                                                    |
| async_tree_memoization_tg | 649 ms                                                   | 553 ms: 1.17x faster                                                    |
| deepcopy_reduce           | 4.07 us                                                  | 3.48 us: 1.17x faster                                                   |
| async_tree_none           | 493 ms                                                   | 437 ms: 1.13x faster                                                    |
| async_tree_none_tg        | 467 ms                                                   | 419 ms: 1.11x faster                                                    |
| async_tree_memoization    | 626 ms                                                   | 568 ms: 1.10x faster                                                    |
| generators                | 37.8 ms                                                  | 34.6 ms: 1.09x faster                                                   |
| pathlib                   | 22.4 ms                                                  | 20.9 ms: 1.07x faster                                                   |
| nbody                     | 114 ms                                                   | 109 ms: 1.04x faster                                                    |
| bench_thread_pool         | 1.28 ms                                                  | 1.23 ms: 1.04x faster                                                   |
| tornado_http              | 131 ms                                                   | 126 ms: 1.04x faster                                                    |
| 2to3                      | 306 ms                                                   | 294 ms: 1.04x faster                                                    |
| async_generators          | 496 ms                                                   | 479 ms: 1.04x faster                                                    |
| async_tree_cpu_io_mixed   | 764 ms                                                   | 739 ms: 1.03x faster                                                    |
| regex_v8                  | 31.5 ms                                                  | 30.5 ms: 1.03x faster                                                   |
| scimark_lu                | 139 ms                                                   | 135 ms: 1.03x faster                                                    |
| bench_mp_pool             | 7.30 ms                                                  | 7.09 ms: 1.03x faster                                                   |
| scimark_sparse_mat_mult   | 6.58 ms                                                  | 6.39 ms: 1.03x faster                                                   |
| logging_silent            | 135 ns                                                   | 132 ns: 1.03x faster                                                    |
| pycparser                 | 1.26 sec                                                 | 1.23 sec: 1.02x faster                                                  |
| pprint_safe_repr          | 926 ms                                                   | 905 ms: 1.02x faster                                                    |
| genshi_text               | 27.7 ms                                                  | 27.1 ms: 1.02x faster                                                   |
| scimark_monte_carlo       | 83.8 ms                                                  | 82.2 ms: 1.02x faster                                                   |
| float                     | 94.4 ms                                                  | 92.6 ms: 1.02x faster                                                   |
| richards_super            | 60.3 ms                                                  | 59.2 ms: 1.02x faster                                                   |
| scimark_fft               | 447 ms                                                   | 440 ms: 1.02x faster                                                    |
| pprint_pformat            | 1.90 sec                                                 | 1.87 sec: 1.02x faster                                                  |
| sqlglot_normalize         | 128 ms                                                   | 126 ms: 1.02x faster                                                    |
| regex_compile             | 128 ms                                                   | 127 ms: 1.01x faster                                                    |
| xml_etree_iterparse       | 147 ms                                                   | 146 ms: 1.01x faster                                                    |
| thrift                    | 946 us                                                   | 939 us: 1.01x faster                                                    |
| coroutines                | 28.2 ms                                                  | 28.3 ms: 1.00x slower                                                   |
| bpe_tokeniser             | 5.90 sec                                                 | 5.94 sec: 1.01x slower                                                  |
| asyncio_websockets        | 656 ms                                                   | 662 ms: 1.01x slower                                                    |
| mako                      | 13.3 ms                                                  | 13.5 ms: 1.01x slower                                                   |
| asyncio_tcp_ssl           | 2.18 sec                                                 | 2.20 sec: 1.01x slower                                                  |
| regex_effbot              | 4.87 ms                                                  | 4.94 ms: 1.01x slower                                                   |
| meteor_contest            | 113 ms                                                   | 115 ms: 1.01x slower                                                    |
| sympy_expand              | 455 ms                                                   | 461 ms: 1.01x slower                                                    |
| raytrace                  | 298 ms                                                   | 303 ms: 1.02x slower                                                    |
| sqlglot_parse             | 1.38 ms                                                  | 1.41 ms: 1.02x slower                                                   |
| json                      | 5.61 ms                                                  | 5.73 ms: 1.02x slower                                                   |
| typing_runtime_protocols  | 192 us                                                   | 197 us: 1.03x slower                                                    |
| fannkuch                  | 452 ms                                                   | 465 ms: 1.03x slower                                                    |
| regex_dna                 | 246 ms                                                   | 254 ms: 1.03x slower                                                    |
| telco                     | 9.73 ms                                                  | 10.1 ms: 1.03x slower                                                   |
| docutils                  | 2.91 sec                                                 | 3.01 sec: 1.04x slower                                                  |
| async_tree_io             | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                  |
| tomli_loads               | 2.53 sec                                                 | 2.63 sec: 1.04x slower                                                  |
| json_loads                | 31.4 us                                                  | 32.7 us: 1.04x slower                                                   |
| pyflate                   | 556 ms                                                   | 582 ms: 1.05x slower                                                    |
| async_tree_io_tg          | 1.09 sec                                                 | 1.17 sec: 1.08x slower                                                  |
| create_gc_cycles          | 2.12 ms                                                  | 2.30 ms: 1.08x slower                                                   |
| gc_traversal              | 4.53 ms                                                  | 4.99 ms: 1.10x slower                                                   |
| Geometric mean            | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (33): logging_format, xml_etree_generate, django_template, genshi_xml, scimark_sor, python_startup, html5lib, sympy_integrate, unpickle_pure_python, logging_simple, richards, async_tree_cpu_io_mixed_tg, sqlglot_optimize, sympy_sum, mdp, sqlglot_transpile, chaos, pickle_pure_python, pidigits, nqueens, crypto_pyaes, sympy_str, python_startup_no_site, spectral_norm, deltablue, coverage, xml_etree_parse, xml_etree_process, asyncio_tcp, json_dumps, hexiom, comprehensions, pylint
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 98.34% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x