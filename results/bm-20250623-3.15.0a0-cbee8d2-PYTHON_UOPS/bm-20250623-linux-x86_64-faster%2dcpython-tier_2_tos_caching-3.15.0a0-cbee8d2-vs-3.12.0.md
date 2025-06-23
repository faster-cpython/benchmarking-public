# Results vs. 3.12.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: cbee8d2
- commit date: 2025-06-23
- overall geometric mean: 1.032x slower
- HPT reliability: 88.88%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-cbee8d2 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 292 ms: 1.07x slower                                                          |
| docutils       | 2.77 sec                                               | 2.82 sec: 1.02x slower                                                        |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-cbee8d2 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 643 ms: 1.80x faster                                                          |
| async_tree_io_tg           | 1.18 sec                                               | 661 ms: 1.79x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 339 ms: 1.69x faster                                                          |
| async_tree_memoization     | 578 ms                                                 | 341 ms: 1.69x faster                                                          |
| async_tree_none_tg         | 450 ms                                                 | 273 ms: 1.64x faster                                                          |
| async_tree_none            | 472 ms                                                 | 289 ms: 1.63x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 522 ms: 1.39x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 532 ms: 1.36x faster                                                          |
| Geometric mean             | (ref)                                                  | 1.62x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-cbee8d2 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 187 ms                                                 | 193 ms: 1.03x slower                                                          |
| float          | 84.7 ms                                                | 91.9 ms: 1.09x slower                                                         |
| nbody          | 97.0 ms                                                | 176 ms: 1.81x slower                                                          |
| Geometric mean | (ref)                                                  | 1.26x slower                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-cbee8d2 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.22 ms: 1.12x faster                                                         |
| regex_dna      | 212 ms                                                 | 199 ms: 1.07x faster                                                          |
| regex_compile  | 148 ms                                                 | 143 ms: 1.04x faster                                                          |
| regex_v8       | 23.1 ms                                                | 22.4 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-cbee8d2 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.08x faster                                                          |
| xml_etree_iterparse  | 107 ms                                                 | 106 ms: 1.01x faster                                                          |
| json_loads           | 28.5 us                                                | 28.3 us: 1.01x faster                                                         |
| json_dumps           | 10.4 ms                                                | 10.9 ms: 1.05x slower                                                         |
| tomli_loads          | 2.33 sec                                               | 2.48 sec: 1.06x slower                                                        |
| xml_etree_generate   | 89.2 ms                                                | 102 ms: 1.14x slower                                                          |
| xml_etree_process    | 61.7 ms                                                | 72.1 ms: 1.17x slower                                                         |
| pickle_pure_python   | 324 us                                                 | 398 us: 1.23x slower                                                          |
| unpickle_pure_python | 230 us                                                 | 334 us: 1.45x slower                                                          |
| Geometric mean       | (ref)                                                  | 1.10x slower                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-cbee8d2 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.94 ms: 1.00x faster                                                         |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.27x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-cbee8d2 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 33.2 ms: 1.04x faster                                                         |
| mako            | 11.9 ms                                                | 16.6 ms: 1.40x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.16x slower                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-cbee8d2 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.41 sec: 1.87x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 643 ms: 1.80x faster                                                          |
| async_tree_io_tg           | 1.18 sec                                               | 661 ms: 1.79x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 339 ms: 1.69x faster                                                          |
| async_tree_memoization     | 578 ms                                                 | 341 ms: 1.69x faster                                                          |
| async_tree_none_tg         | 450 ms                                                 | 273 ms: 1.64x faster                                                          |
| async_tree_none            | 472 ms                                                 | 289 ms: 1.63x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 522 ms: 1.39x faster                                                          |
| deepcopy                   | 371 us                                                 | 267 us: 1.39x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 532 ms: 1.36x faster                                                          |
| deepcopy_memo              | 40.7 us                                                | 30.1 us: 1.35x faster                                                         |
| deepcopy_reduce            | 3.35 us                                                | 2.79 us: 1.20x faster                                                         |
| pathlib                    | 19.3 ms                                                | 17.3 ms: 1.12x faster                                                         |
| regex_effbot               | 3.61 ms                                                | 3.22 ms: 1.12x faster                                                         |
| dulwich_log                | 68.5 ms                                                | 62.0 ms: 1.10x faster                                                         |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.08x faster                                                          |
| scimark_sor                | 129 ms                                                 | 121 ms: 1.07x faster                                                          |
| async_generators           | 463 ms                                                 | 434 ms: 1.07x faster                                                          |
| regex_dna                  | 212 ms                                                 | 199 ms: 1.07x faster                                                          |
| sympy_sum                  | 169 ms                                                 | 159 ms: 1.06x faster                                                          |
| sympy_integrate            | 21.4 ms                                                | 20.4 ms: 1.05x faster                                                         |
| logging_format             | 7.23 us                                                | 6.89 us: 1.05x faster                                                         |
| logging_simple             | 6.46 us                                                | 6.17 us: 1.05x faster                                                         |
| django_template            | 34.6 ms                                                | 33.2 ms: 1.04x faster                                                         |
| regex_compile              | 148 ms                                                 | 143 ms: 1.04x faster                                                          |
| regex_v8                   | 23.1 ms                                                | 22.4 ms: 1.03x faster                                                         |
| sympy_str                  | 300 ms                                                 | 291 ms: 1.03x faster                                                          |
| generators                 | 31.2 ms                                                | 30.5 ms: 1.02x faster                                                         |
| chaos                      | 67.0 ms                                                | 66.4 ms: 1.01x faster                                                         |
| xml_etree_iterparse        | 107 ms                                                 | 106 ms: 1.01x faster                                                          |
| json_loads                 | 28.5 us                                                | 28.3 us: 1.01x faster                                                         |
| python_startup_no_site     | 6.94 ms                                                | 6.94 ms: 1.00x faster                                                         |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                          |
| docutils                   | 2.77 sec                                               | 2.82 sec: 1.02x slower                                                        |
| pidigits                   | 187 ms                                                 | 193 ms: 1.03x slower                                                          |
| sqlite_synth               | 2.83 us                                                | 2.98 us: 1.05x slower                                                         |
| raytrace                   | 312 ms                                                 | 329 ms: 1.05x slower                                                          |
| json_dumps                 | 10.4 ms                                                | 10.9 ms: 1.05x slower                                                         |
| tomli_loads                | 2.33 sec                                               | 2.48 sec: 1.06x slower                                                        |
| 2to3                       | 274 ms                                                 | 292 ms: 1.07x slower                                                          |
| sympy_expand               | 478 ms                                                 | 511 ms: 1.07x slower                                                          |
| coroutines                 | 23.2 ms                                                | 25.0 ms: 1.08x slower                                                         |
| float                      | 84.7 ms                                                | 91.9 ms: 1.09x slower                                                         |
| nqueens                    | 83.3 ms                                                | 91.6 ms: 1.10x slower                                                         |
| scimark_monte_carlo        | 75.1 ms                                                | 82.9 ms: 1.10x slower                                                         |
| xml_etree_generate         | 89.2 ms                                                | 102 ms: 1.14x slower                                                          |
| richards_super             | 51.5 ms                                                | 59.6 ms: 1.16x slower                                                         |
| comprehensions             | 21.8 us                                                | 25.3 us: 1.16x slower                                                         |
| xml_etree_process          | 61.7 ms                                                | 72.1 ms: 1.17x slower                                                         |
| pyflate                    | 482 ms                                                 | 573 ms: 1.19x slower                                                          |
| coverage                   | 72.7 ms                                                | 86.4 ms: 1.19x slower                                                         |
| meteor_contest             | 112 ms                                                 | 135 ms: 1.20x slower                                                          |
| richards                   | 45.8 ms                                                | 56.0 ms: 1.22x slower                                                         |
| spectral_norm              | 115 ms                                                 | 141 ms: 1.23x slower                                                          |
| pycparser                  | 1.18 sec                                               | 1.45 sec: 1.23x slower                                                        |
| pickle_pure_python         | 324 us                                                 | 398 us: 1.23x slower                                                          |
| scimark_fft                | 382 ms                                                 | 472 ms: 1.23x slower                                                          |
| typing_runtime_protocols   | 158 us                                                 | 200 us: 1.27x slower                                                          |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.27x slower                                                         |
| crypto_pyaes               | 81.9 ms                                                | 105 ms: 1.28x slower                                                          |
| telco                      | 7.10 ms                                                | 9.25 ms: 1.30x slower                                                         |
| gc_traversal               | 3.79 ms                                                | 4.96 ms: 1.31x slower                                                         |
| deltablue                  | 3.72 ms                                                | 4.96 ms: 1.34x slower                                                         |
| fannkuch                   | 417 ms                                                 | 564 ms: 1.35x slower                                                          |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 6.97 ms: 1.38x slower                                                         |
| mako                       | 11.9 ms                                                | 16.6 ms: 1.40x slower                                                         |
| unpickle_pure_python       | 230 us                                                 | 334 us: 1.45x slower                                                          |
| pprint_safe_repr           | 776 ms                                                 | 1.13 sec: 1.46x slower                                                        |
| go                         | 139 ms                                                 | 207 ms: 1.48x slower                                                          |
| pprint_pformat             | 1.57 sec                                               | 2.36 sec: 1.50x slower                                                        |
| hexiom                     | 6.41 ms                                                | 9.66 ms: 1.51x slower                                                         |
| create_gc_cycles           | 1.48 ms                                                | 2.60 ms: 1.76x slower                                                         |
| nbody                      | 97.0 ms                                                | 176 ms: 1.81x slower                                                          |
| logging_silent             | 104 ns                                                 | 476 ns: 4.55x slower                                                          |
| Geometric mean             | (ref)                                                  | 1.05x slower                                                                  |

Benchmark hidden because not significant (2): json, scimark_lu
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250623-3.15.0a0-cbee8d2-PYTHON_UOPS/bm-20250623-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-cbee8d2.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.032x slower

# HPT report

- Reliability score: 88.88% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.14x