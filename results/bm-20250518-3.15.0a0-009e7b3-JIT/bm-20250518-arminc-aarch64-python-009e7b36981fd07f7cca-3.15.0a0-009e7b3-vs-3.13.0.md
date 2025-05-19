# Results vs. 3.13.0

- fork: python
- ref: 009e7b36981fd07f7cca
- machine: linux-aarch64
- commit hash: 009e7b3
- commit date: 2025-05-18
- overall geometric mean: 1.045x slower
- HPT reliability: 83.74%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.09 sec: 1.04x slower                                                  |
| html5lib       | 65.6 ms                                                  | 61.0 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 479 ms: 1.38x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 489 ms: 1.36x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 386 ms: 1.26x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 928 ms: 1.26x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 908 ms: 1.25x faster                                                    |
| async_tree_none            | 504 ms                                                   | 411 ms: 1.22x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 667 ms: 1.20x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 675 ms: 1.17x faster                                                    |
| async_generators           | 500 ms                                                   | 485 ms: 1.03x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.19x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 84.8 ms: 1.13x faster                                                   |
| Geometric mean | (ref)                                                    | 1.05x faster                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.84 ms: 1.33x faster                                                   |
| regex_v8       | 32.5 ms                                                  | 28.3 ms: 1.15x faster                                                   |
| regex_dna      | 263 ms                                                   | 238 ms: 1.10x faster                                                    |
| regex_compile  | 134 ms                                                   | 126 ms: 1.06x faster                                                    |
| Geometric mean | (ref)                                                    | 1.16x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads         | 2.67 sec                                                 | 2.35 sec: 1.13x faster                                                  |
| xml_etree_parse     | 203 ms                                                   | 182 ms: 1.11x faster                                                    |
| xml_etree_iterparse | 159 ms                                                   | 143 ms: 1.11x faster                                                    |
| json_dumps          | 14.2 ms                                                  | 13.3 ms: 1.07x faster                                                   |
| xml_etree_process   | 82.1 ms                                                  | 77.8 ms: 1.06x faster                                                   |
| pickle_pure_python  | 374 us                                                   | 396 us: 1.06x slower                                                    |
| json_loads          | 32.8 us                                                  | 35.3 us: 1.08x slower                                                   |
| Geometric mean      | (ref)                                                    | 1.05x faster                                                            |

