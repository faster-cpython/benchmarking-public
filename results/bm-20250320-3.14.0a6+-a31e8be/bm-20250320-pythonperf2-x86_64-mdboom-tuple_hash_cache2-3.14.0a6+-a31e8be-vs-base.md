# Results vs. base

- fork: mdboom
- ref: tuple_hash_cache2
- machine: linux-x86_64
- commit hash: a31e8be
- commit date: 2025-03-20
- overall geometric mean: 1.000x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250319-pythonperf2-x86_64-python-6146295a5b8e9286ccb8-3.14.0a6+-6146295 | bm-20250320-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-a31e8be |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 284 ms                                                                       | 288 ms: 1.01x slower                                                      |
| html5lib       | 69.5 ms                                                                      | 70.4 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                              |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250319-pythonperf2-x86_64-python-6146295a5b8e9286ccb8-3.14.0a6+-6146295 | bm-20250320-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-a31e8be |
|----------------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| coroutines                 | 21.0 ms                                                                      | 21.1 ms: 1.00x slower                                                     |
| asyncio_websockets         | 384 ms                                                                       | 388 ms: 1.01x slower                                                      |
| async_tree_cpu_io_mixed    | 520 ms                                                                       | 528 ms: 1.01x slower                                                      |
| async_tree_io              | 641 ms                                                                       | 660 ms: 1.03x slower                                                      |
| async_tree_cpu_io_mixed_tg | 506 ms                                                                       | 521 ms: 1.03x slower                                                      |
| async_tree_memoization     | 348 ms                                                                       | 359 ms: 1.03x slower                                                      |
| async_tree_io_tg           | 646 ms                                                                       | 668 ms: 1.03x slower                                                      |
| async_tree_none            | 289 ms                                                                       | 299 ms: 1.03x slower                                                      |
| async_tree_none_tg         | 273 ms                                                                       | 284 ms: 1.04x slower                                                      |
| async_tree_memoization_tg  | 339 ms                                                                       | 359 ms: 1.06x slower                                                      |
| Geometric mean             | (ref)                                                                        | 1.03x slower                                                              |

Benchmark hidden because not significant (1): async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250319-pythonperf2-x86_64-python-6146295a5b8e9286ccb8-3.14.0a6+-6146295 | bm-20250320-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-a31e8be |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 106 ms                                                                       | 103 ms: 1.04x faster                                                      |
| float          | 72.3 ms                                                                      | 71.9 ms: 1.01x faster                                                     |
| pidigits       | 255 ms                                                                       | 254 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                                        | 1.01x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250319-pythonperf2-x86_64-python-6146295a5b8e9286ccb8-3.14.0a6+-6146295 | bm-20250320-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-a31e8be |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 25.2 ms                                                                      | 24.0 ms: 1.05x faster                                                     |
| regex_dna      | 237 ms                                                                       | 237 ms: 1.00x faster                                                      |
| regex_effbot   | 3.00 ms                                                                      | 3.01 ms: 1.00x slower                                                     |
| Geometric mean | (ref)                                                                        | 1.01x faster                                                              |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250319-pythonperf2-x86_64-python-6146295a5b8e9286ccb8-3.14.0a6+-6146295 | bm-20250320-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-a31e8be |
|---------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_loads          | 26.4 us                                                                      | 26.3 us: 1.00x faster                                                     |
| json_dumps          | 11.6 ms                                                                      | 11.6 ms: 1.00x faster                                                     |
| pickle_pure_python  | 338 us                                                                       | 340 us: 1.01x slower                                                      |
| xml_etree_iterparse | 97.9 ms                                                                      | 98.8 ms: 1.01x slower                                                     |
| xml_etree_process   | 60.6 ms                                                                      | 61.4 ms: 1.01x slower                                                     |
| xml_etree_generate  | 84.7 ms                                                                      | 86.7 ms: 1.02x slower                                                     |
| Geometric mean      | (ref)                                                                        | 1.01x slower                                                              |

