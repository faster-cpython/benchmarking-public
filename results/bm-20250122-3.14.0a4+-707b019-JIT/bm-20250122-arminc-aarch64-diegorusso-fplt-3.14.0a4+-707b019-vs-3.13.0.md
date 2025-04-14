# Results vs. 3.13.0

- fork: diegorusso
- ref: fplt
- machine: linux-aarch64
- commit hash: 707b019
- commit date: 2025-01-22
- overall geometric mean: 1.042x slower
- HPT reliability: 99.54%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250122-arminc-aarch64-diegorusso-fplt-3.14.0a4+-707b019 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 325 ms: 1.04x slower                                         |
| docutils       | 2.96 sec                                                 | 3.25 sec: 1.09x slower                                       |
| html5lib       | 65.6 ms                                                  | 73.4 ms: 1.12x slower                                        |
| sphinx         | 1.20 sec                                                 | 1.26 sec: 1.05x slower                                       |
| Geometric mean | (ref)                                                    | 1.08x slower                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250122-arminc-aarch64-diegorusso-fplt-3.14.0a4+-707b019 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 478 ms: 1.39x faster                                         |
| async_tree_memoization     | 664 ms                                                   | 500 ms: 1.33x faster                                         |
| async_tree_io_tg           | 1.16 sec                                                 | 908 ms: 1.28x faster                                         |
| async_tree_none            | 504 ms                                                   | 397 ms: 1.27x faster                                         |
| async_tree_io              | 1.14 sec                                                 | 905 ms: 1.26x faster                                         |
| async_tree_none_tg         | 484 ms                                                   | 390 ms: 1.24x faster                                         |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 669 ms: 1.20x faster                                         |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 685 ms: 1.15x faster                                         |
| Geometric mean             | (ref)                                                    | 1.19x faster                                                 |

Benchmark hidden because not significant (3): async_generators, coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250122-arminc-aarch64-diegorusso-fplt-3.14.0a4+-707b019 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 89.6 ms: 1.07x faster                                        |
| nbody          | 118 ms                                                   | 132 ms: 1.12x slower                                         |
| Geometric mean | (ref)                                                    | 1.02x slower                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250122-arminc-aarch64-diegorusso-fplt-3.14.0a4+-707b019 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.09 ms: 1.25x faster                                        |
| regex_compile  | 134 ms                                                   | 148 ms: 1.11x slower                                         |
| Geometric mean | (ref)                                                    | 1.03x faster                                                 |

Benchmark hidden because not significant (2): regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250122-arminc-aarch64-diegorusso-fplt-3.14.0a4+-707b019 |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| xml_etree_parse      | 203 ms                                                   | 179 ms: 1.13x faster                                         |
| xml_etree_iterparse  | 159 ms                                                   | 143 ms: 1.11x faster                                         |
| xml_etree_process    | 82.1 ms                                                  | 86.8 ms: 1.06x slower                                        |
| unpickle_pure_python | 265 us                                                   | 290 us: 1.09x slower                                         |
| pickle_pure_python   | 374 us                                                   | 430 us: 1.15x slower                                         |
| Geometric mean       | (ref)                                                    | 1.00x slower                                                 |

