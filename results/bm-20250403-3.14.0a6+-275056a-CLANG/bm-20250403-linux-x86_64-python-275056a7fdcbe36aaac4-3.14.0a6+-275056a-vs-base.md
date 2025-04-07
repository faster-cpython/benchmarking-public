# Results vs. base

- fork: python
- ref: 275056a7fdcbe36aaac4
- machine: linux-x86_64
- commit hash: 275056a
- commit date: 2025-04-03
- overall geometric mean: 1.030x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250403-3.14.0a6+-275056a/bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a.json | results/bm-20250403-3.14.0a6+-275056a-CLANG/bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 249 ms                                                                                                            | 244 ms: 1.02x faster                                                                                                    |
| docutils       | 2.60 sec                                                                                                          | 2.56 sec: 1.02x faster                                                                                                  |
| html5lib       | 60.8 ms                                                                                                           | 57.7 ms: 1.05x faster                                                                                                   |
| sphinx         | 1.01 sec                                                                                                          | 985 ms: 1.03x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.03x faster                                                                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250403-3.14.0a6+-275056a/bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a.json | results/bm-20250403-3.14.0a6+-275056a-CLANG/bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| coroutines                 | 23.0 ms                                                                                                           | 21.5 ms: 1.07x faster                                                                                                   |
| async_tree_none            | 261 ms                                                                                                            | 253 ms: 1.03x faster                                                                                                    |
| async_tree_memoization     | 312 ms                                                                                                            | 304 ms: 1.03x faster                                                                                                    |
| async_tree_io              | 613 ms                                                                                                            | 597 ms: 1.03x faster                                                                                                    |
| async_tree_none_tg         | 249 ms                                                                                                            | 243 ms: 1.02x faster                                                                                                    |
| async_generators           | 391 ms                                                                                                            | 383 ms: 1.02x faster                                                                                                    |
| async_tree_cpu_io_mixed    | 480 ms                                                                                                            | 483 ms: 1.01x slower                                                                                                    |
| async_tree_cpu_io_mixed_tg | 474 ms                                                                                                            | 480 ms: 1.01x slower                                                                                                    |
| Geometric mean             | (ref)                                                                                                             | 1.02x faster                                                                                                            |

Benchmark hidden because not significant (3): async_tree_memoization_tg, async_tree_io_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250403-3.14.0a6+-275056a/bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a.json | results/bm-20250403-3.14.0a6+-275056a-CLANG/bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| nbody          | 91.3 ms                                                                                                           | 83.5 ms: 1.09x faster                                                                                                   |
| float          | 70.2 ms                                                                                                           | 67.6 ms: 1.04x faster                                                                                                   |
| pidigits       | 186 ms                                                                                                            | 201 ms: 1.08x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.02x faster                                                                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250403-3.14.0a6+-275056a/bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a.json | results/bm-20250403-3.14.0a6+-275056a-CLANG/bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 214 ms                                                                                                            | 188 ms: 1.14x faster                                                                                                    |
| regex_effbot   | 3.35 ms                                                                                                           | 3.08 ms: 1.09x faster                                                                                                   |
| regex_v8       | 24.0 ms                                                                                                           | 22.7 ms: 1.06x faster                                                                                                   |
| regex_compile  | 124 ms                                                                                                            | 124 ms: 1.01x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.07x faster                                                                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250403-3.14.0a6+-275056a/bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a.json | results/bm-20250403-3.14.0a6+-275056a-CLANG/bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.94 sec                                                                                                          | 1.84 sec: 1.05x faster                                                                                                  |
| pickle_pure_python   | 313 us                                                                                                            | 303 us: 1.03x faster                                                                                                    |
| unpickle_pure_python | 217 us                                                                                                            | 210 us: 1.03x faster                                                                                                    |
| json_loads           | 29.8 us                                                                                                           | 29.0 us: 1.02x faster                                                                                                   |
| xml_etree_process    | 58.9 ms                                                                                                           | 59.2 ms: 1.01x slower                                                                                                   |
| xml_etree_generate   | 83.8 ms                                                                                                           | 86.1 ms: 1.03x slower                                                                                                   |
| xml_etree_iterparse  | 98.9 ms                                                                                                           | 103 ms: 1.04x slower                                                                                                    |
| json_dumps           | 11.3 ms                                                                                                           | 12.5 ms: 1.11x slower                                                                                                   |
| xml_etree_parse      | 140 ms                                                                                                            | 162 ms: 1.15x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                             | 1.02x slower                                                                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250403-3.14.0a6+-275056a/bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a.json | results/bm-20250403-3.14.0a6+-275056a-CLANG/bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                                                           | 12.9 ms: 1.02x faster                                                                                                   |
| python_startup_no_site | 8.17 ms                                                                                                           | 8.07 ms: 1.01x faster                                                                                                   |
| Geometric mean         | (ref)                                                                                                             | 1.01x faster                                                                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250403-3.14.0a6+-275056a/bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a.json | results/bm-20250403-3.14.0a6+-275056a-CLANG/bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| genshi_text     | 21.2 ms                                                                                                           | 20.4 ms: 1.04x faster                                                                                                   |
| genshi_xml      | 48.7 ms                                                                                                           | 47.3 ms: 1.03x faster                                                                                                   |
| django_template | 32.0 ms                                                                                                           | 31.8 ms: 1.00x faster                                                                                                   |
| mako            | 11.3 ms                                                                                                           | 11.7 ms: 1.04x slower                                                                                                   |
| Geometric mean  | (ref)                                                                                                             | 1.01x faster                                                                                                            |

