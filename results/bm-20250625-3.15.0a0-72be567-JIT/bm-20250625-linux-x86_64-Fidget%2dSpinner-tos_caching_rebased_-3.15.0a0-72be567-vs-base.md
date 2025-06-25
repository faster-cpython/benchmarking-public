# Results vs. base

- fork: Fidget-Spinner
- ref: tos_caching_rebased_
- machine: linux-x86_64
- commit hash: 72be567
- commit date: 2025-06-25
- overall geometric mean: 1.002x faster
- HPT reliability: 98.58%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250624-linux-x86_64-python-fea5ccc55d8486300beb-3.15.0a0-fea5ccc | bm-20250625-linux-x86_64-Fidget%2dSpinner-tos_caching_rebased_-3.15.0a0-72be567 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| docutils       | 2.63 sec                                                              | 2.65 sec: 1.01x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250624-linux-x86_64-python-fea5ccc55d8486300beb-3.15.0a0-fea5ccc | bm-20250625-linux-x86_64-Fidget%2dSpinner-tos_caching_rebased_-3.15.0a0-72be567 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 502 ms                                                                | 493 ms: 1.02x faster                                                            |
| coroutines                 | 24.9 ms                                                               | 24.6 ms: 1.01x faster                                                           |
| async_tree_cpu_io_mixed_tg | 492 ms                                                                | 487 ms: 1.01x faster                                                            |
| async_generators           | 434 ms                                                                | 431 ms: 1.01x faster                                                            |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (7): async_tree_memoization_tg, async_tree_io, async_tree_io_tg, async_tree_none, asyncio_websockets, async_tree_none_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250624-linux-x86_64-python-fea5ccc55d8486300beb-3.15.0a0-fea5ccc | bm-20250625-linux-x86_64-Fidget%2dSpinner-tos_caching_rebased_-3.15.0a0-72be567 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 97.5 ms                                                               | 90.2 ms: 1.08x faster                                                           |
| float          | 66.2 ms                                                               | 65.3 ms: 1.01x faster                                                           |
| pidigits       | 188 ms                                                                | 188 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250624-linux-x86_64-python-fea5ccc55d8486300beb-3.15.0a0-fea5ccc | bm-20250625-linux-x86_64-Fidget%2dSpinner-tos_caching_rebased_-3.15.0a0-72be567 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                                | 127 ms: 1.00x faster                                                            |
| regex_effbot   | 3.17 ms                                                               | 3.32 ms: 1.04x slower                                                           |
| regex_v8       | 22.1 ms                                                               | 23.4 ms: 1.06x slower                                                           |
| regex_dna      | 200 ms                                                                | 214 ms: 1.07x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250624-linux-x86_64-python-fea5ccc55d8486300beb-3.15.0a0-fea5ccc | bm-20250625-linux-x86_64-Fidget%2dSpinner-tos_caching_rebased_-3.15.0a0-72be567 |
|---------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python  | 323 us                                                                | 320 us: 1.01x faster                                                            |
| xml_etree_process   | 56.2 ms                                                               | 55.7 ms: 1.01x faster                                                           |
| json_dumps          | 11.1 ms                                                               | 11.0 ms: 1.01x faster                                                           |
| xml_etree_generate  | 80.3 ms                                                               | 80.8 ms: 1.01x slower                                                           |
| xml_etree_iterparse | 98.7 ms                                                               | 99.5 ms: 1.01x slower                                                           |
| tomli_loads         | 1.82 sec                                                              | 1.84 sec: 1.01x slower                                                          |
| json_loads          | 28.1 us                                                               | 28.8 us: 1.03x slower                                                           |
| Geometric mean      | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (2): unpickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250624-linux-x86_64-python-fea5ccc55d8486300beb-3.15.0a0-fea5ccc | bm-20250625-linux-x86_64-Fidget%2dSpinner-tos_caching_rebased_-3.15.0a0-72be567 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 12.2 ms                                                               | 12.1 ms: 1.00x faster                                                           |
| python_startup_no_site | 6.95 ms                                                               | 6.93 ms: 1.00x faster                                                           |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250624-linux-x86_64-python-fea5ccc55d8486300beb-3.15.0a0-fea5ccc | bm-20250625-linux-x86_64-Fidget%2dSpinner-tos_caching_rebased_-3.15.0a0-72be567 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.0 ms                                                               | 10.6 ms: 1.03x faster                                                           |
| genshi_xml      | 51.4 ms                                                               | 49.8 ms: 1.03x faster                                                           |
| genshi_text     | 21.7 ms                                                               | 21.4 ms: 1.01x faster                                                           |
| django_template | 32.6 ms                                                               | 32.2 ms: 1.01x faster                                                           |
| Geometric mean  | (ref)                                                                 | 1.02x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20250624-linux-x86_64-python-fea5ccc55d8486300beb-3.15.0a0-fea5ccc | bm-20250625-linux-x86_64-Fidget%2dSpinner-tos_caching_rebased_-3.15.0a0-72be567 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody                      | 97.5 ms                                                               | 90.2 ms: 1.08x faster                                                           |
| mako                       | 11.0 ms                                                               | 10.6 ms: 1.03x faster                                                           |
| genshi_xml                 | 51.4 ms                                                               | 49.8 ms: 1.03x faster                                                           |
| pyflate                    | 420 ms                                                                | 407 ms: 1.03x faster                                                            |
| fannkuch                   | 403 ms                                                                | 393 ms: 1.03x faster                                                            |
| shortest_path              | 504 ms                                                                | 493 ms: 1.02x faster                                                            |
| crypto_pyaes               | 76.8 ms                                                               | 75.3 ms: 1.02x faster                                                           |
| deepcopy_reduce            | 2.78 us                                                               | 2.73 us: 1.02x faster                                                           |
| pprint_pformat             | 1.70 sec                                                              | 1.67 sec: 1.02x faster                                                          |
| logging_simple             | 6.16 us                                                               | 6.05 us: 1.02x faster                                                           |
| async_tree_cpu_io_mixed    | 502 ms                                                                | 493 ms: 1.02x faster                                                            |
| nqueens                    | 83.9 ms                                                               | 82.6 ms: 1.01x faster                                                           |
| coroutines                 | 24.9 ms                                                               | 24.6 ms: 1.01x faster                                                           |
| genshi_text                | 21.7 ms                                                               | 21.4 ms: 1.01x faster                                                           |
| bpe_tokeniser              | 4.42 sec                                                              | 4.36 sec: 1.01x faster                                                          |
| float                      | 66.2 ms                                                               | 65.3 ms: 1.01x faster                                                           |
| subparsers                 | 23.9 ms                                                               | 23.6 ms: 1.01x faster                                                           |
| pickle_pure_python         | 323 us                                                                | 320 us: 1.01x faster                                                            |
| django_template            | 32.6 ms                                                               | 32.2 ms: 1.01x faster                                                           |
| xml_etree_process          | 56.2 ms                                                               | 55.7 ms: 1.01x faster                                                           |
| async_tree_cpu_io_mixed_tg | 492 ms                                                                | 487 ms: 1.01x faster                                                            |
| json_dumps                 | 11.1 ms                                                               | 11.0 ms: 1.01x faster                                                           |
| comprehensions             | 17.2 us                                                               | 17.1 us: 1.01x faster                                                           |
| logging_format             | 6.83 us                                                               | 6.77 us: 1.01x faster                                                           |
| async_generators           | 434 ms                                                                | 431 ms: 1.01x faster                                                            |
| chaos                      | 61.6 ms                                                               | 61.1 ms: 1.01x faster                                                           |
| logging_silent             | 479 ns                                                                | 476 ns: 1.01x faster                                                            |
| scimark_monte_carlo        | 66.0 ms                                                               | 65.5 ms: 1.01x faster                                                           |
| meteor_contest             | 106 ms                                                                | 105 ms: 1.01x faster                                                            |
| deepcopy                   | 260 us                                                                | 259 us: 1.01x faster                                                            |
| sqlite_synth               | 2.80 us                                                               | 2.79 us: 1.01x faster                                                           |
| regex_compile              | 128 ms                                                                | 127 ms: 1.00x faster                                                            |
| sympy_expand               | 470 ms                                                                | 468 ms: 1.00x faster                                                            |
| python_startup             | 12.2 ms                                                               | 12.1 ms: 1.00x faster                                                           |
| dulwich_log                | 59.4 ms                                                               | 59.2 ms: 1.00x faster                                                           |
| python_startup_no_site     | 6.95 ms                                                               | 6.93 ms: 1.00x faster                                                           |
| sqlglot_v2_optimize        | 52.9 ms                                                               | 52.8 ms: 1.00x faster                                                           |
| pidigits                   | 188 ms                                                                | 188 ms: 1.00x faster                                                            |
| sqlglot_v2_transpile       | 1.57 ms                                                               | 1.58 ms: 1.00x slower                                                           |
| docutils                   | 2.63 sec                                                              | 2.65 sec: 1.01x slower                                                          |
| xml_etree_generate         | 80.3 ms                                                               | 80.8 ms: 1.01x slower                                                           |
| xml_etree_iterparse        | 98.7 ms                                                               | 99.5 ms: 1.01x slower                                                           |
| thrift                     | 774 us                                                                | 781 us: 1.01x slower                                                            |
| tomli_loads                | 1.82 sec                                                              | 1.84 sec: 1.01x slower                                                          |
| generators                 | 30.3 ms                                                               | 30.9 ms: 1.02x slower                                                           |
| typing_runtime_protocols   | 166 us                                                                | 170 us: 1.02x slower                                                            |
| json_loads                 | 28.1 us                                                               | 28.8 us: 1.03x slower                                                           |
| djangocms                  | 21.8 us                                                               | 22.4 us: 1.03x slower                                                           |
| pycparser                  | 1.12 sec                                                              | 1.15 sec: 1.03x slower                                                          |
| regex_effbot               | 3.17 ms                                                               | 3.32 ms: 1.04x slower                                                           |
| regex_v8                   | 22.1 ms                                                               | 23.4 ms: 1.06x slower                                                           |
| regex_dna                  | 200 ms                                                                | 214 ms: 1.07x slower                                                            |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (41): scimark_sparse_mat_mult, spectral_norm, async_tree_memoization_tg, async_tree_io, unpickle_pure_python, html5lib, telco, mdp, sqlglot_v2_normalize, sqlglot_v2_parse, deepcopy_memo, many_optionals, async_tree_io_tg, hexiom, sympy_str, create_gc_cycles, connected_components, async_tree_none, scimark_sor, xml_etree_parse, asyncio_websockets, gc_traversal, 2to3, sympy_integrate, raytrace, deltablue, richards_super, coverage, pylint, scimark_lu, sympy_sum, scimark_fft, async_tree_none_tg, pathlib, pprint_safe_repr, richards, json, k_core, go, sphinx, async_tree_memoization

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 98.58% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x