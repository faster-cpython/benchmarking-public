# Results vs. 3.13.0

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-aarch64
- commit hash: 15b187e
- commit date: 2024-08-29
- overall geometric mean: 1.02x faster
- HPT reliability: 99.92%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 292 ms: 1.05x faster                                                    |
| docutils       | 2.91 sec                                                 | 2.98 sec: 1.02x slower                                                  |
| html5lib       | 64.3 ms                                                  | 63.5 ms: 1.01x faster                                                   |
| tornado_http   | 131 ms                                                   | 124 ms: 1.06x faster                                                    |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 545 ms: 1.19x faster                                                    |
| async_tree_none            | 493 ms                                                   | 423 ms: 1.17x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 412 ms: 1.14x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 556 ms: 1.13x faster                                                    |
| asyncio_tcp                | 568 ms                                                   | 538 ms: 1.06x faster                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 724 ms: 1.06x faster                                                    |
| async_generators           | 496 ms                                                   | 479 ms: 1.04x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 721 ms: 1.02x faster                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.16 sec: 1.01x faster                                                  |
| coroutines                 | 28.2 ms                                                  | 29.0 ms: 1.03x slower                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                  |
| async_tree_io_tg           | 1.09 sec                                                 | 1.16 sec: 1.07x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.05x faster                                                            |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 112 ms: 1.02x faster                                                    |
| float          | 94.4 ms                                                  | 92.9 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.4 ms: 1.04x faster                                                   |
| regex_compile  | 128 ms                                                   | 127 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps     | 13.4 ms                                                  | 13.6 ms: 1.02x slower                                                   |
| tomli_loads    | 2.53 sec                                                 | 2.65 sec: 1.05x slower                                                  |
| json_loads     | 31.4 us                                                  | 32.9 us: 1.05x slower                                                   |
| Geometric mean | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (6): xml_etree_process, pickle_pure_python, unpickle_pure_python, xml_etree_iterparse, xml_etree_generate, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 13.3 ms                                                  | 13.4 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (3): genshi_text, genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 51.0 us                                                  | 38.0 us: 1.34x faster                                                   |
| deepcopy                   | 451 us                                                   | 337 us: 1.34x faster                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 545 ms: 1.19x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 3.49 us: 1.17x faster                                                   |
| async_tree_none            | 493 ms                                                   | 423 ms: 1.17x faster                                                    |
| go                         | 163 ms                                                   | 140 ms: 1.16x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 412 ms: 1.14x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 556 ms: 1.13x faster                                                    |
| generators                 | 37.8 ms                                                  | 34.6 ms: 1.09x faster                                                   |
| pathlib                    | 22.4 ms                                                  | 21.1 ms: 1.06x faster                                                   |
| tornado_http               | 131 ms                                                   | 124 ms: 1.06x faster                                                    |
| asyncio_tcp                | 568 ms                                                   | 538 ms: 1.06x faster                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 724 ms: 1.06x faster                                                    |
| 2to3                       | 306 ms                                                   | 292 ms: 1.05x faster                                                    |
| bench_thread_pool          | 1.28 ms                                                  | 1.23 ms: 1.04x faster                                                   |
| pycparser                  | 1.26 sec                                                 | 1.22 sec: 1.04x faster                                                  |
| regex_v8                   | 31.5 ms                                                  | 30.4 ms: 1.04x faster                                                   |
| async_generators           | 496 ms                                                   | 479 ms: 1.04x faster                                                    |
| scimark_monte_carlo        | 83.8 ms                                                  | 81.5 ms: 1.03x faster                                                   |
| scimark_lu                 | 139 ms                                                   | 136 ms: 1.03x faster                                                    |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.42 ms: 1.03x faster                                                   |
| python_startup             | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                   |
| thrift                     | 946 us                                                   | 926 us: 1.02x faster                                                    |
| nbody                      | 114 ms                                                   | 112 ms: 1.02x faster                                                    |
| bench_mp_pool              | 7.30 ms                                                  | 7.15 ms: 1.02x faster                                                   |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 721 ms: 1.02x faster                                                    |
| pprint_safe_repr           | 926 ms                                                   | 910 ms: 1.02x faster                                                    |
| richards_super             | 60.3 ms                                                  | 59.2 ms: 1.02x faster                                                   |
| float                      | 94.4 ms                                                  | 92.9 ms: 1.02x faster                                                   |
| richards                   | 53.5 ms                                                  | 52.7 ms: 1.02x faster                                                   |
| logging_silent             | 135 ns                                                   | 133 ns: 1.01x faster                                                    |
| pprint_pformat             | 1.90 sec                                                 | 1.87 sec: 1.01x faster                                                  |
| regex_compile              | 128 ms                                                   | 127 ms: 1.01x faster                                                    |
| html5lib                   | 64.3 ms                                                  | 63.5 ms: 1.01x faster                                                   |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.16 sec: 1.01x faster                                                  |
| mako                       | 13.3 ms                                                  | 13.4 ms: 1.01x slower                                                   |
| pyflate                    | 556 ms                                                   | 562 ms: 1.01x slower                                                    |
| nqueens                    | 98.7 ms                                                  | 99.9 ms: 1.01x slower                                                   |
| json_dumps                 | 13.4 ms                                                  | 13.6 ms: 1.02x slower                                                   |
| raytrace                   | 298 ms                                                   | 303 ms: 1.02x slower                                                    |
| typing_runtime_protocols   | 192 us                                                   | 196 us: 1.02x slower                                                    |
| telco                      | 9.73 ms                                                  | 9.94 ms: 1.02x slower                                                   |
| docutils                   | 2.91 sec                                                 | 2.98 sec: 1.02x slower                                                  |
| coroutines                 | 28.2 ms                                                  | 29.0 ms: 1.03x slower                                                   |
| json                       | 5.61 ms                                                  | 5.77 ms: 1.03x slower                                                   |
| fannkuch                   | 452 ms                                                   | 464 ms: 1.03x slower                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                  |
| tomli_loads                | 2.53 sec                                                 | 2.65 sec: 1.05x slower                                                  |
| json_loads                 | 31.4 us                                                  | 32.9 us: 1.05x slower                                                   |
| async_tree_io_tg           | 1.09 sec                                                 | 1.16 sec: 1.07x slower                                                  |
| create_gc_cycles           | 2.12 ms                                                  | 2.29 ms: 1.08x slower                                                   |
| gc_traversal               | 4.53 ms                                                  | 4.97 ms: 1.10x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (37): xml_etree_process, sqlglot_transpile, logging_format, sympy_sum, meteor_contest, sympy_integrate, genshi_text, scimark_fft, logging_simple, scimark_sor, regex_effbot, pickle_pure_python, unpickle_pure_python, spectral_norm, genshi_xml, python_startup_no_site, sqlglot_optimize, sympy_str, regex_dna, crypto_pyaes, chaos, xml_etree_iterparse, coverage, pidigits, bpe_tokeniser, xml_etree_generate, mdp, django_template, sqlglot_normalize, sympy_expand, xml_etree_parse, deltablue, asyncio_websockets, comprehensions, hexiom, sqlglot_parse, pylint
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.92% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x