# Results vs. base

- fork: python
- ref: 425f60b9eb253c57bc32
- machine: linux-aarch64
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.145x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x slower
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250329-3.14.0a6+-425f60b/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json | results/bm-20250329-3.14.0a6+-425f60b-NOGIL/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 297 ms                                                                                                              | 359 ms: 1.21x slower                                                                                                      |
| docutils       | 2.95 sec                                                                                                            | 3.31 sec: 1.12x slower                                                                                                    |
| html5lib       | 63.3 ms                                                                                                             | 74.7 ms: 1.18x slower                                                                                                     |
| sphinx         | 1.14 sec                                                                                                            | 1.34 sec: 1.17x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.17x slower                                                                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | results/bm-20250329-3.14.0a6+-425f60b/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json | results/bm-20250329-3.14.0a6+-425f60b-NOGIL/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json |
|---------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg          | 890 ms                                                                                                              | 861 ms: 1.03x faster                                                                                                      |
| async_tree_memoization_tg | 465 ms                                                                                                              | 457 ms: 1.02x faster                                                                                                      |
| async_tree_io             | 876 ms                                                                                                              | 904 ms: 1.03x slower                                                                                                      |
| async_tree_cpu_io_mixed   | 660 ms                                                                                                              | 683 ms: 1.03x slower                                                                                                      |
| asyncio_tcp               | 550 ms                                                                                                              | 579 ms: 1.05x slower                                                                                                      |
| async_tree_memoization    | 470 ms                                                                                                              | 497 ms: 1.06x slower                                                                                                      |
| async_tree_none           | 392 ms                                                                                                              | 418 ms: 1.07x slower                                                                                                      |
| asyncio_tcp_ssl           | 2.17 sec                                                                                                            | 2.44 sec: 1.12x slower                                                                                                    |
| async_generators          | 441 ms                                                                                                              | 519 ms: 1.18x slower                                                                                                      |
| Geometric mean            | (ref)                                                                                                               | 1.04x slower                                                                                                              |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_none_tg, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250329-3.14.0a6+-425f60b/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json | results/bm-20250329-3.14.0a6+-425f60b-NOGIL/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| float          | 85.6 ms                                                                                                             | 101 ms: 1.18x slower                                                                                                      |
| nbody          | 128 ms                                                                                                              | 182 ms: 1.43x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.18x slower                                                                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250329-3.14.0a6+-425f60b/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json | results/bm-20250329-3.14.0a6+-425f60b-NOGIL/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 246 ms                                                                                                              | 253 ms: 1.03x slower                                                                                                      |
| regex_compile  | 123 ms                                                                                                              | 160 ms: 1.30x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.06x slower                                                                                                              |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250329-3.14.0a6+-425f60b/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json | results/bm-20250329-3.14.0a6+-425f60b-NOGIL/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json |
|----------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 141 ms                                                                                                              | 130 ms: 1.08x faster                                                                                                      |
| pickle_list          | 5.63 us                                                                                                             | 5.67 us: 1.01x slower                                                                                                     |
| unpickle             | 18.0 us                                                                                                             | 19.6 us: 1.09x slower                                                                                                     |
| json_loads           | 35.0 us                                                                                                             | 38.4 us: 1.10x slower                                                                                                     |
| json_dumps           | 14.9 ms                                                                                                             | 16.6 ms: 1.11x slower                                                                                                     |
| unpickle_list        | 6.35 us                                                                                                             | 7.21 us: 1.14x slower                                                                                                     |
| unpickle_pure_python | 263 us                                                                                                              | 303 us: 1.15x slower                                                                                                      |
| pickle_pure_python   | 386 us                                                                                                              | 448 us: 1.16x slower                                                                                                      |
| xml_etree_generate   | 113 ms                                                                                                              | 139 ms: 1.22x slower                                                                                                      |
| tomli_loads          | 2.46 sec                                                                                                            | 3.05 sec: 1.24x slower                                                                                                    |
| xml_etree_process    | 78.4 ms                                                                                                             | 100 ms: 1.28x slower                                                                                                      |
| Geometric mean       | (ref)                                                                                                               | 1.10x slower                                                                                                              |

