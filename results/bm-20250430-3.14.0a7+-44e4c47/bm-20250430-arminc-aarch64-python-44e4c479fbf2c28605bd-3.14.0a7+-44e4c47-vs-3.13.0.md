# Results vs. 3.13.0

- fork: python
- ref: 44e4c479fbf2c28605bd
- machine: linux-aarch64
- commit hash: 44e4c47
- commit date: 2025-04-30
- overall geometric mean: 1.063x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-arminc-aarch64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 298 ms: 1.05x faster                                                     |
| html5lib       | 65.6 ms                                                  | 61.5 ms: 1.07x faster                                                    |
| sphinx         | 1.20 sec                                                 | 1.15 sec: 1.04x faster                                                   |
| Geometric mean | (ref)                                                    | 1.04x faster                                                             |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-arminc-aarch64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 466 ms: 1.43x faster                                                     |
| async_tree_memoization_tg  | 663 ms                                                   | 465 ms: 1.42x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 878 ms: 1.33x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 374 ms: 1.30x faster                                                     |
| async_tree_none            | 504 ms                                                   | 393 ms: 1.28x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 897 ms: 1.27x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 656 ms: 1.22x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 676 ms: 1.17x faster                                                     |
| async_generators           | 500 ms                                                   | 454 ms: 1.10x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.22x faster                                                             |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-arminc-aarch64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 85.9 ms: 1.12x faster                                                    |
| Geometric mean | (ref)                                                    | 1.03x faster                                                             |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-arminc-aarch64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.83 ms: 1.33x faster                                                    |
| regex_v8       | 32.5 ms                                                  | 27.4 ms: 1.19x faster                                                    |
| regex_dna      | 263 ms                                                   | 236 ms: 1.11x faster                                                     |
| regex_compile  | 134 ms                                                   | 124 ms: 1.07x faster                                                     |
| Geometric mean | (ref)                                                    | 1.17x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-arminc-aarch64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 176 ms: 1.15x faster                                                     |
| xml_etree_iterparse | 159 ms                                                   | 141 ms: 1.12x faster                                                     |
| tomli_loads         | 2.67 sec                                                 | 2.44 sec: 1.09x faster                                                   |
| json_loads          | 32.8 us                                                  | 35.5 us: 1.08x slower                                                    |
| Geometric mean      | (ref)                                                    | 1.03x faster                                                             |

Benchmark hidden because not significant (5): xml_etree_generate, xml_etree_process, unpickle_pure_python, json_dumps, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-arminc-aarch64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 8.62 ms: 1.02x faster                                                    |
| Geometric mean         | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-arminc-aarch64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 28.6 ms                                                  | 26.5 ms: 1.08x faster                                                    |
| django_template | 39.4 ms                                                  | 39.0 ms: 1.01x faster                                                    |
| Geometric mean  | (ref)                                                    | 1.02x faster                                                             |

