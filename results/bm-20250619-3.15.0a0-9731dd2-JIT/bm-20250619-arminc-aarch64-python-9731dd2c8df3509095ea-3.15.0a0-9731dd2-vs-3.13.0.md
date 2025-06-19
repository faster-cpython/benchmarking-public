# Results vs. 3.13.0

- fork: python
- ref: 9731dd2c8df3509095ea
- machine: linux-aarch64
- commit hash: 9731dd2
- commit date: 2025-06-19
- overall geometric mean: 1.042x faster
- HPT reliability: 98.60%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-arminc-aarch64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.09 sec: 1.04x slower                                                  |
| html5lib       | 65.6 ms                                                  | 63.1 ms: 1.04x faster                                                   |
| sphinx         | 1.20 sec                                                 | 1.17 sec: 1.03x faster                                                  |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-arminc-aarch64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 472 ms: 1.41x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 474 ms: 1.40x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 918 ms: 1.27x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 899 ms: 1.27x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 383 ms: 1.26x faster                                                    |
| async_tree_none            | 504 ms                                                   | 399 ms: 1.26x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 660 ms: 1.21x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 665 ms: 1.19x faster                                                    |
| async_generators           | 500 ms                                                   | 476 ms: 1.05x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.21x faster                                                            |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-arminc-aarch64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 83.4 ms: 1.15x faster                                                   |
| nbody          | 118 ms                                                   | 125 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-arminc-aarch64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.93 ms: 1.30x faster                                                   |
| regex_v8       | 32.5 ms                                                  | 27.4 ms: 1.19x faster                                                   |
| regex_dna      | 263 ms                                                   | 225 ms: 1.17x faster                                                    |
| regex_compile  | 134 ms                                                   | 122 ms: 1.09x faster                                                    |
| Geometric mean | (ref)                                                    | 1.19x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-arminc-aarch64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads         | 2.67 sec                                                 | 2.32 sec: 1.15x faster                                                  |
| xml_etree_parse     | 203 ms                                                   | 178 ms: 1.14x faster                                                    |
| xml_etree_iterparse | 159 ms                                                   | 144 ms: 1.11x faster                                                    |
| xml_etree_generate  | 118 ms                                                   | 110 ms: 1.07x faster                                                    |
| xml_etree_process   | 82.1 ms                                                  | 78.8 ms: 1.04x faster                                                   |
| pickle_pure_python  | 374 us                                                   | 405 us: 1.09x slower                                                    |
| Geometric mean      | (ref)                                                    | 1.06x faster                                                            |

