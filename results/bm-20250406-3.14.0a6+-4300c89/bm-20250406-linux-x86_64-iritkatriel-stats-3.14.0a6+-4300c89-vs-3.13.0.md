# Results vs. 3.13.0

- fork: iritkatriel
- ref: stats
- machine: linux-x86_64
- commit hash: 4300c89
- commit date: 2025-04-06
- overall geometric mean: 1.059x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6+-4300c89 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 251 ms: 1.06x faster                                         |
| html5lib       | 63.4 ms                                                | 60.5 ms: 1.05x faster                                        |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                                 |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6+-4300c89 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                         |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                         |
| async_tree_io_tg           | 861 ms                                                 | 615 ms: 1.40x faster                                         |
| async_tree_io              | 838 ms                                                 | 615 ms: 1.36x faster                                         |
| async_tree_none            | 350 ms                                                 | 259 ms: 1.35x faster                                         |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 483 ms: 1.19x faster                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.13x faster                                         |
| async_generators           | 433 ms                                                 | 397 ms: 1.09x faster                                         |
| coroutines                 | 22.2 ms                                                | 23.3 ms: 1.05x slower                                        |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6+-4300c89 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 78.7 ms                                                | 68.2 ms: 1.15x faster                                        |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                         |
| nbody          | 87.7 ms                                                | 92.2 ms: 1.05x slower                                        |
| Geometric mean | (ref)                                                  | 1.03x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6+-4300c89 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.0 ms: 1.17x faster                                        |
| regex_effbot   | 3.77 ms                                                | 3.32 ms: 1.13x faster                                        |
| regex_compile  | 132 ms                                                 | 125 ms: 1.06x faster                                         |
| Geometric mean | (ref)                                                  | 1.09x faster                                                 |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6+-4300c89 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                         |
| tomli_loads          | 2.12 sec                                               | 1.96 sec: 1.08x faster                                       |
| xml_etree_generate   | 86.8 ms                                                | 83.5 ms: 1.04x faster                                        |
| xml_etree_process    | 60.5 ms                                                | 58.3 ms: 1.04x faster                                        |
| xml_etree_iterparse  | 101 ms                                                 | 98.3 ms: 1.03x faster                                        |
| unpickle_pure_python | 213 us                                                 | 215 us: 1.01x slower                                         |
| pickle_pure_python   | 302 us                                                 | 315 us: 1.04x slower                                         |
| json_loads           | 27.2 us                                                | 29.7 us: 1.09x slower                                        |
| json_dumps           | 10.1 ms                                                | 11.7 ms: 1.15x slower                                        |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6+-4300c89 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.04x slower                                        |
| python_startup_no_site | 7.00 ms                                                | 8.18 ms: 1.17x slower                                        |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6+-4300c89 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 20.9 ms: 1.08x faster                                        |
| genshi_xml      | 50.5 ms                                                | 49.3 ms: 1.02x faster                                        |
| django_template | 31.7 ms                                                | 31.5 ms: 1.01x faster                                        |
| mako            | 10.7 ms                                                | 11.3 ms: 1.06x slower                                        |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6+-4300c89 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.07x faster                                       |
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                         |
| deepcopy                   | 354 us                                                 | 249 us: 1.42x faster                                         |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                         |
| async_tree_io_tg           | 861 ms                                                 | 615 ms: 1.40x faster                                         |
| async_tree_io              | 838 ms                                                 | 615 ms: 1.36x faster                                         |
| async_tree_none            | 350 ms                                                 | 259 ms: 1.35x faster                                         |
| deepcopy_memo              | 38.4 us                                                | 28.8 us: 1.34x faster                                        |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                         |
| go                         | 141 ms                                                 | 111 ms: 1.26x faster                                         |
| deepcopy_reduce            | 3.24 us                                                | 2.57 us: 1.26x faster                                        |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 483 ms: 1.19x faster                                         |
| regex_v8                   | 26.9 ms                                                | 23.0 ms: 1.17x faster                                        |
| float                      | 78.7 ms                                                | 68.2 ms: 1.15x faster                                        |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.13x faster                                         |
| regex_effbot               | 3.77 ms                                                | 3.32 ms: 1.13x faster                                        |
| pylint                     | 312 ms                                                 | 276 ms: 1.13x faster                                         |
| richards                   | 47.5 ms                                                | 42.2 ms: 1.13x faster                                        |
| richards_super             | 53.7 ms                                                | 48.4 ms: 1.11x faster                                        |
| spectral_norm              | 113 ms                                                 | 102 ms: 1.11x faster                                         |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                         |
| async_generators           | 433 ms                                                 | 397 ms: 1.09x faster                                         |
| telco                      | 8.40 ms                                                | 7.70 ms: 1.09x faster                                        |
| dulwich_log                | 64.6 ms                                                | 59.4 ms: 1.09x faster                                        |
| tomli_loads                | 2.12 sec                                               | 1.96 sec: 1.08x faster                                       |
| genshi_text                | 22.6 ms                                                | 20.9 ms: 1.08x faster                                        |
| scimark_fft                | 367 ms                                                 | 342 ms: 1.07x faster                                         |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.75 ms: 1.06x faster                                        |
| 2to3                       | 266 ms                                                 | 251 ms: 1.06x faster                                         |
| regex_compile              | 132 ms                                                 | 125 ms: 1.06x faster                                         |
| pathlib                    | 17.4 ms                                                | 16.5 ms: 1.06x faster                                        |
| logging_silent             | 101 ns                                                 | 96.1 ns: 1.05x faster                                        |
| html5lib                   | 63.4 ms                                                | 60.5 ms: 1.05x faster                                        |
| sqlite_synth               | 2.90 us                                                | 2.78 us: 1.04x faster                                        |
| sympy_integrate            | 19.8 ms                                                | 19.0 ms: 1.04x faster                                        |
| xml_etree_generate         | 86.8 ms                                                | 83.5 ms: 1.04x faster                                        |
| xml_etree_process          | 60.5 ms                                                | 58.3 ms: 1.04x faster                                        |
| pprint_safe_repr           | 727 ms                                                 | 701 ms: 1.04x faster                                         |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.04x faster                                       |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.03x faster                                       |
| bpe_tokeniser              | 4.69 sec                                               | 4.55 sec: 1.03x faster                                       |
| xml_etree_iterparse        | 101 ms                                                 | 98.3 ms: 1.03x faster                                        |
| chaos                      | 58.0 ms                                                | 56.4 ms: 1.03x faster                                        |
| pprint_pformat             | 1.48 sec                                               | 1.44 sec: 1.03x faster                                       |
| gc_traversal               | 4.90 ms                                                | 4.77 ms: 1.03x faster                                        |
| logging_simple             | 5.65 us                                                | 5.51 us: 1.03x faster                                        |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                         |
| genshi_xml                 | 50.5 ms                                                | 49.3 ms: 1.02x faster                                        |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.02x faster                                         |
| scimark_monte_carlo        | 66.8 ms                                                | 65.5 ms: 1.02x faster                                        |
| logging_format             | 6.23 us                                                | 6.11 us: 1.02x faster                                        |
| crypto_pyaes               | 74.7 ms                                                | 73.3 ms: 1.02x faster                                        |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                       |
| pyflate                    | 470 ms                                                 | 462 ms: 1.02x faster                                         |
| sympy_str                  | 273 ms                                                 | 269 ms: 1.02x faster                                         |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.01x faster                                         |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                         |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.7 ms: 1.01x faster                                        |
| django_template            | 31.7 ms                                                | 31.5 ms: 1.01x faster                                        |
| raytrace                   | 262 ms                                                 | 261 ms: 1.00x faster                                         |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                         |
| unpickle_pure_python       | 213 us                                                 | 215 us: 1.01x slower                                         |
| hexiom                     | 6.08 ms                                                | 6.14 ms: 1.01x slower                                        |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                        |
| shortest_path              | 487 ms                                                 | 492 ms: 1.01x slower                                         |
| coverage                   | 82.8 ms                                                | 84.8 ms: 1.02x slower                                        |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.03x slower                                         |
| generators                 | 28.8 ms                                                | 29.6 ms: 1.03x slower                                        |
| comprehensions             | 16.5 us                                                | 17.0 us: 1.03x slower                                        |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                        |
| pickle_pure_python         | 302 us                                                 | 315 us: 1.04x slower                                         |
| typing_runtime_protocols   | 160 us                                                 | 167 us: 1.04x slower                                         |
| coroutines                 | 22.2 ms                                                | 23.3 ms: 1.05x slower                                        |
| fannkuch                   | 394 ms                                                 | 413 ms: 1.05x slower                                         |
| nbody                      | 87.7 ms                                                | 92.2 ms: 1.05x slower                                        |
| deltablue                  | 3.19 ms                                                | 3.37 ms: 1.05x slower                                        |
| mako                       | 10.7 ms                                                | 11.3 ms: 1.06x slower                                        |
| bench_thread_pool          | 818 us                                                 | 883 us: 1.08x slower                                         |
| many_optionals             | 857 us                                                 | 925 us: 1.08x slower                                         |
| json_loads                 | 27.2 us                                                | 29.7 us: 1.09x slower                                        |
| json_dumps                 | 10.1 ms                                                | 11.7 ms: 1.15x slower                                        |
| python_startup_no_site     | 7.00 ms                                                | 8.18 ms: 1.17x slower                                        |
| subparsers                 | 15.5 ms                                                | 20.8 ms: 1.35x slower                                        |
| bench_mp_pool              | 24.0 ms                                                | 81.9 ms: 3.42x slower                                        |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                 |

Benchmark hidden because not significant (7): nqueens, regex_dna, json, connected_components, sympy_expand, docutils, asyncio_websockets
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250406-3.14.0a6+-4300c89/bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6+-4300c89.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.059x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.03x