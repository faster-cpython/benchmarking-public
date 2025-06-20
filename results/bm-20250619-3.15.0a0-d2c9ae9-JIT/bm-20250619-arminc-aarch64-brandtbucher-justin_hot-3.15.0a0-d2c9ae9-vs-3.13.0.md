# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_hot
- machine: linux-aarch64
- commit hash: d2c9ae9
- commit date: 2025-06-19
- overall geometric mean: 1.004x faster
- HPT reliability: 51.29%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.15 sec: 1.06x slower                                              |
| html5lib       | 65.6 ms                                                  | 63.2 ms: 1.04x faster                                               |
| sphinx         | 1.20 sec                                                 | 1.16 sec: 1.04x faster                                              |
| Geometric mean | (ref)                                                    | 1.00x slower                                                        |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 473 ms: 1.40x faster                                                |
| async_tree_memoization_tg  | 663 ms                                                   | 473 ms: 1.40x faster                                                |
| async_tree_none_tg         | 484 ms                                                   | 379 ms: 1.28x faster                                                |
| async_tree_io_tg           | 1.16 sec                                                 | 918 ms: 1.27x faster                                                |
| async_tree_io              | 1.14 sec                                                 | 900 ms: 1.27x faster                                                |
| async_tree_none            | 504 ms                                                   | 403 ms: 1.25x faster                                                |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 665 ms: 1.20x faster                                                |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 665 ms: 1.19x faster                                                |
| async_generators           | 500 ms                                                   | 479 ms: 1.05x faster                                                |
| Geometric mean             | (ref)                                                    | 1.20x faster                                                        |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 88.6 ms: 1.08x faster                                               |
| nbody          | 118 ms                                                   | 147 ms: 1.24x slower                                                |
| Geometric mean | (ref)                                                    | 1.04x slower                                                        |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.94 ms: 1.30x faster                                               |
| regex_v8       | 32.5 ms                                                  | 26.9 ms: 1.21x faster                                               |
| regex_dna      | 263 ms                                                   | 223 ms: 1.18x faster                                                |
| Geometric mean | (ref)                                                    | 1.17x faster                                                        |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_parse      | 203 ms                                                   | 180 ms: 1.12x faster                                                |
| xml_etree_iterparse  | 159 ms                                                   | 144 ms: 1.11x faster                                                |
| tomli_loads          | 2.67 sec                                                 | 2.55 sec: 1.04x faster                                              |
| pickle_pure_python   | 374 us                                                   | 404 us: 1.08x slower                                                |
| unpickle_pure_python | 265 us                                                   | 295 us: 1.11x slower                                                |
| Geometric mean       | (ref)                                                    | 1.02x faster                                                        |

