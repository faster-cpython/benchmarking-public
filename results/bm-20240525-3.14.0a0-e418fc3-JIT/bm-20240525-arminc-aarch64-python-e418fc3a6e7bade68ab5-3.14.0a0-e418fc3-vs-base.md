# Results vs. base

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: linux-aarch64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 306 ms                                                                                                            | 360 ms: 1.18x slower                                                                                                  |
| docutils       | 3.09 sec                                                                                                          | 3.58 sec: 1.16x slower                                                                                                |
| html5lib       | 65.8 ms                                                                                                           | 71.3 ms: 1.08x slower                                                                                                 |
| tornado_http   | 130 ms                                                                                                            | 140 ms: 1.07x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.10x slower                                                                                                          |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.26 sec                                                                                                          | 1.23 sec: 1.03x faster                                                                                                |
| async_tree_none            | 490 ms                                                                                                            | 508 ms: 1.04x slower                                                                                                  |
| async_tree_cpu_io_mixed_tg | 756 ms                                                                                                            | 788 ms: 1.04x slower                                                                                                  |
| async_tree_cpu_io_mixed    | 784 ms                                                                                                            | 822 ms: 1.05x slower                                                                                                  |
| async_tree_memoization_tg  | 600 ms                                                                                                            | 630 ms: 1.05x slower                                                                                                  |
| async_tree_none_tg         | 467 ms                                                                                                            | 491 ms: 1.05x slower                                                                                                  |
| async_tree_io              | 1.20 sec                                                                                                          | 1.27 sec: 1.06x slower                                                                                                |
| async_tree_memoization     | 647 ms                                                                                                            | 685 ms: 1.06x slower                                                                                                  |
| Geometric mean             | (ref)                                                                                                             | 1.04x slower                                                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| float          | 91.9 ms                                                                                                           | 89.3 ms: 1.03x faster                                                                                                 |
| nbody          | 113 ms                                                                                                            | 115 ms: 1.01x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.01x faster                                                                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 30.9 ms                                                                                                           | 30.2 ms: 1.02x faster                                                                                                 |
| regex_compile  | 129 ms                                                                                                            | 174 ms: 1.35x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.07x slower                                                                                                          |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| unpickle_list        | 6.59 us                                                                                                           | 6.43 us: 1.03x faster                                                                                                 |
| pickle_dict          | 37.3 us                                                                                                           | 37.7 us: 1.01x slower                                                                                                 |
| xml_etree_generate   | 113 ms                                                                                                            | 115 ms: 1.02x slower                                                                                                  |
| xml_etree_parse      | 190 ms                                                                                                            | 196 ms: 1.03x slower                                                                                                  |
| tomli_loads          | 2.53 sec                                                                                                          | 2.66 sec: 1.05x slower                                                                                                |
| unpickle_pure_python | 252 us                                                                                                            | 275 us: 1.09x slower                                                                                                  |
| pickle_pure_python   | 361 us                                                                                                            | 405 us: 1.12x slower                                                                                                  |
| Geometric mean       | (ref)                                                                                                             | 1.02x slower                                                                                                          |

Benchmark hidden because not significant (7): xml_etree_iterparse, json_loads, json_dumps, xml_etree_process, unpickle, pickle, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 12.6 ms                                                                                                           | 15.2 ms: 1.20x slower                                                                                                 |
| python_startup_no_site | 8.41 ms                                                                                                           | 10.7 ms: 1.28x slower                                                                                                 |
| Geometric mean         | (ref)                                                                                                             | 1.24x slower                                                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako            | 13.2 ms                                                                                                           | 12.9 ms: 1.02x faster                                                                                                 |
| django_template | 41.6 ms                                                                                                           | 50.4 ms: 1.21x slower                                                                                                 |
| genshi_text     | 27.9 ms                                                                                                           | 34.8 ms: 1.25x slower                                                                                                 |
| genshi_xml      | 60.8 ms                                                                                                           | 81.7 ms: 1.34x slower                                                                                                 |
| Geometric mean  | (ref)                                                                                                             | 1.19x slower                                                                                                          |

All benchmarks:
===============

