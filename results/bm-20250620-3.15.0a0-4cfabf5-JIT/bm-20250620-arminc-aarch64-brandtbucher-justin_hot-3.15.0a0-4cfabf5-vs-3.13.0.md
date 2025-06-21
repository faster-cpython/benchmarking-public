# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_hot
- machine: linux-aarch64
- commit hash: 4cfabf5
- commit date: 2025-06-20
- overall geometric mean: 1.047x faster
- HPT reliability: 99.22%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.12 sec: 1.05x slower                                              |
| html5lib       | 65.6 ms                                                  | 63.3 ms: 1.04x faster                                               |
| sphinx         | 1.20 sec                                                 | 1.17 sec: 1.03x faster                                              |
| Geometric mean | (ref)                                                    | 1.01x faster                                                        |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 471 ms: 1.41x faster                                                |
| async_tree_memoization     | 664 ms                                                   | 477 ms: 1.39x faster                                                |
| async_tree_none_tg         | 484 ms                                                   | 378 ms: 1.28x faster                                                |
| async_tree_io              | 1.14 sec                                                 | 895 ms: 1.27x faster                                                |
| async_tree_io_tg           | 1.16 sec                                                 | 918 ms: 1.27x faster                                                |
| async_tree_none            | 504 ms                                                   | 402 ms: 1.25x faster                                                |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 659 ms: 1.21x faster                                                |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 660 ms: 1.20x faster                                                |
| async_generators           | 500 ms                                                   | 480 ms: 1.04x faster                                                |
| Geometric mean             | (ref)                                                    | 1.20x faster                                                        |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 82.1 ms: 1.17x faster                                               |
| Geometric mean | (ref)                                                    | 1.06x faster                                                        |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.90 ms: 1.31x faster                                               |
| regex_v8       | 32.5 ms                                                  | 26.9 ms: 1.21x faster                                               |
| regex_dna      | 263 ms                                                   | 220 ms: 1.19x faster                                                |
| regex_compile  | 134 ms                                                   | 123 ms: 1.08x faster                                                |
| Geometric mean | (ref)                                                    | 1.20x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|---------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 180 ms: 1.13x faster                                                |
| tomli_loads         | 2.67 sec                                                 | 2.38 sec: 1.12x faster                                              |
| xml_etree_iterparse | 159 ms                                                   | 143 ms: 1.11x faster                                                |
| xml_etree_generate  | 118 ms                                                   | 108 ms: 1.10x faster                                                |
| xml_etree_process   | 82.1 ms                                                  | 78.4 ms: 1.05x faster                                               |
| Geometric mean      | (ref)                                                    | 1.05x faster                                                        |

