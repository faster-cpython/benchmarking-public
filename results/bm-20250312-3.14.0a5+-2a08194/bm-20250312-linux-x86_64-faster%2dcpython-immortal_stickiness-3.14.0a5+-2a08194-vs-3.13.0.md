# Results vs. 3.13.0

- fork: faster-cpython
- ref: immortal_stickiness
- machine: linux-x86_64
- commit hash: 2a08194
- commit date: 2025-03-12
- overall geometric mean: 1.042x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 256 ms: 1.04x faster                                                            |
| docutils       | 2.58 sec                                               | 2.62 sec: 1.01x slower                                                          |
| html5lib       | 63.4 ms                                                | 61.2 ms: 1.03x faster                                                           |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                          |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                                            |
| async_tree_io_tg           | 861 ms                                                 | 612 ms: 1.41x faster                                                            |
| async_tree_memoization     | 437 ms                                                 | 315 ms: 1.39x faster                                                            |
| async_tree_io              | 838 ms                                                 | 607 ms: 1.38x faster                                                            |
| async_tree_none            | 350 ms                                                 | 256 ms: 1.37x faster                                                            |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.29x faster                                                            |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 485 ms: 1.18x faster                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 471 ms: 1.15x faster                                                            |
| async_generators           | 433 ms                                                 | 391 ms: 1.11x faster                                                            |
| coroutines                 | 22.2 ms                                                | 23.4 ms: 1.05x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 70.0 ms: 1.12x faster                                                           |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                            |
| nbody          | 87.7 ms                                                | 95.7 ms: 1.09x slower                                                           |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.5 ms: 1.14x faster                                                           |
| regex_effbot   | 3.77 ms                                                | 3.53 ms: 1.07x faster                                                           |
| regex_compile  | 132 ms                                                 | 125 ms: 1.06x faster                                                            |
| regex_dna      | 220 ms                                                 | 225 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                                            |
| tomli_loads          | 2.12 sec                                               | 1.97 sec: 1.07x faster                                                          |
| xml_etree_process    | 60.5 ms                                                | 58.0 ms: 1.04x faster                                                           |
| xml_etree_generate   | 86.8 ms                                                | 83.3 ms: 1.04x faster                                                           |
| xml_etree_iterparse  | 101 ms                                                 | 98.2 ms: 1.03x faster                                                           |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                                            |
| pickle_pure_python   | 302 us                                                 | 314 us: 1.04x slower                                                            |
| json_loads           | 27.2 us                                                | 30.2 us: 1.11x slower                                                           |
| json_dumps           | 10.1 ms                                                | 11.4 ms: 1.13x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.03x slower                                                           |
| python_startup_no_site | 7.00 ms                                                | 8.19 ms: 1.17x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.8 ms: 1.04x faster                                                           |
| genshi_xml      | 50.5 ms                                                | 49.9 ms: 1.01x faster                                                           |
| django_template | 31.7 ms                                                | 31.4 ms: 1.01x faster                                                           |
| mako            | 10.7 ms                                                | 11.1 ms: 1.04x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                                            |
| async_tree_io_tg           | 861 ms                                                 | 612 ms: 1.41x faster                                                            |
| async_tree_memoization     | 437 ms                                                 | 315 ms: 1.39x faster                                                            |
| async_tree_io              | 838 ms                                                 | 607 ms: 1.38x faster                                                            |
| async_tree_none            | 350 ms                                                 | 256 ms: 1.37x faster                                                            |
| deepcopy                   | 354 us                                                 | 261 us: 1.36x faster                                                            |
| deepcopy_memo              | 38.4 us                                                | 29.1 us: 1.32x faster                                                           |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.29x faster                                                            |
| go                         | 141 ms                                                 | 114 ms: 1.23x faster                                                            |
| deepcopy_reduce            | 3.24 us                                                | 2.71 us: 1.20x faster                                                           |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 485 ms: 1.18x faster                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 471 ms: 1.15x faster                                                            |
| spectral_norm              | 113 ms                                                 | 98.4 ms: 1.15x faster                                                           |
| regex_v8                   | 26.9 ms                                                | 23.5 ms: 1.14x faster                                                           |
| pylint                     | 312 ms                                                 | 276 ms: 1.13x faster                                                            |
| float                      | 78.7 ms                                                | 70.0 ms: 1.12x faster                                                           |
| richards                   | 47.5 ms                                                | 42.6 ms: 1.12x faster                                                           |
| dulwich_log                | 64.6 ms                                                | 58.2 ms: 1.11x faster                                                           |
| async_generators           | 433 ms                                                 | 391 ms: 1.11x faster                                                            |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                                            |
| richards_super             | 53.7 ms                                                | 49.0 ms: 1.10x faster                                                           |
| logging_silent             | 101 ns                                                 | 93.6 ns: 1.08x faster                                                           |
| tomli_loads                | 2.12 sec                                               | 1.97 sec: 1.07x faster                                                          |
| regex_effbot               | 3.77 ms                                                | 3.53 ms: 1.07x faster                                                           |
| telco                      | 8.40 ms                                                | 7.92 ms: 1.06x faster                                                           |
| regex_compile              | 132 ms                                                 | 125 ms: 1.06x faster                                                            |
| scimark_sor                | 122 ms                                                 | 117 ms: 1.05x faster                                                            |
| xml_etree_process          | 60.5 ms                                                | 58.0 ms: 1.04x faster                                                           |
| xml_etree_generate         | 86.8 ms                                                | 83.3 ms: 1.04x faster                                                           |
| 2to3                       | 266 ms                                                 | 256 ms: 1.04x faster                                                            |
| scimark_fft                | 367 ms                                                 | 353 ms: 1.04x faster                                                            |
| deltablue                  | 3.19 ms                                                | 3.08 ms: 1.04x faster                                                           |
| pathlib                    | 17.4 ms                                                | 16.8 ms: 1.04x faster                                                           |
| genshi_text                | 22.6 ms                                                | 21.8 ms: 1.04x faster                                                           |
| html5lib                   | 63.4 ms                                                | 61.2 ms: 1.03x faster                                                           |
| sqlite_synth               | 2.90 us                                                | 2.80 us: 1.03x faster                                                           |
| thrift                     | 800 us                                                 | 774 us: 1.03x faster                                                            |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.03x faster                                                          |
| xml_etree_iterparse        | 101 ms                                                 | 98.2 ms: 1.03x faster                                                           |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.5 ms: 1.03x faster                                                           |
| bpe_tokeniser              | 4.69 sec                                               | 4.58 sec: 1.02x faster                                                          |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.02x faster                                                          |
| mdp                        | 2.54 sec                                               | 2.49 sec: 1.02x faster                                                          |
| sympy_str                  | 273 ms                                                 | 267 ms: 1.02x faster                                                            |
| sqlalchemy_declarative     | 133 ms                                                 | 130 ms: 1.02x faster                                                            |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                                            |
| logging_simple             | 5.65 us                                                | 5.55 us: 1.02x faster                                                           |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                          |
| pyflate                    | 470 ms                                                 | 463 ms: 1.01x faster                                                            |
| sympy_expand               | 456 ms                                                 | 450 ms: 1.01x faster                                                            |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                            |
| genshi_xml                 | 50.5 ms                                                | 49.9 ms: 1.01x faster                                                           |
| django_template            | 31.7 ms                                                | 31.4 ms: 1.01x faster                                                           |
| generators                 | 28.8 ms                                                | 28.6 ms: 1.01x faster                                                           |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.01 ms: 1.00x faster                                                           |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                            |
| sympy_integrate            | 19.8 ms                                                | 19.8 ms: 1.00x faster                                                           |
| pprint_safe_repr           | 727 ms                                                 | 730 ms: 1.01x slower                                                            |
| gc_traversal               | 4.90 ms                                                | 4.92 ms: 1.01x slower                                                           |
| hexiom                     | 6.08 ms                                                | 6.13 ms: 1.01x slower                                                           |
| pprint_pformat             | 1.48 sec                                               | 1.49 sec: 1.01x slower                                                          |
| comprehensions             | 16.5 us                                                | 16.7 us: 1.01x slower                                                           |
| docutils                   | 2.58 sec                                               | 2.62 sec: 1.01x slower                                                          |
| shortest_path              | 487 ms                                                 | 494 ms: 1.01x slower                                                            |
| connected_components       | 447 ms                                                 | 454 ms: 1.02x slower                                                            |
| unpickle_pure_python       | 213 us                                                 | 217 us: 1.02x slower                                                            |
| raytrace                   | 262 ms                                                 | 266 ms: 1.02x slower                                                            |
| regex_dna                  | 220 ms                                                 | 225 ms: 1.02x slower                                                            |
| create_gc_cycles           | 2.45 ms                                                | 2.50 ms: 1.02x slower                                                           |
| crypto_pyaes               | 74.7 ms                                                | 76.4 ms: 1.02x slower                                                           |
| scimark_monte_carlo        | 66.8 ms                                                | 68.5 ms: 1.03x slower                                                           |
| chaos                      | 58.0 ms                                                | 59.7 ms: 1.03x slower                                                           |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.03x slower                                                           |
| nqueens                    | 80.9 ms                                                | 83.5 ms: 1.03x slower                                                           |
| pickle_pure_python         | 302 us                                                 | 314 us: 1.04x slower                                                            |
| mako                       | 10.7 ms                                                | 11.1 ms: 1.04x slower                                                           |
| coroutines                 | 22.2 ms                                                | 23.4 ms: 1.05x slower                                                           |
| bench_thread_pool          | 818 us                                                 | 872 us: 1.07x slower                                                            |
| nbody                      | 87.7 ms                                                | 95.7 ms: 1.09x slower                                                           |
| fannkuch                   | 394 ms                                                 | 430 ms: 1.09x slower                                                            |
| many_optionals             | 857 us                                                 | 939 us: 1.10x slower                                                            |
| json_loads                 | 27.2 us                                                | 30.2 us: 1.11x slower                                                           |
| coverage                   | 82.8 ms                                                | 93.2 ms: 1.12x slower                                                           |
| json_dumps                 | 10.1 ms                                                | 11.4 ms: 1.13x slower                                                           |
| python_startup_no_site     | 7.00 ms                                                | 8.19 ms: 1.17x slower                                                           |
| subparsers                 | 15.5 ms                                                | 20.5 ms: 1.33x slower                                                           |
| bench_mp_pool              | 24.0 ms                                                | 82.8 ms: 3.45x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                    |

Benchmark hidden because not significant (5): typing_runtime_protocols, scimark_lu, asyncio_websockets, json, logging_format
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250312-3.14.0a5+-2a08194/bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.042x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.03x