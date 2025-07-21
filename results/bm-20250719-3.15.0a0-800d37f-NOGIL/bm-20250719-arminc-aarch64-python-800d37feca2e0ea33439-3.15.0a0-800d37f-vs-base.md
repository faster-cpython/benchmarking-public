# Results vs. base

- fork: python
- ref: 800d37feca2e0ea33439
- machine: linux-aarch64
- commit hash: 800d37f
- commit date: 2025-07-19
- overall geometric mean: 1.122x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x slower
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250719-3.15.0a0-800d37f/bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json | results/bm-20250719-3.15.0a0-800d37f-NOGIL/bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 303 ms                                                                                                            | 349 ms: 1.15x slower                                                                                                    |
| docutils       | 2.97 sec                                                                                                          | 3.21 sec: 1.08x slower                                                                                                  |
| html5lib       | 63.5 ms                                                                                                           | 70.9 ms: 1.12x slower                                                                                                   |
| sphinx         | 1.14 sec                                                                                                          | 1.27 sec: 1.11x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.12x slower                                                                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250719-3.15.0a0-800d37f/bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json | results/bm-20250719-3.15.0a0-800d37f-NOGIL/bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 892 ms                                                                                                            | 826 ms: 1.08x faster                                                                                                    |
| async_tree_memoization_tg  | 467 ms                                                                                                            | 441 ms: 1.06x faster                                                                                                    |
| async_tree_cpu_io_mixed_tg | 654 ms                                                                                                            | 632 ms: 1.04x faster                                                                                                    |
| async_tree_io              | 871 ms                                                                                                            | 842 ms: 1.03x faster                                                                                                    |
| async_tree_none_tg         | 376 ms                                                                                                            | 367 ms: 1.02x faster                                                                                                    |
| async_tree_memoization     | 468 ms                                                                                                            | 478 ms: 1.02x slower                                                                                                    |
| async_tree_none            | 372 ms                                                                                                            | 392 ms: 1.05x slower                                                                                                    |
| asyncio_tcp                | 529 ms                                                                                                            | 564 ms: 1.07x slower                                                                                                    |
| coroutines                 | 29.1 ms                                                                                                           | 31.6 ms: 1.08x slower                                                                                                   |
| async_generators           | 459 ms                                                                                                            | 506 ms: 1.10x slower                                                                                                    |
| asyncio_tcp_ssl            | 2.14 sec                                                                                                          | 2.42 sec: 1.13x slower                                                                                                  |
| Geometric mean             | (ref)                                                                                                             | 1.02x slower                                                                                                            |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250719-3.15.0a0-800d37f/bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json | results/bm-20250719-3.15.0a0-800d37f-NOGIL/bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| float          | 84.9 ms                                                                                                           | 94.2 ms: 1.11x slower                                                                                                   |
| nbody          | 120 ms                                                                                                            | 180 ms: 1.50x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.18x slower                                                                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250719-3.15.0a0-800d37f/bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json | results/bm-20250719-3.15.0a0-800d37f-NOGIL/bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 26.6 ms                                                                                                           | 25.7 ms: 1.04x faster                                                                                                   |
| regex_dna      | 219 ms                                                                                                            | 236 ms: 1.08x slower                                                                                                    |
| regex_compile  | 122 ms                                                                                                            | 149 ms: 1.22x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.06x slower                                                                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250719-3.15.0a0-800d37f/bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json | results/bm-20250719-3.15.0a0-800d37f-NOGIL/bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 144 ms                                                                                                            | 135 ms: 1.06x faster                                                                                                    |
| xml_etree_parse      | 178 ms                                                                                                            | 180 ms: 1.01x slower                                                                                                    |
| unpickle_list        | 6.43 us                                                                                                           | 6.95 us: 1.08x slower                                                                                                   |
| json_dumps           | 13.9 ms                                                                                                           | 15.0 ms: 1.08x slower                                                                                                   |
| unpickle             | 18.5 us                                                                                                           | 20.1 us: 1.09x slower                                                                                                   |
| json_loads           | 32.6 us                                                                                                           | 37.0 us: 1.14x slower                                                                                                   |
| pickle_pure_python   | 387 us                                                                                                            | 441 us: 1.14x slower                                                                                                    |
| unpickle_pure_python | 259 us                                                                                                            | 296 us: 1.15x slower                                                                                                    |
| tomli_loads          | 2.44 sec                                                                                                          | 2.82 sec: 1.16x slower                                                                                                  |
| xml_etree_generate   | 112 ms                                                                                                            | 140 ms: 1.25x slower                                                                                                    |
| xml_etree_process    | 79.0 ms                                                                                                           | 102 ms: 1.30x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                             | 1.09x slower                                                                                                            |