Benchmark hidden because not significant (4): xml_etree_generate, tomli_loads, json_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250122-arminc-aarch64-diegorusso-fplt-3.14.0a4+-707b019 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 9.04 ms: 1.03x slower                                        |
| Geometric mean         | (ref)                                                    | 1.02x slower                                                 |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250122-arminc-aarch64-diegorusso-fplt-3.14.0a4+-707b019 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_text     | 28.6 ms                                                  | 33.3 ms: 1.17x slower                                        |
| django_template | 39.4 ms                                                  | 49.5 ms: 1.26x slower                                        |
| genshi_xml      | 61.6 ms                                                  | 83.7 ms: 1.36x slower                                        |
| Geometric mean  | (ref)                                                    | 1.20x slower                                                 |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250122-arminc-aarch64-diegorusso-fplt-3.14.0a4+-707b019 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 478 ms: 1.39x faster                                         |
| async_tree_memoization     | 664 ms                                                   | 500 ms: 1.33x faster                                         |
| async_tree_io_tg           | 1.16 sec                                                 | 908 ms: 1.28x faster                                         |
| async_tree_none            | 504 ms                                                   | 397 ms: 1.27x faster                                         |
| async_tree_io              | 1.14 sec                                                 | 905 ms: 1.26x faster                                         |
| regex_effbot               | 5.10 ms                                                  | 4.09 ms: 1.25x faster                                        |
| async_tree_none_tg         | 484 ms                                                   | 390 ms: 1.24x faster                                         |
| deepcopy_memo              | 53.0 us                                                  | 42.8 us: 1.24x faster                                        |
| deepcopy                   | 479 us                                                   | 388 us: 1.23x faster                                         |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 669 ms: 1.20x faster                                         |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 685 ms: 1.15x faster                                         |
| xml_etree_parse            | 203 ms                                                   | 179 ms: 1.13x faster                                         |
| xml_etree_iterparse        | 159 ms                                                   | 143 ms: 1.11x faster                                         |
| float                      | 95.8 ms                                                  | 89.6 ms: 1.07x faster                                        |
| pathlib                    | 24.3 ms                                                  | 22.9 ms: 1.06x faster                                        |
| deepcopy_reduce            | 4.24 us                                                  | 4.05 us: 1.05x faster                                        |
| bpe_tokeniser              | 6.02 sec                                                 | 5.94 sec: 1.01x faster                                       |
| connected_components       | 547 ms                                                   | 561 ms: 1.03x slower                                         |
| python_startup_no_site     | 8.79 ms                                                  | 9.04 ms: 1.03x slower                                        |
| shortest_path              | 565 ms                                                   | 583 ms: 1.03x slower                                         |
| mdp                        | 3.45 sec                                                 | 3.56 sec: 1.03x slower                                       |
| 2to3                       | 313 ms                                                   | 325 ms: 1.04x slower                                         |
| pyflate                    | 582 ms                                                   | 607 ms: 1.04x slower                                         |
| sphinx                     | 1.20 sec                                                 | 1.26 sec: 1.05x slower                                       |
| xml_etree_process          | 82.1 ms                                                  | 86.8 ms: 1.06x slower                                        |
| meteor_contest             | 117 ms                                                   | 124 ms: 1.06x slower                                         |
| deltablue                  | 3.97 ms                                                  | 4.23 ms: 1.07x slower                                        |
| sqlglot_optimize           | 65.2 ms                                                  | 70.0 ms: 1.07x slower                                        |
| sympy_sum                  | 151 ms                                                   | 163 ms: 1.08x slower                                         |
| scimark_monte_carlo        | 87.8 ms                                                  | 94.8 ms: 1.08x slower                                        |
| create_gc_cycles           | 3.39 ms                                                  | 3.69 ms: 1.09x slower                                        |
| sqlglot_normalize          | 131 ms                                                   | 143 ms: 1.09x slower                                         |
| unpickle_pure_python       | 265 us                                                   | 290 us: 1.09x slower                                         |
| docutils                   | 2.96 sec                                                 | 3.25 sec: 1.09x slower                                       |
| sympy_expand               | 472 ms                                                   | 518 ms: 1.10x slower                                         |
| scimark_lu                 | 146 ms                                                   | 162 ms: 1.11x slower                                         |
| regex_compile              | 134 ms                                                   | 148 ms: 1.11x slower                                         |
| fannkuch                   | 478 ms                                                   | 532 ms: 1.11x slower                                         |
| nbody                      | 118 ms                                                   | 132 ms: 1.12x slower                                         |
| html5lib                   | 65.6 ms                                                  | 73.4 ms: 1.12x slower                                        |
| logging_format             | 8.10 us                                                  | 9.07 us: 1.12x slower                                        |
| logging_silent             | 135 ns                                                   | 151 ns: 1.12x slower                                         |
| crypto_pyaes               | 84.9 ms                                                  | 95.5 ms: 1.12x slower                                        |
| sympy_integrate            | 21.4 ms                                                  | 24.1 ms: 1.13x slower                                        |
| go                         | 164 ms                                                   | 186 ms: 1.13x slower                                         |
| raytrace                   | 310 ms                                                   | 352 ms: 1.13x slower                                         |
| logging_simple             | 7.25 us                                                  | 8.25 us: 1.14x slower                                        |
| sqlglot_parse              | 1.43 ms                                                  | 1.63 ms: 1.14x slower                                        |
| typing_runtime_protocols   | 197 us                                                   | 225 us: 1.14x slower                                         |
| sympy_str                  | 265 ms                                                   | 303 ms: 1.14x slower                                         |
| pickle_pure_python         | 374 us                                                   | 430 us: 1.15x slower                                         |
| richards_super             | 60.8 ms                                                  | 70.2 ms: 1.15x slower                                        |
| pycparser                  | 1.34 sec                                                 | 1.56 sec: 1.16x slower                                       |
| genshi_text                | 28.6 ms                                                  | 33.3 ms: 1.17x slower                                        |
| gc_traversal               | 5.92 ms                                                  | 6.95 ms: 1.17x slower                                        |
| comprehensions             | 20.8 us                                                  | 25.4 us: 1.22x slower                                        |
| nqueens                    | 105 ms                                                   | 129 ms: 1.23x slower                                         |
| chaos                      | 70.7 ms                                                  | 88.2 ms: 1.25x slower                                        |
| django_template            | 39.4 ms                                                  | 49.5 ms: 1.26x slower                                        |
| many_optionals             | 626 us                                                   | 845 us: 1.35x slower                                         |
| hexiom                     | 7.34 ms                                                  | 9.92 ms: 1.35x slower                                        |
| pprint_pformat             | 1.99 sec                                                 | 2.69 sec: 1.35x slower                                       |
| genshi_xml                 | 61.6 ms                                                  | 83.7 ms: 1.36x slower                                        |
| subparsers                 | 20.3 ms                                                  | 28.1 ms: 1.38x slower                                        |
| richards                   | 54.5 ms                                                  | 76.4 ms: 1.40x slower                                        |
| pprint_safe_repr           | 962 ms                                                   | 1.35 sec: 1.40x slower                                       |
| generators                 | 40.3 ms                                                  | 56.7 ms: 1.41x slower                                        |
| bench_mp_pool              | 8.07 ms                                                  | 1.36 sec: 168.39x slower                                     |
| Geometric mean             | (ref)                                                    | 1.10x slower                                                 |

Benchmark hidden because not significant (27): xml_etree_generate, scimark_sor, telco, async_generators, regex_dna, sqlalchemy_declarative, scimark_fft, k_core, coverage, tomli_loads, sqlite_synth, pylint, coroutines, asyncio_websockets, regex_v8, json_loads, spectral_norm, thrift, json, json_dumps, python_startup, pidigits, bench_thread_pool, mako, scimark_sparse_mat_mult, sqlalchemy_imperative, sqlglot_transpile
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20250122-3.14.0a4+-707b019-JIT/bm-20250122-arminc-aarch64-diegorusso-fplt-3.14.0a4+-707b019.json: dulwich_log

- Geometric mean (including insignificant results): 1.042x slower

# HPT report

- Reliability score: 99.54% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.04x