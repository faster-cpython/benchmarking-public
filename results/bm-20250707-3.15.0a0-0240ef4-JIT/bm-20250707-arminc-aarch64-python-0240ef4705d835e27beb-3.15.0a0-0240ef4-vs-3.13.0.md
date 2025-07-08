# Results vs. 3.13.0

- fork: python
- ref: 0240ef4705d835e27beb
- machine: linux-aarch64
- commit hash: 0240ef4
- commit date: 2025-07-07
- overall geometric mean: 1.016x faster
- HPT reliability: 98.48%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.11 sec: 1.05x slower                                                  |
| sphinx         | 1.20 sec                                                 | 1.15 sec: 1.04x faster                                                  |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 476 ms: 1.39x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 478 ms: 1.38x faster                                                    |
| async_tree_none            | 504 ms                                                   | 383 ms: 1.31x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 902 ms: 1.29x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 385 ms: 1.26x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 905 ms: 1.26x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 655 ms: 1.22x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 667 ms: 1.18x faster                                                    |
| async_generators           | 500 ms                                                   | 481 ms: 1.04x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.20x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 82.4 ms: 1.16x faster                                                   |
| nbody          | 118 ms                                                   | 127 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.75 ms: 1.36x faster                                                   |
| regex_v8       | 32.5 ms                                                  | 26.6 ms: 1.22x faster                                                   |
| regex_dna      | 263 ms                                                   | 218 ms: 1.21x faster                                                    |
| regex_compile  | 134 ms                                                   | 123 ms: 1.09x faster                                                    |
| Geometric mean | (ref)                                                    | 1.22x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads         | 2.67 sec                                                 | 2.31 sec: 1.15x faster                                                  |
| xml_etree_parse     | 203 ms                                                   | 178 ms: 1.14x faster                                                    |
| xml_etree_iterparse | 159 ms                                                   | 145 ms: 1.09x faster                                                    |
| xml_etree_process   | 82.1 ms                                                  | 77.9 ms: 1.05x faster                                                   |
| pickle_pure_python  | 374 us                                                   | 400 us: 1.07x slower                                                    |
| Geometric mean      | (ref)                                                    | 1.06x faster                                                            |

