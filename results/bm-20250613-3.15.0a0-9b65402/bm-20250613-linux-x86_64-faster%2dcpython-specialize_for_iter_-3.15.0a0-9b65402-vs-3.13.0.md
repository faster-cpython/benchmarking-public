# Results vs. 3.13.0

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: linux-x86_64
- commit hash: 9b65402
- commit date: 2025-06-13
- overall geometric mean: 1.036x slower
- HPT reliability: 99.71%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 254 ms: 1.05x faster                                                            |
| docutils       | 2.58 sec                                               | 2.56 sec: 1.01x faster                                                          |
| html5lib       | 63.4 ms                                                | 62.3 ms: 1.02x faster                                                           |
| sphinx         | 1.03 sec                                               | 998 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.48x faster                                                            |
| async_tree_io_tg           | 861 ms                                                 | 611 ms: 1.41x faster                                                            |
| async_tree_io              | 838 ms                                                 | 598 ms: 1.40x faster                                                            |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.39x faster                                                            |
| async_tree_none            | 350 ms                                                 | 259 ms: 1.35x faster                                                            |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                            |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 496 ms: 1.16x faster                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 488 ms: 1.11x faster                                                            |
| async_generators           | 433 ms                                                 | 407 ms: 1.07x faster                                                            |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                            |
| coroutines                 | 22.2 ms                                                | 25.0 ms: 1.13x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 73.9 ms: 1.06x faster                                                           |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                            |
| nbody          | 87.7 ms                                                | 100 ms: 1.14x slower                                                            |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.1 ms: 1.21x faster                                                           |
| regex_effbot   | 3.77 ms                                                | 3.11 ms: 1.21x faster                                                           |
| regex_dna      | 220 ms                                                 | 184 ms: 1.19x faster                                                            |
| regex_compile  | 132 ms                                                 | 127 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                  | 1.16x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                                            |
| tomli_loads          | 2.12 sec                                               | 1.99 sec: 1.06x faster                                                          |
| xml_etree_iterparse  | 101 ms                                                 | 99.3 ms: 1.02x faster                                                           |
| xml_etree_generate   | 86.8 ms                                                | 85.4 ms: 1.02x faster                                                           |
| xml_etree_process    | 60.5 ms                                                | 60.2 ms: 1.01x faster                                                           |
| json_loads           | 27.2 us                                                | 27.7 us: 1.02x slower                                                           |
| unpickle_pure_python | 213 us                                                 | 220 us: 1.03x slower                                                            |
| pickle_pure_python   | 302 us                                                 | 317 us: 1.05x slower                                                            |
| json_dumps           | 10.1 ms                                                | 10.9 ms: 1.08x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                           |
| python_startup_no_site | 7.00 ms                                                | 6.91 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.5 ms: 1.05x faster                                                           |
| django_template | 31.7 ms                                                | 32.2 ms: 1.02x slower                                                           |
| mako            | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.07x faster                                                          |
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.48x faster                                                            |
| async_tree_io_tg           | 861 ms                                                 | 611 ms: 1.41x faster                                                            |
| async_tree_io              | 838 ms                                                 | 598 ms: 1.40x faster                                                            |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.39x faster                                                            |
| deepcopy                   | 354 us                                                 | 261 us: 1.36x faster                                                            |
| async_tree_none            | 350 ms                                                 | 259 ms: 1.35x faster                                                            |
| deepcopy_memo              | 38.4 us                                                | 29.2 us: 1.32x faster                                                           |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                            |
| go                         | 141 ms                                                 | 112 ms: 1.25x faster                                                            |
| regex_v8                   | 26.9 ms                                                | 22.1 ms: 1.21x faster                                                           |
| regex_effbot               | 3.77 ms                                                | 3.11 ms: 1.21x faster                                                           |
| regex_dna                  | 220 ms                                                 | 184 ms: 1.19x faster                                                            |
| deepcopy_reduce            | 3.24 us                                                | 2.72 us: 1.19x faster                                                           |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 496 ms: 1.16x faster                                                            |
| pylint                     | 312 ms                                                 | 278 ms: 1.12x faster                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 488 ms: 1.11x faster                                                            |
| richards                   | 47.5 ms                                                | 43.4 ms: 1.10x faster                                                           |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                                            |
| pyflate                    | 470 ms                                                 | 430 ms: 1.09x faster                                                            |
| dulwich_log                | 64.6 ms                                                | 59.5 ms: 1.09x faster                                                           |
| richards_super             | 53.7 ms                                                | 49.5 ms: 1.08x faster                                                           |
| pycparser                  | 1.20 sec                                               | 1.11 sec: 1.08x faster                                                          |
| async_generators           | 433 ms                                                 | 407 ms: 1.07x faster                                                            |
| float                      | 78.7 ms                                                | 73.9 ms: 1.06x faster                                                           |
| tomli_loads                | 2.12 sec                                               | 1.99 sec: 1.06x faster                                                          |
| genshi_text                | 22.6 ms                                                | 21.5 ms: 1.05x faster                                                           |
| bpe_tokeniser              | 4.69 sec                                               | 4.47 sec: 1.05x faster                                                          |
| telco                      | 8.40 ms                                                | 8.02 ms: 1.05x faster                                                           |
| 2to3                       | 266 ms                                                 | 254 ms: 1.05x faster                                                            |
| sympy_integrate            | 19.8 ms                                                | 19.0 ms: 1.05x faster                                                           |
| k_core                     | 2.37 sec                                               | 2.27 sec: 1.04x faster                                                          |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                           |
| spectral_norm              | 113 ms                                                 | 109 ms: 1.04x faster                                                            |
| regex_compile              | 132 ms                                                 | 127 ms: 1.03x faster                                                            |
| sphinx                     | 1.03 sec                                               | 998 ms: 1.03x faster                                                            |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.03x faster                                                            |
| comprehensions             | 16.5 us                                                | 16.0 us: 1.03x faster                                                           |
| json                       | 5.32 ms                                                | 5.22 ms: 1.02x faster                                                           |
| sympy_str                  | 273 ms                                                 | 268 ms: 1.02x faster                                                            |
| pathlib                    | 17.4 ms                                                | 17.0 ms: 1.02x faster                                                           |
| xml_etree_iterparse        | 101 ms                                                 | 99.3 ms: 1.02x faster                                                           |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.02x faster                                                            |
| xml_etree_generate         | 86.8 ms                                                | 85.4 ms: 1.02x faster                                                           |
| html5lib                   | 63.4 ms                                                | 62.3 ms: 1.02x faster                                                           |
| python_startup_no_site     | 7.00 ms                                                | 6.91 ms: 1.01x faster                                                           |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                            |
| sqlite_synth               | 2.90 us                                                | 2.86 us: 1.01x faster                                                           |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.97 ms: 1.01x faster                                                           |
| docutils                   | 2.58 sec                                               | 2.56 sec: 1.01x faster                                                          |
| hexiom                     | 6.08 ms                                                | 6.03 ms: 1.01x faster                                                           |
| xml_etree_process          | 60.5 ms                                                | 60.2 ms: 1.01x faster                                                           |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                            |
| nqueens                    | 80.9 ms                                                | 81.3 ms: 1.01x slower                                                           |
| crypto_pyaes               | 74.7 ms                                                | 75.1 ms: 1.01x slower                                                           |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                                            |
| django_template            | 31.7 ms                                                | 32.2 ms: 1.02x slower                                                           |
| json_loads                 | 27.2 us                                                | 27.7 us: 1.02x slower                                                           |
| scimark_monte_carlo        | 66.8 ms                                                | 68.4 ms: 1.02x slower                                                           |
| chaos                      | 58.0 ms                                                | 59.5 ms: 1.03x slower                                                           |
| unpickle_pure_python       | 213 us                                                 | 220 us: 1.03x slower                                                            |
| raytrace                   | 262 ms                                                 | 270 ms: 1.03x slower                                                            |
| scimark_lu                 | 114 ms                                                 | 118 ms: 1.03x slower                                                            |
| shortest_path              | 487 ms                                                 | 506 ms: 1.04x slower                                                            |
| generators                 | 28.8 ms                                                | 30.0 ms: 1.04x slower                                                           |
| scimark_fft                | 367 ms                                                 | 384 ms: 1.05x slower                                                            |
| pickle_pure_python         | 302 us                                                 | 317 us: 1.05x slower                                                            |
| fannkuch                   | 394 ms                                                 | 414 ms: 1.05x slower                                                            |
| create_gc_cycles           | 2.45 ms                                                | 2.58 ms: 1.06x slower                                                           |
| gc_traversal               | 4.90 ms                                                | 5.17 ms: 1.06x slower                                                           |
| mako                       | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                           |
| typing_runtime_protocols   | 160 us                                                 | 170 us: 1.06x slower                                                            |
| connected_components       | 447 ms                                                 | 476 ms: 1.07x slower                                                            |
| json_dumps                 | 10.1 ms                                                | 10.9 ms: 1.08x slower                                                           |
| logging_simple             | 5.65 us                                                | 6.17 us: 1.09x slower                                                           |
| logging_format             | 6.23 us                                                | 6.89 us: 1.11x slower                                                           |
| deltablue                  | 3.19 ms                                                | 3.54 ms: 1.11x slower                                                           |
| many_optionals             | 857 us                                                 | 957 us: 1.12x slower                                                            |
| pprint_safe_repr           | 727 ms                                                 | 818 ms: 1.13x slower                                                            |
| pprint_pformat             | 1.48 sec                                               | 1.67 sec: 1.13x slower                                                          |
| coroutines                 | 22.2 ms                                                | 25.0 ms: 1.13x slower                                                           |
| nbody                      | 87.7 ms                                                | 100 ms: 1.14x slower                                                            |
| subparsers                 | 15.5 ms                                                | 23.7 ms: 1.53x slower                                                           |
| logging_silent             | 101 ns                                                 | 473 ns: 4.68x slower                                                            |
| coverage                   | 82.8 ms                                                | 419 ms: 5.06x slower                                                            |
| thrift                     | 800 us                                                 | 147 ms: 184.22x slower                                                          |
| Geometric mean             | (ref)                                                  | 1.05x slower                                                                    |

Benchmark hidden because not significant (2): genshi_xml, sympy_expand
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250613-3.15.0a0-9b65402/bm-20250613-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.036x slower

# HPT report

- Reliability score: 99.71% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x