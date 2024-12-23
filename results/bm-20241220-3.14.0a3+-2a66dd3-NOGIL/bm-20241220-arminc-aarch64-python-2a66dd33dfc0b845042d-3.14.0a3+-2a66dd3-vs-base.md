# Results vs. base

- fork: python
- ref: 2a66dd33dfc0b845042d
- machine: linux-aarch64
- commit hash: 2a66dd3
- commit date: 2024-12-20
- overall geometric mean: 1.282x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x slower
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20241220-3.14.0a3+-2a66dd3/bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json | results/bm-20241220-3.14.0a3+-2a66dd3-NOGIL/bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                                                              | 477 ms: 1.55x slower                                                                                                      |
| docutils       | 3.01 sec                                                                                                            | 3.78 sec: 1.25x slower                                                                                                    |
| html5lib       | 64.7 ms                                                                                                             | 109 ms: 1.69x slower                                                                                                      |
| sphinx         | 1.19 sec                                                                                                            | 1.47 sec: 1.24x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.42x slower                                                                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20241220-3.14.0a3+-2a66dd3/bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json | results/bm-20241220-3.14.0a3+-2a66dd3-NOGIL/bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| coroutines                 | 28.9 ms                                                                                                             | 34.6 ms: 1.20x slower                                                                                                     |
| async_tree_cpu_io_mixed_tg | 680 ms                                                                                                              | 824 ms: 1.21x slower                                                                                                      |
| async_generators           | 496 ms                                                                                                              | 606 ms: 1.22x slower                                                                                                      |
| async_tree_cpu_io_mixed    | 686 ms                                                                                                              | 852 ms: 1.24x slower                                                                                                      |
| async_tree_memoization     | 520 ms                                                                                                              | 678 ms: 1.30x slower                                                                                                      |
| async_tree_io              | 928 ms                                                                                                              | 1.21 sec: 1.31x slower                                                                                                    |
| async_tree_io_tg           | 906 ms                                                                                                              | 1.19 sec: 1.31x slower                                                                                                    |
| async_tree_memoization_tg  | 484 ms                                                                                                              | 638 ms: 1.32x slower                                                                                                      |
| async_tree_none_tg         | 390 ms                                                                                                              | 523 ms: 1.34x slower                                                                                                      |
| async_tree_none            | 403 ms                                                                                                              | 542 ms: 1.34x slower                                                                                                      |
| Geometric mean             | (ref)                                                                                                               | 1.25x slower                                                                                                              |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20241220-3.14.0a3+-2a66dd3/bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json | results/bm-20241220-3.14.0a3+-2a66dd3-NOGIL/bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 129 ms                                                                                                              | 188 ms: 1.46x slower                                                                                                      |
| float          | 96.1 ms                                                                                                             | 159 ms: 1.66x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.36x slower                                                                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20241220-3.14.0a3+-2a66dd3/bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json | results/bm-20241220-3.14.0a3+-2a66dd3-NOGIL/bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 127 ms                                                                                                              | 191 ms: 1.51x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.12x slower                                                                                                              |

