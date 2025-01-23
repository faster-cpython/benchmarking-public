# Results vs. 3.13.0

- fork: mdboom
- ref: aa_test_2025_2
- machine: linux-aarch64
- commit hash: 8ffb2c1
- commit date: 2025-01-23
- overall geometric mean: 1.041x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.04 sec: 1.03x slower                                             |
| Geometric mean | (ref)                                                    | 1.00x slower                                                       |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 474 ms: 1.40x faster                                               |
| async_tree_memoization     | 664 ms                                                   | 490 ms: 1.35x faster                                               |
| async_tree_none            | 504 ms                                                   | 377 ms: 1.34x faster                                               |
| async_tree_io_tg           | 1.16 sec                                                 | 897 ms: 1.30x faster                                               |
| async_tree_none_tg         | 484 ms                                                   | 380 ms: 1.27x faster                                               |
| async_tree_io              | 1.14 sec                                                 | 897 ms: 1.27x faster                                               |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 664 ms: 1.21x faster                                               |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 681 ms: 1.16x faster                                               |
| async_generators           | 500 ms                                                   | 447 ms: 1.12x faster                                               |
| Geometric mean             | (ref)                                                    | 1.21x faster                                                       |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 85.0 ms: 1.13x faster                                              |
| Geometric mean | (ref)                                                    | 1.04x faster                                                       |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.03 ms: 1.27x faster                                              |
| Geometric mean | (ref)                                                    | 1.06x faster                                                       |

Benchmark hidden because not significant (3): regex_compile, regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------:|
| xml_etree_parse      | 203 ms                                                   | 180 ms: 1.12x faster                                               |
| xml_etree_iterparse  | 159 ms                                                   | 143 ms: 1.11x faster                                               |
| xml_etree_generate   | 118 ms                                                   | 112 ms: 1.06x faster                                               |
| tomli_loads          | 2.67 sec                                                 | 2.60 sec: 1.03x faster                                             |
| pickle_pure_python   | 374 us                                                   | 404 us: 1.08x slower                                               |
| unpickle_pure_python | 265 us                                                   | 290 us: 1.09x slower                                               |
| Geometric mean       | (ref)                                                    | 1.01x faster                                                       |

Benchmark hidden because not significant (3): json_loads, xml_etree_process, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 9.05 ms: 1.03x slower                                              |
| Geometric mean         | (ref)                                                    | 1.03x slower                                                       |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml      | 61.6 ms                                                  | 64.1 ms: 1.04x slower                                              |
| django_template | 39.4 ms                                                  | 42.8 ms: 1.09x slower                                              |
| Geometric mean  | (ref)                                                    | 1.05x slower                                                       |