Benchmark hidden because not significant (4): xml_etree_generate, json_dumps, xml_etree_process, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 15.0 ms: 1.07x faster                                               |
| python_startup_no_site | 8.79 ms                                                  | 8.60 ms: 1.02x faster                                               |
| Geometric mean         | (ref)                                                    | 1.05x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml     | 61.6 ms                                                  | 64.2 ms: 1.04x slower                                               |
| mako           | 14.0 ms                                                  | 15.1 ms: 1.08x slower                                               |
| Geometric mean | (ref)                                                    | 1.02x slower                                                        |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.72 sec: 2.00x faster                                              |
| deepcopy                   | 479 us                                                   | 331 us: 1.45x faster                                                |
| deepcopy_memo              | 53.0 us                                                  | 37.2 us: 1.43x faster                                               |
| async_tree_memoization     | 664 ms                                                   | 473 ms: 1.40x faster                                                |
| async_tree_memoization_tg  | 663 ms                                                   | 473 ms: 1.40x faster                                                |
| regex_effbot               | 5.10 ms                                                  | 3.94 ms: 1.30x faster                                               |
| async_tree_none_tg         | 484 ms                                                   | 379 ms: 1.28x faster                                                |
| async_tree_io_tg           | 1.16 sec                                                 | 918 ms: 1.27x faster                                                |
| async_tree_io              | 1.14 sec                                                 | 900 ms: 1.27x faster                                                |
| async_tree_none            | 504 ms                                                   | 403 ms: 1.25x faster                                                |
| regex_v8                   | 32.5 ms                                                  | 26.9 ms: 1.21x faster                                               |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 665 ms: 1.20x faster                                                |
| deepcopy_reduce            | 4.24 us                                                  | 3.56 us: 1.19x faster                                               |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 665 ms: 1.19x faster                                                |
| regex_dna                  | 263 ms                                                   | 223 ms: 1.18x faster                                                |
| xml_etree_parse            | 203 ms                                                   | 180 ms: 1.12x faster                                                |
| scimark_sor                | 164 ms                                                   | 147 ms: 1.12x faster                                                |
| generators                 | 40.3 ms                                                  | 36.4 ms: 1.11x faster                                               |
| xml_etree_iterparse        | 159 ms                                                   | 144 ms: 1.11x faster                                                |
| richards_super             | 60.8 ms                                                  | 55.7 ms: 1.09x faster                                               |
| sqlite_synth               | 4.08 us                                                  | 3.77 us: 1.08x faster                                               |
| float                      | 95.8 ms                                                  | 88.6 ms: 1.08x faster                                               |
| thrift                     | 1.01 ms                                                  | 940 us: 1.07x faster                                                |
| python_startup             | 16.0 ms                                                  | 15.0 ms: 1.07x faster                                               |
| coverage                   | 106 ms                                                   | 101 ms: 1.05x faster                                                |
| richards                   | 54.5 ms                                                  | 52.1 ms: 1.05x faster                                               |
| async_generators           | 500 ms                                                   | 479 ms: 1.05x faster                                                |
| tomli_loads                | 2.67 sec                                                 | 2.55 sec: 1.04x faster                                              |
| html5lib                   | 65.6 ms                                                  | 63.2 ms: 1.04x faster                                               |
| sphinx                     | 1.20 sec                                                 | 1.16 sec: 1.04x faster                                              |
| bpe_tokeniser              | 6.02 sec                                                 | 5.82 sec: 1.03x faster                                              |
| python_startup_no_site     | 8.79 ms                                                  | 8.60 ms: 1.02x faster                                               |
| k_core                     | 2.99 sec                                                 | 2.93 sec: 1.02x faster                                              |
| djangocms                  | 66.2 us                                                  | 65.0 us: 1.02x faster                                               |
| pyflate                    | 582 ms                                                   | 606 ms: 1.04x slower                                                |
| genshi_xml                 | 61.6 ms                                                  | 64.2 ms: 1.04x slower                                               |
| sympy_expand               | 472 ms                                                   | 493 ms: 1.04x slower                                                |
| shortest_path              | 565 ms                                                   | 598 ms: 1.06x slower                                                |
| spectral_norm              | 143 ms                                                   | 152 ms: 1.06x slower                                                |
| docutils                   | 2.96 sec                                                 | 3.15 sec: 1.06x slower                                              |
| sympy_str                  | 265 ms                                                   | 282 ms: 1.06x slower                                                |
| connected_components       | 547 ms                                                   | 583 ms: 1.07x slower                                                |
| typing_runtime_protocols   | 197 us                                                   | 210 us: 1.07x slower                                                |
| pickle_pure_python         | 374 us                                                   | 404 us: 1.08x slower                                                |
| mako                       | 14.0 ms                                                  | 15.1 ms: 1.08x slower                                               |
| pycparser                  | 1.34 sec                                                 | 1.46 sec: 1.08x slower                                              |
| meteor_contest             | 117 ms                                                   | 127 ms: 1.09x slower                                                |
| raytrace                   | 310 ms                                                   | 343 ms: 1.11x slower                                                |
| create_gc_cycles           | 3.39 ms                                                  | 3.78 ms: 1.11x slower                                               |
| unpickle_pure_python       | 265 us                                                   | 295 us: 1.11x slower                                                |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.46 ms: 1.12x slower                                               |
| deltablue                  | 3.97 ms                                                  | 4.57 ms: 1.15x slower                                               |
| fannkuch                   | 478 ms                                                   | 557 ms: 1.17x slower                                                |
| go                         | 164 ms                                                   | 193 ms: 1.18x slower                                                |
| gc_traversal               | 5.92 ms                                                  | 7.06 ms: 1.19x slower                                               |
| crypto_pyaes               | 84.9 ms                                                  | 102 ms: 1.21x slower                                                |
| comprehensions             | 20.8 us                                                  | 25.1 us: 1.21x slower                                               |
| hexiom                     | 7.34 ms                                                  | 8.91 ms: 1.21x slower                                               |
| nbody                      | 118 ms                                                   | 147 ms: 1.24x slower                                                |
| many_optionals             | 626 us                                                   | 824 us: 1.31x slower                                                |
| subparsers                 | 20.3 ms                                                  | 28.4 ms: 1.40x slower                                               |
| pprint_safe_repr           | 962 ms                                                   | 1.54 sec: 1.60x slower                                              |
| pprint_pformat             | 1.99 sec                                                 | 3.25 sec: 1.64x slower                                              |
| logging_silent             | 135 ns                                                   | 609 ns: 4.52x slower                                                |
| Geometric mean             | (ref)                                                    | 1.00x slower                                                        |

Benchmark hidden because not significant (24): pathlib, genshi_text, xml_etree_generate, pylint, telco, json, json_dumps, regex_compile, sympy_integrate, sympy_sum, xml_etree_process, json_loads, chaos, asyncio_websockets, scimark_monte_carlo, django_template, pidigits, scimark_fft, nqueens, 2to3, coroutines, logging_format, logging_simple, scimark_lu
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250619-3.15.0a0-d2c9ae9-JIT/bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.004x faster

# HPT report

- Reliability score: 51.29% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x