# Results vs. base

- fork: python
- ref: 328187cc4fcdd578db42
- machine: linux-aarch64
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.060x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20241130-3.14.0a2+-328187c/bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json | results/bm-20241130-3.14.0a2+-328187c-JIT/bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 304 ms                                                                                                              | 334 ms: 1.10x slower                                                                                                    |
| docutils       | 3.12 sec                                                                                                            | 3.39 sec: 1.09x slower                                                                                                  |
| html5lib       | 65.0 ms                                                                                                             | 70.9 ms: 1.09x slower                                                                                                   |
| sphinx         | 1.23 sec                                                                                                            | 1.34 sec: 1.09x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                               | 1.09x slower                                                                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | results/bm-20241130-3.14.0a2+-328187c/bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json | results/bm-20241130-3.14.0a2+-328187c-JIT/bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json |
|-------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 751 ms                                                                                                              | 772 ms: 1.03x slower                                                                                                    |
| async_tree_io           | 1.17 sec                                                                                                            | 1.21 sec: 1.03x slower                                                                                                  |
| async_tree_memoization  | 573 ms                                                                                                              | 598 ms: 1.04x slower                                                                                                    |
| async_generators        | 509 ms                                                                                                              | 538 ms: 1.06x slower                                                                                                    |
| async_tree_none         | 445 ms                                                                                                              | 471 ms: 1.06x slower                                                                                                    |
| Geometric mean          | (ref)                                                                                                               | 1.03x slower                                                                                                            |

Benchmark hidden because not significant (6): coroutines, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20241130-3.14.0a2+-328187c/bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json | results/bm-20241130-3.14.0a2+-328187c-JIT/bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 263 ms                                                                                                              | 246 ms: 1.07x faster                                                                                                    |
| regex_v8       | 32.7 ms                                                                                                             | 31.5 ms: 1.04x faster                                                                                                   |
| regex_compile  | 127 ms                                                                                                              | 151 ms: 1.19x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.02x slower                                                                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark      | results/bm-20241130-3.14.0a2+-328187c/bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json | results/bm-20241130-3.14.0a2+-328187c-JIT/bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| tomli_loads    | 2.74 sec                                                                                                            | 2.60 sec: 1.05x faster                                                                                                  |
| Geometric mean | (ref)                                                                                                               | 1.01x faster                                                                                                            |

