# Results vs. 3.13.0

- fork: faster-cpython
- ref: explicit_check_perio
- machine: linux-x86_64
- commit hash: 494c825
- commit date: 2025-06-20
- overall geometric mean: 1.037x faster
- HPT reliability: 99.55%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 257 ms: 1.04x faster                                                            |
| docutils       | 2.58 sec                                               | 2.61 sec: 1.01x slower                                                          |
| html5lib       | 63.4 ms                                                | 61.9 ms: 1.02x faster                                                           |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                          |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                                            |
| async_tree_io              | 838 ms                                                 | 604 ms: 1.39x faster                                                            |
| async_tree_io_tg           | 861 ms                                                 | 622 ms: 1.38x faster                                                            |
| async_tree_memoization     | 437 ms                                                 | 321 ms: 1.36x faster                                                            |
| async_tree_none            | 350 ms                                                 | 267 ms: 1.31x faster                                                            |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                            |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 502 ms: 1.14x faster                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 490 ms: 1.11x faster                                                            |
| async_generators           | 433 ms                                                 | 412 ms: 1.05x faster                                                            |
| coroutines                 | 22.2 ms                                                | 24.7 ms: 1.11x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 72.3 ms: 1.09x faster                                                           |
| pidigits       | 186 ms                                                 | 189 ms: 1.01x slower                                                            |
| nbody          | 87.7 ms                                                | 99.1 ms: 1.13x slower                                                           |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.22 ms: 1.17x faster                                                           |
| regex_v8       | 26.9 ms                                                | 23.2 ms: 1.16x faster                                                           |
| regex_dna      | 220 ms                                                 | 199 ms: 1.11x faster                                                            |
| regex_compile  | 132 ms                                                 | 130 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 143 ms: 1.08x faster                                                            |
| tomli_loads          | 2.12 sec                                               | 2.02 sec: 1.05x faster                                                          |
| xml_etree_iterparse  | 101 ms                                                 | 98.8 ms: 1.03x faster                                                           |
| xml_etree_generate   | 86.8 ms                                                | 84.8 ms: 1.02x faster                                                           |
| xml_etree_process    | 60.5 ms                                                | 59.7 ms: 1.01x faster                                                           |
| json_loads           | 27.2 us                                                | 28.3 us: 1.04x slower                                                           |
| unpickle_pure_python | 213 us                                                 | 222 us: 1.04x slower                                                            |
| pickle_pure_python   | 302 us                                                 | 327 us: 1.08x slower                                                            |
| json_dumps           | 10.1 ms                                                | 11.2 ms: 1.10x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                           |
| python_startup_no_site | 7.00 ms                                                | 6.94 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.6 ms: 1.04x faster                                                           |
| genshi_xml      | 50.5 ms                                                | 50.0 ms: 1.01x faster                                                           |
| django_template | 31.7 ms                                                | 32.8 ms: 1.03x slower                                                           |
| mako            | 10.7 ms                                                | 11.6 ms: 1.08x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.07x faster                                                          |
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                                            |
| async_tree_io              | 838 ms                                                 | 604 ms: 1.39x faster                                                            |
| async_tree_io_tg           | 861 ms                                                 | 622 ms: 1.38x faster                                                            |
| deepcopy                   | 354 us                                                 | 257 us: 1.38x faster                                                            |
| async_tree_memoization     | 437 ms                                                 | 321 ms: 1.36x faster                                                            |
| async_tree_none            | 350 ms                                                 | 267 ms: 1.31x faster                                                            |
| deepcopy_memo              | 38.4 us                                                | 30.1 us: 1.27x faster                                                           |
| go                         | 141 ms                                                 | 111 ms: 1.27x faster                                                            |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                            |
| deepcopy_reduce            | 3.24 us                                                | 2.72 us: 1.19x faster                                                           |
| regex_effbot               | 3.77 ms                                                | 3.22 ms: 1.17x faster                                                           |
| regex_v8                   | 26.9 ms                                                | 23.2 ms: 1.16x faster                                                           |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 502 ms: 1.14x faster                                                            |
| pylint                     | 312 ms                                                 | 279 ms: 1.12x faster                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 490 ms: 1.11x faster                                                            |
| regex_dna                  | 220 ms                                                 | 199 ms: 1.11x faster                                                            |
| pyflate                    | 470 ms                                                 | 427 ms: 1.10x faster                                                            |
| richards                   | 47.5 ms                                                | 43.2 ms: 1.10x faster                                                           |
| richards_super             | 53.7 ms                                                | 49.4 ms: 1.09x faster                                                           |
| float                      | 78.7 ms                                                | 72.3 ms: 1.09x faster                                                           |
| xml_etree_parse            | 154 ms                                                 | 143 ms: 1.08x faster                                                            |
| dulwich_log                | 64.6 ms                                                | 60.0 ms: 1.08x faster                                                           |
| spectral_norm              | 113 ms                                                 | 107 ms: 1.06x faster                                                            |
| telco                      | 8.40 ms                                                | 7.99 ms: 1.05x faster                                                           |
| async_generators           | 433 ms                                                 | 412 ms: 1.05x faster                                                            |
| pycparser                  | 1.20 sec                                               | 1.14 sec: 1.05x faster                                                          |
| tomli_loads                | 2.12 sec                                               | 2.02 sec: 1.05x faster                                                          |
| genshi_text                | 22.6 ms                                                | 21.6 ms: 1.04x faster                                                           |
| scimark_sor                | 122 ms                                                 | 117 ms: 1.04x faster                                                            |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                           |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                                          |
| 2to3                       | 266 ms                                                 | 257 ms: 1.04x faster                                                            |
| bpe_tokeniser              | 4.69 sec                                               | 4.53 sec: 1.04x faster                                                          |
| djangocms                  | 22.3 us                                                | 21.6 us: 1.03x faster                                                           |
| sympy_integrate            | 19.8 ms                                                | 19.2 ms: 1.03x faster                                                           |
| comprehensions             | 16.5 us                                                | 16.0 us: 1.03x faster                                                           |
| thrift                     | 800 us                                                 | 779 us: 1.03x faster                                                            |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.03x faster                                                            |
| xml_etree_iterparse        | 101 ms                                                 | 98.8 ms: 1.03x faster                                                           |
| html5lib                   | 63.4 ms                                                | 61.9 ms: 1.02x faster                                                           |
| xml_etree_generate         | 86.8 ms                                                | 84.8 ms: 1.02x faster                                                           |
| sympy_str                  | 273 ms                                                 | 268 ms: 1.02x faster                                                            |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                          |
| regex_compile              | 132 ms                                                 | 130 ms: 1.02x faster                                                            |
| sqlite_synth               | 2.90 us                                                | 2.86 us: 1.01x faster                                                           |
| xml_etree_process          | 60.5 ms                                                | 59.7 ms: 1.01x faster                                                           |
| genshi_xml                 | 50.5 ms                                                | 50.0 ms: 1.01x faster                                                           |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                            |
| pathlib                    | 17.4 ms                                                | 17.2 ms: 1.01x faster                                                           |
| python_startup_no_site     | 7.00 ms                                                | 6.94 ms: 1.01x faster                                                           |
| nqueens                    | 80.9 ms                                                | 81.2 ms: 1.00x slower                                                           |
| docutils                   | 2.58 sec                                               | 2.61 sec: 1.01x slower                                                          |
| pidigits                   | 186 ms                                                 | 189 ms: 1.01x slower                                                            |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.09 ms: 1.01x slower                                                           |
| scimark_fft                | 367 ms                                                 | 374 ms: 1.02x slower                                                            |
| generators                 | 28.8 ms                                                | 29.4 ms: 1.02x slower                                                           |
| hexiom                     | 6.08 ms                                                | 6.22 ms: 1.02x slower                                                           |
| crypto_pyaes               | 74.7 ms                                                | 76.8 ms: 1.03x slower                                                           |
| scimark_lu                 | 114 ms                                                 | 118 ms: 1.03x slower                                                            |
| django_template            | 31.7 ms                                                | 32.8 ms: 1.03x slower                                                           |
| json_loads                 | 27.2 us                                                | 28.3 us: 1.04x slower                                                           |
| raytrace                   | 262 ms                                                 | 272 ms: 1.04x slower                                                            |
| chaos                      | 58.0 ms                                                | 60.5 ms: 1.04x slower                                                           |
| unpickle_pure_python       | 213 us                                                 | 222 us: 1.04x slower                                                            |
| typing_runtime_protocols   | 160 us                                                 | 168 us: 1.05x slower                                                            |
| coverage                   | 82.8 ms                                                | 87.1 ms: 1.05x slower                                                           |
| gc_traversal               | 4.90 ms                                                | 5.17 ms: 1.06x slower                                                           |
| fannkuch                   | 394 ms                                                 | 416 ms: 1.06x slower                                                            |
| create_gc_cycles           | 2.45 ms                                                | 2.59 ms: 1.06x slower                                                           |
| shortest_path              | 487 ms                                                 | 521 ms: 1.07x slower                                                            |
| connected_components       | 447 ms                                                 | 482 ms: 1.08x slower                                                            |
| mako                       | 10.7 ms                                                | 11.6 ms: 1.08x slower                                                           |
| pickle_pure_python         | 302 us                                                 | 327 us: 1.08x slower                                                            |
| deltablue                  | 3.19 ms                                                | 3.50 ms: 1.09x slower                                                           |
| json_dumps                 | 10.1 ms                                                | 11.2 ms: 1.10x slower                                                           |
| coroutines                 | 22.2 ms                                                | 24.7 ms: 1.11x slower                                                           |
| pprint_safe_repr           | 727 ms                                                 | 812 ms: 1.12x slower                                                            |
| pprint_pformat             | 1.48 sec                                               | 1.66 sec: 1.12x slower                                                          |
| logging_simple             | 5.65 us                                                | 6.33 us: 1.12x slower                                                           |
| nbody                      | 87.7 ms                                                | 99.1 ms: 1.13x slower                                                           |
| many_optionals             | 857 us                                                 | 969 us: 1.13x slower                                                            |
| logging_format             | 6.23 us                                                | 7.11 us: 1.14x slower                                                           |
| subparsers                 | 15.5 ms                                                | 23.6 ms: 1.53x slower                                                           |
| logging_silent             | 101 ns                                                 | 480 ns: 4.75x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (4): json, sympy_expand, asyncio_websockets, scimark_monte_carlo
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250620-3.15.0a0-494c825/bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.037x faster

# HPT report

- Reliability score: 99.55% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x