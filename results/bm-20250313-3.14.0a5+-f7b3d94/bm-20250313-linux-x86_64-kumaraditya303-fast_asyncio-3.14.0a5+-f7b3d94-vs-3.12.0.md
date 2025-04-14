# Results vs. 3.12.0

- fork: kumaraditya303
- ref: fast_asyncio
- machine: linux-x86_64
- commit hash: f7b3d94
- commit date: 2025-03-13
- overall geometric mean: 1.455x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.76x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 522 ms: 1.90x slower                                                   |
| docutils       | 2.77 sec                                               | 5.25 sec: 1.90x slower                                                 |
| Geometric mean | (ref)                                                  | 1.90x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 1.22 sec: 1.03x slower                                                 |
| async_tree_io              | 1.16 sec                                               | 1.21 sec: 1.05x slower                                                 |
| async_tree_none            | 472 ms                                                 | 515 ms: 1.09x slower                                                   |
| async_tree_none_tg         | 450 ms                                                 | 498 ms: 1.11x slower                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 637 ms: 1.11x slower                                                   |
| async_tree_memoization     | 578 ms                                                 | 646 ms: 1.12x slower                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 973 ms: 1.34x slower                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 1.00 sec: 1.38x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.15x slower                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 144 ms: 1.70x slower                                                   |
| pidigits       | 187 ms                                                 | 372 ms: 1.99x slower                                                   |
| nbody          | 97.0 ms                                                | 203 ms: 2.09x slower                                                   |
| Geometric mean | (ref)                                                  | 1.92x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 256 ms: 1.72x slower                                                   |
| regex_effbot   | 3.61 ms                                                | 6.83 ms: 1.89x slower                                                  |
| regex_v8       | 23.1 ms                                                | 46.5 ms: 2.01x slower                                                  |
| regex_dna      | 212 ms                                                 | 427 ms: 2.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.91x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 3.88 sec: 1.66x slower                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 189 ms: 1.77x slower                                                   |
| xml_etree_parse      | 159 ms                                                 | 287 ms: 1.80x slower                                                   |
| xml_etree_generate   | 89.2 ms                                                | 171 ms: 1.92x slower                                                   |
| xml_etree_process    | 61.7 ms                                                | 119 ms: 1.93x slower                                                   |
| unpickle_pure_python | 230 us                                                 | 444 us: 1.93x slower                                                   |
| pickle_pure_python   | 324 us                                                 | 640 us: 1.98x slower                                                   |
| json_loads           | 28.5 us                                                | 59.5 us: 2.09x slower                                                  |
| json_dumps           | 10.4 ms                                                | 22.8 ms: 2.20x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.91x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 9.55 ms                                                | 31.0 ms: 3.25x slower                                                  |
| python_startup_no_site | 6.94 ms                                                | 31.4 ms: 4.52x slower                                                  |
| Geometric mean         | (ref)                                                  | 3.83x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 64.3 ms: 1.86x slower                                                  |
| mako            | 11.9 ms                                                | 22.5 ms: 1.89x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.88x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 1.22 sec: 1.03x slower                                                 |
| async_tree_io              | 1.16 sec                                               | 1.21 sec: 1.05x slower                                                 |
| async_tree_none            | 472 ms                                                 | 515 ms: 1.09x slower                                                   |
| async_tree_none_tg         | 450 ms                                                 | 498 ms: 1.11x slower                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 637 ms: 1.11x slower                                                   |
| async_tree_memoization     | 578 ms                                                 | 646 ms: 1.12x slower                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 973 ms: 1.34x slower                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 1.00 sec: 1.38x slower                                                 |
| deepcopy                   | 371 us                                                 | 529 us: 1.43x slower                                                   |
| deepcopy_memo              | 40.7 us                                                | 59.8 us: 1.47x slower                                                  |
| comprehensions             | 21.8 us                                                | 33.4 us: 1.53x slower                                                  |
| deepcopy_reduce            | 3.35 us                                                | 5.40 us: 1.62x slower                                                  |
| logging_format             | 7.23 us                                                | 12.0 us: 1.66x slower                                                  |
| tomli_loads                | 2.33 sec                                               | 3.88 sec: 1.66x slower                                                 |
| go                         | 139 ms                                                 | 235 ms: 1.69x slower                                                   |
| logging_simple             | 6.46 us                                                | 10.9 us: 1.69x slower                                                  |
| float                      | 84.7 ms                                                | 144 ms: 1.70x slower                                                   |
| async_generators           | 463 ms                                                 | 787 ms: 1.70x slower                                                   |
| dulwich_log                | 68.5 ms                                                | 118 ms: 1.72x slower                                                   |
| regex_compile              | 148 ms                                                 | 256 ms: 1.72x slower                                                   |
| deltablue                  | 3.72 ms                                                | 6.40 ms: 1.72x slower                                                  |
| raytrace                   | 312 ms                                                 | 542 ms: 1.74x slower                                                   |
| pathlib                    | 19.3 ms                                                | 33.6 ms: 1.74x slower                                                  |
| spectral_norm              | 115 ms                                                 | 202 ms: 1.76x slower                                                   |
| sympy_sum                  | 169 ms                                                 | 297 ms: 1.76x slower                                                   |
| sqlalchemy_imperative      | 18.7 ms                                                | 33.0 ms: 1.77x slower                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 189 ms: 1.77x slower                                                   |
| sqlalchemy_declarative     | 147 ms                                                 | 262 ms: 1.78x slower                                                   |
| sympy_str                  | 300 ms                                                 | 535 ms: 1.78x slower                                                   |
| xml_etree_parse            | 159 ms                                                 | 287 ms: 1.80x slower                                                   |
| chaos                      | 67.0 ms                                                | 123 ms: 1.83x slower                                                   |
| generators                 | 31.2 ms                                                | 57.6 ms: 1.85x slower                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 139 ms: 1.85x slower                                                   |
| django_template            | 34.6 ms                                                | 64.3 ms: 1.86x slower                                                  |
| sympy_integrate            | 21.4 ms                                                | 39.9 ms: 1.86x slower                                                  |
| scimark_sor                | 129 ms                                                 | 241 ms: 1.87x slower                                                   |
| scimark_fft                | 382 ms                                                 | 717 ms: 1.88x slower                                                   |
| crypto_pyaes               | 81.9 ms                                                | 154 ms: 1.89x slower                                                   |
| regex_effbot               | 3.61 ms                                                | 6.83 ms: 1.89x slower                                                  |
| meteor_contest             | 112 ms                                                 | 213 ms: 1.89x slower                                                   |
| mdp                        | 2.63 sec                                               | 4.98 sec: 1.89x slower                                                 |
| sympy_expand               | 478 ms                                                 | 905 ms: 1.89x slower                                                   |
| mako                       | 11.9 ms                                                | 22.5 ms: 1.89x slower                                                  |
| docutils                   | 2.77 sec                                               | 5.25 sec: 1.90x slower                                                 |
| pprint_safe_repr           | 776 ms                                                 | 1.47 sec: 1.90x slower                                                 |
| pyflate                    | 482 ms                                                 | 916 ms: 1.90x slower                                                   |
| 2to3                       | 274 ms                                                 | 522 ms: 1.90x slower                                                   |
| pprint_pformat             | 1.57 sec                                               | 2.99 sec: 1.91x slower                                                 |
| xml_etree_generate         | 89.2 ms                                                | 171 ms: 1.92x slower                                                   |
| logging_silent             | 104 ns                                                 | 201 ns: 1.92x slower                                                   |
| xml_etree_process          | 61.7 ms                                                | 119 ms: 1.93x slower                                                   |
| unpickle_pure_python       | 230 us                                                 | 444 us: 1.93x slower                                                   |
| richards                   | 45.8 ms                                                | 89.1 ms: 1.94x slower                                                  |
| hexiom                     | 6.41 ms                                                | 12.5 ms: 1.94x slower                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 9.84 ms: 1.95x slower                                                  |
| richards_super             | 51.5 ms                                                | 101 ms: 1.96x slower                                                   |
| asyncio_websockets         | 551 ms                                                 | 1.09 sec: 1.97x slower                                                 |
| sqlite_synth               | 2.83 us                                                | 5.58 us: 1.97x slower                                                  |
| pickle_pure_python         | 324 us                                                 | 640 us: 1.98x slower                                                   |
| pidigits                   | 187 ms                                                 | 372 ms: 1.99x slower                                                   |
| nqueens                    | 83.3 ms                                                | 166 ms: 1.99x slower                                                   |
| pycparser                  | 1.18 sec                                               | 2.35 sec: 1.99x slower                                                 |
| scimark_lu                 | 118 ms                                                 | 236 ms: 2.00x slower                                                   |
| regex_v8                   | 23.1 ms                                                | 46.5 ms: 2.01x slower                                                  |
| regex_dna                  | 212 ms                                                 | 427 ms: 2.01x slower                                                   |
| json                       | 5.26 ms                                                | 10.6 ms: 2.01x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 323 us: 2.04x slower                                                   |
| fannkuch                   | 417 ms                                                 | 860 ms: 2.06x slower                                                   |
| coroutines                 | 23.2 ms                                                | 47.8 ms: 2.06x slower                                                  |
| json_loads                 | 28.5 us                                                | 59.5 us: 2.09x slower                                                  |
| nbody                      | 97.0 ms                                                | 203 ms: 2.09x slower                                                   |
| json_dumps                 | 10.4 ms                                                | 22.8 ms: 2.20x slower                                                  |
| telco                      | 7.10 ms                                                | 16.0 ms: 2.25x slower                                                  |
| coverage                   | 72.7 ms                                                | 183 ms: 2.52x slower                                                   |
| gc_traversal               | 3.79 ms                                                | 10.4 ms: 2.73x slower                                                  |
| python_startup             | 9.55 ms                                                | 31.0 ms: 3.25x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 5.07 ms: 3.44x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 31.4 ms: 4.52x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 130 ms: 5.41x slower                                                   |
| bench_thread_pool          | 842 us                                                 | 29.8 ms: 35.46x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.93x slower                                                           |
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250313-3.14.0a5+-f7b3d94/bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.455x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.80x
- 95% likely to have a slowdown of 1.79x
- 99% likely to have a slowdown of 1.76x

# Memory
- memory change: 1.09x