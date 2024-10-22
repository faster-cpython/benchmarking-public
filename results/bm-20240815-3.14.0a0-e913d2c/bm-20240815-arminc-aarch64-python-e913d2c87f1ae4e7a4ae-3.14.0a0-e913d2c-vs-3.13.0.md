# Results vs. 3.13.0

- fork: python
- ref: e913d2c87f1ae4e7a4ae
- machine: linux-aarch64
- commit hash: e913d2c
- commit date: 2024-08-15
- overall geometric mean: 1.02x faster
- HPT reliability: 92.94%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 302 ms: 1.01x faster                                                    |
| docutils       | 2.91 sec                                                 | 3.11 sec: 1.07x slower                                                  |
| html5lib       | 64.3 ms                                                  | 67.6 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                    | 1.02x slower                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 531 ms: 1.22x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 398 ms: 1.17x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 547 ms: 1.14x faster                                                    |
| async_tree_none            | 493 ms                                                   | 433 ms: 1.14x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 699 ms: 1.05x faster                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 729 ms: 1.05x faster                                                    |
| async_generators           | 496 ms                                                   | 487 ms: 1.02x faster                                                    |
| asyncio_websockets         | 656 ms                                                   | 662 ms: 1.01x slower                                                    |
| coroutines                 | 28.2 ms                                                  | 28.5 ms: 1.01x slower                                                   |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.23 sec: 1.02x slower                                                  |
| asyncio_tcp                | 568 ms                                                   | 581 ms: 1.02x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.05x faster                                                            |