Benchmark hidden because not significant (3): unpickle_pure_python, json_dumps, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-arminc-aarch64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 16.0 ms                                                  | 15.2 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-arminc-aarch64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 14.0 ms                                                  | 13.2 ms: 1.06x faster                                                   |
| django_template | 39.4 ms                                                  | 40.5 ms: 1.03x slower                                                   |
| genshi_xml      | 61.6 ms                                                  | 63.9 ms: 1.04x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-arminc-aarch64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.68 sec: 2.05x faster                                                  |
| deepcopy_memo              | 53.0 us                                                  | 37.4 us: 1.42x faster                                                   |
| async_tree_memoization     | 664 ms                                                   | 472 ms: 1.41x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 474 ms: 1.40x faster                                                    |
| deepcopy                   | 479 us                                                   | 342 us: 1.40x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 3.93 ms: 1.30x faster                                                   |
| async_tree_io_tg           | 1.16 sec                                                 | 918 ms: 1.27x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 899 ms: 1.27x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 383 ms: 1.26x faster                                                    |
| async_tree_none            | 504 ms                                                   | 399 ms: 1.26x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 660 ms: 1.21x faster                                                    |
| spectral_norm              | 143 ms                                                   | 121 ms: 1.19x faster                                                    |
| regex_v8                   | 32.5 ms                                                  | 27.4 ms: 1.19x faster                                                   |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 665 ms: 1.19x faster                                                    |
| richards                   | 54.5 ms                                                  | 46.0 ms: 1.19x faster                                                   |
| regex_dna                  | 263 ms                                                   | 225 ms: 1.17x faster                                                    |
| richards_super             | 60.8 ms                                                  | 52.1 ms: 1.17x faster                                                   |
| deepcopy_reduce            | 4.24 us                                                  | 3.66 us: 1.16x faster                                                   |
| tomli_loads                | 2.67 sec                                                 | 2.32 sec: 1.15x faster                                                  |
| float                      | 95.8 ms                                                  | 83.4 ms: 1.15x faster                                                   |
| scimark_sor                | 164 ms                                                   | 143 ms: 1.15x faster                                                    |
| scimark_fft                | 463 ms                                                   | 405 ms: 1.14x faster                                                    |
| xml_etree_parse            | 203 ms                                                   | 178 ms: 1.14x faster                                                    |
| generators                 | 40.3 ms                                                  | 36.0 ms: 1.12x faster                                                   |
| bpe_tokeniser              | 6.02 sec                                                 | 5.39 sec: 1.12x faster                                                  |
| xml_etree_iterparse        | 159 ms                                                   | 144 ms: 1.11x faster                                                    |
| telco                      | 10.5 ms                                                  | 9.55 ms: 1.10x faster                                                   |
| regex_compile              | 134 ms                                                   | 122 ms: 1.09x faster                                                    |
| pathlib                    | 24.3 ms                                                  | 22.3 ms: 1.09x faster                                                   |
| pylint                     | 345 ms                                                   | 318 ms: 1.08x faster                                                    |
| pyflate                    | 582 ms                                                   | 542 ms: 1.07x faster                                                    |
| xml_etree_generate         | 118 ms                                                   | 110 ms: 1.07x faster                                                    |
| mako                       | 14.0 ms                                                  | 13.2 ms: 1.06x faster                                                   |
| python_startup             | 16.0 ms                                                  | 15.2 ms: 1.06x faster                                                   |
| thrift                     | 1.01 ms                                                  | 958 us: 1.05x faster                                                    |
| sqlite_synth               | 4.08 us                                                  | 3.87 us: 1.05x faster                                                   |
| k_core                     | 2.99 sec                                                 | 2.84 sec: 1.05x faster                                                  |
| async_generators           | 500 ms                                                   | 476 ms: 1.05x faster                                                    |
| coverage                   | 106 ms                                                   | 101 ms: 1.05x faster                                                    |
| xml_etree_process          | 82.1 ms                                                  | 78.8 ms: 1.04x faster                                                   |
| go                         | 164 ms                                                   | 158 ms: 1.04x faster                                                    |
| html5lib                   | 65.6 ms                                                  | 63.1 ms: 1.04x faster                                                   |
| meteor_contest             | 117 ms                                                   | 113 ms: 1.03x faster                                                    |
| sphinx                     | 1.20 sec                                                 | 1.17 sec: 1.03x faster                                                  |
| djangocms                  | 66.2 us                                                  | 65.0 us: 1.02x faster                                                   |
| django_template            | 39.4 ms                                                  | 40.5 ms: 1.03x slower                                                   |
| logging_format             | 8.10 us                                                  | 8.38 us: 1.03x slower                                                   |
| connected_components       | 547 ms                                                   | 566 ms: 1.03x slower                                                    |
| genshi_xml                 | 61.6 ms                                                  | 63.9 ms: 1.04x slower                                                   |
| docutils                   | 2.96 sec                                                 | 3.09 sec: 1.04x slower                                                  |
| sympy_expand               | 472 ms                                                   | 493 ms: 1.04x slower                                                    |
| shortest_path              | 565 ms                                                   | 591 ms: 1.05x slower                                                    |
| sympy_str                  | 265 ms                                                   | 278 ms: 1.05x slower                                                    |
| nbody                      | 118 ms                                                   | 125 ms: 1.05x slower                                                    |
| logging_simple             | 7.25 us                                                  | 7.72 us: 1.07x slower                                                   |
| typing_runtime_protocols   | 197 us                                                   | 210 us: 1.07x slower                                                    |
| comprehensions             | 20.8 us                                                  | 22.4 us: 1.08x slower                                                   |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.19 ms: 1.08x slower                                                   |
| raytrace                   | 310 ms                                                   | 335 ms: 1.08x slower                                                    |
| crypto_pyaes               | 84.9 ms                                                  | 91.9 ms: 1.08x slower                                                   |
| pickle_pure_python         | 374 us                                                   | 405 us: 1.09x slower                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 3.82 ms: 1.13x slower                                                   |
| gc_traversal               | 5.92 ms                                                  | 6.88 ms: 1.16x slower                                                   |
| many_optionals             | 626 us                                                   | 814 us: 1.30x slower                                                    |
| pprint_pformat             | 1.99 sec                                                 | 2.61 sec: 1.31x slower                                                  |
| pprint_safe_repr           | 962 ms                                                   | 1.27 sec: 1.32x slower                                                  |
| subparsers                 | 20.3 ms                                                  | 29.1 ms: 1.43x slower                                                   |
| logging_silent             | 135 ns                                                   | 647 ns: 4.80x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (20): scimark_monte_carlo, unpickle_pure_python, json_dumps, json, deltablue, sympy_integrate, nqueens, genshi_text, chaos, json_loads, coroutines, python_startup_no_site, asyncio_websockets, sympy_sum, 2to3, pidigits, fannkuch, hexiom, pycparser, scimark_lu
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250619-3.15.0a0-9731dd2-JIT/bm-20250619-arminc-aarch64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.042x faster

# HPT report

- Reliability score: 98.60% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x