Benchmark hidden because not significant (3): pickle, pickle_dict, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250329-3.14.0a6+-425f60b/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json | results/bm-20250329-3.14.0a6+-425f60b-NOGIL/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json |
|------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 16.3 ms                                                                                                             | 19.6 ms: 1.20x slower                                                                                                     |
| python_startup_no_site | 10.2 ms                                                                                                             | 14.0 ms: 1.38x slower                                                                                                     |
| Geometric mean         | (ref)                                                                                                               | 1.29x slower                                                                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250329-3.14.0a6+-425f60b/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json | results/bm-20250329-3.14.0a6+-425f60b-NOGIL/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json |
|-----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 59.0 ms                                                                                                             | 74.0 ms: 1.25x slower                                                                                                     |
| genshi_text     | 27.1 ms                                                                                                             | 36.5 ms: 1.35x slower                                                                                                     |
| django_template | 39.8 ms                                                                                                             | 53.9 ms: 1.35x slower                                                                                                     |
| mako            | 14.5 ms                                                                                                             | 22.3 ms: 1.54x slower                                                                                                     |
| Geometric mean  | (ref)                                                                                                               | 1.37x slower                                                                                                              |

All benchmarks:
===============

| Benchmark                 | results/bm-20250329-3.14.0a6+-425f60b/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json | results/bm-20250329-3.14.0a6+-425f60b-NOGIL/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json |
|---------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool             | 1.93 sec                                                                                                            | 57.2 ms: 33.74x faster                                                                                                    |
| gc_traversal              | 6.65 ms                                                                                                             | 2.69 ms: 2.47x faster                                                                                                     |
| create_gc_cycles          | 3.63 ms                                                                                                             | 2.12 ms: 1.71x faster                                                                                                     |
| xml_etree_iterparse       | 141 ms                                                                                                              | 130 ms: 1.08x faster                                                                                                      |
| sqlite_synth              | 3.84 us                                                                                                             | 3.59 us: 1.07x faster                                                                                                     |
| async_tree_io_tg          | 890 ms                                                                                                              | 861 ms: 1.03x faster                                                                                                      |
| async_tree_memoization_tg | 465 ms                                                                                                              | 457 ms: 1.02x faster                                                                                                      |
| pickle_list               | 5.63 us                                                                                                             | 5.67 us: 1.01x slower                                                                                                     |
| regex_dna                 | 246 ms                                                                                                              | 253 ms: 1.03x slower                                                                                                      |
| async_tree_io             | 876 ms                                                                                                              | 904 ms: 1.03x slower                                                                                                      |
| async_tree_cpu_io_mixed   | 660 ms                                                                                                              | 683 ms: 1.03x slower                                                                                                      |
| pathlib                   | 21.9 ms                                                                                                             | 23.1 ms: 1.05x slower                                                                                                     |
| asyncio_tcp               | 550 ms                                                                                                              | 579 ms: 1.05x slower                                                                                                      |
| async_tree_memoization    | 470 ms                                                                                                              | 497 ms: 1.06x slower                                                                                                      |
| async_tree_none           | 392 ms                                                                                                              | 418 ms: 1.07x slower                                                                                                      |
| generators                | 35.7 ms                                                                                                             | 38.8 ms: 1.09x slower                                                                                                     |
| unpickle                  | 18.0 us                                                                                                             | 19.6 us: 1.09x slower                                                                                                     |
| json_loads                | 35.0 us                                                                                                             | 38.4 us: 1.10x slower                                                                                                     |
| dulwich_log               | 53.7 ms                                                                                                             | 59.1 ms: 1.10x slower                                                                                                     |
| pycparser                 | 1.25 sec                                                                                                            | 1.39 sec: 1.11x slower                                                                                                    |
| json_dumps                | 14.9 ms                                                                                                             | 16.6 ms: 1.11x slower                                                                                                     |
| json                      | 5.81 ms                                                                                                             | 6.47 ms: 1.11x slower                                                                                                     |
| k_core                    | 2.78 sec                                                                                                            | 3.11 sec: 1.12x slower                                                                                                    |
| asyncio_tcp_ssl           | 2.17 sec                                                                                                            | 2.44 sec: 1.12x slower                                                                                                    |
| spectral_norm             | 125 ms                                                                                                              | 140 ms: 1.12x slower                                                                                                      |
| docutils                  | 2.95 sec                                                                                                            | 3.31 sec: 1.12x slower                                                                                                    |
| pyflate                   | 554 ms                                                                                                              | 627 ms: 1.13x slower                                                                                                      |
| unpickle_list             | 6.35 us                                                                                                             | 7.21 us: 1.14x slower                                                                                                     |
| scimark_fft               | 422 ms                                                                                                              | 480 ms: 1.14x slower                                                                                                      |
| logging_silent            | 128 ns                                                                                                              | 148 ns: 1.15x slower                                                                                                      |
| unpickle_pure_python      | 263 us                                                                                                              | 303 us: 1.15x slower                                                                                                      |
| scimark_sor               | 147 ms                                                                                                              | 170 ms: 1.16x slower                                                                                                      |
| pickle_pure_python        | 386 us                                                                                                              | 448 us: 1.16x slower                                                                                                      |
| connected_components      | 556 ms                                                                                                              | 647 ms: 1.16x slower                                                                                                      |
| shortest_path             | 577 ms                                                                                                              | 676 ms: 1.17x slower                                                                                                      |
| sphinx                    | 1.14 sec                                                                                                            | 1.34 sec: 1.17x slower                                                                                                    |
| nqueens                   | 103 ms                                                                                                              | 121 ms: 1.17x slower                                                                                                      |
| sqlglot_v2_normalize      | 129 ms                                                                                                              | 152 ms: 1.17x slower                                                                                                      |
| float                     | 85.6 ms                                                                                                             | 101 ms: 1.18x slower                                                                                                      |
| pprint_safe_repr          | 938 ms                                                                                                              | 1.10 sec: 1.18x slower                                                                                                    |
| deepcopy                  | 340 us                                                                                                              | 401 us: 1.18x slower                                                                                                      |
| async_generators          | 441 ms                                                                                                              | 519 ms: 1.18x slower                                                                                                      |
| hexiom                    | 7.30 ms                                                                                                             | 8.61 ms: 1.18x slower                                                                                                     |
| pprint_pformat            | 1.94 sec                                                                                                            | 2.29 sec: 1.18x slower                                                                                                    |
| html5lib                  | 63.3 ms                                                                                                             | 74.7 ms: 1.18x slower                                                                                                     |
| deepcopy_reduce           | 3.68 us                                                                                                             | 4.42 us: 1.20x slower                                                                                                     |
| python_startup            | 16.3 ms                                                                                                             | 19.6 ms: 1.20x slower                                                                                                     |
| pylint                    | 310 ms                                                                                                              | 374 ms: 1.20x slower                                                                                                      |
| telco                     | 9.58 ms                                                                                                             | 11.5 ms: 1.21x slower                                                                                                     |
| mdp                       | 1.65 sec                                                                                                            | 1.99 sec: 1.21x slower                                                                                                    |
| 2to3                      | 297 ms                                                                                                              | 359 ms: 1.21x slower                                                                                                      |
| sqlglot_v2_optimize       | 62.3 ms                                                                                                             | 75.5 ms: 1.21x slower                                                                                                     |
| xml_etree_generate        | 113 ms                                                                                                              | 139 ms: 1.22x slower                                                                                                      |
| many_optionals            | 836 us                                                                                                              | 1.02 ms: 1.22x slower                                                                                                     |
| chaos                     | 69.3 ms                                                                                                             | 85.1 ms: 1.23x slower                                                                                                     |
| subparsers                | 25.6 ms                                                                                                             | 31.6 ms: 1.23x slower                                                                                                     |
| tomli_loads               | 2.46 sec                                                                                                            | 3.05 sec: 1.24x slower                                                                                                    |
| fannkuch                  | 502 ms                                                                                                              | 625 ms: 1.24x slower                                                                                                      |
| unpack_sequence           | 60.4 ns                                                                                                             | 75.3 ns: 1.25x slower                                                                                                     |
| go                        | 137 ms                                                                                                              | 171 ms: 1.25x slower                                                                                                      |
| genshi_xml                | 59.0 ms                                                                                                             | 74.0 ms: 1.25x slower                                                                                                     |
| comprehensions            | 21.3 us                                                                                                             | 26.8 us: 1.26x slower                                                                                                     |
| logging_simple            | 6.93 us                                                                                                             | 8.80 us: 1.27x slower                                                                                                     |
| xml_etree_process         | 78.4 ms                                                                                                             | 100 ms: 1.28x slower                                                                                                      |
| scimark_sparse_mat_mult   | 6.35 ms                                                                                                             | 8.11 ms: 1.28x slower                                                                                                     |
| logging_format            | 7.62 us                                                                                                             | 9.75 us: 1.28x slower                                                                                                     |
| deepcopy_memo             | 39.5 us                                                                                                             | 50.7 us: 1.28x slower                                                                                                     |
| sympy_expand              | 467 ms                                                                                                              | 603 ms: 1.29x slower                                                                                                      |
| raytrace                  | 313 ms                                                                                                              | 405 ms: 1.29x slower                                                                                                      |
| bpe_tokeniser             | 5.55 sec                                                                                                            | 7.18 sec: 1.29x slower                                                                                                    |
| regex_compile             | 123 ms                                                                                                              | 160 ms: 1.30x slower                                                                                                      |
| sympy_integrate           | 21.0 ms                                                                                                             | 27.4 ms: 1.31x slower                                                                                                     |
| scimark_lu                | 140 ms                                                                                                              | 186 ms: 1.32x slower                                                                                                      |
| deltablue                 | 3.79 ms                                                                                                             | 5.01 ms: 1.32x slower                                                                                                     |
| crypto_pyaes              | 85.3 ms                                                                                                             | 113 ms: 1.32x slower                                                                                                      |
| meteor_contest            | 113 ms                                                                                                              | 150 ms: 1.33x slower                                                                                                      |
| sympy_str                 | 263 ms                                                                                                              | 353 ms: 1.34x slower                                                                                                      |
| sympy_sum                 | 142 ms                                                                                                              | 191 ms: 1.34x slower                                                                                                      |
| sqlalchemy_declarative    | 146 ms                                                                                                              | 196 ms: 1.34x slower                                                                                                      |
| genshi_text               | 27.1 ms                                                                                                             | 36.5 ms: 1.35x slower                                                                                                     |
| django_template           | 39.8 ms                                                                                                             | 53.9 ms: 1.35x slower                                                                                                     |
| scimark_monte_carlo       | 83.0 ms                                                                                                             | 113 ms: 1.36x slower                                                                                                      |
| typing_runtime_protocols  | 194 us                                                                                                              | 265 us: 1.37x slower                                                                                                      |
| bench_thread_pool         | 1.33 ms                                                                                                             | 1.82 ms: 1.37x slower                                                                                                     |
| sqlalchemy_imperative     | 15.5 ms                                                                                                             | 21.2 ms: 1.37x slower                                                                                                     |
| python_startup_no_site    | 10.2 ms                                                                                                             | 14.0 ms: 1.38x slower                                                                                                     |
| sqlglot_v2_transpile      | 1.74 ms                                                                                                             | 2.41 ms: 1.38x slower                                                                                                     |
| sqlglot_v2_parse          | 1.40 ms                                                                                                             | 1.94 ms: 1.39x slower                                                                                                     |
| nbody                     | 128 ms                                                                                                              | 182 ms: 1.43x slower                                                                                                      |
| richards                  | 50.7 ms                                                                                                             | 73.9 ms: 1.46x slower                                                                                                     |
| richards_super            | 57.3 ms                                                                                                             | 83.8 ms: 1.46x slower                                                                                                     |
| coverage                  | 99.0 ms                                                                                                             | 149 ms: 1.50x slower                                                                                                      |
| mako                      | 14.5 ms                                                                                                             | 22.3 ms: 1.54x slower                                                                                                     |
| Geometric mean            | (ref)                                                                                                               | 1.12x slower                                                                                                              |

Benchmark hidden because not significant (10): regex_v8, pidigits, regex_effbot, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_none_tg, pickle, pickle_dict, xml_etree_parse, coroutines

- Geometric mean (including insignificant results): 1.145x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.15x
- 95% likely to have a slowdown of 1.15x
- 99% likely to have a slowdown of 1.13x

# Memory
- memory change: 1.22x