# Results vs. 3.13.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: cbee8d2
- commit date: 2025-06-23
- overall geometric mean: 1.085x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-cbee8d2 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 292 ms: 1.10x slower                                                          |
| docutils       | 2.58 sec                                               | 2.82 sec: 1.09x slower                                                        |
| html5lib       | 63.4 ms                                                | 64.4 ms: 1.02x slower                                                         |
| sphinx         | 1.03 sec                                               | 1.06 sec: 1.02x slower                                                        |
| Geometric mean | (ref)                                                  | 1.06x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-cbee8d2 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 339 ms: 1.36x faster                                                          |
| async_tree_io              | 838 ms                                                 | 643 ms: 1.30x faster                                                          |
| async_tree_io_tg           | 861 ms                                                 | 661 ms: 1.30x faster                                                          |
| async_tree_memoization     | 437 ms                                                 | 341 ms: 1.28x faster                                                          |
| async_tree_none            | 350 ms                                                 | 289 ms: 1.21x faster                                                          |
| async_tree_none_tg         | 319 ms                                                 | 273 ms: 1.17x faster                                                          |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 532 ms: 1.08x faster                                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 522 ms: 1.04x faster                                                          |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                          |
| coroutines                 | 22.2 ms                                                | 25.0 ms: 1.12x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.14x faster                                                                  |

