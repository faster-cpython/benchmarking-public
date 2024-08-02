# Results vs. base

- fork: python
- ref: 5b941e57c71d7d0ab983
- machine: linux-aarch64
- commit hash: 5b941e5
- commit date: 2024-05-11
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240511-3.14.0a0-5b941e5/bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json | results/bm-20240511-3.14.0a0-5b941e5-JIT/bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 306 ms                                                                                                            | 364 ms: 1.19x slower                                                                                                  |
| chameleon      | 8.99 ms                                                                                                           | 9.32 ms: 1.04x slower                                                                                                 |
| docutils       | 3.09 sec                                                                                                          | 3.56 sec: 1.15x slower                                                                                                |
| html5lib       | 67.1 ms                                                                                                           | 70.7 ms: 1.05x slower                                                                                                 |
| tornado_http   | 133 ms                                                                                                            | 144 ms: 1.09x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.10x slower                                                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | results/bm-20240511-3.14.0a0-5b941e5/bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json | results/bm-20240511-3.14.0a0-5b941e5-JIT/bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json |
|--------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| async_tree_none    | 487 ms                                                                                                            | 499 ms: 1.02x slower                                                                                                  |
| async_tree_none_tg | 465 ms                                                                                                            | 476 ms: 1.02x slower                                                                                                  |
| Geometric mean     | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (6): async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240511-3.14.0a0-5b941e5/bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json | results/bm-20240511-3.14.0a0-5b941e5-JIT/bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| nbody          | 112 ms                                                                                                            | 114 ms: 1.02x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240511-3.14.0a0-5b941e5/bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json | results/bm-20240511-3.14.0a0-5b941e5-JIT/bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 130 ms                                                                                                            | 171 ms: 1.32x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.07x slower                                                                                                          |

Benchmark hidden because not significant (3): regex_v8, regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240511-3.14.0a0-5b941e5/bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json | results/bm-20240511-3.14.0a0-5b941e5-JIT/bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| unpickle_list        | 6.59 us                                                                                                           | 6.35 us: 1.04x faster                                                                                                 |
| xml_etree_generate   | 112 ms                                                                                                            | 113 ms: 1.01x slower                                                                                                  |
| tomli_loads          | 2.58 sec                                                                                                          | 2.61 sec: 1.01x slower                                                                                                |
| xml_etree_process    | 79.3 ms                                                                                                           | 80.3 ms: 1.01x slower                                                                                                 |
| pickle_list          | 5.20 us                                                                                                           | 5.28 us: 1.02x slower                                                                                                 |
| xml_etree_iterparse  | 149 ms                                                                                                            | 152 ms: 1.02x slower                                                                                                  |
| pickle               | 13.8 us                                                                                                           | 14.1 us: 1.02x slower                                                                                                 |
| pickle_pure_python   | 360 us                                                                                                            | 394 us: 1.10x slower                                                                                                  |
| unpickle_pure_python | 252 us                                                                                                            | 276 us: 1.10x slower                                                                                                  |
| Geometric mean       | (ref)                                                                                                             | 1.02x slower                                                                                                          |

Benchmark hidden because not significant (5): json_dumps, xml_etree_parse, json_loads, unpickle, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240511-3.14.0a0-5b941e5/bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json | results/bm-20240511-3.14.0a0-5b941e5-JIT/bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                                                                           | 14.8 ms: 1.19x slower                                                                                                 |
| python_startup_no_site | 8.55 ms                                                                                                           | 10.8 ms: 1.27x slower                                                                                                 |
| Geometric mean         | (ref)                                                                                                             | 1.23x slower                                                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240511-3.14.0a0-5b941e5/bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json | results/bm-20240511-3.14.0a0-5b941e5-JIT/bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako            | 13.2 ms                                                                                                           | 13.1 ms: 1.01x faster                                                                                                 |
| django_template | 41.9 ms                                                                                                           | 49.8 ms: 1.19x slower                                                                                                 |
| genshi_text     | 28.0 ms                                                                                                           | 34.4 ms: 1.23x slower                                                                                                 |
| genshi_xml      | 61.0 ms                                                                                                           | 81.9 ms: 1.34x slower                                                                                                 |
| Geometric mean  | (ref)                                                                                                             | 1.18x slower                                                                                                          |

All benchmarks:
===============

