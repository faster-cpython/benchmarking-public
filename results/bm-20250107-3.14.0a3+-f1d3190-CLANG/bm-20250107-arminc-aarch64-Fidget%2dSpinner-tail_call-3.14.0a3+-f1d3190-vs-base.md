# Results vs. base

- fork: Fidget-Spinner
- ref: tail_call
- machine: linux-aarch64
- commit hash: f1d3190
- commit date: 2025-01-07
- overall geometric mean: 1.092x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250105-arminc-aarch64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 324 ms                                                                   | 293 ms: 1.11x faster                                                    |
| docutils       | 3.12 sec                                                                 | 3.01 sec: 1.04x faster                                                  |
| html5lib       | 68.5 ms                                                                  | 60.6 ms: 1.13x faster                                                   |
| sphinx         | 1.22 sec                                                                 | 1.16 sec: 1.05x faster                                                  |
| Geometric mean | (ref)                                                                    | 1.08x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250105-arminc-aarch64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_generators           | 519 ms                                                                   | 465 ms: 1.12x faster                                                    |
| async_tree_io              | 947 ms                                                                   | 869 ms: 1.09x faster                                                    |
| async_tree_none            | 409 ms                                                                   | 377 ms: 1.09x faster                                                    |
| async_tree_memoization_tg  | 483 ms                                                                   | 446 ms: 1.08x faster                                                    |
| async_tree_none_tg         | 391 ms                                                                   | 361 ms: 1.08x faster                                                    |
| async_tree_io_tg           | 914 ms                                                                   | 848 ms: 1.08x faster                                                    |
| async_tree_memoization     | 507 ms                                                                   | 472 ms: 1.07x faster                                                    |
| coroutines                 | 30.4 ms                                                                  | 29.0 ms: 1.05x faster                                                   |
| async_tree_cpu_io_mixed    | 762 ms                                                                   | 728 ms: 1.05x faster                                                    |
| async_tree_cpu_io_mixed_tg | 755 ms                                                                   | 722 ms: 1.05x faster                                                    |
| Geometric mean             | (ref)                                                                    | 1.07x faster                                                            |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250105-arminc-aarch64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 132 ms                                                                   | 109 ms: 1.21x faster                                                    |
| float          | 93.8 ms                                                                  | 83.8 ms: 1.12x faster                                                   |
| Geometric mean | (ref)                                                                    | 1.11x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250105-arminc-aarch64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 143 ms                                                                   | 127 ms: 1.12x faster                                                    |
| regex_dna      | 240 ms                                                                   | 265 ms: 1.10x slower                                                    |
| Geometric mean | (ref)                                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250105-arminc-aarch64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 304 us                                                                   | 248 us: 1.23x faster                                                    |
| tomli_loads          | 2.90 sec                                                                 | 2.41 sec: 1.21x faster                                                  |
| xml_etree_generate   | 119 ms                                                                   | 107 ms: 1.12x faster                                                    |
| xml_etree_process    | 85.9 ms                                                                  | 78.3 ms: 1.10x faster                                                   |
| pickle_pure_python   | 428 us                                                                   | 399 us: 1.07x faster                                                    |
| xml_etree_iterparse  | 160 ms                                                                   | 152 ms: 1.05x faster                                                    |
| Geometric mean       | (ref)                                                                    | 1.09x faster                                                            |

