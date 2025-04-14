# Results vs. 3.13.0

- fork: mdboom
- ref: aa_test_2025
- machine: linux-aarch64
- commit hash: 4844db8
- commit date: 2025-01-21
- overall geometric mean: 1.140x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x slower
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 385 ms: 1.23x slower                                             |
| docutils       | 2.96 sec                                                 | 3.40 sec: 1.15x slower                                           |
| html5lib       | 65.6 ms                                                  | 80.0 ms: 1.22x slower                                            |
| sphinx         | 1.20 sec                                                 | 1.45 sec: 1.21x slower                                           |
| Geometric mean | (ref)                                                    | 1.20x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 505 ms: 1.31x faster                                             |
| async_tree_io_tg           | 1.16 sec                                                 | 923 ms: 1.26x faster                                             |
| async_tree_memoization     | 664 ms                                                   | 530 ms: 1.25x faster                                             |
| async_tree_none_tg         | 484 ms                                                   | 403 ms: 1.20x faster                                             |
| async_tree_io              | 1.14 sec                                                 | 959 ms: 1.19x faster                                             |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 688 ms: 1.16x faster                                             |
| async_tree_none            | 504 ms                                                   | 437 ms: 1.15x faster                                             |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 733 ms: 1.08x faster                                             |
| async_generators           | 500 ms                                                   | 566 ms: 1.13x slower                                             |
| coroutines                 | 29.4 ms                                                  | 33.5 ms: 1.14x slower                                            |
| Geometric mean             | (ref)                                                    | 1.11x faster                                                     |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 105 ms: 1.09x slower                                             |
| nbody          | 118 ms                                                   | 184 ms: 1.55x slower                                             |
| Geometric mean | (ref)                                                    | 1.19x slower                                                     |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.17 ms: 1.22x faster                                            |
| regex_compile  | 134 ms                                                   | 162 ms: 1.21x slower                                             |
| Geometric mean | (ref)                                                    | 1.01x slower                                                     |

