# Results vs. 3.12.0

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: linux-x86_64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.059x slower
- HPT reliability: 96.50%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 292 ms: 1.06x slower                                                  |
| docutils       | 2.77 sec                                               | 2.86 sec: 1.03x slower                                                |
| Geometric mean | (ref)                                                  | 1.05x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 666 ms: 1.74x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 696 ms: 1.70x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 349 ms: 1.65x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 353 ms: 1.63x faster                                                  |
| async_tree_none            | 472 ms                                                 | 291 ms: 1.62x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 281 ms: 1.60x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 589 ms: 1.23x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 596 ms: 1.22x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.54x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 75.0 ms: 1.13x faster                                                 |
| nbody          | 97.0 ms                                                | 106 ms: 1.09x slower                                                  |
| pidigits       | 187 ms                                                 | 207 ms: 1.11x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.01 ms: 1.20x faster                                                 |
| regex_dna      | 212 ms                                                 | 203 ms: 1.04x faster                                                  |
| regex_compile  | 148 ms                                                 | 144 ms: 1.03x faster                                                  |
| regex_v8       | 23.1 ms                                                | 24.2 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.24 sec: 1.04x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 162 ms: 1.01x slower                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 111 ms: 1.04x slower                                                  |
| pickle_dict          | 35.5 us                                                | 37.9 us: 1.07x slower                                                 |
| unpickle_pure_python | 230 us                                                 | 256 us: 1.11x slower                                                  |
| unpickle_list        | 5.29 us                                                | 5.96 us: 1.13x slower                                                 |
| pickle_pure_python   | 324 us                                                 | 375 us: 1.16x slower                                                  |
| json_loads           | 28.5 us                                                | 33.6 us: 1.18x slower                                                 |
| pickle_list          | 5.08 us                                                | 6.05 us: 1.19x slower                                                 |
| unpickle             | 15.9 us                                                | 19.0 us: 1.20x slower                                                 |
| xml_etree_process    | 61.7 ms                                                | 75.3 ms: 1.22x slower                                                 |
| xml_etree_generate   | 89.2 ms                                                | 110 ms: 1.23x slower                                                  |
| pickle               | 11.6 us                                                | 14.9 us: 1.28x slower                                                 |
| json_dumps           | 10.4 ms                                                | 13.4 ms: 1.29x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.14x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.35 ms: 1.06x slower                                                 |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.21x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 13.8 ms: 1.16x slower                                                 |
| django_template | 34.6 ms                                                | 40.2 ms: 1.16x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.16x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.48 sec: 1.78x faster                                                |
| async_tree_io              | 1.16 sec                                               | 666 ms: 1.74x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 696 ms: 1.70x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 349 ms: 1.65x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 353 ms: 1.63x faster                                                  |
| async_tree_none            | 472 ms                                                 | 291 ms: 1.62x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 281 ms: 1.60x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 589 ms: 1.23x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 596 ms: 1.22x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.01 ms: 1.20x faster                                                 |
| deepcopy_memo              | 40.7 us                                                | 34.3 us: 1.19x faster                                                 |
| deepcopy                   | 371 us                                                 | 314 us: 1.18x faster                                                  |
| go                         | 139 ms                                                 | 119 ms: 1.18x faster                                                  |
| comprehensions             | 21.8 us                                                | 19.2 us: 1.14x faster                                                 |
| float                      | 84.7 ms                                                | 75.0 ms: 1.13x faster                                                 |
| async_generators           | 463 ms                                                 | 419 ms: 1.10x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 64.3 ms: 1.07x faster                                                 |
| pathlib                    | 19.3 ms                                                | 18.2 ms: 1.06x faster                                                 |
| regex_dna                  | 212 ms                                                 | 203 ms: 1.04x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 2.24 sec: 1.04x faster                                                |
| unpack_sequence            | 54.0 ns                                                | 52.1 ns: 1.04x faster                                                 |
| pyflate                    | 482 ms                                                 | 469 ms: 1.03x faster                                                  |
| regex_compile              | 148 ms                                                 | 144 ms: 1.03x faster                                                  |
| asyncio_tcp                | 491 ms                                                 | 480 ms: 1.02x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 21.0 ms: 1.02x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 167 ms: 1.01x faster                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                |
| xml_etree_parse            | 159 ms                                                 | 162 ms: 1.01x slower                                                  |
| spectral_norm              | 115 ms                                                 | 118 ms: 1.03x slower                                                  |
| raytrace                   | 312 ms                                                 | 322 ms: 1.03x slower                                                  |
| docutils                   | 2.77 sec                                               | 2.86 sec: 1.03x slower                                                |
| sympy_str                  | 300 ms                                                 | 310 ms: 1.03x slower                                                  |
| deltablue                  | 3.72 ms                                                | 3.84 ms: 1.03x slower                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 111 ms: 1.04x slower                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 78.2 ms: 1.04x slower                                                 |
| chaos                      | 67.0 ms                                                | 69.9 ms: 1.04x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 24.2 ms: 1.05x slower                                                 |
| hexiom                     | 6.41 ms                                                | 6.71 ms: 1.05x slower                                                 |
| generators                 | 31.2 ms                                                | 32.9 ms: 1.05x slower                                                 |
| meteor_contest             | 112 ms                                                 | 119 ms: 1.05x slower                                                  |
| scimark_sor                | 129 ms                                                 | 137 ms: 1.06x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.35 ms: 1.06x slower                                                 |
| crypto_pyaes               | 81.9 ms                                                | 86.9 ms: 1.06x slower                                                 |
| 2to3                       | 274 ms                                                 | 292 ms: 1.06x slower                                                  |
| pickle_dict                | 35.5 us                                                | 37.9 us: 1.07x slower                                                 |
| pycparser                  | 1.18 sec                                               | 1.26 sec: 1.07x slower                                                |
| scimark_fft                | 382 ms                                                 | 412 ms: 1.08x slower                                                  |
| nbody                      | 97.0 ms                                                | 106 ms: 1.09x slower                                                  |
| pidigits                   | 187 ms                                                 | 207 ms: 1.11x slower                                                  |
| unpickle_pure_python       | 230 us                                                 | 256 us: 1.11x slower                                                  |
| sympy_expand               | 478 ms                                                 | 534 ms: 1.12x slower                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.68 ms: 1.12x slower                                                 |
| unpickle_list              | 5.29 us                                                | 5.96 us: 1.13x slower                                                 |
| scimark_lu                 | 118 ms                                                 | 133 ms: 1.13x slower                                                  |
| sqlite_synth               | 2.83 us                                                | 3.21 us: 1.13x slower                                                 |
| bench_thread_pool          | 842 us                                                 | 954 us: 1.13x slower                                                  |
| pickle_pure_python         | 324 us                                                 | 375 us: 1.16x slower                                                  |
| mako                       | 11.9 ms                                                | 13.8 ms: 1.16x slower                                                 |
| django_template            | 34.6 ms                                                | 40.2 ms: 1.16x slower                                                 |
| json                       | 5.26 ms                                                | 6.11 ms: 1.16x slower                                                 |
| logging_simple             | 6.46 us                                                | 7.51 us: 1.16x slower                                                 |
| coroutines                 | 23.2 ms                                                | 27.0 ms: 1.17x slower                                                 |
| logging_format             | 7.23 us                                                | 8.46 us: 1.17x slower                                                 |
| fannkuch                   | 417 ms                                                 | 491 ms: 1.18x slower                                                  |
| richards                   | 45.8 ms                                                | 54.0 ms: 1.18x slower                                                 |
| json_loads                 | 28.5 us                                                | 33.6 us: 1.18x slower                                                 |
| richards_super             | 51.5 ms                                                | 61.4 ms: 1.19x slower                                                 |
| pickle_list                | 5.08 us                                                | 6.05 us: 1.19x slower                                                 |
| unpickle                   | 15.9 us                                                | 19.0 us: 1.20x slower                                                 |
| nqueens                    | 83.3 ms                                                | 100 ms: 1.20x slower                                                  |
| xml_etree_process          | 61.7 ms                                                | 75.3 ms: 1.22x slower                                                 |
| xml_etree_generate         | 89.2 ms                                                | 110 ms: 1.23x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 197 us: 1.25x slower                                                  |
| pickle                     | 11.6 us                                                | 14.9 us: 1.28x slower                                                 |
| json_dumps                 | 10.4 ms                                                | 13.4 ms: 1.29x slower                                                 |
| pprint_safe_repr           | 776 ms                                                 | 1.00 sec: 1.30x slower                                                |
| pprint_pformat             | 1.57 sec                                               | 2.05 sec: 1.31x slower                                                |
| gc_traversal               | 3.79 ms                                                | 5.13 ms: 1.35x slower                                                 |
| telco                      | 7.10 ms                                                | 9.64 ms: 1.36x slower                                                 |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 2.61 ms: 1.77x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 104 ms: 4.34x slower                                                  |
| logging_silent             | 104 ns                                                 | 625 ns: 5.99x slower                                                  |
| coverage                   | 72.7 ms                                                | 519 ms: 7.14x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.09x slower                                                          |

Benchmark hidden because not significant (2): deepcopy_reduce, asyncio_websockets
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.059x slower

# HPT report

- Reliability score: 96.50% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.13x