# Results vs. 3.13.0

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: linux-aarch64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.039x faster
- HPT reliability: 96.42%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.07 sec: 1.03x slower                                                  |
| html5lib       | 65.6 ms                                                  | 62.7 ms: 1.05x faster                                                   |
| sphinx         | 1.20 sec                                                 | 1.16 sec: 1.03x faster                                                  |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 474 ms: 1.40x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 479 ms: 1.39x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 381 ms: 1.27x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 901 ms: 1.26x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 922 ms: 1.26x faster                                                    |
| async_tree_none            | 504 ms                                                   | 401 ms: 1.26x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 663 ms: 1.21x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 669 ms: 1.18x faster                                                    |
| async_generators           | 500 ms                                                   | 488 ms: 1.02x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.20x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 83.6 ms: 1.15x faster                                                   |
| Geometric mean | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.84 ms: 1.33x faster                                                   |
| regex_v8       | 32.5 ms                                                  | 27.8 ms: 1.17x faster                                                   |
| regex_dna      | 263 ms                                                   | 233 ms: 1.13x faster                                                    |
| regex_compile  | 134 ms                                                   | 122 ms: 1.10x faster                                                    |
| Geometric mean | (ref)                                                    | 1.18x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads         | 2.67 sec                                                 | 2.35 sec: 1.13x faster                                                  |
| xml_etree_iterparse | 159 ms                                                   | 145 ms: 1.10x faster                                                    |
| xml_etree_parse     | 203 ms                                                   | 185 ms: 1.09x faster                                                    |
| json_dumps          | 14.2 ms                                                  | 13.4 ms: 1.06x faster                                                   |
| pickle_pure_python  | 374 us                                                   | 393 us: 1.05x slower                                                    |
| Geometric mean      | (ref)                                                    | 1.05x faster                                                            |