Benchmark hidden because not significant (4): unpickle_pure_python, json_dumps, json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                               |
| python_startup_no_site | 8.79 ms                                                  | 8.58 ms: 1.02x faster                                               |
| Geometric mean         | (ref)                                                    | 1.04x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|-----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 28.6 ms                                                  | 26.8 ms: 1.07x faster                                               |
| mako            | 14.0 ms                                                  | 13.2 ms: 1.06x faster                                               |
| django_template | 39.4 ms                                                  | 40.7 ms: 1.03x slower                                               |
| Geometric mean  | (ref)                                                    | 1.02x faster                                                        |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.68 sec: 2.05x faster                                              |
| deepcopy                   | 479 us                                                   | 330 us: 1.45x faster                                                |
| deepcopy_memo              | 53.0 us                                                  | 36.6 us: 1.45x faster                                               |
| async_tree_memoization_tg  | 663 ms                                                   | 471 ms: 1.41x faster                                                |
| async_tree_memoization     | 664 ms                                                   | 477 ms: 1.39x faster                                                |
| regex_effbot               | 5.10 ms                                                  | 3.90 ms: 1.31x faster                                               |
| async_tree_none_tg         | 484 ms                                                   | 378 ms: 1.28x faster                                                |
| async_tree_io              | 1.14 sec                                                 | 895 ms: 1.27x faster                                                |
| async_tree_io_tg           | 1.16 sec                                                 | 918 ms: 1.27x faster                                                |
| async_tree_none            | 504 ms                                                   | 402 ms: 1.25x faster                                                |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 659 ms: 1.21x faster                                                |
| regex_v8                   | 32.5 ms                                                  | 26.9 ms: 1.21x faster                                               |
| richards                   | 54.5 ms                                                  | 45.6 ms: 1.20x faster                                               |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 660 ms: 1.20x faster                                                |
| regex_dna                  | 263 ms                                                   | 220 ms: 1.19x faster                                                |
| deepcopy_reduce            | 4.24 us                                                  | 3.60 us: 1.18x faster                                               |
| float                      | 95.8 ms                                                  | 82.1 ms: 1.17x faster                                               |
| richards_super             | 60.8 ms                                                  | 52.5 ms: 1.16x faster                                               |
| xml_etree_parse            | 203 ms                                                   | 180 ms: 1.13x faster                                                |
| scimark_sor                | 164 ms                                                   | 146 ms: 1.12x faster                                                |
| tomli_loads                | 2.67 sec                                                 | 2.38 sec: 1.12x faster                                              |
| bpe_tokeniser              | 6.02 sec                                                 | 5.39 sec: 1.12x faster                                              |
| scimark_fft                | 463 ms                                                   | 415 ms: 1.12x faster                                                |
| generators                 | 40.3 ms                                                  | 36.3 ms: 1.11x faster                                               |
| xml_etree_iterparse        | 159 ms                                                   | 143 ms: 1.11x faster                                                |
| telco                      | 10.5 ms                                                  | 9.52 ms: 1.10x faster                                               |
| pyflate                    | 582 ms                                                   | 529 ms: 1.10x faster                                                |
| xml_etree_generate         | 118 ms                                                   | 108 ms: 1.10x faster                                                |
| sqlite_synth               | 4.08 us                                                  | 3.73 us: 1.09x faster                                               |
| spectral_norm              | 143 ms                                                   | 131 ms: 1.09x faster                                                |
| scimark_monte_carlo        | 87.8 ms                                                  | 81.0 ms: 1.08x faster                                               |
| regex_compile              | 134 ms                                                   | 123 ms: 1.08x faster                                                |
| pylint                     | 345 ms                                                   | 320 ms: 1.08x faster                                                |
| thrift                     | 1.01 ms                                                  | 943 us: 1.07x faster                                                |
| genshi_text                | 28.6 ms                                                  | 26.8 ms: 1.07x faster                                               |
| k_core                     | 2.99 sec                                                 | 2.81 sec: 1.06x faster                                              |
| mako                       | 14.0 ms                                                  | 13.2 ms: 1.06x faster                                               |
| python_startup             | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                               |
| nqueens                    | 105 ms                                                   | 100 ms: 1.05x faster                                                |
| xml_etree_process          | 82.1 ms                                                  | 78.4 ms: 1.05x faster                                               |
| async_generators           | 500 ms                                                   | 480 ms: 1.04x faster                                                |
| html5lib                   | 65.6 ms                                                  | 63.3 ms: 1.04x faster                                               |
| sphinx                     | 1.20 sec                                                 | 1.17 sec: 1.03x faster                                              |
| python_startup_no_site     | 8.79 ms                                                  | 8.58 ms: 1.02x faster                                               |
| djangocms                  | 66.2 us                                                  | 65.0 us: 1.02x faster                                               |
| connected_components       | 547 ms                                                   | 563 ms: 1.03x slower                                                |
| django_template            | 39.4 ms                                                  | 40.7 ms: 1.03x slower                                               |
| shortest_path              | 565 ms                                                   | 587 ms: 1.04x slower                                                |
| pycparser                  | 1.34 sec                                                 | 1.40 sec: 1.04x slower                                              |
| sympy_expand               | 472 ms                                                   | 492 ms: 1.04x slower                                                |
| docutils                   | 2.96 sec                                                 | 3.12 sec: 1.05x slower                                              |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.02 ms: 1.06x slower                                               |
| raytrace                   | 310 ms                                                   | 331 ms: 1.07x slower                                                |
| logging_simple             | 7.25 us                                                  | 7.75 us: 1.07x slower                                               |
| sympy_str                  | 265 ms                                                   | 284 ms: 1.07x slower                                                |
| typing_runtime_protocols   | 197 us                                                   | 212 us: 1.08x slower                                                |
| comprehensions             | 20.8 us                                                  | 22.6 us: 1.08x slower                                               |
| crypto_pyaes               | 84.9 ms                                                  | 94.0 ms: 1.11x slower                                               |
| create_gc_cycles           | 3.39 ms                                                  | 3.77 ms: 1.11x slower                                               |
| gc_traversal               | 5.92 ms                                                  | 6.78 ms: 1.15x slower                                               |
| pprint_safe_repr           | 962 ms                                                   | 1.25 sec: 1.30x slower                                              |
| pprint_pformat             | 1.99 sec                                                 | 2.58 sec: 1.30x slower                                              |
| many_optionals             | 626 us                                                   | 817 us: 1.30x slower                                                |
| subparsers                 | 20.3 ms                                                  | 28.5 ms: 1.40x slower                                               |
| logging_silent             | 135 ns                                                   | 611 ns: 4.54x slower                                                |
| Geometric mean             | (ref)                                                    | 1.04x faster                                                        |

Benchmark hidden because not significant (23): pathlib, json, unpickle_pure_python, sympy_sum, coverage, json_dumps, meteor_contest, chaos, go, asyncio_websockets, pidigits, deltablue, 2to3, fannkuch, sympy_integrate, nbody, json_loads, hexiom, coroutines, genshi_xml, logging_format, scimark_lu, pickle_pure_python
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250620-3.15.0a0-4cfabf5-JIT/bm-20250620-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-4cfabf5.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.047x faster

# HPT report

- Reliability score: 99.22% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x