# Results vs. base

- fork: python
- ref: caf6064a1bc15ac344af
- machine: linux-aarch64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 303 ms                                                                                                            | 360 ms: 1.19x slower                                                                                                  |
| chameleon      | 9.03 ms                                                                                                           | 9.20 ms: 1.02x slower                                                                                                 |
| docutils       | 3.09 sec                                                                                                          | 3.54 sec: 1.14x slower                                                                                                |
| tornado_http   | 131 ms                                                                                                            | 145 ms: 1.10x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.10x slower                                                                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| async_tree_none            | 486 ms                                                                                                            | 497 ms: 1.02x slower                                                                                                  |
| async_tree_cpu_io_mixed_tg | 792 ms                                                                                                            | 813 ms: 1.03x slower                                                                                                  |
| async_tree_cpu_io_mixed    | 785 ms                                                                                                            | 807 ms: 1.03x slower                                                                                                  |
| Geometric mean             | (ref)                                                                                                             | 1.02x slower                                                                                                          |

Benchmark hidden because not significant (5): async_tree_memoization_tg, async_tree_io, async_tree_io_tg, async_tree_none_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 31.1 ms                                                                                                           | 30.3 ms: 1.03x faster                                                                                                 |
| regex_dna      | 247 ms                                                                                                            | 251 ms: 1.02x slower                                                                                                  |
| regex_compile  | 131 ms                                                                                                            | 171 ms: 1.30x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.07x slower                                                                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| unpickle_list        | 6.63 us                                                                                                           | 6.55 us: 1.01x faster                                                                                                 |
| json_loads           | 32.3 us                                                                                                           | 32.1 us: 1.01x faster                                                                                                 |
| pickle_dict          | 37.4 us                                                                                                           | 38.2 us: 1.02x slower                                                                                                 |
| pickle_list          | 5.19 us                                                                                                           | 5.32 us: 1.03x slower                                                                                                 |
| tomli_loads          | 2.56 sec                                                                                                          | 2.65 sec: 1.03x slower                                                                                                |
| pickle_pure_python   | 358 us                                                                                                            | 387 us: 1.08x slower                                                                                                  |
| unpickle_pure_python | 254 us                                                                                                            | 276 us: 1.09x slower                                                                                                  |
| Geometric mean       | (ref)                                                                                                             | 1.02x slower                                                                                                          |

Benchmark hidden because not significant (7): xml_etree_parse, unpickle, json_dumps, pickle, xml_etree_process, xml_etree_iterparse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 12.3 ms                                                                                                           | 14.9 ms: 1.21x slower                                                                                                 |
| python_startup_no_site | 8.48 ms                                                                                                           | 10.8 ms: 1.27x slower                                                                                                 |
| Geometric mean         | (ref)                                                                                                             | 1.24x slower                                                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako            | 13.5 ms                                                                                                           | 13.1 ms: 1.03x faster                                                                                                 |
| django_template | 41.7 ms                                                                                                           | 49.6 ms: 1.19x slower                                                                                                 |
| genshi_text     | 28.6 ms                                                                                                           | 35.2 ms: 1.23x slower                                                                                                 |
| genshi_xml      | 61.2 ms                                                                                                           | 83.5 ms: 1.36x slower                                                                                                 |
| Geometric mean  | (ref)                                                                                                             | 1.18x slower                                                                                                          |

All benchmarks:
===============

