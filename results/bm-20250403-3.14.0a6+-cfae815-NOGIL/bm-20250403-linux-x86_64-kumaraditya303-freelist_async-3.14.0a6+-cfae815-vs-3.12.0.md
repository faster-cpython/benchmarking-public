# Results vs. 3.12.0

- fork: kumaraditya303
- ref: freelist_async
- machine: linux-x86_64
- commit hash: cfae815
- commit date: 2025-04-03
- overall geometric mean: 1.047x faster
- HPT reliability: 66.82%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 287 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                  | 1.02x slower                                                             |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 504 ms: 2.34x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 542 ms: 2.13x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 223 ms: 2.02x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 292 ms: 1.97x faster                                                     |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 328 ms: 1.76x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 449 ms: 1.62x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 487 ms: 1.49x faster                                                     |
| Geometric mean             | (ref)                                                  | 1.87x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 68.5 ms: 1.24x faster                                                    |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                                     |
| nbody          | 97.0 ms                                                | 119 ms: 1.22x slower                                                     |
| Geometric mean | (ref)                                                  | 1.00x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.32 ms: 1.09x faster                                                    |
| regex_v8       | 23.1 ms                                                | 22.0 ms: 1.05x faster                                                    |
| regex_compile  | 148 ms                                                 | 143 ms: 1.04x faster                                                     |
| regex_dna      | 212 ms                                                 | 211 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.04x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse  | 107 ms                                                 | 93.9 ms: 1.14x faster                                                    |
| tomli_loads          | 2.33 sec                                               | 2.15 sec: 1.09x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.07x faster                                                     |
| unpickle_pure_python | 230 us                                                 | 236 us: 1.03x slower                                                     |
| pickle_pure_python   | 324 us                                                 | 336 us: 1.04x slower                                                     |
| xml_etree_generate   | 89.2 ms                                                | 93.4 ms: 1.05x slower                                                    |
| xml_etree_process    | 61.7 ms                                                | 65.5 ms: 1.06x slower                                                    |
| json_loads           | 28.5 us                                                | 32.1 us: 1.13x slower                                                    |
| json_dumps           | 10.4 ms                                                | 12.8 ms: 1.23x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 10.9 ms: 1.58x slower                                                    |
| python_startup         | 9.55 ms                                                | 15.6 ms: 1.63x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.60x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 38.2 ms: 1.11x slower                                                    |
| mako            | 11.9 ms                                                | 15.7 ms: 1.32x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.21x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 504 ms: 2.34x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 542 ms: 2.13x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 223 ms: 2.02x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 292 ms: 1.97x faster                                                     |
| mdp                        | 2.63 sec                                               | 1.37 sec: 1.92x faster                                                   |
| gc_traversal               | 3.79 ms                                                | 2.03 ms: 1.87x faster                                                    |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 328 ms: 1.76x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 449 ms: 1.62x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 487 ms: 1.49x faster                                                     |
| deepcopy                   | 371 us                                                 | 292 us: 1.27x faster                                                     |
| float                      | 84.7 ms                                                | 68.5 ms: 1.24x faster                                                    |
| pathlib                    | 19.3 ms                                                | 16.7 ms: 1.16x faster                                                    |
| deepcopy_memo              | 40.7 us                                                | 35.2 us: 1.16x faster                                                    |
| xml_etree_iterparse        | 107 ms                                                 | 93.9 ms: 1.14x faster                                                    |
| comprehensions             | 21.8 us                                                | 19.2 us: 1.14x faster                                                    |
| async_generators           | 463 ms                                                 | 419 ms: 1.11x faster                                                     |
| dulwich_log                | 68.5 ms                                                | 62.7 ms: 1.09x faster                                                    |
| regex_effbot               | 3.61 ms                                                | 3.32 ms: 1.09x faster                                                    |
| tomli_loads                | 2.33 sec                                               | 2.15 sec: 1.09x faster                                                   |
| go                         | 139 ms                                                 | 129 ms: 1.08x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                | 3.10 us: 1.08x faster                                                    |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.07x faster                                                     |
| generators                 | 31.2 ms                                                | 29.6 ms: 1.06x faster                                                    |
| spectral_norm              | 115 ms                                                 | 109 ms: 1.05x faster                                                     |
| regex_v8                   | 23.1 ms                                                | 22.0 ms: 1.05x faster                                                    |
| regex_compile              | 148 ms                                                 | 143 ms: 1.04x faster                                                     |
| deltablue                  | 3.72 ms                                                | 3.60 ms: 1.03x faster                                                    |
| chaos                      | 67.0 ms                                                | 65.0 ms: 1.03x faster                                                    |
| scimark_fft                | 382 ms                                                 | 371 ms: 1.03x faster                                                     |
| pyflate                    | 482 ms                                                 | 469 ms: 1.03x faster                                                     |
| sqlite_synth               | 2.83 us                                                | 2.78 us: 1.02x faster                                                    |
| scimark_sor                | 129 ms                                                 | 127 ms: 1.02x faster                                                     |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                   |
| logging_silent             | 104 ns                                                 | 103 ns: 1.01x faster                                                     |
| raytrace                   | 312 ms                                                 | 308 ms: 1.01x faster                                                     |
| logging_simple             | 6.46 us                                                | 6.41 us: 1.01x faster                                                    |
| regex_dna                  | 212 ms                                                 | 211 ms: 1.01x faster                                                     |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                                     |
| sympy_sum                  | 169 ms                                                 | 173 ms: 1.03x slower                                                     |
| unpickle_pure_python       | 230 us                                                 | 236 us: 1.03x slower                                                     |
| sympy_str                  | 300 ms                                                 | 309 ms: 1.03x slower                                                     |
| pprint_safe_repr           | 776 ms                                                 | 801 ms: 1.03x slower                                                     |
| pickle_pure_python         | 324 us                                                 | 336 us: 1.04x slower                                                     |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.28 ms: 1.04x slower                                                    |
| coroutines                 | 23.2 ms                                                | 24.2 ms: 1.04x slower                                                    |
| 2to3                       | 274 ms                                                 | 287 ms: 1.04x slower                                                     |
| sympy_integrate            | 21.4 ms                                                | 22.4 ms: 1.05x slower                                                    |
| scimark_monte_carlo        | 75.1 ms                                                | 78.7 ms: 1.05x slower                                                    |
| xml_etree_generate         | 89.2 ms                                                | 93.4 ms: 1.05x slower                                                    |
| crypto_pyaes               | 81.9 ms                                                | 86.1 ms: 1.05x slower                                                    |
| json                       | 5.26 ms                                                | 5.56 ms: 1.06x slower                                                    |
| pprint_pformat             | 1.57 sec                                               | 1.66 sec: 1.06x slower                                                   |
| xml_etree_process          | 61.7 ms                                                | 65.5 ms: 1.06x slower                                                    |
| nqueens                    | 83.3 ms                                                | 89.3 ms: 1.07x slower                                                    |
| sqlalchemy_declarative     | 147 ms                                                 | 158 ms: 1.07x slower                                                     |
| sympy_expand               | 478 ms                                                 | 520 ms: 1.09x slower                                                     |
| sqlalchemy_imperative      | 18.7 ms                                                | 20.5 ms: 1.10x slower                                                    |
| django_template            | 34.6 ms                                                | 38.2 ms: 1.11x slower                                                    |
| hexiom                     | 6.41 ms                                                | 7.17 ms: 1.12x slower                                                    |
| scimark_lu                 | 118 ms                                                 | 132 ms: 1.12x slower                                                     |
| richards                   | 45.8 ms                                                | 51.5 ms: 1.12x slower                                                    |
| json_loads                 | 28.5 us                                                | 32.1 us: 1.13x slower                                                    |
| richards_super             | 51.5 ms                                                | 59.0 ms: 1.14x slower                                                    |
| create_gc_cycles           | 1.48 ms                                                | 1.69 ms: 1.15x slower                                                    |
| fannkuch                   | 417 ms                                                 | 482 ms: 1.15x slower                                                     |
| meteor_contest             | 112 ms                                                 | 133 ms: 1.18x slower                                                     |
| nbody                      | 97.0 ms                                                | 119 ms: 1.22x slower                                                     |
| json_dumps                 | 10.4 ms                                                | 12.8 ms: 1.23x slower                                                    |
| typing_runtime_protocols   | 158 us                                                 | 195 us: 1.23x slower                                                     |
| telco                      | 7.10 ms                                                | 9.18 ms: 1.29x slower                                                    |
| mako                       | 11.9 ms                                                | 15.7 ms: 1.32x slower                                                    |
| python_startup_no_site     | 6.94 ms                                                | 10.9 ms: 1.58x slower                                                    |
| coverage                   | 72.7 ms                                                | 119 ms: 1.63x slower                                                     |
| python_startup             | 9.55 ms                                                | 15.6 ms: 1.63x slower                                                    |
| bench_mp_pool              | 24.0 ms                                                | 90.1 ms: 3.75x slower                                                    |
| bench_thread_pool          | 842 us                                                 | 3.25 ms: 3.86x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (3): asyncio_websockets, docutils, logging_format
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250403-3.14.0a6+-cfae815-NOGIL/bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.047x faster

# HPT report

- Reliability score: 66.82% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.32x