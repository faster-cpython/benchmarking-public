# Results vs. base

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: linux-aarch64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.125x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x slower
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-NOGIL/bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 301 ms                                                                                                            | 350 ms: 1.16x slower                                                                                                    |
| docutils       | 2.94 sec                                                                                                          | 3.16 sec: 1.08x slower                                                                                                  |
| html5lib       | 60.8 ms                                                                                                           | 70.0 ms: 1.15x slower                                                                                                   |
| sphinx         | 1.13 sec                                                                                                          | 1.27 sec: 1.12x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.13x slower                                                                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-NOGIL/bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 906 ms                                                                                                            | 827 ms: 1.10x faster                                                                                                    |
| async_tree_io              | 879 ms                                                                                                            | 846 ms: 1.04x faster                                                                                                    |
| async_tree_memoization_tg  | 451 ms                                                                                                            | 438 ms: 1.03x faster                                                                                                    |
| async_tree_cpu_io_mixed_tg | 646 ms                                                                                                            | 633 ms: 1.02x faster                                                                                                    |
| async_tree_none            | 383 ms                                                                                                            | 390 ms: 1.02x slower                                                                                                    |
| async_tree_memoization     | 456 ms                                                                                                            | 470 ms: 1.03x slower                                                                                                    |
| asyncio_tcp                | 531 ms                                                                                                            | 559 ms: 1.05x slower                                                                                                    |
| coroutines                 | 29.5 ms                                                                                                           | 31.6 ms: 1.07x slower                                                                                                   |
| asyncio_tcp_ssl            | 2.18 sec                                                                                                          | 2.43 sec: 1.11x slower                                                                                                  |
| async_generators           | 453 ms                                                                                                            | 519 ms: 1.14x slower                                                                                                    |
| Geometric mean             | (ref)                                                                                                             | 1.02x slower                                                                                                            |

Benchmark hidden because not significant (3): asyncio_websockets, async_tree_none_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-NOGIL/bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                                                                           | 94.0 ms: 1.11x slower                                                                                                   |
| nbody          | 124 ms                                                                                                            | 183 ms: 1.47x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.17x slower                                                                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-NOGIL/bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 222 ms                                                                                                            | 238 ms: 1.07x slower                                                                                                    |
| regex_compile  | 121 ms                                                                                                            | 153 ms: 1.26x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.06x slower                                                                                                            |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-NOGIL/bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 141 ms                                                                                                            | 130 ms: 1.08x faster                                                                                                    |
| pickle_list          | 5.59 us                                                                                                           | 5.83 us: 1.04x slower                                                                                                   |
| xml_etree_parse      | 178 ms                                                                                                            | 186 ms: 1.05x slower                                                                                                    |
| unpickle_list        | 6.47 us                                                                                                           | 6.87 us: 1.06x slower                                                                                                   |
| json_dumps           | 13.7 ms                                                                                                           | 14.9 ms: 1.08x slower                                                                                                   |
| unpickle             | 18.5 us                                                                                                           | 20.1 us: 1.09x slower                                                                                                   |
| json_loads           | 33.1 us                                                                                                           | 36.6 us: 1.11x slower                                                                                                   |
| pickle_pure_python   | 396 us                                                                                                            | 442 us: 1.12x slower                                                                                                    |
| unpickle_pure_python | 261 us                                                                                                            | 300 us: 1.15x slower                                                                                                    |
| tomli_loads          | 2.45 sec                                                                                                          | 2.86 sec: 1.17x slower                                                                                                  |
| xml_etree_generate   | 110 ms                                                                                                            | 139 ms: 1.27x slower                                                                                                    |
| xml_etree_process    | 78.6 ms                                                                                                           | 101 ms: 1.28x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                             | 1.09x slower                                                                                                            |

