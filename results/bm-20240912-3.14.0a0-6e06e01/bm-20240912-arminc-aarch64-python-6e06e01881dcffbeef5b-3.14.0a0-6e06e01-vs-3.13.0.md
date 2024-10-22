# Results vs. 3.13.0

- fork: python
- ref: 6e06e01881dcffbeef5b
- machine: linux-aarch64
- commit hash: 6e06e01
- commit date: 2024-09-12
- overall geometric mean: 1.01x faster
- HPT reliability: 96.80%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 297 ms: 1.03x faster                                                    |
| docutils       | 2.91 sec                                                 | 3.05 sec: 1.05x slower                                                  |
| Geometric mean | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 553 ms: 1.18x faster                                                    |
| async_tree_none            | 493 ms                                                   | 421 ms: 1.17x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 416 ms: 1.12x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 562 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 720 ms: 1.06x faster                                                    |
| async_generators           | 496 ms                                                   | 479 ms: 1.04x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 718 ms: 1.03x faster                                                    |
| asyncio_websockets         | 656 ms                                                   | 661 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.21 sec: 1.01x slower                                                  |
| coroutines                 | 28.2 ms                                                  | 28.9 ms: 1.02x slower                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.14 sec: 1.03x slower                                                  |
| async_tree_io_tg           | 1.09 sec                                                 | 1.18 sec: 1.08x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (1): asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 110 ms: 1.03x faster                                                    |
| float          | 94.4 ms                                                  | 92.9 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.5 ms: 1.03x faster                                                   |
| regex_compile  | 128 ms                                                   | 127 ms: 1.02x faster                                                    |
| regex_effbot   | 4.87 ms                                                  | 4.95 ms: 1.02x slower                                                   |
| regex_dna      | 246 ms                                                   | 255 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                    | 1.00x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|--------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_list      | 6.65 us                                                  | 6.40 us: 1.04x faster                                                   |
| unpickle           | 20.2 us                                                  | 19.5 us: 1.03x faster                                                   |
| pickle_list        | 5.34 us                                                  | 5.20 us: 1.03x faster                                                   |
| pickle             | 13.5 us                                                  | 13.7 us: 1.01x slower                                                   |
| pickle_pure_python | 359 us                                                   | 373 us: 1.04x slower                                                    |
| tomli_loads        | 2.53 sec                                                 | 2.65 sec: 1.05x slower                                                  |
| Geometric mean     | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (8): unpickle_pure_python, xml_etree_generate, pickle_dict, json_dumps, json_loads, xml_etree_iterparse, xml_etree_parse, xml_etree_process

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 13.3 ms                                                  | 13.5 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (3): genshi_text, django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 51.0 us                                                  | 37.5 us: 1.36x faster                                                   |
| deepcopy                   | 451 us                                                   | 337 us: 1.34x faster                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 553 ms: 1.18x faster                                                    |
| go                         | 163 ms                                                   | 139 ms: 1.17x faster                                                    |
| async_tree_none            | 493 ms                                                   | 421 ms: 1.17x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 3.57 us: 1.14x faster                                                   |
| async_tree_none_tg         | 467 ms                                                   | 416 ms: 1.12x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 562 ms: 1.11x faster                                                    |
| generators                 | 37.8 ms                                                  | 34.9 ms: 1.08x faster                                                   |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 720 ms: 1.06x faster                                                    |
| pathlib                    | 22.4 ms                                                  | 21.1 ms: 1.06x faster                                                   |
| unpickle_list              | 6.65 us                                                  | 6.40 us: 1.04x faster                                                   |
| bench_thread_pool          | 1.28 ms                                                  | 1.23 ms: 1.04x faster                                                   |
| async_generators           | 496 ms                                                   | 479 ms: 1.04x faster                                                    |
| scimark_lu                 | 139 ms                                                   | 135 ms: 1.04x faster                                                    |
| regex_v8                   | 31.5 ms                                                  | 30.5 ms: 1.03x faster                                                   |
| nbody                      | 114 ms                                                   | 110 ms: 1.03x faster                                                    |
| unpickle                   | 20.2 us                                                  | 19.5 us: 1.03x faster                                                   |
| 2to3                       | 306 ms                                                   | 297 ms: 1.03x faster                                                    |
| pickle_list                | 5.34 us                                                  | 5.20 us: 1.03x faster                                                   |
| bench_mp_pool              | 7.30 ms                                                  | 7.11 ms: 1.03x faster                                                   |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 718 ms: 1.03x faster                                                    |
| pycparser                  | 1.26 sec                                                 | 1.23 sec: 1.02x faster                                                  |
| scimark_monte_carlo        | 83.8 ms                                                  | 82.1 ms: 1.02x faster                                                   |
| logging_silent             | 135 ns                                                   | 133 ns: 1.02x faster                                                    |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.47 ms: 1.02x faster                                                   |
| thrift                     | 946 us                                                   | 931 us: 1.02x faster                                                    |
| float                      | 94.4 ms                                                  | 92.9 ms: 1.02x faster                                                   |
| meteor_contest             | 113 ms                                                   | 112 ms: 1.02x faster                                                    |
| regex_compile              | 128 ms                                                   | 127 ms: 1.02x faster                                                    |
| sqlglot_normalize          | 128 ms                                                   | 127 ms: 1.01x faster                                                    |
| richards                   | 53.5 ms                                                  | 52.8 ms: 1.01x faster                                                   |
| sympy_integrate            | 21.0 ms                                                  | 20.7 ms: 1.01x faster                                                   |
| bpe_tokeniser              | 5.90 sec                                                 | 5.83 sec: 1.01x faster                                                  |
| coverage                   | 98.5 ms                                                  | 97.6 ms: 1.01x faster                                                   |
| spectral_norm              | 141 ms                                                   | 140 ms: 1.01x faster                                                    |
| sqlite_synth               | 3.84 us                                                  | 3.81 us: 1.01x faster                                                   |
| pprint_pformat             | 1.90 sec                                                 | 1.91 sec: 1.01x slower                                                  |
| asyncio_websockets         | 656 ms                                                   | 661 ms: 1.01x slower                                                    |
| raytrace                   | 298 ms                                                   | 301 ms: 1.01x slower                                                    |
| mako                       | 13.3 ms                                                  | 13.5 ms: 1.01x slower                                                   |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.21 sec: 1.01x slower                                                  |
| pickle                     | 13.5 us                                                  | 13.7 us: 1.01x slower                                                   |
| regex_effbot               | 4.87 ms                                                  | 4.95 ms: 1.02x slower                                                   |
| sympy_expand               | 455 ms                                                   | 462 ms: 1.02x slower                                                    |
| logging_simple             | 7.04 us                                                  | 7.18 us: 1.02x slower                                                   |
| coroutines                 | 28.2 ms                                                  | 28.9 ms: 1.02x slower                                                   |
| fannkuch                   | 452 ms                                                   | 462 ms: 1.02x slower                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.14 sec: 1.03x slower                                                  |
| sqlglot_parse              | 1.38 ms                                                  | 1.43 ms: 1.03x slower                                                   |
| regex_dna                  | 246 ms                                                   | 255 ms: 1.04x slower                                                    |
| pickle_pure_python         | 359 us                                                   | 373 us: 1.04x slower                                                    |
| pyflate                    | 556 ms                                                   | 580 ms: 1.04x slower                                                    |
| tomli_loads                | 2.53 sec                                                 | 2.65 sec: 1.05x slower                                                  |
| docutils                   | 2.91 sec                                                 | 3.05 sec: 1.05x slower                                                  |
| telco                      | 9.73 ms                                                  | 10.2 ms: 1.05x slower                                                   |
| create_gc_cycles           | 2.12 ms                                                  | 2.27 ms: 1.07x slower                                                   |
| async_tree_io_tg           | 1.09 sec                                                 | 1.18 sec: 1.08x slower                                                  |
| gc_traversal               | 4.53 ms                                                  | 5.09 ms: 1.12x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (37): tornado_http, python_startup, genshi_text, crypto_pyaes, scimark_sor, unpack_sequence, sympy_sum, unpickle_pure_python, python_startup_no_site, xml_etree_generate, chaos, json, scimark_fft, pickle_dict, nqueens, richards_super, asyncio_tcp, typing_runtime_protocols, sympy_str, pidigits, pprint_safe_repr, sqlglot_optimize, django_template, json_dumps, mdp, genshi_xml, comprehensions, deltablue, hexiom, json_loads, sqlglot_transpile, logging_format, xml_etree_iterparse, xml_etree_parse, xml_etree_process, html5lib, pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240912-3.14.0a0-6e06e01/bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json: dulwich_log

# HPT report

- Reliability score: 96.80% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x