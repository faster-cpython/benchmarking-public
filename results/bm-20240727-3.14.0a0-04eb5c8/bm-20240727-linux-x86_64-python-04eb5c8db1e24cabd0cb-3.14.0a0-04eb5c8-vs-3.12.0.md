# Results vs. 3.12.0

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: linux-x86_64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 264 ms: 1.04x faster                                                  |
| docutils       | 2.77 sec                                               | 2.74 sec: 1.01x faster                                                |
| tornado_http   | 103 ms                                                 | 90.9 ms: 1.13x faster                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 299 ms: 1.50x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 391 ms: 1.47x faster                                                  |
| async_tree_none            | 472 ms                                                 | 323 ms: 1.46x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 409 ms: 1.41x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 860 ms: 1.37x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 530 ms: 1.37x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 893 ms: 1.29x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 562 ms: 1.29x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.39x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 89.0 ms: 1.09x faster                                                 |
| float          | 84.7 ms                                                | 78.1 ms: 1.08x faster                                                 |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 131 ms: 1.13x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.67 ms: 1.02x slower                                                 |
| regex_dna      | 212 ms                                                 | 226 ms: 1.06x slower                                                  |
| regex_v8       | 23.1 ms                                                | 24.6 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.03 sec: 1.15x faster                                                |
| unpickle_pure_python | 230 us                                                 | 212 us: 1.08x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 306 us: 1.06x faster                                                  |
| xml_etree_parse      | 159 ms                                                 | 154 ms: 1.03x faster                                                  |
| json_loads           | 28.5 us                                                | 27.6 us: 1.03x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 60.2 ms: 1.03x faster                                                 |
| xml_etree_generate   | 89.2 ms                                                | 87.0 ms: 1.02x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 105 ms: 1.02x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.10 ms: 1.02x slower                                                 |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako           | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 299 ms: 1.50x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 391 ms: 1.47x faster                                                  |
| async_tree_none            | 472 ms                                                 | 323 ms: 1.46x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 409 ms: 1.41x faster                                                  |
| deepcopy                   | 371 us                                                 | 267 us: 1.39x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 29.4 us: 1.38x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 860 ms: 1.37x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 530 ms: 1.37x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 893 ms: 1.29x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 562 ms: 1.29x faster                                                  |
| pathlib                    | 19.3 ms                                                | 15.7 ms: 1.23x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.76 us: 1.21x faster                                                 |
| raytrace                   | 312 ms                                                 | 261 ms: 1.19x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.49 us: 1.18x faster                                                 |
| logging_format             | 7.23 us                                                | 6.17 us: 1.17x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.24 ms: 1.15x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 2.03 sec: 1.15x faster                                                |
| regex_compile              | 148 ms                                                 | 131 ms: 1.13x faster                                                  |
| chaos                      | 67.0 ms                                                | 59.3 ms: 1.13x faster                                                 |
| tornado_http               | 103 ms                                                 | 90.9 ms: 1.13x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 152 ms: 1.11x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 73.6 ms: 1.11x faster                                                 |
| generators                 | 31.2 ms                                                | 28.5 ms: 1.10x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 68.6 ms: 1.09x faster                                                 |
| sympy_str                  | 300 ms                                                 | 274 ms: 1.09x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.62 ms: 1.09x faster                                                 |
| nbody                      | 97.0 ms                                                | 89.0 ms: 1.09x faster                                                 |
| scimark_fft                | 382 ms                                                 | 351 ms: 1.09x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 212 us: 1.08x faster                                                  |
| float                      | 84.7 ms                                                | 78.1 ms: 1.08x faster                                                 |
| sympy_integrate            | 21.4 ms                                                | 19.8 ms: 1.08x faster                                                 |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                 |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.08x faster                                                 |
| bench_thread_pool          | 842 us                                                 | 789 us: 1.07x faster                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.07x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 306 us: 1.06x faster                                                  |
| async_generators           | 463 ms                                                 | 437 ms: 1.06x faster                                                  |
| dask                       | 372 ms                                                 | 355 ms: 1.05x faster                                                  |
| nqueens                    | 83.3 ms                                                | 79.8 ms: 1.04x faster                                                 |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.04x faster                                                  |
| mdp                        | 2.63 sec                                               | 2.52 sec: 1.04x faster                                                |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                  |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.04x faster                                                |
| 2to3                       | 274 ms                                                 | 264 ms: 1.04x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 748 ms: 1.04x faster                                                  |
| sqlglot_normalize          | 110 ms                                                 | 106 ms: 1.04x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 154 ms: 1.03x faster                                                  |
| hexiom                     | 6.41 ms                                                | 6.22 ms: 1.03x faster                                                 |
| sympy_expand               | 478 ms                                                 | 464 ms: 1.03x faster                                                  |
| json_loads                 | 28.5 us                                                | 27.6 us: 1.03x faster                                                 |
| fannkuch                   | 417 ms                                                 | 405 ms: 1.03x faster                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 53.2 ms: 1.03x faster                                                 |
| scimark_sor                | 129 ms                                                 | 126 ms: 1.03x faster                                                  |
| pyflate                    | 482 ms                                                 | 470 ms: 1.03x faster                                                  |
| coroutines                 | 23.2 ms                                                | 22.6 ms: 1.03x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 60.2 ms: 1.03x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 87.0 ms: 1.02x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.54 sec: 1.02x faster                                                |
| xml_etree_iterparse        | 107 ms                                                 | 105 ms: 1.02x faster                                                  |
| json                       | 5.26 ms                                                | 5.17 ms: 1.02x faster                                                 |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.01x faster                                                  |
| gc_traversal               | 3.79 ms                                                | 3.75 ms: 1.01x faster                                                 |
| docutils                   | 2.77 sec                                               | 2.74 sec: 1.01x faster                                                |
| asyncio_tcp                | 491 ms                                                 | 487 ms: 1.01x faster                                                  |
| logging_silent             | 104 ns                                                 | 104 ns: 1.00x faster                                                  |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x slower                                                  |
| richards_super             | 51.5 ms                                                | 51.8 ms: 1.01x slower                                                 |
| asyncio_websockets         | 551 ms                                                 | 560 ms: 1.02x slower                                                  |
| regex_effbot               | 3.61 ms                                                | 3.67 ms: 1.02x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 7.10 ms: 1.02x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                                  |
| regex_dna                  | 212 ms                                                 | 226 ms: 1.06x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 24.6 ms: 1.07x slower                                                 |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| telco                      | 7.10 ms                                                | 8.10 ms: 1.14x slower                                                 |
| coverage                   | 72.7 ms                                                | 85.4 ms: 1.17x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.74 ms: 1.18x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (6): go, django_template, json_dumps, bench_mp_pool, asyncio_tcp_ssl, richards
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.98x