# Results vs. 3.13.0

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: linux-aarch64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.043x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| sphinx         | 1.20 sec                                                 | 1.16 sec: 1.03x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                             |

Benchmark hidden because not significant (3): 2to3, docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 481 ms: 1.38x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 505 ms: 1.31x faster                                                     |
| async_tree_none            | 504 ms                                                   | 402 ms: 1.25x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 931 ms: 1.25x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 924 ms: 1.23x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 395 ms: 1.23x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 671 ms: 1.19x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 694 ms: 1.14x faster                                                     |
| async_generators           | 500 ms                                                   | 450 ms: 1.11x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.19x faster                                                             |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 88.2 ms: 1.09x faster                                                    |
| Geometric mean | (ref)                                                    | 1.02x faster                                                             |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.06 ms: 1.26x faster                                                    |
| regex_dna      | 263 ms                                                   | 247 ms: 1.07x faster                                                     |
| Geometric mean | (ref)                                                    | 1.08x faster                                                             |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 182 ms: 1.11x faster                                                     |
| xml_etree_iterparse | 159 ms                                                   | 147 ms: 1.08x faster                                                     |
| tomli_loads         | 2.67 sec                                                 | 2.58 sec: 1.03x faster                                                   |
| pickle_pure_python  | 374 us                                                   | 398 us: 1.06x slower                                                     |
| Geometric mean      | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (5): xml_etree_process, xml_etree_generate, unpickle_pure_python, json_dumps, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 9.05 ms: 1.03x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.03x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, genshi_xml, django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                   | 479 us                                                   | 344 us: 1.39x faster                                                     |
| async_tree_memoization_tg  | 663 ms                                                   | 481 ms: 1.38x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 505 ms: 1.31x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 41.7 us: 1.27x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 4.06 ms: 1.26x faster                                                    |
| async_tree_none            | 504 ms                                                   | 402 ms: 1.25x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 931 ms: 1.25x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 924 ms: 1.23x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 395 ms: 1.23x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 671 ms: 1.19x faster                                                     |
| spectral_norm              | 143 ms                                                   | 123 ms: 1.17x faster                                                     |
| pathlib                    | 24.3 ms                                                  | 21.1 ms: 1.15x faster                                                    |
| go                         | 164 ms                                                   | 144 ms: 1.14x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 694 ms: 1.14x faster                                                     |
| xml_etree_parse            | 203 ms                                                   | 182 ms: 1.11x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.82 us: 1.11x faster                                                    |
| async_generators           | 500 ms                                                   | 450 ms: 1.11x faster                                                     |
| scimark_fft                | 463 ms                                                   | 419 ms: 1.10x faster                                                     |
| telco                      | 10.5 ms                                                  | 9.52 ms: 1.10x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.52 sec: 1.09x faster                                                   |
| float                      | 95.8 ms                                                  | 88.2 ms: 1.09x faster                                                    |
| xml_etree_iterparse        | 159 ms                                                   | 147 ms: 1.08x faster                                                     |
| scimark_sor                | 164 ms                                                   | 152 ms: 1.08x faster                                                     |
| pylint                     | 345 ms                                                   | 322 ms: 1.07x faster                                                     |
| regex_dna                  | 263 ms                                                   | 247 ms: 1.07x faster                                                     |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 6.27 ms: 1.06x faster                                                    |
| sqlglot_optimize           | 65.2 ms                                                  | 61.7 ms: 1.06x faster                                                    |
| pycparser                  | 1.34 sec                                                 | 1.27 sec: 1.06x faster                                                   |
| coverage                   | 106 ms                                                   | 100 ms: 1.06x faster                                                     |
| scimark_lu                 | 146 ms                                                   | 139 ms: 1.05x faster                                                     |
| k_core                     | 2.99 sec                                                 | 2.88 sec: 1.04x faster                                                   |
| tomli_loads                | 2.67 sec                                                 | 2.58 sec: 1.03x faster                                                   |
| sphinx                     | 1.20 sec                                                 | 1.16 sec: 1.03x faster                                                   |
| typing_runtime_protocols   | 197 us                                                   | 193 us: 1.02x faster                                                     |
| mdp                        | 3.45 sec                                                 | 3.39 sec: 1.02x faster                                                   |
| python_startup_no_site     | 8.79 ms                                                  | 9.05 ms: 1.03x slower                                                    |
| pickle_pure_python         | 374 us                                                   | 398 us: 1.06x slower                                                     |
| create_gc_cycles           | 3.39 ms                                                  | 3.65 ms: 1.08x slower                                                    |
| gc_traversal               | 5.92 ms                                                  | 6.50 ms: 1.10x slower                                                    |
| many_optionals             | 626 us                                                   | 706 us: 1.13x slower                                                     |
| subparsers                 | 20.3 ms                                                  | 25.4 ms: 1.25x slower                                                    |
| bench_mp_pool              | 8.07 ms                                                  | 5.94 sec: 736.76x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.03x slower                                                             |

Benchmark hidden because not significant (53): generators, regex_compile, sqlalchemy_imperative, genshi_text, nqueens, 2to3, bench_thread_pool, sqlalchemy_declarative, chaos, richards, thrift, deltablue, pyflate, richards_super, xml_etree_process, meteor_contest, xml_etree_generate, unpickle_pure_python, scimark_monte_carlo, sympy_sum, logging_format, sqlglot_transpile, asyncio_websockets, pidigits, fannkuch, sqlglot_normalize, docutils, sqlite_synth, coroutines, pprint_pformat, sympy_integrate, hexiom, html5lib, shortest_path, sympy_expand, logging_silent, connected_components, sympy_str, sqlglot_parse, genshi_xml, json, django_template, raytrace, logging_simple, comprehensions, python_startup, pprint_safe_repr, regex_v8, nbody, mako, json_dumps, crypto_pyaes, json_loads
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (9) of results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.043x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.02x