Benchmark hidden because not significant (3): pickle, pickle_list, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250719-3.15.0a0-800d37f/bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json | results/bm-20250719-3.15.0a0-800d37f-NOGIL/bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 14.8 ms                                                                                                           | 20.0 ms: 1.35x slower                                                                                                   |
| python_startup_no_site | 8.42 ms                                                                                                           | 12.0 ms: 1.43x slower                                                                                                   |
| Geometric mean         | (ref)                                                                                                             | 1.39x slower                                                                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250719-3.15.0a0-800d37f/bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json | results/bm-20250719-3.15.0a0-800d37f-NOGIL/bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 62.4 ms                                                                                                           | 74.6 ms: 1.20x slower                                                                                                   |
| django_template | 40.6 ms                                                                                                           | 51.0 ms: 1.26x slower                                                                                                   |
| genshi_text     | 26.8 ms                                                                                                           | 36.7 ms: 1.37x slower                                                                                                   |
| mako            | 13.6 ms                                                                                                           | 21.3 ms: 1.57x slower                                                                                                   |
| Geometric mean  | (ref)                                                                                                             | 1.34x slower                                                                                                            |

All benchmarks:
===============

| Benchmark                  | results/bm-20250719-3.15.0a0-800d37f/bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json | results/bm-20250719-3.15.0a0-800d37f-NOGIL/bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool              | 3.17 sec                                                                                                          | 66.4 ms: 47.77x faster                                                                                                  |
| gc_traversal               | 6.94 ms                                                                                                           | 2.84 ms: 2.44x faster                                                                                                   |
| create_gc_cycles           | 3.82 ms                                                                                                           | 2.25 ms: 1.70x faster                                                                                                   |
| sqlite_synth               | 3.81 us                                                                                                           | 3.44 us: 1.10x faster                                                                                                   |
| async_tree_io_tg           | 892 ms                                                                                                            | 826 ms: 1.08x faster                                                                                                    |
| xml_etree_iterparse        | 144 ms                                                                                                            | 135 ms: 1.06x faster                                                                                                    |
| async_tree_memoization_tg  | 467 ms                                                                                                            | 441 ms: 1.06x faster                                                                                                    |
| regex_v8                   | 26.6 ms                                                                                                           | 25.7 ms: 1.04x faster                                                                                                   |
| async_tree_cpu_io_mixed_tg | 654 ms                                                                                                            | 632 ms: 1.04x faster                                                                                                    |
| async_tree_io              | 871 ms                                                                                                            | 842 ms: 1.03x faster                                                                                                    |
| async_tree_none_tg         | 376 ms                                                                                                            | 367 ms: 1.02x faster                                                                                                    |
| xml_etree_parse            | 178 ms                                                                                                            | 180 ms: 1.01x slower                                                                                                    |
| async_tree_memoization     | 468 ms                                                                                                            | 478 ms: 1.02x slower                                                                                                    |
| async_tree_none            | 372 ms                                                                                                            | 392 ms: 1.05x slower                                                                                                    |
| asyncio_tcp                | 529 ms                                                                                                            | 564 ms: 1.07x slower                                                                                                    |
| scimark_sparse_mat_mult    | 7.09 ms                                                                                                           | 7.56 ms: 1.07x slower                                                                                                   |
| logging_silent             | 130 ns                                                                                                            | 140 ns: 1.07x slower                                                                                                    |
| pycparser                  | 1.25 sec                                                                                                          | 1.34 sec: 1.08x slower                                                                                                  |
| docutils                   | 2.97 sec                                                                                                          | 3.21 sec: 1.08x slower                                                                                                  |
| regex_dna                  | 219 ms                                                                                                            | 236 ms: 1.08x slower                                                                                                    |
| unpickle_list              | 6.43 us                                                                                                           | 6.95 us: 1.08x slower                                                                                                   |
| json_dumps                 | 13.9 ms                                                                                                           | 15.0 ms: 1.08x slower                                                                                                   |
| coroutines                 | 29.1 ms                                                                                                           | 31.6 ms: 1.08x slower                                                                                                   |
| unpickle                   | 18.5 us                                                                                                           | 20.1 us: 1.09x slower                                                                                                   |
| dulwich_log                | 55.1 ms                                                                                                           | 60.3 ms: 1.09x slower                                                                                                   |
| k_core                     | 2.78 sec                                                                                                          | 3.05 sec: 1.10x slower                                                                                                  |
| scimark_sor                | 145 ms                                                                                                            | 160 ms: 1.10x slower                                                                                                    |
| async_generators           | 459 ms                                                                                                            | 506 ms: 1.10x slower                                                                                                    |
| pyflate                    | 534 ms                                                                                                            | 588 ms: 1.10x slower                                                                                                    |
| float                      | 84.9 ms                                                                                                           | 94.2 ms: 1.11x slower                                                                                                   |
| scimark_fft                | 424 ms                                                                                                            | 470 ms: 1.11x slower                                                                                                    |
| sphinx                     | 1.14 sec                                                                                                          | 1.27 sec: 1.11x slower                                                                                                  |
| html5lib                   | 63.5 ms                                                                                                           | 70.9 ms: 1.12x slower                                                                                                   |
| json                       | 5.65 ms                                                                                                           | 6.34 ms: 1.12x slower                                                                                                   |
| asyncio_tcp_ssl            | 2.14 sec                                                                                                          | 2.42 sec: 1.13x slower                                                                                                  |
| json_loads                 | 32.6 us                                                                                                           | 37.0 us: 1.14x slower                                                                                                   |
| hexiom                     | 6.80 ms                                                                                                           | 7.72 ms: 1.14x slower                                                                                                   |
| mdp                        | 1.70 sec                                                                                                          | 1.93 sec: 1.14x slower                                                                                                  |
| pickle_pure_python         | 387 us                                                                                                            | 441 us: 1.14x slower                                                                                                    |
| generators                 | 35.3 ms                                                                                                           | 40.4 ms: 1.14x slower                                                                                                   |
| deltablue                  | 4.05 ms                                                                                                           | 4.63 ms: 1.14x slower                                                                                                   |
| unpickle_pure_python       | 259 us                                                                                                            | 296 us: 1.15x slower                                                                                                    |
| 2to3                       | 303 ms                                                                                                            | 349 ms: 1.15x slower                                                                                                    |
| tomli_loads                | 2.44 sec                                                                                                          | 2.82 sec: 1.16x slower                                                                                                  |
| telco                      | 163 ms                                                                                                            | 189 ms: 1.16x slower                                                                                                    |
| connected_components       | 557 ms                                                                                                            | 649 ms: 1.16x slower                                                                                                    |
| nqueens                    | 99.7 ms                                                                                                           | 116 ms: 1.16x slower                                                                                                    |
| logging_simple             | 6.97 us                                                                                                           | 8.15 us: 1.17x slower                                                                                                   |
| go                         | 129 ms                                                                                                            | 151 ms: 1.17x slower                                                                                                    |
| pprint_safe_repr           | 900 ms                                                                                                            | 1.05 sec: 1.17x slower                                                                                                  |
| logging_format             | 7.75 us                                                                                                           | 9.10 us: 1.17x slower                                                                                                   |
| deepcopy                   | 331 us                                                                                                            | 390 us: 1.18x slower                                                                                                    |
| pprint_pformat             | 1.84 sec                                                                                                          | 2.17 sec: 1.18x slower                                                                                                  |
| shortest_path              | 582 ms                                                                                                            | 690 ms: 1.18x slower                                                                                                    |
| sqlglot_v2_normalize       | 127 ms                                                                                                            | 150 ms: 1.19x slower                                                                                                    |
| genshi_xml                 | 62.4 ms                                                                                                           | 74.6 ms: 1.20x slower                                                                                                   |
| raytrace                   | 328 ms                                                                                                            | 393 ms: 1.20x slower                                                                                                    |
| many_optionals             | 760 us                                                                                                            | 912 us: 1.20x slower                                                                                                    |
| pylint                     | 315 ms                                                                                                            | 379 ms: 1.20x slower                                                                                                    |
| comprehensions             | 20.3 us                                                                                                           | 24.4 us: 1.20x slower                                                                                                   |
| spectral_norm              | 118 ms                                                                                                            | 143 ms: 1.21x slower                                                                                                    |
| subparsers                 | 28.1 ms                                                                                                           | 34.2 ms: 1.21x slower                                                                                                   |
| regex_compile              | 122 ms                                                                                                            | 149 ms: 1.22x slower                                                                                                    |
| deepcopy_reduce            | 3.61 us                                                                                                           | 4.40 us: 1.22x slower                                                                                                   |
| chaos                      | 67.6 ms                                                                                                           | 82.8 ms: 1.22x slower                                                                                                   |
| sqlglot_v2_optimize        | 60.6 ms                                                                                                           | 74.5 ms: 1.23x slower                                                                                                   |
| sympy_integrate            | 20.5 ms                                                                                                           | 25.4 ms: 1.24x slower                                                                                                   |
| bpe_tokeniser              | 5.51 sec                                                                                                          | 6.87 sec: 1.25x slower                                                                                                  |
| deepcopy_memo              | 37.2 us                                                                                                           | 46.5 us: 1.25x slower                                                                                                   |
| xml_etree_generate         | 112 ms                                                                                                            | 140 ms: 1.25x slower                                                                                                    |
| typing_runtime_protocols   | 197 us                                                                                                            | 247 us: 1.25x slower                                                                                                    |
| django_template            | 40.6 ms                                                                                                           | 51.0 ms: 1.26x slower                                                                                                   |
| thrift                     | 957 us                                                                                                            | 1.20 ms: 1.26x slower                                                                                                   |
| sympy_expand               | 463 ms                                                                                                            | 584 ms: 1.26x slower                                                                                                    |
| sympy_sum                  | 145 ms                                                                                                            | 184 ms: 1.26x slower                                                                                                    |
| crypto_pyaes               | 86.4 ms                                                                                                           | 110 ms: 1.27x slower                                                                                                    |
| fannkuch                   | 470 ms                                                                                                            | 598 ms: 1.27x slower                                                                                                    |
| scimark_lu                 | 146 ms                                                                                                            | 186 ms: 1.28x slower                                                                                                    |
| sqlglot_v2_parse           | 1.43 ms                                                                                                           | 1.85 ms: 1.29x slower                                                                                                   |
| meteor_contest             | 107 ms                                                                                                            | 139 ms: 1.29x slower                                                                                                    |
| sympy_str                  | 262 ms                                                                                                            | 339 ms: 1.29x slower                                                                                                    |
| sqlglot_v2_transpile       | 1.79 ms                                                                                                           | 2.32 ms: 1.29x slower                                                                                                   |
| xml_etree_process          | 79.0 ms                                                                                                           | 102 ms: 1.30x slower                                                                                                    |
| scimark_monte_carlo        | 80.2 ms                                                                                                           | 107 ms: 1.33x slower                                                                                                    |
| richards                   | 53.1 ms                                                                                                           | 70.8 ms: 1.33x slower                                                                                                   |
| bench_thread_pool          | 1.37 ms                                                                                                           | 1.82 ms: 1.33x slower                                                                                                   |
| python_startup             | 14.8 ms                                                                                                           | 20.0 ms: 1.35x slower                                                                                                   |
| richards_super             | 58.8 ms                                                                                                           | 79.8 ms: 1.36x slower                                                                                                   |
| genshi_text                | 26.8 ms                                                                                                           | 36.7 ms: 1.37x slower                                                                                                   |
| coverage                   | 104 ms                                                                                                            | 144 ms: 1.39x slower                                                                                                    |
| python_startup_no_site     | 8.42 ms                                                                                                           | 12.0 ms: 1.43x slower                                                                                                   |
| unpack_sequence            | 50.2 ns                                                                                                           | 72.7 ns: 1.45x slower                                                                                                   |
| nbody                      | 120 ms                                                                                                            | 180 ms: 1.50x slower                                                                                                    |
| mako                       | 13.6 ms                                                                                                           | 21.3 ms: 1.57x slower                                                                                                   |
| Geometric mean             | (ref)                                                                                                             | 1.09x slower                                                                                                            |

Benchmark hidden because not significant (8): regex_effbot, pidigits, pickle, async_tree_cpu_io_mixed, pickle_list, asyncio_websockets, pickle_dict, pathlib
Ignored benchmarks (1) of results/bm-20250719-3.15.0a0-800d37f/bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json: djangocms

- Geometric mean (including insignificant results): 1.122x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.12x
- 95% likely to have a slowdown of 1.12x
- 99% likely to have a slowdown of 1.11x

# Memory
- memory change: 1.20x