Benchmark hidden because not significant (2): async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 111 ms: 1.03x faster                                                    |
| float          | 94.4 ms                                                  | 92.5 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.3 ms: 1.04x faster                                                   |
| regex_compile  | 128 ms                                                   | 127 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse | 147 ms                                                   | 148 ms: 1.01x slower                                                    |
| tomli_loads         | 2.53 sec                                                 | 2.56 sec: 1.01x slower                                                  |
| json_loads          | 31.4 us                                                  | 32.5 us: 1.03x slower                                                   |
| Geometric mean      | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (6): xml_etree_generate, pickle_pure_python, xml_etree_process, unpickle_pure_python, xml_etree_parse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 13.3 ms                                                  | 13.1 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): django_template, mako, genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 451 us                                                   | 332 us: 1.36x faster                                                    |
| deepcopy_memo              | 51.0 us                                                  | 37.9 us: 1.35x faster                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 531 ms: 1.22x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 3.42 us: 1.19x faster                                                   |
| async_tree_none_tg         | 467 ms                                                   | 398 ms: 1.17x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 547 ms: 1.14x faster                                                    |
| async_tree_none            | 493 ms                                                   | 433 ms: 1.14x faster                                                    |
| generators                 | 37.8 ms                                                  | 34.7 ms: 1.09x faster                                                   |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 699 ms: 1.05x faster                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 729 ms: 1.05x faster                                                    |
| pathlib                    | 22.4 ms                                                  | 21.5 ms: 1.04x faster                                                   |
| regex_v8                   | 31.5 ms                                                  | 30.3 ms: 1.04x faster                                                   |
| scimark_lu                 | 139 ms                                                   | 134 ms: 1.04x faster                                                    |
| bench_mp_pool              | 7.30 ms                                                  | 7.04 ms: 1.04x faster                                                   |
| pycparser                  | 1.26 sec                                                 | 1.22 sec: 1.03x faster                                                  |
| logging_silent             | 135 ns                                                   | 131 ns: 1.03x faster                                                    |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.37 ms: 1.03x faster                                                   |
| bench_thread_pool          | 1.28 ms                                                  | 1.24 ms: 1.03x faster                                                   |
| logging_format             | 7.83 us                                                  | 7.59 us: 1.03x faster                                                   |
| nbody                      | 114 ms                                                   | 111 ms: 1.03x faster                                                    |
| scimark_monte_carlo        | 83.8 ms                                                  | 81.9 ms: 1.02x faster                                                   |
| float                      | 94.4 ms                                                  | 92.5 ms: 1.02x faster                                                   |
| async_generators           | 496 ms                                                   | 487 ms: 1.02x faster                                                    |
| go                         | 163 ms                                                   | 160 ms: 1.02x faster                                                    |
| python_startup             | 13.3 ms                                                  | 13.1 ms: 1.02x faster                                                   |
| mdp                        | 3.36 sec                                                 | 3.31 sec: 1.02x faster                                                  |
| deltablue                  | 3.85 ms                                                  | 3.79 ms: 1.02x faster                                                   |
| regex_compile              | 128 ms                                                   | 127 ms: 1.02x faster                                                    |
| 2to3                       | 306 ms                                                   | 302 ms: 1.01x faster                                                    |
| chaos                      | 68.8 ms                                                  | 68.0 ms: 1.01x faster                                                   |
| coverage                   | 98.5 ms                                                  | 97.4 ms: 1.01x faster                                                   |
| bpe_tokeniser              | 5.90 sec                                                 | 5.83 sec: 1.01x faster                                                  |
| sqlglot_optimize           | 62.4 ms                                                  | 61.8 ms: 1.01x faster                                                   |
| hexiom                     | 7.13 ms                                                  | 7.07 ms: 1.01x faster                                                   |
| pprint_safe_repr           | 926 ms                                                   | 934 ms: 1.01x slower                                                    |
| xml_etree_iterparse        | 147 ms                                                   | 148 ms: 1.01x slower                                                    |
| asyncio_websockets         | 656 ms                                                   | 662 ms: 1.01x slower                                                    |
| coroutines                 | 28.2 ms                                                  | 28.5 ms: 1.01x slower                                                   |
| tomli_loads                | 2.53 sec                                                 | 2.56 sec: 1.01x slower                                                  |
| sympy_expand               | 455 ms                                                   | 461 ms: 1.01x slower                                                    |
| telco                      | 9.73 ms                                                  | 9.88 ms: 1.02x slower                                                   |
| pprint_pformat             | 1.90 sec                                                 | 1.93 sec: 1.02x slower                                                  |
| sympy_str                  | 264 ms                                                   | 268 ms: 1.02x slower                                                    |
| pyflate                    | 556 ms                                                   | 566 ms: 1.02x slower                                                    |
| json                       | 5.61 ms                                                  | 5.72 ms: 1.02x slower                                                   |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.23 sec: 1.02x slower                                                  |
| sympy_sum                  | 143 ms                                                   | 147 ms: 1.02x slower                                                    |
| sqlglot_parse              | 1.38 ms                                                  | 1.41 ms: 1.02x slower                                                   |
| asyncio_tcp                | 568 ms                                                   | 581 ms: 1.02x slower                                                    |
| fannkuch                   | 452 ms                                                   | 463 ms: 1.02x slower                                                    |
| thrift                     | 946 us                                                   | 975 us: 1.03x slower                                                    |
| json_loads                 | 31.4 us                                                  | 32.5 us: 1.03x slower                                                   |
| typing_runtime_protocols   | 192 us                                                   | 201 us: 1.05x slower                                                    |
| html5lib                   | 64.3 ms                                                  | 67.6 ms: 1.05x slower                                                   |
| docutils                   | 2.91 sec                                                 | 3.11 sec: 1.07x slower                                                  |
| create_gc_cycles           | 2.12 ms                                                  | 2.30 ms: 1.08x slower                                                   |
| gc_traversal               | 4.53 ms                                                  | 5.05 ms: 1.11x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (32): tornado_http, xml_etree_generate, async_tree_io, scimark_sor, logging_simple, pickle_pure_python, scimark_fft, django_template, meteor_contest, crypto_pyaes, richards, xml_etree_process, sqlglot_normalize, unpickle_pure_python, raytrace, pidigits, regex_effbot, regex_dna, mako, genshi_text, sqlglot_transpile, python_startup_no_site, comprehensions, xml_etree_parse, richards_super, nqueens, spectral_norm, genshi_xml, sympy_integrate, json_dumps, async_tree_io_tg, pylint
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 92.94% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x