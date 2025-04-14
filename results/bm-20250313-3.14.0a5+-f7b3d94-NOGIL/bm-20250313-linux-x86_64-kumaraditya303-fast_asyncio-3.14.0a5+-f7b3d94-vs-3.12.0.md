# Results vs. 3.12.0

- fork: kumaraditya303
- ref: fast_asyncio
- machine: linux-x86_64
- commit hash: f7b3d94
- commit date: 2025-03-13
- overall geometric mean: 1.505x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.99x slower
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 607 ms: 2.21x slower                                                   |
| docutils       | 2.77 sec                                               | 5.62 sec: 2.03x slower                                                 |
| Geometric mean | (ref)                                                  | 2.12x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 1.04 sec: 1.14x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 1.14 sec: 1.01x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 458 ms: 1.02x slower                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 615 ms: 1.07x slower                                                   |
| async_tree_none            | 472 ms                                                 | 547 ms: 1.16x slower                                                   |
| async_tree_memoization     | 578 ms                                                 | 693 ms: 1.20x slower                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 925 ms: 1.27x slower                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 1.01 sec: 1.40x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.11x slower                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 153 ms: 1.81x slower                                                   |
| pidigits       | 187 ms                                                 | 379 ms: 2.02x slower                                                   |
| nbody          | 97.0 ms                                                | 277 ms: 2.86x slower                                                   |
| Geometric mean | (ref)                                                  | 2.19x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 6.75 ms: 1.87x slower                                                  |
| regex_v8       | 23.1 ms                                                | 45.1 ms: 1.95x slower                                                  |
| regex_compile  | 148 ms                                                 | 297 ms: 2.00x slower                                                   |
| regex_dna      | 212 ms                                                 | 432 ms: 2.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.96x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_iterparse  | 107 ms                                                 | 185 ms: 1.73x slower                                                   |
| xml_etree_parse      | 159 ms                                                 | 298 ms: 1.87x slower                                                   |
| tomli_loads          | 2.33 sec                                               | 4.64 sec: 1.99x slower                                                 |
| pickle_pure_python   | 324 us                                                 | 698 us: 2.15x slower                                                   |
| unpickle_pure_python | 230 us                                                 | 503 us: 2.19x slower                                                   |
| xml_etree_generate   | 89.2 ms                                                | 197 ms: 2.21x slower                                                   |
| xml_etree_process    | 61.7 ms                                                | 138 ms: 2.23x slower                                                   |
| json_loads           | 28.5 us                                                | 65.4 us: 2.29x slower                                                  |
| json_dumps           | 10.4 ms                                                | 25.6 ms: 2.47x slower                                                  |
| Geometric mean       | (ref)                                                  | 2.12x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 9.55 ms                                                | 32.6 ms: 3.41x slower                                                  |
| python_startup_no_site | 6.94 ms                                                | 30.9 ms: 4.45x slower                                                  |
| Geometric mean         | (ref)                                                  | 3.90x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 80.4 ms: 2.32x slower                                                  |
| mako            | 11.9 ms                                                | 32.3 ms: 2.71x slower                                                  |
| Geometric mean  | (ref)                                                  | 2.51x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 1.04 sec: 1.14x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 1.14 sec: 1.01x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 458 ms: 1.02x slower                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 615 ms: 1.07x slower                                                   |
| async_tree_none            | 472 ms                                                 | 547 ms: 1.16x slower                                                   |
| gc_traversal               | 3.79 ms                                                | 4.55 ms: 1.20x slower                                                  |
| async_tree_memoization     | 578 ms                                                 | 693 ms: 1.20x slower                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 925 ms: 1.27x slower                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 1.01 sec: 1.40x slower                                                 |
| deepcopy                   | 371 us                                                 | 615 us: 1.66x slower                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 185 ms: 1.73x slower                                                   |
| pathlib                    | 19.3 ms                                                | 34.9 ms: 1.80x slower                                                  |
| float                      | 84.7 ms                                                | 153 ms: 1.81x slower                                                   |
| comprehensions             | 21.8 us                                                | 39.7 us: 1.83x slower                                                  |
| dulwich_log                | 68.5 ms                                                | 126 ms: 1.83x slower                                                   |
| async_generators           | 463 ms                                                 | 862 ms: 1.86x slower                                                   |
| xml_etree_parse            | 159 ms                                                 | 298 ms: 1.87x slower                                                   |
| regex_effbot               | 3.61 ms                                                | 6.75 ms: 1.87x slower                                                  |
| pycparser                  | 1.18 sec                                               | 2.27 sec: 1.92x slower                                                 |
| generators                 | 31.2 ms                                                | 60.3 ms: 1.93x slower                                                  |
| sqlite_synth               | 2.83 us                                                | 5.49 us: 1.94x slower                                                  |
| spectral_norm              | 115 ms                                                 | 224 ms: 1.95x slower                                                   |
| regex_v8                   | 23.1 ms                                                | 45.1 ms: 1.95x slower                                                  |
| deepcopy_memo              | 40.7 us                                                | 79.7 us: 1.96x slower                                                  |
| deepcopy_reduce            | 3.35 us                                                | 6.58 us: 1.97x slower                                                  |
| tomli_loads                | 2.33 sec                                               | 4.64 sec: 1.99x slower                                                 |
| coroutines                 | 23.2 ms                                                | 46.2 ms: 2.00x slower                                                  |
| regex_compile              | 148 ms                                                 | 297 ms: 2.00x slower                                                   |
| asyncio_websockets         | 551 ms                                                 | 1.11 sec: 2.02x slower                                                 |
| pidigits                   | 187 ms                                                 | 379 ms: 2.02x slower                                                   |
| logging_simple             | 6.46 us                                                | 13.1 us: 2.03x slower                                                  |
| docutils                   | 2.77 sec                                               | 5.62 sec: 2.03x slower                                                 |
| logging_format             | 7.23 us                                                | 14.7 us: 2.03x slower                                                  |
| go                         | 139 ms                                                 | 284 ms: 2.04x slower                                                   |
| regex_dna                  | 212 ms                                                 | 432 ms: 2.04x slower                                                   |
| sympy_sum                  | 169 ms                                                 | 352 ms: 2.08x slower                                                   |
| mdp                        | 2.63 sec                                               | 5.49 sec: 2.09x slower                                                 |
| deltablue                  | 3.72 ms                                                | 7.88 ms: 2.12x slower                                                  |
| logging_silent             | 104 ns                                                 | 222 ns: 2.12x slower                                                   |
| sympy_str                  | 300 ms                                                 | 637 ms: 2.13x slower                                                   |
| raytrace                   | 312 ms                                                 | 667 ms: 2.14x slower                                                   |
| chaos                      | 67.0 ms                                                | 144 ms: 2.15x slower                                                   |
| scimark_sor                | 129 ms                                                 | 278 ms: 2.15x slower                                                   |
| pickle_pure_python         | 324 us                                                 | 698 us: 2.15x slower                                                   |
| json                       | 5.26 ms                                                | 11.4 ms: 2.16x slower                                                  |
| pyflate                    | 482 ms                                                 | 1.05 sec: 2.18x slower                                                 |
| sqlalchemy_declarative     | 147 ms                                                 | 320 ms: 2.18x slower                                                   |
| pprint_safe_repr           | 776 ms                                                 | 1.69 sec: 2.18x slower                                                 |
| sqlalchemy_imperative      | 18.7 ms                                                | 40.8 ms: 2.18x slower                                                  |
| unpickle_pure_python       | 230 us                                                 | 503 us: 2.19x slower                                                   |
| crypto_pyaes               | 81.9 ms                                                | 179 ms: 2.19x slower                                                   |
| sympy_integrate            | 21.4 ms                                                | 47.1 ms: 2.20x slower                                                  |
| xml_etree_generate         | 89.2 ms                                                | 197 ms: 2.21x slower                                                   |
| 2to3                       | 274 ms                                                 | 607 ms: 2.21x slower                                                   |
| sympy_expand               | 478 ms                                                 | 1.07 sec: 2.23x slower                                                 |
| pprint_pformat             | 1.57 sec                                               | 3.50 sec: 2.23x slower                                                 |
| xml_etree_process          | 61.7 ms                                                | 138 ms: 2.23x slower                                                   |
| scimark_fft                | 382 ms                                                 | 854 ms: 2.24x slower                                                   |
| json_loads                 | 28.5 us                                                | 65.4 us: 2.29x slower                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 174 ms: 2.32x slower                                                   |
| django_template            | 34.6 ms                                                | 80.4 ms: 2.32x slower                                                  |
| richards                   | 45.8 ms                                                | 107 ms: 2.34x slower                                                   |
| create_gc_cycles           | 1.48 ms                                                | 3.47 ms: 2.35x slower                                                  |
| nqueens                    | 83.3 ms                                                | 196 ms: 2.36x slower                                                   |
| meteor_contest             | 112 ms                                                 | 267 ms: 2.37x slower                                                   |
| hexiom                     | 6.41 ms                                                | 15.3 ms: 2.39x slower                                                  |
| scimark_lu                 | 118 ms                                                 | 288 ms: 2.44x slower                                                   |
| richards_super             | 51.5 ms                                                | 127 ms: 2.46x slower                                                   |
| json_dumps                 | 10.4 ms                                                | 25.6 ms: 2.47x slower                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 12.5 ms: 2.47x slower                                                  |
| fannkuch                   | 417 ms                                                 | 1.05 sec: 2.51x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 408 us: 2.58x slower                                                   |
| telco                      | 7.10 ms                                                | 19.0 ms: 2.68x slower                                                  |
| mako                       | 11.9 ms                                                | 32.3 ms: 2.71x slower                                                  |
| nbody                      | 97.0 ms                                                | 277 ms: 2.86x slower                                                   |
| coverage                   | 72.7 ms                                                | 218 ms: 2.99x slower                                                   |
| python_startup             | 9.55 ms                                                | 32.6 ms: 3.41x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 30.9 ms: 4.45x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 142 ms: 5.92x slower                                                   |
| bench_thread_pool          | 842 us                                                 | 36.5 ms: 43.35x slower                                                 |
| Geometric mean             | (ref)                                                  | 2.13x slower                                                           |
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250313-3.14.0a5+-f7b3d94-NOGIL/bm-20250313-linux-x86_64-kumaraditya303-fast_asyncio-3.14.0a5+-f7b3d94.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.505x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 2.03x
- 95% likely to have a slowdown of 2.02x
- 99% likely to have a slowdown of 1.99x

# Memory
- memory change: 1.31x