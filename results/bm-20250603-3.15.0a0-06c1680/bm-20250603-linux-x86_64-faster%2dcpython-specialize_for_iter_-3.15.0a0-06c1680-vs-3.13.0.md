# Results vs. 3.13.0

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: linux-x86_64
- commit hash: 06c1680
- commit date: 2025-06-03
- overall geometric mean: 1.043x slower
- HPT reliability: 98.62%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 256 ms: 1.04x faster                                                            |
| html5lib       | 63.4 ms                                                | 60.9 ms: 1.04x faster                                                           |
| sphinx         | 1.03 sec                                               | 1.00 sec: 1.03x faster                                                          |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.46x faster                                                            |
| async_tree_io              | 838 ms                                                 | 598 ms: 1.40x faster                                                            |
| async_tree_io_tg           | 861 ms                                                 | 615 ms: 1.40x faster                                                            |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                            |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.35x faster                                                            |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                            |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 505 ms: 1.13x faster                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 497 ms: 1.09x faster                                                            |
| async_generators           | 433 ms                                                 | 412 ms: 1.05x faster                                                            |
| coroutines                 | 22.2 ms                                                | 25.6 ms: 1.15x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 73.2 ms: 1.07x faster                                                           |
| pidigits       | 186 ms                                                 | 192 ms: 1.03x slower                                                            |
| nbody          | 87.7 ms                                                | 102 ms: 1.16x slower                                                            |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.2 ms: 1.16x faster                                                           |
| regex_effbot   | 3.77 ms                                                | 3.26 ms: 1.16x faster                                                           |
| regex_dna      | 220 ms                                                 | 205 ms: 1.07x faster                                                            |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 142 ms: 1.09x faster                                                            |
| tomli_loads          | 2.12 sec                                               | 2.03 sec: 1.04x faster                                                          |
| xml_etree_iterparse  | 101 ms                                                 | 99.3 ms: 1.02x faster                                                           |
| xml_etree_generate   | 86.8 ms                                                | 85.6 ms: 1.01x faster                                                           |
| unpickle_pure_python | 213 us                                                 | 222 us: 1.04x slower                                                            |
| json_loads           | 27.2 us                                                | 28.4 us: 1.05x slower                                                           |
| pickle_pure_python   | 302 us                                                 | 322 us: 1.06x slower                                                            |
| json_dumps           | 10.1 ms                                                | 11.0 ms: 1.08x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                           |
| python_startup_no_site | 7.00 ms                                                | 6.92 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.6 ms: 1.05x faster                                                           |
| genshi_xml      | 50.5 ms                                                | 49.5 ms: 1.02x faster                                                           |
| django_template | 31.7 ms                                                | 32.3 ms: 1.02x slower                                                           |
| mako            | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.24 sec: 2.06x faster                                                          |
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.46x faster                                                            |
| async_tree_io              | 838 ms                                                 | 598 ms: 1.40x faster                                                            |
| async_tree_io_tg           | 861 ms                                                 | 615 ms: 1.40x faster                                                            |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                            |
| deepcopy                   | 354 us                                                 | 257 us: 1.38x faster                                                            |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.35x faster                                                            |
| deepcopy_memo              | 38.4 us                                                | 29.4 us: 1.31x faster                                                           |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                            |
| go                         | 141 ms                                                 | 113 ms: 1.24x faster                                                            |
| deepcopy_reduce            | 3.24 us                                                | 2.72 us: 1.19x faster                                                           |
| regex_v8                   | 26.9 ms                                                | 23.2 ms: 1.16x faster                                                           |
| regex_effbot               | 3.77 ms                                                | 3.26 ms: 1.16x faster                                                           |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 505 ms: 1.13x faster                                                            |
| pylint                     | 312 ms                                                 | 278 ms: 1.12x faster                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 497 ms: 1.09x faster                                                            |
| richards                   | 47.5 ms                                                | 43.5 ms: 1.09x faster                                                           |
| xml_etree_parse            | 154 ms                                                 | 142 ms: 1.09x faster                                                            |
| richards_super             | 53.7 ms                                                | 49.5 ms: 1.09x faster                                                           |
| dulwich_log                | 64.6 ms                                                | 59.6 ms: 1.08x faster                                                           |
| float                      | 78.7 ms                                                | 73.2 ms: 1.07x faster                                                           |
| regex_dna                  | 220 ms                                                 | 205 ms: 1.07x faster                                                            |
| async_generators           | 433 ms                                                 | 412 ms: 1.05x faster                                                            |
| pyflate                    | 470 ms                                                 | 446 ms: 1.05x faster                                                            |
| telco                      | 8.40 ms                                                | 7.99 ms: 1.05x faster                                                           |
| genshi_text                | 22.6 ms                                                | 21.6 ms: 1.05x faster                                                           |
| sympy_integrate            | 19.8 ms                                                | 19.0 ms: 1.04x faster                                                           |
| tomli_loads                | 2.12 sec                                               | 2.03 sec: 1.04x faster                                                          |
| bpe_tokeniser              | 4.69 sec                                               | 4.50 sec: 1.04x faster                                                          |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                           |
| 2to3                       | 266 ms                                                 | 256 ms: 1.04x faster                                                            |
| html5lib                   | 63.4 ms                                                | 60.9 ms: 1.04x faster                                                           |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.04x faster                                                          |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                            |
| sphinx                     | 1.03 sec                                               | 1.00 sec: 1.03x faster                                                          |
| spectral_norm              | 113 ms                                                 | 111 ms: 1.02x faster                                                            |
| sympy_str                  | 273 ms                                                 | 267 ms: 1.02x faster                                                            |
| json                       | 5.32 ms                                                | 5.21 ms: 1.02x faster                                                           |
| comprehensions             | 16.5 us                                                | 16.2 us: 1.02x faster                                                           |
| xml_etree_iterparse        | 101 ms                                                 | 99.3 ms: 1.02x faster                                                           |
| genshi_xml                 | 50.5 ms                                                | 49.5 ms: 1.02x faster                                                           |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.02x faster                                                          |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.02x faster                                                            |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.01x faster                                                            |
| xml_etree_generate         | 86.8 ms                                                | 85.6 ms: 1.01x faster                                                           |
| sqlite_synth               | 2.90 us                                                | 2.87 us: 1.01x faster                                                           |
| python_startup_no_site     | 7.00 ms                                                | 6.92 ms: 1.01x faster                                                           |
| meteor_contest             | 108 ms                                                 | 108 ms: 1.00x faster                                                            |
| sympy_expand               | 456 ms                                                 | 455 ms: 1.00x faster                                                            |
| hexiom                     | 6.08 ms                                                | 6.11 ms: 1.01x slower                                                           |
| nqueens                    | 80.9 ms                                                | 81.4 ms: 1.01x slower                                                           |
| gc_traversal               | 4.90 ms                                                | 4.93 ms: 1.01x slower                                                           |
| pathlib                    | 17.4 ms                                                | 17.6 ms: 1.01x slower                                                           |
| shortest_path              | 487 ms                                                 | 494 ms: 1.02x slower                                                            |
| crypto_pyaes               | 74.7 ms                                                | 76.2 ms: 1.02x slower                                                           |
| django_template            | 31.7 ms                                                | 32.3 ms: 1.02x slower                                                           |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.14 ms: 1.02x slower                                                           |
| pidigits                   | 186 ms                                                 | 192 ms: 1.03x slower                                                            |
| chaos                      | 58.0 ms                                                | 60.2 ms: 1.04x slower                                                           |
| scimark_lu                 | 114 ms                                                 | 119 ms: 1.04x slower                                                            |
| scimark_fft                | 367 ms                                                 | 382 ms: 1.04x slower                                                            |
| unpickle_pure_python       | 213 us                                                 | 222 us: 1.04x slower                                                            |
| connected_components       | 447 ms                                                 | 466 ms: 1.04x slower                                                            |
| raytrace                   | 262 ms                                                 | 273 ms: 1.04x slower                                                            |
| scimark_monte_carlo        | 66.8 ms                                                | 69.9 ms: 1.05x slower                                                           |
| json_loads                 | 27.2 us                                                | 28.4 us: 1.05x slower                                                           |
| generators                 | 28.8 ms                                                | 30.2 ms: 1.05x slower                                                           |
| create_gc_cycles           | 2.45 ms                                                | 2.59 ms: 1.06x slower                                                           |
| typing_runtime_protocols   | 160 us                                                 | 170 us: 1.06x slower                                                            |
| mako                       | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                           |
| pickle_pure_python         | 302 us                                                 | 322 us: 1.06x slower                                                            |
| fannkuch                   | 394 ms                                                 | 419 ms: 1.07x slower                                                            |
| json_dumps                 | 10.1 ms                                                | 11.0 ms: 1.08x slower                                                           |
| logging_simple             | 5.65 us                                                | 6.15 us: 1.09x slower                                                           |
| logging_format             | 6.23 us                                                | 6.82 us: 1.09x slower                                                           |
| deltablue                  | 3.19 ms                                                | 3.54 ms: 1.11x slower                                                           |
| many_optionals             | 857 us                                                 | 953 us: 1.11x slower                                                            |
| pprint_safe_repr           | 727 ms                                                 | 811 ms: 1.12x slower                                                            |
| pprint_pformat             | 1.48 sec                                               | 1.65 sec: 1.12x slower                                                          |
| coroutines                 | 22.2 ms                                                | 25.6 ms: 1.15x slower                                                           |
| nbody                      | 87.7 ms                                                | 102 ms: 1.16x slower                                                            |
| subparsers                 | 15.5 ms                                                | 23.6 ms: 1.53x slower                                                           |
| logging_silent             | 101 ns                                                 | 478 ns: 4.73x slower                                                            |
| coverage                   | 82.8 ms                                                | 442 ms: 5.34x slower                                                            |
| thrift                     | 800 us                                                 | 149 ms: 185.72x slower                                                          |
| Geometric mean             | (ref)                                                  | 1.06x slower                                                                    |

Benchmark hidden because not significant (3): xml_etree_process, docutils, asyncio_websockets
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250603-3.15.0a0-06c1680/bm-20250603-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.043x slower

# HPT report

- Reliability score: 98.62% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x