Benchmark hidden because not significant (3): regex_effbot, regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20241220-3.14.0a3+-2a66dd3/bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json | results/bm-20241220-3.14.0a3+-2a66dd3-NOGIL/bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json |
|----------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 144 ms                                                                                                              | 135 ms: 1.07x faster                                                                                                      |
| json_loads           | 32.7 us                                                                                                             | 37.4 us: 1.14x slower                                                                                                     |
| xml_etree_generate   | 125 ms                                                                                                              | 143 ms: 1.15x slower                                                                                                      |
| json_dumps           | 14.5 ms                                                                                                             | 18.2 ms: 1.25x slower                                                                                                     |
| xml_etree_process    | 83.2 ms                                                                                                             | 111 ms: 1.34x slower                                                                                                      |
| tomli_loads          | 2.62 sec                                                                                                            | 3.57 sec: 1.36x slower                                                                                                    |
| unpickle_pure_python | 265 us                                                                                                              | 472 us: 1.78x slower                                                                                                      |
| pickle_pure_python   | 385 us                                                                                                              | 692 us: 1.80x slower                                                                                                      |
| Geometric mean       | (ref)                                                                                                               | 1.27x slower                                                                                                              |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20241220-3.14.0a3+-2a66dd3/bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json | results/bm-20241220-3.14.0a3+-2a66dd3-NOGIL/bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json |
|------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 16.2 ms                                                                                                             | 21.4 ms: 1.32x slower                                                                                                     |
| python_startup_no_site | 8.97 ms                                                                                                             | 12.5 ms: 1.40x slower                                                                                                     |
| Geometric mean         | (ref)                                                                                                               | 1.36x slower                                                                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20241220-3.14.0a3+-2a66dd3/bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json | results/bm-20241220-3.14.0a3+-2a66dd3-NOGIL/bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json |
|-----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 66.6 ms                                                                                                             | 83.9 ms: 1.26x slower                                                                                                     |
| genshi_text     | 28.6 ms                                                                                                             | 42.2 ms: 1.48x slower                                                                                                     |
| django_template | 41.5 ms                                                                                                             | 67.4 ms: 1.62x slower                                                                                                     |
| mako            | 14.3 ms                                                                                                             | 25.6 ms: 1.79x slower                                                                                                     |
| Geometric mean  | (ref)                                                                                                               | 1.53x slower                                                                                                              |

All benchmarks:
===============

