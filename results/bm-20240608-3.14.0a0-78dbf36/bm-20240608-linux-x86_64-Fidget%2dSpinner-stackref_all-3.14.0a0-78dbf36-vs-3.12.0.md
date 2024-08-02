# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: stackref_all
- machine: linux-x86_64
- commit hash: 78dbf36
- commit date: 2024-06-08
- overall geometric mean: 1.04x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-78dbf36 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 268 ms: 1.02x faster                                                    |
| tornado_http   | 103 ms                                                 | 93.8 ms: 1.09x faster                                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                                            |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-78dbf36 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 336 ms: 1.34x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 439 ms: 1.31x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 919 ms: 1.29x faster                                                    |
| async_tree_none            | 472 ms                                                 | 374 ms: 1.26x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 468 ms: 1.24x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 595 ms: 1.22x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 954 ms: 1.21x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 631 ms: 1.15x faster                                                    |
| Geometric mean             | (ref)                                                  | 1.25x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-78dbf36 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 86.3 ms: 1.12x faster                                                   |
| float          | 84.7 ms                                                | 77.9 ms: 1.09x faster                                                   |
| pidigits       | 187 ms                                                 | 190 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                  | 1.06x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-78dbf36 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 132 ms: 1.12x faster                                                    |
| regex_effbot   | 3.61 ms                                                | 3.80 ms: 1.05x slower                                                   |
| regex_dna      | 212 ms                                                 | 233 ms: 1.10x slower                                                    |
| regex_v8       | 23.1 ms                                                | 26.0 ms: 1.12x slower                                                   |
| Geometric mean | (ref)                                                  | 1.04x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-78dbf36 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 324 us                                                 | 299 us: 1.08x faster                                                    |
| tomli_loads          | 2.33 sec                                               | 2.15 sec: 1.08x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.06x faster                                                    |
| unpickle             | 15.9 us                                                | 15.1 us: 1.05x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 85.6 ms: 1.04x faster                                                   |
| xml_etree_process    | 61.7 ms                                                | 59.6 ms: 1.04x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 156 ms: 1.02x faster                                                    |
| pickle_dict          | 35.5 us                                                | 35.2 us: 1.01x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 106 ms: 1.01x faster                                                    |
| json_loads           | 28.5 us                                                | 28.6 us: 1.00x slower                                                   |
| pickle               | 11.6 us                                                | 11.8 us: 1.01x slower                                                   |
| pickle_list          | 5.08 us                                                | 5.18 us: 1.02x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                            |

