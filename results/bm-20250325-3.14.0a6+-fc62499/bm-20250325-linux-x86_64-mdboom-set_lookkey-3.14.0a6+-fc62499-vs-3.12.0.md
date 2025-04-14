# Results vs. 3.12.0

- fork: mdboom
- ref: set_lookkey
- machine: linux-x86_64
- commit hash: fc62499
- commit date: 2025-03-25
- overall geometric mean: 1.105x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6+-fc62499 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 257 ms: 1.07x faster                                          |
| docutils       | 2.77 sec                                               | 2.62 sec: 1.06x faster                                        |
| Geometric mean | (ref)                                                  | 1.06x faster                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6+-fc62499 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 611 ms: 1.93x faster                                          |
| async_tree_io              | 1.16 sec                                               | 610 ms: 1.89x faster                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 309 ms: 1.86x faster                                          |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                          |
| async_tree_none            | 472 ms                                                 | 257 ms: 1.83x faster                                          |
| async_tree_none_tg         | 450 ms                                                 | 247 ms: 1.82x faster                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 472 ms: 1.54x faster                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 489 ms: 1.48x faster                                          |
| Geometric mean             | (ref)                                                  | 1.77x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6+-fc62499 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.0 ms: 1.21x faster                                         |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                          |
| nbody          | 97.0 ms                                                | 99.9 ms: 1.03x slower                                         |
| Geometric mean | (ref)                                                  | 1.06x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6+-fc62499 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                          |
| regex_effbot   | 3.61 ms                                                | 3.30 ms: 1.10x faster                                         |
| regex_dna      | 212 ms                                                 | 219 ms: 1.03x slower                                          |
| regex_v8       | 23.1 ms                                                | 24.0 ms: 1.04x slower                                         |
| Geometric mean | (ref)                                                  | 1.05x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6+-fc62499 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.02 sec: 1.15x faster                                        |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                          |
| xml_etree_iterparse  | 107 ms                                                 | 98.8 ms: 1.08x faster                                         |
| xml_etree_generate   | 89.2 ms                                                | 84.2 ms: 1.06x faster                                         |
| xml_etree_process    | 61.7 ms                                                | 58.7 ms: 1.05x faster                                         |
| unpickle_pure_python | 230 us                                                 | 221 us: 1.04x faster                                          |
| pickle_pure_python   | 324 us                                                 | 315 us: 1.03x faster                                          |
| json_loads           | 28.5 us                                                | 30.0 us: 1.05x slower                                         |
| json_dumps           | 10.4 ms                                                | 11.5 ms: 1.10x slower                                         |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6+-fc62499 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.22 ms: 1.19x slower                                         |
| python_startup         | 9.55 ms                                                | 13.2 ms: 1.38x slower                                         |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6+-fc62499 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.4 ms: 1.10x faster                                         |
| mako            | 11.9 ms                                                | 11.2 ms: 1.07x faster                                         |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6+-fc62499 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 611 ms: 1.93x faster                                          |
| async_tree_io              | 1.16 sec                                               | 610 ms: 1.89x faster                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 309 ms: 1.86x faster                                          |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                          |
| async_tree_none            | 472 ms                                                 | 257 ms: 1.83x faster                                          |
| async_tree_none_tg         | 450 ms                                                 | 247 ms: 1.82x faster                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 472 ms: 1.54x faster                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 489 ms: 1.48x faster                                          |
| deepcopy                   | 371 us                                                 | 256 us: 1.45x faster                                          |
| deepcopy_memo              | 40.7 us                                                | 29.6 us: 1.37x faster                                         |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                         |
| deepcopy_reduce            | 3.35 us                                                | 2.70 us: 1.24x faster                                         |
| go                         | 139 ms                                                 | 114 ms: 1.22x faster                                          |
| float                      | 84.7 ms                                                | 70.0 ms: 1.21x faster                                         |
| deltablue                  | 3.72 ms                                                | 3.08 ms: 1.21x faster                                         |
| raytrace                   | 312 ms                                                 | 265 ms: 1.18x faster                                          |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                          |
| pathlib                    | 19.3 ms                                                | 16.6 ms: 1.16x faster                                         |
| async_generators           | 463 ms                                                 | 398 ms: 1.16x faster                                          |
| logging_simple             | 6.46 us                                                | 5.60 us: 1.15x faster                                         |
| tomli_loads                | 2.33 sec                                               | 2.02 sec: 1.15x faster                                        |
| logging_format             | 7.23 us                                                | 6.28 us: 1.15x faster                                         |
| dulwich_log                | 68.5 ms                                                | 60.1 ms: 1.14x faster                                         |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                          |
| logging_silent             | 104 ns                                                 | 93.0 ns: 1.12x faster                                         |
| chaos                      | 67.0 ms                                                | 59.6 ms: 1.12x faster                                         |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.12x faster                                          |
| sympy_sum                  | 169 ms                                                 | 152 ms: 1.11x faster                                          |
| sympy_str                  | 300 ms                                                 | 269 ms: 1.11x faster                                          |
| sqlalchemy_declarative     | 147 ms                                                 | 132 ms: 1.11x faster                                          |
| scimark_monte_carlo        | 75.1 ms                                                | 68.2 ms: 1.10x faster                                         |
| django_template            | 34.6 ms                                                | 31.4 ms: 1.10x faster                                         |
| regex_effbot               | 3.61 ms                                                | 3.30 ms: 1.10x faster                                         |
| sympy_integrate            | 21.4 ms                                                | 19.7 ms: 1.09x faster                                         |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.08x faster                                          |
| xml_etree_iterparse        | 107 ms                                                 | 98.8 ms: 1.08x faster                                         |
| generators                 | 31.2 ms                                                | 28.9 ms: 1.08x faster                                         |
| 2to3                       | 274 ms                                                 | 257 ms: 1.07x faster                                          |
| scimark_fft                | 382 ms                                                 | 358 ms: 1.07x faster                                          |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.5 ms: 1.07x faster                                         |
| pprint_safe_repr           | 776 ms                                                 | 727 ms: 1.07x faster                                          |
| mako                       | 11.9 ms                                                | 11.2 ms: 1.07x faster                                         |
| xml_etree_generate         | 89.2 ms                                                | 84.2 ms: 1.06x faster                                         |
| crypto_pyaes               | 81.9 ms                                                | 77.3 ms: 1.06x faster                                         |
| docutils                   | 2.77 sec                                               | 2.62 sec: 1.06x faster                                        |
| xml_etree_process          | 61.7 ms                                                | 58.7 ms: 1.05x faster                                         |
| richards                   | 45.8 ms                                                | 43.6 ms: 1.05x faster                                         |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.05x faster                                        |
| sympy_expand               | 478 ms                                                 | 455 ms: 1.05x faster                                          |
| mdp                        | 2.63 sec                                               | 2.51 sec: 1.05x faster                                        |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.04x faster                                        |
| unpickle_pure_python       | 230 us                                                 | 221 us: 1.04x faster                                          |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.89 ms: 1.03x faster                                         |
| richards_super             | 51.5 ms                                                | 49.9 ms: 1.03x faster                                         |
| pickle_pure_python         | 324 us                                                 | 315 us: 1.03x faster                                          |
| pyflate                    | 482 ms                                                 | 470 ms: 1.03x faster                                          |
| meteor_contest             | 112 ms                                                 | 110 ms: 1.03x faster                                          |
| sqlite_synth               | 2.83 us                                                | 2.77 us: 1.02x faster                                         |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                          |
| hexiom                     | 6.41 ms                                                | 6.33 ms: 1.01x faster                                         |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                          |
| typing_runtime_protocols   | 158 us                                                 | 159 us: 1.01x slower                                          |
| nqueens                    | 83.3 ms                                                | 84.2 ms: 1.01x slower                                         |
| json                       | 5.26 ms                                                | 5.35 ms: 1.02x slower                                         |
| nbody                      | 97.0 ms                                                | 99.9 ms: 1.03x slower                                         |
| regex_dna                  | 212 ms                                                 | 219 ms: 1.03x slower                                          |
| regex_v8                   | 23.1 ms                                                | 24.0 ms: 1.04x slower                                         |
| coroutines                 | 23.2 ms                                                | 24.2 ms: 1.04x slower                                         |
| bench_thread_pool          | 842 us                                                 | 880 us: 1.05x slower                                          |
| fannkuch                   | 417 ms                                                 | 437 ms: 1.05x slower                                          |
| json_loads                 | 28.5 us                                                | 30.0 us: 1.05x slower                                         |
| json_dumps                 | 10.4 ms                                                | 11.5 ms: 1.10x slower                                         |
| telco                      | 7.10 ms                                                | 7.84 ms: 1.10x slower                                         |
| python_startup_no_site     | 6.94 ms                                                | 8.22 ms: 1.19x slower                                         |
| coverage                   | 72.7 ms                                                | 92.4 ms: 1.27x slower                                         |
| gc_traversal               | 3.79 ms                                                | 4.99 ms: 1.32x slower                                         |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.38x slower                                         |
| create_gc_cycles           | 1.48 ms                                                | 2.49 ms: 1.69x slower                                         |
| bench_mp_pool              | 24.0 ms                                                | 84.1 ms: 3.50x slower                                         |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                  |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250325-3.14.0a6+-fc62499/bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6+-fc62499.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.105x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.10x