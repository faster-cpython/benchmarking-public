# Results vs. 3.12.0

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: linux-x86_64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 271 ms: 1.01x faster                                                  |
| docutils       | 2.77 sec                                               | 2.91 sec: 1.05x slower                                                |
| tornado_http   | 103 ms                                                 | 92.8 ms: 1.11x faster                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 302 ms: 1.49x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 392 ms: 1.47x faster                                                  |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 860 ms: 1.38x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 532 ms: 1.36x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 427 ms: 1.35x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 563 ms: 1.29x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 904 ms: 1.28x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.38x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.6 ms: 1.20x faster                                                 |
| nbody          | 97.0 ms                                                | 81.5 ms: 1.19x faster                                                 |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 134 ms: 1.11x faster                                                  |
| regex_dna      | 212 ms                                                 | 220 ms: 1.04x slower                                                  |
| regex_effbot   | 3.61 ms                                                | 3.76 ms: 1.04x slower                                                 |
| regex_v8       | 23.1 ms                                                | 25.5 ms: 1.10x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.93 sec: 1.21x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 80.7 ms: 1.10x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 56.5 ms: 1.09x faster                                                 |
| pickle_pure_python   | 324 us                                                 | 299 us: 1.08x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 99.1 ms: 1.08x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 214 us: 1.07x faster                                                  |
| json_loads           | 28.5 us                                                | 27.9 us: 1.02x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.16 ms: 1.03x slower                                                 |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.10x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.75 ms: 1.22x faster                                                 |
| django_template | 34.6 ms                                                | 36.3 ms: 1.05x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 302 ms: 1.49x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 392 ms: 1.47x faster                                                  |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 29.0 us: 1.40x faster                                                 |
| deepcopy                   | 371 us                                                 | 269 us: 1.38x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 860 ms: 1.38x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 532 ms: 1.36x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 427 ms: 1.35x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 563 ms: 1.29x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 904 ms: 1.28x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 60.0 ms: 1.25x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.70 us: 1.24x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 66.4 ms: 1.23x faster                                                 |
| scimark_fft                | 382 ms                                                 | 310 ms: 1.23x faster                                                  |
| mako                       | 11.9 ms                                                | 9.75 ms: 1.22x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 1.93 sec: 1.21x faster                                                |
| float                      | 84.7 ms                                                | 70.6 ms: 1.20x faster                                                 |
| nbody                      | 97.0 ms                                                | 81.5 ms: 1.19x faster                                                 |
| pathlib                    | 19.3 ms                                                | 16.3 ms: 1.19x faster                                                 |
| raytrace                   | 312 ms                                                 | 265 ms: 1.18x faster                                                  |
| logging_format             | 7.23 us                                                | 6.14 us: 1.18x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.30 ms: 1.17x faster                                                 |
| chaos                      | 67.0 ms                                                | 57.5 ms: 1.17x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.59 us: 1.16x faster                                                 |
| spectral_norm              | 115 ms                                                 | 100 ms: 1.15x faster                                                  |
| fannkuch                   | 417 ms                                                 | 366 ms: 1.14x faster                                                  |
| richards                   | 45.8 ms                                                | 40.6 ms: 1.13x faster                                                 |
| pyflate                    | 482 ms                                                 | 430 ms: 1.12x faster                                                  |
| richards_super             | 51.5 ms                                                | 46.3 ms: 1.11x faster                                                 |
| regex_compile              | 148 ms                                                 | 134 ms: 1.11x faster                                                  |
| tornado_http               | 103 ms                                                 | 92.8 ms: 1.11x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 80.7 ms: 1.10x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 56.5 ms: 1.09x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 712 ms: 1.09x faster                                                  |
| generators                 | 31.2 ms                                                | 28.7 ms: 1.09x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 299 us: 1.08x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 99.1 ms: 1.08x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.46 sec: 1.07x faster                                                |
| deltablue                  | 3.72 ms                                                | 3.46 ms: 1.07x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 214 us: 1.07x faster                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.07x faster                                                 |
| sqlglot_transpile          | 1.68 ms                                                | 1.59 ms: 1.06x faster                                                 |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.06x faster                                                  |
| mdp                        | 2.63 sec                                               | 2.54 sec: 1.04x faster                                                |
| coroutines                 | 23.2 ms                                                | 22.6 ms: 1.03x faster                                                 |
| json                       | 5.26 ms                                                | 5.13 ms: 1.02x faster                                                 |
| json_loads                 | 28.5 us                                                | 27.9 us: 1.02x faster                                                 |
| bench_thread_pool          | 842 us                                                 | 824 us: 1.02x faster                                                  |
| dask                       | 372 ms                                                 | 365 ms: 1.02x faster                                                  |
| scimark_sor                | 129 ms                                                 | 127 ms: 1.02x faster                                                  |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.01x faster                                                |
| 2to3                       | 274 ms                                                 | 271 ms: 1.01x faster                                                  |
| logging_silent             | 104 ns                                                 | 103 ns: 1.01x faster                                                  |
| sympy_str                  | 300 ms                                                 | 297 ms: 1.01x faster                                                  |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                  |
| gc_traversal               | 3.79 ms                                                | 3.76 ms: 1.01x faster                                                 |
| async_generators           | 463 ms                                                 | 460 ms: 1.01x faster                                                  |
| asyncio_websockets         | 551 ms                                                 | 557 ms: 1.01x slower                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                |
| go                         | 139 ms                                                 | 142 ms: 1.02x slower                                                  |
| hexiom                     | 6.41 ms                                                | 6.54 ms: 1.02x slower                                                 |
| nqueens                    | 83.3 ms                                                | 85.4 ms: 1.03x slower                                                 |
| asyncio_tcp                | 491 ms                                                 | 504 ms: 1.03x slower                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 56.4 ms: 1.03x slower                                                 |
| sqlglot_normalize          | 110 ms                                                 | 114 ms: 1.03x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.16 ms: 1.03x slower                                                 |
| regex_dna                  | 212 ms                                                 | 220 ms: 1.04x slower                                                  |
| sympy_integrate            | 21.4 ms                                                | 22.2 ms: 1.04x slower                                                 |
| regex_effbot               | 3.61 ms                                                | 3.76 ms: 1.04x slower                                                 |
| django_template            | 34.6 ms                                                | 36.3 ms: 1.05x slower                                                 |
| sympy_expand               | 478 ms                                                 | 502 ms: 1.05x slower                                                  |
| docutils                   | 2.77 sec                                               | 2.91 sec: 1.05x slower                                                |
| scimark_lu                 | 118 ms                                                 | 125 ms: 1.06x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 169 us: 1.07x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 25.5 ms: 1.10x slower                                                 |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.10x slower                                                 |
| telco                      | 7.10 ms                                                | 7.93 ms: 1.12x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.76 ms: 1.20x slower                                                 |
| coverage                   | 72.7 ms                                                | 90.5 ms: 1.25x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (3): json_dumps, bench_mp_pool, sympy_sum
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x