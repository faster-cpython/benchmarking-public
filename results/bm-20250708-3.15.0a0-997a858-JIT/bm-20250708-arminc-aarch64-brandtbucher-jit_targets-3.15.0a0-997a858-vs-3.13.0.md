# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_targets
- machine: linux-aarch64
- commit hash: 997a858
- commit date: 2025-07-08
- overall geometric mean: 1.015x faster
- HPT reliability: 97.77%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250708-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.09 sec: 1.04x slower                                               |
| html5lib       | 65.6 ms                                                  | 62.7 ms: 1.05x faster                                                |
| sphinx         | 1.20 sec                                                 | 1.16 sec: 1.03x faster                                               |
| Geometric mean | (ref)                                                    | 1.01x faster                                                         |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250708-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 474 ms: 1.40x faster                                                 |
| async_tree_memoization     | 664 ms                                                   | 480 ms: 1.38x faster                                                 |
| async_tree_none            | 504 ms                                                   | 388 ms: 1.30x faster                                                 |
| async_tree_io_tg           | 1.16 sec                                                 | 908 ms: 1.28x faster                                                 |
| async_tree_io              | 1.14 sec                                                 | 906 ms: 1.26x faster                                                 |
| async_tree_none_tg         | 484 ms                                                   | 388 ms: 1.25x faster                                                 |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 662 ms: 1.21x faster                                                 |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 674 ms: 1.17x faster                                                 |
| async_generators           | 500 ms                                                   | 489 ms: 1.02x faster                                                 |
| Geometric mean             | (ref)                                                    | 1.20x faster                                                         |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250708-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 82.3 ms: 1.16x faster                                                |
| nbody          | 118 ms                                                   | 128 ms: 1.08x slower                                                 |
| Geometric mean | (ref)                                                    | 1.02x faster                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250708-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.77 ms: 1.35x faster                                                |
| regex_v8       | 32.5 ms                                                  | 26.7 ms: 1.22x faster                                                |
| regex_dna      | 263 ms                                                   | 217 ms: 1.21x faster                                                 |
| regex_compile  | 134 ms                                                   | 124 ms: 1.08x faster                                                 |
| Geometric mean | (ref)                                                    | 1.21x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250708-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|---------------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads         | 2.67 sec                                                 | 2.34 sec: 1.14x faster                                               |
| xml_etree_parse     | 203 ms                                                   | 179 ms: 1.13x faster                                                 |
| xml_etree_generate  | 118 ms                                                   | 108 ms: 1.10x faster                                                 |
| xml_etree_iterparse | 159 ms                                                   | 146 ms: 1.09x faster                                                 |
| xml_etree_process   | 82.1 ms                                                  | 77.3 ms: 1.06x faster                                                |
| pickle_pure_python  | 374 us                                                   | 400 us: 1.07x slower                                                 |
| Geometric mean      | (ref)                                                    | 1.06x faster                                                         |

