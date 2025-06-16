# Results vs. 3.12.0

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: linux-x86_64
- commit hash: c41d531
- commit date: 2025-06-16
- overall geometric mean: 1.092x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250616-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 254 ms: 1.08x faster                                                            |
| docutils       | 2.77 sec                                               | 2.57 sec: 1.08x faster                                                          |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250616-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 600 ms: 1.93x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 626 ms: 1.89x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.83x faster                                                            |
| async_tree_none            | 472 ms                                                 | 260 ms: 1.82x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 492 ms: 1.47x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 499 ms: 1.45x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250616-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 72.8 ms: 1.16x faster                                                           |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                            |
| nbody          | 97.0 ms                                                | 97.8 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250616-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                            |
| regex_effbot   | 3.61 ms                                                | 3.15 ms: 1.14x faster                                                           |
| regex_dna      | 212 ms                                                 | 191 ms: 1.11x faster                                                            |
| regex_v8       | 23.1 ms                                                | 22.2 ms: 1.04x faster                                                           |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250616-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.03 sec: 1.15x faster                                                          |
| xml_etree_parse      | 159 ms                                                 | 143 ms: 1.11x faster                                                            |
| xml_etree_iterparse  | 107 ms                                                 | 99.3 ms: 1.07x faster                                                           |
| unpickle_pure_python | 230 us                                                 | 219 us: 1.05x faster                                                            |
| xml_etree_generate   | 89.2 ms                                                | 85.9 ms: 1.04x faster                                                           |
| xml_etree_process    | 61.7 ms                                                | 60.6 ms: 1.02x faster                                                           |
| pickle_pure_python   | 324 us                                                 | 319 us: 1.02x faster                                                            |
| json_dumps           | 10.4 ms                                                | 11.1 ms: 1.07x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                    |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250616-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.93 ms: 1.00x faster                                                           |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.28x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250616-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.5 ms: 1.06x faster                                                           |
| mako            | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250616-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.22 sec: 2.15x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 600 ms: 1.93x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 626 ms: 1.89x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.83x faster                                                            |
| async_tree_none            | 472 ms                                                 | 260 ms: 1.82x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 492 ms: 1.47x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 499 ms: 1.45x faster                                                            |
| deepcopy                   | 371 us                                                 | 261 us: 1.42x faster                                                            |
| deepcopy_memo              | 40.7 us                                                | 29.2 us: 1.40x faster                                                           |
| comprehensions             | 21.8 us                                                | 16.0 us: 1.36x faster                                                           |
| go                         | 139 ms                                                 | 111 ms: 1.26x faster                                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.79 us: 1.20x faster                                                           |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                            |
| float                      | 84.7 ms                                                | 72.8 ms: 1.16x faster                                                           |
| raytrace                   | 312 ms                                                 | 269 ms: 1.16x faster                                                            |
| dulwich_log                | 68.5 ms                                                | 59.2 ms: 1.16x faster                                                           |
| tomli_loads                | 2.33 sec                                               | 2.03 sec: 1.15x faster                                                          |
| regex_effbot               | 3.61 ms                                                | 3.15 ms: 1.14x faster                                                           |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                                            |
| pathlib                    | 19.3 ms                                                | 17.0 ms: 1.14x faster                                                           |
| sympy_integrate            | 21.4 ms                                                | 18.9 ms: 1.13x faster                                                           |
| chaos                      | 67.0 ms                                                | 59.2 ms: 1.13x faster                                                           |
| sympy_str                  | 300 ms                                                 | 266 ms: 1.13x faster                                                            |
| async_generators           | 463 ms                                                 | 414 ms: 1.12x faster                                                            |
| scimark_monte_carlo        | 75.1 ms                                                | 67.2 ms: 1.12x faster                                                           |
| xml_etree_parse            | 159 ms                                                 | 143 ms: 1.11x faster                                                            |
| regex_dna                  | 212 ms                                                 | 191 ms: 1.11x faster                                                            |
| pyflate                    | 482 ms                                                 | 435 ms: 1.11x faster                                                            |
| crypto_pyaes               | 81.9 ms                                                | 74.2 ms: 1.10x faster                                                           |
| 2to3                       | 274 ms                                                 | 254 ms: 1.08x faster                                                            |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.08x faster                                                            |
| docutils                   | 2.77 sec                                               | 2.57 sec: 1.08x faster                                                          |
| xml_etree_iterparse        | 107 ms                                                 | 99.3 ms: 1.07x faster                                                           |
| logging_format             | 7.23 us                                                | 6.77 us: 1.07x faster                                                           |
| deltablue                  | 3.72 ms                                                | 3.49 ms: 1.06x faster                                                           |
| django_template            | 34.6 ms                                                | 32.5 ms: 1.06x faster                                                           |
| logging_simple             | 6.46 us                                                | 6.07 us: 1.06x faster                                                           |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                            |
| hexiom                     | 6.41 ms                                                | 6.05 ms: 1.06x faster                                                           |
| sympy_expand               | 478 ms                                                 | 452 ms: 1.06x faster                                                            |
| richards                   | 45.8 ms                                                | 43.5 ms: 1.05x faster                                                           |
| generators                 | 31.2 ms                                                | 29.6 ms: 1.05x faster                                                           |
| unpickle_pure_python       | 230 us                                                 | 219 us: 1.05x faster                                                            |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                           |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.05x faster                                                          |
| richards_super             | 51.5 ms                                                | 49.4 ms: 1.04x faster                                                           |
| regex_v8                   | 23.1 ms                                                | 22.2 ms: 1.04x faster                                                           |
| xml_etree_generate         | 89.2 ms                                                | 85.9 ms: 1.04x faster                                                           |
| spectral_norm              | 115 ms                                                 | 111 ms: 1.04x faster                                                            |
| nqueens                    | 83.3 ms                                                | 80.8 ms: 1.03x faster                                                           |
| xml_etree_process          | 61.7 ms                                                | 60.6 ms: 1.02x faster                                                           |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                                            |
| pickle_pure_python         | 324 us                                                 | 319 us: 1.02x faster                                                            |
| python_startup_no_site     | 6.94 ms                                                | 6.93 ms: 1.00x faster                                                           |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                            |
| nbody                      | 97.0 ms                                                | 97.8 ms: 1.01x slower                                                           |
| sqlite_synth               | 2.83 us                                                | 2.86 us: 1.01x slower                                                           |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.11 ms: 1.01x slower                                                           |
| pprint_safe_repr           | 776 ms                                                 | 810 ms: 1.04x slower                                                            |
| pprint_pformat             | 1.57 sec                                               | 1.65 sec: 1.05x slower                                                          |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                                            |
| json_dumps                 | 10.4 ms                                                | 11.1 ms: 1.07x slower                                                           |
| coroutines                 | 23.2 ms                                                | 25.1 ms: 1.08x slower                                                           |
| telco                      | 7.10 ms                                                | 7.98 ms: 1.12x slower                                                           |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.28x slower                                                           |
| gc_traversal               | 3.79 ms                                                | 5.07 ms: 1.34x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 2.59 ms: 1.75x slower                                                           |
| logging_silent             | 104 ns                                                 | 475 ns: 4.54x slower                                                            |
| coverage                   | 72.7 ms                                                | 418 ms: 5.74x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                                    |

Benchmark hidden because not significant (5): asyncio_websockets, json_loads, fannkuch, scimark_fft, json
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250616-3.15.0a0-c41d531/bm-20250616-linux-x86_64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.092x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.13x