# Results vs. 3.13.0

- fork: mdboom
- ref: faster_pprint3
- machine: linux-x86_64
- commit hash: 4fbfba2
- commit date: 2025-06-18
- overall geometric mean: 1.075x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250618-linux-x86_64-mdboom-faster_pprint3-3.15.0a0-4fbfba2 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 292 ms: 1.10x slower                                            |
| docutils       | 2.58 sec                                               | 2.85 sec: 1.10x slower                                          |
| html5lib       | 63.4 ms                                                | 64.7 ms: 1.02x slower                                           |
| sphinx         | 1.03 sec                                               | 1.12 sec: 1.09x slower                                          |
| Geometric mean | (ref)                                                  | 1.08x slower                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250618-linux-x86_64-mdboom-faster_pprint3-3.15.0a0-4fbfba2 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 346 ms: 1.34x faster                                            |
| async_tree_io_tg           | 861 ms                                                 | 679 ms: 1.27x faster                                            |
| async_tree_io              | 838 ms                                                 | 663 ms: 1.26x faster                                            |
| async_tree_memoization     | 437 ms                                                 | 347 ms: 1.26x faster                                            |
| async_tree_none            | 350 ms                                                 | 289 ms: 1.21x faster                                            |
| async_tree_none_tg         | 319 ms                                                 | 277 ms: 1.15x faster                                            |
| async_generators           | 433 ms                                                 | 413 ms: 1.05x faster                                            |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                            |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 602 ms: 1.05x slower                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 591 ms: 1.09x slower                                            |
| coroutines                 | 22.2 ms                                                | 26.9 ms: 1.21x slower                                           |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250618-linux-x86_64-mdboom-faster_pprint3-3.15.0a0-4fbfba2 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 78.7 ms                                                | 75.4 ms: 1.04x faster                                           |
| pidigits       | 186 ms                                                 | 205 ms: 1.10x slower                                            |
| nbody          | 87.7 ms                                                | 106 ms: 1.21x slower                                            |
| Geometric mean | (ref)                                                  | 1.08x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250618-linux-x86_64-mdboom-faster_pprint3-3.15.0a0-4fbfba2 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 2.93 ms: 1.29x faster                                           |
| regex_v8       | 26.9 ms                                                | 24.0 ms: 1.12x faster                                           |
| regex_dna      | 220 ms                                                 | 197 ms: 1.12x faster                                            |
| regex_compile  | 132 ms                                                 | 144 ms: 1.09x slower                                            |
| Geometric mean | (ref)                                                  | 1.10x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250618-linux-x86_64-mdboom-faster_pprint3-3.15.0a0-4fbfba2 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 2.21 sec: 1.05x slower                                          |
| xml_etree_parse      | 154 ms                                                 | 163 ms: 1.05x slower                                            |
| xml_etree_iterparse  | 101 ms                                                 | 112 ms: 1.11x slower                                            |
| unpickle_pure_python | 213 us                                                 | 257 us: 1.21x slower                                            |
| xml_etree_process    | 60.5 ms                                                | 74.5 ms: 1.23x slower                                           |
| pickle_pure_python   | 302 us                                                 | 376 us: 1.24x slower                                            |
| xml_etree_generate   | 86.8 ms                                                | 108 ms: 1.25x slower                                            |
| json_loads           | 27.2 us                                                | 34.1 us: 1.25x slower                                           |
| json_dumps           | 10.1 ms                                                | 13.5 ms: 1.33x slower                                           |
| Geometric mean       | (ref)                                                  | 1.19x slower                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250618-linux-x86_64-mdboom-faster_pprint3-3.15.0a0-4fbfba2 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.04x slower                                           |
| python_startup_no_site | 7.00 ms                                                | 7.42 ms: 1.06x slower                                           |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250618-linux-x86_64-mdboom-faster_pprint3-3.15.0a0-4fbfba2 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| genshi_xml      | 50.5 ms                                                | 57.2 ms: 1.13x slower                                           |
| genshi_text     | 22.6 ms                                                | 25.7 ms: 1.14x slower                                           |
| mako            | 10.7 ms                                                | 13.6 ms: 1.28x slower                                           |
| django_template | 31.7 ms                                                | 40.9 ms: 1.29x slower                                           |
| Geometric mean  | (ref)                                                  | 1.21x slower                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250618-linux-x86_64-mdboom-faster_pprint3-3.15.0a0-4fbfba2 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.47 sec: 1.73x faster                                          |
| async_tree_memoization_tg  | 463 ms                                                 | 346 ms: 1.34x faster                                            |
| regex_effbot               | 3.77 ms                                                | 2.93 ms: 1.29x faster                                           |
| async_tree_io_tg           | 861 ms                                                 | 679 ms: 1.27x faster                                            |
| async_tree_io              | 838 ms                                                 | 663 ms: 1.26x faster                                            |
| async_tree_memoization     | 437 ms                                                 | 347 ms: 1.26x faster                                            |
| async_tree_none            | 350 ms                                                 | 289 ms: 1.21x faster                                            |
| go                         | 141 ms                                                 | 119 ms: 1.18x faster                                            |
| async_tree_none_tg         | 319 ms                                                 | 277 ms: 1.15x faster                                            |
| deepcopy_memo              | 38.4 us                                                | 34.0 us: 1.13x faster                                           |
| deepcopy                   | 354 us                                                 | 316 us: 1.12x faster                                            |
| regex_v8                   | 26.9 ms                                                | 24.0 ms: 1.12x faster                                           |
| regex_dna                  | 220 ms                                                 | 197 ms: 1.12x faster                                            |
| async_generators           | 433 ms                                                 | 413 ms: 1.05x faster                                            |
| float                      | 78.7 ms                                                | 75.4 ms: 1.04x faster                                           |
| dulwich_log                | 64.6 ms                                                | 63.5 ms: 1.02x faster                                           |
| pyflate                    | 470 ms                                                 | 464 ms: 1.01x faster                                            |
| spectral_norm              | 113 ms                                                 | 113 ms: 1.00x faster                                            |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                            |
| k_core                     | 2.37 sec                                               | 2.41 sec: 1.02x slower                                          |
| html5lib                   | 63.4 ms                                                | 64.7 ms: 1.02x slower                                           |
| deepcopy_reduce            | 3.24 us                                                | 3.33 us: 1.03x slower                                           |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                           |
| tomli_loads                | 2.12 sec                                               | 2.21 sec: 1.05x slower                                          |
| gc_traversal               | 4.90 ms                                                | 5.14 ms: 1.05x slower                                           |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 602 ms: 1.05x slower                                            |
| pycparser                  | 1.20 sec                                               | 1.26 sec: 1.05x slower                                          |
| xml_etree_parse            | 154 ms                                                 | 163 ms: 1.05x slower                                            |
| sympy_integrate            | 19.8 ms                                                | 20.9 ms: 1.06x slower                                           |
| python_startup_no_site     | 7.00 ms                                                | 7.42 ms: 1.06x slower                                           |
| pathlib                    | 17.4 ms                                                | 18.4 ms: 1.06x slower                                           |
| meteor_contest             | 108 ms                                                 | 116 ms: 1.07x slower                                            |
| create_gc_cycles           | 2.45 ms                                                | 2.64 ms: 1.08x slower                                           |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 591 ms: 1.09x slower                                            |
| regex_compile              | 132 ms                                                 | 144 ms: 1.09x slower                                            |
| sphinx                     | 1.03 sec                                               | 1.12 sec: 1.09x slower                                          |
| sqlite_synth               | 2.90 us                                                | 3.16 us: 1.09x slower                                           |
| shortest_path              | 487 ms                                                 | 532 ms: 1.09x slower                                            |
| hexiom                     | 6.08 ms                                                | 6.64 ms: 1.09x slower                                           |
| scimark_sor                | 122 ms                                                 | 134 ms: 1.10x slower                                            |
| scimark_fft                | 367 ms                                                 | 403 ms: 1.10x slower                                            |
| pidigits                   | 186 ms                                                 | 205 ms: 1.10x slower                                            |
| 2to3                       | 266 ms                                                 | 292 ms: 1.10x slower                                            |
| connected_components       | 447 ms                                                 | 492 ms: 1.10x slower                                            |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.55 ms: 1.10x slower                                           |
| docutils                   | 2.58 sec                                               | 2.85 sec: 1.10x slower                                          |
| xml_etree_iterparse        | 101 ms                                                 | 112 ms: 1.11x slower                                            |
| djangocms                  | 22.3 us                                                | 24.8 us: 1.11x slower                                           |
| sympy_sum                  | 150 ms                                                 | 167 ms: 1.11x slower                                            |
| sympy_str                  | 273 ms                                                 | 308 ms: 1.13x slower                                            |
| genshi_xml                 | 50.5 ms                                                | 57.2 ms: 1.13x slower                                           |
| genshi_text                | 22.6 ms                                                | 25.7 ms: 1.14x slower                                           |
| bpe_tokeniser              | 4.69 sec                                               | 5.32 sec: 1.14x slower                                          |
| telco                      | 8.40 ms                                                | 9.55 ms: 1.14x slower                                           |
| richards                   | 47.5 ms                                                | 54.2 ms: 1.14x slower                                           |
| generators                 | 28.8 ms                                                | 32.9 ms: 1.14x slower                                           |
| json                       | 5.32 ms                                                | 6.09 ms: 1.14x slower                                           |
| crypto_pyaes               | 74.7 ms                                                | 85.5 ms: 1.14x slower                                           |
| scimark_monte_carlo        | 66.8 ms                                                | 76.7 ms: 1.15x slower                                           |
| richards_super             | 53.7 ms                                                | 62.0 ms: 1.15x slower                                           |
| scimark_lu                 | 114 ms                                                 | 133 ms: 1.17x slower                                            |
| comprehensions             | 16.5 us                                                | 19.3 us: 1.17x slower                                           |
| sympy_expand               | 456 ms                                                 | 538 ms: 1.18x slower                                            |
| chaos                      | 58.0 ms                                                | 68.6 ms: 1.18x slower                                           |
| thrift                     | 800 us                                                 | 957 us: 1.20x slower                                            |
| unpickle_pure_python       | 213 us                                                 | 257 us: 1.21x slower                                            |
| deltablue                  | 3.19 ms                                                | 3.86 ms: 1.21x slower                                           |
| nbody                      | 87.7 ms                                                | 106 ms: 1.21x slower                                            |
| coroutines                 | 22.2 ms                                                | 26.9 ms: 1.21x slower                                           |
| fannkuch                   | 394 ms                                                 | 479 ms: 1.22x slower                                            |
| nqueens                    | 80.9 ms                                                | 98.6 ms: 1.22x slower                                           |
| raytrace                   | 262 ms                                                 | 321 ms: 1.23x slower                                            |
| pprint_pformat             | 1.48 sec                                               | 1.82 sec: 1.23x slower                                          |
| xml_etree_process          | 60.5 ms                                                | 74.5 ms: 1.23x slower                                           |
| typing_runtime_protocols   | 160 us                                                 | 198 us: 1.23x slower                                            |
| pprint_safe_repr           | 727 ms                                                 | 898 ms: 1.24x slower                                            |
| pickle_pure_python         | 302 us                                                 | 376 us: 1.24x slower                                            |
| coverage                   | 82.8 ms                                                | 103 ms: 1.24x slower                                            |
| xml_etree_generate         | 86.8 ms                                                | 108 ms: 1.25x slower                                            |
| json_loads                 | 27.2 us                                                | 34.1 us: 1.25x slower                                           |
| many_optionals             | 857 us                                                 | 1.08 ms: 1.26x slower                                           |
| mako                       | 10.7 ms                                                | 13.6 ms: 1.28x slower                                           |
| django_template            | 31.7 ms                                                | 40.9 ms: 1.29x slower                                           |
| logging_simple             | 5.65 us                                                | 7.46 us: 1.32x slower                                           |
| json_dumps                 | 10.1 ms                                                | 13.5 ms: 1.33x slower                                           |
| logging_format             | 6.23 us                                                | 8.40 us: 1.35x slower                                           |
| subparsers                 | 15.5 ms                                                | 28.0 ms: 1.81x slower                                           |
| logging_silent             | 101 ns                                                 | 622 ns: 6.16x slower                                            |
| Geometric mean             | (ref)                                                  | 1.10x slower                                                    |

Benchmark hidden because not significant (1): pylint
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250618-3.15.0a0-4fbfba2/bm-20250618-linux-x86_64-mdboom-faster_pprint3-3.15.0a0-4fbfba2.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.075x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: 1.05x