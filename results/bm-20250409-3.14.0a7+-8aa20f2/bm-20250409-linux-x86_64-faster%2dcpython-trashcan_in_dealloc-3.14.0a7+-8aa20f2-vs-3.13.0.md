# Results vs. 3.13.0

- fork: faster-cpython
- ref: trashcan_in_dealloc
- machine: linux-x86_64
- commit hash: 8aa20f2
- commit date: 2025-04-09
- overall geometric mean: 1.052x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 252 ms: 1.05x faster                                                            |
| html5lib       | 63.4 ms                                                | 61.0 ms: 1.04x faster                                                           |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                          |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                                            |
| async_tree_io_tg           | 861 ms                                                 | 615 ms: 1.40x faster                                                            |
| async_tree_memoization     | 437 ms                                                 | 315 ms: 1.39x faster                                                            |
| async_tree_io              | 838 ms                                                 | 619 ms: 1.35x faster                                                            |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                            |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                                            |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 490 ms: 1.17x faster                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 484 ms: 1.12x faster                                                            |
| async_generators           | 433 ms                                                 | 405 ms: 1.07x faster                                                            |
| coroutines                 | 22.2 ms                                                | 24.0 ms: 1.08x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 69.7 ms: 1.13x faster                                                           |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                            |
| nbody          | 87.7 ms                                                | 89.3 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.0 ms: 1.22x faster                                                           |
| regex_effbot   | 3.77 ms                                                | 3.33 ms: 1.13x faster                                                           |
| regex_compile  | 132 ms                                                 | 126 ms: 1.05x faster                                                            |
| regex_dna      | 220 ms                                                 | 213 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 142 ms: 1.09x faster                                                            |
| tomli_loads          | 2.12 sec                                               | 1.97 sec: 1.07x faster                                                          |
| xml_etree_process    | 60.5 ms                                                | 58.5 ms: 1.03x faster                                                           |
| xml_etree_generate   | 86.8 ms                                                | 84.3 ms: 1.03x faster                                                           |
| xml_etree_iterparse  | 101 ms                                                 | 98.7 ms: 1.03x faster                                                           |
| unpickle_pure_python | 213 us                                                 | 218 us: 1.02x slower                                                            |
| pickle_pure_python   | 302 us                                                 | 314 us: 1.04x slower                                                            |
| json_loads           | 27.2 us                                                | 30.3 us: 1.12x slower                                                           |
| json_dumps           | 10.1 ms                                                | 11.8 ms: 1.17x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                           |
| python_startup_no_site | 7.00 ms                                                | 8.22 ms: 1.17x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 20.9 ms: 1.08x faster                                                           |
| genshi_xml      | 50.5 ms                                                | 48.9 ms: 1.03x faster                                                           |
| django_template | 31.7 ms                                                | 31.9 ms: 1.01x slower                                                           |
| mako            | 10.7 ms                                                | 11.1 ms: 1.04x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.24 sec: 2.06x faster                                                          |
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                                            |
| async_tree_io_tg           | 861 ms                                                 | 615 ms: 1.40x faster                                                            |
| async_tree_memoization     | 437 ms                                                 | 315 ms: 1.39x faster                                                            |
| deepcopy                   | 354 us                                                 | 257 us: 1.38x faster                                                            |
| async_tree_io              | 838 ms                                                 | 619 ms: 1.35x faster                                                            |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                            |
| go                         | 141 ms                                                 | 108 ms: 1.30x faster                                                            |
| deepcopy_memo              | 38.4 us                                                | 29.7 us: 1.29x faster                                                           |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                                            |
| regex_v8                   | 26.9 ms                                                | 22.0 ms: 1.22x faster                                                           |
| deepcopy_reduce            | 3.24 us                                                | 2.72 us: 1.19x faster                                                           |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 490 ms: 1.17x faster                                                            |
| regex_effbot               | 3.77 ms                                                | 3.33 ms: 1.13x faster                                                           |
| float                      | 78.7 ms                                                | 69.7 ms: 1.13x faster                                                           |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 484 ms: 1.12x faster                                                            |
| pylint                     | 312 ms                                                 | 278 ms: 1.12x faster                                                            |
| richards                   | 47.5 ms                                                | 42.5 ms: 1.12x faster                                                           |
| richards_super             | 53.7 ms                                                | 48.6 ms: 1.10x faster                                                           |
| xml_etree_parse            | 154 ms                                                 | 142 ms: 1.09x faster                                                            |
| genshi_text                | 22.6 ms                                                | 20.9 ms: 1.08x faster                                                           |
| spectral_norm              | 113 ms                                                 | 105 ms: 1.08x faster                                                            |
| dulwich_log                | 64.6 ms                                                | 59.9 ms: 1.08x faster                                                           |
| tomli_loads                | 2.12 sec                                               | 1.97 sec: 1.07x faster                                                          |
| pyflate                    | 470 ms                                                 | 437 ms: 1.07x faster                                                            |
| async_generators           | 433 ms                                                 | 405 ms: 1.07x faster                                                            |
| 2to3                       | 266 ms                                                 | 252 ms: 1.05x faster                                                            |
| telco                      | 8.40 ms                                                | 7.99 ms: 1.05x faster                                                           |
| regex_compile              | 132 ms                                                 | 126 ms: 1.05x faster                                                            |
| scimark_sor                | 122 ms                                                 | 117 ms: 1.04x faster                                                            |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.04x faster                                                          |
| html5lib                   | 63.4 ms                                                | 61.0 ms: 1.04x faster                                                           |
| sympy_integrate            | 19.8 ms                                                | 19.1 ms: 1.04x faster                                                           |
| logging_silent             | 101 ns                                                 | 97.6 ns: 1.03x faster                                                           |
| regex_dna                  | 220 ms                                                 | 213 ms: 1.03x faster                                                            |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.03x faster                                                            |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.03x faster                                                          |
| xml_etree_process          | 60.5 ms                                                | 58.5 ms: 1.03x faster                                                           |
| genshi_xml                 | 50.5 ms                                                | 48.9 ms: 1.03x faster                                                           |
| sqlite_synth               | 2.90 us                                                | 2.81 us: 1.03x faster                                                           |
| scimark_fft                | 367 ms                                                 | 356 ms: 1.03x faster                                                            |
| xml_etree_generate         | 86.8 ms                                                | 84.3 ms: 1.03x faster                                                           |
| pathlib                    | 17.4 ms                                                | 16.9 ms: 1.03x faster                                                           |
| bpe_tokeniser              | 4.69 sec                                               | 4.57 sec: 1.03x faster                                                          |
| xml_etree_iterparse        | 101 ms                                                 | 98.7 ms: 1.03x faster                                                           |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.92 ms: 1.02x faster                                                           |
| gc_traversal               | 4.90 ms                                                | 4.79 ms: 1.02x faster                                                           |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                          |
| sympy_str                  | 273 ms                                                 | 269 ms: 1.02x faster                                                            |
| logging_simple             | 5.65 us                                                | 5.60 us: 1.01x faster                                                           |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                            |
| pprint_safe_repr           | 727 ms                                                 | 721 ms: 1.01x faster                                                            |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                            |
| sympy_expand               | 456 ms                                                 | 459 ms: 1.01x slower                                                            |
| django_template            | 31.7 ms                                                | 31.9 ms: 1.01x slower                                                           |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.0 ms: 1.01x slower                                                           |
| hexiom                     | 6.08 ms                                                | 6.12 ms: 1.01x slower                                                           |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                                           |
| nqueens                    | 80.9 ms                                                | 81.6 ms: 1.01x slower                                                           |
| typing_runtime_protocols   | 160 us                                                 | 162 us: 1.01x slower                                                            |
| raytrace                   | 262 ms                                                 | 266 ms: 1.02x slower                                                            |
| crypto_pyaes               | 74.7 ms                                                | 76.0 ms: 1.02x slower                                                           |
| nbody                      | 87.7 ms                                                | 89.3 ms: 1.02x slower                                                           |
| shortest_path              | 487 ms                                                 | 496 ms: 1.02x slower                                                            |
| unpickle_pure_python       | 213 us                                                 | 218 us: 1.02x slower                                                            |
| comprehensions             | 16.5 us                                                | 16.9 us: 1.02x slower                                                           |
| generators                 | 28.8 ms                                                | 29.5 ms: 1.02x slower                                                           |
| deltablue                  | 3.19 ms                                                | 3.28 ms: 1.03x slower                                                           |
| coverage                   | 82.8 ms                                                | 85.2 ms: 1.03x slower                                                           |
| scimark_lu                 | 114 ms                                                 | 118 ms: 1.03x slower                                                            |
| connected_components       | 447 ms                                                 | 461 ms: 1.03x slower                                                            |
| mako                       | 10.7 ms                                                | 11.1 ms: 1.04x slower                                                           |
| pickle_pure_python         | 302 us                                                 | 314 us: 1.04x slower                                                            |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                           |
| fannkuch                   | 394 ms                                                 | 415 ms: 1.05x slower                                                            |
| json                       | 5.32 ms                                                | 5.63 ms: 1.06x slower                                                           |
| bench_thread_pool          | 818 us                                                 | 883 us: 1.08x slower                                                            |
| coroutines                 | 22.2 ms                                                | 24.0 ms: 1.08x slower                                                           |
| many_optionals             | 857 us                                                 | 934 us: 1.09x slower                                                            |
| json_loads                 | 27.2 us                                                | 30.3 us: 1.12x slower                                                           |
| json_dumps                 | 10.1 ms                                                | 11.8 ms: 1.17x slower                                                           |
| python_startup_no_site     | 7.00 ms                                                | 8.22 ms: 1.17x slower                                                           |
| subparsers                 | 15.5 ms                                                | 20.8 ms: 1.34x slower                                                           |
| bench_mp_pool              | 24.0 ms                                                | 82.4 ms: 3.44x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                                    |

Benchmark hidden because not significant (7): logging_format, scimark_monte_carlo, sqlalchemy_declarative, pprint_pformat, asyncio_websockets, chaos, docutils
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250409-3.14.0a7+-8aa20f2/bm-20250409-linux-x86_64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.052x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x