# Results vs. 3.12.0

- fork: faster-cpython
- ref: immortal_stickiness
- machine: linux-x86_64
- commit hash: 490cf8d
- commit date: 2025-03-12
- overall geometric mean: 1.106x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 257 ms: 1.07x faster                                                            |
| docutils       | 2.77 sec                                               | 2.61 sec: 1.06x faster                                                          |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 612 ms: 1.93x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 611 ms: 1.89x faster                                                            |
| async_tree_none            | 472 ms                                                 | 257 ms: 1.83x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 316 ms: 1.83x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 481 ms: 1.51x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 496 ms: 1.46x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 71.0 ms: 1.19x faster                                                           |
| nbody          | 97.0 ms                                                | 96.4 ms: 1.01x faster                                                           |
| pidigits       | 187 ms                                                 | 186 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.17x faster                                                            |
| regex_effbot   | 3.61 ms                                                | 3.56 ms: 1.01x faster                                                           |
| regex_v8       | 23.1 ms                                                | 24.0 ms: 1.04x slower                                                           |
| regex_dna      | 212 ms                                                 | 227 ms: 1.07x slower                                                            |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.98 sec: 1.18x faster                                                          |
| xml_etree_parse      | 159 ms                                                 | 142 ms: 1.12x faster                                                            |
| xml_etree_iterparse  | 107 ms                                                 | 98.0 ms: 1.09x faster                                                           |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                            |
| xml_etree_generate   | 89.2 ms                                                | 84.1 ms: 1.06x faster                                                           |
| xml_etree_process    | 61.7 ms                                                | 58.7 ms: 1.05x faster                                                           |
| pickle_pure_python   | 324 us                                                 | 318 us: 1.02x faster                                                            |
| json_loads           | 28.5 us                                                | 30.2 us: 1.06x slower                                                           |
| json_dumps           | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.18 ms: 1.18x slower                                                           |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.9 ms: 1.08x faster                                                           |
| mako            | 11.9 ms                                                | 11.4 ms: 1.05x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 612 ms: 1.93x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 611 ms: 1.89x faster                                                            |
| async_tree_none            | 472 ms                                                 | 257 ms: 1.83x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 316 ms: 1.83x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 481 ms: 1.51x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 496 ms: 1.46x faster                                                            |
| deepcopy                   | 371 us                                                 | 262 us: 1.41x faster                                                            |
| deepcopy_memo              | 40.7 us                                                | 29.4 us: 1.38x faster                                                           |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                           |
| deepcopy_reduce            | 3.35 us                                                | 2.75 us: 1.22x faster                                                           |
| go                         | 139 ms                                                 | 115 ms: 1.21x faster                                                            |
| float                      | 84.7 ms                                                | 71.0 ms: 1.19x faster                                                           |
| async_generators           | 463 ms                                                 | 391 ms: 1.18x faster                                                            |
| deltablue                  | 3.72 ms                                                | 3.15 ms: 1.18x faster                                                           |
| pathlib                    | 19.3 ms                                                | 16.4 ms: 1.18x faster                                                           |
| tomli_loads                | 2.33 sec                                               | 1.98 sec: 1.18x faster                                                          |
| logging_format             | 7.23 us                                                | 6.16 us: 1.17x faster                                                           |
| dulwich_log                | 68.5 ms                                                | 58.4 ms: 1.17x faster                                                           |
| regex_compile              | 148 ms                                                 | 126 ms: 1.17x faster                                                            |
| logging_simple             | 6.46 us                                                | 5.58 us: 1.16x faster                                                           |
| raytrace                   | 312 ms                                                 | 271 ms: 1.15x faster                                                            |
| spectral_norm              | 115 ms                                                 | 99.8 ms: 1.15x faster                                                           |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                                            |
| sqlalchemy_declarative     | 147 ms                                                 | 130 ms: 1.13x faster                                                            |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.6 ms: 1.13x faster                                                           |
| xml_etree_parse            | 159 ms                                                 | 142 ms: 1.12x faster                                                            |
| sympy_str                  | 300 ms                                                 | 267 ms: 1.12x faster                                                            |
| chaos                      | 67.0 ms                                                | 60.3 ms: 1.11x faster                                                           |
| pyflate                    | 482 ms                                                 | 436 ms: 1.11x faster                                                            |
| generators                 | 31.2 ms                                                | 28.6 ms: 1.09x faster                                                           |
| scimark_monte_carlo        | 75.1 ms                                                | 68.8 ms: 1.09x faster                                                           |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.09x faster                                                            |
| xml_etree_iterparse        | 107 ms                                                 | 98.0 ms: 1.09x faster                                                           |
| scimark_fft                | 382 ms                                                 | 352 ms: 1.08x faster                                                            |
| django_template            | 34.6 ms                                                | 31.9 ms: 1.08x faster                                                           |
| sympy_integrate            | 21.4 ms                                                | 19.9 ms: 1.08x faster                                                           |
| crypto_pyaes               | 81.9 ms                                                | 76.3 ms: 1.07x faster                                                           |
| 2to3                       | 274 ms                                                 | 257 ms: 1.07x faster                                                            |
| mdp                        | 2.63 sec                                               | 2.48 sec: 1.06x faster                                                          |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                            |
| xml_etree_generate         | 89.2 ms                                                | 84.1 ms: 1.06x faster                                                           |
| docutils                   | 2.77 sec                                               | 2.61 sec: 1.06x faster                                                          |
| sympy_expand               | 478 ms                                                 | 452 ms: 1.06x faster                                                            |
| xml_etree_process          | 61.7 ms                                                | 58.7 ms: 1.05x faster                                                           |
| mako                       | 11.9 ms                                                | 11.4 ms: 1.05x faster                                                           |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                            |
| logging_silent             | 104 ns                                                 | 99.9 ns: 1.05x faster                                                           |
| hexiom                     | 6.41 ms                                                | 6.15 ms: 1.04x faster                                                           |
| pprint_safe_repr           | 776 ms                                                 | 746 ms: 1.04x faster                                                            |
| richards                   | 45.8 ms                                                | 44.1 ms: 1.04x faster                                                           |
| pprint_pformat             | 1.57 sec                                               | 1.52 sec: 1.03x faster                                                          |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.90 ms: 1.03x faster                                                           |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.02x faster                                                            |
| richards_super             | 51.5 ms                                                | 50.6 ms: 1.02x faster                                                           |
| pickle_pure_python         | 324 us                                                 | 318 us: 1.02x faster                                                            |
| sqlite_synth               | 2.83 us                                                | 2.79 us: 1.02x faster                                                           |
| regex_effbot               | 3.61 ms                                                | 3.56 ms: 1.01x faster                                                           |
| nbody                      | 97.0 ms                                                | 96.4 ms: 1.01x faster                                                           |
| pidigits                   | 187 ms                                                 | 186 ms: 1.00x faster                                                            |
| nqueens                    | 83.3 ms                                                | 83.5 ms: 1.00x slower                                                           |
| json                       | 5.26 ms                                                | 5.32 ms: 1.01x slower                                                           |
| fannkuch                   | 417 ms                                                 | 422 ms: 1.01x slower                                                            |
| coroutines                 | 23.2 ms                                                | 23.5 ms: 1.01x slower                                                           |
| typing_runtime_protocols   | 158 us                                                 | 163 us: 1.03x slower                                                            |
| regex_v8                   | 23.1 ms                                                | 24.0 ms: 1.04x slower                                                           |
| bench_thread_pool          | 842 us                                                 | 873 us: 1.04x slower                                                            |
| json_loads                 | 28.5 us                                                | 30.2 us: 1.06x slower                                                           |
| regex_dna                  | 212 ms                                                 | 227 ms: 1.07x slower                                                            |
| json_dumps                 | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                           |
| telco                      | 7.10 ms                                                | 7.93 ms: 1.12x slower                                                           |
| python_startup_no_site     | 6.94 ms                                                | 8.18 ms: 1.18x slower                                                           |
| coverage                   | 72.7 ms                                                | 91.9 ms: 1.26x slower                                                           |
| gc_traversal               | 3.79 ms                                                | 5.02 ms: 1.32x slower                                                           |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 2.48 ms: 1.68x slower                                                           |
| bench_mp_pool              | 24.0 ms                                                | 83.2 ms: 3.46x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                                    |

Benchmark hidden because not significant (2): pycparser, asyncio_websockets
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250312-3.14.0a5+-490cf8d/bm-20250312-linux-x86_64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.106x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.10x