# Results vs. 3.13.0

- fork: brandtbucher
- ref: warmup_side_4096
- machine: linux-aarch64
- commit hash: a8a4ed3
- commit date: 2024-11-22
- overall geometric mean: 1.055x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-arminc-aarch64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 315 ms: 1.04x slower                                                       |
| docutils       | 2.89 sec                                                 | 3.24 sec: 1.12x slower                                                     |
| html5lib       | 66.4 ms                                                  | 72.3 ms: 1.09x slower                                                      |
| sphinx         | 1.17 sec                                                 | 1.30 sec: 1.11x slower                                                     |
| Geometric mean | (ref)                                                    | 1.09x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-arminc-aarch64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|---------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg | 649 ms                                                   | 573 ms: 1.13x faster                                                       |
| async_tree_memoization    | 651 ms                                                   | 598 ms: 1.09x faster                                                       |
| async_tree_none           | 497 ms                                                   | 469 ms: 1.06x faster                                                       |
| async_tree_io             | 1.11 sec                                                 | 1.21 sec: 1.09x slower                                                     |
| async_generators          | 489 ms                                                   | 539 ms: 1.10x slower                                                       |
| async_tree_io_tg          | 1.13 sec                                                 | 1.27 sec: 1.12x slower                                                     |
| Geometric mean            | (ref)                                                    | 1.01x slower                                                               |

Benchmark hidden because not significant (5): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_none_tg, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-arminc-aarch64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 93.3 ms                                                  | 98.4 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                    | 1.04x slower                                                               |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-arminc-aarch64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 4.89 ms                                                  | 4.22 ms: 1.16x faster                                                      |
| regex_dna      | 253 ms                                                   | 270 ms: 1.07x slower                                                       |
| regex_compile  | 127 ms                                                   | 141 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                    | 1.02x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-arminc-aarch64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_generate   | 113 ms                                                   | 111 ms: 1.02x faster                                                       |
| tomli_loads          | 2.54 sec                                                 | 2.64 sec: 1.04x slower                                                     |
| unpickle_pure_python | 251 us                                                   | 271 us: 1.08x slower                                                       |
| json_dumps           | 13.6 ms                                                  | 14.7 ms: 1.08x slower                                                      |
| pickle_pure_python   | 357 us                                                   | 392 us: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                    | 1.03x slower                                                               |