Benchmark hidden because not significant (8): xml_etree_generate, xml_etree_parse, unpickle_pure_python, xml_etree_process, pickle_pure_python, json_loads, json_dumps, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20241130-3.14.0a2+-328187c/bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json | results/bm-20241130-3.14.0a2+-328187c-JIT/bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json |
|-----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| genshi_text     | 29.2 ms                                                                                                             | 32.3 ms: 1.11x slower                                                                                                   |
| django_template | 40.6 ms                                                                                                             | 47.5 ms: 1.17x slower                                                                                                   |
| genshi_xml      | 62.9 ms                                                                                                             | 79.5 ms: 1.26x slower                                                                                                   |
| Geometric mean  | (ref)                                                                                                               | 1.12x slower                                                                                                            |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | results/bm-20241130-3.14.0a2+-328187c/bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json | results/bm-20241130-3.14.0a2+-328187c-JIT/bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json |
|--------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool            | 5.89 sec                                                                                                            | 1.53 sec: 3.86x faster                                                                                                  |
| regex_dna                | 263 ms                                                                                                              | 246 ms: 1.07x faster                                                                                                    |
| logging_silent           | 143 ns                                                                                                              | 135 ns: 1.06x faster                                                                                                    |
| tomli_loads              | 2.74 sec                                                                                                            | 2.60 sec: 1.05x faster                                                                                                  |
| regex_v8                 | 32.7 ms                                                                                                             | 31.5 ms: 1.04x faster                                                                                                   |
| djangocms                | 67.2 us                                                                                                             | 66.1 us: 1.02x faster                                                                                                   |
| async_tree_cpu_io_mixed  | 751 ms                                                                                                              | 772 ms: 1.03x slower                                                                                                    |
| async_tree_io            | 1.17 sec                                                                                                            | 1.21 sec: 1.03x slower                                                                                                  |
| k_core                   | 3.55 sec                                                                                                            | 3.67 sec: 1.03x slower                                                                                                  |
| pyflate                  | 601 ms                                                                                                              | 625 ms: 1.04x slower                                                                                                    |
| shortest_path            | 562 ms                                                                                                              | 585 ms: 1.04x slower                                                                                                    |
| async_tree_memoization   | 573 ms                                                                                                              | 598 ms: 1.04x slower                                                                                                    |
| connected_components     | 539 ms                                                                                                              | 563 ms: 1.04x slower                                                                                                    |
| logging_format           | 7.78 us                                                                                                             | 8.14 us: 1.05x slower                                                                                                   |
| fannkuch                 | 486 ms                                                                                                              | 509 ms: 1.05x slower                                                                                                    |
| bench_thread_pool        | 1.31 ms                                                                                                             | 1.37 ms: 1.05x slower                                                                                                   |
| mdp                      | 3.42 sec                                                                                                            | 3.60 sec: 1.05x slower                                                                                                  |
| async_generators         | 509 ms                                                                                                              | 538 ms: 1.06x slower                                                                                                    |
| async_tree_none          | 445 ms                                                                                                              | 471 ms: 1.06x slower                                                                                                    |
| logging_simple           | 6.99 us                                                                                                             | 7.41 us: 1.06x slower                                                                                                   |
| sqlalchemy_imperative    | 16.7 ms                                                                                                             | 17.8 ms: 1.07x slower                                                                                                   |
| meteor_contest           | 116 ms                                                                                                              | 124 ms: 1.07x slower                                                                                                    |
| scimark_sparse_mat_mult  | 6.75 ms                                                                                                             | 7.28 ms: 1.08x slower                                                                                                   |
| docutils                 | 3.12 sec                                                                                                            | 3.39 sec: 1.09x slower                                                                                                  |
| crypto_pyaes             | 84.5 ms                                                                                                             | 91.9 ms: 1.09x slower                                                                                                   |
| sympy_integrate          | 22.1 ms                                                                                                             | 24.1 ms: 1.09x slower                                                                                                   |
| html5lib                 | 65.0 ms                                                                                                             | 70.9 ms: 1.09x slower                                                                                                   |
| sphinx                   | 1.23 sec                                                                                                            | 1.34 sec: 1.09x slower                                                                                                  |
| scimark_lu               | 138 ms                                                                                                              | 151 ms: 1.09x slower                                                                                                    |
| deepcopy                 | 354 us                                                                                                              | 389 us: 1.10x slower                                                                                                    |
| 2to3                     | 304 ms                                                                                                              | 334 ms: 1.10x slower                                                                                                    |
| typing_runtime_protocols | 206 us                                                                                                              | 228 us: 1.10x slower                                                                                                    |
| genshi_text              | 29.2 ms                                                                                                             | 32.3 ms: 1.11x slower                                                                                                   |
| raytrace                 | 323 ms                                                                                                              | 358 ms: 1.11x slower                                                                                                    |
| sqlalchemy_declarative   | 146 ms                                                                                                              | 163 ms: 1.11x slower                                                                                                    |
| sympy_expand             | 480 ms                                                                                                              | 536 ms: 1.12x slower                                                                                                    |
| sqlglot_transpile        | 1.84 ms                                                                                                             | 2.05 ms: 1.12x slower                                                                                                   |
| sympy_str                | 283 ms                                                                                                              | 317 ms: 1.12x slower                                                                                                    |
| sqlglot_optimize         | 63.0 ms                                                                                                             | 70.8 ms: 1.12x slower                                                                                                   |
| sqlglot_parse            | 1.47 ms                                                                                                             | 1.66 ms: 1.12x slower                                                                                                   |
| deepcopy_reduce          | 3.58 us                                                                                                             | 4.08 us: 1.14x slower                                                                                                   |
| pylint                   | 297 ms                                                                                                              | 342 ms: 1.15x slower                                                                                                    |
| chaos                    | 72.0 ms                                                                                                             | 84.2 ms: 1.17x slower                                                                                                   |
| comprehensions           | 21.8 us                                                                                                             | 25.5 us: 1.17x slower                                                                                                   |
| django_template          | 40.6 ms                                                                                                             | 47.5 ms: 1.17x slower                                                                                                   |
| pycparser                | 1.28 sec                                                                                                            | 1.50 sec: 1.17x slower                                                                                                  |
| dulwich_log              | 63.6 ms                                                                                                             | 75.1 ms: 1.18x slower                                                                                                   |
| sympy_sum                | 153 ms                                                                                                              | 182 ms: 1.19x slower                                                                                                    |
| regex_compile            | 127 ms                                                                                                              | 151 ms: 1.19x slower                                                                                                    |
| nqueens                  | 107 ms                                                                                                              | 129 ms: 1.21x slower                                                                                                    |
| many_optionals           | 719 us                                                                                                              | 873 us: 1.21x slower                                                                                                    |
| genshi_xml               | 62.9 ms                                                                                                             | 79.5 ms: 1.26x slower                                                                                                   |
| pprint_safe_repr         | 947 ms                                                                                                              | 1.24 sec: 1.31x slower                                                                                                  |
| pprint_pformat           | 1.96 sec                                                                                                            | 2.62 sec: 1.34x slower                                                                                                  |
| hexiom                   | 7.34 ms                                                                                                             | 9.84 ms: 1.34x slower                                                                                                   |
| go                       | 142 ms                                                                                                              | 196 ms: 1.38x slower                                                                                                    |
| generators               | 35.6 ms                                                                                                             | 49.8 ms: 1.40x slower                                                                                                   |
| Geometric mean           | (ref)                                                                                                               | 1.05x slower                                                                                                            |

Benchmark hidden because not significant (40): coverage, mako, sqlite_synth, xml_etree_generate, scimark_sor, scimark_fft, richards_super, richards, xml_etree_parse, pathlib, coroutines, unpickle_pure_python, nbody, xml_etree_process, float, scimark_monte_carlo, pidigits, pickle_pure_python, gc_traversal, asyncio_websockets, bpe_tokeniser, python_startup_no_site, python_startup, subparsers, json_loads, json_dumps, json, regex_effbot, xml_etree_iterparse, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, deltablue, telco, async_tree_none_tg, thrift, create_gc_cycles, sqlglot_normalize, spectral_norm, deepcopy_memo

- Geometric mean (including insignificant results): 1.060x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.02x