Benchmark hidden because not significant (4): xml_etree_generate, unpickle_pure_python, xml_etree_process, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 16.0 ms                                                  | 15.2 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 14.0 ms                                                  | 13.2 ms: 1.06x faster                                                   |
| genshi_xml     | 61.6 ms                                                  | 63.1 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.68 sec: 2.05x faster                                                  |
| deepcopy                   | 479 us                                                   | 329 us: 1.45x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 474 ms: 1.40x faster                                                    |
| deepcopy_memo              | 53.0 us                                                  | 38.1 us: 1.39x faster                                                   |
| async_tree_memoization     | 664 ms                                                   | 479 ms: 1.39x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 3.84 ms: 1.33x faster                                                   |
| async_tree_none_tg         | 484 ms                                                   | 381 ms: 1.27x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 901 ms: 1.26x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 922 ms: 1.26x faster                                                    |
| async_tree_none            | 504 ms                                                   | 401 ms: 1.26x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 663 ms: 1.21x faster                                                    |
| richards                   | 54.5 ms                                                  | 45.8 ms: 1.19x faster                                                   |
| richards_super             | 60.8 ms                                                  | 51.4 ms: 1.18x faster                                                   |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 669 ms: 1.18x faster                                                    |
| regex_v8                   | 32.5 ms                                                  | 27.8 ms: 1.17x faster                                                   |
| deepcopy_reduce            | 4.24 us                                                  | 3.65 us: 1.16x faster                                                   |
| float                      | 95.8 ms                                                  | 83.6 ms: 1.15x faster                                                   |
| tomli_loads                | 2.67 sec                                                 | 2.35 sec: 1.13x faster                                                  |
| regex_dna                  | 263 ms                                                   | 233 ms: 1.13x faster                                                    |
| scimark_sor                | 164 ms                                                   | 147 ms: 1.12x faster                                                    |
| pathlib                    | 24.3 ms                                                  | 22.1 ms: 1.10x faster                                                   |
| bpe_tokeniser              | 6.02 sec                                                 | 5.47 sec: 1.10x faster                                                  |
| regex_compile              | 134 ms                                                   | 122 ms: 1.10x faster                                                    |
| xml_etree_iterparse        | 159 ms                                                   | 145 ms: 1.10x faster                                                    |
| xml_etree_parse            | 203 ms                                                   | 185 ms: 1.09x faster                                                    |
| scimark_fft                | 463 ms                                                   | 423 ms: 1.09x faster                                                    |
| pyflate                    | 582 ms                                                   | 532 ms: 1.09x faster                                                    |
| pylint                     | 345 ms                                                   | 318 ms: 1.09x faster                                                    |
| telco                      | 10.5 ms                                                  | 9.64 ms: 1.08x faster                                                   |
| generators                 | 40.3 ms                                                  | 37.4 ms: 1.08x faster                                                   |
| scimark_monte_carlo        | 87.8 ms                                                  | 81.4 ms: 1.08x faster                                                   |
| spectral_norm              | 143 ms                                                   | 134 ms: 1.07x faster                                                    |
| sqlite_synth               | 4.08 us                                                  | 3.83 us: 1.07x faster                                                   |
| json_dumps                 | 14.2 ms                                                  | 13.4 ms: 1.06x faster                                                   |
| mako                       | 14.0 ms                                                  | 13.2 ms: 1.06x faster                                                   |
| python_startup             | 16.0 ms                                                  | 15.2 ms: 1.05x faster                                                   |
| k_core                     | 2.99 sec                                                 | 2.86 sec: 1.05x faster                                                  |
| html5lib                   | 65.6 ms                                                  | 62.7 ms: 1.05x faster                                                   |
| sphinx                     | 1.20 sec                                                 | 1.16 sec: 1.03x faster                                                  |
| async_generators           | 500 ms                                                   | 488 ms: 1.02x faster                                                    |
| genshi_xml                 | 61.6 ms                                                  | 63.1 ms: 1.02x slower                                                   |
| docutils                   | 2.96 sec                                                 | 3.07 sec: 1.03x slower                                                  |
| hexiom                     | 7.34 ms                                                  | 7.60 ms: 1.04x slower                                                   |
| sympy_expand               | 472 ms                                                   | 490 ms: 1.04x slower                                                    |
| logging_simple             | 7.25 us                                                  | 7.55 us: 1.04x slower                                                   |
| shortest_path              | 565 ms                                                   | 591 ms: 1.05x slower                                                    |
| logging_format             | 8.10 us                                                  | 8.49 us: 1.05x slower                                                   |
| pickle_pure_python         | 374 us                                                   | 393 us: 1.05x slower                                                    |
| connected_components       | 547 ms                                                   | 577 ms: 1.05x slower                                                    |
| sympy_str                  | 265 ms                                                   | 281 ms: 1.06x slower                                                    |
| typing_runtime_protocols   | 197 us                                                   | 210 us: 1.07x slower                                                    |
| comprehensions             | 20.8 us                                                  | 22.3 us: 1.07x slower                                                   |
| crypto_pyaes               | 84.9 ms                                                  | 91.8 ms: 1.08x slower                                                   |
| raytrace                   | 310 ms                                                   | 336 ms: 1.08x slower                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 3.84 ms: 1.13x slower                                                   |
| gc_traversal               | 5.92 ms                                                  | 6.82 ms: 1.15x slower                                                   |
| pprint_pformat             | 1.99 sec                                                 | 2.56 sec: 1.29x slower                                                  |
| pprint_safe_repr           | 962 ms                                                   | 1.25 sec: 1.30x slower                                                  |
| subparsers                 | 20.3 ms                                                  | 28.4 ms: 1.40x slower                                                   |
| many_optionals             | 626 us                                                   | 901 us: 1.44x slower                                                    |
| logging_silent             | 135 ns                                                   | 625 ns: 4.64x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (27): xml_etree_generate, thrift, unpickle_pure_python, genshi_text, coverage, sympy_integrate, xml_etree_process, json, chaos, deltablue, go, djangocms, python_startup_no_site, asyncio_websockets, sympy_sum, 2to3, pidigits, nqueens, json_loads, nbody, meteor_contest, django_template, pycparser, coroutines, fannkuch, scimark_lu, scimark_sparse_mat_mult
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.039x faster

# HPT report

- Reliability score: 96.42% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x