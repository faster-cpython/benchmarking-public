# Results vs. base

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: linux-aarch64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.158x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x slower
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json | results/bm-20250201-3.14.0a4+-cf4c4ec-NOGIL/bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 301 ms                                                                                                              | 379 ms: 1.26x slower                                                                                                      |
| docutils       | 2.96 sec                                                                                                            | 3.38 sec: 1.14x slower                                                                                                    |
| html5lib       | 66.0 ms                                                                                                             | 75.6 ms: 1.15x slower                                                                                                     |
| sphinx         | 1.16 sec                                                                                                            | 1.37 sec: 1.17x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.18x slower                                                                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json | results/bm-20250201-3.14.0a4+-cf4c4ec-NOGIL/bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 671 ms                                                                                                              | 695 ms: 1.04x slower                                                                                                      |
| async_tree_cpu_io_mixed    | 694 ms                                                                                                              | 722 ms: 1.04x slower                                                                                                      |
| async_tree_io              | 924 ms                                                                                                              | 966 ms: 1.05x slower                                                                                                      |
| async_tree_memoization_tg  | 481 ms                                                                                                              | 503 ms: 1.05x slower                                                                                                      |
| async_tree_none_tg         | 395 ms                                                                                                              | 414 ms: 1.05x slower                                                                                                      |
| async_tree_memoization     | 505 ms                                                                                                              | 549 ms: 1.09x slower                                                                                                      |
| async_tree_none            | 402 ms                                                                                                              | 443 ms: 1.10x slower                                                                                                      |
| asyncio_tcp                | 546 ms                                                                                                              | 611 ms: 1.12x slower                                                                                                      |
| asyncio_tcp_ssl            | 2.26 sec                                                                                                            | 2.56 sec: 1.14x slower                                                                                                    |
| async_generators           | 450 ms                                                                                                              | 542 ms: 1.20x slower                                                                                                      |
| Geometric mean             | (ref)                                                                                                               | 1.07x slower                                                                                                              |

Benchmark hidden because not significant (3): async_tree_io_tg, asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json | results/bm-20250201-3.14.0a4+-cf4c4ec-NOGIL/bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| float          | 88.2 ms                                                                                                             | 103 ms: 1.17x slower                                                                                                      |
| nbody          | 123 ms                                                                                                              | 188 ms: 1.53x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.21x slower                                                                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json | results/bm-20250201-3.14.0a4+-cf4c4ec-NOGIL/bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 247 ms                                                                                                              | 261 ms: 1.06x slower                                                                                                      |
| regex_compile  | 127 ms                                                                                                              | 158 ms: 1.25x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.06x slower                                                                                                              |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json | results/bm-20250201-3.14.0a4+-cf4c4ec-NOGIL/bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json |
|----------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 147 ms                                                                                                              | 130 ms: 1.13x faster                                                                                                      |
| unpickle             | 18.6 us                                                                                                             | 19.9 us: 1.07x slower                                                                                                     |
| json_loads           | 34.5 us                                                                                                             | 38.3 us: 1.11x slower                                                                                                     |
| unpickle_list        | 6.68 us                                                                                                             | 7.45 us: 1.12x slower                                                                                                     |
| json_dumps           | 14.7 ms                                                                                                             | 17.1 ms: 1.16x slower                                                                                                     |
| unpickle_pure_python | 262 us                                                                                                              | 308 us: 1.18x slower                                                                                                      |
| pickle_pure_python   | 398 us                                                                                                              | 484 us: 1.22x slower                                                                                                      |
| xml_etree_generate   | 116 ms                                                                                                              | 143 ms: 1.23x slower                                                                                                      |
| tomli_loads          | 2.58 sec                                                                                                            | 3.20 sec: 1.24x slower                                                                                                    |
| xml_etree_process    | 80.5 ms                                                                                                             | 103 ms: 1.28x slower                                                                                                      |
| Geometric mean       | (ref)                                                                                                               | 1.10x slower                                                                                                              |

