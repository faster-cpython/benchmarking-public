# Results vs. 3.12.0

- fork: kumaraditya303
- ref: freelist_async
- machine: linux-x86_64
- commit hash: cfae815
- commit date: 2025-04-03
- overall geometric mean: 1.135x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 247 ms: 1.11x faster                                                     |
| docutils       | 2.77 sec                                               | 2.59 sec: 1.07x faster                                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 601 ms: 1.97x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 621 ms: 1.86x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 311 ms: 1.86x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.82x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.81x faster                                                     |
| async_tree_none            | 472 ms                                                 | 263 ms: 1.80x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.51x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 485 ms: 1.50x faster                                                     |
| Geometric mean             | (ref)                                                  | 1.76x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 67.0 ms: 1.26x faster                                                    |
| nbody          | 97.0 ms                                                | 90.1 ms: 1.08x faster                                                    |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.11x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 123 ms: 1.20x faster                                                     |
| regex_effbot   | 3.61 ms                                                | 3.34 ms: 1.08x faster                                                    |
| regex_v8       | 23.1 ms                                                | 23.1 ms: 1.00x faster                                                    |
| regex_dna      | 212 ms                                                 | 219 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                  | 1.06x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.90 sec: 1.23x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                 | 98.5 ms: 1.08x faster                                                    |
| unpickle_pure_python | 230 us                                                 | 215 us: 1.07x faster                                                     |
| xml_etree_generate   | 89.2 ms                                                | 84.1 ms: 1.06x faster                                                    |
| xml_etree_process    | 61.7 ms                                                | 58.5 ms: 1.06x faster                                                    |
| pickle_pure_python   | 324 us                                                 | 311 us: 1.04x faster                                                     |
| json_loads           | 28.5 us                                                | 30.0 us: 1.05x slower                                                    |
| json_dumps           | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.17 ms: 1.18x slower                                                    |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.4 ms: 1.07x faster                                                    |
| mako            | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.22 sec: 2.16x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 601 ms: 1.97x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 621 ms: 1.86x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 311 ms: 1.86x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.82x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.81x faster                                                     |
| async_tree_none            | 472 ms                                                 | 263 ms: 1.80x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.51x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 485 ms: 1.50x faster                                                     |
| deepcopy                   | 371 us                                                 | 252 us: 1.48x faster                                                     |
| deepcopy_memo              | 40.7 us                                                | 28.9 us: 1.41x faster                                                    |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                    |
| go                         | 139 ms                                                 | 108 ms: 1.29x faster                                                     |
| float                      | 84.7 ms                                                | 67.0 ms: 1.26x faster                                                    |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                                    |
| raytrace                   | 312 ms                                                 | 254 ms: 1.23x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 1.90 sec: 1.23x faster                                                   |
| regex_compile              | 148 ms                                                 | 123 ms: 1.20x faster                                                     |
| chaos                      | 67.0 ms                                                | 56.2 ms: 1.19x faster                                                    |
| logging_format             | 7.23 us                                                | 6.08 us: 1.19x faster                                                    |
| scimark_monte_carlo        | 75.1 ms                                                | 63.9 ms: 1.18x faster                                                    |
| async_generators           | 463 ms                                                 | 394 ms: 1.18x faster                                                     |
| logging_simple             | 6.46 us                                                | 5.50 us: 1.17x faster                                                    |
| dulwich_log                | 68.5 ms                                                | 59.0 ms: 1.16x faster                                                    |
| pathlib                    | 19.3 ms                                                | 16.7 ms: 1.16x faster                                                    |
| deltablue                  | 3.72 ms                                                | 3.24 ms: 1.15x faster                                                    |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                                     |
| logging_silent             | 104 ns                                                 | 92.2 ns: 1.13x faster                                                    |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.13x faster                                                     |
| sympy_integrate            | 21.4 ms                                                | 19.1 ms: 1.12x faster                                                    |
| scimark_fft                | 382 ms                                                 | 340 ms: 1.12x faster                                                     |
| sympy_str                  | 300 ms                                                 | 267 ms: 1.12x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 73.1 ms: 1.12x faster                                                    |
| scimark_sor                | 129 ms                                                 | 115 ms: 1.12x faster                                                     |
| sqlalchemy_declarative     | 147 ms                                                 | 132 ms: 1.11x faster                                                     |
| pyflate                    | 482 ms                                                 | 435 ms: 1.11x faster                                                     |
| 2to3                       | 274 ms                                                 | 247 ms: 1.11x faster                                                     |
| spectral_norm              | 115 ms                                                 | 104 ms: 1.10x faster                                                     |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.0 ms: 1.10x faster                                                    |
| generators                 | 31.2 ms                                                | 28.7 ms: 1.09x faster                                                    |
| pprint_safe_repr           | 776 ms                                                 | 713 ms: 1.09x faster                                                     |
| richards                   | 45.8 ms                                                | 42.3 ms: 1.08x faster                                                    |
| xml_etree_iterparse        | 107 ms                                                 | 98.5 ms: 1.08x faster                                                    |
| regex_effbot               | 3.61 ms                                                | 3.34 ms: 1.08x faster                                                    |
| pprint_pformat             | 1.57 sec                                               | 1.45 sec: 1.08x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.70 ms: 1.08x faster                                                    |
| nbody                      | 97.0 ms                                                | 90.1 ms: 1.08x faster                                                    |
| unpickle_pure_python       | 230 us                                                 | 215 us: 1.07x faster                                                     |
| docutils                   | 2.77 sec                                               | 2.59 sec: 1.07x faster                                                   |
| django_template            | 34.6 ms                                                | 32.4 ms: 1.07x faster                                                    |
| richards_super             | 51.5 ms                                                | 48.3 ms: 1.07x faster                                                    |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                     |
| xml_etree_generate         | 89.2 ms                                                | 84.1 ms: 1.06x faster                                                    |
| xml_etree_process          | 61.7 ms                                                | 58.5 ms: 1.06x faster                                                    |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                    |
| sympy_expand               | 478 ms                                                 | 457 ms: 1.05x faster                                                     |
| pickle_pure_python         | 324 us                                                 | 311 us: 1.04x faster                                                     |
| hexiom                     | 6.41 ms                                                | 6.19 ms: 1.04x faster                                                    |
| nqueens                    | 83.3 ms                                                | 80.7 ms: 1.03x faster                                                    |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                   |
| sqlite_synth               | 2.83 us                                                | 2.78 us: 1.02x faster                                                    |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                                     |
| fannkuch                   | 417 ms                                                 | 412 ms: 1.01x faster                                                     |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                     |
| regex_v8                   | 23.1 ms                                                | 23.1 ms: 1.00x faster                                                    |
| coroutines                 | 23.2 ms                                                | 23.8 ms: 1.03x slower                                                    |
| regex_dna                  | 212 ms                                                 | 219 ms: 1.03x slower                                                     |
| bench_thread_pool          | 842 us                                                 | 875 us: 1.04x slower                                                     |
| typing_runtime_protocols   | 158 us                                                 | 165 us: 1.05x slower                                                     |
| json_loads                 | 28.5 us                                                | 30.0 us: 1.05x slower                                                    |
| telco                      | 7.10 ms                                                | 7.79 ms: 1.10x slower                                                    |
| json_dumps                 | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                    |
| coverage                   | 72.7 ms                                                | 85.5 ms: 1.18x slower                                                    |
| python_startup_no_site     | 6.94 ms                                                | 8.17 ms: 1.18x slower                                                    |
| gc_traversal               | 3.79 ms                                                | 4.95 ms: 1.30x slower                                                    |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                    |
| create_gc_cycles           | 1.48 ms                                                | 2.45 ms: 1.66x slower                                                    |
| bench_mp_pool              | 24.0 ms                                                | 82.1 ms: 3.42x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.11x faster                                                             |

Benchmark hidden because not significant (2): asyncio_websockets, json
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250403-3.14.0a6+-cfae815/bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.135x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.10x