Benchmark hidden because not significant (2): json_dumps, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-78dbf36 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.12 ms: 1.03x slower                                                   |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-78dbf36 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.2 ms: 1.07x faster                                                   |
| django_template | 34.6 ms                                                | 34.2 ms: 1.01x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-78dbf36 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 336 ms: 1.34x faster                                                    |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 439 ms: 1.31x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 919 ms: 1.29x faster                                                    |
| async_tree_none            | 472 ms                                                 | 374 ms: 1.26x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 468 ms: 1.24x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 595 ms: 1.22x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 954 ms: 1.21x faster                                                    |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.21x faster                                                   |
| raytrace                   | 312 ms                                                 | 264 ms: 1.18x faster                                                    |
| logging_format             | 7.23 us                                                | 6.24 us: 1.16x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 631 ms: 1.15x faster                                                    |
| logging_simple             | 6.46 us                                                | 5.62 us: 1.15x faster                                                   |
| deltablue                  | 3.72 ms                                                | 3.29 ms: 1.13x faster                                                   |
| chaos                      | 67.0 ms                                                | 59.3 ms: 1.13x faster                                                   |
| nbody                      | 97.0 ms                                                | 86.3 ms: 1.12x faster                                                   |
| regex_compile              | 148 ms                                                 | 132 ms: 1.12x faster                                                    |
| scimark_monte_carlo        | 75.1 ms                                                | 67.7 ms: 1.11x faster                                                   |
| sympy_sum                  | 169 ms                                                 | 154 ms: 1.09x faster                                                    |
| tornado_http               | 103 ms                                                 | 93.8 ms: 1.09x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 75.2 ms: 1.09x faster                                                   |
| float                      | 84.7 ms                                                | 77.9 ms: 1.09x faster                                                   |
| pickle_pure_python         | 324 us                                                 | 299 us: 1.08x faster                                                    |
| tomli_loads                | 2.33 sec                                               | 2.15 sec: 1.08x faster                                                  |
| sympy_str                  | 300 ms                                                 | 277 ms: 1.08x faster                                                    |
| generators                 | 31.2 ms                                                | 29.0 ms: 1.08x faster                                                   |
| mako                       | 11.9 ms                                                | 11.2 ms: 1.07x faster                                                   |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.06x faster                                                    |
| sympy_integrate            | 21.4 ms                                                | 20.3 ms: 1.06x faster                                                   |
| dulwich_log                | 68.5 ms                                                | 65.1 ms: 1.05x faster                                                   |
| nqueens                    | 83.3 ms                                                | 79.3 ms: 1.05x faster                                                   |
| async_generators           | 463 ms                                                 | 441 ms: 1.05x faster                                                    |
| fannkuch                   | 417 ms                                                 | 398 ms: 1.05x faster                                                    |
| unpickle                   | 15.9 us                                                | 15.1 us: 1.05x faster                                                   |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                    |
| sqlglot_transpile          | 1.68 ms                                                | 1.61 ms: 1.04x faster                                                   |
| pprint_safe_repr           | 776 ms                                                 | 744 ms: 1.04x faster                                                    |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 85.6 ms: 1.04x faster                                                   |
| xml_etree_process          | 61.7 ms                                                | 59.6 ms: 1.04x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 39.3 us: 1.04x faster                                                   |
| hexiom                     | 6.41 ms                                                | 6.19 ms: 1.04x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                | 3.24 us: 1.03x faster                                                   |
| mdp                        | 2.63 sec                                               | 2.56 sec: 1.03x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.92 ms: 1.03x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.53 sec: 1.03x faster                                                  |
| deepcopy                   | 371 us                                                 | 362 us: 1.03x faster                                                    |
| scimark_sor                | 129 ms                                                 | 126 ms: 1.02x faster                                                    |
| 2to3                       | 274 ms                                                 | 268 ms: 1.02x faster                                                    |
| xml_etree_parse            | 159 ms                                                 | 156 ms: 1.02x faster                                                    |
| pyflate                    | 482 ms                                                 | 473 ms: 1.02x faster                                                    |
| sympy_expand               | 478 ms                                                 | 471 ms: 1.01x faster                                                    |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                    |
| bench_thread_pool          | 842 us                                                 | 833 us: 1.01x faster                                                    |
| django_template            | 34.6 ms                                                | 34.2 ms: 1.01x faster                                                   |
| pickle_dict                | 35.5 us                                                | 35.2 us: 1.01x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 106 ms: 1.01x faster                                                    |
| sqlglot_normalize          | 110 ms                                                 | 109 ms: 1.01x faster                                                    |
| bench_mp_pool              | 24.0 ms                                                | 23.8 ms: 1.01x faster                                                   |
| json_loads                 | 28.5 us                                                | 28.6 us: 1.00x slower                                                   |
| logging_silent             | 104 ns                                                 | 105 ns: 1.01x slower                                                    |
| pickle                     | 11.6 us                                                | 11.8 us: 1.01x slower                                                   |
| go                         | 139 ms                                                 | 142 ms: 1.02x slower                                                    |
| pidigits                   | 187 ms                                                 | 190 ms: 1.02x slower                                                    |
| pycparser                  | 1.18 sec                                               | 1.20 sec: 1.02x slower                                                  |
| json                       | 5.26 ms                                                | 5.36 ms: 1.02x slower                                                   |
| pickle_list                | 5.08 us                                                | 5.18 us: 1.02x slower                                                   |
| asyncio_tcp                | 491 ms                                                 | 501 ms: 1.02x slower                                                    |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.83 sec: 1.03x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.12 ms: 1.03x slower                                                   |
| asyncio_websockets         | 551 ms                                                 | 567 ms: 1.03x slower                                                    |
| richards                   | 45.8 ms                                                | 47.4 ms: 1.03x slower                                                   |
| sqlite_synth               | 2.83 us                                                | 2.93 us: 1.03x slower                                                   |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                    |
| richards_super             | 51.5 ms                                                | 54.0 ms: 1.05x slower                                                   |
| gc_traversal               | 3.79 ms                                                | 3.98 ms: 1.05x slower                                                   |
| regex_effbot               | 3.61 ms                                                | 3.80 ms: 1.05x slower                                                   |
| regex_dna                  | 212 ms                                                 | 233 ms: 1.10x slower                                                    |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                   |
| regex_v8                   | 23.1 ms                                                | 26.0 ms: 1.12x slower                                                   |
| telco                      | 7.10 ms                                                | 8.35 ms: 1.18x slower                                                   |
| create_gc_cycles           | 1.48 ms                                                | 1.78 ms: 1.21x slower                                                   |
| coverage                   | 72.7 ms                                                | 92.1 ms: 1.27x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                            |

Benchmark hidden because not significant (8): scimark_fft, dask, spectral_norm, coroutines, json_dumps, sqlglot_optimize, docutils, unpickle_list
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240608-3.14.0a0-78dbf36/bm-20240608-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-78dbf36.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.97x