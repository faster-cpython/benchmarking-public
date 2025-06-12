# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_hot
- machine: linux-x86_64
- commit hash: 5606078
- commit date: 2025-06-11
- overall geometric mean: 1.109x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 259 ms: 1.06x faster                                              |
| docutils       | 2.77 sec                                               | 2.64 sec: 1.05x faster                                            |
| Geometric mean | (ref)                                                  | 1.05x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 600 ms: 1.93x faster                                              |
| async_tree_io_tg           | 1.18 sec                                               | 619 ms: 1.91x faster                                              |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                              |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                              |
| async_tree_none            | 472 ms                                                 | 263 ms: 1.79x faster                                              |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                              |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 485 ms: 1.49x faster                                              |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 490 ms: 1.48x faster                                              |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 84.7 ms                                                | 65.0 ms: 1.30x faster                                             |
| nbody          | 97.0 ms                                                | 90.2 ms: 1.08x faster                                             |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                              |
| Geometric mean | (ref)                                                  | 1.12x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                              |
| regex_effbot   | 3.61 ms                                                | 3.43 ms: 1.05x faster                                             |
| regex_dna      | 212 ms                                                 | 215 ms: 1.01x slower                                              |
| regex_v8       | 23.1 ms                                                | 23.5 ms: 1.02x slower                                             |
| Geometric mean | (ref)                                                  | 1.04x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.86 sec: 1.25x faster                                            |
| unpickle_pure_python | 230 us                                                 | 196 us: 1.17x faster                                              |
| xml_etree_parse      | 159 ms                                                 | 139 ms: 1.14x faster                                              |
| xml_etree_process    | 61.7 ms                                                | 55.4 ms: 1.11x faster                                             |
| xml_etree_generate   | 89.2 ms                                                | 80.2 ms: 1.11x faster                                             |
| xml_etree_iterparse  | 107 ms                                                 | 98.0 ms: 1.09x faster                                             |
| json_loads           | 28.5 us                                                | 27.8 us: 1.03x faster                                             |
| pickle_pure_python   | 324 us                                                 | 322 us: 1.01x faster                                              |
| json_dumps           | 10.4 ms                                                | 11.0 ms: 1.06x slower                                             |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.91 ms: 1.00x faster                                             |
| python_startup         | 9.55 ms                                                | 12.1 ms: 1.27x slower                                             |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.5 ms: 1.13x faster                                             |
| django_template | 34.6 ms                                                | 32.6 ms: 1.06x faster                                             |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.26 sec: 2.09x faster                                            |
| async_tree_io              | 1.16 sec                                               | 600 ms: 1.93x faster                                              |
| async_tree_io_tg           | 1.18 sec                                               | 619 ms: 1.91x faster                                              |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                              |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                              |
| async_tree_none            | 472 ms                                                 | 263 ms: 1.79x faster                                              |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                              |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 485 ms: 1.49x faster                                              |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 490 ms: 1.48x faster                                              |
| deepcopy                   | 371 us                                                 | 262 us: 1.42x faster                                              |
| richards                   | 45.8 ms                                                | 32.6 ms: 1.41x faster                                             |
| deepcopy_memo              | 40.7 us                                                | 29.7 us: 1.37x faster                                             |
| richards_super             | 51.5 ms                                                | 38.0 ms: 1.35x faster                                             |
| float                      | 84.7 ms                                                | 65.0 ms: 1.30x faster                                             |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.30x faster                                             |
| tomli_loads                | 2.33 sec                                               | 1.86 sec: 1.25x faster                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.75 us: 1.22x faster                                             |
| deltablue                  | 3.72 ms                                                | 3.07 ms: 1.21x faster                                             |
| go                         | 139 ms                                                 | 116 ms: 1.20x faster                                              |
| scimark_fft                | 382 ms                                                 | 323 ms: 1.18x faster                                              |
| unpickle_pure_python       | 230 us                                                 | 196 us: 1.17x faster                                              |
| pyflate                    | 482 ms                                                 | 412 ms: 1.17x faster                                              |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                              |
| spectral_norm              | 115 ms                                                 | 98.9 ms: 1.16x faster                                             |
| scimark_monte_carlo        | 75.1 ms                                                | 65.6 ms: 1.15x faster                                             |
| xml_etree_parse            | 159 ms                                                 | 139 ms: 1.14x faster                                              |
| raytrace                   | 312 ms                                                 | 274 ms: 1.14x faster                                              |
| pathlib                    | 19.3 ms                                                | 17.0 ms: 1.14x faster                                             |
| mako                       | 11.9 ms                                                | 10.5 ms: 1.13x faster                                             |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                              |
| xml_etree_process          | 61.7 ms                                                | 55.4 ms: 1.11x faster                                             |
| xml_etree_generate         | 89.2 ms                                                | 80.2 ms: 1.11x faster                                             |
| dulwich_log                | 68.5 ms                                                | 61.8 ms: 1.11x faster                                             |
| crypto_pyaes               | 81.9 ms                                                | 74.0 ms: 1.11x faster                                             |
| sympy_integrate            | 21.4 ms                                                | 19.4 ms: 1.10x faster                                             |
| sympy_str                  | 300 ms                                                 | 273 ms: 1.10x faster                                              |
| xml_etree_iterparse        | 107 ms                                                 | 98.0 ms: 1.09x faster                                             |
| async_generators           | 463 ms                                                 | 425 ms: 1.09x faster                                              |
| chaos                      | 67.0 ms                                                | 61.7 ms: 1.09x faster                                             |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.08x faster                                              |
| nbody                      | 97.0 ms                                                | 90.2 ms: 1.08x faster                                             |
| django_template            | 34.6 ms                                                | 32.6 ms: 1.06x faster                                             |
| logging_format             | 7.23 us                                                | 6.82 us: 1.06x faster                                             |
| 2to3                       | 274 ms                                                 | 259 ms: 1.06x faster                                              |
| regex_effbot               | 3.61 ms                                                | 3.43 ms: 1.05x faster                                             |
| logging_simple             | 6.46 us                                                | 6.15 us: 1.05x faster                                             |
| docutils                   | 2.77 sec                                               | 2.64 sec: 1.05x faster                                            |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.83 ms: 1.05x faster                                             |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                              |
| generators                 | 31.2 ms                                                | 30.0 ms: 1.04x faster                                             |
| fannkuch                   | 417 ms                                                 | 401 ms: 1.04x faster                                              |
| json                       | 5.26 ms                                                | 5.10 ms: 1.03x faster                                             |
| json_loads                 | 28.5 us                                                | 27.8 us: 1.03x faster                                             |
| sympy_expand               | 478 ms                                                 | 469 ms: 1.02x faster                                              |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                            |
| hexiom                     | 6.41 ms                                                | 6.32 ms: 1.01x faster                                             |
| sqlite_synth               | 2.83 us                                                | 2.81 us: 1.01x faster                                             |
| pickle_pure_python         | 324 us                                                 | 322 us: 1.01x faster                                              |
| python_startup_no_site     | 6.94 ms                                                | 6.91 ms: 1.00x faster                                             |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                              |
| pprint_safe_repr           | 776 ms                                                 | 785 ms: 1.01x slower                                              |
| regex_dna                  | 212 ms                                                 | 215 ms: 1.01x slower                                              |
| regex_v8                   | 23.1 ms                                                | 23.5 ms: 1.02x slower                                             |
| scimark_lu                 | 118 ms                                                 | 122 ms: 1.03x slower                                              |
| pprint_pformat             | 1.57 sec                                               | 1.63 sec: 1.04x slower                                            |
| json_dumps                 | 10.4 ms                                                | 11.0 ms: 1.06x slower                                             |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.06x slower                                              |
| coroutines                 | 23.2 ms                                                | 24.7 ms: 1.07x slower                                             |
| telco                      | 7.10 ms                                                | 7.78 ms: 1.10x slower                                             |
| python_startup             | 9.55 ms                                                | 12.1 ms: 1.27x slower                                             |
| gc_traversal               | 3.79 ms                                                | 5.03 ms: 1.33x slower                                             |
| create_gc_cycles           | 1.48 ms                                                | 2.58 ms: 1.75x slower                                             |
| logging_silent             | 104 ns                                                 | 475 ns: 4.55x slower                                              |
| coverage                   | 72.7 ms                                                | 428 ms: 5.89x slower                                              |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                      |

Benchmark hidden because not significant (2): asyncio_websockets, nqueens
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250611-3.15.0a0-5606078-JIT/bm-20250611-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-5606078.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.109x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.15x