All benchmarks:
===============

| Benchmark                  | results/bm-20250403-3.14.0a6+-275056a/bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a.json | results/bm-20250403-3.14.0a6+-275056a-CLANG/bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| scimark_sparse_mat_mult    | 4.64 ms                                                                                                           | 3.96 ms: 1.17x faster                                                                                                   |
| spectral_norm              | 101 ms                                                                                                            | 87.5 ms: 1.15x faster                                                                                                   |
| scimark_fft                | 340 ms                                                                                                            | 296 ms: 1.15x faster                                                                                                    |
| regex_dna                  | 214 ms                                                                                                            | 188 ms: 1.14x faster                                                                                                    |
| deltablue                  | 3.31 ms                                                                                                           | 2.92 ms: 1.13x faster                                                                                                   |
| scimark_monte_carlo        | 66.2 ms                                                                                                           | 58.8 ms: 1.13x faster                                                                                                   |
| pathlib                    | 16.5 ms                                                                                                           | 14.9 ms: 1.11x faster                                                                                                   |
| nbody                      | 91.3 ms                                                                                                           | 83.5 ms: 1.09x faster                                                                                                   |
| deepcopy_reduce            | 2.76 us                                                                                                           | 2.53 us: 1.09x faster                                                                                                   |
| regex_effbot               | 3.35 ms                                                                                                           | 3.08 ms: 1.09x faster                                                                                                   |
| pyflate                    | 445 ms                                                                                                            | 410 ms: 1.09x faster                                                                                                    |
| richards                   | 43.0 ms                                                                                                           | 39.8 ms: 1.08x faster                                                                                                   |
| typing_runtime_protocols   | 166 us                                                                                                            | 154 us: 1.08x faster                                                                                                    |
| scimark_sor                | 115 ms                                                                                                            | 107 ms: 1.08x faster                                                                                                    |
| richards_super             | 49.3 ms                                                                                                           | 46.0 ms: 1.07x faster                                                                                                   |
| coroutines                 | 23.0 ms                                                                                                           | 21.5 ms: 1.07x faster                                                                                                   |
| logging_silent             | 94.4 ns                                                                                                           | 88.8 ns: 1.06x faster                                                                                                   |
| hexiom                     | 6.14 ms                                                                                                           | 5.79 ms: 1.06x faster                                                                                                   |
| generators                 | 29.9 ms                                                                                                           | 28.3 ms: 1.06x faster                                                                                                   |
| regex_v8                   | 24.0 ms                                                                                                           | 22.7 ms: 1.06x faster                                                                                                   |
| comprehensions             | 16.9 us                                                                                                           | 16.0 us: 1.06x faster                                                                                                   |
| sqlglot_v2_parse           | 1.24 ms                                                                                                           | 1.18 ms: 1.06x faster                                                                                                   |
| html5lib                   | 60.8 ms                                                                                                           | 57.7 ms: 1.05x faster                                                                                                   |
| tomli_loads                | 1.94 sec                                                                                                          | 1.84 sec: 1.05x faster                                                                                                  |
| sqlglot_v2_transpile       | 1.56 ms                                                                                                           | 1.48 ms: 1.05x faster                                                                                                   |
| chaos                      | 56.5 ms                                                                                                           | 53.9 ms: 1.05x faster                                                                                                   |
| go                         | 111 ms                                                                                                            | 106 ms: 1.05x faster                                                                                                    |
| bpe_tokeniser              | 4.51 sec                                                                                                          | 4.32 sec: 1.04x faster                                                                                                  |
| deepcopy                   | 253 us                                                                                                            | 243 us: 1.04x faster                                                                                                    |
| deepcopy_memo              | 29.3 us                                                                                                           | 28.2 us: 1.04x faster                                                                                                   |
| bench_thread_pool          | 877 us                                                                                                            | 842 us: 1.04x faster                                                                                                    |
| coverage                   | 84.4 ms                                                                                                           | 81.1 ms: 1.04x faster                                                                                                   |
| telco                      | 7.80 ms                                                                                                           | 7.50 ms: 1.04x faster                                                                                                   |
| genshi_text                | 21.2 ms                                                                                                           | 20.4 ms: 1.04x faster                                                                                                   |
| float                      | 70.2 ms                                                                                                           | 67.6 ms: 1.04x faster                                                                                                   |
| nqueens                    | 81.7 ms                                                                                                           | 78.7 ms: 1.04x faster                                                                                                   |
| scimark_lu                 | 116 ms                                                                                                            | 111 ms: 1.04x faster                                                                                                    |
| raytrace                   | 258 ms                                                                                                            | 249 ms: 1.04x faster                                                                                                    |
| fannkuch                   | 413 ms                                                                                                            | 398 ms: 1.04x faster                                                                                                    |
| sympy_sum                  | 150 ms                                                                                                            | 145 ms: 1.04x faster                                                                                                    |
| sympy_integrate            | 19.0 ms                                                                                                           | 18.4 ms: 1.04x faster                                                                                                   |
| sqlite_synth               | 2.77 us                                                                                                           | 2.68 us: 1.04x faster                                                                                                   |
| sqlalchemy_declarative     | 132 ms                                                                                                            | 127 ms: 1.03x faster                                                                                                    |
| pickle_pure_python         | 313 us                                                                                                            | 303 us: 1.03x faster                                                                                                    |
| async_tree_none            | 261 ms                                                                                                            | 253 ms: 1.03x faster                                                                                                    |
| sqlalchemy_imperative      | 16.9 ms                                                                                                           | 16.4 ms: 1.03x faster                                                                                                   |
| genshi_xml                 | 48.7 ms                                                                                                           | 47.3 ms: 1.03x faster                                                                                                   |
| many_optionals             | 933 us                                                                                                            | 906 us: 1.03x faster                                                                                                    |
| unpickle_pure_python       | 217 us                                                                                                            | 210 us: 1.03x faster                                                                                                    |
| async_tree_memoization     | 312 ms                                                                                                            | 304 ms: 1.03x faster                                                                                                    |
| sphinx                     | 1.01 sec                                                                                                          | 985 ms: 1.03x faster                                                                                                    |
| dulwich_log                | 59.5 ms                                                                                                           | 57.8 ms: 1.03x faster                                                                                                   |
| crypto_pyaes               | 73.0 ms                                                                                                           | 71.0 ms: 1.03x faster                                                                                                   |
| async_tree_io              | 613 ms                                                                                                            | 597 ms: 1.03x faster                                                                                                    |
| sympy_str                  | 268 ms                                                                                                            | 261 ms: 1.03x faster                                                                                                    |
| json_loads                 | 29.8 us                                                                                                           | 29.0 us: 1.02x faster                                                                                                   |
| async_tree_none_tg         | 249 ms                                                                                                            | 243 ms: 1.02x faster                                                                                                    |
| mdp                        | 1.22 sec                                                                                                          | 1.20 sec: 1.02x faster                                                                                                  |
| async_generators           | 391 ms                                                                                                            | 383 ms: 1.02x faster                                                                                                    |
| logging_format             | 6.12 us                                                                                                           | 5.99 us: 1.02x faster                                                                                                   |
| 2to3                       | 249 ms                                                                                                            | 244 ms: 1.02x faster                                                                                                    |
| sympy_expand               | 457 ms                                                                                                            | 448 ms: 1.02x faster                                                                                                    |
| bench_mp_pool              | 81.9 ms                                                                                                           | 80.4 ms: 1.02x faster                                                                                                   |
| docutils                   | 2.60 sec                                                                                                          | 2.56 sec: 1.02x faster                                                                                                  |
| python_startup             | 13.1 ms                                                                                                           | 12.9 ms: 1.02x faster                                                                                                   |
| gc_traversal               | 5.02 ms                                                                                                           | 4.94 ms: 1.02x faster                                                                                                   |
| subparsers                 | 20.7 ms                                                                                                           | 20.4 ms: 1.01x faster                                                                                                   |
| python_startup_no_site     | 8.17 ms                                                                                                           | 8.07 ms: 1.01x faster                                                                                                   |
| logging_simple             | 5.51 us                                                                                                           | 5.46 us: 1.01x faster                                                                                                   |
| sqlglot_v2_normalize       | 106 ms                                                                                                            | 105 ms: 1.01x faster                                                                                                    |
| regex_compile              | 124 ms                                                                                                            | 124 ms: 1.01x faster                                                                                                    |
| django_template            | 32.0 ms                                                                                                           | 31.8 ms: 1.00x faster                                                                                                   |
| xml_etree_process          | 58.9 ms                                                                                                           | 59.2 ms: 1.01x slower                                                                                                   |
| async_tree_cpu_io_mixed    | 480 ms                                                                                                            | 483 ms: 1.01x slower                                                                                                    |
| shortest_path              | 495 ms                                                                                                            | 499 ms: 1.01x slower                                                                                                    |
| async_tree_cpu_io_mixed_tg | 474 ms                                                                                                            | 480 ms: 1.01x slower                                                                                                    |
| create_gc_cycles           | 2.46 ms                                                                                                           | 2.50 ms: 1.02x slower                                                                                                   |
| connected_components       | 453 ms                                                                                                            | 462 ms: 1.02x slower                                                                                                    |
| xml_etree_generate         | 83.8 ms                                                                                                           | 86.1 ms: 1.03x slower                                                                                                   |
| pprint_pformat             | 1.48 sec                                                                                                          | 1.52 sec: 1.03x slower                                                                                                  |
| pprint_safe_repr           | 724 ms                                                                                                            | 745 ms: 1.03x slower                                                                                                    |
| meteor_contest             | 106 ms                                                                                                            | 109 ms: 1.03x slower                                                                                                    |
| mako                       | 11.3 ms                                                                                                           | 11.7 ms: 1.04x slower                                                                                                   |
| xml_etree_iterparse        | 98.9 ms                                                                                                           | 103 ms: 1.04x slower                                                                                                    |
| pidigits                   | 186 ms                                                                                                            | 201 ms: 1.08x slower                                                                                                    |
| json_dumps                 | 11.3 ms                                                                                                           | 12.5 ms: 1.11x slower                                                                                                   |
| xml_etree_parse            | 140 ms                                                                                                            | 162 ms: 1.15x slower                                                                                                    |
| Geometric mean             | (ref)                                                                                                             | 1.03x faster                                                                                                            |

Benchmark hidden because not significant (8): async_tree_memoization_tg, pylint, json, async_tree_io_tg, asyncio_websockets, sqlglot_v2_optimize, pycparser, k_core

- Geometric mean (including insignificant results): 1.030x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.01x