Benchmark hidden because not significant (2): pickle, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-NOGIL/bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 15.1 ms                                                                                                           | 19.9 ms: 1.32x slower                                                                                                   |
| python_startup_no_site | 8.58 ms                                                                                                           | 12.0 ms: 1.40x slower                                                                                                   |
| Geometric mean         | (ref)                                                                                                             | 1.36x slower                                                                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-NOGIL/bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 60.7 ms                                                                                                           | 76.0 ms: 1.25x slower                                                                                                   |
| django_template | 40.2 ms                                                                                                           | 50.9 ms: 1.27x slower                                                                                                   |
| genshi_text     | 27.4 ms                                                                                                           | 36.2 ms: 1.32x slower                                                                                                   |
| mako            | 13.8 ms                                                                                                           | 21.4 ms: 1.55x slower                                                                                                   |
| Geometric mean  | (ref)                                                                                                             | 1.34x slower                                                                                                            |

All benchmarks:
===============

| Benchmark                  | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-NOGIL/bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool              | 2.99 sec                                                                                                          | 63.8 ms: 46.86x faster                                                                                                  |
| gc_traversal               | 6.88 ms                                                                                                           | 2.87 ms: 2.39x faster                                                                                                   |
| create_gc_cycles           | 3.74 ms                                                                                                           | 2.27 ms: 1.65x faster                                                                                                   |
| async_tree_io_tg           | 906 ms                                                                                                            | 827 ms: 1.10x faster                                                                                                    |
| sqlite_synth               | 3.75 us                                                                                                           | 3.44 us: 1.09x faster                                                                                                   |
| xml_etree_iterparse        | 141 ms                                                                                                            | 130 ms: 1.08x faster                                                                                                    |
| async_tree_io              | 879 ms                                                                                                            | 846 ms: 1.04x faster                                                                                                    |
| async_tree_memoization_tg  | 451 ms                                                                                                            | 438 ms: 1.03x faster                                                                                                    |
| async_tree_cpu_io_mixed_tg | 646 ms                                                                                                            | 633 ms: 1.02x faster                                                                                                    |
| async_tree_none            | 383 ms                                                                                                            | 390 ms: 1.02x slower                                                                                                    |
| async_tree_memoization     | 456 ms                                                                                                            | 470 ms: 1.03x slower                                                                                                    |
| pickle_list                | 5.59 us                                                                                                           | 5.83 us: 1.04x slower                                                                                                   |
| pathlib                    | 21.7 ms                                                                                                           | 22.6 ms: 1.04x slower                                                                                                   |
| xml_etree_parse            | 178 ms                                                                                                            | 186 ms: 1.05x slower                                                                                                    |
| asyncio_tcp                | 531 ms                                                                                                            | 559 ms: 1.05x slower                                                                                                    |
| unpickle_list              | 6.47 us                                                                                                           | 6.87 us: 1.06x slower                                                                                                   |
| pycparser                  | 1.24 sec                                                                                                          | 1.33 sec: 1.07x slower                                                                                                  |
| regex_dna                  | 222 ms                                                                                                            | 238 ms: 1.07x slower                                                                                                    |
| coroutines                 | 29.5 ms                                                                                                           | 31.6 ms: 1.07x slower                                                                                                   |
| docutils                   | 2.94 sec                                                                                                          | 3.16 sec: 1.08x slower                                                                                                  |
| json                       | 5.81 ms                                                                                                           | 6.25 ms: 1.08x slower                                                                                                   |
| json_dumps                 | 13.7 ms                                                                                                           | 14.9 ms: 1.08x slower                                                                                                   |
| logging_silent             | 128 ns                                                                                                            | 139 ns: 1.09x slower                                                                                                    |
| unpickle                   | 18.5 us                                                                                                           | 20.1 us: 1.09x slower                                                                                                   |
| scimark_sparse_mat_mult    | 7.05 ms                                                                                                           | 7.73 ms: 1.10x slower                                                                                                   |
| k_core                     | 2.77 sec                                                                                                          | 3.03 sec: 1.10x slower                                                                                                  |
| dulwich_log                | 53.9 ms                                                                                                           | 59.1 ms: 1.10x slower                                                                                                   |
| scimark_fft                | 422 ms                                                                                                            | 466 ms: 1.10x slower                                                                                                    |
| json_loads                 | 33.1 us                                                                                                           | 36.6 us: 1.11x slower                                                                                                   |
| float                      | 84.7 ms                                                                                                           | 94.0 ms: 1.11x slower                                                                                                   |
| asyncio_tcp_ssl            | 2.18 sec                                                                                                          | 2.43 sec: 1.11x slower                                                                                                  |
| many_optionals             | 973 us                                                                                                            | 1.08 ms: 1.11x slower                                                                                                   |
| pickle_pure_python         | 396 us                                                                                                            | 442 us: 1.12x slower                                                                                                    |
| hexiom                     | 6.92 ms                                                                                                           | 7.77 ms: 1.12x slower                                                                                                   |
| sphinx                     | 1.13 sec                                                                                                          | 1.27 sec: 1.12x slower                                                                                                  |
| pyflate                    | 515 ms                                                                                                            | 584 ms: 1.13x slower                                                                                                    |
| telco                      | 164 ms                                                                                                            | 186 ms: 1.14x slower                                                                                                    |
| scimark_sor                | 142 ms                                                                                                            | 162 ms: 1.14x slower                                                                                                    |
| async_generators           | 453 ms                                                                                                            | 519 ms: 1.14x slower                                                                                                    |
| mdp                        | 1.68 sec                                                                                                          | 1.93 sec: 1.15x slower                                                                                                  |
| unpickle_pure_python       | 261 us                                                                                                            | 300 us: 1.15x slower                                                                                                    |
| html5lib                   | 60.8 ms                                                                                                           | 70.0 ms: 1.15x slower                                                                                                   |
| generators                 | 35.3 ms                                                                                                           | 40.7 ms: 1.15x slower                                                                                                   |
| pylint                     | 321 ms                                                                                                            | 373 ms: 1.16x slower                                                                                                    |
| shortest_path              | 585 ms                                                                                                            | 678 ms: 1.16x slower                                                                                                    |
| 2to3                       | 301 ms                                                                                                            | 350 ms: 1.16x slower                                                                                                    |
| pprint_safe_repr           | 896 ms                                                                                                            | 1.04 sec: 1.17x slower                                                                                                  |
| tomli_loads                | 2.45 sec                                                                                                          | 2.86 sec: 1.17x slower                                                                                                  |
| deepcopy                   | 329 us                                                                                                            | 386 us: 1.17x slower                                                                                                    |
| pprint_pformat             | 1.82 sec                                                                                                          | 2.14 sec: 1.17x slower                                                                                                  |
| chaos                      | 69.5 ms                                                                                                           | 82.0 ms: 1.18x slower                                                                                                   |
| nqueens                    | 98.2 ms                                                                                                           | 116 ms: 1.18x slower                                                                                                    |
| connected_components       | 553 ms                                                                                                            | 654 ms: 1.18x slower                                                                                                    |
| go                         | 128 ms                                                                                                            | 152 ms: 1.19x slower                                                                                                    |
| sqlglot_v2_optimize        | 61.4 ms                                                                                                           | 73.4 ms: 1.19x slower                                                                                                   |
| logging_simple             | 6.90 us                                                                                                           | 8.24 us: 1.19x slower                                                                                                   |
| sqlglot_v2_normalize       | 125 ms                                                                                                            | 151 ms: 1.20x slower                                                                                                    |
| comprehensions             | 19.9 us                                                                                                           | 24.1 us: 1.21x slower                                                                                                   |
| logging_format             | 7.56 us                                                                                                           | 9.21 us: 1.22x slower                                                                                                   |
| subparsers                 | 47.5 ms                                                                                                           | 58.0 ms: 1.22x slower                                                                                                   |
| spectral_norm              | 118 ms                                                                                                            | 144 ms: 1.22x slower                                                                                                    |
| deltablue                  | 3.91 ms                                                                                                           | 4.80 ms: 1.23x slower                                                                                                   |
| sympy_str                  | 274 ms                                                                                                            | 337 ms: 1.23x slower                                                                                                    |
| thrift                     | 980 us                                                                                                            | 1.20 ms: 1.23x slower                                                                                                   |
| deepcopy_memo              | 36.7 us                                                                                                           | 45.3 us: 1.23x slower                                                                                                   |
| raytrace                   | 323 ms                                                                                                            | 398 ms: 1.24x slower                                                                                                    |
| genshi_xml                 | 60.7 ms                                                                                                           | 76.0 ms: 1.25x slower                                                                                                   |
| typing_runtime_protocols   | 195 us                                                                                                            | 244 us: 1.25x slower                                                                                                    |
| bpe_tokeniser              | 5.52 sec                                                                                                          | 6.92 sec: 1.25x slower                                                                                                  |
| deepcopy_reduce            | 3.50 us                                                                                                           | 4.39 us: 1.26x slower                                                                                                   |
| regex_compile              | 121 ms                                                                                                            | 153 ms: 1.26x slower                                                                                                    |
| meteor_contest             | 111 ms                                                                                                            | 139 ms: 1.26x slower                                                                                                    |
| django_template            | 40.2 ms                                                                                                           | 50.9 ms: 1.27x slower                                                                                                   |
| sympy_expand               | 463 ms                                                                                                            | 586 ms: 1.27x slower                                                                                                    |
| xml_etree_generate         | 110 ms                                                                                                            | 139 ms: 1.27x slower                                                                                                    |
| richards_super             | 63.2 ms                                                                                                           | 80.3 ms: 1.27x slower                                                                                                   |
| crypto_pyaes               | 84.1 ms                                                                                                           | 107 ms: 1.27x slower                                                                                                    |
| fannkuch                   | 462 ms                                                                                                            | 588 ms: 1.27x slower                                                                                                    |
| sympy_integrate            | 20.1 ms                                                                                                           | 25.6 ms: 1.28x slower                                                                                                   |
| xml_etree_process          | 78.6 ms                                                                                                           | 101 ms: 1.28x slower                                                                                                    |
| scimark_monte_carlo        | 80.3 ms                                                                                                           | 103 ms: 1.29x slower                                                                                                    |
| sqlglot_v2_parse           | 1.44 ms                                                                                                           | 1.86 ms: 1.29x slower                                                                                                   |
| sqlglot_v2_transpile       | 1.75 ms                                                                                                           | 2.28 ms: 1.31x slower                                                                                                   |
| scimark_lu                 | 142 ms                                                                                                            | 186 ms: 1.31x slower                                                                                                    |
| sympy_sum                  | 142 ms                                                                                                            | 186 ms: 1.31x slower                                                                                                    |
| genshi_text                | 27.4 ms                                                                                                           | 36.2 ms: 1.32x slower                                                                                                   |
| python_startup             | 15.1 ms                                                                                                           | 19.9 ms: 1.32x slower                                                                                                   |
| richards                   | 53.5 ms                                                                                                           | 70.7 ms: 1.32x slower                                                                                                   |
| bench_thread_pool          | 1.36 ms                                                                                                           | 1.80 ms: 1.32x slower                                                                                                   |
| coverage                   | 102 ms                                                                                                            | 142 ms: 1.39x slower                                                                                                    |
| python_startup_no_site     | 8.58 ms                                                                                                           | 12.0 ms: 1.40x slower                                                                                                   |
| nbody                      | 124 ms                                                                                                            | 183 ms: 1.47x slower                                                                                                    |
| unpack_sequence            | 49.6 ns                                                                                                           | 74.4 ns: 1.50x slower                                                                                                   |
| mako                       | 13.8 ms                                                                                                           | 21.4 ms: 1.55x slower                                                                                                   |
| Geometric mean             | (ref)                                                                                                             | 1.09x slower                                                                                                            |

Benchmark hidden because not significant (8): regex_v8, pickle, pidigits, asyncio_websockets, regex_effbot, async_tree_none_tg, async_tree_cpu_io_mixed, pickle_dict
Ignored benchmarks (1) of results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: djangocms

- Geometric mean (including insignificant results): 1.125x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.13x
- 95% likely to have a slowdown of 1.12x
- 99% likely to have a slowdown of 1.11x

# Memory
- memory change: 1.20x