Benchmark hidden because not significant (4): xml_etree_process, xml_etree_iterparse, json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-arminc-aarch64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 16.3 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                    | 1.04x slower                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-arminc-aarch64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|-----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 41.6 ms                                                  | 48.7 ms: 1.17x slower                                                      |
| genshi_text     | 27.7 ms                                                  | 32.7 ms: 1.18x slower                                                      |
| genshi_xml      | 60.3 ms                                                  | 81.0 ms: 1.34x slower                                                      |
| Geometric mean  | (ref)                                                    | 1.17x slower                                                               |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-arminc-aarch64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|---------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo             | 50.4 us                                                  | 41.0 us: 1.23x faster                                                      |
| regex_effbot              | 4.89 ms                                                  | 4.22 ms: 1.16x faster                                                      |
| async_tree_memoization_tg | 649 ms                                                   | 573 ms: 1.13x faster                                                       |
| deepcopy                  | 447 us                                                   | 397 us: 1.13x faster                                                       |
| async_tree_memoization    | 651 ms                                                   | 598 ms: 1.09x faster                                                       |
| pylint                    | 342 ms                                                   | 318 ms: 1.07x faster                                                       |
| async_tree_none           | 497 ms                                                   | 469 ms: 1.06x faster                                                       |
| xml_etree_generate        | 113 ms                                                   | 111 ms: 1.02x faster                                                       |
| pathlib                   | 22.7 ms                                                  | 22.3 ms: 1.02x faster                                                      |
| shortest_path             | 565 ms                                                   | 585 ms: 1.04x slower                                                       |
| 2to3                      | 304 ms                                                   | 315 ms: 1.04x slower                                                       |
| tomli_loads               | 2.54 sec                                                 | 2.64 sec: 1.04x slower                                                     |
| connected_components      | 533 ms                                                   | 556 ms: 1.04x slower                                                       |
| scimark_monte_carlo       | 83.6 ms                                                  | 87.9 ms: 1.05x slower                                                      |
| richards                  | 53.6 ms                                                  | 56.4 ms: 1.05x slower                                                      |
| float                     | 93.3 ms                                                  | 98.4 ms: 1.05x slower                                                      |
| python_startup            | 15.4 ms                                                  | 16.3 ms: 1.06x slower                                                      |
| crypto_pyaes              | 83.7 ms                                                  | 88.7 ms: 1.06x slower                                                      |
| mdp                       | 3.34 sec                                                 | 3.56 sec: 1.07x slower                                                     |
| regex_dna                 | 253 ms                                                   | 270 ms: 1.07x slower                                                       |
| fannkuch                  | 461 ms                                                   | 494 ms: 1.07x slower                                                       |
| deltablue                 | 3.82 ms                                                  | 4.11 ms: 1.08x slower                                                      |
| bench_thread_pool         | 1.27 ms                                                  | 1.37 ms: 1.08x slower                                                      |
| unpickle_pure_python      | 251 us                                                   | 271 us: 1.08x slower                                                       |
| spectral_norm             | 143 ms                                                   | 154 ms: 1.08x slower                                                       |
| json_dumps                | 13.6 ms                                                  | 14.7 ms: 1.08x slower                                                      |
| pyflate                   | 556 ms                                                   | 603 ms: 1.08x slower                                                       |
| html5lib                  | 66.4 ms                                                  | 72.3 ms: 1.09x slower                                                      |
| logging_format            | 7.82 us                                                  | 8.52 us: 1.09x slower                                                      |
| scimark_sparse_mat_mult   | 6.51 ms                                                  | 7.11 ms: 1.09x slower                                                      |
| async_tree_io             | 1.11 sec                                                 | 1.21 sec: 1.09x slower                                                     |
| scimark_lu                | 139 ms                                                   | 153 ms: 1.09x slower                                                       |
| pickle_pure_python        | 357 us                                                   | 392 us: 1.10x slower                                                       |
| async_generators          | 489 ms                                                   | 539 ms: 1.10x slower                                                       |
| typing_runtime_protocols  | 193 us                                                   | 214 us: 1.10x slower                                                       |
| regex_compile             | 127 ms                                                   | 141 ms: 1.11x slower                                                       |
| meteor_contest            | 114 ms                                                   | 126 ms: 1.11x slower                                                       |
| sympy_sum                 | 144 ms                                                   | 159 ms: 1.11x slower                                                       |
| gc_traversal              | 5.77 ms                                                  | 6.42 ms: 1.11x slower                                                      |
| sqlalchemy_imperative     | 15.1 ms                                                  | 16.9 ms: 1.11x slower                                                      |
| sphinx                    | 1.17 sec                                                 | 1.30 sec: 1.11x slower                                                     |
| sqlglot_optimize          | 62.2 ms                                                  | 69.3 ms: 1.11x slower                                                      |
| sqlglot_normalize         | 127 ms                                                   | 141 ms: 1.12x slower                                                       |
| create_gc_cycles          | 3.35 ms                                                  | 3.74 ms: 1.12x slower                                                      |
| docutils                  | 2.89 sec                                                 | 3.24 sec: 1.12x slower                                                     |
| async_tree_io_tg          | 1.13 sec                                                 | 1.27 sec: 1.12x slower                                                     |
| logging_simple            | 7.07 us                                                  | 7.97 us: 1.13x slower                                                      |
| sympy_expand              | 457 ms                                                   | 516 ms: 1.13x slower                                                       |
| sympy_str                 | 264 ms                                                   | 300 ms: 1.14x slower                                                       |
| go                        | 160 ms                                                   | 183 ms: 1.14x slower                                                       |
| sqlglot_transpile         | 1.73 ms                                                  | 1.98 ms: 1.14x slower                                                      |
| pycparser                 | 1.27 sec                                                 | 1.46 sec: 1.15x slower                                                     |
| sympy_integrate           | 20.8 ms                                                  | 24.0 ms: 1.15x slower                                                      |
| django_template           | 41.6 ms                                                  | 48.7 ms: 1.17x slower                                                      |
| sqlglot_parse             | 1.38 ms                                                  | 1.61 ms: 1.17x slower                                                      |
| genshi_text               | 27.7 ms                                                  | 32.7 ms: 1.18x slower                                                      |
| raytrace                  | 300 ms                                                   | 361 ms: 1.21x slower                                                       |
| comprehensions            | 20.4 us                                                  | 25.0 us: 1.23x slower                                                      |
| k_core                    | 2.96 sec                                                 | 3.68 sec: 1.24x slower                                                     |
| chaos                     | 68.0 ms                                                  | 85.2 ms: 1.25x slower                                                      |
| hexiom                    | 7.11 ms                                                  | 9.22 ms: 1.30x slower                                                      |
| nqueens                   | 100 ms                                                   | 132 ms: 1.32x slower                                                       |
| generators                | 37.6 ms                                                  | 50.4 ms: 1.34x slower                                                      |
| genshi_xml                | 60.3 ms                                                  | 81.0 ms: 1.34x slower                                                      |
| pprint_safe_repr          | 926 ms                                                   | 1.27 sec: 1.37x slower                                                     |
| pprint_pformat            | 1.90 sec                                                 | 2.64 sec: 1.39x slower                                                     |
| bench_mp_pool             | 7.68 ms                                                  | 2.26 sec: 294.10x slower                                                   |
| Geometric mean            | (ref)                                                    | 1.14x slower                                                               |

Benchmark hidden because not significant (25): xml_etree_process, sqlalchemy_declarative, richards_super, deepcopy_reduce, telco, async_tree_cpu_io_mixed, scimark_sor, bpe_tokeniser, xml_etree_iterparse, async_tree_cpu_io_mixed_tg, asyncio_websockets, scimark_fft, json, python_startup_no_site, json_loads, mako, async_tree_none_tg, nbody, xml_etree_parse, thrift, coverage, pidigits, coroutines, regex_v8, logging_silent
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (5) of results/bm-20241122-3.14.0a2+-a8a4ed3-JIT/bm-20241122-arminc-aarch64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3.json: djangocms, dulwich_log, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.055x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.03x