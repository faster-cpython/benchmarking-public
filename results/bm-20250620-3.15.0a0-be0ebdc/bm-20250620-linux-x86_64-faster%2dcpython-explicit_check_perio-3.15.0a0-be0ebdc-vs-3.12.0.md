# Results vs. 3.12.0

- fork: faster-cpython
- ref: explicit_check_perio
- machine: linux-x86_64
- commit hash: be0ebdc
- commit date: 2025-06-20
- overall geometric mean: 1.100x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 259 ms: 1.06x faster                                                            |
| docutils       | 2.77 sec                                               | 2.61 sec: 1.06x faster                                                          |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 602 ms: 1.92x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 637 ms: 1.86x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 317 ms: 1.82x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                            |
| async_tree_none            | 472 ms                                                 | 265 ms: 1.78x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 500 ms: 1.45x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 510 ms: 1.42x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.72x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 74.3 ms: 1.14x faster                                                           |
| pidigits       | 187 ms                                                 | 193 ms: 1.03x slower                                                            |
| nbody          | 97.0 ms                                                | 100 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 130 ms: 1.14x faster                                                            |
| regex_effbot   | 3.61 ms                                                | 3.33 ms: 1.08x faster                                                           |
| regex_v8       | 23.1 ms                                                | 23.5 ms: 1.02x slower                                                           |
| regex_dna      | 212 ms                                                 | 216 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.01 sec: 1.16x faster                                                          |
| xml_etree_parse      | 159 ms                                                 | 142 ms: 1.12x faster                                                            |
| xml_etree_iterparse  | 107 ms                                                 | 99.1 ms: 1.08x faster                                                           |
| xml_etree_generate   | 89.2 ms                                                | 86.2 ms: 1.03x faster                                                           |
| unpickle_pure_python | 230 us                                                 | 225 us: 1.02x faster                                                            |
| xml_etree_process    | 61.7 ms                                                | 60.4 ms: 1.02x faster                                                           |
| json_loads           | 28.5 us                                                | 28.8 us: 1.01x slower                                                           |
| pickle_pure_python   | 324 us                                                 | 327 us: 1.01x slower                                                            |
| json_dumps           | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.95 ms: 1.00x slower                                                           |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.28x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.6 ms: 1.06x faster                                                           |
| mako            | 11.9 ms                                                | 11.8 ms: 1.01x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.23 sec: 2.14x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 602 ms: 1.92x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 637 ms: 1.86x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 317 ms: 1.82x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                            |
| async_tree_none            | 472 ms                                                 | 265 ms: 1.78x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 500 ms: 1.45x faster                                                            |
| deepcopy                   | 371 us                                                 | 260 us: 1.43x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 510 ms: 1.42x faster                                                            |
| comprehensions             | 21.8 us                                                | 16.2 us: 1.34x faster                                                           |
| deepcopy_memo              | 40.7 us                                                | 30.5 us: 1.33x faster                                                           |
| go                         | 139 ms                                                 | 114 ms: 1.22x faster                                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.75 us: 1.21x faster                                                           |
| tomli_loads                | 2.33 sec                                               | 2.01 sec: 1.16x faster                                                          |
| dulwich_log                | 68.5 ms                                                | 59.5 ms: 1.15x faster                                                           |
| regex_compile              | 148 ms                                                 | 130 ms: 1.14x faster                                                            |
| float                      | 84.7 ms                                                | 74.3 ms: 1.14x faster                                                           |
| pathlib                    | 19.3 ms                                                | 17.0 ms: 1.13x faster                                                           |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.13x faster                                                            |
| raytrace                   | 312 ms                                                 | 276 ms: 1.13x faster                                                            |
| xml_etree_parse            | 159 ms                                                 | 142 ms: 1.12x faster                                                            |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.12x faster                                                            |
| pyflate                    | 482 ms                                                 | 431 ms: 1.12x faster                                                            |
| sympy_integrate            | 21.4 ms                                                | 19.2 ms: 1.12x faster                                                           |
| sympy_str                  | 300 ms                                                 | 269 ms: 1.11x faster                                                            |
| async_generators           | 463 ms                                                 | 418 ms: 1.11x faster                                                            |
| scimark_monte_carlo        | 75.1 ms                                                | 68.2 ms: 1.10x faster                                                           |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.10x faster                                                            |
| chaos                      | 67.0 ms                                                | 61.5 ms: 1.09x faster                                                           |
| regex_effbot               | 3.61 ms                                                | 3.33 ms: 1.08x faster                                                           |
| xml_etree_iterparse        | 107 ms                                                 | 99.1 ms: 1.08x faster                                                           |
| crypto_pyaes               | 81.9 ms                                                | 76.4 ms: 1.07x faster                                                           |
| django_template            | 34.6 ms                                                | 32.6 ms: 1.06x faster                                                           |
| docutils                   | 2.77 sec                                               | 2.61 sec: 1.06x faster                                                          |
| 2to3                       | 274 ms                                                 | 259 ms: 1.06x faster                                                            |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                            |
| sympy_expand               | 478 ms                                                 | 457 ms: 1.05x faster                                                            |
| generators                 | 31.2 ms                                                | 29.9 ms: 1.05x faster                                                           |
| deltablue                  | 3.72 ms                                                | 3.57 ms: 1.04x faster                                                           |
| scimark_fft                | 382 ms                                                 | 369 ms: 1.04x faster                                                            |
| xml_etree_generate         | 89.2 ms                                                | 86.2 ms: 1.03x faster                                                           |
| logging_format             | 7.23 us                                                | 7.02 us: 1.03x faster                                                           |
| richards                   | 45.8 ms                                                | 44.6 ms: 1.03x faster                                                           |
| unpickle_pure_python       | 230 us                                                 | 225 us: 1.02x faster                                                            |
| xml_etree_process          | 61.7 ms                                                | 60.4 ms: 1.02x faster                                                           |
| logging_simple             | 6.46 us                                                | 6.33 us: 1.02x faster                                                           |
| richards_super             | 51.5 ms                                                | 50.7 ms: 1.02x faster                                                           |
| nqueens                    | 83.3 ms                                                | 81.9 ms: 1.02x faster                                                           |
| mako                       | 11.9 ms                                                | 11.8 ms: 1.01x faster                                                           |
| hexiom                     | 6.41 ms                                                | 6.37 ms: 1.01x faster                                                           |
| python_startup_no_site     | 6.94 ms                                                | 6.95 ms: 1.00x slower                                                           |
| sqlite_synth               | 2.83 us                                                | 2.86 us: 1.01x slower                                                           |
| json_loads                 | 28.5 us                                                | 28.8 us: 1.01x slower                                                           |
| pickle_pure_python         | 324 us                                                 | 327 us: 1.01x slower                                                            |
| json                       | 5.26 ms                                                | 5.34 ms: 1.01x slower                                                           |
| regex_v8                   | 23.1 ms                                                | 23.5 ms: 1.02x slower                                                           |
| regex_dna                  | 212 ms                                                 | 216 ms: 1.02x slower                                                            |
| pidigits                   | 187 ms                                                 | 193 ms: 1.03x slower                                                            |
| nbody                      | 97.0 ms                                                | 100 ms: 1.03x slower                                                            |
| pprint_safe_repr           | 776 ms                                                 | 815 ms: 1.05x slower                                                            |
| pprint_pformat             | 1.57 sec                                               | 1.66 sec: 1.06x slower                                                          |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                                            |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.37 ms: 1.06x slower                                                           |
| coroutines                 | 23.2 ms                                                | 24.7 ms: 1.07x slower                                                           |
| json_dumps                 | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                           |
| telco                      | 7.10 ms                                                | 8.02 ms: 1.13x slower                                                           |
| coverage                   | 72.7 ms                                                | 87.7 ms: 1.21x slower                                                           |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.28x slower                                                           |
| gc_traversal               | 3.79 ms                                                | 4.96 ms: 1.31x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 2.59 ms: 1.75x slower                                                           |
| logging_silent             | 104 ns                                                 | 481 ns: 4.60x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                    |

Benchmark hidden because not significant (4): fannkuch, asyncio_websockets, pycparser, scimark_lu
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250620-3.15.0a0-be0ebdc/bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.100x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.13x