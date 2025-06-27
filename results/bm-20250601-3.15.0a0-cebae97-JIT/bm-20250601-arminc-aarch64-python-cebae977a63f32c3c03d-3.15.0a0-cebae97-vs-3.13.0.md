# Results vs. 3.13.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-aarch64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.448x faster
- HPT reliability: 99.67%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.11 sec: 1.05x slower                                                  |
| html5lib       | 65.6 ms                                                  | 61.9 ms: 1.06x faster                                                   |
| sphinx         | 1.20 sec                                                 | 1.16 sec: 1.03x faster                                                  |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 475 ms: 1.40x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 481 ms: 1.38x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 914 ms: 1.27x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 381 ms: 1.27x faster                                                    |
| async_tree_none            | 504 ms                                                   | 398 ms: 1.27x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 914 ms: 1.25x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 666 ms: 1.20x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 678 ms: 1.16x faster                                                    |
| async_generators           | 500 ms                                                   | 484 ms: 1.03x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.19x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 85.8 ms: 1.12x faster                                                   |
| Geometric mean | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.03 ms: 1.27x faster                                                   |
| regex_v8       | 32.5 ms                                                  | 27.7 ms: 1.18x faster                                                   |
| regex_dna      | 263 ms                                                   | 233 ms: 1.13x faster                                                    |
| Geometric mean | (ref)                                                    | 1.19x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads         | 2.67 sec                                                 | 2.35 sec: 1.14x faster                                                  |
| xml_etree_parse     | 203 ms                                                   | 186 ms: 1.09x faster                                                    |
| xml_etree_iterparse | 159 ms                                                   | 148 ms: 1.07x faster                                                    |
| xml_etree_generate  | 118 ms                                                   | 110 ms: 1.07x faster                                                    |
| json_dumps          | 14.2 ms                                                  | 13.3 ms: 1.07x faster                                                   |
| xml_etree_process   | 82.1 ms                                                  | 78.0 ms: 1.05x faster                                                   |
| Geometric mean      | (ref)                                                    | 1.06x faster                                                            |

