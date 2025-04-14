# Results vs. 3.12.0

- fork: mdboom
- ref: tuple_hash_cache2
- machine: linux-x86_64
- commit hash: d2c521a
- commit date: 2025-03-24
- overall geometric mean: 1.043x slower
- HPT reliability: 99.35%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-d2c521a |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 325 ms: 1.14x slower                                                      |
| docutils       | 2.87 sec                                                     | 2.94 sec: 1.03x slower                                                    |
| Geometric mean | (ref)                                                        | 1.08x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-d2c521a |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 551 ms: 1.91x faster                                                      |
| async_tree_io              | 1.04 sec                                                     | 587 ms: 1.78x faster                                                      |
| async_tree_none_tg         | 431 ms                                                       | 246 ms: 1.75x faster                                                      |
| async_tree_memoization_tg  | 540 ms                                                       | 310 ms: 1.75x faster                                                      |
| async_tree_none            | 452 ms                                                       | 283 ms: 1.59x faster                                                      |
| async_tree_memoization     | 544 ms                                                       | 342 ms: 1.59x faster                                                      |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 477 ms: 1.46x faster                                                      |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 511 ms: 1.36x faster                                                      |
| Geometric mean             | (ref)                                                        | 1.64x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-d2c521a |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 249 ms: 1.06x faster                                                      |
| nbody          | 88.0 ms                                                      | 131 ms: 1.49x slower                                                      |
| Geometric mean | (ref)                                                        | 1.12x slower                                                              |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-d2c521a |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.09 ms: 1.16x faster                                                     |
| regex_v8       | 23.6 ms                                                      | 23.1 ms: 1.02x faster                                                     |
| regex_dna      | 239 ms                                                       | 234 ms: 1.02x faster                                                      |
| regex_compile  | 144 ms                                                       | 161 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                        | 1.02x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-d2c521a |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 88.8 ms: 1.16x faster                                                     |
| xml_etree_parse      | 144 ms                                                       | 136 ms: 1.06x faster                                                      |
| xml_etree_generate   | 86.1 ms                                                      | 97.2 ms: 1.13x slower                                                     |
| tomli_loads          | 2.16 sec                                                     | 2.44 sec: 1.13x slower                                                    |
| pickle_pure_python   | 318 us                                                       | 372 us: 1.17x slower                                                      |
| unpickle_pure_python | 210 us                                                       | 247 us: 1.18x slower                                                      |
| xml_etree_process    | 58.4 ms                                                      | 69.7 ms: 1.19x slower                                                     |
| json_loads           | 24.4 us                                                      | 29.1 us: 1.20x slower                                                     |
| json_dumps           | 10.2 ms                                                      | 13.2 ms: 1.29x slower                                                     |
| Geometric mean       | (ref)                                                        | 1.11x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-d2c521a |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 13.8 ms: 1.60x slower                                                     |
| python_startup         | 11.6 ms                                                      | 19.5 ms: 1.68x slower                                                     |
| Geometric mean         | (ref)                                                        | 1.64x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-d2c521a |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 45.8 ms: 1.20x slower                                                     |
| mako            | 10.0 ms                                                      | 17.6 ms: 1.76x slower                                                     |
| Geometric mean  | (ref)                                                        | 1.45x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-d2c521a |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 551 ms: 1.91x faster                                                      |
| async_tree_io              | 1.04 sec                                                     | 587 ms: 1.78x faster                                                      |
| async_tree_none_tg         | 431 ms                                                       | 246 ms: 1.75x faster                                                      |
| async_tree_memoization_tg  | 540 ms                                                       | 310 ms: 1.75x faster                                                      |
| gc_traversal               | 3.48 ms                                                      | 2.12 ms: 1.64x faster                                                     |
| mdp                        | 2.57 sec                                                     | 1.57 sec: 1.64x faster                                                    |
| async_tree_none            | 452 ms                                                       | 283 ms: 1.59x faster                                                      |
| async_tree_memoization     | 544 ms                                                       | 342 ms: 1.59x faster                                                      |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 477 ms: 1.46x faster                                                      |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 511 ms: 1.36x faster                                                      |
| generators                 | 37.4 ms                                                      | 30.3 ms: 1.24x faster                                                     |
| xml_etree_iterparse        | 103 ms                                                       | 88.8 ms: 1.16x faster                                                     |
| regex_effbot               | 3.57 ms                                                      | 3.09 ms: 1.16x faster                                                     |
| deepcopy                   | 368 us                                                       | 333 us: 1.11x faster                                                      |
| coroutines                 | 23.0 ms                                                      | 21.2 ms: 1.08x faster                                                     |
| pathlib                    | 18.9 ms                                                      | 17.4 ms: 1.08x faster                                                     |
| comprehensions             | 21.9 us                                                      | 20.2 us: 1.08x faster                                                     |
| sqlite_synth               | 2.77 us                                                      | 2.59 us: 1.07x faster                                                     |
| pidigits                   | 265 ms                                                       | 249 ms: 1.06x faster                                                      |
| xml_etree_parse            | 144 ms                                                       | 136 ms: 1.06x faster                                                      |
| regex_v8                   | 23.6 ms                                                      | 23.1 ms: 1.02x faster                                                     |
| regex_dna                  | 239 ms                                                       | 234 ms: 1.02x faster                                                      |
| dulwich_log                | 65.4 ms                                                      | 64.3 ms: 1.02x faster                                                     |
| asyncio_websockets         | 387 ms                                                       | 381 ms: 1.02x faster                                                      |
| go                         | 150 ms                                                       | 151 ms: 1.01x slower                                                      |
| pycparser                  | 1.23 sec                                                     | 1.26 sec: 1.02x slower                                                    |
| docutils                   | 2.87 sec                                                     | 2.94 sec: 1.03x slower                                                    |
| deepcopy_reduce            | 3.37 us                                                      | 3.56 us: 1.06x slower                                                     |
| logging_format             | 7.48 us                                                      | 7.95 us: 1.06x slower                                                     |
| logging_simple             | 6.71 us                                                      | 7.18 us: 1.07x slower                                                     |
| logging_silent             | 94.4 ns                                                      | 101 ns: 1.07x slower                                                      |
| sqlalchemy_declarative     | 159 ms                                                       | 172 ms: 1.08x slower                                                      |
| sympy_sum                  | 162 ms                                                       | 175 ms: 1.08x slower                                                      |
| chaos                      | 64.0 ms                                                      | 69.8 ms: 1.09x slower                                                     |
| sqlalchemy_imperative      | 18.7 ms                                                      | 20.6 ms: 1.10x slower                                                     |
| json                       | 5.12 ms                                                      | 5.64 ms: 1.10x slower                                                     |
| sympy_integrate            | 23.9 ms                                                      | 26.5 ms: 1.11x slower                                                     |
| raytrace                   | 298 ms                                                       | 330 ms: 1.11x slower                                                      |
| spectral_norm              | 91.6 ms                                                      | 102 ms: 1.11x slower                                                      |
| scimark_sor                | 109 ms                                                       | 121 ms: 1.11x slower                                                      |
| sympy_str                  | 302 ms                                                       | 336 ms: 1.11x slower                                                      |
| pprint_safe_repr           | 807 ms                                                       | 900 ms: 1.12x slower                                                      |
| pprint_pformat             | 1.65 sec                                                     | 1.85 sec: 1.12x slower                                                    |
| regex_compile              | 144 ms                                                       | 161 ms: 1.12x slower                                                      |
| xml_etree_generate         | 86.1 ms                                                      | 97.2 ms: 1.13x slower                                                     |
| tomli_loads                | 2.16 sec                                                     | 2.44 sec: 1.13x slower                                                    |
| pyflate                    | 439 ms                                                       | 497 ms: 1.13x slower                                                      |
| 2to3                       | 285 ms                                                       | 325 ms: 1.14x slower                                                      |
| scimark_fft                | 301 ms                                                       | 352 ms: 1.17x slower                                                      |
| sympy_expand               | 484 ms                                                       | 566 ms: 1.17x slower                                                      |
| pickle_pure_python         | 318 us                                                       | 372 us: 1.17x slower                                                      |
| unpickle_pure_python       | 210 us                                                       | 247 us: 1.18x slower                                                      |
| create_gc_cycles           | 1.59 ms                                                      | 1.90 ms: 1.19x slower                                                     |
| async_generators           | 390 ms                                                       | 465 ms: 1.19x slower                                                      |
| xml_etree_process          | 58.4 ms                                                      | 69.7 ms: 1.19x slower                                                     |
| crypto_pyaes               | 80.3 ms                                                      | 96.0 ms: 1.19x slower                                                     |
| json_loads                 | 24.4 us                                                      | 29.1 us: 1.20x slower                                                     |
| django_template            | 38.2 ms                                                      | 45.8 ms: 1.20x slower                                                     |
| meteor_contest             | 128 ms                                                       | 155 ms: 1.21x slower                                                      |
| scimark_monte_carlo        | 69.0 ms                                                      | 83.8 ms: 1.22x slower                                                     |
| nqueens                    | 89.9 ms                                                      | 111 ms: 1.24x slower                                                      |
| scimark_lu                 | 98.8 ms                                                      | 123 ms: 1.24x slower                                                      |
| richards                   | 45.7 ms                                                      | 56.9 ms: 1.24x slower                                                     |
| deltablue                  | 3.24 ms                                                      | 4.04 ms: 1.25x slower                                                     |
| hexiom                     | 5.96 ms                                                      | 7.48 ms: 1.26x slower                                                     |
| richards_super             | 51.3 ms                                                      | 65.7 ms: 1.28x slower                                                     |
| json_dumps                 | 10.2 ms                                                      | 13.2 ms: 1.29x slower                                                     |
| telco                      | 6.96 ms                                                      | 9.46 ms: 1.36x slower                                                     |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.78 ms: 1.37x slower                                                     |
| fannkuch                   | 350 ms                                                       | 483 ms: 1.38x slower                                                      |
| typing_runtime_protocols   | 152 us                                                       | 218 us: 1.44x slower                                                      |
| nbody                      | 88.0 ms                                                      | 131 ms: 1.49x slower                                                      |
| bench_thread_pool          | 950 us                                                       | 1.44 ms: 1.52x slower                                                     |
| python_startup_no_site     | 8.64 ms                                                      | 13.8 ms: 1.60x slower                                                     |
| python_startup             | 11.6 ms                                                      | 19.5 ms: 1.68x slower                                                     |
| coverage                   | 66.7 ms                                                      | 116 ms: 1.74x slower                                                      |
| mako                       | 10.0 ms                                                      | 17.6 ms: 1.76x slower                                                     |
| bench_mp_pool              | 4.76 ms                                                      | 50.4 ms: 10.58x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.08x slower                                                              |

Benchmark hidden because not significant (2): float, deepcopy_memo
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250324-3.14.0a6+-d2c521a-NOGIL/bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-d2c521a.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.043x slower

# HPT report

- Reliability score: 99.35% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.29x