| Benchmark                | results/bm-20240511-3.14.0a0-5b941e5/bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json | results/bm-20240511-3.14.0a0-5b941e5-JIT/bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json |
|--------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| unpickle_list            | 6.59 us                                                                                                           | 6.35 us: 1.04x faster                                                                                                 |
| deepcopy_memo            | 51.4 us                                                                                                           | 50.1 us: 1.03x faster                                                                                                 |
| sqlite_synth             | 3.90 us                                                                                                           | 3.80 us: 1.03x faster                                                                                                 |
| coroutines               | 29.2 ms                                                                                                           | 28.9 ms: 1.01x faster                                                                                                 |
| mako                     | 13.2 ms                                                                                                           | 13.1 ms: 1.01x faster                                                                                                 |
| xml_etree_generate       | 112 ms                                                                                                            | 113 ms: 1.01x slower                                                                                                  |
| telco                    | 164 ms                                                                                                            | 166 ms: 1.01x slower                                                                                                  |
| tomli_loads              | 2.58 sec                                                                                                          | 2.61 sec: 1.01x slower                                                                                                |
| xml_etree_process        | 79.3 ms                                                                                                           | 80.3 ms: 1.01x slower                                                                                                 |
| richards                 | 53.4 ms                                                                                                           | 54.1 ms: 1.01x slower                                                                                                 |
| nbody                    | 112 ms                                                                                                            | 114 ms: 1.02x slower                                                                                                  |
| richards_super           | 60.3 ms                                                                                                           | 61.3 ms: 1.02x slower                                                                                                 |
| pickle_list              | 5.20 us                                                                                                           | 5.28 us: 1.02x slower                                                                                                 |
| xml_etree_iterparse      | 149 ms                                                                                                            | 152 ms: 1.02x slower                                                                                                  |
| logging_format           | 7.76 us                                                                                                           | 7.92 us: 1.02x slower                                                                                                 |
| pickle                   | 13.8 us                                                                                                           | 14.1 us: 1.02x slower                                                                                                 |
| asyncio_tcp_ssl          | 2.21 sec                                                                                                          | 2.26 sec: 1.02x slower                                                                                                |
| async_tree_none          | 487 ms                                                                                                            | 499 ms: 1.02x slower                                                                                                  |
| async_tree_none_tg       | 465 ms                                                                                                            | 476 ms: 1.02x slower                                                                                                  |
| scimark_fft              | 444 ms                                                                                                            | 455 ms: 1.02x slower                                                                                                  |
| fannkuch                 | 461 ms                                                                                                            | 475 ms: 1.03x slower                                                                                                  |
| coverage                 | 97.5 ms                                                                                                           | 101 ms: 1.03x slower                                                                                                  |
| dask                     | 384 ms                                                                                                            | 397 ms: 1.03x slower                                                                                                  |
| logging_simple           | 7.15 us                                                                                                           | 7.39 us: 1.03x slower                                                                                                 |
| spectral_norm            | 141 ms                                                                                                            | 146 ms: 1.04x slower                                                                                                  |
| chameleon                | 8.99 ms                                                                                                           | 9.32 ms: 1.04x slower                                                                                                 |
| bench_thread_pool        | 1.28 ms                                                                                                           | 1.33 ms: 1.04x slower                                                                                                 |
| scimark_sparse_mat_mult  | 6.58 ms                                                                                                           | 6.84 ms: 1.04x slower                                                                                                 |
| create_gc_cycles         | 2.40 ms                                                                                                           | 2.49 ms: 1.04x slower                                                                                                 |
| mdp                      | 3.35 sec                                                                                                          | 3.48 sec: 1.04x slower                                                                                                |
| gc_traversal             | 5.14 ms                                                                                                           | 5.35 ms: 1.04x slower                                                                                                 |
| scimark_monte_carlo      | 83.9 ms                                                                                                           | 87.4 ms: 1.04x slower                                                                                                 |
| logging_silent           | 134 ns                                                                                                            | 139 ns: 1.04x slower                                                                                                  |
| async_generators         | 489 ms                                                                                                            | 513 ms: 1.05x slower                                                                                                  |
| asyncio_tcp              | 576 ms                                                                                                            | 605 ms: 1.05x slower                                                                                                  |
| meteor_contest           | 113 ms                                                                                                            | 119 ms: 1.05x slower                                                                                                  |
| typing_runtime_protocols | 196 us                                                                                                            | 207 us: 1.05x slower                                                                                                  |
| html5lib                 | 67.1 ms                                                                                                           | 70.7 ms: 1.05x slower                                                                                                 |
| crypto_pyaes             | 81.9 ms                                                                                                           | 87.0 ms: 1.06x slower                                                                                                 |
| pyflate                  | 581 ms                                                                                                            | 619 ms: 1.07x slower                                                                                                  |
| tornado_http             | 133 ms                                                                                                            | 144 ms: 1.09x slower                                                                                                  |
| deepcopy                 | 454 us                                                                                                            | 495 us: 1.09x slower                                                                                                  |
| pickle_pure_python       | 360 us                                                                                                            | 394 us: 1.10x slower                                                                                                  |
| unpickle_pure_python     | 252 us                                                                                                            | 276 us: 1.10x slower                                                                                                  |
| raytrace                 | 296 ms                                                                                                            | 325 ms: 1.10x slower                                                                                                  |
| comprehensions           | 20.9 us                                                                                                           | 22.9 us: 1.10x slower                                                                                                 |
| go                       | 161 ms                                                                                                            | 179 ms: 1.11x slower                                                                                                  |
| pycparser                | 1.22 sec                                                                                                          | 1.36 sec: 1.11x slower                                                                                                |
| sqlglot_normalize        | 129 ms                                                                                                            | 144 ms: 1.11x slower                                                                                                  |
| scimark_sor              | 158 ms                                                                                                            | 176 ms: 1.11x slower                                                                                                  |
| sqlglot_optimize         | 62.6 ms                                                                                                           | 69.9 ms: 1.12x slower                                                                                                 |
| deepcopy_reduce          | 4.15 us                                                                                                           | 4.67 us: 1.13x slower                                                                                                 |
| sqlglot_parse            | 1.40 ms                                                                                                           | 1.60 ms: 1.14x slower                                                                                                 |
| docutils                 | 3.09 sec                                                                                                          | 3.56 sec: 1.15x slower                                                                                                |
| bench_mp_pool            | 7.14 ms                                                                                                           | 8.24 ms: 1.15x slower                                                                                                 |
| sqlglot_transpile        | 1.75 ms                                                                                                           | 2.04 ms: 1.17x slower                                                                                                 |
| dulwich_log              | 61.4 ms                                                                                                           | 71.8 ms: 1.17x slower                                                                                                 |
| pprint_safe_repr         | 941 ms                                                                                                            | 1.11 sec: 1.18x slower                                                                                                |
| deltablue                | 3.85 ms                                                                                                           | 4.56 ms: 1.19x slower                                                                                                 |
| django_template          | 41.9 ms                                                                                                           | 49.8 ms: 1.19x slower                                                                                                 |
| python_startup           | 12.5 ms                                                                                                           | 14.8 ms: 1.19x slower                                                                                                 |
| 2to3                     | 306 ms                                                                                                            | 364 ms: 1.19x slower                                                                                                  |
| pprint_pformat           | 1.92 sec                                                                                                          | 2.29 sec: 1.19x slower                                                                                                |
| nqueens                  | 98.0 ms                                                                                                           | 118 ms: 1.21x slower                                                                                                  |
| sympy_expand             | 459 ms                                                                                                            | 554 ms: 1.21x slower                                                                                                  |
| sympy_str                | 269 ms                                                                                                            | 326 ms: 1.21x slower                                                                                                  |
| pylint                   | 343 ms                                                                                                            | 419 ms: 1.22x slower                                                                                                  |
| sympy_integrate          | 21.6 ms                                                                                                           | 26.4 ms: 1.22x slower                                                                                                 |
| genshi_text              | 28.0 ms                                                                                                           | 34.4 ms: 1.23x slower                                                                                                 |
| hexiom                   | 7.11 ms                                                                                                           | 8.99 ms: 1.26x slower                                                                                                 |
| sympy_sum                | 149 ms                                                                                                            | 189 ms: 1.27x slower                                                                                                  |
| python_startup_no_site   | 8.55 ms                                                                                                           | 10.8 ms: 1.27x slower                                                                                                 |
| chaos                    | 67.8 ms                                                                                                           | 88.7 ms: 1.31x slower                                                                                                 |
| regex_compile            | 130 ms                                                                                                            | 171 ms: 1.32x slower                                                                                                  |
| scimark_lu               | 138 ms                                                                                                            | 182 ms: 1.32x slower                                                                                                  |
| genshi_xml               | 61.0 ms                                                                                                           | 81.9 ms: 1.34x slower                                                                                                 |
| Geometric mean           | (ref)                                                                                                             | 1.07x slower                                                                                                          |

Benchmark hidden because not significant (22): generators, async_tree_memoization_tg, json_dumps, xml_etree_parse, json_loads, unpickle, regex_v8, pathlib, json, pidigits, asyncio_websockets, regex_effbot, regex_dna, float, pickle_dict, async_tree_cpu_io_mixed, async_tree_io, async_tree_io_tg, thrift, async_tree_memoization, async_tree_cpu_io_mixed_tg, flaskblogging

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.10x