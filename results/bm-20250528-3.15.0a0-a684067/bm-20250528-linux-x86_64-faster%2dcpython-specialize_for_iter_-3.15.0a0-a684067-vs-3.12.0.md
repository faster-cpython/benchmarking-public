# Results vs. 3.12.0

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: linux-x86_64
- commit hash: a684067
- commit date: 2025-05-28
- overall geometric mean: 1.079x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250528-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 254 ms: 1.08x faster                                                            |
| docutils       | 2.77 sec                                               | 2.57 sec: 1.08x faster                                                          |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250528-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 600 ms: 1.93x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 620 ms: 1.91x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 315 ms: 1.83x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 318 ms: 1.81x faster                                                            |
| async_tree_none            | 472 ms                                                 | 263 ms: 1.80x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 483 ms: 1.50x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 493 ms: 1.47x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250528-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 71.4 ms: 1.19x faster                                                           |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                            |
| nbody          | 97.0 ms                                                | 100 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250528-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                            |
| regex_effbot   | 3.61 ms                                                | 3.22 ms: 1.12x faster                                                           |
| regex_dna      | 212 ms                                                 | 210 ms: 1.01x faster                                                            |
| regex_v8       | 23.1 ms                                                | 23.5 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250528-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.98 sec: 1.18x faster                                                          |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                                            |
| xml_etree_iterparse  | 107 ms                                                 | 99.0 ms: 1.08x faster                                                           |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                            |
| xml_etree_generate   | 89.2 ms                                                | 84.4 ms: 1.06x faster                                                           |
| xml_etree_process    | 61.7 ms                                                | 59.9 ms: 1.03x faster                                                           |
| pickle_pure_python   | 324 us                                                 | 316 us: 1.02x faster                                                            |
| json_loads           | 28.5 us                                                | 29.0 us: 1.02x slower                                                           |
| json_dumps           | 10.4 ms                                                | 11.0 ms: 1.06x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250528-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.92 ms: 1.00x faster                                                           |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.28x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250528-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.3 ms: 1.06x faster                                                           |
| django_template | 34.6 ms                                                | 32.8 ms: 1.06x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250528-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.22 sec: 2.16x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 600 ms: 1.93x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 620 ms: 1.91x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 315 ms: 1.83x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 318 ms: 1.81x faster                                                            |
| async_tree_none            | 472 ms                                                 | 263 ms: 1.80x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 483 ms: 1.50x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 493 ms: 1.47x faster                                                            |
| deepcopy                   | 371 us                                                 | 254 us: 1.46x faster                                                            |
| deepcopy_memo              | 40.7 us                                                | 29.5 us: 1.38x faster                                                           |
| comprehensions             | 21.8 us                                                | 16.1 us: 1.35x faster                                                           |
| go                         | 139 ms                                                 | 111 ms: 1.25x faster                                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.68 us: 1.25x faster                                                           |
| float                      | 84.7 ms                                                | 71.4 ms: 1.19x faster                                                           |
| tomli_loads                | 2.33 sec                                               | 1.98 sec: 1.18x faster                                                          |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                            |
| raytrace                   | 312 ms                                                 | 269 ms: 1.16x faster                                                            |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                                            |
| async_generators           | 463 ms                                                 | 403 ms: 1.15x faster                                                            |
| dulwich_log                | 68.5 ms                                                | 60.0 ms: 1.14x faster                                                           |
| pyflate                    | 482 ms                                                 | 423 ms: 1.14x faster                                                            |
| sympy_integrate            | 21.4 ms                                                | 18.9 ms: 1.13x faster                                                           |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                            |
| pathlib                    | 19.3 ms                                                | 17.1 ms: 1.13x faster                                                           |
| sympy_str                  | 300 ms                                                 | 265 ms: 1.13x faster                                                            |
| regex_effbot               | 3.61 ms                                                | 3.22 ms: 1.12x faster                                                           |
| chaos                      | 67.0 ms                                                | 60.1 ms: 1.11x faster                                                           |
| crypto_pyaes               | 81.9 ms                                                | 74.0 ms: 1.11x faster                                                           |
| scimark_monte_carlo        | 75.1 ms                                                | 68.1 ms: 1.10x faster                                                           |
| deltablue                  | 3.72 ms                                                | 3.43 ms: 1.08x faster                                                           |
| xml_etree_iterparse        | 107 ms                                                 | 99.0 ms: 1.08x faster                                                           |
| 2to3                       | 274 ms                                                 | 254 ms: 1.08x faster                                                            |
| meteor_contest             | 112 ms                                                 | 104 ms: 1.08x faster                                                            |
| docutils                   | 2.77 sec                                               | 2.57 sec: 1.08x faster                                                          |
| logging_format             | 7.23 us                                                | 6.71 us: 1.08x faster                                                           |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.07x faster                                                            |
| hexiom                     | 6.41 ms                                                | 5.99 ms: 1.07x faster                                                           |
| richards                   | 45.8 ms                                                | 42.8 ms: 1.07x faster                                                           |
| sympy_expand               | 478 ms                                                 | 448 ms: 1.07x faster                                                            |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                            |
| pycparser                  | 1.18 sec                                               | 1.11 sec: 1.06x faster                                                          |
| logging_simple             | 6.46 us                                                | 6.11 us: 1.06x faster                                                           |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.06x faster                                                           |
| xml_etree_generate         | 89.2 ms                                                | 84.4 ms: 1.06x faster                                                           |
| django_template            | 34.6 ms                                                | 32.8 ms: 1.06x faster                                                           |
| generators                 | 31.2 ms                                                | 29.6 ms: 1.05x faster                                                           |
| spectral_norm              | 115 ms                                                 | 109 ms: 1.05x faster                                                            |
| richards_super             | 51.5 ms                                                | 49.2 ms: 1.05x faster                                                           |
| nqueens                    | 83.3 ms                                                | 80.2 ms: 1.04x faster                                                           |
| xml_etree_process          | 61.7 ms                                                | 59.9 ms: 1.03x faster                                                           |
| scimark_fft                | 382 ms                                                 | 372 ms: 1.03x faster                                                            |
| json                       | 5.26 ms                                                | 5.14 ms: 1.02x faster                                                           |
| pickle_pure_python         | 324 us                                                 | 316 us: 1.02x faster                                                            |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.98 ms: 1.02x faster                                                           |
| regex_dna                  | 212 ms                                                 | 210 ms: 1.01x faster                                                            |
| fannkuch                   | 417 ms                                                 | 413 ms: 1.01x faster                                                            |
| python_startup_no_site     | 6.94 ms                                                | 6.92 ms: 1.00x faster                                                           |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                            |
| regex_v8                   | 23.1 ms                                                | 23.5 ms: 1.01x slower                                                           |
| pprint_safe_repr           | 776 ms                                                 | 787 ms: 1.01x slower                                                            |
| sqlite_synth               | 2.83 us                                                | 2.88 us: 1.02x slower                                                           |
| scimark_lu                 | 118 ms                                                 | 120 ms: 1.02x slower                                                            |
| json_loads                 | 28.5 us                                                | 29.0 us: 1.02x slower                                                           |
| pprint_pformat             | 1.57 sec                                               | 1.61 sec: 1.03x slower                                                          |
| nbody                      | 97.0 ms                                                | 100 ms: 1.03x slower                                                            |
| bench_thread_pool          | 842 us                                                 | 886 us: 1.05x slower                                                            |
| json_dumps                 | 10.4 ms                                                | 11.0 ms: 1.06x slower                                                           |
| typing_runtime_protocols   | 158 us                                                 | 169 us: 1.07x slower                                                            |
| coroutines                 | 23.2 ms                                                | 25.6 ms: 1.11x slower                                                           |
| telco                      | 7.10 ms                                                | 7.99 ms: 1.12x slower                                                           |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.28x slower                                                           |
| gc_traversal               | 3.79 ms                                                | 5.18 ms: 1.37x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 2.59 ms: 1.76x slower                                                           |
| dask                       | 372 ms                                                 | 909 ms: 2.44x slower                                                            |
| bench_mp_pool              | 24.0 ms                                                | 92.9 ms: 3.87x slower                                                           |
| logging_silent             | 104 ns                                                 | 471 ns: 4.51x slower                                                            |
| coverage                   | 72.7 ms                                                | 423 ms: 5.82x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (24) of results/bm-20250528-3.15.0a0-a684067/bm-20250528-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.079x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.13x