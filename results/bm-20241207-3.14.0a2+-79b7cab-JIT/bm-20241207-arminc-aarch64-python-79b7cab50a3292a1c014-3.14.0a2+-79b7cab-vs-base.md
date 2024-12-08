# Results vs. base

- fork: python
- ref: 79b7cab50a3292a1c014
- machine: linux-aarch64
- commit hash: 79b7cab
- commit date: 2024-12-07
- overall geometric mean: 1.054x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20241207-3.14.0a2+-79b7cab/bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json | results/bm-20241207-3.14.0a2+-79b7cab-JIT/bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| docutils       | 3.05 sec                                                                                                            | 3.20 sec: 1.05x slower                                                                                                  |
| html5lib       | 63.8 ms                                                                                                             | 72.9 ms: 1.14x slower                                                                                                   |
| sphinx         | 1.18 sec                                                                                                            | 1.26 sec: 1.07x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                               | 1.07x slower                                                                                                            |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | results/bm-20241207-3.14.0a2+-79b7cab/bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json | results/bm-20241207-3.14.0a2+-79b7cab-JIT/bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json |
|-------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| async_tree_io           | 917 ms                                                                                                              | 946 ms: 1.03x slower                                                                                                    |
| async_tree_cpu_io_mixed | 690 ms                                                                                                              | 719 ms: 1.04x slower                                                                                                    |
| async_tree_none         | 401 ms                                                                                                              | 423 ms: 1.05x slower                                                                                                    |
| Geometric mean          | (ref)                                                                                                               | 1.03x slower                                                                                                            |

Benchmark hidden because not significant (8): asyncio_websockets, async_tree_io_tg, coroutines, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_none_tg, async_generators, async_tree_memoization

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20241207-3.14.0a2+-79b7cab/bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json | results/bm-20241207-3.14.0a2+-79b7cab-JIT/bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 255 ms                                                                                                              | 264 ms: 1.04x slower                                                                                                    |
| regex_compile  | 128 ms                                                                                                              | 142 ms: 1.11x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.04x slower                                                                                                            |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark          | results/bm-20241207-3.14.0a2+-79b7cab/bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json | results/bm-20241207-3.14.0a2+-79b7cab-JIT/bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json |
|--------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| tomli_loads        | 2.76 sec                                                                                                            | 2.63 sec: 1.05x faster                                                                                                  |
| xml_etree_generate | 116 ms                                                                                                              | 111 ms: 1.04x faster                                                                                                    |
| pickle_pure_python | 386 us                                                                                                              | 408 us: 1.06x slower                                                                                                    |
| Geometric mean     | (ref)                                                                                                               | 1.01x faster                                                                                                            |

