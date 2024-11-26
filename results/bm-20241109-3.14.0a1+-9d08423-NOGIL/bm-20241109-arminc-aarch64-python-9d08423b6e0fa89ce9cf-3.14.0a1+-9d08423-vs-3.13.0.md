# Results vs. 3.13.0

- fork: python
- ref: 9d08423b6e0fa89ce9cf
- machine: linux-aarch64
- commit hash: 9d08423
- commit date: 2024-11-09
- overall geometric mean: 1.375x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.40x slower
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 538 ms: 1.77x slower                                                     |
| docutils       | 2.89 sec                                                 | 4.28 sec: 1.48x slower                                                   |
| html5lib       | 66.4 ms                                                  | 123 ms: 1.85x slower                                                     |
| sphinx         | 1.17 sec                                                 | 1.70 sec: 1.46x slower                                                   |
| Geometric mean | (ref)                                                    | 1.63x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| asyncio_websockets         | 659 ms                                                   | 687 ms: 1.04x slower                                                     |
| async_tree_memoization_tg  | 649 ms                                                   | 759 ms: 1.17x slower                                                     |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 925 ms: 1.20x slower                                                     |
| async_tree_memoization     | 651 ms                                                   | 790 ms: 1.21x slower                                                     |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 951 ms: 1.24x slower                                                     |
| async_tree_io_tg           | 1.13 sec                                                 | 1.44 sec: 1.27x slower                                                   |
| async_tree_none            | 497 ms                                                   | 635 ms: 1.28x slower                                                     |
| async_tree_none_tg         | 470 ms                                                   | 614 ms: 1.31x slower                                                     |
| async_tree_io              | 1.11 sec                                                 | 1.47 sec: 1.32x slower                                                   |
| coroutines                 | 28.5 ms                                                  | 40.6 ms: 1.43x slower                                                    |
| async_generators           | 489 ms                                                   | 703 ms: 1.44x slower                                                     |
| Geometric mean             | (ref)                                                    | 1.26x slower                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 93.3 ms                                                  | 213 ms: 2.29x slower                                                     |
| nbody          | 114 ms                                                   | 280 ms: 2.44x slower                                                     |
| Geometric mean | (ref)                                                    | 1.79x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 253 ms                                                   | 271 ms: 1.07x slower                                                     |
| regex_v8       | 31.8 ms                                                  | 35.4 ms: 1.11x slower                                                    |
| regex_compile  | 127 ms                                                   | 256 ms: 2.01x slower                                                     |
| Geometric mean | (ref)                                                    | 1.24x slower                                                             |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                   | 187 ms: 1.05x faster                                                     |
| xml_etree_iterparse  | 149 ms                                                   | 158 ms: 1.06x slower                                                     |
| json_loads           | 31.7 us                                                  | 39.2 us: 1.24x slower                                                    |
| xml_etree_generate   | 113 ms                                                   | 164 ms: 1.45x slower                                                     |
| json_dumps           | 13.6 ms                                                  | 20.2 ms: 1.49x slower                                                    |
| xml_etree_process    | 80.5 ms                                                  | 133 ms: 1.65x slower                                                     |
| tomli_loads          | 2.54 sec                                                 | 4.28 sec: 1.68x slower                                                   |
| unpickle_pure_python | 251 us                                                   | 567 us: 2.26x slower                                                     |
| pickle_pure_python   | 357 us                                                   | 842 us: 2.36x slower                                                     |
| Geometric mean       | (ref)                                                    | 1.51x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 15.4 ms                                                  | 21.1 ms: 1.37x slower                                                    |
| python_startup_no_site | 8.73 ms                                                  | 12.5 ms: 1.44x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.40x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 60.3 ms                                                  | 104 ms: 1.72x slower                                                     |
| django_template | 41.6 ms                                                  | 83.8 ms: 2.01x slower                                                    |
| genshi_text     | 27.7 ms                                                  | 56.6 ms: 2.04x slower                                                    |
| mako            | 13.4 ms                                                  | 29.3 ms: 2.19x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.98x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| gc_traversal               | 5.77 ms                                                  | 4.48 ms: 1.29x faster                                                    |
| create_gc_cycles           | 3.35 ms                                                  | 2.65 ms: 1.26x faster                                                    |
| xml_etree_parse            | 197 ms                                                   | 187 ms: 1.05x faster                                                     |
| asyncio_websockets         | 659 ms                                                   | 687 ms: 1.04x slower                                                     |
| xml_etree_iterparse        | 149 ms                                                   | 158 ms: 1.06x slower                                                     |
| regex_dna                  | 253 ms                                                   | 271 ms: 1.07x slower                                                     |
| regex_v8                   | 31.8 ms                                                  | 35.4 ms: 1.11x slower                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 759 ms: 1.17x slower                                                     |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 925 ms: 1.20x slower                                                     |
| k_core                     | 2.96 sec                                                 | 3.59 sec: 1.21x slower                                                   |
| async_tree_memoization     | 651 ms                                                   | 790 ms: 1.21x slower                                                     |
| deepcopy                   | 447 us                                                   | 547 us: 1.22x slower                                                     |
| json                       | 5.73 ms                                                  | 7.01 ms: 1.22x slower                                                    |
| scimark_fft                | 447 ms                                                   | 549 ms: 1.23x slower                                                     |
| json_loads                 | 31.7 us                                                  | 39.2 us: 1.24x slower                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 951 ms: 1.24x slower                                                     |
| pathlib                    | 22.7 ms                                                  | 28.4 ms: 1.25x slower                                                    |
| async_tree_io_tg           | 1.13 sec                                                 | 1.44 sec: 1.27x slower                                                   |
| async_tree_none            | 497 ms                                                   | 635 ms: 1.28x slower                                                     |
| shortest_path              | 565 ms                                                   | 737 ms: 1.30x slower                                                     |
| async_tree_none_tg         | 470 ms                                                   | 614 ms: 1.31x slower                                                     |
| async_tree_io              | 1.11 sec                                                 | 1.47 sec: 1.32x slower                                                   |
| telco                      | 9.74 ms                                                  | 13.0 ms: 1.34x slower                                                    |
| connected_components       | 533 ms                                                   | 714 ms: 1.34x slower                                                     |
| mdp                        | 3.34 sec                                                 | 4.52 sec: 1.35x slower                                                   |
| python_startup             | 15.4 ms                                                  | 21.1 ms: 1.37x slower                                                    |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 8.93 ms: 1.37x slower                                                    |
| deepcopy_memo              | 50.4 us                                                  | 70.6 us: 1.40x slower                                                    |
| coroutines                 | 28.5 ms                                                  | 40.6 ms: 1.43x slower                                                    |
| coverage                   | 99.1 ms                                                  | 142 ms: 1.43x slower                                                     |
| async_generators           | 489 ms                                                   | 703 ms: 1.44x slower                                                     |
| python_startup_no_site     | 8.73 ms                                                  | 12.5 ms: 1.44x slower                                                    |
| xml_etree_generate         | 113 ms                                                   | 164 ms: 1.45x slower                                                     |
| sphinx                     | 1.17 sec                                                 | 1.70 sec: 1.46x slower                                                   |
| docutils                   | 2.89 sec                                                 | 4.28 sec: 1.48x slower                                                   |
| json_dumps                 | 13.6 ms                                                  | 20.2 ms: 1.49x slower                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 6.08 us: 1.49x slower                                                    |
| pylint                     | 342 ms                                                   | 523 ms: 1.53x slower                                                     |
| spectral_norm              | 143 ms                                                   | 219 ms: 1.53x slower                                                     |
| meteor_contest             | 114 ms                                                   | 177 ms: 1.56x slower                                                     |
| nqueens                    | 100 ms                                                   | 159 ms: 1.59x slower                                                     |
| bpe_tokeniser              | 5.87 sec                                                 | 9.36 sec: 1.59x slower                                                   |
| bench_thread_pool          | 1.27 ms                                                  | 2.07 ms: 1.62x slower                                                    |
| fannkuch                   | 461 ms                                                   | 751 ms: 1.63x slower                                                     |
| xml_etree_process          | 80.5 ms                                                  | 133 ms: 1.65x slower                                                     |
| generators                 | 37.6 ms                                                  | 62.3 ms: 1.66x slower                                                    |
| pycparser                  | 1.27 sec                                                 | 2.14 sec: 1.68x slower                                                   |
| tomli_loads                | 2.54 sec                                                 | 4.28 sec: 1.68x slower                                                   |
| genshi_xml                 | 60.3 ms                                                  | 104 ms: 1.72x slower                                                     |
| crypto_pyaes               | 83.7 ms                                                  | 144 ms: 1.72x slower                                                     |
| sympy_integrate            | 20.8 ms                                                  | 36.3 ms: 1.74x slower                                                    |
| 2to3                       | 304 ms                                                   | 538 ms: 1.77x slower                                                     |
| thrift                     | 968 us                                                   | 1.72 ms: 1.78x slower                                                    |
| typing_runtime_protocols   | 193 us                                                   | 348 us: 1.80x slower                                                     |
| sqlalchemy_declarative     | 150 ms                                                   | 273 ms: 1.81x slower                                                     |
| sqlglot_optimize           | 62.2 ms                                                  | 115 ms: 1.85x slower                                                     |
| html5lib                   | 66.4 ms                                                  | 123 ms: 1.85x slower                                                     |
| pyflate                    | 556 ms                                                   | 1.03 sec: 1.86x slower                                                   |
| sqlglot_normalize          | 127 ms                                                   | 236 ms: 1.86x slower                                                     |
| pprint_safe_repr           | 926 ms                                                   | 1.76 sec: 1.90x slower                                                   |
| pprint_pformat             | 1.90 sec                                                 | 3.61 sec: 1.90x slower                                                   |
| sympy_str                  | 264 ms                                                   | 532 ms: 2.01x slower                                                     |
| regex_compile              | 127 ms                                                   | 256 ms: 2.01x slower                                                     |
| django_template            | 41.6 ms                                                  | 83.8 ms: 2.01x slower                                                    |
| genshi_text                | 27.7 ms                                                  | 56.6 ms: 2.04x slower                                                    |
| comprehensions             | 20.4 us                                                  | 42.8 us: 2.10x slower                                                    |
| logging_format             | 7.82 us                                                  | 16.5 us: 2.11x slower                                                    |
| scimark_monte_carlo        | 83.6 ms                                                  | 177 ms: 2.12x slower                                                     |
| logging_simple             | 7.07 us                                                  | 15.0 us: 2.12x slower                                                    |
| sqlalchemy_imperative      | 15.1 ms                                                  | 32.2 ms: 2.12x slower                                                    |
| sympy_expand               | 457 ms                                                   | 988 ms: 2.16x slower                                                     |
| scimark_sor                | 160 ms                                                   | 346 ms: 2.17x slower                                                     |
| mako                       | 13.4 ms                                                  | 29.3 ms: 2.19x slower                                                    |
| logging_silent             | 133 ns                                                   | 292 ns: 2.20x slower                                                     |
| richards                   | 53.6 ms                                                  | 121 ms: 2.25x slower                                                     |
| hexiom                     | 7.11 ms                                                  | 16.0 ms: 2.26x slower                                                    |
| unpickle_pure_python       | 251 us                                                   | 567 us: 2.26x slower                                                     |
| float                      | 93.3 ms                                                  | 213 ms: 2.29x slower                                                     |
| sympy_sum                  | 144 ms                                                   | 329 ms: 2.29x slower                                                     |
| chaos                      | 68.0 ms                                                  | 159 ms: 2.34x slower                                                     |
| pickle_pure_python         | 357 us                                                   | 842 us: 2.36x slower                                                     |
| nbody                      | 114 ms                                                   | 280 ms: 2.44x slower                                                     |
| richards_super             | 60.1 ms                                                  | 147 ms: 2.45x slower                                                     |
| scimark_lu                 | 139 ms                                                   | 346 ms: 2.49x slower                                                     |
| go                         | 160 ms                                                   | 402 ms: 2.52x slower                                                     |
| sqlglot_transpile          | 1.73 ms                                                  | 4.49 ms: 2.59x slower                                                    |
| sqlglot_parse              | 1.38 ms                                                  | 3.81 ms: 2.77x slower                                                    |
| raytrace                   | 300 ms                                                   | 835 ms: 2.79x slower                                                     |
| deltablue                  | 3.82 ms                                                  | 13.4 ms: 3.50x slower                                                    |
| bench_mp_pool              | 7.68 ms                                                  | 63.5 ms: 8.27x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.66x slower                                                             |

Benchmark hidden because not significant (2): regex_effbot, pidigits
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (2) of results/bm-20241109-3.14.0a1+-9d08423-NOGIL/bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json: dulwich_log, sqlite_synth

- Geometric mean (including insignificant results): 1.375x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.46x
- 95% likely to have a slowdown of 1.43x
- 99% likely to have a slowdown of 1.40x

# Memory
- memory change: 1.22x