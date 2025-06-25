# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: tos_caching_rebased_
- machine: linux-x86_64
- commit hash: 72be567
- commit date: 2025-06-25
- overall geometric mean: 1.132x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250625-linux-x86_64-Fidget%2dSpinner-tos_caching_rebased_-3.15.0a0-72be567 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 260 ms: 1.06x faster                                                            |
| docutils       | 2.77 sec                                               | 2.65 sec: 1.05x faster                                                          |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250625-linux-x86_64-Fidget%2dSpinner-tos_caching_rebased_-3.15.0a0-72be567 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 600 ms: 1.93x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 615 ms: 1.92x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.83x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 316 ms: 1.83x faster                                                            |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.79x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 487 ms: 1.49x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 493 ms: 1.47x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250625-linux-x86_64-Fidget%2dSpinner-tos_caching_rebased_-3.15.0a0-72be567 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 65.3 ms: 1.30x faster                                                           |
| nbody          | 97.0 ms                                                | 90.2 ms: 1.07x faster                                                           |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250625-linux-x86_64-Fidget%2dSpinner-tos_caching_rebased_-3.15.0a0-72be567 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                            |
| regex_effbot   | 3.61 ms                                                | 3.32 ms: 1.09x faster                                                           |
| regex_dna      | 212 ms                                                 | 214 ms: 1.01x slower                                                            |
| regex_v8       | 23.1 ms                                                | 23.4 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250625-linux-x86_64-Fidget%2dSpinner-tos_caching_rebased_-3.15.0a0-72be567 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.84 sec: 1.27x faster                                                          |
| unpickle_pure_python | 230 us                                                 | 201 us: 1.15x faster                                                            |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                                            |
| xml_etree_process    | 61.7 ms                                                | 55.7 ms: 1.11x faster                                                           |
| xml_etree_generate   | 89.2 ms                                                | 80.8 ms: 1.10x faster                                                           |
| xml_etree_iterparse  | 107 ms                                                 | 99.5 ms: 1.07x faster                                                           |
| pickle_pure_python   | 324 us                                                 | 320 us: 1.01x faster                                                            |
| json_loads           | 28.5 us                                                | 28.8 us: 1.01x slower                                                           |
| json_dumps           | 10.4 ms                                                | 11.0 ms: 1.06x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250625-linux-x86_64-Fidget%2dSpinner-tos_caching_rebased_-3.15.0a0-72be567 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.93 ms: 1.00x faster                                                           |
| python_startup         | 9.55 ms                                                | 12.1 ms: 1.27x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250625-linux-x86_64-Fidget%2dSpinner-tos_caching_rebased_-3.15.0a0-72be567 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.6 ms: 1.12x faster                                                           |
| django_template | 34.6 ms                                                | 32.2 ms: 1.07x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250625-linux-x86_64-Fidget%2dSpinner-tos_caching_rebased_-3.15.0a0-72be567 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.24 sec: 2.12x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 600 ms: 1.93x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 615 ms: 1.92x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.83x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 316 ms: 1.83x faster                                                            |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.79x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 487 ms: 1.49x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 493 ms: 1.47x faster                                                            |
| deepcopy                   | 371 us                                                 | 259 us: 1.43x faster                                                            |
| deepcopy_memo              | 40.7 us                                                | 29.3 us: 1.39x faster                                                           |
| richards                   | 45.8 ms                                                | 33.4 ms: 1.37x faster                                                           |
| richards_super             | 51.5 ms                                                | 39.2 ms: 1.31x faster                                                           |
| float                      | 84.7 ms                                                | 65.3 ms: 1.30x faster                                                           |
| comprehensions             | 21.8 us                                                | 17.1 us: 1.28x faster                                                           |
| tomli_loads                | 2.33 sec                                               | 1.84 sec: 1.27x faster                                                          |
| deepcopy_reduce            | 3.35 us                                                | 2.73 us: 1.23x faster                                                           |
| spectral_norm              | 115 ms                                                 | 93.8 ms: 1.23x faster                                                           |
| scimark_fft                | 382 ms                                                 | 315 ms: 1.21x faster                                                            |
| deltablue                  | 3.72 ms                                                | 3.10 ms: 1.20x faster                                                           |
| pyflate                    | 482 ms                                                 | 407 ms: 1.18x faster                                                            |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                            |
| dulwich_log                | 68.5 ms                                                | 59.2 ms: 1.16x faster                                                           |
| go                         | 139 ms                                                 | 121 ms: 1.15x faster                                                            |
| scimark_monte_carlo        | 75.1 ms                                                | 65.5 ms: 1.15x faster                                                           |
| unpickle_pure_python       | 230 us                                                 | 201 us: 1.15x faster                                                            |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                                            |
| pathlib                    | 19.3 ms                                                | 17.1 ms: 1.13x faster                                                           |
| raytrace                   | 312 ms                                                 | 275 ms: 1.13x faster                                                            |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.13x faster                                                            |
| mako                       | 11.9 ms                                                | 10.6 ms: 1.12x faster                                                           |
| xml_etree_process          | 61.7 ms                                                | 55.7 ms: 1.11x faster                                                           |
| sympy_integrate            | 21.4 ms                                                | 19.3 ms: 1.11x faster                                                           |
| xml_etree_generate         | 89.2 ms                                                | 80.8 ms: 1.10x faster                                                           |
| sympy_str                  | 300 ms                                                 | 272 ms: 1.10x faster                                                            |
| chaos                      | 67.0 ms                                                | 61.1 ms: 1.10x faster                                                           |
| regex_effbot               | 3.61 ms                                                | 3.32 ms: 1.09x faster                                                           |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.09x faster                                                            |
| crypto_pyaes               | 81.9 ms                                                | 75.3 ms: 1.09x faster                                                           |
| nbody                      | 97.0 ms                                                | 90.2 ms: 1.07x faster                                                           |
| async_generators           | 463 ms                                                 | 431 ms: 1.07x faster                                                            |
| django_template            | 34.6 ms                                                | 32.2 ms: 1.07x faster                                                           |
| xml_etree_iterparse        | 107 ms                                                 | 99.5 ms: 1.07x faster                                                           |
| logging_format             | 7.23 us                                                | 6.77 us: 1.07x faster                                                           |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                                            |
| logging_simple             | 6.46 us                                                | 6.05 us: 1.07x faster                                                           |
| fannkuch                   | 417 ms                                                 | 393 ms: 1.06x faster                                                            |
| 2to3                       | 274 ms                                                 | 260 ms: 1.06x faster                                                            |
| docutils                   | 2.77 sec                                               | 2.65 sec: 1.05x faster                                                          |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.02x faster                                                          |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.94 ms: 1.02x faster                                                           |
| sympy_expand               | 478 ms                                                 | 468 ms: 1.02x faster                                                            |
| sqlite_synth               | 2.83 us                                                | 2.79 us: 1.02x faster                                                           |
| pickle_pure_python         | 324 us                                                 | 320 us: 1.01x faster                                                            |
| generators                 | 31.2 ms                                                | 30.9 ms: 1.01x faster                                                           |
| nqueens                    | 83.3 ms                                                | 82.6 ms: 1.01x faster                                                           |
| python_startup_no_site     | 6.94 ms                                                | 6.93 ms: 1.00x faster                                                           |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                            |
| regex_dna                  | 212 ms                                                 | 214 ms: 1.01x slower                                                            |
| json                       | 5.26 ms                                                | 5.31 ms: 1.01x slower                                                           |
| regex_v8                   | 23.1 ms                                                | 23.4 ms: 1.01x slower                                                           |
| hexiom                     | 6.41 ms                                                | 6.48 ms: 1.01x slower                                                           |
| json_loads                 | 28.5 us                                                | 28.8 us: 1.01x slower                                                           |
| json_dumps                 | 10.4 ms                                                | 11.0 ms: 1.06x slower                                                           |
| coroutines                 | 23.2 ms                                                | 24.6 ms: 1.06x slower                                                           |
| pprint_pformat             | 1.57 sec                                               | 1.67 sec: 1.06x slower                                                          |
| pprint_safe_repr           | 776 ms                                                 | 826 ms: 1.06x slower                                                            |
| typing_runtime_protocols   | 158 us                                                 | 170 us: 1.07x slower                                                            |
| telco                      | 7.10 ms                                                | 7.71 ms: 1.09x slower                                                           |
| coverage                   | 72.7 ms                                                | 87.5 ms: 1.20x slower                                                           |
| python_startup             | 9.55 ms                                                | 12.1 ms: 1.27x slower                                                           |
| gc_traversal               | 3.79 ms                                                | 4.93 ms: 1.30x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 2.58 ms: 1.75x slower                                                           |
| logging_silent             | 104 ns                                                 | 476 ns: 4.56x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.11x faster                                                                    |

Benchmark hidden because not significant (2): scimark_lu, asyncio_websockets
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250625-3.15.0a0-72be567-JIT/bm-20250625-linux-x86_64-Fidget%2dSpinner-tos_caching_rebased_-3.15.0a0-72be567.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.132x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.15x