Benchmark hidden because not significant (3): json_loads, xml_etree_parse, json_dumps

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250105-arminc-aarch64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|-----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 71.2 ms                                                                  | 60.1 ms: 1.18x faster                                                   |
| genshi_text     | 32.0 ms                                                                  | 27.2 ms: 1.18x faster                                                   |
| django_template | 44.2 ms                                                                  | 38.8 ms: 1.14x faster                                                   |
| mako            | 15.2 ms                                                                  | 14.2 ms: 1.07x faster                                                   |
| Geometric mean  | (ref)                                                                    | 1.14x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20250105-arminc-aarch64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-arminc-aarch64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| scimark_sor                | 173 ms                                                                   | 138 ms: 1.26x faster                                                    |
| generators                 | 44.9 ms                                                                  | 35.8 ms: 1.25x faster                                                   |
| scimark_monte_carlo        | 93.5 ms                                                                  | 74.7 ms: 1.25x faster                                                   |
| go                         | 163 ms                                                                   | 131 ms: 1.24x faster                                                    |
| scimark_lu                 | 156 ms                                                                   | 127 ms: 1.23x faster                                                    |
| unpickle_pure_python       | 304 us                                                                   | 248 us: 1.23x faster                                                    |
| deltablue                  | 4.65 ms                                                                  | 3.80 ms: 1.22x faster                                                   |
| deepcopy_memo              | 45.1 us                                                                  | 36.9 us: 1.22x faster                                                   |
| nbody                      | 132 ms                                                                   | 109 ms: 1.21x faster                                                    |
| sqlglot_parse              | 1.59 ms                                                                  | 1.31 ms: 1.21x faster                                                   |
| chaos                      | 78.3 ms                                                                  | 65.0 ms: 1.21x faster                                                   |
| tomli_loads                | 2.90 sec                                                                 | 2.41 sec: 1.21x faster                                                  |
| fannkuch                   | 571 ms                                                                   | 482 ms: 1.18x faster                                                    |
| genshi_xml                 | 71.2 ms                                                                  | 60.1 ms: 1.18x faster                                                   |
| genshi_text                | 32.0 ms                                                                  | 27.2 ms: 1.18x faster                                                   |
| sqlglot_transpile          | 2.01 ms                                                                  | 1.72 ms: 1.17x faster                                                   |
| richards_super             | 63.5 ms                                                                  | 54.4 ms: 1.17x faster                                                   |
| logging_silent             | 138 ns                                                                   | 118 ns: 1.16x faster                                                    |
| sqlglot_normalize          | 144 ms                                                                   | 124 ms: 1.16x faster                                                    |
| comprehensions             | 23.3 us                                                                  | 20.0 us: 1.16x faster                                                   |
| hexiom                     | 8.34 ms                                                                  | 7.20 ms: 1.16x faster                                                   |
| richards                   | 57.3 ms                                                                  | 49.4 ms: 1.16x faster                                                   |
| logging_simple             | 7.77 us                                                                  | 6.71 us: 1.16x faster                                                   |
| logging_format             | 8.63 us                                                                  | 7.48 us: 1.15x faster                                                   |
| deepcopy                   | 363 us                                                                   | 315 us: 1.15x faster                                                    |
| deepcopy_reduce            | 3.92 us                                                                  | 3.41 us: 1.15x faster                                                   |
| spectral_norm              | 124 ms                                                                   | 109 ms: 1.14x faster                                                    |
| raytrace                   | 344 ms                                                                   | 302 ms: 1.14x faster                                                    |
| django_template            | 44.2 ms                                                                  | 38.8 ms: 1.14x faster                                                   |
| pprint_safe_repr           | 1.10 sec                                                                 | 971 ms: 1.13x faster                                                    |
| html5lib                   | 68.5 ms                                                                  | 60.6 ms: 1.13x faster                                                   |
| scimark_fft                | 410 ms                                                                   | 363 ms: 1.13x faster                                                    |
| pylint                     | 337 ms                                                                   | 299 ms: 1.13x faster                                                    |
| sympy_str                  | 293 ms                                                                   | 261 ms: 1.13x faster                                                    |
| pprint_pformat             | 2.22 sec                                                                 | 1.97 sec: 1.12x faster                                                  |
| regex_compile              | 143 ms                                                                   | 127 ms: 1.12x faster                                                    |
| pyflate                    | 598 ms                                                                   | 533 ms: 1.12x faster                                                    |
| float                      | 93.8 ms                                                                  | 83.8 ms: 1.12x faster                                                   |
| async_generators           | 519 ms                                                                   | 465 ms: 1.12x faster                                                    |
| xml_etree_generate         | 119 ms                                                                   | 107 ms: 1.12x faster                                                    |
| meteor_contest             | 130 ms                                                                   | 117 ms: 1.11x faster                                                    |
| 2to3                       | 324 ms                                                                   | 293 ms: 1.11x faster                                                    |
| telco                      | 10.1 ms                                                                  | 9.18 ms: 1.10x faster                                                   |
| sqlglot_optimize           | 69.3 ms                                                                  | 62.8 ms: 1.10x faster                                                   |
| pycparser                  | 1.37 sec                                                                 | 1.24 sec: 1.10x faster                                                  |
| sympy_sum                  | 158 ms                                                                   | 144 ms: 1.10x faster                                                    |
| xml_etree_process          | 85.9 ms                                                                  | 78.3 ms: 1.10x faster                                                   |
| nqueens                    | 110 ms                                                                   | 101 ms: 1.09x faster                                                    |
| sympy_expand               | 504 ms                                                                   | 462 ms: 1.09x faster                                                    |
| many_optionals             | 784 us                                                                   | 718 us: 1.09x faster                                                    |
| async_tree_io              | 947 ms                                                                   | 869 ms: 1.09x faster                                                    |
| async_tree_none            | 409 ms                                                                   | 377 ms: 1.09x faster                                                    |
| thrift                     | 1.03 ms                                                                  | 955 us: 1.08x faster                                                    |
| async_tree_memoization_tg  | 483 ms                                                                   | 446 ms: 1.08x faster                                                    |
| async_tree_none_tg         | 391 ms                                                                   | 361 ms: 1.08x faster                                                    |
| crypto_pyaes               | 94.0 ms                                                                  | 87.1 ms: 1.08x faster                                                   |
| async_tree_io_tg           | 914 ms                                                                   | 848 ms: 1.08x faster                                                    |
| async_tree_memoization     | 507 ms                                                                   | 472 ms: 1.07x faster                                                    |
| pickle_pure_python         | 428 us                                                                   | 399 us: 1.07x faster                                                    |
| bench_thread_pool          | 1.37 ms                                                                  | 1.28 ms: 1.07x faster                                                   |
| bpe_tokeniser              | 5.91 sec                                                                 | 5.52 sec: 1.07x faster                                                  |
| mako                       | 15.2 ms                                                                  | 14.2 ms: 1.07x faster                                                   |
| sympy_integrate            | 21.8 ms                                                                  | 20.7 ms: 1.05x faster                                                   |
| xml_etree_iterparse        | 160 ms                                                                   | 152 ms: 1.05x faster                                                    |
| coroutines                 | 30.4 ms                                                                  | 29.0 ms: 1.05x faster                                                   |
| sphinx                     | 1.22 sec                                                                 | 1.16 sec: 1.05x faster                                                  |
| async_tree_cpu_io_mixed    | 762 ms                                                                   | 728 ms: 1.05x faster                                                    |
| async_tree_cpu_io_mixed_tg | 755 ms                                                                   | 722 ms: 1.05x faster                                                    |
| typing_runtime_protocols   | 207 us                                                                   | 199 us: 1.04x faster                                                    |
| docutils                   | 3.12 sec                                                                 | 3.01 sec: 1.04x faster                                                  |
| mdp                        | 3.37 sec                                                                 | 3.27 sec: 1.03x faster                                                  |
| connected_components       | 554 ms                                                                   | 538 ms: 1.03x faster                                                    |
| regex_dna                  | 240 ms                                                                   | 265 ms: 1.10x slower                                                    |
| Geometric mean             | (ref)                                                                    | 1.10x faster                                                            |

Benchmark hidden because not significant (23): bench_mp_pool, sqlalchemy_imperative, pathlib, dulwich_log, sqlite_synth, subparsers, json_loads, sqlalchemy_declarative, coverage, scimark_sparse_mat_mult, shortest_path, python_startup, json, k_core, xml_etree_parse, regex_v8, json_dumps, python_startup_no_site, pidigits, asyncio_websockets, gc_traversal, create_gc_cycles, regex_effbot

- Geometric mean (including insignificant results): 1.092x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.00x