Benchmark hidden because not significant (3): unpickle_pure_python, tomli_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250319-pythonperf2-x86_64-python-6146295a5b8e9286ccb8-3.14.0a6+-6146295 | bm-20250320-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-a31e8be |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup | 16.4 ms                                                                      | 16.4 ms: 1.00x slower                                                     |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                              |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250319-pythonperf2-x86_64-python-6146295a5b8e9286ccb8-3.14.0a6+-6146295 | bm-20250320-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-a31e8be |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_xml     | 56.9 ms                                                                      | 55.8 ms: 1.02x faster                                                     |
| genshi_text    | 24.4 ms                                                                      | 25.0 ms: 1.03x slower                                                     |
| mako           | 11.0 ms                                                                      | 11.2 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                              |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20250319-pythonperf2-x86_64-python-6146295a5b8e9286ccb8-3.14.0a6+-6146295 | bm-20250320-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-a31e8be |
|----------------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mdp                        | 2.51 sec                                                                     | 1.34 sec: 1.87x faster                                                    |
| regex_v8                   | 25.2 ms                                                                      | 24.0 ms: 1.05x faster                                                     |
| richards                   | 49.2 ms                                                                      | 47.2 ms: 1.04x faster                                                     |
| richards_super             | 55.5 ms                                                                      | 53.4 ms: 1.04x faster                                                     |
| nbody                      | 106 ms                                                                       | 103 ms: 1.04x faster                                                      |
| gc_traversal               | 6.54 ms                                                                      | 6.38 ms: 1.03x faster                                                     |
| scimark_sparse_mat_mult    | 4.83 ms                                                                      | 4.72 ms: 1.02x faster                                                     |
| genshi_xml                 | 56.9 ms                                                                      | 55.8 ms: 1.02x faster                                                     |
| crypto_pyaes               | 83.0 ms                                                                      | 81.5 ms: 1.02x faster                                                     |
| generators                 | 29.0 ms                                                                      | 28.5 ms: 1.02x faster                                                     |
| coverage                   | 80.2 ms                                                                      | 78.8 ms: 1.02x faster                                                     |
| hexiom                     | 6.53 ms                                                                      | 6.45 ms: 1.01x faster                                                     |
| shortest_path              | 459 ms                                                                       | 454 ms: 1.01x faster                                                      |
| fannkuch                   | 393 ms                                                                       | 388 ms: 1.01x faster                                                      |
| float                      | 72.3 ms                                                                      | 71.9 ms: 1.01x faster                                                     |
| pprint_safe_repr           | 843 ms                                                                       | 838 ms: 1.01x faster                                                      |
| json_loads                 | 26.4 us                                                                      | 26.3 us: 1.00x faster                                                     |
| pprint_pformat             | 1.70 sec                                                                     | 1.69 sec: 1.00x faster                                                    |
| json_dumps                 | 11.6 ms                                                                      | 11.6 ms: 1.00x faster                                                     |
| pidigits                   | 255 ms                                                                       | 254 ms: 1.00x faster                                                      |
| regex_dna                  | 237 ms                                                                       | 237 ms: 1.00x faster                                                      |
| regex_effbot               | 3.00 ms                                                                      | 3.01 ms: 1.00x slower                                                     |
| bpe_tokeniser              | 4.86 sec                                                                     | 4.87 sec: 1.00x slower                                                    |
| python_startup             | 16.4 ms                                                                      | 16.4 ms: 1.00x slower                                                     |
| coroutines                 | 21.0 ms                                                                      | 21.1 ms: 1.00x slower                                                     |
| deepcopy                   | 286 us                                                                       | 289 us: 1.01x slower                                                      |
| scimark_sor                | 111 ms                                                                       | 111 ms: 1.01x slower                                                      |
| deepcopy_reduce            | 2.97 us                                                                      | 3.00 us: 1.01x slower                                                     |
| connected_components       | 431 ms                                                                       | 434 ms: 1.01x slower                                                      |
| pickle_pure_python         | 338 us                                                                       | 340 us: 1.01x slower                                                      |
| spectral_norm              | 90.8 ms                                                                      | 91.6 ms: 1.01x slower                                                     |
| chaos                      | 65.3 ms                                                                      | 65.9 ms: 1.01x slower                                                     |
| nqueens                    | 95.8 ms                                                                      | 96.7 ms: 1.01x slower                                                     |
| xml_etree_iterparse        | 97.9 ms                                                                      | 98.8 ms: 1.01x slower                                                     |
| asyncio_websockets         | 384 ms                                                                       | 388 ms: 1.01x slower                                                      |
| sqlite_synth               | 2.83 us                                                                      | 2.86 us: 1.01x slower                                                     |
| html5lib                   | 69.5 ms                                                                      | 70.4 ms: 1.01x slower                                                     |
| meteor_contest             | 129 ms                                                                       | 130 ms: 1.01x slower                                                      |
| 2to3                       | 284 ms                                                                       | 288 ms: 1.01x slower                                                      |
| many_optionals             | 1.03 ms                                                                      | 1.04 ms: 1.01x slower                                                     |
| xml_etree_process          | 60.6 ms                                                                      | 61.4 ms: 1.01x slower                                                     |
| dulwich_log                | 62.3 ms                                                                      | 63.2 ms: 1.01x slower                                                     |
| typing_runtime_protocols   | 174 us                                                                       | 176 us: 1.01x slower                                                      |
| async_tree_cpu_io_mixed    | 520 ms                                                                       | 528 ms: 1.01x slower                                                      |
| logging_format             | 7.20 us                                                                      | 7.31 us: 1.01x slower                                                     |
| go                         | 131 ms                                                                       | 133 ms: 1.02x slower                                                      |
| sqlglot_v2_optimize        | 58.9 ms                                                                      | 59.9 ms: 1.02x slower                                                     |
| sqlalchemy_declarative     | 145 ms                                                                       | 148 ms: 1.02x slower                                                      |
| sqlalchemy_imperative      | 18.0 ms                                                                      | 18.3 ms: 1.02x slower                                                     |
| subparsers                 | 23.1 ms                                                                      | 23.5 ms: 1.02x slower                                                     |
| sqlglot_v2_normalize       | 119 ms                                                                       | 121 ms: 1.02x slower                                                      |
| pathlib                    | 17.0 ms                                                                      | 17.4 ms: 1.02x slower                                                     |
| json                       | 5.39 ms                                                                      | 5.50 ms: 1.02x slower                                                     |
| xml_etree_generate         | 84.7 ms                                                                      | 86.7 ms: 1.02x slower                                                     |
| genshi_text                | 24.4 ms                                                                      | 25.0 ms: 1.03x slower                                                     |
| mako                       | 11.0 ms                                                                      | 11.2 ms: 1.03x slower                                                     |
| deepcopy_memo              | 29.6 us                                                                      | 30.4 us: 1.03x slower                                                     |
| sqlglot_v2_transpile       | 1.78 ms                                                                      | 1.83 ms: 1.03x slower                                                     |
| sqlglot_v2_parse           | 1.41 ms                                                                      | 1.45 ms: 1.03x slower                                                     |
| async_tree_io              | 641 ms                                                                       | 660 ms: 1.03x slower                                                      |
| async_tree_cpu_io_mixed_tg | 506 ms                                                                       | 521 ms: 1.03x slower                                                      |
| async_tree_memoization     | 348 ms                                                                       | 359 ms: 1.03x slower                                                      |
| scimark_lu                 | 99.9 ms                                                                      | 103 ms: 1.03x slower                                                      |
| async_tree_io_tg           | 646 ms                                                                       | 668 ms: 1.03x slower                                                      |
| async_tree_none            | 289 ms                                                                       | 299 ms: 1.03x slower                                                      |
| raytrace                   | 290 ms                                                                       | 301 ms: 1.04x slower                                                      |
| pycparser                  | 1.25 sec                                                                     | 1.30 sec: 1.04x slower                                                    |
| scimark_fft                | 312 ms                                                                       | 324 ms: 1.04x slower                                                      |
| async_tree_none_tg         | 273 ms                                                                       | 284 ms: 1.04x slower                                                      |
| pyflate                    | 445 ms                                                                       | 464 ms: 1.04x slower                                                      |
| async_tree_memoization_tg  | 339 ms                                                                       | 359 ms: 1.06x slower                                                      |
| Geometric mean             | (ref)                                                                        | 1.00x slower                                                              |

Benchmark hidden because not significant (20): bench_mp_pool, deltablue, unpickle_pure_python, tomli_loads, async_generators, bench_thread_pool, docutils, regex_compile, k_core, logging_silent, scimark_monte_carlo, create_gc_cycles, python_startup_no_site, comprehensions, telco, django_template, xml_etree_parse, sphinx, logging_simple, pylint
Ignored benchmarks (5) of results/bm-20250319-3.14.0a6+-6146295/bm-20250319-pythonperf2-x86_64-python-6146295a5b8e9286ccb8-3.14.0a6+-6146295.json: sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift

- Geometric mean (including insignificant results): 1.000x faster

# HPT report

- Reliability score: 99.97% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x