| Benchmark                  | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako                       | 13.5 ms                                                                                                           | 13.1 ms: 1.03x faster                                                                                                 |
| regex_v8                   | 31.1 ms                                                                                                           | 30.3 ms: 1.03x faster                                                                                                 |
| deepcopy_memo              | 51.3 us                                                                                                           | 50.0 us: 1.03x faster                                                                                                 |
| gc_traversal               | 5.29 ms                                                                                                           | 5.18 ms: 1.02x faster                                                                                                 |
| sqlite_synth               | 3.90 us                                                                                                           | 3.82 us: 1.02x faster                                                                                                 |
| generators                 | 39.0 ms                                                                                                           | 38.3 ms: 1.02x faster                                                                                                 |
| unpickle_list              | 6.63 us                                                                                                           | 6.55 us: 1.01x faster                                                                                                 |
| json_loads                 | 32.3 us                                                                                                           | 32.1 us: 1.01x faster                                                                                                 |
| asyncio_websockets         | 658 ms                                                                                                            | 665 ms: 1.01x slower                                                                                                  |
| richards                   | 53.3 ms                                                                                                           | 54.1 ms: 1.01x slower                                                                                                 |
| regex_dna                  | 247 ms                                                                                                            | 251 ms: 1.02x slower                                                                                                  |
| chameleon                  | 9.03 ms                                                                                                           | 9.20 ms: 1.02x slower                                                                                                 |
| asyncio_tcp_ssl            | 2.22 sec                                                                                                          | 2.27 sec: 1.02x slower                                                                                                |
| pickle_dict                | 37.4 us                                                                                                           | 38.2 us: 1.02x slower                                                                                                 |
| async_tree_none            | 486 ms                                                                                                            | 497 ms: 1.02x slower                                                                                                  |
| pickle_list                | 5.19 us                                                                                                           | 5.32 us: 1.03x slower                                                                                                 |
| richards_super             | 60.1 ms                                                                                                           | 61.7 ms: 1.03x slower                                                                                                 |
| async_tree_cpu_io_mixed_tg | 792 ms                                                                                                            | 813 ms: 1.03x slower                                                                                                  |
| async_tree_cpu_io_mixed    | 785 ms                                                                                                            | 807 ms: 1.03x slower                                                                                                  |
| fannkuch                   | 463 ms                                                                                                            | 477 ms: 1.03x slower                                                                                                  |
| scimark_fft                | 443 ms                                                                                                            | 456 ms: 1.03x slower                                                                                                  |
| mdp                        | 3.37 sec                                                                                                          | 3.48 sec: 1.03x slower                                                                                                |
| tomli_loads                | 2.56 sec                                                                                                          | 2.65 sec: 1.03x slower                                                                                                |
| spectral_norm              | 141 ms                                                                                                            | 146 ms: 1.03x slower                                                                                                  |
| logging_simple             | 7.00 us                                                                                                           | 7.24 us: 1.03x slower                                                                                                 |
| async_generators           | 496 ms                                                                                                            | 514 ms: 1.04x slower                                                                                                  |
| logging_silent             | 133 ns                                                                                                            | 140 ns: 1.05x slower                                                                                                  |
| meteor_contest             | 113 ms                                                                                                            | 119 ms: 1.05x slower                                                                                                  |
| scimark_sparse_mat_mult    | 6.53 ms                                                                                                           | 6.88 ms: 1.05x slower                                                                                                 |
| dask                       | 373 ms                                                                                                            | 393 ms: 1.05x slower                                                                                                  |
| scimark_monte_carlo        | 83.0 ms                                                                                                           | 87.5 ms: 1.05x slower                                                                                                 |
| typing_runtime_protocols   | 197 us                                                                                                            | 208 us: 1.06x slower                                                                                                  |
| crypto_pyaes               | 81.5 ms                                                                                                           | 87.2 ms: 1.07x slower                                                                                                 |
| asyncio_tcp                | 574 ms                                                                                                            | 615 ms: 1.07x slower                                                                                                  |
| pyflate                    | 578 ms                                                                                                            | 623 ms: 1.08x slower                                                                                                  |
| pickle_pure_python         | 358 us                                                                                                            | 387 us: 1.08x slower                                                                                                  |
| unpickle_pure_python       | 254 us                                                                                                            | 276 us: 1.09x slower                                                                                                  |
| raytrace                   | 297 ms                                                                                                            | 325 ms: 1.10x slower                                                                                                  |
| flaskblogging              | 4.76 ms                                                                                                           | 5.23 ms: 1.10x slower                                                                                                 |
| deepcopy                   | 450 us                                                                                                            | 494 us: 1.10x slower                                                                                                  |
| tornado_http               | 131 ms                                                                                                            | 145 ms: 1.10x slower                                                                                                  |
| scimark_sor                | 159 ms                                                                                                            | 176 ms: 1.11x slower                                                                                                  |
| sqlglot_optimize           | 63.0 ms                                                                                                           | 69.8 ms: 1.11x slower                                                                                                 |
| pycparser                  | 1.22 sec                                                                                                          | 1.36 sec: 1.11x slower                                                                                                |
| go                         | 161 ms                                                                                                            | 179 ms: 1.11x slower                                                                                                  |
| comprehensions             | 20.7 us                                                                                                           | 23.0 us: 1.11x slower                                                                                                 |
| sqlglot_parse              | 1.40 ms                                                                                                           | 1.58 ms: 1.12x slower                                                                                                 |
| sqlglot_normalize          | 128 ms                                                                                                            | 145 ms: 1.13x slower                                                                                                  |
| docutils                   | 3.09 sec                                                                                                          | 3.54 sec: 1.14x slower                                                                                                |
| deepcopy_reduce            | 4.07 us                                                                                                           | 4.67 us: 1.15x slower                                                                                                 |
| sqlglot_transpile          | 1.73 ms                                                                                                           | 2.01 ms: 1.16x slower                                                                                                 |
| bench_mp_pool              | 7.41 ms                                                                                                           | 8.66 ms: 1.17x slower                                                                                                 |
| sympy_expand               | 462 ms                                                                                                            | 541 ms: 1.17x slower                                                                                                  |
| pprint_safe_repr           | 935 ms                                                                                                            | 1.10 sec: 1.18x slower                                                                                                |
| deltablue                  | 3.88 ms                                                                                                           | 4.58 ms: 1.18x slower                                                                                                 |
| sympy_str                  | 268 ms                                                                                                            | 317 ms: 1.18x slower                                                                                                  |
| django_template            | 41.7 ms                                                                                                           | 49.6 ms: 1.19x slower                                                                                                 |
| 2to3                       | 303 ms                                                                                                            | 360 ms: 1.19x slower                                                                                                  |
| dulwich_log                | 58.3 ms                                                                                                           | 69.7 ms: 1.19x slower                                                                                                 |
| pprint_pformat             | 1.91 sec                                                                                                          | 2.28 sec: 1.20x slower                                                                                                |
| nqueens                    | 99.0 ms                                                                                                           | 119 ms: 1.20x slower                                                                                                  |
| pylint                     | 342 ms                                                                                                            | 411 ms: 1.20x slower                                                                                                  |
| python_startup             | 12.3 ms                                                                                                           | 14.9 ms: 1.21x slower                                                                                                 |
| sympy_integrate            | 21.1 ms                                                                                                           | 26.0 ms: 1.23x slower                                                                                                 |
| genshi_text                | 28.6 ms                                                                                                           | 35.2 ms: 1.23x slower                                                                                                 |
| python_startup_no_site     | 8.48 ms                                                                                                           | 10.8 ms: 1.27x slower                                                                                                 |
| sympy_sum                  | 144 ms                                                                                                            | 184 ms: 1.27x slower                                                                                                  |
| hexiom                     | 7.03 ms                                                                                                           | 9.07 ms: 1.29x slower                                                                                                 |
| regex_compile              | 131 ms                                                                                                            | 171 ms: 1.30x slower                                                                                                  |
| chaos                      | 67.6 ms                                                                                                           | 88.5 ms: 1.31x slower                                                                                                 |
| scimark_lu                 | 139 ms                                                                                                            | 182 ms: 1.31x slower                                                                                                  |
| genshi_xml                 | 61.2 ms                                                                                                           | 83.5 ms: 1.36x slower                                                                                                 |
| Geometric mean             | (ref)                                                                                                             | 1.07x slower                                                                                                          |

Benchmark hidden because not significant (26): xml_etree_parse, async_tree_memoization_tg, logging_format, unpickle, coroutines, json_dumps, float, create_gc_cycles, regex_effbot, pidigits, pickle, coverage, telco, json, nbody, xml_etree_process, xml_etree_iterparse, async_tree_io, pathlib, async_tree_io_tg, thrift, async_tree_none_tg, async_tree_memoization, bench_thread_pool, html5lib, xml_etree_generate

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.10x