Benchmark hidden because not significant (6): xml_etree_process, xml_etree_parse, unpickle_pure_python, json_dumps, json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20241207-3.14.0a2+-79b7cab/bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json | results/bm-20241207-3.14.0a2+-79b7cab-JIT/bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json |
|-----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| genshi_text     | 29.4 ms                                                                                                             | 32.7 ms: 1.11x slower                                                                                                   |
| django_template | 40.5 ms                                                                                                             | 48.4 ms: 1.19x slower                                                                                                   |
| genshi_xml      | 63.3 ms                                                                                                             | 82.0 ms: 1.29x slower                                                                                                   |
| Geometric mean  | (ref)                                                                                                               | 1.14x slower                                                                                                            |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | results/bm-20241207-3.14.0a2+-79b7cab/bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json | results/bm-20241207-3.14.0a2+-79b7cab-JIT/bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json |
|--------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool            | 3.66 sec                                                                                                            | 1.46 sec: 2.52x faster                                                                                                  |
| tomli_loads              | 2.76 sec                                                                                                            | 2.63 sec: 1.05x faster                                                                                                  |
| telco                    | 10.00 ms                                                                                                            | 9.50 ms: 1.05x faster                                                                                                   |
| xml_etree_generate       | 116 ms                                                                                                              | 111 ms: 1.04x faster                                                                                                    |
| bpe_tokeniser            | 5.73 sec                                                                                                            | 5.86 sec: 1.02x slower                                                                                                  |
| async_tree_io            | 917 ms                                                                                                              | 946 ms: 1.03x slower                                                                                                    |
| regex_dna                | 255 ms                                                                                                              | 264 ms: 1.04x slower                                                                                                    |
| mdp                      | 3.44 sec                                                                                                            | 3.59 sec: 1.04x slower                                                                                                  |
| async_tree_cpu_io_mixed  | 690 ms                                                                                                              | 719 ms: 1.04x slower                                                                                                    |
| fannkuch                 | 490 ms                                                                                                              | 512 ms: 1.04x slower                                                                                                    |
| docutils                 | 3.05 sec                                                                                                            | 3.20 sec: 1.05x slower                                                                                                  |
| async_tree_none          | 401 ms                                                                                                              | 423 ms: 1.05x slower                                                                                                    |
| spectral_norm            | 146 ms                                                                                                              | 154 ms: 1.06x slower                                                                                                    |
| sqlalchemy_imperative    | 15.5 ms                                                                                                             | 16.4 ms: 1.06x slower                                                                                                   |
| pylint                   | 318 ms                                                                                                              | 336 ms: 1.06x slower                                                                                                    |
| pickle_pure_python       | 386 us                                                                                                              | 408 us: 1.06x slower                                                                                                    |
| thrift                   | 977 us                                                                                                              | 1.04 ms: 1.07x slower                                                                                                   |
| sphinx                   | 1.18 sec                                                                                                            | 1.26 sec: 1.07x slower                                                                                                  |
| subparsers               | 25.9 ms                                                                                                             | 27.7 ms: 1.07x slower                                                                                                   |
| typing_runtime_protocols | 205 us                                                                                                              | 220 us: 1.07x slower                                                                                                    |
| sqlglot_normalize        | 134 ms                                                                                                              | 145 ms: 1.08x slower                                                                                                    |
| logging_simple           | 7.24 us                                                                                                             | 7.90 us: 1.09x slower                                                                                                   |
| sympy_str                | 278 ms                                                                                                              | 304 ms: 1.09x slower                                                                                                    |
| sympy_integrate          | 21.9 ms                                                                                                             | 24.1 ms: 1.10x slower                                                                                                   |
| crypto_pyaes             | 85.2 ms                                                                                                             | 94.2 ms: 1.11x slower                                                                                                   |
| sqlglot_optimize         | 62.9 ms                                                                                                             | 69.7 ms: 1.11x slower                                                                                                   |
| sympy_expand             | 471 ms                                                                                                              | 523 ms: 1.11x slower                                                                                                    |
| genshi_text              | 29.4 ms                                                                                                             | 32.7 ms: 1.11x slower                                                                                                   |
| regex_compile            | 128 ms                                                                                                              | 142 ms: 1.11x slower                                                                                                    |
| scimark_lu               | 137 ms                                                                                                              | 153 ms: 1.11x slower                                                                                                    |
| deepcopy_reduce          | 3.62 us                                                                                                             | 4.05 us: 1.12x slower                                                                                                   |
| sqlglot_transpile        | 1.78 ms                                                                                                             | 2.00 ms: 1.12x slower                                                                                                   |
| raytrace                 | 321 ms                                                                                                              | 361 ms: 1.12x slower                                                                                                    |
| sqlglot_parse            | 1.45 ms                                                                                                             | 1.63 ms: 1.13x slower                                                                                                   |
| pycparser                | 1.23 sec                                                                                                            | 1.39 sec: 1.13x slower                                                                                                  |
| html5lib                 | 63.8 ms                                                                                                             | 72.9 ms: 1.14x slower                                                                                                   |
| dulwich_log              | 60.6 ms                                                                                                             | 69.6 ms: 1.15x slower                                                                                                   |
| logging_format           | 7.74 us                                                                                                             | 8.89 us: 1.15x slower                                                                                                   |
| deepcopy                 | 344 us                                                                                                              | 396 us: 1.15x slower                                                                                                    |
| sympy_sum                | 143 ms                                                                                                              | 166 ms: 1.16x slower                                                                                                    |
| chaos                    | 71.1 ms                                                                                                             | 84.1 ms: 1.18x slower                                                                                                   |
| django_template          | 40.5 ms                                                                                                             | 48.4 ms: 1.19x slower                                                                                                   |
| many_optionals           | 712 us                                                                                                              | 857 us: 1.20x slower                                                                                                    |
| comprehensions           | 21.0 us                                                                                                             | 25.3 us: 1.20x slower                                                                                                   |
| go                       | 144 ms                                                                                                              | 180 ms: 1.25x slower                                                                                                    |
| nqueens                  | 107 ms                                                                                                              | 134 ms: 1.25x slower                                                                                                    |
| hexiom                   | 7.25 ms                                                                                                             | 9.35 ms: 1.29x slower                                                                                                   |
| genshi_xml               | 63.3 ms                                                                                                             | 82.0 ms: 1.29x slower                                                                                                   |
| pprint_safe_repr         | 952 ms                                                                                                              | 1.27 sec: 1.34x slower                                                                                                  |
| pprint_pformat           | 1.95 sec                                                                                                            | 2.63 sec: 1.35x slower                                                                                                  |
| generators               | 36.6 ms                                                                                                             | 50.5 ms: 1.38x slower                                                                                                   |
| Geometric mean           | (ref)                                                                                                               | 1.05x slower                                                                                                            |

Benchmark hidden because not significant (46): pathlib, xml_etree_process, richards_super, mako, xml_etree_parse, gc_traversal, unpickle_pure_python, create_gc_cycles, json_dumps, sqlite_synth, float, nbody, json, regex_v8, scimark_fft, deepcopy_memo, k_core, scimark_sor, asyncio_websockets, shortest_path, regex_effbot, djangocms, pyflate, connected_components, json_loads, pidigits, async_tree_io_tg, python_startup_no_site, sqlalchemy_declarative, logging_silent, python_startup, coroutines, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, xml_etree_iterparse, async_tree_none_tg, richards, coverage, async_generators, async_tree_memoization, scimark_monte_carlo, bench_thread_pool, 2to3, deltablue, scimark_sparse_mat_mult, meteor_contest

- Geometric mean (including insignificant results): 1.054x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.01x