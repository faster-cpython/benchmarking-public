# Results vs. 3.13.0

- fork: python
- ref: 1e69cd1634e4f0f8c375
- machine: linux-aarch64
- commit hash: 1e69cd1
- commit date: 2025-07-25
- overall geometric mean: 1.007x faster
- HPT reliability: 98.88%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-arminc-aarch64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.10 sec: 1.04x slower                                                  |
| sphinx         | 1.20 sec                                                 | 1.15 sec: 1.04x faster                                                  |
| Geometric mean | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-arminc-aarch64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 464 ms: 1.43x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 471 ms: 1.41x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 378 ms: 1.28x faster                                                    |
| async_tree_none            | 504 ms                                                   | 395 ms: 1.28x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 900 ms: 1.27x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 922 ms: 1.26x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 658 ms: 1.22x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 667 ms: 1.18x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.20x faster                                                            |

Benchmark hidden because not significant (3): async_generators, asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-arminc-aarch64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 82.4 ms: 1.16x faster                                                   |
| nbody          | 118 ms                                                   | 129 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-arminc-aarch64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.79 ms: 1.35x faster                                                   |
| regex_v8       | 32.5 ms                                                  | 26.3 ms: 1.24x faster                                                   |
| regex_dna      | 263 ms                                                   | 218 ms: 1.21x faster                                                    |
| regex_compile  | 134 ms                                                   | 125 ms: 1.07x faster                                                    |
| Geometric mean | (ref)                                                    | 1.21x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-arminc-aarch64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads         | 2.67 sec                                                 | 2.32 sec: 1.15x faster                                                  |
| xml_etree_parse     | 203 ms                                                   | 178 ms: 1.14x faster                                                    |
| xml_etree_iterparse | 159 ms                                                   | 145 ms: 1.10x faster                                                    |
| xml_etree_generate  | 118 ms                                                   | 109 ms: 1.09x faster                                                    |
| pickle_pure_python  | 374 us                                                   | 403 us: 1.08x slower                                                    |
| Geometric mean      | (ref)                                                    | 1.05x faster                                                            |

