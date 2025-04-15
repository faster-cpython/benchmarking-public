# Results vs. 3.12.0

- fork: eendebakpt
- ref: list_freelist_plus
- machine: linux-x86_64
- commit hash: 77f3e29
- commit date: 2025-04-08
- overall geometric mean: 1.137x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7+-77f3e29 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 252 ms: 1.09x faster                                                     |
| docutils       | 2.77 sec                                               | 2.59 sec: 1.07x faster                                                   |
| Geometric mean | (ref)                                                  | 1.08x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7+-77f3e29 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 617 ms: 1.92x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 608 ms: 1.90x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 310 ms: 1.86x faster                                                     |
| async_tree_none            | 472 ms                                                 | 255 ms: 1.85x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 312 ms: 1.84x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 247 ms: 1.82x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 469 ms: 1.55x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 481 ms: 1.51x faster                                                     |
| Geometric mean             | (ref)                                                  | 1.77x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7+-77f3e29 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 68.3 ms: 1.24x faster                                                    |
| nbody          | 97.0 ms                                                | 95.5 ms: 1.02x faster                                                    |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.08x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7+-77f3e29 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 125 ms: 1.19x faster                                                     |
| regex_effbot   | 3.61 ms                                                | 3.10 ms: 1.17x faster                                                    |
| regex_dna      | 212 ms                                                 | 204 ms: 1.04x faster                                                     |
| regex_v8       | 23.1 ms                                                | 22.8 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                  | 1.10x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7+-77f3e29 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 143 ms: 1.11x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                 | 99.3 ms: 1.08x faster                                                    |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                     |
| xml_etree_generate   | 89.2 ms                                                | 85.1 ms: 1.05x faster                                                    |
| pickle_pure_python   | 324 us                                                 | 312 us: 1.04x faster                                                     |
| xml_etree_process    | 61.7 ms                                                | 59.9 ms: 1.03x faster                                                    |
| json_loads           | 28.5 us                                                | 29.2 us: 1.03x slower                                                    |
| json_dumps           | 10.4 ms                                                | 11.6 ms: 1.11x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7+-77f3e29 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.21 ms: 1.18x slower                                                    |
| python_startup         | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7+-77f3e29 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.4 ms: 1.10x faster                                                    |
| mako            | 11.9 ms                                                | 11.2 ms: 1.06x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7+-77f3e29 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.21 sec: 2.17x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 617 ms: 1.92x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 608 ms: 1.90x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 310 ms: 1.86x faster                                                     |
| async_tree_none            | 472 ms                                                 | 255 ms: 1.85x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 312 ms: 1.84x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 247 ms: 1.82x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 469 ms: 1.55x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 481 ms: 1.51x faster                                                     |
| deepcopy                   | 371 us                                                 | 251 us: 1.48x faster                                                     |
| deepcopy_memo              | 40.7 us                                                | 28.8 us: 1.41x faster                                                    |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.30x faster                                                    |
| deepcopy_reduce            | 3.35 us                                                | 2.60 us: 1.29x faster                                                    |
| go                         | 139 ms                                                 | 112 ms: 1.25x faster                                                     |
| float                      | 84.7 ms                                                | 68.3 ms: 1.24x faster                                                    |
| chaos                      | 67.0 ms                                                | 54.6 ms: 1.23x faster                                                    |
| raytrace                   | 312 ms                                                 | 257 ms: 1.22x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                   |
| logging_format             | 7.23 us                                                | 6.04 us: 1.20x faster                                                    |
| async_generators           | 463 ms                                                 | 388 ms: 1.19x faster                                                     |
| regex_compile              | 148 ms                                                 | 125 ms: 1.19x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 69.9 ms: 1.17x faster                                                    |
| regex_effbot               | 3.61 ms                                                | 3.10 ms: 1.17x faster                                                    |
| pathlib                    | 19.3 ms                                                | 16.6 ms: 1.16x faster                                                    |
| logging_simple             | 6.46 us                                                | 5.55 us: 1.16x faster                                                    |
| dulwich_log                | 68.5 ms                                                | 59.3 ms: 1.15x faster                                                    |
| scimark_monte_carlo        | 75.1 ms                                                | 65.3 ms: 1.15x faster                                                    |
| spectral_norm              | 115 ms                                                 | 100.0 ms: 1.15x faster                                                   |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                                     |
| sympy_integrate            | 21.4 ms                                                | 19.2 ms: 1.12x faster                                                    |
| sympy_str                  | 300 ms                                                 | 268 ms: 1.12x faster                                                     |
| xml_etree_parse            | 159 ms                                                 | 143 ms: 1.11x faster                                                     |
| scimark_fft                | 382 ms                                                 | 344 ms: 1.11x faster                                                     |
| sqlalchemy_declarative     | 147 ms                                                 | 132 ms: 1.11x faster                                                     |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.9 ms: 1.11x faster                                                    |
| deltablue                  | 3.72 ms                                                | 3.36 ms: 1.10x faster                                                    |
| django_template            | 34.6 ms                                                | 31.4 ms: 1.10x faster                                                    |
| fannkuch                   | 417 ms                                                 | 381 ms: 1.10x faster                                                     |
| 2to3                       | 274 ms                                                 | 252 ms: 1.09x faster                                                     |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.08x faster                                                     |
| pyflate                    | 482 ms                                                 | 446 ms: 1.08x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                 | 99.3 ms: 1.08x faster                                                    |
| nqueens                    | 83.3 ms                                                | 77.7 ms: 1.07x faster                                                    |
| hexiom                     | 6.41 ms                                                | 5.99 ms: 1.07x faster                                                    |
| pycparser                  | 1.18 sec                                               | 1.10 sec: 1.07x faster                                                   |
| pprint_safe_repr           | 776 ms                                                 | 725 ms: 1.07x faster                                                     |
| docutils                   | 2.77 sec                                               | 2.59 sec: 1.07x faster                                                   |
| mako                       | 11.9 ms                                                | 11.2 ms: 1.06x faster                                                    |
| richards                   | 45.8 ms                                                | 43.1 ms: 1.06x faster                                                    |
| logging_silent             | 104 ns                                                 | 98.2 ns: 1.06x faster                                                    |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                     |
| generators                 | 31.2 ms                                                | 29.5 ms: 1.06x faster                                                    |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                     |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.80 ms: 1.05x faster                                                    |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.05x faster                                                   |
| sympy_expand               | 478 ms                                                 | 455 ms: 1.05x faster                                                     |
| xml_etree_generate         | 89.2 ms                                                | 85.1 ms: 1.05x faster                                                    |
| richards_super             | 51.5 ms                                                | 49.4 ms: 1.04x faster                                                    |
| regex_dna                  | 212 ms                                                 | 204 ms: 1.04x faster                                                     |
| pickle_pure_python         | 324 us                                                 | 312 us: 1.04x faster                                                     |
| xml_etree_process          | 61.7 ms                                                | 59.9 ms: 1.03x faster                                                    |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.02x faster                                                     |
| sqlite_synth               | 2.83 us                                                | 2.79 us: 1.02x faster                                                    |
| nbody                      | 97.0 ms                                                | 95.5 ms: 1.02x faster                                                    |
| regex_v8                   | 23.1 ms                                                | 22.8 ms: 1.01x faster                                                    |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                     |
| coroutines                 | 23.2 ms                                                | 23.3 ms: 1.01x slower                                                    |
| json_loads                 | 28.5 us                                                | 29.2 us: 1.03x slower                                                    |
| bench_thread_pool          | 842 us                                                 | 878 us: 1.04x slower                                                     |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                                     |
| telco                      | 7.10 ms                                                | 7.70 ms: 1.08x slower                                                    |
| json_dumps                 | 10.4 ms                                                | 11.6 ms: 1.11x slower                                                    |
| python_startup_no_site     | 6.94 ms                                                | 8.21 ms: 1.18x slower                                                    |
| coverage                   | 72.7 ms                                                | 86.3 ms: 1.19x slower                                                    |
| gc_traversal               | 3.79 ms                                                | 4.64 ms: 1.22x slower                                                    |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                    |
| create_gc_cycles           | 1.48 ms                                                | 2.45 ms: 1.66x slower                                                    |
| bench_mp_pool              | 24.0 ms                                                | 82.2 ms: 3.42x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.12x faster                                                             |

Benchmark hidden because not significant (2): json, asyncio_websockets
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250408-3.14.0a7+-77f3e29/bm-20250408-linux-x86_64-eendebakpt-list_freelist_plus-3.14.0a7+-77f3e29.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.137x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.10x