Benchmark hidden because not significant (3): unpickle_pure_python, json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 15.0 ms: 1.07x faster                                                   |
| python_startup_no_site | 8.79 ms                                                  | 8.56 ms: 1.03x faster                                                   |
| Geometric mean         | (ref)                                                    | 1.05x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 14.0 ms                                                  | 13.1 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (3): genshi_text, django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pprint_pformat             | 1.99 sec                                                 | 1.91 us: 1039516.71x faster                                             |
| pprint_safe_repr           | 962 ms                                                   | 1.05 us: 914551.88x faster                                              |
| mdp                        | 3.45 sec                                                 | 1.69 sec: 2.04x faster                                                  |
| deepcopy                   | 479 us                                                   | 325 us: 1.47x faster                                                    |
| deepcopy_memo              | 53.0 us                                                  | 37.8 us: 1.40x faster                                                   |
| async_tree_memoization     | 664 ms                                                   | 475 ms: 1.40x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 481 ms: 1.38x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 914 ms: 1.27x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 381 ms: 1.27x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 4.03 ms: 1.27x faster                                                   |
| async_tree_none            | 504 ms                                                   | 398 ms: 1.27x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 914 ms: 1.25x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 666 ms: 1.20x faster                                                    |
| richards                   | 54.5 ms                                                  | 45.4 ms: 1.20x faster                                                   |
| regex_v8                   | 32.5 ms                                                  | 27.7 ms: 1.18x faster                                                   |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 678 ms: 1.16x faster                                                    |
| deepcopy_reduce            | 4.24 us                                                  | 3.65 us: 1.16x faster                                                   |
| richards_super             | 60.8 ms                                                  | 52.5 ms: 1.16x faster                                                   |
| telco                      | 10.5 ms                                                  | 9.15 ms: 1.14x faster                                                   |
| tomli_loads                | 2.67 sec                                                 | 2.35 sec: 1.14x faster                                                  |
| regex_dna                  | 263 ms                                                   | 233 ms: 1.13x faster                                                    |
| scimark_sor                | 164 ms                                                   | 147 ms: 1.12x faster                                                    |
| float                      | 95.8 ms                                                  | 85.8 ms: 1.12x faster                                                   |
| generators                 | 40.3 ms                                                  | 36.1 ms: 1.12x faster                                                   |
| bpe_tokeniser              | 6.02 sec                                                 | 5.40 sec: 1.11x faster                                                  |
| spectral_norm              | 143 ms                                                   | 130 ms: 1.10x faster                                                    |
| pyflate                    | 582 ms                                                   | 532 ms: 1.09x faster                                                    |
| scimark_fft                | 463 ms                                                   | 423 ms: 1.09x faster                                                    |
| sqlite_synth               | 4.08 us                                                  | 3.74 us: 1.09x faster                                                   |
| xml_etree_parse            | 203 ms                                                   | 186 ms: 1.09x faster                                                    |
| xml_etree_iterparse        | 159 ms                                                   | 148 ms: 1.07x faster                                                    |
| pylint                     | 345 ms                                                   | 323 ms: 1.07x faster                                                    |
| xml_etree_generate         | 118 ms                                                   | 110 ms: 1.07x faster                                                    |
| python_startup             | 16.0 ms                                                  | 15.0 ms: 1.07x faster                                                   |
| json_dumps                 | 14.2 ms                                                  | 13.3 ms: 1.07x faster                                                   |
| scimark_monte_carlo        | 87.8 ms                                                  | 82.3 ms: 1.07x faster                                                   |
| mako                       | 14.0 ms                                                  | 13.1 ms: 1.06x faster                                                   |
| html5lib                   | 65.6 ms                                                  | 61.9 ms: 1.06x faster                                                   |
| xml_etree_process          | 82.1 ms                                                  | 78.0 ms: 1.05x faster                                                   |
| k_core                     | 2.99 sec                                                 | 2.87 sec: 1.04x faster                                                  |
| async_generators           | 500 ms                                                   | 484 ms: 1.03x faster                                                    |
| go                         | 164 ms                                                   | 159 ms: 1.03x faster                                                    |
| sphinx                     | 1.20 sec                                                 | 1.16 sec: 1.03x faster                                                  |
| python_startup_no_site     | 8.79 ms                                                  | 8.56 ms: 1.03x faster                                                   |
| connected_components       | 547 ms                                                   | 557 ms: 1.02x slower                                                    |
| shortest_path              | 565 ms                                                   | 581 ms: 1.03x slower                                                    |
| pycparser                  | 1.34 sec                                                 | 1.39 sec: 1.03x slower                                                  |
| typing_runtime_protocols   | 197 us                                                   | 206 us: 1.04x slower                                                    |
| sympy_expand               | 472 ms                                                   | 494 ms: 1.05x slower                                                    |
| docutils                   | 2.96 sec                                                 | 3.11 sec: 1.05x slower                                                  |
| meteor_contest             | 117 ms                                                   | 125 ms: 1.07x slower                                                    |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.12 ms: 1.07x slower                                                   |
| raytrace                   | 310 ms                                                   | 332 ms: 1.07x slower                                                    |
| logging_simple             | 7.25 us                                                  | 7.77 us: 1.07x slower                                                   |
| sympy_str                  | 265 ms                                                   | 285 ms: 1.08x slower                                                    |
| crypto_pyaes               | 84.9 ms                                                  | 91.9 ms: 1.08x slower                                                   |
| comprehensions             | 20.8 us                                                  | 22.5 us: 1.08x slower                                                   |
| create_gc_cycles           | 3.39 ms                                                  | 3.77 ms: 1.11x slower                                                   |
| gc_traversal               | 5.92 ms                                                  | 6.85 ms: 1.16x slower                                                   |
| subparsers                 | 20.3 ms                                                  | 29.4 ms: 1.44x slower                                                   |
| many_optionals             | 626 us                                                   | 925 us: 1.48x slower                                                    |
| logging_silent             | 135 ns                                                   | 610 ns: 4.53x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.42x faster                                                            |

Benchmark hidden because not significant (25): pathlib, genshi_text, json, unpickle_pure_python, deltablue, json_loads, coverage, pidigits, djangocms, sympy_integrate, thrift, 2to3, asyncio_websockets, sympy_sum, chaos, nbody, coroutines, scimark_lu, nqueens, logging_format, django_template, hexiom, fannkuch, genshi_xml, pickle_pure_python
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, regex_compile, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.448x faster

# HPT report

- Reliability score: 99.67% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x