Benchmark hidden because not significant (2): xml_etree_generate, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 16.0 ms                                                  | 15.3 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 14.0 ms                                                  | 13.5 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (3): genshi_text, django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.68 sec: 2.05x faster                                                  |
| deepcopy                   | 479 us                                                   | 333 us: 1.44x faster                                                    |
| deepcopy_memo              | 53.0 us                                                  | 37.5 us: 1.41x faster                                                   |
| async_tree_memoization_tg  | 663 ms                                                   | 479 ms: 1.38x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 489 ms: 1.36x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 3.84 ms: 1.33x faster                                                   |
| async_tree_none_tg         | 484 ms                                                   | 386 ms: 1.26x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 928 ms: 1.26x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 908 ms: 1.25x faster                                                    |
| async_tree_none            | 504 ms                                                   | 411 ms: 1.22x faster                                                    |
| deepcopy_reduce            | 4.24 us                                                  | 3.52 us: 1.21x faster                                                   |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 667 ms: 1.20x faster                                                    |
| richards_super             | 60.8 ms                                                  | 51.9 ms: 1.17x faster                                                   |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 675 ms: 1.17x faster                                                    |
| richards                   | 54.5 ms                                                  | 47.2 ms: 1.16x faster                                                   |
| regex_v8                   | 32.5 ms                                                  | 28.3 ms: 1.15x faster                                                   |
| tomli_loads                | 2.67 sec                                                 | 2.35 sec: 1.13x faster                                                  |
| float                      | 95.8 ms                                                  | 84.8 ms: 1.13x faster                                                   |
| scimark_sor                | 164 ms                                                   | 147 ms: 1.12x faster                                                    |
| xml_etree_parse            | 203 ms                                                   | 182 ms: 1.11x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.42 sec: 1.11x faster                                                  |
| xml_etree_iterparse        | 159 ms                                                   | 143 ms: 1.11x faster                                                    |
| regex_dna                  | 263 ms                                                   | 238 ms: 1.10x faster                                                    |
| generators                 | 40.3 ms                                                  | 36.8 ms: 1.10x faster                                                   |
| spectral_norm              | 143 ms                                                   | 131 ms: 1.09x faster                                                    |
| telco                      | 10.5 ms                                                  | 9.60 ms: 1.09x faster                                                   |
| sqlite_synth               | 4.08 us                                                  | 3.77 us: 1.08x faster                                                   |
| scimark_fft                | 463 ms                                                   | 430 ms: 1.08x faster                                                    |
| html5lib                   | 65.6 ms                                                  | 61.0 ms: 1.07x faster                                                   |
| json_dumps                 | 14.2 ms                                                  | 13.3 ms: 1.07x faster                                                   |
| regex_compile              | 134 ms                                                   | 126 ms: 1.06x faster                                                    |
| pyflate                    | 582 ms                                                   | 548 ms: 1.06x faster                                                    |
| xml_etree_process          | 82.1 ms                                                  | 77.8 ms: 1.06x faster                                                   |
| python_startup             | 16.0 ms                                                  | 15.3 ms: 1.05x faster                                                   |
| k_core                     | 2.99 sec                                                 | 2.87 sec: 1.04x faster                                                  |
| mako                       | 14.0 ms                                                  | 13.5 ms: 1.04x faster                                                   |
| async_generators           | 500 ms                                                   | 485 ms: 1.03x faster                                                    |
| sympy_str                  | 265 ms                                                   | 269 ms: 1.02x slower                                                    |
| connected_components       | 547 ms                                                   | 559 ms: 1.02x slower                                                    |
| pycparser                  | 1.34 sec                                                 | 1.39 sec: 1.03x slower                                                  |
| shortest_path              | 565 ms                                                   | 588 ms: 1.04x slower                                                    |
| docutils                   | 2.96 sec                                                 | 3.09 sec: 1.04x slower                                                  |
| bench_thread_pool          | 1.34 ms                                                  | 1.40 ms: 1.05x slower                                                   |
| logging_simple             | 7.25 us                                                  | 7.63 us: 1.05x slower                                                   |
| pickle_pure_python         | 374 us                                                   | 396 us: 1.06x slower                                                    |
| typing_runtime_protocols   | 197 us                                                   | 209 us: 1.06x slower                                                    |
| hexiom                     | 7.34 ms                                                  | 7.90 ms: 1.08x slower                                                   |
| raytrace                   | 310 ms                                                   | 334 ms: 1.08x slower                                                    |
| json_loads                 | 32.8 us                                                  | 35.3 us: 1.08x slower                                                   |
| create_gc_cycles           | 3.39 ms                                                  | 3.76 ms: 1.11x slower                                                   |
| crypto_pyaes               | 84.9 ms                                                  | 94.4 ms: 1.11x slower                                                   |
| comprehensions             | 20.8 us                                                  | 23.6 us: 1.13x slower                                                   |
| gc_traversal               | 5.92 ms                                                  | 6.85 ms: 1.16x slower                                                   |
| pprint_safe_repr           | 962 ms                                                   | 1.14 sec: 1.18x slower                                                  |
| pprint_pformat             | 1.99 sec                                                 | 2.35 sec: 1.18x slower                                                  |
| subparsers                 | 20.3 ms                                                  | 29.3 ms: 1.44x slower                                                   |
| many_optionals             | 626 us                                                   | 940 us: 1.50x slower                                                    |
| logging_silent             | 135 ns                                                   | 626 ns: 4.65x slower                                                    |
| coverage                   | 106 ms                                                   | 548 ms: 5.19x slower                                                    |
| thrift                     | 1.01 ms                                                  | 194 ms: 191.64x slower                                                  |
| bench_mp_pool              | 8.07 ms                                                  | 3.94 sec: 488.74x slower                                                |
| Geometric mean             | (ref)                                                    | 1.13x slower                                                            |

Benchmark hidden because not significant (28): xml_etree_generate, pathlib, genshi_text, pylint, deltablue, unpickle_pure_python, sympy_integrate, pidigits, sphinx, nbody, asyncio_websockets, scimark_monte_carlo, python_startup_no_site, sympy_sum, chaos, nqueens, django_template, 2to3, scimark_lu, json, sympy_expand, coroutines, genshi_xml, go, meteor_contest, scimark_sparse_mat_mult, fannkuch, logging_format
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250518-3.15.0a0-009e7b3-JIT/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.045x slower

# HPT report

- Reliability score: 83.74% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x