Benchmark hidden because not significant (4): unpickle_pure_python, xml_etree_process, json_dumps, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-arminc-aarch64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 15.1 ms: 1.07x faster                                                   |
| python_startup_no_site | 8.79 ms                                                  | 8.56 ms: 1.03x faster                                                   |
| Geometric mean         | (ref)                                                    | 1.05x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-arminc-aarch64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 14.0 ms                                                  | 13.0 ms: 1.08x faster                                                   |
| genshi_text     | 28.6 ms                                                  | 27.3 ms: 1.05x faster                                                   |
| django_template | 39.4 ms                                                  | 39.1 ms: 1.01x faster                                                   |
| genshi_xml      | 61.6 ms                                                  | 64.8 ms: 1.05x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.02x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-arminc-aarch64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.67 sec: 2.06x faster                                                  |
| deepcopy                   | 479 us                                                   | 331 us: 1.45x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 464 ms: 1.43x faster                                                    |
| deepcopy_memo              | 53.0 us                                                  | 37.1 us: 1.43x faster                                                   |
| async_tree_memoization     | 664 ms                                                   | 471 ms: 1.41x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 3.79 ms: 1.35x faster                                                   |
| async_tree_none_tg         | 484 ms                                                   | 378 ms: 1.28x faster                                                    |
| async_tree_none            | 504 ms                                                   | 395 ms: 1.28x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 900 ms: 1.27x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 922 ms: 1.26x faster                                                    |
| regex_v8                   | 32.5 ms                                                  | 26.3 ms: 1.24x faster                                                   |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 658 ms: 1.22x faster                                                    |
| richards                   | 54.5 ms                                                  | 45.0 ms: 1.21x faster                                                   |
| regex_dna                  | 263 ms                                                   | 218 ms: 1.21x faster                                                    |
| spectral_norm              | 143 ms                                                   | 119 ms: 1.20x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 667 ms: 1.18x faster                                                    |
| richards_super             | 60.8 ms                                                  | 51.5 ms: 1.18x faster                                                   |
| deepcopy_reduce            | 4.24 us                                                  | 3.63 us: 1.17x faster                                                   |
| float                      | 95.8 ms                                                  | 82.4 ms: 1.16x faster                                                   |
| tomli_loads                | 2.67 sec                                                 | 2.32 sec: 1.15x faster                                                  |
| scimark_sor                | 164 ms                                                   | 143 ms: 1.14x faster                                                    |
| xml_etree_parse            | 203 ms                                                   | 178 ms: 1.14x faster                                                    |
| generators                 | 40.3 ms                                                  | 35.6 ms: 1.13x faster                                                   |
| scimark_fft                | 463 ms                                                   | 414 ms: 1.12x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.40 sec: 1.11x faster                                                  |
| sqlite_synth               | 4.08 us                                                  | 3.71 us: 1.10x faster                                                   |
| xml_etree_iterparse        | 159 ms                                                   | 145 ms: 1.10x faster                                                    |
| pathlib                    | 24.3 ms                                                  | 22.2 ms: 1.10x faster                                                   |
| xml_etree_generate         | 118 ms                                                   | 109 ms: 1.09x faster                                                    |
| pyflate                    | 582 ms                                                   | 536 ms: 1.08x faster                                                    |
| mako                       | 14.0 ms                                                  | 13.0 ms: 1.08x faster                                                   |
| go                         | 164 ms                                                   | 154 ms: 1.07x faster                                                    |
| python_startup             | 16.0 ms                                                  | 15.1 ms: 1.07x faster                                                   |
| regex_compile              | 134 ms                                                   | 125 ms: 1.07x faster                                                    |
| pylint                     | 345 ms                                                   | 325 ms: 1.06x faster                                                    |
| k_core                     | 2.99 sec                                                 | 2.83 sec: 1.06x faster                                                  |
| logging_format             | 8.10 us                                                  | 7.68 us: 1.06x faster                                                   |
| genshi_text                | 28.6 ms                                                  | 27.3 ms: 1.05x faster                                                   |
| sphinx                     | 1.20 sec                                                 | 1.15 sec: 1.04x faster                                                  |
| python_startup_no_site     | 8.79 ms                                                  | 8.56 ms: 1.03x faster                                                   |
| djangocms                  | 66.2 us                                                  | 65.0 us: 1.02x faster                                                   |
| django_template            | 39.4 ms                                                  | 39.1 ms: 1.01x faster                                                   |
| typing_runtime_protocols   | 197 us                                                   | 203 us: 1.03x slower                                                    |
| sympy_expand               | 472 ms                                                   | 488 ms: 1.03x slower                                                    |
| connected_components       | 547 ms                                                   | 565 ms: 1.03x slower                                                    |
| sympy_str                  | 265 ms                                                   | 275 ms: 1.04x slower                                                    |
| docutils                   | 2.96 sec                                                 | 3.10 sec: 1.04x slower                                                  |
| shortest_path              | 565 ms                                                   | 595 ms: 1.05x slower                                                    |
| genshi_xml                 | 61.6 ms                                                  | 64.8 ms: 1.05x slower                                                   |
| comprehensions             | 20.8 us                                                  | 22.3 us: 1.07x slower                                                   |
| raytrace                   | 310 ms                                                   | 333 ms: 1.07x slower                                                    |
| pickle_pure_python         | 374 us                                                   | 403 us: 1.08x slower                                                    |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.23 ms: 1.09x slower                                                   |
| nbody                      | 118 ms                                                   | 129 ms: 1.09x slower                                                    |
| crypto_pyaes               | 84.9 ms                                                  | 93.5 ms: 1.10x slower                                                   |
| create_gc_cycles           | 3.39 ms                                                  | 3.76 ms: 1.11x slower                                                   |
| gc_traversal               | 5.92 ms                                                  | 6.82 ms: 1.15x slower                                                   |
| pprint_pformat             | 1.99 sec                                                 | 2.30 sec: 1.16x slower                                                  |
| pprint_safe_repr           | 962 ms                                                   | 1.14 sec: 1.19x slower                                                  |
| many_optionals             | 626 us                                                   | 984 us: 1.57x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 48.5 ms: 2.39x slower                                                   |
| telco                      | 10.5 ms                                                  | 164 ms: 15.65x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (26): scimark_monte_carlo, thrift, unpickle_pure_python, coverage, logging_simple, deltablue, meteor_contest, sympy_integrate, fannkuch, sympy_sum, xml_etree_process, logging_silent, json, nqueens, async_generators, json_dumps, html5lib, asyncio_websockets, chaos, 2to3, pidigits, scimark_lu, pycparser, json_loads, coroutines, hexiom
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250725-3.15.0a0-1e69cd1-JIT/bm-20250725-arminc-aarch64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.007x faster

# HPT report

- Reliability score: 98.88% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x