Benchmark hidden because not significant (4): pickle, pickle_list, xml_etree_parse, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json | results/bm-20250201-3.14.0a4+-cf4c4ec-NOGIL/bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json |
|------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 16.4 ms                                                                                                             | 20.0 ms: 1.22x slower                                                                                                     |
| python_startup_no_site | 9.05 ms                                                                                                             | 12.2 ms: 1.35x slower                                                                                                     |
| Geometric mean         | (ref)                                                                                                               | 1.28x slower                                                                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json | results/bm-20250201-3.14.0a4+-cf4c4ec-NOGIL/bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json |
|-----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 62.4 ms                                                                                                             | 78.9 ms: 1.26x slower                                                                                                     |
| genshi_text     | 27.2 ms                                                                                                             | 37.1 ms: 1.36x slower                                                                                                     |
| django_template | 40.1 ms                                                                                                             | 55.2 ms: 1.38x slower                                                                                                     |
| mako            | 14.5 ms                                                                                                             | 23.5 ms: 1.62x slower                                                                                                     |
| Geometric mean  | (ref)                                                                                                               | 1.40x slower                                                                                                              |

All benchmarks:
===============

| Benchmark                  | results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json | results/bm-20250201-3.14.0a4+-cf4c4ec-NOGIL/bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool              | 5.94 sec                                                                                                            | 54.9 ms: 108.37x faster                                                                                                   |
| gc_traversal               | 6.50 ms                                                                                                             | 2.70 ms: 2.41x faster                                                                                                     |
| create_gc_cycles           | 3.65 ms                                                                                                             | 2.16 ms: 1.69x faster                                                                                                     |
| xml_etree_iterparse        | 147 ms                                                                                                              | 130 ms: 1.13x faster                                                                                                      |
| sqlite_synth               | 4.08 us                                                                                                             | 3.71 us: 1.10x faster                                                                                                     |
| async_tree_cpu_io_mixed_tg | 671 ms                                                                                                              | 695 ms: 1.04x slower                                                                                                      |
| async_tree_cpu_io_mixed    | 694 ms                                                                                                              | 722 ms: 1.04x slower                                                                                                      |
| async_tree_io              | 924 ms                                                                                                              | 966 ms: 1.05x slower                                                                                                      |
| async_tree_memoization_tg  | 481 ms                                                                                                              | 503 ms: 1.05x slower                                                                                                      |
| async_tree_none_tg         | 395 ms                                                                                                              | 414 ms: 1.05x slower                                                                                                      |
| regex_dna                  | 247 ms                                                                                                              | 261 ms: 1.06x slower                                                                                                      |
| unpickle                   | 18.6 us                                                                                                             | 19.9 us: 1.07x slower                                                                                                     |
| pathlib                    | 21.1 ms                                                                                                             | 22.8 ms: 1.08x slower                                                                                                     |
| async_tree_memoization     | 505 ms                                                                                                              | 549 ms: 1.09x slower                                                                                                      |
| json                       | 6.03 ms                                                                                                             | 6.59 ms: 1.09x slower                                                                                                     |
| async_tree_none            | 402 ms                                                                                                              | 443 ms: 1.10x slower                                                                                                      |
| k_core                     | 2.88 sec                                                                                                            | 3.18 sec: 1.11x slower                                                                                                    |
| json_loads                 | 34.5 us                                                                                                             | 38.3 us: 1.11x slower                                                                                                     |
| unpickle_list              | 6.68 us                                                                                                             | 7.45 us: 1.12x slower                                                                                                     |
| asyncio_tcp                | 546 ms                                                                                                              | 611 ms: 1.12x slower                                                                                                      |
| generators                 | 37.8 ms                                                                                                             | 42.4 ms: 1.12x slower                                                                                                     |
| pycparser                  | 1.27 sec                                                                                                            | 1.43 sec: 1.13x slower                                                                                                    |
| asyncio_tcp_ssl            | 2.26 sec                                                                                                            | 2.56 sec: 1.14x slower                                                                                                    |
| mdp                        | 3.39 sec                                                                                                            | 3.86 sec: 1.14x slower                                                                                                    |
| docutils                   | 2.96 sec                                                                                                            | 3.38 sec: 1.14x slower                                                                                                    |
| html5lib                   | 66.0 ms                                                                                                             | 75.6 ms: 1.15x slower                                                                                                     |
| logging_silent             | 136 ns                                                                                                              | 156 ns: 1.15x slower                                                                                                      |
| pyflate                    | 568 ms                                                                                                              | 655 ms: 1.15x slower                                                                                                      |
| json_dumps                 | 14.7 ms                                                                                                             | 17.1 ms: 1.16x slower                                                                                                     |
| scimark_fft                | 419 ms                                                                                                              | 487 ms: 1.16x slower                                                                                                      |
| float                      | 88.2 ms                                                                                                             | 103 ms: 1.17x slower                                                                                                      |
| spectral_norm              | 123 ms                                                                                                              | 144 ms: 1.17x slower                                                                                                      |
| sphinx                     | 1.16 sec                                                                                                            | 1.37 sec: 1.17x slower                                                                                                    |
| pprint_safe_repr           | 988 ms                                                                                                              | 1.16 sec: 1.18x slower                                                                                                    |
| unpickle_pure_python       | 262 us                                                                                                              | 308 us: 1.18x slower                                                                                                      |
| sqlglot_normalize          | 131 ms                                                                                                              | 156 ms: 1.19x slower                                                                                                      |
| connected_components       | 552 ms                                                                                                              | 658 ms: 1.19x slower                                                                                                      |
| dulwich_log                | 60.6 ms                                                                                                             | 72.5 ms: 1.20x slower                                                                                                     |
| pprint_pformat             | 1.99 sec                                                                                                            | 2.38 sec: 1.20x slower                                                                                                    |
| pylint                     | 322 ms                                                                                                              | 385 ms: 1.20x slower                                                                                                      |
| scimark_sor                | 152 ms                                                                                                              | 182 ms: 1.20x slower                                                                                                      |
| telco                      | 9.52 ms                                                                                                             | 11.4 ms: 1.20x slower                                                                                                     |
| async_generators           | 450 ms                                                                                                              | 542 ms: 1.20x slower                                                                                                      |
| shortest_path              | 570 ms                                                                                                              | 691 ms: 1.21x slower                                                                                                      |
| pickle_pure_python         | 398 us                                                                                                              | 484 us: 1.22x slower                                                                                                      |
| logging_simple             | 7.38 us                                                                                                             | 8.99 us: 1.22x slower                                                                                                     |
| python_startup             | 16.4 ms                                                                                                             | 20.0 ms: 1.22x slower                                                                                                     |
| deepcopy_reduce            | 3.82 us                                                                                                             | 4.67 us: 1.22x slower                                                                                                     |
| deepcopy                   | 344 us                                                                                                              | 421 us: 1.22x slower                                                                                                      |
| xml_etree_generate         | 116 ms                                                                                                              | 143 ms: 1.23x slower                                                                                                      |
| logging_format             | 8.07 us                                                                                                             | 9.96 us: 1.24x slower                                                                                                     |
| tomli_loads                | 2.58 sec                                                                                                            | 3.20 sec: 1.24x slower                                                                                                    |
| regex_compile              | 127 ms                                                                                                              | 158 ms: 1.25x slower                                                                                                      |
| go                         | 144 ms                                                                                                              | 180 ms: 1.25x slower                                                                                                      |
| scimark_sparse_mat_mult    | 6.27 ms                                                                                                             | 7.85 ms: 1.25x slower                                                                                                     |
| comprehensions             | 21.3 us                                                                                                             | 26.7 us: 1.26x slower                                                                                                     |
| 2to3                       | 301 ms                                                                                                              | 379 ms: 1.26x slower                                                                                                      |
| sqlglot_optimize           | 61.7 ms                                                                                                             | 77.7 ms: 1.26x slower                                                                                                     |
| deepcopy_memo              | 41.7 us                                                                                                             | 52.5 us: 1.26x slower                                                                                                     |
| genshi_xml                 | 62.4 ms                                                                                                             | 78.9 ms: 1.26x slower                                                                                                     |
| thrift                     | 982 us                                                                                                              | 1.24 ms: 1.27x slower                                                                                                     |
| subparsers                 | 25.4 ms                                                                                                             | 32.2 ms: 1.27x slower                                                                                                     |
| hexiom                     | 7.38 ms                                                                                                             | 9.41 ms: 1.28x slower                                                                                                     |
| scimark_monte_carlo        | 87.3 ms                                                                                                             | 112 ms: 1.28x slower                                                                                                      |
| xml_etree_process          | 80.5 ms                                                                                                             | 103 ms: 1.28x slower                                                                                                      |
| sympy_expand               | 476 ms                                                                                                              | 614 ms: 1.29x slower                                                                                                      |
| crypto_pyaes               | 88.8 ms                                                                                                             | 115 ms: 1.29x slower                                                                                                      |
| unpack_sequence            | 58.1 ns                                                                                                             | 75.4 ns: 1.30x slower                                                                                                     |
| chaos                      | 68.4 ms                                                                                                             | 88.7 ms: 1.30x slower                                                                                                     |
| sqlglot_transpile          | 1.83 ms                                                                                                             | 2.38 ms: 1.30x slower                                                                                                     |
| sympy_sum                  | 150 ms                                                                                                              | 197 ms: 1.31x slower                                                                                                      |
| raytrace                   | 315 ms                                                                                                              | 415 ms: 1.31x slower                                                                                                      |
| bpe_tokeniser              | 5.52 sec                                                                                                            | 7.28 sec: 1.32x slower                                                                                                    |
| meteor_contest             | 115 ms                                                                                                              | 152 ms: 1.32x slower                                                                                                      |
| many_optionals             | 706 us                                                                                                              | 944 us: 1.34x slower                                                                                                      |
| python_startup_no_site     | 9.05 ms                                                                                                             | 12.2 ms: 1.35x slower                                                                                                     |
| sqlalchemy_declarative     | 148 ms                                                                                                              | 201 ms: 1.35x slower                                                                                                      |
| sympy_integrate            | 21.5 ms                                                                                                             | 29.2 ms: 1.36x slower                                                                                                     |
| genshi_text                | 27.2 ms                                                                                                             | 37.1 ms: 1.36x slower                                                                                                     |
| sympy_str                  | 268 ms                                                                                                              | 368 ms: 1.37x slower                                                                                                      |
| django_template            | 40.1 ms                                                                                                             | 55.2 ms: 1.38x slower                                                                                                     |
| sqlglot_parse              | 1.45 ms                                                                                                             | 2.00 ms: 1.38x slower                                                                                                     |
| nqueens                    | 101 ms                                                                                                              | 139 ms: 1.38x slower                                                                                                      |
| coverage                   | 100 ms                                                                                                              | 140 ms: 1.40x slower                                                                                                      |
| scimark_lu                 | 139 ms                                                                                                              | 195 ms: 1.40x slower                                                                                                      |
| fannkuch                   | 477 ms                                                                                                              | 672 ms: 1.41x slower                                                                                                      |
| richards                   | 52.9 ms                                                                                                             | 75.1 ms: 1.42x slower                                                                                                     |
| bench_thread_pool          | 1.29 ms                                                                                                             | 1.88 ms: 1.46x slower                                                                                                     |
| typing_runtime_protocols   | 193 us                                                                                                              | 282 us: 1.47x slower                                                                                                      |
| sqlalchemy_imperative      | 15.3 ms                                                                                                             | 22.4 ms: 1.47x slower                                                                                                     |
| richards_super             | 59.4 ms                                                                                                             | 88.4 ms: 1.49x slower                                                                                                     |
| nbody                      | 123 ms                                                                                                              | 188 ms: 1.53x slower                                                                                                      |
| deltablue                  | 3.86 ms                                                                                                             | 6.17 ms: 1.60x slower                                                                                                     |
| mako                       | 14.5 ms                                                                                                             | 23.5 ms: 1.62x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                               | 1.13x slower                                                                                                              |

Benchmark hidden because not significant (10): regex_v8, pickle, pickle_list, pidigits, regex_effbot, async_tree_io_tg, xml_etree_parse, asyncio_websockets, coroutines, pickle_dict

- Geometric mean (including insignificant results): 1.158x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.18x
- 95% likely to have a slowdown of 1.17x
- 99% likely to have a slowdown of 1.15x

# Memory
- memory change: 1.20x