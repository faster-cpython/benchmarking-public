# Results vs. 3.12.0

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: linux-x86_64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.102x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-linux-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 253 ms: 1.08x faster                                                  |
| docutils       | 2.77 sec                                               | 2.63 sec: 1.05x faster                                                |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-linux-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 585 ms: 1.97x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 616 ms: 1.92x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 308 ms: 1.88x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 309 ms: 1.86x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 245 ms: 1.84x faster                                                  |
| async_tree_none            | 472 ms                                                 | 257 ms: 1.84x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 496 ms: 1.46x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 505 ms: 1.44x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.76x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-linux-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 67.5 ms: 1.26x faster                                                 |
| nbody          | 97.0 ms                                                | 86.4 ms: 1.12x faster                                                 |
| pidigits       | 187 ms                                                 | 210 ms: 1.12x slower                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-linux-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 124 ms: 1.20x faster                                                  |
| regex_dna      | 212 ms                                                 | 206 ms: 1.03x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.54 ms: 1.02x faster                                                 |
| regex_v8       | 23.1 ms                                                | 25.0 ms: 1.08x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-linux-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                |
| unpickle_list        | 5.29 us                                                | 4.67 us: 1.13x faster                                                 |
| unpickle             | 15.9 us                                                | 14.4 us: 1.10x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 212 us: 1.09x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 308 us: 1.05x faster                                                  |
| pickle_dict          | 35.5 us                                                | 34.4 us: 1.03x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 60.1 ms: 1.03x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 104 ms: 1.03x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 88.6 ms: 1.01x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 164 ms: 1.03x slower                                                  |
| pickle_list          | 5.08 us                                                | 5.31 us: 1.05x slower                                                 |
| json_loads           | 28.5 us                                                | 29.8 us: 1.05x slower                                                 |
| pickle               | 11.6 us                                                | 13.2 us: 1.14x slower                                                 |
| json_dumps           | 10.4 ms                                                | 12.9 ms: 1.24x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-linux-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.92 ms: 1.00x faster                                                 |
| python_startup         | 9.55 ms                                                | 12.1 ms: 1.27x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-linux-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.4 ms: 1.10x faster                                                 |
| mako            | 11.9 ms                                                | 12.2 ms: 1.03x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-linux-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.22 sec: 2.16x faster                                                |
| async_tree_io              | 1.16 sec                                               | 585 ms: 1.97x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 616 ms: 1.92x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 308 ms: 1.88x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 309 ms: 1.86x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 245 ms: 1.84x faster                                                  |
| async_tree_none            | 472 ms                                                 | 257 ms: 1.84x faster                                                  |
| deepcopy                   | 371 us                                                 | 246 us: 1.51x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 496 ms: 1.46x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 505 ms: 1.44x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 28.8 us: 1.42x faster                                                 |
| comprehensions             | 21.8 us                                                | 16.0 us: 1.36x faster                                                 |
| go                         | 139 ms                                                 | 107 ms: 1.30x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.60 us: 1.29x faster                                                 |
| pathlib                    | 19.3 ms                                                | 15.4 ms: 1.26x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 59.7 ms: 1.26x faster                                                 |
| float                      | 84.7 ms                                                | 67.5 ms: 1.26x faster                                                 |
| raytrace                   | 312 ms                                                 | 249 ms: 1.25x faster                                                  |
| scimark_fft                | 382 ms                                                 | 305 ms: 1.25x faster                                                  |
| deltablue                  | 3.72 ms                                                | 2.98 ms: 1.25x faster                                                 |
| chaos                      | 67.0 ms                                                | 53.9 ms: 1.24x faster                                                 |
| spectral_norm              | 115 ms                                                 | 94.5 ms: 1.22x faster                                                 |
| scimark_sor                | 129 ms                                                 | 108 ms: 1.20x faster                                                  |
| regex_compile              | 148 ms                                                 | 124 ms: 1.20x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                |
| dulwich_log                | 68.5 ms                                                | 58.0 ms: 1.18x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.29 ms: 1.18x faster                                                 |
| async_generators           | 463 ms                                                 | 394 ms: 1.17x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 18.4 ms: 1.17x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 146 ms: 1.16x faster                                                  |
| sympy_str                  | 300 ms                                                 | 262 ms: 1.14x faster                                                  |
| pyflate                    | 482 ms                                                 | 423 ms: 1.14x faster                                                  |
| unpickle_list              | 5.29 us                                                | 4.67 us: 1.13x faster                                                 |
| nbody                      | 97.0 ms                                                | 86.4 ms: 1.12x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 73.1 ms: 1.12x faster                                                 |
| richards                   | 45.8 ms                                                | 41.0 ms: 1.12x faster                                                 |
| hexiom                     | 6.41 ms                                                | 5.76 ms: 1.11x faster                                                 |
| scimark_lu                 | 118 ms                                                 | 106 ms: 1.11x faster                                                  |
| unpickle                   | 15.9 us                                                | 14.4 us: 1.10x faster                                                 |
| django_template            | 34.6 ms                                                | 31.4 ms: 1.10x faster                                                 |
| richards_super             | 51.5 ms                                                | 47.3 ms: 1.09x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 212 us: 1.09x faster                                                  |
| 2to3                       | 274 ms                                                 | 253 ms: 1.08x faster                                                  |
| generators                 | 31.2 ms                                                | 28.9 ms: 1.08x faster                                                 |
| sympy_expand               | 478 ms                                                 | 446 ms: 1.07x faster                                                  |
| logging_simple             | 6.46 us                                                | 6.04 us: 1.07x faster                                                 |
| nqueens                    | 83.3 ms                                                | 78.1 ms: 1.07x faster                                                 |
| logging_format             | 7.23 us                                                | 6.79 us: 1.06x faster                                                 |
| unpack_sequence            | 54.0 ns                                                | 51.3 ns: 1.05x faster                                                 |
| docutils                   | 2.77 sec                                               | 2.63 sec: 1.05x faster                                                |
| pickle_pure_python         | 324 us                                                 | 308 us: 1.05x faster                                                  |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.04x faster                                                |
| pickle_dict                | 35.5 us                                                | 34.4 us: 1.03x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 751 ms: 1.03x faster                                                  |
| regex_dna                  | 212 ms                                                 | 206 ms: 1.03x faster                                                  |
| sqlite_synth               | 2.83 us                                                | 2.75 us: 1.03x faster                                                 |
| asyncio_tcp                | 491 ms                                                 | 477 ms: 1.03x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 60.1 ms: 1.03x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 104 ms: 1.03x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.54 ms: 1.02x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.54 sec: 1.02x faster                                                |
| fannkuch                   | 417 ms                                                 | 412 ms: 1.01x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 88.6 ms: 1.01x faster                                                 |
| python_startup_no_site     | 6.94 ms                                                | 6.92 ms: 1.00x faster                                                 |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x slower                                                |
| bench_thread_pool          | 842 us                                                 | 852 us: 1.01x slower                                                  |
| json                       | 5.26 ms                                                | 5.32 ms: 1.01x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 160 us: 1.01x slower                                                  |
| meteor_contest             | 112 ms                                                 | 115 ms: 1.02x slower                                                  |
| mako                       | 11.9 ms                                                | 12.2 ms: 1.03x slower                                                 |
| xml_etree_parse            | 159 ms                                                 | 164 ms: 1.03x slower                                                  |
| telco                      | 7.10 ms                                                | 7.33 ms: 1.03x slower                                                 |
| pickle_list                | 5.08 us                                                | 5.31 us: 1.05x slower                                                 |
| json_loads                 | 28.5 us                                                | 29.8 us: 1.05x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 25.0 ms: 1.08x slower                                                 |
| pidigits                   | 187 ms                                                 | 210 ms: 1.12x slower                                                  |
| pickle                     | 11.6 us                                                | 13.2 us: 1.14x slower                                                 |
| json_dumps                 | 10.4 ms                                                | 12.9 ms: 1.24x slower                                                 |
| python_startup             | 9.55 ms                                                | 12.1 ms: 1.27x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 4.88 ms: 1.29x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 2.64 ms: 1.78x slower                                                 |
| dask                       | 372 ms                                                 | 895 ms: 2.41x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 92.5 ms: 3.85x slower                                                 |
| logging_silent             | 104 ns                                                 | 508 ns: 4.87x slower                                                  |
| coverage                   | 72.7 ms                                                | 413 ms: 5.68x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (24) of results/bm-20250510-3.15.0a0-1a87b6e-CLANG/bm-20250510-linux-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.102x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.14x