Benchmark hidden because not significant (4): unpickle_pure_python, xml_etree_generate, json_dumps, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 15.0 ms: 1.07x faster                                                   |
| python_startup_no_site | 8.79 ms                                                  | 8.60 ms: 1.02x faster                                                   |
| Geometric mean         | (ref)                                                    | 1.05x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 14.0 ms                                                  | 13.1 ms: 1.07x faster                                                   |
| genshi_text    | 28.6 ms                                                  | 27.1 ms: 1.05x faster                                                   |
| genshi_xml     | 61.6 ms                                                  | 63.2 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.69 sec: 2.04x faster                                                  |
| deepcopy                   | 479 us                                                   | 330 us: 1.45x faster                                                    |
| deepcopy_memo              | 53.0 us                                                  | 36.7 us: 1.44x faster                                                   |
| async_tree_memoization     | 664 ms                                                   | 476 ms: 1.39x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 478 ms: 1.38x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 3.75 ms: 1.36x faster                                                   |
| async_tree_none            | 504 ms                                                   | 383 ms: 1.31x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 902 ms: 1.29x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 385 ms: 1.26x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 905 ms: 1.26x faster                                                    |
| regex_v8                   | 32.5 ms                                                  | 26.6 ms: 1.22x faster                                                   |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 655 ms: 1.22x faster                                                    |
| regex_dna                  | 263 ms                                                   | 218 ms: 1.21x faster                                                    |
| richards_super             | 60.8 ms                                                  | 50.4 ms: 1.21x faster                                                   |
| richards                   | 54.5 ms                                                  | 45.6 ms: 1.19x faster                                                   |
| spectral_norm              | 143 ms                                                   | 120 ms: 1.19x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 667 ms: 1.18x faster                                                    |
| deepcopy_reduce            | 4.24 us                                                  | 3.60 us: 1.18x faster                                                   |
| float                      | 95.8 ms                                                  | 82.4 ms: 1.16x faster                                                   |
| scimark_sor                | 164 ms                                                   | 142 ms: 1.16x faster                                                    |
| tomli_loads                | 2.67 sec                                                 | 2.31 sec: 1.15x faster                                                  |
| xml_etree_parse            | 203 ms                                                   | 178 ms: 1.14x faster                                                    |
| scimark_fft                | 463 ms                                                   | 409 ms: 1.13x faster                                                    |
| generators                 | 40.3 ms                                                  | 35.7 ms: 1.13x faster                                                   |
| bpe_tokeniser              | 6.02 sec                                                 | 5.40 sec: 1.11x faster                                                  |
| pyflate                    | 582 ms                                                   | 525 ms: 1.11x faster                                                    |
| xml_etree_iterparse        | 159 ms                                                   | 145 ms: 1.09x faster                                                    |
| sqlite_synth               | 4.08 us                                                  | 3.74 us: 1.09x faster                                                   |
| pathlib                    | 24.3 ms                                                  | 22.3 ms: 1.09x faster                                                   |
| regex_compile              | 134 ms                                                   | 123 ms: 1.09x faster                                                    |
| scimark_monte_carlo        | 87.8 ms                                                  | 80.7 ms: 1.09x faster                                                   |
| mako                       | 14.0 ms                                                  | 13.1 ms: 1.07x faster                                                   |
| python_startup             | 16.0 ms                                                  | 15.0 ms: 1.07x faster                                                   |
| genshi_text                | 28.6 ms                                                  | 27.1 ms: 1.05x faster                                                   |
| xml_etree_process          | 82.1 ms                                                  | 77.9 ms: 1.05x faster                                                   |
| logging_silent             | 135 ns                                                   | 128 ns: 1.05x faster                                                    |
| k_core                     | 2.99 sec                                                 | 2.84 sec: 1.05x faster                                                  |
| go                         | 164 ms                                                   | 156 ms: 1.05x faster                                                    |
| logging_simple             | 7.25 us                                                  | 6.91 us: 1.05x faster                                                   |
| coverage                   | 106 ms                                                   | 101 ms: 1.04x faster                                                    |
| meteor_contest             | 117 ms                                                   | 112 ms: 1.04x faster                                                    |
| sphinx                     | 1.20 sec                                                 | 1.15 sec: 1.04x faster                                                  |
| logging_format             | 8.10 us                                                  | 7.79 us: 1.04x faster                                                   |
| async_generators           | 500 ms                                                   | 481 ms: 1.04x faster                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 8.60 ms: 1.02x faster                                                   |
| djangocms                  | 66.2 us                                                  | 65.0 us: 1.02x faster                                                   |
| genshi_xml                 | 61.6 ms                                                  | 63.2 ms: 1.03x slower                                                   |
| typing_runtime_protocols   | 197 us                                                   | 204 us: 1.03x slower                                                    |
| sympy_str                  | 265 ms                                                   | 275 ms: 1.04x slower                                                    |
| sympy_expand               | 472 ms                                                   | 492 ms: 1.04x slower                                                    |
| docutils                   | 2.96 sec                                                 | 3.11 sec: 1.05x slower                                                  |
| hexiom                     | 7.34 ms                                                  | 7.70 ms: 1.05x slower                                                   |
| connected_components       | 547 ms                                                   | 576 ms: 1.05x slower                                                    |
| comprehensions             | 20.8 us                                                  | 22.0 us: 1.05x slower                                                   |
| shortest_path              | 565 ms                                                   | 597 ms: 1.06x slower                                                    |
| raytrace                   | 310 ms                                                   | 331 ms: 1.07x slower                                                    |
| nbody                      | 118 ms                                                   | 127 ms: 1.07x slower                                                    |
| pickle_pure_python         | 374 us                                                   | 400 us: 1.07x slower                                                    |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.15 ms: 1.07x slower                                                   |
| crypto_pyaes               | 84.9 ms                                                  | 93.3 ms: 1.10x slower                                                   |
| create_gc_cycles           | 3.39 ms                                                  | 3.80 ms: 1.12x slower                                                   |
| gc_traversal               | 5.92 ms                                                  | 6.86 ms: 1.16x slower                                                   |
| pprint_pformat             | 1.99 sec                                                 | 2.34 sec: 1.18x slower                                                  |
| pprint_safe_repr           | 962 ms                                                   | 1.15 sec: 1.19x slower                                                  |
| many_optionals             | 626 us                                                   | 805 us: 1.29x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 28.9 ms: 1.42x slower                                                   |
| telco                      | 10.5 ms                                                  | 168 ms: 16.04x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (21): unpickle_pure_python, pylint, xml_etree_generate, json_dumps, html5lib, thrift, json, sympy_integrate, deltablue, chaos, nqueens, sympy_sum, asyncio_websockets, fannkuch, 2to3, json_loads, pidigits, scimark_lu, pycparser, django_template, coroutines
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250707-3.15.0a0-0240ef4-JIT/bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.016x faster

# HPT report

- Reliability score: 98.48% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x