| Benchmark                  | results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json | results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| float                      | 91.9 ms                                                                                                           | 89.3 ms: 1.03x faster                                                                                                 |
| async_tree_io_tg           | 1.26 sec                                                                                                          | 1.23 sec: 1.03x faster                                                                                                |
| unpickle_list              | 6.59 us                                                                                                           | 6.43 us: 1.03x faster                                                                                                 |
| mako                       | 13.2 ms                                                                                                           | 12.9 ms: 1.02x faster                                                                                                 |
| regex_v8                   | 30.9 ms                                                                                                           | 30.2 ms: 1.02x faster                                                                                                 |
| deepcopy_memo              | 50.1 us                                                                                                           | 49.7 us: 1.01x faster                                                                                                 |
| asyncio_tcp_ssl            | 2.21 sec                                                                                                          | 2.23 sec: 1.01x slower                                                                                                |
| pickle_dict                | 37.3 us                                                                                                           | 37.7 us: 1.01x slower                                                                                                 |
| nbody                      | 113 ms                                                                                                            | 115 ms: 1.01x slower                                                                                                  |
| sqlite_synth               | 3.84 us                                                                                                           | 3.89 us: 1.02x slower                                                                                                 |
| coverage                   | 97.9 ms                                                                                                           | 99.5 ms: 1.02x slower                                                                                                 |
| richards                   | 53.7 ms                                                                                                           | 54.7 ms: 1.02x slower                                                                                                 |
| xml_etree_generate         | 113 ms                                                                                                            | 115 ms: 1.02x slower                                                                                                  |
| pathlib                    | 21.4 ms                                                                                                           | 21.9 ms: 1.02x slower                                                                                                 |
| logging_silent             | 134 ns                                                                                                            | 138 ns: 1.02x slower                                                                                                  |
| xml_etree_parse            | 190 ms                                                                                                            | 196 ms: 1.03x slower                                                                                                  |
| fannkuch                   | 460 ms                                                                                                            | 475 ms: 1.03x slower                                                                                                  |
| richards_super             | 60.4 ms                                                                                                           | 62.4 ms: 1.03x slower                                                                                                 |
| mdp                        | 3.32 sec                                                                                                          | 3.43 sec: 1.04x slower                                                                                                |
| scimark_fft                | 446 ms                                                                                                            | 462 ms: 1.04x slower                                                                                                  |
| async_tree_none            | 490 ms                                                                                                            | 508 ms: 1.04x slower                                                                                                  |
| spectral_norm              | 141 ms                                                                                                            | 146 ms: 1.04x slower                                                                                                  |
| telco                      | 9.85 ms                                                                                                           | 10.2 ms: 1.04x slower                                                                                                 |
| logging_simple             | 7.11 us                                                                                                           | 7.38 us: 1.04x slower                                                                                                 |
| async_tree_cpu_io_mixed_tg | 756 ms                                                                                                            | 788 ms: 1.04x slower                                                                                                  |
| async_generators           | 483 ms                                                                                                            | 505 ms: 1.04x slower                                                                                                  |
| scimark_sparse_mat_mult    | 6.65 ms                                                                                                           | 6.95 ms: 1.04x slower                                                                                                 |
| logging_format             | 7.78 us                                                                                                           | 8.13 us: 1.05x slower                                                                                                 |
| flaskblogging              | 4.74 ms                                                                                                           | 4.96 ms: 1.05x slower                                                                                                 |
| async_tree_cpu_io_mixed    | 784 ms                                                                                                            | 822 ms: 1.05x slower                                                                                                  |
| meteor_contest             | 112 ms                                                                                                            | 118 ms: 1.05x slower                                                                                                  |
| tomli_loads                | 2.53 sec                                                                                                          | 2.66 sec: 1.05x slower                                                                                                |
| async_tree_memoization_tg  | 600 ms                                                                                                            | 630 ms: 1.05x slower                                                                                                  |
| async_tree_none_tg         | 467 ms                                                                                                            | 491 ms: 1.05x slower                                                                                                  |
| async_tree_io              | 1.20 sec                                                                                                          | 1.27 sec: 1.06x slower                                                                                                |
| async_tree_memoization     | 647 ms                                                                                                            | 685 ms: 1.06x slower                                                                                                  |
| generators                 | 37.6 ms                                                                                                           | 39.9 ms: 1.06x slower                                                                                                 |
| dask                       | 368 ms                                                                                                            | 391 ms: 1.06x slower                                                                                                  |
| bench_thread_pool          | 1.27 ms                                                                                                           | 1.34 ms: 1.06x slower                                                                                                 |
| typing_runtime_protocols   | 200 us                                                                                                            | 212 us: 1.06x slower                                                                                                  |
| asyncio_tcp                | 573 ms                                                                                                            | 611 ms: 1.07x slower                                                                                                  |
| tornado_http               | 130 ms                                                                                                            | 140 ms: 1.07x slower                                                                                                  |
| html5lib                   | 65.8 ms                                                                                                           | 71.3 ms: 1.08x slower                                                                                                 |
| scimark_sor                | 159 ms                                                                                                            | 173 ms: 1.09x slower                                                                                                  |
| crypto_pyaes               | 82.0 ms                                                                                                           | 89.5 ms: 1.09x slower                                                                                                 |
| scimark_monte_carlo        | 81.1 ms                                                                                                           | 88.6 ms: 1.09x slower                                                                                                 |
| unpickle_pure_python       | 252 us                                                                                                            | 275 us: 1.09x slower                                                                                                  |
| raytrace                   | 297 ms                                                                                                            | 325 ms: 1.10x slower                                                                                                  |
| pycparser                  | 1.23 sec                                                                                                          | 1.36 sec: 1.11x slower                                                                                                |
| pyflate                    | 557 ms                                                                                                            | 616 ms: 1.11x slower                                                                                                  |
| sqlglot_parse              | 1.40 ms                                                                                                           | 1.57 ms: 1.12x slower                                                                                                 |
| sqlglot_optimize           | 62.1 ms                                                                                                           | 69.5 ms: 1.12x slower                                                                                                 |
| deepcopy                   | 445 us                                                                                                            | 499 us: 1.12x slower                                                                                                  |
| go                         | 160 ms                                                                                                            | 179 ms: 1.12x slower                                                                                                  |
| sqlglot_normalize          | 128 ms                                                                                                            | 143 ms: 1.12x slower                                                                                                  |
| pickle_pure_python         | 361 us                                                                                                            | 405 us: 1.12x slower                                                                                                  |
| comprehensions             | 20.4 us                                                                                                           | 22.9 us: 1.13x slower                                                                                                 |
| sqlglot_transpile          | 1.73 ms                                                                                                           | 1.98 ms: 1.15x slower                                                                                                 |
| docutils                   | 3.09 sec                                                                                                          | 3.58 sec: 1.16x slower                                                                                                |
| 2to3                       | 306 ms                                                                                                            | 360 ms: 1.18x slower                                                                                                  |
| deepcopy_reduce            | 4.02 us                                                                                                           | 4.74 us: 1.18x slower                                                                                                 |
| sympy_expand               | 461 ms                                                                                                            | 548 ms: 1.19x slower                                                                                                  |
| dulwich_log                | 59.4 ms                                                                                                           | 70.8 ms: 1.19x slower                                                                                                 |
| bench_mp_pool              | 7.02 ms                                                                                                           | 8.41 ms: 1.20x slower                                                                                                 |
| pprint_safe_repr           | 930 ms                                                                                                            | 1.11 sec: 1.20x slower                                                                                                |
| deltablue                  | 3.90 ms                                                                                                           | 4.69 ms: 1.20x slower                                                                                                 |
| python_startup             | 12.6 ms                                                                                                           | 15.2 ms: 1.20x slower                                                                                                 |
| pprint_pformat             | 1.91 sec                                                                                                          | 2.30 sec: 1.21x slower                                                                                                |
| sympy_str                  | 268 ms                                                                                                            | 323 ms: 1.21x slower                                                                                                  |
| django_template            | 41.6 ms                                                                                                           | 50.4 ms: 1.21x slower                                                                                                 |
| nqueens                    | 98.0 ms                                                                                                           | 120 ms: 1.22x slower                                                                                                  |
| pylint                     | 342 ms                                                                                                            | 423 ms: 1.24x slower                                                                                                  |
| sympy_integrate            | 21.3 ms                                                                                                           | 26.4 ms: 1.24x slower                                                                                                 |
| genshi_text                | 27.9 ms                                                                                                           | 34.8 ms: 1.25x slower                                                                                                 |
| hexiom                     | 7.07 ms                                                                                                           | 8.96 ms: 1.27x slower                                                                                                 |
| python_startup_no_site     | 8.41 ms                                                                                                           | 10.7 ms: 1.28x slower                                                                                                 |
| sympy_sum                  | 144 ms                                                                                                            | 187 ms: 1.29x slower                                                                                                  |
| chaos                      | 67.9 ms                                                                                                           | 88.2 ms: 1.30x slower                                                                                                 |
| scimark_lu                 | 137 ms                                                                                                            | 181 ms: 1.32x slower                                                                                                  |
| genshi_xml                 | 60.8 ms                                                                                                           | 81.7 ms: 1.34x slower                                                                                                 |
| regex_compile              | 129 ms                                                                                                            | 174 ms: 1.35x slower                                                                                                  |
| Geometric mean             | (ref)                                                                                                             | 1.08x slower                                                                                                          |

Benchmark hidden because not significant (17): xml_etree_iterparse, create_gc_cycles, json, asyncio_websockets, json_loads, thrift, json_dumps, xml_etree_process, coroutines, pidigits, regex_effbot, unpickle, pickle, chameleon, regex_dna, pickle_list, gc_traversal

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.10x