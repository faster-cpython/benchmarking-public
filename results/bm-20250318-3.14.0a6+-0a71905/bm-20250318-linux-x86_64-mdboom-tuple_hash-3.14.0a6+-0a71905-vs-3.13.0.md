# Results vs. 3.13.0

- fork: mdboom
- ref: tuple_hash
- machine: linux-x86_64
- commit hash: 0a71905
- commit date: 2025-03-18
- overall geometric mean: 1.041x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-linux-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 256 ms: 1.04x faster                                         |
| docutils       | 2.58 sec                                               | 2.62 sec: 1.01x slower                                       |
| html5lib       | 63.4 ms                                                | 61.3 ms: 1.03x faster                                        |
| sphinx         | 1.03 sec                                               | 1.02 sec: 1.01x faster                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-linux-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.48x faster                                         |
| async_tree_io_tg           | 861 ms                                                 | 611 ms: 1.41x faster                                         |
| async_tree_memoization     | 437 ms                                                 | 315 ms: 1.39x faster                                         |
| async_tree_io              | 838 ms                                                 | 610 ms: 1.37x faster                                         |
| async_tree_none            | 350 ms                                                 | 256 ms: 1.37x faster                                         |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.29x faster                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 487 ms: 1.18x faster                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 471 ms: 1.15x faster                                         |
| async_generators           | 433 ms                                                 | 390 ms: 1.11x faster                                         |
| coroutines                 | 22.2 ms                                                | 24.2 ms: 1.09x slower                                        |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-linux-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 78.7 ms                                                | 70.0 ms: 1.12x faster                                        |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                         |
| nbody          | 87.7 ms                                                | 98.1 ms: 1.12x slower                                        |
| Geometric mean | (ref)                                                  | 1.00x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-linux-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.26 ms: 1.15x faster                                        |
| regex_v8       | 26.9 ms                                                | 24.2 ms: 1.11x faster                                        |
| regex_compile  | 132 ms                                                 | 126 ms: 1.04x faster                                         |
| Geometric mean | (ref)                                                  | 1.07x faster                                                 |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-linux-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 142 ms: 1.09x faster                                         |
| tomli_loads          | 2.12 sec                                               | 2.00 sec: 1.06x faster                                       |
| xml_etree_process    | 60.5 ms                                                | 58.3 ms: 1.04x faster                                        |
| xml_etree_generate   | 86.8 ms                                                | 84.2 ms: 1.03x faster                                        |
| xml_etree_iterparse  | 101 ms                                                 | 98.2 ms: 1.03x faster                                        |
| unpickle_pure_python | 213 us                                                 | 218 us: 1.02x slower                                         |
| pickle_pure_python   | 302 us                                                 | 315 us: 1.04x slower                                         |
| json_loads           | 27.2 us                                                | 30.1 us: 1.11x slower                                        |
| json_dumps           | 10.1 ms                                                | 11.4 ms: 1.13x slower                                        |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-linux-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.04x slower                                        |
| python_startup_no_site | 7.00 ms                                                | 8.21 ms: 1.17x slower                                        |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-linux-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_text    | 22.6 ms                                                | 21.5 ms: 1.05x faster                                        |
| genshi_xml     | 50.5 ms                                                | 49.4 ms: 1.02x faster                                        |
| mako           | 10.7 ms                                                | 11.3 ms: 1.06x slower                                        |
| Geometric mean | (ref)                                                  | 1.00x faster                                                 |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-linux-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.48x faster                                         |
| async_tree_io_tg           | 861 ms                                                 | 611 ms: 1.41x faster                                         |
| deepcopy                   | 354 us                                                 | 255 us: 1.39x faster                                         |
| async_tree_memoization     | 437 ms                                                 | 315 ms: 1.39x faster                                         |
| async_tree_io              | 838 ms                                                 | 610 ms: 1.37x faster                                         |
| async_tree_none            | 350 ms                                                 | 256 ms: 1.37x faster                                         |
| deepcopy_memo              | 38.4 us                                                | 29.1 us: 1.32x faster                                        |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.29x faster                                         |
| go                         | 141 ms                                                 | 113 ms: 1.24x faster                                         |
| deepcopy_reduce            | 3.24 us                                                | 2.66 us: 1.22x faster                                        |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 487 ms: 1.18x faster                                         |
| spectral_norm              | 113 ms                                                 | 97.7 ms: 1.16x faster                                        |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 471 ms: 1.15x faster                                         |
| regex_effbot               | 3.77 ms                                                | 3.26 ms: 1.15x faster                                        |
| pylint                     | 312 ms                                                 | 276 ms: 1.13x faster                                         |
| richards                   | 47.5 ms                                                | 42.1 ms: 1.13x faster                                        |
| float                      | 78.7 ms                                                | 70.0 ms: 1.12x faster                                        |
| async_generators           | 433 ms                                                 | 390 ms: 1.11x faster                                         |
| dulwich_log                | 64.6 ms                                                | 58.3 ms: 1.11x faster                                        |
| regex_v8                   | 26.9 ms                                                | 24.2 ms: 1.11x faster                                        |
| richards_super             | 53.7 ms                                                | 48.6 ms: 1.11x faster                                        |
| xml_etree_parse            | 154 ms                                                 | 142 ms: 1.09x faster                                         |
| telco                      | 8.40 ms                                                | 7.80 ms: 1.08x faster                                        |
| logging_silent             | 101 ns                                                 | 94.2 ns: 1.07x faster                                        |
| pycparser                  | 1.20 sec                                               | 1.13 sec: 1.06x faster                                       |
| tomli_loads                | 2.12 sec                                               | 2.00 sec: 1.06x faster                                       |
| genshi_text                | 22.6 ms                                                | 21.5 ms: 1.05x faster                                        |
| pathlib                    | 17.4 ms                                                | 16.5 ms: 1.05x faster                                        |
| scimark_fft                | 367 ms                                                 | 350 ms: 1.05x faster                                         |
| sqlite_synth               | 2.90 us                                                | 2.77 us: 1.05x faster                                        |
| regex_compile              | 132 ms                                                 | 126 ms: 1.04x faster                                         |
| 2to3                       | 266 ms                                                 | 256 ms: 1.04x faster                                         |
| xml_etree_process          | 60.5 ms                                                | 58.3 ms: 1.04x faster                                        |
| pyflate                    | 470 ms                                                 | 454 ms: 1.04x faster                                         |
| html5lib                   | 63.4 ms                                                | 61.3 ms: 1.03x faster                                        |
| xml_etree_generate         | 86.8 ms                                                | 84.2 ms: 1.03x faster                                        |
| xml_etree_iterparse        | 101 ms                                                 | 98.2 ms: 1.03x faster                                        |
| scimark_sor                | 122 ms                                                 | 118 ms: 1.03x faster                                         |
| thrift                     | 800 us                                                 | 776 us: 1.03x faster                                         |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.4 ms: 1.03x faster                                        |
| deltablue                  | 3.19 ms                                                | 3.11 ms: 1.03x faster                                        |
| k_core                     | 2.37 sec                                               | 2.31 sec: 1.03x faster                                       |
| genshi_xml                 | 50.5 ms                                                | 49.4 ms: 1.02x faster                                        |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                         |
| logging_simple             | 5.65 us                                                | 5.54 us: 1.02x faster                                        |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                         |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.94 ms: 1.02x faster                                        |
| sympy_str                  | 273 ms                                                 | 269 ms: 1.02x faster                                         |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.02x faster                                         |
| sphinx                     | 1.03 sec                                               | 1.02 sec: 1.01x faster                                       |
| bpe_tokeniser              | 4.69 sec                                               | 4.64 sec: 1.01x faster                                       |
| generators                 | 28.8 ms                                                | 28.6 ms: 1.01x faster                                        |
| pprint_pformat             | 1.48 sec                                               | 1.47 sec: 1.00x faster                                       |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                         |
| gc_traversal               | 4.90 ms                                                | 4.92 ms: 1.01x slower                                        |
| docutils                   | 2.58 sec                                               | 2.62 sec: 1.01x slower                                       |
| raytrace                   | 262 ms                                                 | 265 ms: 1.01x slower                                         |
| comprehensions             | 16.5 us                                                | 16.7 us: 1.01x slower                                        |
| crypto_pyaes               | 74.7 ms                                                | 75.8 ms: 1.02x slower                                        |
| connected_components       | 447 ms                                                 | 455 ms: 1.02x slower                                         |
| shortest_path              | 487 ms                                                 | 497 ms: 1.02x slower                                         |
| unpickle_pure_python       | 213 us                                                 | 218 us: 1.02x slower                                         |
| create_gc_cycles           | 2.45 ms                                                | 2.50 ms: 1.02x slower                                        |
| scimark_monte_carlo        | 66.8 ms                                                | 68.5 ms: 1.03x slower                                        |
| chaos                      | 58.0 ms                                                | 59.8 ms: 1.03x slower                                        |
| typing_runtime_protocols   | 160 us                                                 | 166 us: 1.03x slower                                         |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.04x slower                                        |
| hexiom                     | 6.08 ms                                                | 6.31 ms: 1.04x slower                                        |
| pickle_pure_python         | 302 us                                                 | 315 us: 1.04x slower                                         |
| nqueens                    | 80.9 ms                                                | 84.3 ms: 1.04x slower                                        |
| mdp                        | 2.54 sec                                               | 2.66 sec: 1.05x slower                                       |
| mako                       | 10.7 ms                                                | 11.3 ms: 1.06x slower                                        |
| bench_thread_pool          | 818 us                                                 | 869 us: 1.06x slower                                         |
| coroutines                 | 22.2 ms                                                | 24.2 ms: 1.09x slower                                        |
| coverage                   | 82.8 ms                                                | 90.8 ms: 1.10x slower                                        |
| fannkuch                   | 394 ms                                                 | 432 ms: 1.10x slower                                         |
| many_optionals             | 857 us                                                 | 949 us: 1.11x slower                                         |
| json_loads                 | 27.2 us                                                | 30.1 us: 1.11x slower                                        |
| nbody                      | 87.7 ms                                                | 98.1 ms: 1.12x slower                                        |
| json_dumps                 | 10.1 ms                                                | 11.4 ms: 1.13x slower                                        |
| python_startup_no_site     | 7.00 ms                                                | 8.21 ms: 1.17x slower                                        |
| subparsers                 | 15.5 ms                                                | 20.8 ms: 1.35x slower                                        |
| bench_mp_pool              | 24.0 ms                                                | 82.9 ms: 3.46x slower                                        |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                 |

Benchmark hidden because not significant (9): django_template, pprint_safe_repr, sympy_integrate, logging_format, json, sympy_expand, asyncio_websockets, regex_dna, scimark_lu
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250318-3.14.0a6+-0a71905/bm-20250318-linux-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.041x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x