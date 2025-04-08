# Results vs. 3.13.0

- fork: mdboom
- ref: unicode_hash_eq
- machine: linux-x86_64
- commit hash: ff745e5
- commit date: 2025-04-08
- overall geometric mean: 1.051x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-linux-x86_64-mdboom-unicode_hash_eq-3.14.0a6+-ff745e5 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 256 ms: 1.04x faster                                              |
| docutils       | 2.58 sec                                               | 2.60 sec: 1.00x slower                                            |
| html5lib       | 63.4 ms                                                | 62.6 ms: 1.01x faster                                             |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                            |
| Geometric mean | (ref)                                                  | 1.02x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-linux-x86_64-mdboom-unicode_hash_eq-3.14.0a6+-ff745e5 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                              |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                              |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                              |
| async_tree_io              | 838 ms                                                 | 614 ms: 1.37x faster                                              |
| async_tree_none            | 350 ms                                                 | 259 ms: 1.35x faster                                              |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                              |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 487 ms: 1.18x faster                                              |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 477 ms: 1.14x faster                                              |
| async_generators           | 433 ms                                                 | 396 ms: 1.10x faster                                              |
| coroutines                 | 22.2 ms                                                | 23.0 ms: 1.03x slower                                             |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                      |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-linux-x86_64-mdboom-unicode_hash_eq-3.14.0a6+-ff745e5 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 78.7 ms                                                | 70.6 ms: 1.11x faster                                             |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                              |
| nbody          | 87.7 ms                                                | 95.9 ms: 1.09x slower                                             |
| Geometric mean | (ref)                                                  | 1.01x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-linux-x86_64-mdboom-unicode_hash_eq-3.14.0a6+-ff745e5 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.0 ms: 1.17x faster                                             |
| regex_compile  | 132 ms                                                 | 125 ms: 1.05x faster                                              |
| regex_dna      | 220 ms                                                 | 216 ms: 1.02x faster                                              |
| regex_effbot   | 3.77 ms                                                | 3.81 ms: 1.01x slower                                             |
| Geometric mean | (ref)                                                  | 1.05x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-linux-x86_64-mdboom-unicode_hash_eq-3.14.0a6+-ff745e5 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.93 sec: 1.09x faster                                            |
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                              |
| xml_etree_process    | 60.5 ms                                                | 58.7 ms: 1.03x faster                                             |
| xml_etree_iterparse  | 101 ms                                                 | 98.6 ms: 1.03x faster                                             |
| xml_etree_generate   | 86.8 ms                                                | 85.1 ms: 1.02x faster                                             |
| unpickle_pure_python | 213 us                                                 | 218 us: 1.02x slower                                              |
| pickle_pure_python   | 302 us                                                 | 320 us: 1.06x slower                                              |
| json_loads           | 27.2 us                                                | 29.8 us: 1.10x slower                                             |
| json_dumps           | 10.1 ms                                                | 11.4 ms: 1.12x slower                                             |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-linux-x86_64-mdboom-unicode_hash_eq-3.14.0a6+-ff745e5 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.04x slower                                             |
| python_startup_no_site | 7.00 ms                                                | 8.20 ms: 1.17x slower                                             |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-linux-x86_64-mdboom-unicode_hash_eq-3.14.0a6+-ff745e5 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_text    | 22.6 ms                                                | 21.5 ms: 1.05x faster                                             |
| genshi_xml     | 50.5 ms                                                | 49.4 ms: 1.02x faster                                             |
| mako           | 10.7 ms                                                | 11.3 ms: 1.06x slower                                             |
| Geometric mean | (ref)                                                  | 1.01x faster                                                      |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-linux-x86_64-mdboom-unicode_hash_eq-3.14.0a6+-ff745e5 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.06x faster                                            |
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                              |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                              |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                              |
| deepcopy                   | 354 us                                                 | 256 us: 1.38x faster                                              |
| async_tree_io              | 838 ms                                                 | 614 ms: 1.37x faster                                              |
| async_tree_none            | 350 ms                                                 | 259 ms: 1.35x faster                                              |
| deepcopy_memo              | 38.4 us                                                | 29.7 us: 1.29x faster                                             |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                              |
| go                         | 141 ms                                                 | 115 ms: 1.23x faster                                              |
| deepcopy_reduce            | 3.24 us                                                | 2.69 us: 1.21x faster                                             |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 487 ms: 1.18x faster                                              |
| regex_v8                   | 26.9 ms                                                | 23.0 ms: 1.17x faster                                             |
| spectral_norm              | 113 ms                                                 | 98.7 ms: 1.15x faster                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 477 ms: 1.14x faster                                              |
| pylint                     | 312 ms                                                 | 277 ms: 1.13x faster                                              |
| float                      | 78.7 ms                                                | 70.6 ms: 1.11x faster                                             |
| dulwich_log                | 64.6 ms                                                | 58.0 ms: 1.11x faster                                             |
| async_generators           | 433 ms                                                 | 396 ms: 1.10x faster                                              |
| tomli_loads                | 2.12 sec                                               | 1.93 sec: 1.09x faster                                            |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                              |
| richards                   | 47.5 ms                                                | 44.0 ms: 1.08x faster                                             |
| richards_super             | 53.7 ms                                                | 50.1 ms: 1.07x faster                                             |
| telco                      | 8.40 ms                                                | 7.90 ms: 1.06x faster                                             |
| pathlib                    | 17.4 ms                                                | 16.4 ms: 1.06x faster                                             |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.75 ms: 1.06x faster                                             |
| genshi_text                | 22.6 ms                                                | 21.5 ms: 1.05x faster                                             |
| regex_compile              | 132 ms                                                 | 125 ms: 1.05x faster                                              |
| scimark_fft                | 367 ms                                                 | 351 ms: 1.05x faster                                              |
| k_core                     | 2.37 sec                                               | 2.27 sec: 1.04x faster                                            |
| pyflate                    | 470 ms                                                 | 451 ms: 1.04x faster                                              |
| sqlite_synth               | 2.90 us                                                | 2.79 us: 1.04x faster                                             |
| 2to3                       | 266 ms                                                 | 256 ms: 1.04x faster                                              |
| sympy_integrate            | 19.8 ms                                                | 19.2 ms: 1.03x faster                                             |
| xml_etree_process          | 60.5 ms                                                | 58.7 ms: 1.03x faster                                             |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.03x faster                                            |
| xml_etree_iterparse        | 101 ms                                                 | 98.6 ms: 1.03x faster                                             |
| bpe_tokeniser              | 4.69 sec                                               | 4.57 sec: 1.03x faster                                            |
| logging_simple             | 5.65 us                                                | 5.51 us: 1.03x faster                                             |
| genshi_xml                 | 50.5 ms                                                | 49.4 ms: 1.02x faster                                             |
| sympy_str                  | 273 ms                                                 | 267 ms: 1.02x faster                                              |
| logging_format             | 6.23 us                                                | 6.10 us: 1.02x faster                                             |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                            |
| xml_etree_generate         | 86.8 ms                                                | 85.1 ms: 1.02x faster                                             |
| generators                 | 28.8 ms                                                | 28.2 ms: 1.02x faster                                             |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                              |
| regex_dna                  | 220 ms                                                 | 216 ms: 1.02x faster                                              |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.02x faster                                              |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.02x faster                                              |
| html5lib                   | 63.4 ms                                                | 62.6 ms: 1.01x faster                                             |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                              |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.7 ms: 1.01x faster                                             |
| crypto_pyaes               | 74.7 ms                                                | 74.0 ms: 1.01x faster                                             |
| scimark_lu                 | 114 ms                                                 | 114 ms: 1.01x faster                                              |
| chaos                      | 58.0 ms                                                | 57.6 ms: 1.01x faster                                             |
| pprint_safe_repr           | 727 ms                                                 | 723 ms: 1.00x faster                                              |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                              |
| gc_traversal               | 4.90 ms                                                | 4.89 ms: 1.00x faster                                             |
| docutils                   | 2.58 sec                                               | 2.60 sec: 1.00x slower                                            |
| coverage                   | 82.8 ms                                                | 83.4 ms: 1.01x slower                                             |
| comprehensions             | 16.5 us                                                | 16.7 us: 1.01x slower                                             |
| regex_effbot               | 3.77 ms                                                | 3.81 ms: 1.01x slower                                             |
| raytrace                   | 262 ms                                                 | 265 ms: 1.01x slower                                              |
| scimark_monte_carlo        | 66.8 ms                                                | 67.7 ms: 1.01x slower                                             |
| create_gc_cycles           | 2.45 ms                                                | 2.49 ms: 1.02x slower                                             |
| nqueens                    | 80.9 ms                                                | 82.4 ms: 1.02x slower                                             |
| unpickle_pure_python       | 213 us                                                 | 218 us: 1.02x slower                                              |
| coroutines                 | 22.2 ms                                                | 23.0 ms: 1.03x slower                                             |
| hexiom                     | 6.08 ms                                                | 6.29 ms: 1.03x slower                                             |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.04x slower                                             |
| mako                       | 10.7 ms                                                | 11.3 ms: 1.06x slower                                             |
| pickle_pure_python         | 302 us                                                 | 320 us: 1.06x slower                                              |
| connected_components       | 447 ms                                                 | 477 ms: 1.07x slower                                              |
| bench_thread_pool          | 818 us                                                 | 874 us: 1.07x slower                                              |
| fannkuch                   | 394 ms                                                 | 422 ms: 1.07x slower                                              |
| shortest_path              | 487 ms                                                 | 522 ms: 1.07x slower                                              |
| nbody                      | 87.7 ms                                                | 95.9 ms: 1.09x slower                                             |
| json_loads                 | 27.2 us                                                | 29.8 us: 1.10x slower                                             |
| many_optionals             | 857 us                                                 | 944 us: 1.10x slower                                              |
| json_dumps                 | 10.1 ms                                                | 11.4 ms: 1.12x slower                                             |
| python_startup_no_site     | 7.00 ms                                                | 8.20 ms: 1.17x slower                                             |
| subparsers                 | 15.5 ms                                                | 20.6 ms: 1.33x slower                                             |
| bench_mp_pool              | 24.0 ms                                                | 83.3 ms: 3.47x slower                                             |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                      |

Benchmark hidden because not significant (8): json, django_template, deltablue, pprint_pformat, asyncio_websockets, sympy_expand, typing_runtime_protocols, logging_silent
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250408-3.14.0a6+-ff745e5/bm-20250408-linux-x86_64-mdboom-unicode_hash_eq-3.14.0a6+-ff745e5.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.051x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x