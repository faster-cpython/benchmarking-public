# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_up_7_6
- machine: linux-x86_64
- commit hash: b88f481
- commit date: 2025-07-01
- overall geometric mean: 1.144x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_6-3.15.0a0-b88f481 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 265 ms: 1.03x faster                                              |
| docutils       | 2.77 sec                                               | 2.67 sec: 1.04x faster                                            |
| Geometric mean | (ref)                                                  | 1.04x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_6-3.15.0a0-b88f481 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 603 ms: 1.92x faster                                              |
| async_tree_io_tg           | 1.18 sec                                               | 637 ms: 1.86x faster                                              |
| async_tree_memoization_tg  | 575 ms                                                 | 311 ms: 1.85x faster                                              |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.84x faster                                              |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.81x faster                                              |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                              |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 483 ms: 1.50x faster                                              |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 492 ms: 1.48x faster                                              |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_6-3.15.0a0-b88f481 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 84.7 ms                                                | 65.7 ms: 1.29x faster                                             |
| nbody          | 97.0 ms                                                | 93.0 ms: 1.04x faster                                             |
| pidigits       | 187 ms                                                 | 196 ms: 1.05x slower                                              |
| Geometric mean | (ref)                                                  | 1.09x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_6-3.15.0a0-b88f481 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                              |
| regex_effbot   | 3.61 ms                                                | 3.32 ms: 1.09x faster                                             |
| regex_dna      | 212 ms                                                 | 202 ms: 1.05x faster                                              |
| regex_v8       | 23.1 ms                                                | 22.5 ms: 1.03x faster                                             |
| Geometric mean | (ref)                                                  | 1.08x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_6-3.15.0a0-b88f481 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.84 sec: 1.26x faster                                            |
| unpickle_pure_python | 230 us                                                 | 196 us: 1.18x faster                                              |
| xml_etree_parse      | 159 ms                                                 | 139 ms: 1.14x faster                                              |
| xml_etree_generate   | 89.2 ms                                                | 80.4 ms: 1.11x faster                                             |
| xml_etree_process    | 61.7 ms                                                | 55.8 ms: 1.11x faster                                             |
| xml_etree_iterparse  | 107 ms                                                 | 98.2 ms: 1.09x faster                                             |
| pickle_pure_python   | 324 us                                                 | 321 us: 1.01x faster                                              |
| json_loads           | 28.5 us                                                | 28.3 us: 1.01x faster                                             |
| json_dumps           | 10.4 ms                                                | 11.0 ms: 1.06x slower                                             |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_6-3.15.0a0-b88f481 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.94 ms: 1.00x slower                                             |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.27x slower                                             |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_6-3.15.0a0-b88f481 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.5 ms: 1.13x faster                                             |
| django_template | 34.6 ms                                                | 32.7 ms: 1.06x faster                                             |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_6-3.15.0a0-b88f481 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.23 sec: 2.14x faster                                            |
| async_tree_io              | 1.16 sec                                               | 603 ms: 1.92x faster                                              |
| async_tree_io_tg           | 1.18 sec                                               | 637 ms: 1.86x faster                                              |
| async_tree_memoization_tg  | 575 ms                                                 | 311 ms: 1.85x faster                                              |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.84x faster                                              |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.81x faster                                              |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                              |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 483 ms: 1.50x faster                                              |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 492 ms: 1.48x faster                                              |
| richards                   | 45.8 ms                                                | 31.3 ms: 1.47x faster                                             |
| deepcopy                   | 371 us                                                 | 259 us: 1.43x faster                                              |
| richards_super             | 51.5 ms                                                | 36.2 ms: 1.42x faster                                             |
| deepcopy_memo              | 40.7 us                                                | 29.7 us: 1.37x faster                                             |
| comprehensions             | 21.8 us                                                | 16.4 us: 1.33x faster                                             |
| float                      | 84.7 ms                                                | 65.7 ms: 1.29x faster                                             |
| tomli_loads                | 2.33 sec                                               | 1.84 sec: 1.26x faster                                            |
| spectral_norm              | 115 ms                                                 | 92.2 ms: 1.25x faster                                             |
| go                         | 139 ms                                                 | 114 ms: 1.23x faster                                              |
| deltablue                  | 3.72 ms                                                | 3.05 ms: 1.22x faster                                             |
| deepcopy_reduce            | 3.35 us                                                | 2.75 us: 1.22x faster                                             |
| scimark_fft                | 382 ms                                                 | 315 ms: 1.21x faster                                              |
| pyflate                    | 482 ms                                                 | 406 ms: 1.19x faster                                              |
| unpickle_pure_python       | 230 us                                                 | 196 us: 1.18x faster                                              |
| logging_format             | 7.23 us                                                | 6.26 us: 1.16x faster                                             |
| raytrace                   | 312 ms                                                 | 271 ms: 1.15x faster                                              |
| logging_simple             | 6.46 us                                                | 5.61 us: 1.15x faster                                             |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                              |
| dulwich_log                | 68.5 ms                                                | 59.7 ms: 1.15x faster                                             |
| xml_etree_parse            | 159 ms                                                 | 139 ms: 1.14x faster                                              |
| scimark_monte_carlo        | 75.1 ms                                                | 66.2 ms: 1.13x faster                                             |
| mako                       | 11.9 ms                                                | 10.5 ms: 1.13x faster                                             |
| pathlib                    | 19.3 ms                                                | 17.2 ms: 1.12x faster                                             |
| crypto_pyaes               | 81.9 ms                                                | 73.8 ms: 1.11x faster                                             |
| xml_etree_generate         | 89.2 ms                                                | 80.4 ms: 1.11x faster                                             |
| chaos                      | 67.0 ms                                                | 60.4 ms: 1.11x faster                                             |
| xml_etree_process          | 61.7 ms                                                | 55.8 ms: 1.11x faster                                             |
| sympy_sum                  | 169 ms                                                 | 154 ms: 1.10x faster                                              |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.10x faster                                              |
| sympy_str                  | 300 ms                                                 | 274 ms: 1.09x faster                                              |
| regex_effbot               | 3.61 ms                                                | 3.32 ms: 1.09x faster                                             |
| xml_etree_iterparse        | 107 ms                                                 | 98.2 ms: 1.09x faster                                             |
| sympy_integrate            | 21.4 ms                                                | 19.8 ms: 1.08x faster                                             |
| pprint_pformat             | 1.57 sec                                               | 1.45 sec: 1.08x faster                                            |
| pprint_safe_repr           | 776 ms                                                 | 719 ms: 1.08x faster                                              |
| async_generators           | 463 ms                                                 | 434 ms: 1.07x faster                                              |
| fannkuch                   | 417 ms                                                 | 391 ms: 1.07x faster                                              |
| django_template            | 34.6 ms                                                | 32.7 ms: 1.06x faster                                             |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                              |
| regex_dna                  | 212 ms                                                 | 202 ms: 1.05x faster                                              |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.82 ms: 1.05x faster                                             |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.05x faster                                            |
| nbody                      | 97.0 ms                                                | 93.0 ms: 1.04x faster                                             |
| docutils                   | 2.77 sec                                               | 2.67 sec: 1.04x faster                                            |
| 2to3                       | 274 ms                                                 | 265 ms: 1.03x faster                                              |
| hexiom                     | 6.41 ms                                                | 6.22 ms: 1.03x faster                                             |
| regex_v8                   | 23.1 ms                                                | 22.5 ms: 1.03x faster                                             |
| generators                 | 31.2 ms                                                | 30.4 ms: 1.03x faster                                             |
| sympy_expand               | 478 ms                                                 | 467 ms: 1.02x faster                                              |
| nqueens                    | 83.3 ms                                                | 81.5 ms: 1.02x faster                                             |
| logging_silent             | 104 ns                                                 | 103 ns: 1.01x faster                                              |
| pickle_pure_python         | 324 us                                                 | 321 us: 1.01x faster                                              |
| json_loads                 | 28.5 us                                                | 28.3 us: 1.01x faster                                             |
| python_startup_no_site     | 6.94 ms                                                | 6.94 ms: 1.00x slower                                             |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                              |
| pidigits                   | 187 ms                                                 | 196 ms: 1.05x slower                                              |
| json_dumps                 | 10.4 ms                                                | 11.0 ms: 1.06x slower                                             |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                              |
| telco                      | 7.10 ms                                                | 7.63 ms: 1.07x slower                                             |
| coroutines                 | 23.2 ms                                                | 25.0 ms: 1.08x slower                                             |
| coverage                   | 72.7 ms                                                | 88.5 ms: 1.22x slower                                             |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.27x slower                                             |
| gc_traversal               | 3.79 ms                                                | 4.91 ms: 1.29x slower                                             |
| create_gc_cycles           | 1.48 ms                                                | 2.60 ms: 1.76x slower                                             |
| Geometric mean             | (ref)                                                  | 1.14x faster                                                      |

Benchmark hidden because not significant (3): json, sqlite_synth, scimark_lu
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250701-3.15.0a0-b88f481-JIT/bm-20250701-linux-x86_64-brandtbucher-jit_up_7_6-3.15.0a0-b88f481.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.144x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.17x