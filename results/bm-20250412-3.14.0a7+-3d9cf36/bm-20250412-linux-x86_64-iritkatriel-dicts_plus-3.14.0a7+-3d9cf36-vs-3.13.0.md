# Results vs. 3.13.0

- fork: iritkatriel
- ref: dicts_plus
- machine: linux-x86_64
- commit hash: 3d9cf36
- commit date: 2025-04-12
- overall geometric mean: 1.064x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 250 ms: 1.07x faster                                              |
| html5lib       | 63.4 ms                                                | 60.4 ms: 1.05x faster                                             |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                            |
| Geometric mean | (ref)                                                  | 1.03x faster                                                      |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                              |
| async_tree_memoization     | 437 ms                                                 | 309 ms: 1.41x faster                                              |
| async_tree_io_tg           | 861 ms                                                 | 612 ms: 1.41x faster                                              |
| async_tree_none            | 350 ms                                                 | 254 ms: 1.38x faster                                              |
| async_tree_io              | 838 ms                                                 | 611 ms: 1.37x faster                                              |
| async_tree_none_tg         | 319 ms                                                 | 246 ms: 1.30x faster                                              |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 476 ms: 1.20x faster                                              |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 473 ms: 1.15x faster                                              |
| async_generators           | 433 ms                                                 | 390 ms: 1.11x faster                                              |
| coroutines                 | 22.2 ms                                                | 23.8 ms: 1.07x slower                                             |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                      |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 78.7 ms                                                | 68.1 ms: 1.15x faster                                             |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                              |
| nbody          | 87.7 ms                                                | 90.0 ms: 1.03x slower                                             |
| Geometric mean | (ref)                                                  | 1.04x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.16 ms: 1.19x faster                                             |
| regex_v8       | 26.9 ms                                                | 23.1 ms: 1.16x faster                                             |
| regex_compile  | 132 ms                                                 | 124 ms: 1.06x faster                                              |
| regex_dna      | 220 ms                                                 | 208 ms: 1.06x faster                                              |
| Geometric mean | (ref)                                                  | 1.12x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                              |
| tomli_loads          | 2.12 sec                                               | 1.93 sec: 1.10x faster                                            |
| xml_etree_generate   | 86.8 ms                                                | 83.2 ms: 1.04x faster                                             |
| xml_etree_process    | 60.5 ms                                                | 58.1 ms: 1.04x faster                                             |
| xml_etree_iterparse  | 101 ms                                                 | 98.4 ms: 1.03x faster                                             |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                              |
| pickle_pure_python   | 302 us                                                 | 314 us: 1.04x slower                                              |
| json_loads           | 27.2 us                                                | 29.3 us: 1.08x slower                                             |
| json_dumps           | 10.1 ms                                                | 11.7 ms: 1.16x slower                                             |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.04x slower                                             |
| python_startup_no_site | 7.00 ms                                                | 8.20 ms: 1.17x slower                                             |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 20.8 ms: 1.09x faster                                             |
| genshi_xml      | 50.5 ms                                                | 48.7 ms: 1.04x faster                                             |
| django_template | 31.7 ms                                                | 31.1 ms: 1.02x faster                                             |
| mako            | 10.7 ms                                                | 11.4 ms: 1.07x slower                                             |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.20 sec: 2.12x faster                                            |
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                              |
| deepcopy                   | 354 us                                                 | 248 us: 1.43x faster                                              |
| async_tree_memoization     | 437 ms                                                 | 309 ms: 1.41x faster                                              |
| async_tree_io_tg           | 861 ms                                                 | 612 ms: 1.41x faster                                              |
| async_tree_none            | 350 ms                                                 | 254 ms: 1.38x faster                                              |
| async_tree_io              | 838 ms                                                 | 611 ms: 1.37x faster                                              |
| deepcopy_memo              | 38.4 us                                                | 28.6 us: 1.34x faster                                             |
| async_tree_none_tg         | 319 ms                                                 | 246 ms: 1.30x faster                                              |
| go                         | 141 ms                                                 | 110 ms: 1.28x faster                                              |
| deepcopy_reduce            | 3.24 us                                                | 2.58 us: 1.26x faster                                             |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 476 ms: 1.20x faster                                              |
| regex_effbot               | 3.77 ms                                                | 3.16 ms: 1.19x faster                                             |
| regex_v8                   | 26.9 ms                                                | 23.1 ms: 1.16x faster                                             |
| float                      | 78.7 ms                                                | 68.1 ms: 1.15x faster                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 473 ms: 1.15x faster                                              |
| spectral_norm              | 113 ms                                                 | 100 ms: 1.13x faster                                              |
| pylint                     | 312 ms                                                 | 278 ms: 1.12x faster                                              |
| async_generators           | 433 ms                                                 | 390 ms: 1.11x faster                                              |
| richards                   | 47.5 ms                                                | 42.8 ms: 1.11x faster                                             |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                              |
| tomli_loads                | 2.12 sec                                               | 1.93 sec: 1.10x faster                                            |
| richards_super             | 53.7 ms                                                | 49.2 ms: 1.09x faster                                             |
| dulwich_log                | 64.6 ms                                                | 59.2 ms: 1.09x faster                                             |
| genshi_text                | 22.6 ms                                                | 20.8 ms: 1.09x faster                                             |
| telco                      | 8.40 ms                                                | 7.77 ms: 1.08x faster                                             |
| pycparser                  | 1.20 sec                                               | 1.12 sec: 1.07x faster                                            |
| 2to3                       | 266 ms                                                 | 250 ms: 1.07x faster                                              |
| scimark_fft                | 367 ms                                                 | 345 ms: 1.06x faster                                              |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.73 ms: 1.06x faster                                             |
| logging_silent             | 101 ns                                                 | 95.0 ns: 1.06x faster                                             |
| regex_compile              | 132 ms                                                 | 124 ms: 1.06x faster                                              |
| bpe_tokeniser              | 4.69 sec                                               | 4.43 sec: 1.06x faster                                            |
| regex_dna                  | 220 ms                                                 | 208 ms: 1.06x faster                                              |
| sqlite_synth               | 2.90 us                                                | 2.75 us: 1.05x faster                                             |
| html5lib                   | 63.4 ms                                                | 60.4 ms: 1.05x faster                                             |
| sympy_integrate            | 19.8 ms                                                | 18.9 ms: 1.05x faster                                             |
| xml_etree_generate         | 86.8 ms                                                | 83.2 ms: 1.04x faster                                             |
| xml_etree_process          | 60.5 ms                                                | 58.1 ms: 1.04x faster                                             |
| pathlib                    | 17.4 ms                                                | 16.7 ms: 1.04x faster                                             |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                            |
| chaos                      | 58.0 ms                                                | 55.9 ms: 1.04x faster                                             |
| scimark_sor                | 122 ms                                                 | 118 ms: 1.04x faster                                              |
| gc_traversal               | 4.90 ms                                                | 4.72 ms: 1.04x faster                                             |
| genshi_xml                 | 50.5 ms                                                | 48.7 ms: 1.04x faster                                             |
| sympy_str                  | 273 ms                                                 | 264 ms: 1.03x faster                                              |
| pyflate                    | 470 ms                                                 | 456 ms: 1.03x faster                                              |
| xml_etree_iterparse        | 101 ms                                                 | 98.4 ms: 1.03x faster                                             |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.03x faster                                              |
| crypto_pyaes               | 74.7 ms                                                | 72.8 ms: 1.03x faster                                             |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                            |
| logging_simple             | 5.65 us                                                | 5.52 us: 1.02x faster                                             |
| scimark_monte_carlo        | 66.8 ms                                                | 65.2 ms: 1.02x faster                                             |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                              |
| pprint_pformat             | 1.48 sec                                               | 1.45 sec: 1.02x faster                                            |
| pprint_safe_repr           | 727 ms                                                 | 714 ms: 1.02x faster                                              |
| django_template            | 31.7 ms                                                | 31.1 ms: 1.02x faster                                             |
| logging_format             | 6.23 us                                                | 6.13 us: 1.02x faster                                             |
| sqlalchemy_declarative     | 133 ms                                                 | 132 ms: 1.01x faster                                              |
| raytrace                   | 262 ms                                                 | 259 ms: 1.01x faster                                              |
| sympy_expand               | 456 ms                                                 | 452 ms: 1.01x faster                                              |
| nqueens                    | 80.9 ms                                                | 80.2 ms: 1.01x faster                                             |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                              |
| scimark_lu                 | 114 ms                                                 | 115 ms: 1.01x slower                                              |
| unpickle_pure_python       | 213 us                                                 | 216 us: 1.01x slower                                              |
| comprehensions             | 16.5 us                                                | 16.7 us: 1.01x slower                                             |
| generators                 | 28.8 ms                                                | 29.2 ms: 1.02x slower                                             |
| hexiom                     | 6.08 ms                                                | 6.19 ms: 1.02x slower                                             |
| typing_runtime_protocols   | 160 us                                                 | 164 us: 1.02x slower                                              |
| nbody                      | 87.7 ms                                                | 90.0 ms: 1.03x slower                                             |
| pickle_pure_python         | 302 us                                                 | 314 us: 1.04x slower                                              |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                             |
| fannkuch                   | 394 ms                                                 | 412 ms: 1.05x slower                                              |
| deltablue                  | 3.19 ms                                                | 3.38 ms: 1.06x slower                                             |
| coverage                   | 82.8 ms                                                | 87.6 ms: 1.06x slower                                             |
| mako                       | 10.7 ms                                                | 11.4 ms: 1.07x slower                                             |
| coroutines                 | 22.2 ms                                                | 23.8 ms: 1.07x slower                                             |
| json_loads                 | 27.2 us                                                | 29.3 us: 1.08x slower                                             |
| bench_thread_pool          | 818 us                                                 | 887 us: 1.08x slower                                              |
| many_optionals             | 857 us                                                 | 930 us: 1.08x slower                                              |
| json_dumps                 | 10.1 ms                                                | 11.7 ms: 1.16x slower                                             |
| python_startup_no_site     | 7.00 ms                                                | 8.20 ms: 1.17x slower                                             |
| subparsers                 | 15.5 ms                                                | 20.7 ms: 1.34x slower                                             |
| bench_mp_pool              | 24.0 ms                                                | 81.9 ms: 3.42x slower                                             |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                      |

Benchmark hidden because not significant (7): json, create_gc_cycles, docutils, asyncio_websockets, shortest_path, sqlalchemy_imperative, connected_components
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250412-3.14.0a7+-3d9cf36/bm-20250412-linux-x86_64-iritkatriel-dicts_plus-3.14.0a7+-3d9cf36.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.064x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.04x