Benchmark hidden because not significant (2): mako, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 474 ms: 1.40x faster                                               |
| deepcopy                   | 479 us                                                   | 351 us: 1.37x faster                                               |
| async_tree_memoization     | 664 ms                                                   | 490 ms: 1.35x faster                                               |
| async_tree_none            | 504 ms                                                   | 377 ms: 1.34x faster                                               |
| async_tree_io_tg           | 1.16 sec                                                 | 897 ms: 1.30x faster                                               |
| deepcopy_memo              | 53.0 us                                                  | 40.8 us: 1.30x faster                                              |
| async_tree_none_tg         | 484 ms                                                   | 380 ms: 1.27x faster                                               |
| async_tree_io              | 1.14 sec                                                 | 897 ms: 1.27x faster                                               |
| regex_effbot               | 5.10 ms                                                  | 4.03 ms: 1.27x faster                                              |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 664 ms: 1.21x faster                                               |
| spectral_norm              | 143 ms                                                   | 122 ms: 1.18x faster                                               |
| go                         | 164 ms                                                   | 141 ms: 1.17x faster                                               |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 681 ms: 1.16x faster                                               |
| deepcopy_reduce            | 4.24 us                                                  | 3.72 us: 1.14x faster                                              |
| float                      | 95.8 ms                                                  | 85.0 ms: 1.13x faster                                              |
| pylint                     | 345 ms                                                   | 307 ms: 1.12x faster                                               |
| xml_etree_parse            | 203 ms                                                   | 180 ms: 1.12x faster                                               |
| async_generators           | 500 ms                                                   | 447 ms: 1.12x faster                                               |
| xml_etree_iterparse        | 159 ms                                                   | 143 ms: 1.11x faster                                               |
| scimark_fft                | 463 ms                                                   | 424 ms: 1.09x faster                                               |
| telco                      | 10.5 ms                                                  | 9.60 ms: 1.09x faster                                              |
| pathlib                    | 24.3 ms                                                  | 22.4 ms: 1.09x faster                                              |
| generators                 | 40.3 ms                                                  | 37.3 ms: 1.08x faster                                              |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 6.23 ms: 1.07x faster                                              |
| thrift                     | 1.01 ms                                                  | 948 us: 1.07x faster                                               |
| richards                   | 54.5 ms                                                  | 51.2 ms: 1.06x faster                                              |
| scimark_lu                 | 146 ms                                                   | 137 ms: 1.06x faster                                               |
| coverage                   | 106 ms                                                   | 99.5 ms: 1.06x faster                                              |
| xml_etree_generate         | 118 ms                                                   | 112 ms: 1.06x faster                                               |
| bpe_tokeniser              | 6.02 sec                                                 | 5.71 sec: 1.05x faster                                             |
| scimark_sor                | 164 ms                                                   | 156 ms: 1.05x faster                                               |
| k_core                     | 2.99 sec                                                 | 2.86 sec: 1.05x faster                                             |
| pycparser                  | 1.34 sec                                                 | 1.29 sec: 1.04x faster                                             |
| richards_super             | 60.8 ms                                                  | 58.3 ms: 1.04x faster                                              |
| tomli_loads                | 2.67 sec                                                 | 2.60 sec: 1.03x faster                                             |
| docutils                   | 2.96 sec                                                 | 3.04 sec: 1.03x slower                                             |
| python_startup_no_site     | 8.79 ms                                                  | 9.05 ms: 1.03x slower                                              |
| genshi_xml                 | 61.6 ms                                                  | 64.1 ms: 1.04x slower                                              |
| typing_runtime_protocols   | 197 us                                                   | 207 us: 1.05x slower                                               |
| pickle_pure_python         | 374 us                                                   | 404 us: 1.08x slower                                               |
| django_template            | 39.4 ms                                                  | 42.8 ms: 1.09x slower                                              |
| unpickle_pure_python       | 265 us                                                   | 290 us: 1.09x slower                                               |
| create_gc_cycles           | 3.39 ms                                                  | 3.76 ms: 1.11x slower                                              |
| many_optionals             | 626 us                                                   | 713 us: 1.14x slower                                               |
| gc_traversal               | 5.92 ms                                                  | 7.01 ms: 1.18x slower                                              |
| subparsers                 | 20.3 ms                                                  | 27.1 ms: 1.33x slower                                              |
| bench_mp_pool              | 8.07 ms                                                  | 6.60 sec: 817.63x slower                                           |
| Geometric mean             | (ref)                                                    | 1.03x slower                                                       |

Benchmark hidden because not significant (48): sympy_sum, sqlglot_transpile, scimark_monte_carlo, nqueens, chaos, sqlalchemy_declarative, regex_compile, sphinx, html5lib, nbody, sqlglot_optimize, json_loads, coroutines, json, crypto_pyaes, sqlalchemy_imperative, sympy_integrate, meteor_contest, shortest_path, regex_dna, bench_thread_pool, fannkuch, sympy_str, pidigits, pprint_pformat, sympy_expand, asyncio_websockets, regex_v8, connected_components, logging_format, mdp, pyflate, sqlite_synth, pprint_safe_repr, hexiom, 2to3, raytrace, logging_silent, sqlglot_parse, deltablue, python_startup, sqlglot_normalize, mako, genshi_text, comprehensions, xml_etree_process, json_dumps, logging_simple
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20250123-3.14.0a4+-8ffb2c1/bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1.json: dulwich_log

- Geometric mean (including insignificant results): 1.041x faster

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x