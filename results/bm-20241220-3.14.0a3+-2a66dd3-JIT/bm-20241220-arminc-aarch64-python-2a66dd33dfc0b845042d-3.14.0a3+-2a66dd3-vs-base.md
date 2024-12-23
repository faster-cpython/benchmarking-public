# Results vs. base

- fork: python
- ref: 2a66dd33dfc0b845042d
- machine: linux-aarch64
- commit hash: 2a66dd3
- commit date: 2024-12-20
- overall geometric mean: 1.050x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20241220-3.14.0a3+-2a66dd3/bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json | results/bm-20241220-3.14.0a3+-2a66dd3-JIT/bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                                                              | 321 ms: 1.04x slower                                                                                                    |
| docutils       | 3.01 sec                                                                                                            | 3.26 sec: 1.08x slower                                                                                                  |
| html5lib       | 64.7 ms                                                                                                             | 71.4 ms: 1.10x slower                                                                                                   |
| sphinx         | 1.19 sec                                                                                                            | 1.27 sec: 1.07x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                               | 1.07x slower                                                                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | results/bm-20241220-3.14.0a3+-2a66dd3/bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json | results/bm-20241220-3.14.0a3+-2a66dd3-JIT/bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json |
|---------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed   | 686 ms                                                                                                              | 703 ms: 1.03x slower                                                                                                    |
| async_tree_io_tg          | 906 ms                                                                                                              | 935 ms: 1.03x slower                                                                                                    |
| async_tree_io             | 928 ms                                                                                                              | 962 ms: 1.04x slower                                                                                                    |
| async_tree_memoization_tg | 484 ms                                                                                                              | 502 ms: 1.04x slower                                                                                                    |
| async_tree_none           | 403 ms                                                                                                              | 428 ms: 1.06x slower                                                                                                    |
| async_generators          | 496 ms                                                                                                              | 543 ms: 1.09x slower                                                                                                    |
| Geometric mean            | (ref)                                                                                                               | 1.03x slower                                                                                                            |

Benchmark hidden because not significant (5): asyncio_websockets, async_tree_cpu_io_mixed_tg, coroutines, async_tree_none_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20241220-3.14.0a3+-2a66dd3/bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json | results/bm-20241220-3.14.0a3+-2a66dd3-JIT/bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 32.5 ms                                                                                                             | 31.3 ms: 1.04x faster                                                                                                   |
| regex_compile  | 127 ms                                                                                                              | 142 ms: 1.12x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.01x slower                                                                                                            |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark          | results/bm-20241220-3.14.0a3+-2a66dd3/bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json | results/bm-20241220-3.14.0a3+-2a66dd3-JIT/bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json |
|--------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| xml_etree_generate | 125 ms                                                                                                              | 113 ms: 1.10x faster                                                                                                    |
| tomli_loads        | 2.62 sec                                                                                                            | 2.54 sec: 1.03x faster                                                                                                  |
| Geometric mean     | (ref)                                                                                                               | 1.02x faster                                                                                                            |

Benchmark hidden because not significant (7): xml_etree_process, json_loads, unpickle_pure_python, xml_etree_iterparse, json_dumps, xml_etree_parse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20241220-3.14.0a3+-2a66dd3/bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json | results/bm-20241220-3.14.0a3+-2a66dd3-JIT/bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json |
|-----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| mako            | 14.3 ms                                                                                                             | 13.5 ms: 1.06x faster                                                                                                   |
| django_template | 41.5 ms                                                                                                             | 47.8 ms: 1.15x slower                                                                                                   |
| genshi_text     | 28.6 ms                                                                                                             | 33.1 ms: 1.16x slower                                                                                                   |
| genshi_xml      | 66.6 ms                                                                                                             | 83.4 ms: 1.25x slower                                                                                                   |
| Geometric mean  | (ref)                                                                                                               | 1.12x slower                                                                                                            |

All benchmarks:
===============