Benchmark hidden because not significant (3): unpickle_pure_python, json_dumps, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250708-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                                |
| python_startup_no_site | 8.79 ms                                                  | 8.61 ms: 1.02x faster                                                |
| Geometric mean         | (ref)                                                    | 1.04x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250708-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako           | 14.0 ms                                                  | 13.0 ms: 1.08x faster                                                |
| genshi_xml     | 61.6 ms                                                  | 63.3 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                    | 1.01x faster                                                         |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250708-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.66 sec: 2.07x faster                                               |
| deepcopy                   | 479 us                                                   | 326 us: 1.47x faster                                                 |
| async_tree_memoization_tg  | 663 ms                                                   | 474 ms: 1.40x faster                                                 |
| async_tree_memoization     | 664 ms                                                   | 480 ms: 1.38x faster                                                 |
| deepcopy_memo              | 53.0 us                                                  | 38.4 us: 1.38x faster                                                |
| regex_effbot               | 5.10 ms                                                  | 3.77 ms: 1.35x faster                                                |
| async_tree_none            | 504 ms                                                   | 388 ms: 1.30x faster                                                 |
| async_tree_io_tg           | 1.16 sec                                                 | 908 ms: 1.28x faster                                                 |
| async_tree_io              | 1.14 sec                                                 | 906 ms: 1.26x faster                                                 |
| async_tree_none_tg         | 484 ms                                                   | 388 ms: 1.25x faster                                                 |
| richards                   | 54.5 ms                                                  | 44.1 ms: 1.24x faster                                                |
| regex_v8                   | 32.5 ms                                                  | 26.7 ms: 1.22x faster                                                |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 662 ms: 1.21x faster                                                 |
| regex_dna                  | 263 ms                                                   | 217 ms: 1.21x faster                                                 |
| spectral_norm              | 143 ms                                                   | 121 ms: 1.19x faster                                                 |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 674 ms: 1.17x faster                                                 |
| richards_super             | 60.8 ms                                                  | 52.0 ms: 1.17x faster                                                |
| float                      | 95.8 ms                                                  | 82.3 ms: 1.16x faster                                                |
| tomli_loads                | 2.67 sec                                                 | 2.34 sec: 1.14x faster                                               |
| scimark_sor                | 164 ms                                                   | 144 ms: 1.14x faster                                                 |
| xml_etree_parse            | 203 ms                                                   | 179 ms: 1.13x faster                                                 |
| deepcopy_reduce            | 4.24 us                                                  | 3.75 us: 1.13x faster                                                |
| scimark_fft                | 463 ms                                                   | 411 ms: 1.13x faster                                                 |
| generators                 | 40.3 ms                                                  | 35.8 ms: 1.13x faster                                                |
| bpe_tokeniser              | 6.02 sec                                                 | 5.43 sec: 1.11x faster                                               |
| pyflate                    | 582 ms                                                   | 526 ms: 1.11x faster                                                 |
| sqlite_synth               | 4.08 us                                                  | 3.70 us: 1.10x faster                                                |
| xml_etree_generate         | 118 ms                                                   | 108 ms: 1.10x faster                                                 |
| xml_etree_iterparse        | 159 ms                                                   | 146 ms: 1.09x faster                                                 |
| regex_compile              | 134 ms                                                   | 124 ms: 1.08x faster                                                 |
| scimark_monte_carlo        | 87.8 ms                                                  | 81.3 ms: 1.08x faster                                                |
| mako                       | 14.0 ms                                                  | 13.0 ms: 1.08x faster                                                |
| go                         | 164 ms                                                   | 154 ms: 1.07x faster                                                 |
| pylint                     | 345 ms                                                   | 323 ms: 1.07x faster                                                 |
| logging_format             | 8.10 us                                                  | 7.60 us: 1.07x faster                                                |
| python_startup             | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                                |
| xml_etree_process          | 82.1 ms                                                  | 77.3 ms: 1.06x faster                                                |
| html5lib                   | 65.6 ms                                                  | 62.7 ms: 1.05x faster                                                |
| nqueens                    | 105 ms                                                   | 101 ms: 1.04x faster                                                 |
| k_core                     | 2.99 sec                                                 | 2.89 sec: 1.03x faster                                               |
| sphinx                     | 1.20 sec                                                 | 1.16 sec: 1.03x faster                                               |
| async_generators           | 500 ms                                                   | 489 ms: 1.02x faster                                                 |
| python_startup_no_site     | 8.79 ms                                                  | 8.61 ms: 1.02x faster                                                |
| djangocms                  | 66.2 us                                                  | 65.0 us: 1.02x faster                                                |
| genshi_xml                 | 61.6 ms                                                  | 63.3 ms: 1.03x slower                                                |
| sympy_str                  | 265 ms                                                   | 275 ms: 1.04x slower                                                 |
| comprehensions             | 20.8 us                                                  | 21.6 us: 1.04x slower                                                |
| sympy_expand               | 472 ms                                                   | 491 ms: 1.04x slower                                                 |
| docutils                   | 2.96 sec                                                 | 3.09 sec: 1.04x slower                                               |
| connected_components       | 547 ms                                                   | 569 ms: 1.04x slower                                                 |
| typing_runtime_protocols   | 197 us                                                   | 207 us: 1.05x slower                                                 |
| raytrace                   | 310 ms                                                   | 328 ms: 1.06x slower                                                 |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.06 ms: 1.06x slower                                                |
| shortest_path              | 565 ms                                                   | 605 ms: 1.07x slower                                                 |
| pickle_pure_python         | 374 us                                                   | 400 us: 1.07x slower                                                 |
| nbody                      | 118 ms                                                   | 128 ms: 1.08x slower                                                 |
| crypto_pyaes               | 84.9 ms                                                  | 94.1 ms: 1.11x slower                                                |
| pprint_pformat             | 1.99 sec                                                 | 2.29 sec: 1.15x slower                                               |
| create_gc_cycles           | 3.39 ms                                                  | 3.93 ms: 1.16x slower                                                |
| gc_traversal               | 5.92 ms                                                  | 6.91 ms: 1.17x slower                                                |
| pprint_safe_repr           | 962 ms                                                   | 1.15 sec: 1.20x slower                                               |
| many_optionals             | 626 us                                                   | 812 us: 1.30x slower                                                 |
| subparsers                 | 20.3 ms                                                  | 29.0 ms: 1.43x slower                                                |
| telco                      | 10.5 ms                                                  | 167 ms: 15.99x slower                                                |
| Geometric mean             | (ref)                                                    | 1.03x faster                                                         |

Benchmark hidden because not significant (24): unpickle_pure_python, json_dumps, pathlib, thrift, genshi_text, logging_simple, chaos, sympy_sum, deltablue, sympy_integrate, meteor_contest, logging_silent, coverage, asyncio_websockets, json, 2to3, coroutines, fannkuch, pycparser, json_loads, pidigits, scimark_lu, hexiom, django_template
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250708-3.15.0a0-997a858-JIT/bm-20250708-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-997a858.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.015x faster

# HPT report

- Reliability score: 97.77% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x