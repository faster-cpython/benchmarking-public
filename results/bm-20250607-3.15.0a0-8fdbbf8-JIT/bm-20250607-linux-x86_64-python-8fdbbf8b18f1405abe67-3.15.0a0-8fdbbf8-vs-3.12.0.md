# Results vs. 3.12.0

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: linux-x86_64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.044x slower
- HPT reliability: 76.73%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 297 ms: 1.08x slower                                                  |
| docutils       | 2.77 sec                                               | 2.92 sec: 1.06x slower                                                |
| Geometric mean | (ref)                                                  | 1.07x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 655 ms: 1.76x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 690 ms: 1.71x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 343 ms: 1.68x faster                                                  |
| async_tree_none            | 472 ms                                                 | 285 ms: 1.65x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 350 ms: 1.64x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 276 ms: 1.63x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 595 ms: 1.22x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 600 ms: 1.21x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.55x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 67.9 ms: 1.25x faster                                                 |
| pidigits       | 187 ms                                                 | 203 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.18 ms: 1.13x faster                                                 |
| regex_dna      | 212 ms                                                 | 199 ms: 1.06x faster                                                  |
| regex_compile  | 148 ms                                                 | 144 ms: 1.03x faster                                                  |
| regex_v8       | 23.1 ms                                                | 25.6 ms: 1.11x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.10 sec: 1.11x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 161 ms: 1.01x slower                                                  |
| unpickle_pure_python | 230 us                                                 | 240 us: 1.04x slower                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 112 ms: 1.04x slower                                                  |
| pickle_dict          | 35.5 us                                                | 37.7 us: 1.06x slower                                                 |
| unpickle_list        | 5.29 us                                                | 5.86 us: 1.11x slower                                                 |
| xml_etree_process    | 61.7 ms                                                | 68.8 ms: 1.11x slower                                                 |
| xml_etree_generate   | 89.2 ms                                                | 102 ms: 1.14x slower                                                  |
| pickle_pure_python   | 324 us                                                 | 377 us: 1.16x slower                                                  |
| json_loads           | 28.5 us                                                | 33.5 us: 1.17x slower                                                 |
| pickle_list          | 5.08 us                                                | 6.04 us: 1.19x slower                                                 |
| unpickle             | 15.9 us                                                | 19.0 us: 1.20x slower                                                 |
| json_dumps           | 10.4 ms                                                | 13.3 ms: 1.28x slower                                                 |
| pickle               | 11.6 us                                                | 15.0 us: 1.29x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.12x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.39 ms: 1.06x slower                                                 |
| python_startup         | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.21x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 13.2 ms: 1.11x slower                                                 |
| django_template | 34.6 ms                                                | 40.6 ms: 1.17x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.14x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.48 sec: 1.78x faster                                                |
| async_tree_io              | 1.16 sec                                               | 655 ms: 1.76x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 690 ms: 1.71x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 343 ms: 1.68x faster                                                  |
| async_tree_none            | 472 ms                                                 | 285 ms: 1.65x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 350 ms: 1.64x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 276 ms: 1.63x faster                                                  |
| float                      | 84.7 ms                                                | 67.9 ms: 1.25x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 595 ms: 1.22x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 600 ms: 1.21x faster                                                  |
| deepcopy                   | 371 us                                                 | 312 us: 1.19x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 34.4 us: 1.18x faster                                                 |
| richards                   | 45.8 ms                                                | 39.7 ms: 1.15x faster                                                 |
| regex_effbot               | 3.61 ms                                                | 3.18 ms: 1.13x faster                                                 |
| richards_super             | 51.5 ms                                                | 46.3 ms: 1.11x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 2.10 sec: 1.11x faster                                                |
| scimark_fft                | 382 ms                                                 | 351 ms: 1.09x faster                                                  |
| go                         | 139 ms                                                 | 129 ms: 1.08x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.45 ms: 1.08x faster                                                 |
| pathlib                    | 19.3 ms                                                | 18.1 ms: 1.07x faster                                                 |
| comprehensions             | 21.8 us                                                | 20.4 us: 1.07x faster                                                 |
| regex_dna                  | 212 ms                                                 | 199 ms: 1.06x faster                                                  |
| pyflate                    | 482 ms                                                 | 455 ms: 1.06x faster                                                  |
| async_generators           | 463 ms                                                 | 437 ms: 1.06x faster                                                  |
| spectral_norm              | 115 ms                                                 | 110 ms: 1.04x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 72.7 ms: 1.03x faster                                                 |
| regex_compile              | 148 ms                                                 | 144 ms: 1.03x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 66.9 ms: 1.02x faster                                                 |
| asyncio_tcp                | 491 ms                                                 | 484 ms: 1.01x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 168 ms: 1.00x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 3.38 us: 1.01x slower                                                 |
| xml_etree_parse            | 159 ms                                                 | 161 ms: 1.01x slower                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.02x slower                                                |
| raytrace                   | 312 ms                                                 | 323 ms: 1.03x slower                                                  |
| scimark_sor                | 129 ms                                                 | 134 ms: 1.04x slower                                                  |
| meteor_contest             | 112 ms                                                 | 117 ms: 1.04x slower                                                  |
| unpickle_pure_python       | 230 us                                                 | 240 us: 1.04x slower                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 112 ms: 1.04x slower                                                  |
| sympy_str                  | 300 ms                                                 | 314 ms: 1.05x slower                                                  |
| chaos                      | 67.0 ms                                                | 70.2 ms: 1.05x slower                                                 |
| crypto_pyaes               | 81.9 ms                                                | 86.3 ms: 1.05x slower                                                 |
| docutils                   | 2.77 sec                                               | 2.92 sec: 1.06x slower                                                |
| pickle_dict                | 35.5 us                                                | 37.7 us: 1.06x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 7.39 ms: 1.06x slower                                                 |
| generators                 | 31.2 ms                                                | 33.5 ms: 1.07x slower                                                 |
| pycparser                  | 1.18 sec                                               | 1.27 sec: 1.08x slower                                                |
| hexiom                     | 6.41 ms                                                | 6.94 ms: 1.08x slower                                                 |
| pidigits                   | 187 ms                                                 | 203 ms: 1.08x slower                                                  |
| 2to3                       | 274 ms                                                 | 297 ms: 1.08x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 25.6 ms: 1.11x slower                                                 |
| unpickle_list              | 5.29 us                                                | 5.86 us: 1.11x slower                                                 |
| sqlite_synth               | 2.83 us                                                | 3.14 us: 1.11x slower                                                 |
| mako                       | 11.9 ms                                                | 13.2 ms: 1.11x slower                                                 |
| xml_etree_process          | 61.7 ms                                                | 68.8 ms: 1.11x slower                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.64 ms: 1.12x slower                                                 |
| scimark_lu                 | 118 ms                                                 | 134 ms: 1.14x slower                                                  |
| xml_etree_generate         | 89.2 ms                                                | 102 ms: 1.14x slower                                                  |
| json                       | 5.26 ms                                                | 6.02 ms: 1.14x slower                                                 |
| sympy_expand               | 478 ms                                                 | 548 ms: 1.15x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 965 us: 1.15x slower                                                  |
| logging_simple             | 6.46 us                                                | 7.45 us: 1.15x slower                                                 |
| fannkuch                   | 417 ms                                                 | 482 ms: 1.16x slower                                                  |
| logging_format             | 7.23 us                                                | 8.38 us: 1.16x slower                                                 |
| pickle_pure_python         | 324 us                                                 | 377 us: 1.16x slower                                                  |
| coroutines                 | 23.2 ms                                                | 27.0 ms: 1.17x slower                                                 |
| django_template            | 34.6 ms                                                | 40.6 ms: 1.17x slower                                                 |
| json_loads                 | 28.5 us                                                | 33.5 us: 1.17x slower                                                 |
| pickle_list                | 5.08 us                                                | 6.04 us: 1.19x slower                                                 |
| unpickle                   | 15.9 us                                                | 19.0 us: 1.20x slower                                                 |
| nqueens                    | 83.3 ms                                                | 100 ms: 1.20x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 200 us: 1.26x slower                                                  |
| telco                      | 7.10 ms                                                | 9.07 ms: 1.28x slower                                                 |
| json_dumps                 | 10.4 ms                                                | 13.3 ms: 1.28x slower                                                 |
| pickle                     | 11.6 us                                                | 15.0 us: 1.29x slower                                                 |
| unpack_sequence            | 54.0 ns                                                | 70.2 ns: 1.30x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 5.11 ms: 1.35x slower                                                 |
| pprint_safe_repr           | 776 ms                                                 | 1.06 sec: 1.37x slower                                                |
| pprint_pformat             | 1.57 sec                                               | 2.15 sec: 1.37x slower                                                |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 2.62 ms: 1.78x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 104 ms: 4.33x slower                                                  |
| logging_silent             | 104 ns                                                 | 633 ns: 6.06x slower                                                  |
| coverage                   | 72.7 ms                                                | 518 ms: 7.13x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.08x slower                                                          |

Benchmark hidden because not significant (3): nbody, sympy_integrate, asyncio_websockets
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.044x slower

# HPT report

- Reliability score: 76.73% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.15x