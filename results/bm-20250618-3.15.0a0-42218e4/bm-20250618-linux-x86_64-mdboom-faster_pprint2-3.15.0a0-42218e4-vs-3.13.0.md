# Results vs. 3.13.0

- fork: mdboom
- ref: faster_pprint2
- machine: linux-x86_64
- commit hash: 42218e4
- commit date: 2025-06-18
- overall geometric mean: 1.044x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 255 ms: 1.04x faster                                            |
| html5lib       | 63.4 ms                                                | 61.9 ms: 1.02x faster                                           |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                          |
| Geometric mean | (ref)                                                  | 1.02x faster                                                    |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 308 ms: 1.50x faster                                            |
| async_tree_io              | 838 ms                                                 | 598 ms: 1.40x faster                                            |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.39x faster                                            |
| async_tree_io_tg           | 861 ms                                                 | 626 ms: 1.37x faster                                            |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                            |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.29x faster                                            |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 497 ms: 1.15x faster                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 487 ms: 1.12x faster                                            |
| async_generators           | 433 ms                                                 | 409 ms: 1.06x faster                                            |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                            |
| coroutines                 | 22.2 ms                                                | 25.0 ms: 1.13x slower                                           |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 78.7 ms                                                | 72.9 ms: 1.08x faster                                           |
| pidigits       | 186 ms                                                 | 192 ms: 1.03x slower                                            |
| nbody          | 87.7 ms                                                | 97.8 ms: 1.12x slower                                           |
| Geometric mean | (ref)                                                  | 1.02x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.0 ms: 1.17x faster                                           |
| regex_effbot   | 3.77 ms                                                | 3.31 ms: 1.14x faster                                           |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                            |
| regex_dna      | 220 ms                                                 | 215 ms: 1.02x faster                                            |
| Geometric mean | (ref)                                                  | 1.09x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                            |
| tomli_loads          | 2.12 sec                                               | 2.03 sec: 1.04x faster                                          |
| xml_etree_iterparse  | 101 ms                                                 | 98.2 ms: 1.03x faster                                           |
| xml_etree_generate   | 86.8 ms                                                | 85.2 ms: 1.02x faster                                           |
| xml_etree_process    | 60.5 ms                                                | 59.9 ms: 1.01x faster                                           |
| unpickle_pure_python | 213 us                                                 | 218 us: 1.02x slower                                            |
| json_loads           | 27.2 us                                                | 28.2 us: 1.04x slower                                           |
| pickle_pure_python   | 302 us                                                 | 323 us: 1.07x slower                                            |
| json_dumps           | 10.1 ms                                                | 11.3 ms: 1.11x slower                                           |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                           |
| python_startup_no_site | 7.00 ms                                                | 6.92 ms: 1.01x faster                                           |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.4 ms: 1.06x faster                                           |
| genshi_xml      | 50.5 ms                                                | 48.8 ms: 1.03x faster                                           |
| django_template | 31.7 ms                                                | 32.3 ms: 1.02x slower                                           |
| mako            | 10.7 ms                                                | 11.7 ms: 1.10x slower                                           |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.22 sec: 2.08x faster                                          |
| async_tree_memoization_tg  | 463 ms                                                 | 308 ms: 1.50x faster                                            |
| async_tree_io              | 838 ms                                                 | 598 ms: 1.40x faster                                            |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.39x faster                                            |
| deepcopy                   | 354 us                                                 | 255 us: 1.39x faster                                            |
| async_tree_io_tg           | 861 ms                                                 | 626 ms: 1.37x faster                                            |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                            |
| deepcopy_memo              | 38.4 us                                                | 29.1 us: 1.32x faster                                           |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.29x faster                                            |
| go                         | 141 ms                                                 | 111 ms: 1.27x faster                                            |
| deepcopy_reduce            | 3.24 us                                                | 2.76 us: 1.17x faster                                           |
| regex_v8                   | 26.9 ms                                                | 23.0 ms: 1.17x faster                                           |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 497 ms: 1.15x faster                                            |
| regex_effbot               | 3.77 ms                                                | 3.31 ms: 1.14x faster                                           |
| pylint                     | 312 ms                                                 | 279 ms: 1.12x faster                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 487 ms: 1.12x faster                                            |
| pyflate                    | 470 ms                                                 | 423 ms: 1.11x faster                                            |
| richards                   | 47.5 ms                                                | 42.9 ms: 1.11x faster                                           |
| dulwich_log                | 64.6 ms                                                | 59.1 ms: 1.09x faster                                           |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                            |
| richards_super             | 53.7 ms                                                | 49.3 ms: 1.09x faster                                           |
| float                      | 78.7 ms                                                | 72.9 ms: 1.08x faster                                           |
| spectral_norm              | 113 ms                                                 | 107 ms: 1.06x faster                                            |
| async_generators           | 433 ms                                                 | 409 ms: 1.06x faster                                            |
| genshi_text                | 22.6 ms                                                | 21.4 ms: 1.06x faster                                           |
| telco                      | 8.40 ms                                                | 7.96 ms: 1.05x faster                                           |
| sympy_integrate            | 19.8 ms                                                | 18.9 ms: 1.05x faster                                           |
| thrift                     | 800 us                                                 | 766 us: 1.04x faster                                            |
| tomli_loads                | 2.12 sec                                               | 2.03 sec: 1.04x faster                                          |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                            |
| 2to3                       | 266 ms                                                 | 255 ms: 1.04x faster                                            |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                           |
| meteor_contest             | 108 ms                                                 | 104 ms: 1.04x faster                                            |
| bpe_tokeniser              | 4.69 sec                                               | 4.52 sec: 1.04x faster                                          |
| genshi_xml                 | 50.5 ms                                                | 48.8 ms: 1.03x faster                                           |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.03x faster                                          |
| sympy_str                  | 273 ms                                                 | 264 ms: 1.03x faster                                            |
| xml_etree_iterparse        | 101 ms                                                 | 98.2 ms: 1.03x faster                                           |
| json                       | 5.32 ms                                                | 5.17 ms: 1.03x faster                                           |
| comprehensions             | 16.5 us                                                | 16.0 us: 1.03x faster                                           |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.03x faster                                            |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                          |
| pathlib                    | 17.4 ms                                                | 17.0 ms: 1.02x faster                                           |
| regex_dna                  | 220 ms                                                 | 215 ms: 1.02x faster                                            |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                          |
| html5lib                   | 63.4 ms                                                | 61.9 ms: 1.02x faster                                           |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                            |
| xml_etree_generate         | 86.8 ms                                                | 85.2 ms: 1.02x faster                                           |
| hexiom                     | 6.08 ms                                                | 5.97 ms: 1.02x faster                                           |
| sympy_expand               | 456 ms                                                 | 449 ms: 1.02x faster                                            |
| scimark_monte_carlo        | 66.8 ms                                                | 65.9 ms: 1.01x faster                                           |
| python_startup_no_site     | 7.00 ms                                                | 6.92 ms: 1.01x faster                                           |
| xml_etree_process          | 60.5 ms                                                | 59.9 ms: 1.01x faster                                           |
| scimark_fft                | 367 ms                                                 | 364 ms: 1.01x faster                                            |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                            |
| pprint_safe_repr           | 727 ms                                                 | 729 ms: 1.00x slower                                            |
| pprint_pformat             | 1.48 sec                                               | 1.49 sec: 1.01x slower                                          |
| crypto_pyaes               | 74.7 ms                                                | 75.6 ms: 1.01x slower                                           |
| django_template            | 31.7 ms                                                | 32.3 ms: 1.02x slower                                           |
| unpickle_pure_python       | 213 us                                                 | 218 us: 1.02x slower                                            |
| scimark_lu                 | 114 ms                                                 | 118 ms: 1.03x slower                                            |
| pidigits                   | 186 ms                                                 | 192 ms: 1.03x slower                                            |
| gc_traversal               | 4.90 ms                                                | 5.06 ms: 1.03x slower                                           |
| generators                 | 28.8 ms                                                | 29.8 ms: 1.04x slower                                           |
| raytrace                   | 262 ms                                                 | 271 ms: 1.04x slower                                            |
| json_loads                 | 27.2 us                                                | 28.2 us: 1.04x slower                                           |
| coverage                   | 82.8 ms                                                | 87.1 ms: 1.05x slower                                           |
| chaos                      | 58.0 ms                                                | 61.1 ms: 1.05x slower                                           |
| typing_runtime_protocols   | 160 us                                                 | 169 us: 1.05x slower                                            |
| create_gc_cycles           | 2.45 ms                                                | 2.59 ms: 1.06x slower                                           |
| fannkuch                   | 394 ms                                                 | 416 ms: 1.06x slower                                            |
| pickle_pure_python         | 302 us                                                 | 323 us: 1.07x slower                                            |
| connected_components       | 447 ms                                                 | 481 ms: 1.08x slower                                            |
| shortest_path              | 487 ms                                                 | 526 ms: 1.08x slower                                            |
| deltablue                  | 3.19 ms                                                | 3.47 ms: 1.09x slower                                           |
| mako                       | 10.7 ms                                                | 11.7 ms: 1.10x slower                                           |
| logging_format             | 6.23 us                                                | 6.87 us: 1.10x slower                                           |
| logging_simple             | 5.65 us                                                | 6.24 us: 1.10x slower                                           |
| json_dumps                 | 10.1 ms                                                | 11.3 ms: 1.11x slower                                           |
| nbody                      | 87.7 ms                                                | 97.8 ms: 1.12x slower                                           |
| many_optionals             | 857 us                                                 | 957 us: 1.12x slower                                            |
| coroutines                 | 22.2 ms                                                | 25.0 ms: 1.13x slower                                           |
| subparsers                 | 15.5 ms                                                | 23.6 ms: 1.53x slower                                           |
| logging_silent             | 101 ns                                                 | 469 ns: 4.64x slower                                            |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                    |

Benchmark hidden because not significant (5): djangocms, scimark_sparse_mat_mult, sqlite_synth, docutils, nqueens
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250618-3.15.0a0-42218e4/bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.044x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.06x