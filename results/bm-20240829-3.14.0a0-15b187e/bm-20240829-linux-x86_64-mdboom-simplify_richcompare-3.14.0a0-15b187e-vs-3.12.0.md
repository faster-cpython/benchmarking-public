# Results vs. 3.12.0

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: 15b187e
- commit date: 2024-08-29
- overall geometric mean: 1.087x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 256 ms: 1.07x faster                                                  |
| docutils       | 2.77 sec                                               | 2.67 sec: 1.04x faster                                                |
| tornado_http   | 103 ms                                                 | 89.9 ms: 1.14x faster                                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization     | 578 ms                                                 | 389 ms: 1.49x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 306 ms: 1.47x faster                                                  |
| async_tree_none            | 472 ms                                                 | 322 ms: 1.47x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 399 ms: 1.44x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 538 ms: 1.35x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 887 ms: 1.33x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 557 ms: 1.30x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 920 ms: 1.26x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.39x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 78.3 ms: 1.08x faster                                                 |
| nbody          | 97.0 ms                                                | 89.8 ms: 1.08x faster                                                 |
| pidigits       | 187 ms                                                 | 186 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.77 ms: 1.04x slower                                                 |
| regex_dna      | 212 ms                                                 | 224 ms: 1.06x slower                                                  |
| regex_v8       | 23.1 ms                                                | 26.1 ms: 1.13x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.08 sec: 1.12x faster                                                |
| pickle_pure_python   | 324 us                                                 | 301 us: 1.08x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 214 us: 1.07x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 84.6 ms: 1.05x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 58.7 ms: 1.05x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 154 ms: 1.03x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 104 ms: 1.03x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (2): json_dumps, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                 |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.5 ms: 1.04x faster                                                 |
| django_template | 34.6 ms                                                | 33.8 ms: 1.02x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization     | 578 ms                                                 | 389 ms: 1.49x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 306 ms: 1.47x faster                                                  |
| async_tree_none            | 472 ms                                                 | 322 ms: 1.47x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 399 ms: 1.44x faster                                                  |
| deepcopy                   | 371 us                                                 | 260 us: 1.43x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 30.1 us: 1.35x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 538 ms: 1.35x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 887 ms: 1.33x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 557 ms: 1.30x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 920 ms: 1.26x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.67 us: 1.25x faster                                                 |
| pathlib                    | 19.3 ms                                                | 15.7 ms: 1.23x faster                                                 |
| raytrace                   | 312 ms                                                 | 262 ms: 1.19x faster                                                  |
| go                         | 139 ms                                                 | 119 ms: 1.18x faster                                                  |
| logging_format             | 7.23 us                                                | 6.18 us: 1.17x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.55 us: 1.16x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.20 ms: 1.16x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 146 ms: 1.15x faster                                                  |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 71.4 ms: 1.15x faster                                                 |
| chaos                      | 67.0 ms                                                | 58.6 ms: 1.14x faster                                                 |
| tornado_http               | 103 ms                                                 | 89.9 ms: 1.14x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 66.7 ms: 1.13x faster                                                 |
| generators                 | 31.2 ms                                                | 27.8 ms: 1.12x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 2.08 sec: 1.12x faster                                                |
| sympy_str                  | 300 ms                                                 | 269 ms: 1.11x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 19.4 ms: 1.10x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 716 ms: 1.08x faster                                                  |
| float                      | 84.7 ms                                                | 78.3 ms: 1.08x faster                                                 |
| nbody                      | 97.0 ms                                                | 89.8 ms: 1.08x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 301 us: 1.08x faster                                                  |
| bench_thread_pool          | 842 us                                                 | 784 us: 1.07x faster                                                  |
| 2to3                       | 274 ms                                                 | 256 ms: 1.07x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 214 us: 1.07x faster                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.07x faster                                                |
| sqlglot_transpile          | 1.68 ms                                                | 1.57 ms: 1.07x faster                                                 |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.06x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 84.6 ms: 1.05x faster                                                 |
| async_generators           | 463 ms                                                 | 439 ms: 1.05x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 58.7 ms: 1.05x faster                                                 |
| mdp                        | 2.63 sec                                               | 2.50 sec: 1.05x faster                                                |
| sympy_expand               | 478 ms                                                 | 455 ms: 1.05x faster                                                  |
| hexiom                     | 6.41 ms                                                | 6.11 ms: 1.05x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.83 ms: 1.05x faster                                                 |
| docutils                   | 2.77 sec                                               | 2.67 sec: 1.04x faster                                                |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.04x faster                                                  |
| asyncio_tcp                | 491 ms                                                 | 473 ms: 1.04x faster                                                  |
| mako                       | 11.9 ms                                                | 11.5 ms: 1.04x faster                                                 |
| nqueens                    | 83.3 ms                                                | 80.4 ms: 1.04x faster                                                 |
| fannkuch                   | 417 ms                                                 | 403 ms: 1.04x faster                                                  |
| scimark_fft                | 382 ms                                                 | 369 ms: 1.04x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 154 ms: 1.03x faster                                                  |
| logging_silent             | 104 ns                                                 | 101 ns: 1.03x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 104 ms: 1.03x faster                                                  |
| django_template            | 34.6 ms                                                | 33.8 ms: 1.02x faster                                                 |
| gc_traversal               | 3.79 ms                                                | 3.71 ms: 1.02x faster                                                 |
| scimark_sor                | 129 ms                                                 | 126 ms: 1.02x faster                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 53.7 ms: 1.02x faster                                                 |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                                  |
| pyflate                    | 482 ms                                                 | 474 ms: 1.02x faster                                                  |
| sqlglot_normalize          | 110 ms                                                 | 108 ms: 1.02x faster                                                  |
| pidigits                   | 187 ms                                                 | 186 ms: 1.00x faster                                                  |
| richards_super             | 51.5 ms                                                | 51.9 ms: 1.01x slower                                                 |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                                  |
| json                       | 5.26 ms                                                | 5.33 ms: 1.01x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                 |
| coroutines                 | 23.2 ms                                                | 23.8 ms: 1.03x slower                                                 |
| regex_effbot               | 3.61 ms                                                | 3.77 ms: 1.04x slower                                                 |
| regex_dna                  | 212 ms                                                 | 224 ms: 1.06x slower                                                  |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 26.1 ms: 1.13x slower                                                 |
| telco                      | 7.10 ms                                                | 8.32 ms: 1.17x slower                                                 |
| coverage                   | 72.7 ms                                                | 86.2 ms: 1.19x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.75 ms: 1.19x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (7): pycparser, asyncio_tcp_ssl, richards, bench_mp_pool, json_dumps, json_loads, typing_runtime_protocols
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240829-3.14.0a0-15b187e/bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.087x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.98x