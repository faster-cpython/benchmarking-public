# Results vs. 3.12.0

- fork: faster-cpython
- ref: fast_side_exits
- machine: linux-x86_64
- commit hash: 73832b2
- commit date: 2025-07-08
- overall geometric mean: 1.032x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-pythonperf2-x86_64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 286 ms: 1.00x slower                                                             |
| docutils       | 2.87 sec                                                     | 2.91 sec: 1.02x slower                                                           |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-pythonperf2-x86_64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io              | 1.04 sec                                                     | 624 ms: 1.67x faster                                                             |
| async_tree_io_tg           | 1.05 sec                                                     | 632 ms: 1.67x faster                                                             |
| async_tree_memoization     | 544 ms                                                       | 331 ms: 1.64x faster                                                             |
| async_tree_none            | 452 ms                                                       | 275 ms: 1.64x faster                                                             |
| async_tree_memoization_tg  | 540 ms                                                       | 333 ms: 1.62x faster                                                             |
| async_tree_none_tg         | 431 ms                                                       | 273 ms: 1.58x faster                                                             |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 503 ms: 1.38x faster                                                             |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 510 ms: 1.37x faster                                                             |
| Geometric mean             | (ref)                                                        | 1.57x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-pythonperf2-x86_64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 63.6 ms: 1.21x faster                                                            |
| pidigits       | 265 ms                                                       | 255 ms: 1.04x faster                                                             |
| nbody          | 88.0 ms                                                      | 99.7 ms: 1.13x slower                                                            |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-pythonperf2-x86_64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 133 ms: 1.08x faster                                                             |
| regex_dna      | 239 ms                                                       | 225 ms: 1.06x faster                                                             |
| regex_effbot   | 3.57 ms                                                      | 3.67 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                     |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-pythonperf2-x86_64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 1.94 sec: 1.11x faster                                                           |
| xml_etree_generate   | 86.1 ms                                                      | 78.9 ms: 1.09x faster                                                            |
| xml_etree_parse      | 144 ms                                                       | 134 ms: 1.07x faster                                                             |
| xml_etree_iterparse  | 103 ms                                                       | 96.9 ms: 1.06x faster                                                            |
| unpickle_pure_python | 210 us                                                       | 198 us: 1.06x faster                                                             |
| xml_etree_process    | 58.4 ms                                                      | 55.4 ms: 1.05x faster                                                            |
| json_loads           | 24.4 us                                                      | 25.2 us: 1.03x slower                                                            |
| pickle_pure_python   | 318 us                                                       | 338 us: 1.06x slower                                                             |
| json_dumps           | 10.2 ms                                                      | 11.1 ms: 1.09x slower                                                            |
| Geometric mean       | (ref)                                                        | 1.03x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-pythonperf2-x86_64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.86 ms: 1.03x slower                                                            |
| python_startup         | 11.6 ms                                                      | 15.4 ms: 1.32x slower                                                            |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-pythonperf2-x86_64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.4 ms: 1.08x faster                                                            |
| mako            | 10.0 ms                                                      | 10.1 ms: 1.01x slower                                                            |
| Geometric mean  | (ref)                                                        | 1.03x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-pythonperf2-x86_64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.29 sec: 1.99x faster                                                           |
| async_tree_io              | 1.04 sec                                                     | 624 ms: 1.67x faster                                                             |
| async_tree_io_tg           | 1.05 sec                                                     | 632 ms: 1.67x faster                                                             |
| async_tree_memoization     | 544 ms                                                       | 331 ms: 1.64x faster                                                             |
| async_tree_none            | 452 ms                                                       | 275 ms: 1.64x faster                                                             |
| async_tree_memoization_tg  | 540 ms                                                       | 333 ms: 1.62x faster                                                             |
| async_tree_none_tg         | 431 ms                                                       | 273 ms: 1.58x faster                                                             |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 503 ms: 1.38x faster                                                             |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 510 ms: 1.37x faster                                                             |
| generators                 | 37.4 ms                                                      | 28.2 ms: 1.33x faster                                                            |
| richards                   | 45.7 ms                                                      | 34.5 ms: 1.32x faster                                                            |
| deepcopy_memo              | 36.8 us                                                      | 28.1 us: 1.31x faster                                                            |
| deepcopy                   | 368 us                                                       | 281 us: 1.31x faster                                                             |
| richards_super             | 51.3 ms                                                      | 40.3 ms: 1.28x faster                                                            |
| comprehensions             | 21.9 us                                                      | 17.5 us: 1.25x faster                                                            |
| float                      | 76.6 ms                                                      | 63.6 ms: 1.21x faster                                                            |
| go                         | 150 ms                                                       | 127 ms: 1.18x faster                                                             |
| spectral_norm              | 91.6 ms                                                      | 81.3 ms: 1.13x faster                                                            |
| deltablue                  | 3.24 ms                                                      | 2.89 ms: 1.12x faster                                                            |
| deepcopy_reduce            | 3.37 us                                                      | 3.02 us: 1.12x faster                                                            |
| tomli_loads                | 2.16 sec                                                     | 1.94 sec: 1.11x faster                                                           |
| pathlib                    | 18.9 ms                                                      | 17.0 ms: 1.11x faster                                                            |
| logging_format             | 7.48 us                                                      | 6.79 us: 1.10x faster                                                            |
| dulwich_log                | 65.4 ms                                                      | 59.8 ms: 1.09x faster                                                            |
| xml_etree_generate         | 86.1 ms                                                      | 78.9 ms: 1.09x faster                                                            |
| logging_simple             | 6.71 us                                                      | 6.15 us: 1.09x faster                                                            |
| scimark_monte_carlo        | 69.0 ms                                                      | 63.3 ms: 1.09x faster                                                            |
| pyflate                    | 439 ms                                                       | 405 ms: 1.08x faster                                                             |
| regex_compile              | 144 ms                                                       | 133 ms: 1.08x faster                                                             |
| django_template            | 38.2 ms                                                      | 35.4 ms: 1.08x faster                                                            |
| sympy_sum                  | 162 ms                                                       | 151 ms: 1.07x faster                                                             |
| pprint_pformat             | 1.65 sec                                                     | 1.54 sec: 1.07x faster                                                           |
| sympy_integrate            | 23.9 ms                                                      | 22.4 ms: 1.07x faster                                                            |
| xml_etree_parse            | 144 ms                                                       | 134 ms: 1.07x faster                                                             |
| meteor_contest             | 128 ms                                                       | 121 ms: 1.06x faster                                                             |
| xml_etree_iterparse        | 103 ms                                                       | 96.9 ms: 1.06x faster                                                            |
| chaos                      | 64.0 ms                                                      | 60.4 ms: 1.06x faster                                                            |
| unpickle_pure_python       | 210 us                                                       | 198 us: 1.06x faster                                                             |
| regex_dna                  | 239 ms                                                       | 225 ms: 1.06x faster                                                             |
| xml_etree_process          | 58.4 ms                                                      | 55.4 ms: 1.05x faster                                                            |
| pprint_safe_repr           | 807 ms                                                       | 766 ms: 1.05x faster                                                             |
| sympy_str                  | 302 ms                                                       | 290 ms: 1.04x faster                                                             |
| pidigits                   | 265 ms                                                       | 255 ms: 1.04x faster                                                             |
| crypto_pyaes               | 80.3 ms                                                      | 77.6 ms: 1.04x faster                                                            |
| scimark_sor                | 109 ms                                                       | 105 ms: 1.04x faster                                                             |
| coroutines                 | 23.0 ms                                                      | 22.3 ms: 1.03x faster                                                            |
| raytrace                   | 298 ms                                                       | 294 ms: 1.01x faster                                                             |
| logging_silent             | 94.4 ns                                                      | 93.3 ns: 1.01x faster                                                            |
| 2to3                       | 285 ms                                                       | 286 ms: 1.00x slower                                                             |
| scimark_fft                | 301 ms                                                       | 303 ms: 1.01x slower                                                             |
| mako                       | 10.0 ms                                                      | 10.1 ms: 1.01x slower                                                            |
| docutils                   | 2.87 sec                                                     | 2.91 sec: 1.02x slower                                                           |
| scimark_lu                 | 98.8 ms                                                      | 101 ms: 1.02x slower                                                             |
| python_startup_no_site     | 8.64 ms                                                      | 8.86 ms: 1.03x slower                                                            |
| regex_effbot               | 3.57 ms                                                      | 3.67 ms: 1.03x slower                                                            |
| sympy_expand               | 484 ms                                                       | 497 ms: 1.03x slower                                                             |
| hexiom                     | 5.96 ms                                                      | 6.13 ms: 1.03x slower                                                            |
| nqueens                    | 89.9 ms                                                      | 92.5 ms: 1.03x slower                                                            |
| json_loads                 | 24.4 us                                                      | 25.2 us: 1.03x slower                                                            |
| json                       | 5.12 ms                                                      | 5.35 ms: 1.04x slower                                                            |
| sqlite_synth               | 2.77 us                                                      | 2.93 us: 1.06x slower                                                            |
| pickle_pure_python         | 318 us                                                       | 338 us: 1.06x slower                                                             |
| json_dumps                 | 10.2 ms                                                      | 11.1 ms: 1.09x slower                                                            |
| fannkuch                   | 350 ms                                                       | 383 ms: 1.09x slower                                                             |
| nbody                      | 88.0 ms                                                      | 99.7 ms: 1.13x slower                                                            |
| async_generators           | 390 ms                                                       | 444 ms: 1.14x slower                                                             |
| typing_runtime_protocols   | 152 us                                                       | 174 us: 1.15x slower                                                             |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.00 ms: 1.19x slower                                                            |
| coverage                   | 66.7 ms                                                      | 80.3 ms: 1.20x slower                                                            |
| python_startup             | 11.6 ms                                                      | 15.4 ms: 1.32x slower                                                            |
| create_gc_cycles           | 1.59 ms                                                      | 2.84 ms: 1.79x slower                                                            |
| gc_traversal               | 3.48 ms                                                      | 6.48 ms: 1.86x slower                                                            |
| telco                      | 6.96 ms                                                      | 160 ms: 23.02x slower                                                            |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                     |

Benchmark hidden because not significant (2): asyncio_websockets, regex_v8
Ignored benchmarks (23) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, pycparser, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250708-3.15.0a0-73832b2-JIT/bm-20250708-pythonperf2-x86_64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.032x faster

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.14x