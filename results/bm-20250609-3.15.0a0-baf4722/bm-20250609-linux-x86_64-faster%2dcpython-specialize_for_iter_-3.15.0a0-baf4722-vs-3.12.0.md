# Results vs. 3.12.0

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: linux-x86_64
- commit hash: baf4722
- commit date: 2025-06-09
- overall geometric mean: 1.089x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250609-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 254 ms: 1.08x faster                                                            |
| docutils       | 2.77 sec                                               | 2.59 sec: 1.07x faster                                                          |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250609-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 595 ms: 1.94x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 619 ms: 1.91x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                            |
| async_tree_none            | 472 ms                                                 | 260 ms: 1.81x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.80x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 483 ms: 1.50x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 491 ms: 1.48x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.76x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250609-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 73.7 ms: 1.15x faster                                                           |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                    |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250609-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.16x faster                                                            |
| regex_effbot   | 3.61 ms                                                | 3.29 ms: 1.10x faster                                                           |
| regex_dna      | 212 ms                                                 | 207 ms: 1.02x faster                                                            |
| regex_v8       | 23.1 ms                                                | 23.4 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250609-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.03 sec: 1.15x faster                                                          |
| xml_etree_parse      | 159 ms                                                 | 142 ms: 1.12x faster                                                            |
| xml_etree_iterparse  | 107 ms                                                 | 99.4 ms: 1.07x faster                                                           |
| unpickle_pure_python | 230 us                                                 | 220 us: 1.05x faster                                                            |
| xml_etree_generate   | 89.2 ms                                                | 85.2 ms: 1.05x faster                                                           |
| xml_etree_process    | 61.7 ms                                                | 60.1 ms: 1.03x faster                                                           |
| pickle_pure_python   | 324 us                                                 | 318 us: 1.02x faster                                                            |
| json_loads           | 28.5 us                                                | 28.1 us: 1.01x faster                                                           |
| json_dumps           | 10.4 ms                                                | 11.0 ms: 1.06x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250609-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.90 ms: 1.01x faster                                                           |
| python_startup         | 9.55 ms                                                | 12.1 ms: 1.27x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250609-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.2 ms: 1.06x faster                                                           |
| django_template | 34.6 ms                                                | 32.8 ms: 1.06x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250609-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.23 sec: 2.15x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 595 ms: 1.94x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 619 ms: 1.91x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                            |
| async_tree_none            | 472 ms                                                 | 260 ms: 1.81x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.80x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 483 ms: 1.50x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 491 ms: 1.48x faster                                                            |
| deepcopy                   | 371 us                                                 | 258 us: 1.44x faster                                                            |
| deepcopy_memo              | 40.7 us                                                | 29.6 us: 1.38x faster                                                           |
| comprehensions             | 21.8 us                                                | 16.1 us: 1.35x faster                                                           |
| deepcopy_reduce            | 3.35 us                                                | 2.66 us: 1.26x faster                                                           |
| go                         | 139 ms                                                 | 112 ms: 1.25x faster                                                            |
| regex_compile              | 148 ms                                                 | 127 ms: 1.16x faster                                                            |
| pathlib                    | 19.3 ms                                                | 16.7 ms: 1.16x faster                                                           |
| dulwich_log                | 68.5 ms                                                | 59.3 ms: 1.16x faster                                                           |
| tomli_loads                | 2.33 sec                                               | 2.03 sec: 1.15x faster                                                          |
| float                      | 84.7 ms                                                | 73.7 ms: 1.15x faster                                                           |
| raytrace                   | 312 ms                                                 | 272 ms: 1.15x faster                                                            |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                                            |
| async_generators           | 463 ms                                                 | 410 ms: 1.13x faster                                                            |
| sympy_integrate            | 21.4 ms                                                | 19.0 ms: 1.12x faster                                                           |
| pyflate                    | 482 ms                                                 | 430 ms: 1.12x faster                                                            |
| sympy_str                  | 300 ms                                                 | 267 ms: 1.12x faster                                                            |
| xml_etree_parse            | 159 ms                                                 | 142 ms: 1.12x faster                                                            |
| chaos                      | 67.0 ms                                                | 60.0 ms: 1.12x faster                                                           |
| scimark_monte_carlo        | 75.1 ms                                                | 68.1 ms: 1.10x faster                                                           |
| regex_effbot               | 3.61 ms                                                | 3.29 ms: 1.10x faster                                                           |
| crypto_pyaes               | 81.9 ms                                                | 75.7 ms: 1.08x faster                                                           |
| 2to3                       | 274 ms                                                 | 254 ms: 1.08x faster                                                            |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.08x faster                                                            |
| xml_etree_iterparse        | 107 ms                                                 | 99.4 ms: 1.07x faster                                                           |
| hexiom                     | 6.41 ms                                                | 5.98 ms: 1.07x faster                                                           |
| docutils                   | 2.77 sec                                               | 2.59 sec: 1.07x faster                                                          |
| logging_format             | 7.23 us                                                | 6.78 us: 1.07x faster                                                           |
| richards                   | 45.8 ms                                                | 43.0 ms: 1.07x faster                                                           |
| mako                       | 11.9 ms                                                | 11.2 ms: 1.06x faster                                                           |
| logging_simple             | 6.46 us                                                | 6.10 us: 1.06x faster                                                           |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                            |
| sympy_expand               | 478 ms                                                 | 452 ms: 1.06x faster                                                            |
| django_template            | 34.6 ms                                                | 32.8 ms: 1.06x faster                                                           |
| generators                 | 31.2 ms                                                | 29.6 ms: 1.05x faster                                                           |
| deltablue                  | 3.72 ms                                                | 3.54 ms: 1.05x faster                                                           |
| unpickle_pure_python       | 230 us                                                 | 220 us: 1.05x faster                                                            |
| xml_etree_generate         | 89.2 ms                                                | 85.2 ms: 1.05x faster                                                           |
| richards_super             | 51.5 ms                                                | 49.6 ms: 1.04x faster                                                           |
| spectral_norm              | 115 ms                                                 | 111 ms: 1.04x faster                                                            |
| nqueens                    | 83.3 ms                                                | 80.4 ms: 1.04x faster                                                           |
| xml_etree_process          | 61.7 ms                                                | 60.1 ms: 1.03x faster                                                           |
| regex_dna                  | 212 ms                                                 | 207 ms: 1.02x faster                                                            |
| pickle_pure_python         | 324 us                                                 | 318 us: 1.02x faster                                                            |
| json_loads                 | 28.5 us                                                | 28.1 us: 1.01x faster                                                           |
| pycparser                  | 1.18 sec                                               | 1.17 sec: 1.01x faster                                                          |
| json                       | 5.26 ms                                                | 5.20 ms: 1.01x faster                                                           |
| fannkuch                   | 417 ms                                                 | 413 ms: 1.01x faster                                                            |
| python_startup_no_site     | 6.94 ms                                                | 6.90 ms: 1.01x faster                                                           |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                            |
| sqlite_synth               | 2.83 us                                                | 2.86 us: 1.01x slower                                                           |
| regex_v8                   | 23.1 ms                                                | 23.4 ms: 1.01x slower                                                           |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.15 ms: 1.02x slower                                                           |
| pprint_safe_repr           | 776 ms                                                 | 806 ms: 1.04x slower                                                            |
| pprint_pformat             | 1.57 sec                                               | 1.64 sec: 1.05x slower                                                          |
| json_dumps                 | 10.4 ms                                                | 11.0 ms: 1.06x slower                                                           |
| typing_runtime_protocols   | 158 us                                                 | 169 us: 1.07x slower                                                            |
| coroutines                 | 23.2 ms                                                | 24.7 ms: 1.07x slower                                                           |
| telco                      | 7.10 ms                                                | 8.05 ms: 1.13x slower                                                           |
| python_startup             | 9.55 ms                                                | 12.1 ms: 1.27x slower                                                           |
| gc_traversal               | 3.79 ms                                                | 5.07 ms: 1.34x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 2.58 ms: 1.75x slower                                                           |
| logging_silent             | 104 ns                                                 | 471 ns: 4.51x slower                                                            |
| coverage                   | 72.7 ms                                                | 421 ms: 5.79x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                                    |

Benchmark hidden because not significant (4): nbody, scimark_fft, asyncio_websockets, scimark_lu
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250609-3.15.0a0-baf4722/bm-20250609-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.089x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.13x