Benchmark hidden because not significant (2): mako, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-arminc-aarch64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.68 sec: 2.05x faster                                                   |
| deepcopy                   | 479 us                                                   | 326 us: 1.47x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 466 ms: 1.43x faster                                                     |
| async_tree_memoization_tg  | 663 ms                                                   | 465 ms: 1.42x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 38.1 us: 1.39x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 3.83 ms: 1.33x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 878 ms: 1.33x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 374 ms: 1.30x faster                                                     |
| async_tree_none            | 504 ms                                                   | 393 ms: 1.28x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 897 ms: 1.27x faster                                                     |
| go                         | 164 ms                                                   | 129 ms: 1.27x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 656 ms: 1.22x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.53 us: 1.20x faster                                                    |
| regex_v8                   | 32.5 ms                                                  | 27.4 ms: 1.19x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 676 ms: 1.17x faster                                                     |
| xml_etree_parse            | 203 ms                                                   | 176 ms: 1.15x faster                                                     |
| xml_etree_iterparse        | 159 ms                                                   | 141 ms: 1.12x faster                                                     |
| scimark_sor                | 164 ms                                                   | 147 ms: 1.12x faster                                                     |
| float                      | 95.8 ms                                                  | 85.9 ms: 1.12x faster                                                    |
| regex_dna                  | 263 ms                                                   | 236 ms: 1.11x faster                                                     |
| bpe_tokeniser              | 6.02 sec                                                 | 5.43 sec: 1.11x faster                                                   |
| async_generators           | 500 ms                                                   | 454 ms: 1.10x faster                                                     |
| telco                      | 10.5 ms                                                  | 9.51 ms: 1.10x faster                                                    |
| generators                 | 40.3 ms                                                  | 36.7 ms: 1.10x faster                                                    |
| pathlib                    | 24.3 ms                                                  | 22.2 ms: 1.10x faster                                                    |
| tomli_loads                | 2.67 sec                                                 | 2.44 sec: 1.09x faster                                                   |
| scimark_monte_carlo        | 87.8 ms                                                  | 80.4 ms: 1.09x faster                                                    |
| spectral_norm              | 143 ms                                                   | 132 ms: 1.09x faster                                                     |
| genshi_text                | 28.6 ms                                                  | 26.5 ms: 1.08x faster                                                    |
| pycparser                  | 1.34 sec                                                 | 1.25 sec: 1.08x faster                                                   |
| regex_compile              | 134 ms                                                   | 124 ms: 1.07x faster                                                     |
| richards                   | 54.5 ms                                                  | 50.8 ms: 1.07x faster                                                    |
| pprint_pformat             | 1.99 sec                                                 | 1.85 sec: 1.07x faster                                                   |
| pylint                     | 345 ms                                                   | 323 ms: 1.07x faster                                                     |
| sympy_sum                  | 151 ms                                                   | 142 ms: 1.07x faster                                                     |
| html5lib                   | 65.6 ms                                                  | 61.5 ms: 1.07x faster                                                    |
| nqueens                    | 105 ms                                                   | 98.4 ms: 1.07x faster                                                    |
| sympy_integrate            | 21.4 ms                                                  | 20.1 ms: 1.07x faster                                                    |
| sqlite_synth               | 4.08 us                                                  | 3.83 us: 1.07x faster                                                    |
| richards_super             | 60.8 ms                                                  | 57.1 ms: 1.06x faster                                                    |
| pyflate                    | 582 ms                                                   | 548 ms: 1.06x faster                                                     |
| pprint_safe_repr           | 962 ms                                                   | 908 ms: 1.06x faster                                                     |
| hexiom                     | 7.34 ms                                                  | 6.96 ms: 1.06x faster                                                    |
| deltablue                  | 3.97 ms                                                  | 3.77 ms: 1.05x faster                                                    |
| k_core                     | 2.99 sec                                                 | 2.85 sec: 1.05x faster                                                   |
| logging_format             | 8.10 us                                                  | 7.72 us: 1.05x faster                                                    |
| 2to3                       | 313 ms                                                   | 298 ms: 1.05x faster                                                     |
| scimark_fft                | 463 ms                                                   | 442 ms: 1.05x faster                                                     |
| chaos                      | 70.7 ms                                                  | 67.5 ms: 1.05x faster                                                    |
| sphinx                     | 1.20 sec                                                 | 1.15 sec: 1.04x faster                                                   |
| meteor_contest             | 117 ms                                                   | 112 ms: 1.04x faster                                                     |
| logging_simple             | 7.25 us                                                  | 6.97 us: 1.04x faster                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 8.62 ms: 1.02x faster                                                    |
| django_template            | 39.4 ms                                                  | 39.0 ms: 1.01x faster                                                    |
| shortest_path              | 565 ms                                                   | 582 ms: 1.03x slower                                                     |
| connected_components       | 547 ms                                                   | 563 ms: 1.03x slower                                                     |
| raytrace                   | 310 ms                                                   | 322 ms: 1.04x slower                                                     |
| coverage                   | 106 ms                                                   | 111 ms: 1.05x slower                                                     |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.02 ms: 1.05x slower                                                    |
| json_loads                 | 32.8 us                                                  | 35.5 us: 1.08x slower                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 3.71 ms: 1.09x slower                                                    |
| gc_traversal               | 5.92 ms                                                  | 6.66 ms: 1.12x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 25.8 ms: 1.27x slower                                                    |
| many_optionals             | 626 us                                                   | 844 us: 1.35x slower                                                     |
| bench_mp_pool              | 8.07 ms                                                  | 2.81 sec: 348.72x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.00x faster                                                             |

Benchmark hidden because not significant (25): xml_etree_generate, sqlalchemy_declarative, xml_etree_process, sympy_expand, logging_silent, scimark_lu, pidigits, sqlalchemy_imperative, asyncio_websockets, mako, comprehensions, unpickle_pure_python, docutils, python_startup, coroutines, crypto_pyaes, typing_runtime_protocols, fannkuch, json_dumps, bench_thread_pool, sympy_str, genshi_xml, pickle_pure_python, json, nbody
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (5) of results/bm-20250430-3.14.0a7+-44e4c47/bm-20250430-arminc-aarch64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.063x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.04x