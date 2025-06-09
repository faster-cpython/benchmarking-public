# Results vs. 3.13.0

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: linux-x86_64
- commit hash: baf4722
- commit date: 2025-06-09
- overall geometric mean: 1.038x slower
- HPT reliability: 99.55%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250609-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 254 ms: 1.05x faster                                                            |
| html5lib       | 63.4 ms                                                | 61.7 ms: 1.03x faster                                                           |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.03x faster                                                          |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250609-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.46x faster                                                            |
| async_tree_io              | 838 ms                                                 | 595 ms: 1.41x faster                                                            |
| async_tree_io_tg           | 861 ms                                                 | 619 ms: 1.39x faster                                                            |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                            |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.34x faster                                                            |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                            |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 491 ms: 1.17x faster                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 483 ms: 1.13x faster                                                            |
| async_generators           | 433 ms                                                 | 410 ms: 1.06x faster                                                            |
| coroutines                 | 22.2 ms                                                | 24.7 ms: 1.11x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250609-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 73.7 ms: 1.07x faster                                                           |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                            |
| nbody          | 87.7 ms                                                | 96.8 ms: 1.10x slower                                                           |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250609-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.4 ms: 1.15x faster                                                           |
| regex_effbot   | 3.77 ms                                                | 3.29 ms: 1.15x faster                                                           |
| regex_dna      | 220 ms                                                 | 207 ms: 1.06x faster                                                            |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                            |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250609-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 142 ms: 1.08x faster                                                            |
| tomli_loads          | 2.12 sec                                               | 2.03 sec: 1.04x faster                                                          |
| xml_etree_generate   | 86.8 ms                                                | 85.2 ms: 1.02x faster                                                           |
| xml_etree_iterparse  | 101 ms                                                 | 99.4 ms: 1.02x faster                                                           |
| xml_etree_process    | 60.5 ms                                                | 60.1 ms: 1.01x faster                                                           |
| unpickle_pure_python | 213 us                                                 | 220 us: 1.03x slower                                                            |
| json_loads           | 27.2 us                                                | 28.1 us: 1.03x slower                                                           |
| pickle_pure_python   | 302 us                                                 | 318 us: 1.05x slower                                                            |
| json_dumps           | 10.1 ms                                                | 11.0 ms: 1.09x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250609-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.1 ms: 1.04x faster                                                           |
| python_startup_no_site | 7.00 ms                                                | 6.90 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250609-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.0 ms: 1.08x faster                                                           |
| django_template | 31.7 ms                                                | 32.8 ms: 1.03x slower                                                           |
| mako            | 10.7 ms                                                | 11.2 ms: 1.05x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250609-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.07x faster                                                          |
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.46x faster                                                            |
| async_tree_io              | 838 ms                                                 | 595 ms: 1.41x faster                                                            |
| async_tree_io_tg           | 861 ms                                                 | 619 ms: 1.39x faster                                                            |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                            |
| deepcopy                   | 354 us                                                 | 258 us: 1.37x faster                                                            |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.34x faster                                                            |
| deepcopy_memo              | 38.4 us                                                | 29.6 us: 1.30x faster                                                           |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                            |
| go                         | 141 ms                                                 | 112 ms: 1.26x faster                                                            |
| deepcopy_reduce            | 3.24 us                                                | 2.66 us: 1.22x faster                                                           |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 491 ms: 1.17x faster                                                            |
| regex_v8                   | 26.9 ms                                                | 23.4 ms: 1.15x faster                                                           |
| regex_effbot               | 3.77 ms                                                | 3.29 ms: 1.15x faster                                                           |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 483 ms: 1.13x faster                                                            |
| pylint                     | 312 ms                                                 | 279 ms: 1.12x faster                                                            |
| richards                   | 47.5 ms                                                | 43.0 ms: 1.11x faster                                                           |
| pyflate                    | 470 ms                                                 | 430 ms: 1.09x faster                                                            |
| dulwich_log                | 64.6 ms                                                | 59.3 ms: 1.09x faster                                                           |
| richards_super             | 53.7 ms                                                | 49.6 ms: 1.08x faster                                                           |
| xml_etree_parse            | 154 ms                                                 | 142 ms: 1.08x faster                                                            |
| genshi_text                | 22.6 ms                                                | 21.0 ms: 1.08x faster                                                           |
| float                      | 78.7 ms                                                | 73.7 ms: 1.07x faster                                                           |
| regex_dna                  | 220 ms                                                 | 207 ms: 1.06x faster                                                            |
| async_generators           | 433 ms                                                 | 410 ms: 1.06x faster                                                            |
| 2to3                       | 266 ms                                                 | 254 ms: 1.05x faster                                                            |
| tomli_loads                | 2.12 sec                                               | 2.03 sec: 1.04x faster                                                          |
| telco                      | 8.40 ms                                                | 8.05 ms: 1.04x faster                                                           |
| python_startup             | 12.7 ms                                                | 12.1 ms: 1.04x faster                                                           |
| pathlib                    | 17.4 ms                                                | 16.7 ms: 1.04x faster                                                           |
| sympy_integrate            | 19.8 ms                                                | 19.0 ms: 1.04x faster                                                           |
| bpe_tokeniser              | 4.69 sec                                               | 4.52 sec: 1.04x faster                                                          |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                            |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.03x faster                                                          |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.03x faster                                                          |
| html5lib                   | 63.4 ms                                                | 61.7 ms: 1.03x faster                                                           |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.03x faster                                                          |
| comprehensions             | 16.5 us                                                | 16.1 us: 1.02x faster                                                           |
| json                       | 5.32 ms                                                | 5.20 ms: 1.02x faster                                                           |
| spectral_norm              | 113 ms                                                 | 111 ms: 1.02x faster                                                            |
| sympy_str                  | 273 ms                                                 | 267 ms: 1.02x faster                                                            |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                            |
| xml_etree_generate         | 86.8 ms                                                | 85.2 ms: 1.02x faster                                                           |
| xml_etree_iterparse        | 101 ms                                                 | 99.4 ms: 1.02x faster                                                           |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.02x faster                                                            |
| hexiom                     | 6.08 ms                                                | 5.98 ms: 1.02x faster                                                           |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                                            |
| sqlite_synth               | 2.90 us                                                | 2.86 us: 1.01x faster                                                           |
| python_startup_no_site     | 7.00 ms                                                | 6.90 ms: 1.01x faster                                                           |
| sympy_expand               | 456 ms                                                 | 452 ms: 1.01x faster                                                            |
| nqueens                    | 80.9 ms                                                | 80.4 ms: 1.01x faster                                                           |
| xml_etree_process          | 60.5 ms                                                | 60.1 ms: 1.01x faster                                                           |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                                            |
| crypto_pyaes               | 74.7 ms                                                | 75.7 ms: 1.01x slower                                                           |
| scimark_monte_carlo        | 66.8 ms                                                | 68.1 ms: 1.02x slower                                                           |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.15 ms: 1.02x slower                                                           |
| generators                 | 28.8 ms                                                | 29.6 ms: 1.03x slower                                                           |
| unpickle_pure_python       | 213 us                                                 | 220 us: 1.03x slower                                                            |
| chaos                      | 58.0 ms                                                | 60.0 ms: 1.03x slower                                                           |
| json_loads                 | 27.2 us                                                | 28.1 us: 1.03x slower                                                           |
| django_template            | 31.7 ms                                                | 32.8 ms: 1.03x slower                                                           |
| gc_traversal               | 4.90 ms                                                | 5.07 ms: 1.04x slower                                                           |
| scimark_lu                 | 114 ms                                                 | 119 ms: 1.04x slower                                                            |
| raytrace                   | 262 ms                                                 | 272 ms: 1.04x slower                                                            |
| scimark_fft                | 367 ms                                                 | 382 ms: 1.04x slower                                                            |
| shortest_path              | 487 ms                                                 | 507 ms: 1.04x slower                                                            |
| fannkuch                   | 394 ms                                                 | 413 ms: 1.05x slower                                                            |
| mako                       | 10.7 ms                                                | 11.2 ms: 1.05x slower                                                           |
| pickle_pure_python         | 302 us                                                 | 318 us: 1.05x slower                                                            |
| typing_runtime_protocols   | 160 us                                                 | 169 us: 1.05x slower                                                            |
| create_gc_cycles           | 2.45 ms                                                | 2.58 ms: 1.05x slower                                                           |
| connected_components       | 447 ms                                                 | 475 ms: 1.06x slower                                                            |
| logging_simple             | 5.65 us                                                | 6.10 us: 1.08x slower                                                           |
| logging_format             | 6.23 us                                                | 6.78 us: 1.09x slower                                                           |
| json_dumps                 | 10.1 ms                                                | 11.0 ms: 1.09x slower                                                           |
| nbody                      | 87.7 ms                                                | 96.8 ms: 1.10x slower                                                           |
| deltablue                  | 3.19 ms                                                | 3.54 ms: 1.11x slower                                                           |
| pprint_pformat             | 1.48 sec                                               | 1.64 sec: 1.11x slower                                                          |
| pprint_safe_repr           | 727 ms                                                 | 806 ms: 1.11x slower                                                            |
| coroutines                 | 22.2 ms                                                | 24.7 ms: 1.11x slower                                                           |
| many_optionals             | 857 us                                                 | 962 us: 1.12x slower                                                            |
| subparsers                 | 15.5 ms                                                | 23.7 ms: 1.54x slower                                                           |
| logging_silent             | 101 ns                                                 | 471 ns: 4.66x slower                                                            |
| coverage                   | 82.8 ms                                                | 421 ms: 5.08x slower                                                            |
| thrift                     | 800 us                                                 | 148 ms: 184.76x slower                                                          |
| Geometric mean             | (ref)                                                  | 1.06x slower                                                                    |

Benchmark hidden because not significant (3): genshi_xml, docutils, asyncio_websockets
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250609-3.15.0a0-baf4722/bm-20250609-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.038x slower

# HPT report

- Reliability score: 99.55% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x