| Benchmark                  | results/bm-20241220-3.14.0a3+-2a66dd3/bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json | results/bm-20241220-3.14.0a3+-2a66dd3-NOGIL/bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool              | 5.45 sec                                                                                                            | 64.1 ms: 85.04x faster                                                                                                    |
| gc_traversal               | 6.92 ms                                                                                                             | 5.03 ms: 1.37x faster                                                                                                     |
| create_gc_cycles           | 3.56 ms                                                                                                             | 2.90 ms: 1.23x faster                                                                                                     |
| xml_etree_iterparse        | 144 ms                                                                                                              | 135 ms: 1.07x faster                                                                                                      |
| sqlite_synth               | 4.07 us                                                                                                             | 3.85 us: 1.06x faster                                                                                                     |
| pathlib                    | 21.7 ms                                                                                                             | 24.2 ms: 1.12x slower                                                                                                     |
| json_loads                 | 32.7 us                                                                                                             | 37.4 us: 1.14x slower                                                                                                     |
| xml_etree_generate         | 125 ms                                                                                                              | 143 ms: 1.15x slower                                                                                                      |
| k_core                     | 2.86 sec                                                                                                            | 3.31 sec: 1.16x slower                                                                                                    |
| json                       | 5.81 ms                                                                                                             | 6.85 ms: 1.18x slower                                                                                                     |
| mdp                        | 3.43 sec                                                                                                            | 4.05 sec: 1.18x slower                                                                                                    |
| spectral_norm              | 132 ms                                                                                                              | 157 ms: 1.18x slower                                                                                                      |
| coroutines                 | 28.9 ms                                                                                                             | 34.6 ms: 1.20x slower                                                                                                     |
| async_tree_cpu_io_mixed_tg | 680 ms                                                                                                              | 824 ms: 1.21x slower                                                                                                      |
| async_generators           | 496 ms                                                                                                              | 606 ms: 1.22x slower                                                                                                      |
| scimark_fft                | 423 ms                                                                                                              | 517 ms: 1.22x slower                                                                                                      |
| sphinx                     | 1.19 sec                                                                                                            | 1.47 sec: 1.24x slower                                                                                                    |
| async_tree_cpu_io_mixed    | 686 ms                                                                                                              | 852 ms: 1.24x slower                                                                                                      |
| json_dumps                 | 14.5 ms                                                                                                             | 18.2 ms: 1.25x slower                                                                                                     |
| docutils                   | 3.01 sec                                                                                                            | 3.78 sec: 1.25x slower                                                                                                    |
| deepcopy                   | 346 us                                                                                                              | 435 us: 1.26x slower                                                                                                      |
| genshi_xml                 | 66.6 ms                                                                                                             | 83.9 ms: 1.26x slower                                                                                                     |
| shortest_path              | 573 ms                                                                                                              | 724 ms: 1.26x slower                                                                                                      |
| telco                      | 9.52 ms                                                                                                             | 12.1 ms: 1.27x slower                                                                                                     |
| connected_components       | 544 ms                                                                                                              | 693 ms: 1.27x slower                                                                                                      |
| nqueens                    | 105 ms                                                                                                              | 135 ms: 1.29x slower                                                                                                      |
| async_tree_memoization     | 520 ms                                                                                                              | 678 ms: 1.30x slower                                                                                                      |
| async_tree_io              | 928 ms                                                                                                              | 1.21 sec: 1.31x slower                                                                                                    |
| async_tree_io_tg           | 906 ms                                                                                                              | 1.19 sec: 1.31x slower                                                                                                    |
| python_startup             | 16.2 ms                                                                                                             | 21.4 ms: 1.32x slower                                                                                                     |
| async_tree_memoization_tg  | 484 ms                                                                                                              | 638 ms: 1.32x slower                                                                                                      |
| sqlglot_optimize           | 66.4 ms                                                                                                             | 87.9 ms: 1.32x slower                                                                                                     |
| deepcopy_reduce            | 3.61 us                                                                                                             | 4.81 us: 1.33x slower                                                                                                     |
| xml_etree_process          | 83.2 ms                                                                                                             | 111 ms: 1.34x slower                                                                                                      |
| async_tree_none_tg         | 390 ms                                                                                                              | 523 ms: 1.34x slower                                                                                                      |
| async_tree_none            | 403 ms                                                                                                              | 542 ms: 1.34x slower                                                                                                      |
| scimark_sparse_mat_mult    | 6.20 ms                                                                                                             | 8.38 ms: 1.35x slower                                                                                                     |
| pycparser                  | 1.28 sec                                                                                                            | 1.74 sec: 1.36x slower                                                                                                    |
| tomli_loads                | 2.62 sec                                                                                                            | 3.57 sec: 1.36x slower                                                                                                    |
| dulwich_log                | 62.3 ms                                                                                                             | 84.9 ms: 1.36x slower                                                                                                     |
| meteor_contest             | 116 ms                                                                                                              | 159 ms: 1.37x slower                                                                                                      |
| pylint                     | 326 ms                                                                                                              | 446 ms: 1.37x slower                                                                                                      |
| typing_runtime_protocols   | 206 us                                                                                                              | 284 us: 1.38x slower                                                                                                      |
| sqlglot_normalize          | 129 ms                                                                                                              | 179 ms: 1.38x slower                                                                                                      |
| bpe_tokeniser              | 5.74 sec                                                                                                            | 7.99 sec: 1.39x slower                                                                                                    |
| python_startup_no_site     | 8.97 ms                                                                                                             | 12.5 ms: 1.40x slower                                                                                                     |
| deepcopy_memo              | 41.3 us                                                                                                             | 57.8 us: 1.40x slower                                                                                                     |
| thrift                     | 962 us                                                                                                              | 1.35 ms: 1.40x slower                                                                                                     |
| coverage                   | 102 ms                                                                                                              | 144 ms: 1.41x slower                                                                                                      |
| subparsers                 | 26.5 ms                                                                                                             | 37.6 ms: 1.42x slower                                                                                                     |
| fannkuch                   | 492 ms                                                                                                              | 698 ms: 1.42x slower                                                                                                      |
| pprint_pformat             | 2.02 sec                                                                                                            | 2.87 sec: 1.42x slower                                                                                                    |
| pprint_safe_repr           | 974 ms                                                                                                              | 1.39 sec: 1.43x slower                                                                                                    |
| many_optionals             | 707 us                                                                                                              | 1.02 ms: 1.44x slower                                                                                                     |
| bench_thread_pool          | 1.35 ms                                                                                                             | 1.97 ms: 1.46x slower                                                                                                     |
| crypto_pyaes               | 83.6 ms                                                                                                             | 122 ms: 1.46x slower                                                                                                      |
| nbody                      | 129 ms                                                                                                              | 188 ms: 1.46x slower                                                                                                      |
| sympy_integrate            | 22.4 ms                                                                                                             | 32.7 ms: 1.46x slower                                                                                                     |
| mypy2                      | 1.04 sec                                                                                                            | 1.53 sec: 1.46x slower                                                                                                    |
| genshi_text                | 28.6 ms                                                                                                             | 42.2 ms: 1.48x slower                                                                                                     |
| pyflate                    | 596 ms                                                                                                              | 894 ms: 1.50x slower                                                                                                      |
| regex_compile              | 127 ms                                                                                                              | 191 ms: 1.51x slower                                                                                                      |
| scimark_lu                 | 143 ms                                                                                                              | 218 ms: 1.52x slower                                                                                                      |
| 2to3                       | 308 ms                                                                                                              | 477 ms: 1.55x slower                                                                                                      |
| generators                 | 37.1 ms                                                                                                             | 58.1 ms: 1.56x slower                                                                                                     |
| logging_format             | 7.97 us                                                                                                             | 12.5 us: 1.57x slower                                                                                                     |
| logging_simple             | 7.17 us                                                                                                             | 11.5 us: 1.60x slower                                                                                                     |
| django_template            | 41.5 ms                                                                                                             | 67.4 ms: 1.62x slower                                                                                                     |
| float                      | 96.1 ms                                                                                                             | 159 ms: 1.66x slower                                                                                                      |
| sqlalchemy_declarative     | 149 ms                                                                                                              | 248 ms: 1.66x slower                                                                                                      |
| sqlalchemy_imperative      | 15.9 ms                                                                                                             | 26.5 ms: 1.66x slower                                                                                                     |
| html5lib                   | 64.7 ms                                                                                                             | 109 ms: 1.69x slower                                                                                                      |
| richards                   | 56.7 ms                                                                                                             | 96.0 ms: 1.69x slower                                                                                                     |
| sympy_str                  | 275 ms                                                                                                              | 468 ms: 1.70x slower                                                                                                      |
| hexiom                     | 7.51 ms                                                                                                             | 13.0 ms: 1.73x slower                                                                                                     |
| comprehensions             | 22.4 us                                                                                                             | 38.8 us: 1.73x slower                                                                                                     |
| unpickle_pure_python       | 265 us                                                                                                              | 472 us: 1.78x slower                                                                                                      |
| chaos                      | 72.7 ms                                                                                                             | 129 ms: 1.78x slower                                                                                                      |
| mako                       | 14.3 ms                                                                                                             | 25.6 ms: 1.79x slower                                                                                                     |
| scimark_monte_carlo        | 85.7 ms                                                                                                             | 154 ms: 1.80x slower                                                                                                      |
| pickle_pure_python         | 385 us                                                                                                              | 692 us: 1.80x slower                                                                                                      |
| richards_super             | 60.3 ms                                                                                                             | 109 ms: 1.80x slower                                                                                                      |
| sympy_expand               | 481 ms                                                                                                              | 870 ms: 1.81x slower                                                                                                      |
| scimark_sor                | 157 ms                                                                                                              | 283 ms: 1.81x slower                                                                                                      |
| logging_silent             | 142 ns                                                                                                              | 258 ns: 1.81x slower                                                                                                      |
| sqlglot_transpile          | 1.87 ms                                                                                                             | 3.52 ms: 1.89x slower                                                                                                     |
| sympy_sum                  | 146 ms                                                                                                              | 290 ms: 1.99x slower                                                                                                      |
| raytrace                   | 327 ms                                                                                                              | 663 ms: 2.03x slower                                                                                                      |
| sqlglot_parse              | 1.47 ms                                                                                                             | 3.12 ms: 2.12x slower                                                                                                     |
| go                         | 144 ms                                                                                                              | 336 ms: 2.33x slower                                                                                                      |
| deltablue                  | 4.02 ms                                                                                                             | 11.0 ms: 2.73x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                               | 1.33x slower                                                                                                              |

Benchmark hidden because not significant (6): xml_etree_parse, regex_effbot, regex_dna, asyncio_websockets, pidigits, regex_v8
Ignored benchmarks (1) of results/bm-20241220-3.14.0a3+-2a66dd3/bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json: djangocms

- Geometric mean (including insignificant results): 1.282x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.32x
- 95% likely to have a slowdown of 1.32x
- 99% likely to have a slowdown of 1.30x

# Memory
- memory change: 1.19x