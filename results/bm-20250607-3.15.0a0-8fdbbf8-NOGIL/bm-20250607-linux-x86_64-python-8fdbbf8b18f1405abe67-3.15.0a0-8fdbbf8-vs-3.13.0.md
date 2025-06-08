# Results vs. 3.13.0

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: linux-x86_64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.208x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x slower
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 339 ms: 1.27x slower                                                  |
| docutils       | 2.58 sec                                               | 3.14 sec: 1.21x slower                                                |
| html5lib       | 63.4 ms                                                | 75.5 ms: 1.19x slower                                                 |
| sphinx         | 1.03 sec                                               | 1.26 sec: 1.22x slower                                                |
| Geometric mean | (ref)                                                  | 1.22x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 861 ms                                                 | 603 ms: 1.43x faster                                                  |
| async_tree_memoization_tg  | 463 ms                                                 | 340 ms: 1.36x faster                                                  |
| async_tree_io              | 838 ms                                                 | 642 ms: 1.30x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 262 ms: 1.22x faster                                                  |
| async_tree_none            | 350 ms                                                 | 301 ms: 1.16x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 381 ms: 1.15x faster                                                  |
| async_generators           | 433 ms                                                 | 455 ms: 1.05x slower                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 582 ms: 1.07x slower                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 626 ms: 1.09x slower                                                  |
| coroutines                 | 22.2 ms                                                | 29.1 ms: 1.31x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 82.0 ms: 1.04x slower                                                 |
| pidigits       | 186 ms                                                 | 201 ms: 1.08x slower                                                  |
| nbody          | 87.7 ms                                                | 154 ms: 1.76x slower                                                  |
| Geometric mean | (ref)                                                  | 1.26x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 2.97 ms: 1.27x faster                                                 |
| regex_dna      | 220 ms                                                 | 192 ms: 1.15x faster                                                  |
| regex_v8       | 26.9 ms                                                | 23.7 ms: 1.13x faster                                                 |
| regex_compile  | 132 ms                                                 | 172 ms: 1.31x slower                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_iterparse  | 101 ms                                                 | 108 ms: 1.06x slower                                                  |
| xml_etree_parse      | 154 ms                                                 | 164 ms: 1.06x slower                                                  |
| tomli_loads          | 2.12 sec                                               | 2.63 sec: 1.24x slower                                                |
| json_loads           | 27.2 us                                                | 37.7 us: 1.39x slower                                                 |
| pickle_pure_python   | 302 us                                                 | 423 us: 1.40x slower                                                  |
| unpickle_pure_python | 213 us                                                 | 301 us: 1.41x slower                                                  |
| xml_etree_process    | 60.5 ms                                                | 86.8 ms: 1.43x slower                                                 |
| xml_etree_generate   | 86.8 ms                                                | 125 ms: 1.44x slower                                                  |
| json_dumps           | 10.1 ms                                                | 14.9 ms: 1.47x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.31x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 17.1 ms: 1.35x slower                                                 |
| python_startup_no_site | 7.00 ms                                                | 9.97 ms: 1.42x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.39x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 50.5 ms                                                | 76.2 ms: 1.51x slower                                                 |
| genshi_text     | 22.6 ms                                                | 35.2 ms: 1.56x slower                                                 |
| django_template | 31.7 ms                                                | 53.2 ms: 1.68x slower                                                 |
| mako            | 10.7 ms                                                | 18.6 ms: 1.74x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.62x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| gc_traversal               | 4.90 ms                                                | 2.48 ms: 1.97x faster                                                 |
| mdp                        | 2.54 sec                                               | 1.74 sec: 1.46x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 603 ms: 1.43x faster                                                  |
| async_tree_memoization_tg  | 463 ms                                                 | 340 ms: 1.36x faster                                                  |
| create_gc_cycles           | 2.45 ms                                                | 1.86 ms: 1.32x faster                                                 |
| async_tree_io              | 838 ms                                                 | 642 ms: 1.30x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 2.97 ms: 1.27x faster                                                 |
| async_tree_none_tg         | 319 ms                                                 | 262 ms: 1.22x faster                                                  |
| async_tree_none            | 350 ms                                                 | 301 ms: 1.16x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 381 ms: 1.15x faster                                                  |
| regex_dna                  | 220 ms                                                 | 192 ms: 1.15x faster                                                  |
| regex_v8                   | 26.9 ms                                                | 23.7 ms: 1.13x faster                                                 |
| float                      | 78.7 ms                                                | 82.0 ms: 1.04x slower                                                 |
| async_generators           | 433 ms                                                 | 455 ms: 1.05x slower                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 108 ms: 1.06x slower                                                  |
| xml_etree_parse            | 154 ms                                                 | 164 ms: 1.06x slower                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 582 ms: 1.07x slower                                                  |
| deepcopy_memo              | 38.4 us                                                | 41.2 us: 1.07x slower                                                 |
| pidigits                   | 186 ms                                                 | 201 ms: 1.08x slower                                                  |
| pycparser                  | 1.20 sec                                               | 1.30 sec: 1.08x slower                                                |
| deepcopy                   | 354 us                                                 | 383 us: 1.08x slower                                                  |
| k_core                     | 2.37 sec                                               | 2.58 sec: 1.09x slower                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 626 ms: 1.09x slower                                                  |
| sqlite_synth               | 2.90 us                                                | 3.24 us: 1.12x slower                                                 |
| dulwich_log                | 64.6 ms                                                | 72.4 ms: 1.12x slower                                                 |
| pathlib                    | 17.4 ms                                                | 19.7 ms: 1.13x slower                                                 |
| pylint                     | 312 ms                                                 | 357 ms: 1.14x slower                                                  |
| pyflate                    | 470 ms                                                 | 549 ms: 1.17x slower                                                  |
| html5lib                   | 63.4 ms                                                | 75.5 ms: 1.19x slower                                                 |
| shortest_path              | 487 ms                                                 | 585 ms: 1.20x slower                                                  |
| generators                 | 28.8 ms                                                | 34.8 ms: 1.21x slower                                                 |
| docutils                   | 2.58 sec                                               | 3.14 sec: 1.21x slower                                                |
| connected_components       | 447 ms                                                 | 545 ms: 1.22x slower                                                  |
| sphinx                     | 1.03 sec                                               | 1.26 sec: 1.22x slower                                                |
| json                       | 5.32 ms                                                | 6.54 ms: 1.23x slower                                                 |
| tomli_loads                | 2.12 sec                                               | 2.63 sec: 1.24x slower                                                |
| meteor_contest             | 108 ms                                                 | 135 ms: 1.25x slower                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 5.88 sec: 1.25x slower                                                |
| sympy_integrate            | 19.8 ms                                                | 25.2 ms: 1.27x slower                                                 |
| spectral_norm              | 113 ms                                                 | 144 ms: 1.27x slower                                                  |
| 2to3                       | 266 ms                                                 | 339 ms: 1.27x slower                                                  |
| deepcopy_reduce            | 3.24 us                                                | 4.13 us: 1.27x slower                                                 |
| hexiom                     | 6.08 ms                                                | 7.87 ms: 1.29x slower                                                 |
| scimark_sor                | 122 ms                                                 | 158 ms: 1.30x slower                                                  |
| regex_compile              | 132 ms                                                 | 172 ms: 1.31x slower                                                  |
| coroutines                 | 22.2 ms                                                | 29.1 ms: 1.31x slower                                                 |
| sympy_sum                  | 150 ms                                                 | 198 ms: 1.32x slower                                                  |
| scimark_fft                | 367 ms                                                 | 485 ms: 1.32x slower                                                  |
| sympy_str                  | 273 ms                                                 | 369 ms: 1.35x slower                                                  |
| python_startup             | 12.7 ms                                                | 17.1 ms: 1.35x slower                                                 |
| comprehensions             | 16.5 us                                                | 22.6 us: 1.37x slower                                                 |
| sympy_expand               | 456 ms                                                 | 627 ms: 1.37x slower                                                  |
| json_loads                 | 27.2 us                                                | 37.7 us: 1.39x slower                                                 |
| pickle_pure_python         | 302 us                                                 | 423 us: 1.40x slower                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 7.09 ms: 1.41x slower                                                 |
| unpickle_pure_python       | 213 us                                                 | 301 us: 1.41x slower                                                  |
| telco                      | 8.40 ms                                                | 11.9 ms: 1.41x slower                                                 |
| python_startup_no_site     | 7.00 ms                                                | 9.97 ms: 1.42x slower                                                 |
| chaos                      | 58.0 ms                                                | 82.7 ms: 1.42x slower                                                 |
| richards                   | 47.5 ms                                                | 68.0 ms: 1.43x slower                                                 |
| xml_etree_process          | 60.5 ms                                                | 86.8 ms: 1.43x slower                                                 |
| xml_etree_generate         | 86.8 ms                                                | 125 ms: 1.44x slower                                                  |
| scimark_lu                 | 114 ms                                                 | 165 ms: 1.44x slower                                                  |
| many_optionals             | 857 us                                                 | 1.24 ms: 1.45x slower                                                 |
| deltablue                  | 3.19 ms                                                | 4.63 ms: 1.45x slower                                                 |
| nqueens                    | 80.9 ms                                                | 118 ms: 1.46x slower                                                  |
| richards_super             | 53.7 ms                                                | 78.9 ms: 1.47x slower                                                 |
| json_dumps                 | 10.1 ms                                                | 14.9 ms: 1.47x slower                                                 |
| raytrace                   | 262 ms                                                 | 388 ms: 1.49x slower                                                  |
| fannkuch                   | 394 ms                                                 | 588 ms: 1.49x slower                                                  |
| crypto_pyaes               | 74.7 ms                                                | 112 ms: 1.50x slower                                                  |
| thrift                     | 800 us                                                 | 1.21 ms: 1.51x slower                                                 |
| genshi_xml                 | 50.5 ms                                                | 76.2 ms: 1.51x slower                                                 |
| scimark_monte_carlo        | 66.8 ms                                                | 101 ms: 1.52x slower                                                  |
| typing_runtime_protocols   | 160 us                                                 | 244 us: 1.52x slower                                                  |
| genshi_text                | 22.6 ms                                                | 35.2 ms: 1.56x slower                                                 |
| coverage                   | 82.8 ms                                                | 132 ms: 1.59x slower                                                  |
| logging_simple             | 5.65 us                                                | 9.10 us: 1.61x slower                                                 |
| pprint_safe_repr           | 727 ms                                                 | 1.17 sec: 1.61x slower                                                |
| pprint_pformat             | 1.48 sec                                               | 2.40 sec: 1.63x slower                                                |
| logging_format             | 6.23 us                                                | 10.2 us: 1.64x slower                                                 |
| django_template            | 31.7 ms                                                | 53.2 ms: 1.68x slower                                                 |
| mako                       | 10.7 ms                                                | 18.6 ms: 1.74x slower                                                 |
| nbody                      | 87.7 ms                                                | 154 ms: 1.76x slower                                                  |
| subparsers                 | 15.5 ms                                                | 33.6 ms: 2.18x slower                                                 |
| bench_thread_pool          | 818 us                                                 | 3.51 ms: 4.30x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 111 ms: 4.62x slower                                                  |
| logging_silent             | 101 ns                                                 | 705 ns: 6.98x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.29x slower                                                          |

Benchmark hidden because not significant (2): asyncio_websockets, go
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250607-3.15.0a0-8fdbbf8-NOGIL/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.208x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.21x
- 95% likely to have a slowdown of 1.19x
- 99% likely to have a slowdown of 1.15x

# Memory
- memory change: 1.28x