| Benchmark                 | results/bm-20241220-3.14.0a3+-2a66dd3/bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json | results/bm-20241220-3.14.0a3+-2a66dd3-JIT/bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json |
|---------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool             | 5.45 sec                                                                                                            | 1.37 sec: 3.98x faster                                                                                                  |
| xml_etree_generate        | 125 ms                                                                                                              | 113 ms: 1.10x faster                                                                                                    |
| deepcopy_memo             | 41.3 us                                                                                                             | 38.7 us: 1.07x faster                                                                                                   |
| mako                      | 14.3 ms                                                                                                             | 13.5 ms: 1.06x faster                                                                                                   |
| regex_v8                  | 32.5 ms                                                                                                             | 31.3 ms: 1.04x faster                                                                                                   |
| tomli_loads               | 2.62 sec                                                                                                            | 2.54 sec: 1.03x faster                                                                                                  |
| bpe_tokeniser             | 5.74 sec                                                                                                            | 5.78 sec: 1.01x slower                                                                                                  |
| shortest_path             | 573 ms                                                                                                              | 587 ms: 1.03x slower                                                                                                    |
| async_tree_cpu_io_mixed   | 686 ms                                                                                                              | 703 ms: 1.03x slower                                                                                                    |
| async_tree_io_tg          | 906 ms                                                                                                              | 935 ms: 1.03x slower                                                                                                    |
| async_tree_io             | 928 ms                                                                                                              | 962 ms: 1.04x slower                                                                                                    |
| async_tree_memoization_tg | 484 ms                                                                                                              | 502 ms: 1.04x slower                                                                                                    |
| k_core                    | 2.86 sec                                                                                                            | 2.96 sec: 1.04x slower                                                                                                  |
| mdp                       | 3.43 sec                                                                                                            | 3.57 sec: 1.04x slower                                                                                                  |
| mypy2                     | 1.04 sec                                                                                                            | 1.09 sec: 1.04x slower                                                                                                  |
| 2to3                      | 308 ms                                                                                                              | 321 ms: 1.04x slower                                                                                                    |
| sqlglot_parse             | 1.47 ms                                                                                                             | 1.55 ms: 1.05x slower                                                                                                   |
| async_tree_none           | 403 ms                                                                                                              | 428 ms: 1.06x slower                                                                                                    |
| spectral_norm             | 132 ms                                                                                                              | 141 ms: 1.06x slower                                                                                                    |
| fannkuch                  | 492 ms                                                                                                              | 524 ms: 1.07x slower                                                                                                    |
| sympy_expand              | 481 ms                                                                                                              | 514 ms: 1.07x slower                                                                                                    |
| sphinx                    | 1.19 sec                                                                                                            | 1.27 sec: 1.07x slower                                                                                                  |
| scimark_sparse_mat_mult   | 6.20 ms                                                                                                             | 6.63 ms: 1.07x slower                                                                                                   |
| docutils                  | 3.01 sec                                                                                                            | 3.26 sec: 1.08x slower                                                                                                  |
| scimark_lu                | 143 ms                                                                                                              | 155 ms: 1.08x slower                                                                                                    |
| deepcopy_reduce           | 3.61 us                                                                                                             | 3.93 us: 1.09x slower                                                                                                   |
| async_generators          | 496 ms                                                                                                              | 543 ms: 1.09x slower                                                                                                    |
| sqlalchemy_imperative     | 15.9 ms                                                                                                             | 17.4 ms: 1.09x slower                                                                                                   |
| logging_format            | 7.97 us                                                                                                             | 8.73 us: 1.10x slower                                                                                                   |
| sympy_integrate           | 22.4 ms                                                                                                             | 24.5 ms: 1.10x slower                                                                                                   |
| sqlglot_normalize         | 129 ms                                                                                                              | 142 ms: 1.10x slower                                                                                                    |
| meteor_contest            | 116 ms                                                                                                              | 128 ms: 1.10x slower                                                                                                    |
| html5lib                  | 64.7 ms                                                                                                             | 71.4 ms: 1.10x slower                                                                                                   |
| deltablue                 | 4.02 ms                                                                                                             | 4.44 ms: 1.11x slower                                                                                                   |
| logging_simple            | 7.17 us                                                                                                             | 7.93 us: 1.11x slower                                                                                                   |
| deepcopy                  | 346 us                                                                                                              | 385 us: 1.11x slower                                                                                                    |
| comprehensions            | 22.4 us                                                                                                             | 25.0 us: 1.11x slower                                                                                                   |
| many_optionals            | 707 us                                                                                                              | 787 us: 1.11x slower                                                                                                    |
| crypto_pyaes              | 83.6 ms                                                                                                             | 93.2 ms: 1.11x slower                                                                                                   |
| regex_compile             | 127 ms                                                                                                              | 142 ms: 1.12x slower                                                                                                    |
| sympy_str                 | 275 ms                                                                                                              | 311 ms: 1.13x slower                                                                                                    |
| raytrace                  | 327 ms                                                                                                              | 369 ms: 1.13x slower                                                                                                    |
| pycparser                 | 1.28 sec                                                                                                            | 1.46 sec: 1.14x slower                                                                                                  |
| django_template           | 41.5 ms                                                                                                             | 47.8 ms: 1.15x slower                                                                                                   |
| dulwich_log               | 62.3 ms                                                                                                             | 72.1 ms: 1.16x slower                                                                                                   |
| genshi_text               | 28.6 ms                                                                                                             | 33.1 ms: 1.16x slower                                                                                                   |
| sympy_sum                 | 146 ms                                                                                                              | 171 ms: 1.17x slower                                                                                                    |
| go                        | 144 ms                                                                                                              | 171 ms: 1.18x slower                                                                                                    |
| chaos                     | 72.7 ms                                                                                                             | 87.5 ms: 1.20x slower                                                                                                   |
| nqueens                   | 105 ms                                                                                                              | 129 ms: 1.22x slower                                                                                                    |
| genshi_xml                | 66.6 ms                                                                                                             | 83.4 ms: 1.25x slower                                                                                                   |
| hexiom                    | 7.51 ms                                                                                                             | 9.59 ms: 1.28x slower                                                                                                   |
| pprint_safe_repr          | 974 ms                                                                                                              | 1.26 sec: 1.29x slower                                                                                                  |
| pprint_pformat            | 2.02 sec                                                                                                            | 2.65 sec: 1.31x slower                                                                                                  |
| generators                | 37.1 ms                                                                                                             | 51.9 ms: 1.40x slower                                                                                                   |
| Geometric mean            | (ref)                                                                                                               | 1.04x slower                                                                                                            |

Benchmark hidden because not significant (43): nbody, float, scimark_monte_carlo, xml_etree_process, json_loads, sqlite_synth, regex_effbot, scimark_fft, regex_dna, pyflate, richards, asyncio_websockets, unpickle_pure_python, xml_etree_iterparse, json_dumps, xml_etree_parse, async_tree_cpu_io_mixed_tg, coverage, richards_super, connected_components, pathlib, python_startup, scimark_sor, pidigits, djangocms, coroutines, logging_silent, python_startup_no_site, json, pickle_pure_python, async_tree_none_tg, sqlglot_optimize, typing_runtime_protocols, async_tree_memoization, pylint, gc_traversal, telco, create_gc_cycles, sqlglot_transpile, subparsers, sqlalchemy_declarative, bench_thread_pool, thrift

- Geometric mean (including insignificant results): 1.050x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.02x