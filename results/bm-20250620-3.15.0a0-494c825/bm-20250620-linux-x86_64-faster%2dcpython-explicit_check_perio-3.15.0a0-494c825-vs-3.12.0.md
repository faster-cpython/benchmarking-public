# Results vs. 3.12.0

- fork: faster-cpython
- ref: explicit_check_perio
- machine: linux-x86_64
- commit hash: 494c825
- commit date: 2025-06-20
- overall geometric mean: 1.109x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 257 ms: 1.07x faster                                                            |
| docutils       | 2.77 sec                                               | 2.61 sec: 1.06x faster                                                          |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 604 ms: 1.91x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 622 ms: 1.90x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 321 ms: 1.80x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.78x faster                                                            |
| async_tree_none            | 472 ms                                                 | 267 ms: 1.77x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 490 ms: 1.48x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 502 ms: 1.44x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.73x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 72.3 ms: 1.17x faster                                                           |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                                            |
| nbody          | 97.0 ms                                                | 99.1 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 130 ms: 1.15x faster                                                            |
| regex_effbot   | 3.61 ms                                                | 3.22 ms: 1.12x faster                                                           |
| regex_dna      | 212 ms                                                 | 199 ms: 1.07x faster                                                            |
| regex_v8       | 23.1 ms                                                | 23.2 ms: 1.00x slower                                                           |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.02 sec: 1.15x faster                                                          |
| xml_etree_parse      | 159 ms                                                 | 143 ms: 1.12x faster                                                            |
| xml_etree_iterparse  | 107 ms                                                 | 98.8 ms: 1.08x faster                                                           |
| xml_etree_generate   | 89.2 ms                                                | 84.8 ms: 1.05x faster                                                           |
| unpickle_pure_python | 230 us                                                 | 222 us: 1.03x faster                                                            |
| xml_etree_process    | 61.7 ms                                                | 59.7 ms: 1.03x faster                                                           |
| json_loads           | 28.5 us                                                | 28.3 us: 1.01x faster                                                           |
| pickle_pure_python   | 324 us                                                 | 327 us: 1.01x slower                                                            |
| json_dumps           | 10.4 ms                                                | 11.2 ms: 1.07x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup | 9.55 ms                                                | 12.2 ms: 1.28x slower                                                           |
| Geometric mean | (ref)                                                  | 1.13x slower                                                                    |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.8 ms: 1.06x faster                                                           |
| mako            | 11.9 ms                                                | 11.6 ms: 1.03x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.23 sec: 2.15x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 604 ms: 1.91x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 622 ms: 1.90x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 321 ms: 1.80x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.78x faster                                                            |
| async_tree_none            | 472 ms                                                 | 267 ms: 1.77x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 490 ms: 1.48x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 502 ms: 1.44x faster                                                            |
| deepcopy                   | 371 us                                                 | 257 us: 1.44x faster                                                            |
| comprehensions             | 21.8 us                                                | 16.0 us: 1.36x faster                                                           |
| deepcopy_memo              | 40.7 us                                                | 30.1 us: 1.35x faster                                                           |
| go                         | 139 ms                                                 | 111 ms: 1.26x faster                                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.72 us: 1.23x faster                                                           |
| float                      | 84.7 ms                                                | 72.3 ms: 1.17x faster                                                           |
| tomli_loads                | 2.33 sec                                               | 2.02 sec: 1.15x faster                                                          |
| raytrace                   | 312 ms                                                 | 272 ms: 1.15x faster                                                            |
| regex_compile              | 148 ms                                                 | 130 ms: 1.15x faster                                                            |
| dulwich_log                | 68.5 ms                                                | 60.0 ms: 1.14x faster                                                           |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.13x faster                                                            |
| pyflate                    | 482 ms                                                 | 427 ms: 1.13x faster                                                            |
| pathlib                    | 19.3 ms                                                | 17.2 ms: 1.12x faster                                                           |
| async_generators           | 463 ms                                                 | 412 ms: 1.12x faster                                                            |
| regex_effbot               | 3.61 ms                                                | 3.22 ms: 1.12x faster                                                           |
| scimark_monte_carlo        | 75.1 ms                                                | 67.1 ms: 1.12x faster                                                           |
| sympy_str                  | 300 ms                                                 | 268 ms: 1.12x faster                                                            |
| sympy_integrate            | 21.4 ms                                                | 19.2 ms: 1.12x faster                                                           |
| xml_etree_parse            | 159 ms                                                 | 143 ms: 1.12x faster                                                            |
| chaos                      | 67.0 ms                                                | 60.5 ms: 1.11x faster                                                           |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.10x faster                                                            |
| xml_etree_iterparse        | 107 ms                                                 | 98.8 ms: 1.08x faster                                                           |
| spectral_norm              | 115 ms                                                 | 107 ms: 1.07x faster                                                            |
| 2to3                       | 274 ms                                                 | 257 ms: 1.07x faster                                                            |
| regex_dna                  | 212 ms                                                 | 199 ms: 1.07x faster                                                            |
| crypto_pyaes               | 81.9 ms                                                | 76.8 ms: 1.07x faster                                                           |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                            |
| deltablue                  | 3.72 ms                                                | 3.50 ms: 1.06x faster                                                           |
| docutils                   | 2.77 sec                                               | 2.61 sec: 1.06x faster                                                          |
| richards                   | 45.8 ms                                                | 43.2 ms: 1.06x faster                                                           |
| generators                 | 31.2 ms                                                | 29.4 ms: 1.06x faster                                                           |
| django_template            | 34.6 ms                                                | 32.8 ms: 1.06x faster                                                           |
| xml_etree_generate         | 89.2 ms                                                | 84.8 ms: 1.05x faster                                                           |
| sympy_expand               | 478 ms                                                 | 456 ms: 1.05x faster                                                            |
| richards_super             | 51.5 ms                                                | 49.4 ms: 1.04x faster                                                           |
| unpickle_pure_python       | 230 us                                                 | 222 us: 1.03x faster                                                            |
| xml_etree_process          | 61.7 ms                                                | 59.7 ms: 1.03x faster                                                           |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.03x faster                                                          |
| hexiom                     | 6.41 ms                                                | 6.22 ms: 1.03x faster                                                           |
| mako                       | 11.9 ms                                                | 11.6 ms: 1.03x faster                                                           |
| nqueens                    | 83.3 ms                                                | 81.2 ms: 1.03x faster                                                           |
| scimark_fft                | 382 ms                                                 | 374 ms: 1.02x faster                                                            |
| logging_simple             | 6.46 us                                                | 6.33 us: 1.02x faster                                                           |
| logging_format             | 7.23 us                                                | 7.11 us: 1.02x faster                                                           |
| json_loads                 | 28.5 us                                                | 28.3 us: 1.01x faster                                                           |
| regex_v8                   | 23.1 ms                                                | 23.2 ms: 1.00x slower                                                           |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                                            |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.09 ms: 1.01x slower                                                           |
| pickle_pure_python         | 324 us                                                 | 327 us: 1.01x slower                                                            |
| sqlite_synth               | 2.83 us                                                | 2.86 us: 1.01x slower                                                           |
| nbody                      | 97.0 ms                                                | 99.1 ms: 1.02x slower                                                           |
| pprint_safe_repr           | 776 ms                                                 | 812 ms: 1.05x slower                                                            |
| pprint_pformat             | 1.57 sec                                               | 1.66 sec: 1.06x slower                                                          |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.06x slower                                                            |
| coroutines                 | 23.2 ms                                                | 24.7 ms: 1.07x slower                                                           |
| json_dumps                 | 10.4 ms                                                | 11.2 ms: 1.07x slower                                                           |
| telco                      | 7.10 ms                                                | 7.99 ms: 1.12x slower                                                           |
| coverage                   | 72.7 ms                                                | 87.1 ms: 1.20x slower                                                           |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.28x slower                                                           |
| gc_traversal               | 3.79 ms                                                | 5.17 ms: 1.36x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 2.59 ms: 1.76x slower                                                           |
| logging_silent             | 104 ns                                                 | 480 ns: 4.59x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                                    |

Benchmark hidden because not significant (5): fannkuch, python_startup_no_site, asyncio_websockets, scimark_lu, json
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250620-3.15.0a0-494c825/bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.109x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.13x