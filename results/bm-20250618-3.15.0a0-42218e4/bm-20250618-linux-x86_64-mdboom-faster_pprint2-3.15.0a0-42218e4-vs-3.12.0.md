# Results vs. 3.12.0

- fork: mdboom
- ref: faster_pprint2
- machine: linux-x86_64
- commit hash: 42218e4
- commit date: 2025-06-18
- overall geometric mean: 1.118x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 255 ms: 1.07x faster                                            |
| docutils       | 2.77 sec                                               | 2.58 sec: 1.07x faster                                          |
| Geometric mean | (ref)                                                  | 1.07x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 598 ms: 1.93x faster                                            |
| async_tree_io_tg           | 1.18 sec                                               | 626 ms: 1.89x faster                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 308 ms: 1.87x faster                                            |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.84x faster                                            |
| async_tree_none_tg         | 450 ms                                                 | 247 ms: 1.82x faster                                            |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 487 ms: 1.49x faster                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 497 ms: 1.46x faster                                            |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 84.7 ms                                                | 72.9 ms: 1.16x faster                                           |
| nbody          | 97.0 ms                                                | 97.8 ms: 1.01x slower                                           |
| pidigits       | 187 ms                                                 | 192 ms: 1.02x slower                                            |
| Geometric mean | (ref)                                                  | 1.04x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                            |
| regex_effbot   | 3.61 ms                                                | 3.31 ms: 1.09x faster                                           |
| regex_v8       | 23.1 ms                                                | 23.0 ms: 1.01x faster                                           |
| regex_dna      | 212 ms                                                 | 215 ms: 1.01x slower                                            |
| Geometric mean | (ref)                                                  | 1.06x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.03 sec: 1.15x faster                                          |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                            |
| xml_etree_iterparse  | 107 ms                                                 | 98.2 ms: 1.09x faster                                           |
| unpickle_pure_python | 230 us                                                 | 218 us: 1.05x faster                                            |
| xml_etree_generate   | 89.2 ms                                                | 85.2 ms: 1.05x faster                                           |
| xml_etree_process    | 61.7 ms                                                | 59.9 ms: 1.03x faster                                           |
| json_loads           | 28.5 us                                                | 28.2 us: 1.01x faster                                           |
| json_dumps           | 10.4 ms                                                | 11.3 ms: 1.08x slower                                           |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                    |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.92 ms: 1.00x faster                                           |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.28x slower                                           |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.3 ms: 1.07x faster                                           |
| mako            | 11.9 ms                                                | 11.7 ms: 1.01x faster                                           |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.22 sec: 2.15x faster                                          |
| async_tree_io              | 1.16 sec                                               | 598 ms: 1.93x faster                                            |
| async_tree_io_tg           | 1.18 sec                                               | 626 ms: 1.89x faster                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 308 ms: 1.87x faster                                            |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.84x faster                                            |
| async_tree_none_tg         | 450 ms                                                 | 247 ms: 1.82x faster                                            |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 487 ms: 1.49x faster                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 497 ms: 1.46x faster                                            |
| deepcopy                   | 371 us                                                 | 255 us: 1.45x faster                                            |
| deepcopy_memo              | 40.7 us                                                | 29.1 us: 1.40x faster                                           |
| comprehensions             | 21.8 us                                                | 16.0 us: 1.36x faster                                           |
| go                         | 139 ms                                                 | 111 ms: 1.26x faster                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.76 us: 1.21x faster                                           |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                            |
| float                      | 84.7 ms                                                | 72.9 ms: 1.16x faster                                           |
| dulwich_log                | 68.5 ms                                                | 59.1 ms: 1.16x faster                                           |
| raytrace                   | 312 ms                                                 | 271 ms: 1.15x faster                                            |
| tomli_loads                | 2.33 sec                                               | 2.03 sec: 1.15x faster                                          |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                            |
| pyflate                    | 482 ms                                                 | 423 ms: 1.14x faster                                            |
| pathlib                    | 19.3 ms                                                | 17.0 ms: 1.14x faster                                           |
| scimark_monte_carlo        | 75.1 ms                                                | 65.9 ms: 1.14x faster                                           |
| sympy_str                  | 300 ms                                                 | 264 ms: 1.13x faster                                            |
| sympy_integrate            | 21.4 ms                                                | 18.9 ms: 1.13x faster                                           |
| async_generators           | 463 ms                                                 | 409 ms: 1.13x faster                                            |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                            |
| chaos                      | 67.0 ms                                                | 61.1 ms: 1.10x faster                                           |
| regex_effbot               | 3.61 ms                                                | 3.31 ms: 1.09x faster                                           |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.09x faster                                            |
| xml_etree_iterparse        | 107 ms                                                 | 98.2 ms: 1.09x faster                                           |
| crypto_pyaes               | 81.9 ms                                                | 75.6 ms: 1.08x faster                                           |
| meteor_contest             | 112 ms                                                 | 104 ms: 1.08x faster                                            |
| spectral_norm              | 115 ms                                                 | 107 ms: 1.08x faster                                            |
| hexiom                     | 6.41 ms                                                | 5.97 ms: 1.07x faster                                           |
| 2to3                       | 274 ms                                                 | 255 ms: 1.07x faster                                            |
| docutils                   | 2.77 sec                                               | 2.58 sec: 1.07x faster                                          |
| django_template            | 34.6 ms                                                | 32.3 ms: 1.07x faster                                           |
| deltablue                  | 3.72 ms                                                | 3.47 ms: 1.07x faster                                           |
| richards                   | 45.8 ms                                                | 42.9 ms: 1.07x faster                                           |
| sympy_expand               | 478 ms                                                 | 449 ms: 1.06x faster                                            |
| pprint_safe_repr           | 776 ms                                                 | 729 ms: 1.06x faster                                            |
| unpickle_pure_python       | 230 us                                                 | 218 us: 1.05x faster                                            |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.05x faster                                          |
| logging_format             | 7.23 us                                                | 6.87 us: 1.05x faster                                           |
| scimark_fft                | 382 ms                                                 | 364 ms: 1.05x faster                                            |
| generators                 | 31.2 ms                                                | 29.8 ms: 1.05x faster                                           |
| xml_etree_generate         | 89.2 ms                                                | 85.2 ms: 1.05x faster                                           |
| richards_super             | 51.5 ms                                                | 49.3 ms: 1.04x faster                                           |
| logging_simple             | 6.46 us                                                | 6.24 us: 1.03x faster                                           |
| nqueens                    | 83.3 ms                                                | 80.8 ms: 1.03x faster                                           |
| xml_etree_process          | 61.7 ms                                                | 59.9 ms: 1.03x faster                                           |
| json                       | 5.26 ms                                                | 5.17 ms: 1.02x faster                                           |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                          |
| mako                       | 11.9 ms                                                | 11.7 ms: 1.01x faster                                           |
| json_loads                 | 28.5 us                                                | 28.2 us: 1.01x faster                                           |
| regex_v8                   | 23.1 ms                                                | 23.0 ms: 1.01x faster                                           |
| python_startup_no_site     | 6.94 ms                                                | 6.92 ms: 1.00x faster                                           |
| nbody                      | 97.0 ms                                                | 97.8 ms: 1.01x slower                                           |
| regex_dna                  | 212 ms                                                 | 215 ms: 1.01x slower                                            |
| sqlite_synth               | 2.83 us                                                | 2.90 us: 1.02x slower                                           |
| pidigits                   | 187 ms                                                 | 192 ms: 1.02x slower                                            |
| typing_runtime_protocols   | 158 us                                                 | 169 us: 1.07x slower                                            |
| coroutines                 | 23.2 ms                                                | 25.0 ms: 1.08x slower                                           |
| json_dumps                 | 10.4 ms                                                | 11.3 ms: 1.08x slower                                           |
| telco                      | 7.10 ms                                                | 7.96 ms: 1.12x slower                                           |
| coverage                   | 72.7 ms                                                | 87.1 ms: 1.20x slower                                           |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.28x slower                                           |
| gc_traversal               | 3.79 ms                                                | 5.06 ms: 1.33x slower                                           |
| create_gc_cycles           | 1.48 ms                                                | 2.59 ms: 1.75x slower                                           |
| logging_silent             | 104 ns                                                 | 469 ns: 4.49x slower                                            |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                    |

Benchmark hidden because not significant (5): scimark_sparse_mat_mult, pickle_pure_python, scimark_lu, fannkuch, asyncio_websockets
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250618-3.15.0a0-42218e4/bm-20250618-linux-x86_64-mdboom-faster_pprint2-3.15.0a0-42218e4.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.118x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.13x