Benchmark hidden because not significant (1): async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-cbee8d2 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 193 ms: 1.03x slower                                                          |
| float          | 78.7 ms                                                | 91.9 ms: 1.17x slower                                                         |
| nbody          | 87.7 ms                                                | 176 ms: 2.00x slower                                                          |
| Geometric mean | (ref)                                                  | 1.34x slower                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-cbee8d2 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.4 ms: 1.20x faster                                                         |
| regex_effbot   | 3.77 ms                                                | 3.22 ms: 1.17x faster                                                         |
| regex_dna      | 220 ms                                                 | 199 ms: 1.11x faster                                                          |
| regex_compile  | 132 ms                                                 | 143 ms: 1.09x slower                                                          |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-cbee8d2 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 148 ms: 1.04x faster                                                          |
| json_loads           | 27.2 us                                                | 28.3 us: 1.04x slower                                                         |
| xml_etree_iterparse  | 101 ms                                                 | 106 ms: 1.05x slower                                                          |
| json_dumps           | 10.1 ms                                                | 10.9 ms: 1.08x slower                                                         |
| xml_etree_generate   | 86.8 ms                                                | 102 ms: 1.17x slower                                                          |
| tomli_loads          | 2.12 sec                                               | 2.48 sec: 1.17x slower                                                        |
| xml_etree_process    | 60.5 ms                                                | 72.1 ms: 1.19x slower                                                         |
| pickle_pure_python   | 302 us                                                 | 398 us: 1.32x slower                                                          |
| unpickle_pure_python | 213 us                                                 | 334 us: 1.57x slower                                                          |
| Geometric mean       | (ref)                                                  | 1.16x slower                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-cbee8d2 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                         |
| python_startup_no_site | 7.00 ms                                                | 6.94 ms: 1.01x faster                                                         |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-cbee8d2 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.6 ms: 1.05x faster                                                         |
| django_template | 31.7 ms                                                | 33.2 ms: 1.05x slower                                                         |
| genshi_xml      | 50.5 ms                                                | 54.0 ms: 1.07x slower                                                         |
| mako            | 10.7 ms                                                | 16.6 ms: 1.55x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.14x slower                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-cbee8d2 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.41 sec: 1.80x faster                                                        |
| async_tree_memoization_tg  | 463 ms                                                 | 339 ms: 1.36x faster                                                          |
| deepcopy                   | 354 us                                                 | 267 us: 1.33x faster                                                          |
| async_tree_io              | 838 ms                                                 | 643 ms: 1.30x faster                                                          |
| async_tree_io_tg           | 861 ms                                                 | 661 ms: 1.30x faster                                                          |
| async_tree_memoization     | 437 ms                                                 | 341 ms: 1.28x faster                                                          |
| deepcopy_memo              | 38.4 us                                                | 30.1 us: 1.28x faster                                                         |
| async_tree_none            | 350 ms                                                 | 289 ms: 1.21x faster                                                          |
| regex_v8                   | 26.9 ms                                                | 22.4 ms: 1.20x faster                                                         |
| regex_effbot               | 3.77 ms                                                | 3.22 ms: 1.17x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 273 ms: 1.17x faster                                                          |
| deepcopy_reduce            | 3.24 us                                                | 2.79 us: 1.16x faster                                                         |
| regex_dna                  | 220 ms                                                 | 199 ms: 1.11x faster                                                          |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 532 ms: 1.08x faster                                                          |
| pylint                     | 312 ms                                                 | 291 ms: 1.07x faster                                                          |
| genshi_text                | 22.6 ms                                                | 21.6 ms: 1.05x faster                                                         |
| xml_etree_parse            | 154 ms                                                 | 148 ms: 1.04x faster                                                          |
| dulwich_log                | 64.6 ms                                                | 62.0 ms: 1.04x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 522 ms: 1.04x faster                                                          |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                         |
| thrift                     | 800 us                                                 | 774 us: 1.03x faster                                                          |
| json                       | 5.32 ms                                                | 5.22 ms: 1.02x faster                                                         |
| scimark_sor                | 122 ms                                                 | 121 ms: 1.01x faster                                                          |
| python_startup_no_site     | 7.00 ms                                                | 6.94 ms: 1.01x faster                                                         |
| pathlib                    | 17.4 ms                                                | 17.3 ms: 1.01x faster                                                         |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                          |
| gc_traversal               | 4.90 ms                                                | 4.96 ms: 1.01x slower                                                         |
| html5lib                   | 63.4 ms                                                | 64.4 ms: 1.02x slower                                                         |
| sphinx                     | 1.03 sec                                               | 1.06 sec: 1.02x slower                                                        |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.03x slower                                                          |
| sqlite_synth               | 2.90 us                                                | 2.98 us: 1.03x slower                                                         |
| sympy_integrate            | 19.8 ms                                                | 20.4 ms: 1.03x slower                                                         |
| pidigits                   | 186 ms                                                 | 193 ms: 1.03x slower                                                          |
| k_core                     | 2.37 sec                                               | 2.46 sec: 1.04x slower                                                        |
| json_loads                 | 27.2 us                                                | 28.3 us: 1.04x slower                                                         |
| coverage                   | 82.8 ms                                                | 86.4 ms: 1.04x slower                                                         |
| xml_etree_iterparse        | 101 ms                                                 | 106 ms: 1.05x slower                                                          |
| django_template            | 31.7 ms                                                | 33.2 ms: 1.05x slower                                                         |
| djangocms                  | 22.3 us                                                | 23.4 us: 1.05x slower                                                         |
| sympy_sum                  | 150 ms                                                 | 159 ms: 1.06x slower                                                          |
| create_gc_cycles           | 2.45 ms                                                | 2.60 ms: 1.06x slower                                                         |
| generators                 | 28.8 ms                                                | 30.5 ms: 1.06x slower                                                         |
| sympy_str                  | 273 ms                                                 | 291 ms: 1.07x slower                                                          |
| genshi_xml                 | 50.5 ms                                                | 54.0 ms: 1.07x slower                                                         |
| json_dumps                 | 10.1 ms                                                | 10.9 ms: 1.08x slower                                                         |
| regex_compile              | 132 ms                                                 | 143 ms: 1.09x slower                                                          |
| logging_simple             | 5.65 us                                                | 6.17 us: 1.09x slower                                                         |
| docutils                   | 2.58 sec                                               | 2.82 sec: 1.09x slower                                                        |
| 2to3                       | 266 ms                                                 | 292 ms: 1.10x slower                                                          |
| telco                      | 8.40 ms                                                | 9.25 ms: 1.10x slower                                                         |
| logging_format             | 6.23 us                                                | 6.89 us: 1.11x slower                                                         |
| richards_super             | 53.7 ms                                                | 59.6 ms: 1.11x slower                                                         |
| sympy_expand               | 456 ms                                                 | 511 ms: 1.12x slower                                                          |
| coroutines                 | 22.2 ms                                                | 25.0 ms: 1.12x slower                                                         |
| nqueens                    | 80.9 ms                                                | 91.6 ms: 1.13x slower                                                         |
| chaos                      | 58.0 ms                                                | 66.4 ms: 1.14x slower                                                         |
| shortest_path              | 487 ms                                                 | 558 ms: 1.15x slower                                                          |
| float                      | 78.7 ms                                                | 91.9 ms: 1.17x slower                                                         |
| xml_etree_generate         | 86.8 ms                                                | 102 ms: 1.17x slower                                                          |
| tomli_loads                | 2.12 sec                                               | 2.48 sec: 1.17x slower                                                        |
| richards                   | 47.5 ms                                                | 56.0 ms: 1.18x slower                                                         |
| connected_components       | 447 ms                                                 | 532 ms: 1.19x slower                                                          |
| xml_etree_process          | 60.5 ms                                                | 72.1 ms: 1.19x slower                                                         |
| many_optionals             | 857 us                                                 | 1.02 ms: 1.19x slower                                                         |
| pycparser                  | 1.20 sec                                               | 1.45 sec: 1.21x slower                                                        |
| pyflate                    | 470 ms                                                 | 573 ms: 1.22x slower                                                          |
| bpe_tokeniser              | 4.69 sec                                               | 5.82 sec: 1.24x slower                                                        |
| scimark_monte_carlo        | 66.8 ms                                                | 82.9 ms: 1.24x slower                                                         |
| meteor_contest             | 108 ms                                                 | 135 ms: 1.24x slower                                                          |
| spectral_norm              | 113 ms                                                 | 141 ms: 1.24x slower                                                          |
| typing_runtime_protocols   | 160 us                                                 | 200 us: 1.25x slower                                                          |
| raytrace                   | 262 ms                                                 | 329 ms: 1.26x slower                                                          |
| scimark_fft                | 367 ms                                                 | 472 ms: 1.29x slower                                                          |
| pickle_pure_python         | 302 us                                                 | 398 us: 1.32x slower                                                          |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 6.97 ms: 1.39x slower                                                         |
| crypto_pyaes               | 74.7 ms                                                | 105 ms: 1.40x slower                                                          |
| fannkuch                   | 394 ms                                                 | 564 ms: 1.43x slower                                                          |
| go                         | 141 ms                                                 | 207 ms: 1.47x slower                                                          |
| comprehensions             | 16.5 us                                                | 25.3 us: 1.54x slower                                                         |
| deltablue                  | 3.19 ms                                                | 4.96 ms: 1.55x slower                                                         |
| mako                       | 10.7 ms                                                | 16.6 ms: 1.55x slower                                                         |
| pprint_safe_repr           | 727 ms                                                 | 1.13 sec: 1.56x slower                                                        |
| unpickle_pure_python       | 213 us                                                 | 334 us: 1.57x slower                                                          |
| hexiom                     | 6.08 ms                                                | 9.66 ms: 1.59x slower                                                         |
| pprint_pformat             | 1.48 sec                                               | 2.36 sec: 1.60x slower                                                        |
| subparsers                 | 15.5 ms                                                | 25.1 ms: 1.63x slower                                                         |
| nbody                      | 87.7 ms                                                | 176 ms: 2.00x slower                                                          |
| logging_silent             | 101 ns                                                 | 476 ns: 4.71x slower                                                          |
| Geometric mean             | (ref)                                                  | 1.11x slower                                                                  |

Benchmark hidden because not significant (1): async_generators
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250623-3.15.0a0-cbee8d2-PYTHON_UOPS/bm-20250623-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-cbee8d2.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.085x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.07x