Benchmark hidden because not significant (2): regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| xml_etree_iterparse  | 159 ms                                                   | 130 ms: 1.23x faster                                             |
| xml_etree_parse      | 203 ms                                                   | 179 ms: 1.13x faster                                             |
| json_loads           | 32.8 us                                                  | 37.6 us: 1.15x slower                                            |
| json_dumps           | 14.2 ms                                                  | 16.9 ms: 1.19x slower                                            |
| xml_etree_generate   | 118 ms                                                   | 141 ms: 1.19x slower                                             |
| tomli_loads          | 2.67 sec                                                 | 3.26 sec: 1.22x slower                                           |
| unpickle_pure_python | 265 us                                                   | 345 us: 1.30x slower                                             |
| pickle_pure_python   | 374 us                                                   | 494 us: 1.32x slower                                             |
| xml_etree_process    | 82.1 ms                                                  | 111 ms: 1.35x slower                                             |
| Geometric mean       | (ref)                                                    | 1.14x slower                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|------------------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 20.1 ms: 1.26x slower                                            |
| python_startup_no_site | 8.79 ms                                                  | 12.2 ms: 1.38x slower                                            |
| Geometric mean         | (ref)                                                    | 1.32x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|-----------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_xml      | 61.6 ms                                                  | 79.5 ms: 1.29x slower                                            |
| genshi_text     | 28.6 ms                                                  | 38.2 ms: 1.34x slower                                            |
| django_template | 39.4 ms                                                  | 56.2 ms: 1.43x slower                                            |
| mako            | 14.0 ms                                                  | 22.3 ms: 1.60x slower                                            |
| Geometric mean  | (ref)                                                    | 1.41x slower                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| create_gc_cycles           | 3.39 ms                                                  | 2.15 ms: 1.58x faster                                            |
| async_tree_memoization_tg  | 663 ms                                                   | 505 ms: 1.31x faster                                             |
| async_tree_io_tg           | 1.16 sec                                                 | 923 ms: 1.26x faster                                             |
| async_tree_memoization     | 664 ms                                                   | 530 ms: 1.25x faster                                             |
| xml_etree_iterparse        | 159 ms                                                   | 130 ms: 1.23x faster                                             |
| regex_effbot               | 5.10 ms                                                  | 4.17 ms: 1.22x faster                                            |
| async_tree_none_tg         | 484 ms                                                   | 403 ms: 1.20x faster                                             |
| async_tree_io              | 1.14 sec                                                 | 959 ms: 1.19x faster                                             |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 688 ms: 1.16x faster                                             |
| async_tree_none            | 504 ms                                                   | 437 ms: 1.15x faster                                             |
| xml_etree_parse            | 203 ms                                                   | 179 ms: 1.13x faster                                             |
| gc_traversal               | 5.92 ms                                                  | 5.36 ms: 1.10x faster                                            |
| deepcopy                   | 479 us                                                   | 439 us: 1.09x faster                                             |
| sqlite_synth               | 4.08 us                                                  | 3.75 us: 1.09x faster                                            |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 733 ms: 1.08x faster                                             |
| json                       | 5.94 ms                                                  | 6.25 ms: 1.05x slower                                            |
| k_core                     | 2.99 sec                                                 | 3.19 sec: 1.07x slower                                           |
| scimark_fft                | 463 ms                                                   | 502 ms: 1.09x slower                                             |
| generators                 | 40.3 ms                                                  | 43.9 ms: 1.09x slower                                            |
| deepcopy_reduce            | 4.24 us                                                  | 4.63 us: 1.09x slower                                            |
| float                      | 95.8 ms                                                  | 105 ms: 1.09x slower                                             |
| go                         | 164 ms                                                   | 180 ms: 1.10x slower                                             |
| pycparser                  | 1.34 sec                                                 | 1.48 sec: 1.10x slower                                           |
| scimark_sor                | 164 ms                                                   | 181 ms: 1.10x slower                                             |
| mdp                        | 3.45 sec                                                 | 3.87 sec: 1.12x slower                                           |
| pyflate                    | 582 ms                                                   | 654 ms: 1.12x slower                                             |
| async_generators           | 500 ms                                                   | 566 ms: 1.13x slower                                             |
| pylint                     | 345 ms                                                   | 391 ms: 1.13x slower                                             |
| coroutines                 | 29.4 ms                                                  | 33.5 ms: 1.14x slower                                            |
| json_loads                 | 32.8 us                                                  | 37.6 us: 1.15x slower                                            |
| docutils                   | 2.96 sec                                                 | 3.40 sec: 1.15x slower                                           |
| telco                      | 10.5 ms                                                  | 12.2 ms: 1.17x slower                                            |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.85 ms: 1.18x slower                                            |
| json_dumps                 | 14.2 ms                                                  | 16.9 ms: 1.19x slower                                            |
| logging_silent             | 135 ns                                                   | 160 ns: 1.19x slower                                             |
| xml_etree_generate         | 118 ms                                                   | 141 ms: 1.19x slower                                             |
| sqlglot_optimize           | 65.2 ms                                                  | 78.5 ms: 1.20x slower                                            |
| pprint_safe_repr           | 962 ms                                                   | 1.16 sec: 1.21x slower                                           |
| sphinx                     | 1.20 sec                                                 | 1.45 sec: 1.21x slower                                           |
| pprint_pformat             | 1.99 sec                                                 | 2.41 sec: 1.21x slower                                           |
| regex_compile              | 134 ms                                                   | 162 ms: 1.21x slower                                             |
| connected_components       | 547 ms                                                   | 664 ms: 1.21x slower                                             |
| html5lib                   | 65.6 ms                                                  | 80.0 ms: 1.22x slower                                            |
| tomli_loads                | 2.67 sec                                                 | 3.26 sec: 1.22x slower                                           |
| sqlglot_normalize          | 131 ms                                                   | 161 ms: 1.23x slower                                             |
| 2to3                       | 313 ms                                                   | 385 ms: 1.23x slower                                             |
| shortest_path              | 565 ms                                                   | 701 ms: 1.24x slower                                             |
| coverage                   | 106 ms                                                   | 132 ms: 1.25x slower                                             |
| python_startup             | 16.0 ms                                                  | 20.1 ms: 1.26x slower                                            |
| thrift                     | 1.01 ms                                                  | 1.27 ms: 1.26x slower                                            |
| bpe_tokeniser              | 6.02 sec                                                 | 7.61 sec: 1.27x slower                                           |
| sympy_sum                  | 151 ms                                                   | 192 ms: 1.27x slower                                             |
| logging_format             | 8.10 us                                                  | 10.3 us: 1.27x slower                                            |
| chaos                      | 70.7 ms                                                  | 90.7 ms: 1.28x slower                                            |
| genshi_xml                 | 61.6 ms                                                  | 79.5 ms: 1.29x slower                                            |
| logging_simple             | 7.25 us                                                  | 9.40 us: 1.30x slower                                            |
| sympy_integrate            | 21.4 ms                                                  | 27.8 ms: 1.30x slower                                            |
| unpickle_pure_python       | 265 us                                                   | 345 us: 1.30x slower                                             |
| scimark_monte_carlo        | 87.8 ms                                                  | 115 ms: 1.31x slower                                             |
| crypto_pyaes               | 84.9 ms                                                  | 111 ms: 1.31x slower                                             |
| sympy_expand               | 472 ms                                                   | 620 ms: 1.31x slower                                             |
| nqueens                    | 105 ms                                                   | 138 ms: 1.32x slower                                             |
| hexiom                     | 7.34 ms                                                  | 9.70 ms: 1.32x slower                                            |
| scimark_lu                 | 146 ms                                                   | 193 ms: 1.32x slower                                             |
| pickle_pure_python         | 374 us                                                   | 494 us: 1.32x slower                                             |
| genshi_text                | 28.6 ms                                                  | 38.2 ms: 1.34x slower                                            |
| meteor_contest             | 117 ms                                                   | 157 ms: 1.35x slower                                             |
| richards                   | 54.5 ms                                                  | 73.4 ms: 1.35x slower                                            |
| xml_etree_process          | 82.1 ms                                                  | 111 ms: 1.35x slower                                             |
| sqlglot_transpile          | 1.84 ms                                                  | 2.48 ms: 1.35x slower                                            |
| sqlalchemy_declarative     | 154 ms                                                   | 210 ms: 1.36x slower                                             |
| comprehensions             | 20.8 us                                                  | 28.5 us: 1.37x slower                                            |
| raytrace                   | 310 ms                                                   | 425 ms: 1.37x slower                                             |
| python_startup_no_site     | 8.79 ms                                                  | 12.2 ms: 1.38x slower                                            |
| sympy_str                  | 265 ms                                                   | 369 ms: 1.39x slower                                             |
| bench_thread_pool          | 1.34 ms                                                  | 1.89 ms: 1.41x slower                                            |
| fannkuch                   | 478 ms                                                   | 675 ms: 1.41x slower                                             |
| sqlglot_parse              | 1.43 ms                                                  | 2.04 ms: 1.42x slower                                            |
| django_template            | 39.4 ms                                                  | 56.2 ms: 1.43x slower                                            |
| richards_super             | 60.8 ms                                                  | 87.4 ms: 1.44x slower                                            |
| typing_runtime_protocols   | 197 us                                                   | 289 us: 1.47x slower                                             |
| sqlalchemy_imperative      | 16.1 ms                                                  | 24.1 ms: 1.49x slower                                            |
| many_optionals             | 626 us                                                   | 953 us: 1.52x slower                                             |
| nbody                      | 118 ms                                                   | 184 ms: 1.55x slower                                             |
| deltablue                  | 3.97 ms                                                  | 6.31 ms: 1.59x slower                                            |
| mako                       | 14.0 ms                                                  | 22.3 ms: 1.60x slower                                            |
| subparsers                 | 20.3 ms                                                  | 34.4 ms: 1.69x slower                                            |
| bench_mp_pool              | 8.07 ms                                                  | 57.5 ms: 7.12x slower                                            |
| Geometric mean             | (ref)                                                    | 1.19x slower                                                     |

Benchmark hidden because not significant (7): pathlib, pidigits, deepcopy_memo, regex_dna, asyncio_websockets, regex_v8, spectral_norm
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20250121-3.14.0a4+-4844db8-NOGIL/bm-20250121-arminc-aarch64-mdboom-aa_test_2025-3.14.0a4+-4844db8.json: dulwich_log

- Geometric mean (including insignificant results): 1.140x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.14x
- 95% likely to have a slowdown of 1.13x
- 99% likely to have a slowdown of 1.10x

# Memory
- memory change: 1.23x