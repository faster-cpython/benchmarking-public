# Results vs. 3.12.0

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: linux-x86_64
- commit hash: 06c1680
- commit date: 2025-06-03
- overall geometric mean: 1.082x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 256 ms: 1.07x faster                                                            |
| docutils       | 2.77 sec                                               | 2.58 sec: 1.07x faster                                                          |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 598 ms: 1.93x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 615 ms: 1.92x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                            |
| async_tree_none            | 472 ms                                                 | 260 ms: 1.81x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 497 ms: 1.46x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 505 ms: 1.44x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 73.2 ms: 1.16x faster                                                           |
| pidigits       | 187 ms                                                 | 192 ms: 1.03x slower                                                            |
| nbody          | 97.0 ms                                                | 102 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                            |
| regex_effbot   | 3.61 ms                                                | 3.26 ms: 1.11x faster                                                           |
| regex_dna      | 212 ms                                                 | 205 ms: 1.03x faster                                                            |
| regex_v8       | 23.1 ms                                                | 23.2 ms: 1.00x slower                                                           |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.03 sec: 1.15x faster                                                          |
| xml_etree_parse      | 159 ms                                                 | 142 ms: 1.12x faster                                                            |
| xml_etree_iterparse  | 107 ms                                                 | 99.3 ms: 1.08x faster                                                           |
| xml_etree_generate   | 89.2 ms                                                | 85.6 ms: 1.04x faster                                                           |
| unpickle_pure_python | 230 us                                                 | 222 us: 1.04x faster                                                            |
| xml_etree_process    | 61.7 ms                                                | 60.4 ms: 1.02x faster                                                           |
| pickle_pure_python   | 324 us                                                 | 322 us: 1.01x faster                                                            |
| json_dumps           | 10.4 ms                                                | 11.0 ms: 1.05x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                    |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.92 ms: 1.00x faster                                                           |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.27x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.3 ms: 1.07x faster                                                           |
| mako            | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.24 sec: 2.13x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 598 ms: 1.93x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 615 ms: 1.92x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                            |
| async_tree_none            | 472 ms                                                 | 260 ms: 1.81x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 497 ms: 1.46x faster                                                            |
| deepcopy                   | 371 us                                                 | 257 us: 1.44x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 505 ms: 1.44x faster                                                            |
| deepcopy_memo              | 40.7 us                                                | 29.4 us: 1.39x faster                                                           |
| comprehensions             | 21.8 us                                                | 16.2 us: 1.35x faster                                                           |
| go                         | 139 ms                                                 | 113 ms: 1.23x faster                                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.72 us: 1.23x faster                                                           |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                            |
| float                      | 84.7 ms                                                | 73.2 ms: 1.16x faster                                                           |
| dulwich_log                | 68.5 ms                                                | 59.6 ms: 1.15x faster                                                           |
| tomli_loads                | 2.33 sec                                               | 2.03 sec: 1.15x faster                                                          |
| raytrace                   | 312 ms                                                 | 273 ms: 1.14x faster                                                            |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                                            |
| sympy_integrate            | 21.4 ms                                                | 19.0 ms: 1.13x faster                                                           |
| async_generators           | 463 ms                                                 | 412 ms: 1.12x faster                                                            |
| xml_etree_parse            | 159 ms                                                 | 142 ms: 1.12x faster                                                            |
| sympy_str                  | 300 ms                                                 | 267 ms: 1.12x faster                                                            |
| chaos                      | 67.0 ms                                                | 60.2 ms: 1.11x faster                                                           |
| regex_effbot               | 3.61 ms                                                | 3.26 ms: 1.11x faster                                                           |
| pathlib                    | 19.3 ms                                                | 17.6 ms: 1.10x faster                                                           |
| pyflate                    | 482 ms                                                 | 446 ms: 1.08x faster                                                            |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.08x faster                                                            |
| xml_etree_iterparse        | 107 ms                                                 | 99.3 ms: 1.08x faster                                                           |
| crypto_pyaes               | 81.9 ms                                                | 76.2 ms: 1.07x faster                                                           |
| scimark_monte_carlo        | 75.1 ms                                                | 69.9 ms: 1.07x faster                                                           |
| 2to3                       | 274 ms                                                 | 256 ms: 1.07x faster                                                            |
| docutils                   | 2.77 sec                                               | 2.58 sec: 1.07x faster                                                          |
| django_template            | 34.6 ms                                                | 32.3 ms: 1.07x faster                                                           |
| logging_format             | 7.23 us                                                | 6.82 us: 1.06x faster                                                           |
| richards                   | 45.8 ms                                                | 43.5 ms: 1.05x faster                                                           |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                           |
| sympy_expand               | 478 ms                                                 | 455 ms: 1.05x faster                                                            |
| deltablue                  | 3.72 ms                                                | 3.54 ms: 1.05x faster                                                           |
| logging_simple             | 6.46 us                                                | 6.15 us: 1.05x faster                                                           |
| hexiom                     | 6.41 ms                                                | 6.11 ms: 1.05x faster                                                           |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                            |
| xml_etree_generate         | 89.2 ms                                                | 85.6 ms: 1.04x faster                                                           |
| richards_super             | 51.5 ms                                                | 49.5 ms: 1.04x faster                                                           |
| spectral_norm              | 115 ms                                                 | 111 ms: 1.04x faster                                                            |
| unpickle_pure_python       | 230 us                                                 | 222 us: 1.04x faster                                                            |
| regex_dna                  | 212 ms                                                 | 205 ms: 1.03x faster                                                            |
| generators                 | 31.2 ms                                                | 30.2 ms: 1.03x faster                                                           |
| nqueens                    | 83.3 ms                                                | 81.4 ms: 1.02x faster                                                           |
| xml_etree_process          | 61.7 ms                                                | 60.4 ms: 1.02x faster                                                           |
| json                       | 5.26 ms                                                | 5.21 ms: 1.01x faster                                                           |
| pickle_pure_python         | 324 us                                                 | 322 us: 1.01x faster                                                            |
| python_startup_no_site     | 6.94 ms                                                | 6.92 ms: 1.00x faster                                                           |
| regex_v8                   | 23.1 ms                                                | 23.2 ms: 1.00x slower                                                           |
| fannkuch                   | 417 ms                                                 | 419 ms: 1.01x slower                                                            |
| scimark_lu                 | 118 ms                                                 | 119 ms: 1.01x slower                                                            |
| sqlite_synth               | 2.83 us                                                | 2.87 us: 1.01x slower                                                           |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.14 ms: 1.02x slower                                                           |
| pidigits                   | 187 ms                                                 | 192 ms: 1.03x slower                                                            |
| pprint_safe_repr           | 776 ms                                                 | 811 ms: 1.05x slower                                                            |
| nbody                      | 97.0 ms                                                | 102 ms: 1.05x slower                                                            |
| pprint_pformat             | 1.57 sec                                               | 1.65 sec: 1.05x slower                                                          |
| json_dumps                 | 10.4 ms                                                | 11.0 ms: 1.05x slower                                                           |
| typing_runtime_protocols   | 158 us                                                 | 170 us: 1.07x slower                                                            |
| coroutines                 | 23.2 ms                                                | 25.6 ms: 1.11x slower                                                           |
| telco                      | 7.10 ms                                                | 7.99 ms: 1.13x slower                                                           |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.27x slower                                                           |
| gc_traversal               | 3.79 ms                                                | 4.93 ms: 1.30x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 2.59 ms: 1.75x slower                                                           |
| logging_silent             | 104 ns                                                 | 478 ns: 4.58x slower                                                            |
| coverage                   | 72.7 ms                                                | 442 ms: 6.08x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                                    |

Benchmark hidden because not significant (4): json_loads, pycparser, scimark_fft, asyncio_websockets
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250603-3.15.0a0-06c1680/bm-20250603-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.082x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.13x