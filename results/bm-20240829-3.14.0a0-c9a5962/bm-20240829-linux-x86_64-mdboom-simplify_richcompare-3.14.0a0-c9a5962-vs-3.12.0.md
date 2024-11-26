# Results vs. 3.12.0

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: c9a5962
- commit date: 2024-08-29
- overall geometric mean: 1.094x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 253 ms: 1.09x faster                                                  |
| docutils       | 2.77 sec                                               | 2.64 sec: 1.05x faster                                                |
| tornado_http   | 103 ms                                                 | 89.5 ms: 1.15x faster                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization     | 578 ms                                                 | 389 ms: 1.49x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 307 ms: 1.46x faster                                                  |
| async_tree_none            | 472 ms                                                 | 322 ms: 1.46x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 400 ms: 1.44x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 541 ms: 1.34x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 892 ms: 1.33x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 561 ms: 1.29x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 926 ms: 1.25x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.38x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 85.3 ms: 1.14x faster                                                 |
| float          | 84.7 ms                                                | 76.5 ms: 1.11x faster                                                 |
| pidigits       | 187 ms                                                 | 186 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.54 ms: 1.02x faster                                                 |
| regex_dna      | 212 ms                                                 | 218 ms: 1.03x slower                                                  |
| regex_v8       | 23.1 ms                                                | 24.3 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.05 sec: 1.14x faster                                                |
| unpickle_pure_python | 230 us                                                 | 212 us: 1.08x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 301 us: 1.08x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 58.8 ms: 1.05x faster                                                 |
| xml_etree_generate   | 89.2 ms                                                | 85.2 ms: 1.05x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 156 ms: 1.02x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 104 ms: 1.02x faster                                                  |
| json_loads           | 28.5 us                                                | 28.6 us: 1.00x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.04 ms: 1.01x slower                                                 |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.09x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.4 ms: 1.04x faster                                                 |
| django_template | 34.6 ms                                                | 33.7 ms: 1.03x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization     | 578 ms                                                 | 389 ms: 1.49x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 307 ms: 1.46x faster                                                  |
| async_tree_none            | 472 ms                                                 | 322 ms: 1.46x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 400 ms: 1.44x faster                                                  |
| deepcopy                   | 371 us                                                 | 260 us: 1.43x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 29.6 us: 1.37x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 541 ms: 1.34x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 892 ms: 1.33x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 561 ms: 1.29x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.66 us: 1.26x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 926 ms: 1.25x faster                                                  |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                                 |
| raytrace                   | 312 ms                                                 | 261 ms: 1.20x faster                                                  |
| go                         | 139 ms                                                 | 117 ms: 1.19x faster                                                  |
| logging_format             | 7.23 us                                                | 6.10 us: 1.18x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.58 us: 1.16x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.22 ms: 1.16x faster                                                 |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                  |
| chaos                      | 67.0 ms                                                | 58.2 ms: 1.15x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                                  |
| tornado_http               | 103 ms                                                 | 89.5 ms: 1.15x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 2.05 sec: 1.14x faster                                                |
| nbody                      | 97.0 ms                                                | 85.3 ms: 1.14x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 66.4 ms: 1.13x faster                                                 |
| generators                 | 31.2 ms                                                | 27.7 ms: 1.13x faster                                                 |
| sympy_str                  | 300 ms                                                 | 267 ms: 1.12x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 72.9 ms: 1.12x faster                                                 |
| float                      | 84.7 ms                                                | 76.5 ms: 1.11x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 702 ms: 1.10x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 19.5 ms: 1.10x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.44 sec: 1.09x faster                                                |
| 2to3                       | 274 ms                                                 | 253 ms: 1.09x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 212 us: 1.08x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 301 us: 1.08x faster                                                  |
| bench_thread_pool          | 842 us                                                 | 783 us: 1.07x faster                                                  |
| gc_traversal               | 3.79 ms                                                | 3.54 ms: 1.07x faster                                                 |
| sqlglot_transpile          | 1.68 ms                                                | 1.57 ms: 1.07x faster                                                 |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.07x faster                                                 |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.77 ms: 1.06x faster                                                 |
| sympy_expand               | 478 ms                                                 | 452 ms: 1.06x faster                                                  |
| async_generators           | 463 ms                                                 | 439 ms: 1.05x faster                                                  |
| mdp                        | 2.63 sec                                               | 2.50 sec: 1.05x faster                                                |
| scimark_fft                | 382 ms                                                 | 363 ms: 1.05x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 58.8 ms: 1.05x faster                                                 |
| docutils                   | 2.77 sec                                               | 2.64 sec: 1.05x faster                                                |
| pyflate                    | 482 ms                                                 | 461 ms: 1.05x faster                                                  |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.05x faster                                                |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.05x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 85.2 ms: 1.05x faster                                                 |
| scimark_sor                | 129 ms                                                 | 124 ms: 1.04x faster                                                  |
| nqueens                    | 83.3 ms                                                | 79.8 ms: 1.04x faster                                                 |
| logging_silent             | 104 ns                                                 | 100 ns: 1.04x faster                                                  |
| mako                       | 11.9 ms                                                | 11.4 ms: 1.04x faster                                                 |
| fannkuch                   | 417 ms                                                 | 402 ms: 1.04x faster                                                  |
| hexiom                     | 6.41 ms                                                | 6.19 ms: 1.04x faster                                                 |
| django_template            | 34.6 ms                                                | 33.7 ms: 1.03x faster                                                 |
| sqlglot_optimize           | 54.8 ms                                                | 53.5 ms: 1.03x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 156 ms: 1.02x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 104 ms: 1.02x faster                                                  |
| spectral_norm              | 115 ms                                                 | 112 ms: 1.02x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.54 ms: 1.02x faster                                                 |
| sqlglot_normalize          | 110 ms                                                 | 108 ms: 1.02x faster                                                  |
| asyncio_tcp                | 491 ms                                                 | 486 ms: 1.01x faster                                                  |
| pidigits                   | 187 ms                                                 | 186 ms: 1.00x faster                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x slower                                                |
| json_loads                 | 28.5 us                                                | 28.6 us: 1.00x slower                                                 |
| json                       | 5.26 ms                                                | 5.31 ms: 1.01x slower                                                 |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.04 ms: 1.01x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 161 us: 1.02x slower                                                  |
| regex_dna                  | 212 ms                                                 | 218 ms: 1.03x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 24.3 ms: 1.05x slower                                                 |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.09x slower                                                 |
| telco                      | 7.10 ms                                                | 8.34 ms: 1.17x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.73 ms: 1.17x slower                                                 |
| coverage                   | 72.7 ms                                                | 85.7 ms: 1.18x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (5): bench_mp_pool, json_dumps, richards, richards_super, coroutines
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240829-3.14.0a0-c9a5962/bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.094x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 0.98x