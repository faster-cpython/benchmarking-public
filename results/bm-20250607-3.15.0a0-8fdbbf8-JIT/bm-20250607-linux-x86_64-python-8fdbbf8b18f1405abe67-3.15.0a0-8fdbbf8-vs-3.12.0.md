# Results vs. 3.12.0

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: linux-x86_64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.122x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 259 ms: 1.06x faster                                                  |
| docutils       | 2.77 sec                                               | 2.65 sec: 1.04x faster                                                |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 599 ms: 1.93x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 613 ms: 1.93x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                  |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.80x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.80x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 482 ms: 1.51x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 489 ms: 1.48x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.76x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 64.1 ms: 1.32x faster                                                 |
| nbody          | 97.0 ms                                                | 91.9 ms: 1.06x faster                                                 |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.36 ms: 1.07x faster                                                 |
| regex_v8       | 23.1 ms                                                | 23.3 ms: 1.01x slower                                                 |
| regex_dna      | 212 ms                                                 | 215 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.91 sec: 1.22x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 203 us: 1.13x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 80.8 ms: 1.10x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 56.0 ms: 1.10x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 97.8 ms: 1.09x faster                                                 |
| pickle_pure_python   | 324 us                                                 | 322 us: 1.01x faster                                                  |
| json_loads           | 28.5 us                                                | 28.8 us: 1.01x slower                                                 |
| json_dumps           | 10.4 ms                                                | 11.0 ms: 1.06x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.94 ms: 1.00x faster                                                 |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.27x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.7 ms: 1.11x faster                                                 |
| django_template | 34.6 ms                                                | 32.4 ms: 1.07x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.24 sec: 2.11x faster                                                |
| async_tree_io              | 1.16 sec                                               | 599 ms: 1.93x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 613 ms: 1.93x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                  |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.80x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.80x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 482 ms: 1.51x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 489 ms: 1.48x faster                                                  |
| deepcopy                   | 371 us                                                 | 256 us: 1.45x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 29.9 us: 1.36x faster                                                 |
| richards                   | 45.8 ms                                                | 34.1 ms: 1.35x faster                                                 |
| float                      | 84.7 ms                                                | 64.1 ms: 1.32x faster                                                 |
| richards_super             | 51.5 ms                                                | 39.8 ms: 1.29x faster                                                 |
| comprehensions             | 21.8 us                                                | 17.2 us: 1.27x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.66 us: 1.26x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 1.91 sec: 1.22x faster                                                |
| deltablue                  | 3.72 ms                                                | 3.13 ms: 1.19x faster                                                 |
| pyflate                    | 482 ms                                                 | 417 ms: 1.16x faster                                                  |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 59.4 ms: 1.15x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                                  |
| scimark_fft                | 382 ms                                                 | 336 ms: 1.14x faster                                                  |
| raytrace                   | 312 ms                                                 | 276 ms: 1.13x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 203 us: 1.13x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.13x faster                                                  |
| pathlib                    | 19.3 ms                                                | 17.3 ms: 1.12x faster                                                 |
| mako                       | 11.9 ms                                                | 10.7 ms: 1.11x faster                                                 |
| go                         | 139 ms                                                 | 125 ms: 1.11x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 19.3 ms: 1.11x faster                                                 |
| sympy_str                  | 300 ms                                                 | 271 ms: 1.11x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 80.8 ms: 1.10x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 56.0 ms: 1.10x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 68.1 ms: 1.10x faster                                                 |
| spectral_norm              | 115 ms                                                 | 105 ms: 1.09x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 97.8 ms: 1.09x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 75.7 ms: 1.08x faster                                                 |
| chaos                      | 67.0 ms                                                | 62.3 ms: 1.07x faster                                                 |
| regex_effbot               | 3.61 ms                                                | 3.36 ms: 1.07x faster                                                 |
| django_template            | 34.6 ms                                                | 32.4 ms: 1.07x faster                                                 |
| logging_format             | 7.23 us                                                | 6.77 us: 1.07x faster                                                 |
| scimark_sor                | 129 ms                                                 | 121 ms: 1.06x faster                                                  |
| async_generators           | 463 ms                                                 | 437 ms: 1.06x faster                                                  |
| 2to3                       | 274 ms                                                 | 259 ms: 1.06x faster                                                  |
| nbody                      | 97.0 ms                                                | 91.9 ms: 1.06x faster                                                 |
| logging_simple             | 6.46 us                                                | 6.14 us: 1.05x faster                                                 |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.65 sec: 1.04x faster                                                |
| sympy_expand               | 478 ms                                                 | 465 ms: 1.03x faster                                                  |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.01x faster                                                |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                                 |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 322 us: 1.01x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.03 ms: 1.00x faster                                                 |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                  |
| python_startup_no_site     | 6.94 ms                                                | 6.94 ms: 1.00x faster                                                 |
| nqueens                    | 83.3 ms                                                | 83.7 ms: 1.00x slower                                                 |
| generators                 | 31.2 ms                                                | 31.5 ms: 1.01x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 23.3 ms: 1.01x slower                                                 |
| json                       | 5.26 ms                                                | 5.30 ms: 1.01x slower                                                 |
| hexiom                     | 6.41 ms                                                | 6.47 ms: 1.01x slower                                                 |
| json_loads                 | 28.5 us                                                | 28.8 us: 1.01x slower                                                 |
| regex_dna                  | 212 ms                                                 | 215 ms: 1.01x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 11.0 ms: 1.06x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 169 us: 1.07x slower                                                  |
| pprint_safe_repr           | 776 ms                                                 | 830 ms: 1.07x slower                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.69 sec: 1.08x slower                                                |
| coroutines                 | 23.2 ms                                                | 25.5 ms: 1.10x slower                                                 |
| telco                      | 7.10 ms                                                | 7.82 ms: 1.10x slower                                                 |
| coverage                   | 72.7 ms                                                | 87.5 ms: 1.20x slower                                                 |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.27x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 4.94 ms: 1.30x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 2.58 ms: 1.75x slower                                                 |
| logging_silent             | 104 ns                                                 | 479 ns: 4.59x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                          |

Benchmark hidden because not significant (2): asyncio_websockets, fannkuch
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.122x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.15x