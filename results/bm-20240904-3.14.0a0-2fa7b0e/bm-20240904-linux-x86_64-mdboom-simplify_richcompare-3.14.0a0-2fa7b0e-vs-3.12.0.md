# Results vs. 3.12.0

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: 2fa7b0e
- commit date: 2024-09-04
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 257 ms: 1.07x faster                                                  |
| docutils       | 2.77 sec                                               | 2.66 sec: 1.04x faster                                                |
| tornado_http   | 103 ms                                                 | 90.7 ms: 1.13x faster                                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization     | 578 ms                                                 | 394 ms: 1.47x faster                                                  |
| async_tree_none            | 472 ms                                                 | 327 ms: 1.44x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 313 ms: 1.44x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 405 ms: 1.42x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 549 ms: 1.32x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 908 ms: 1.30x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 567 ms: 1.28x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 937 ms: 1.23x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.36x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 86.0 ms: 1.13x faster                                                 |
| float          | 84.7 ms                                                | 77.5 ms: 1.09x faster                                                 |
| pidigits       | 187 ms                                                 | 186 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 131 ms: 1.13x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.77 ms: 1.04x slower                                                 |
| regex_dna      | 212 ms                                                 | 222 ms: 1.05x slower                                                  |
| regex_v8       | 23.1 ms                                                | 26.1 ms: 1.13x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.10 sec: 1.11x faster                                                |
| unpickle_pure_python | 230 us                                                 | 210 us: 1.09x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 301 us: 1.08x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 59.4 ms: 1.04x faster                                                 |
| xml_etree_generate   | 89.2 ms                                                | 86.0 ms: 1.04x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 155 ms: 1.03x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 106 ms: 1.01x faster                                                  |
| json_loads           | 28.5 us                                                | 28.7 us: 1.01x slower                                                 |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                 |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.2 ms: 1.06x faster                                                 |
| django_template | 34.6 ms                                                | 34.0 ms: 1.02x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization     | 578 ms                                                 | 394 ms: 1.47x faster                                                  |
| async_tree_none            | 472 ms                                                 | 327 ms: 1.44x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 313 ms: 1.44x faster                                                  |
| deepcopy                   | 371 us                                                 | 260 us: 1.43x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 405 ms: 1.42x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 30.3 us: 1.34x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 549 ms: 1.32x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.30x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 908 ms: 1.30x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 567 ms: 1.28x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.65 us: 1.26x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 937 ms: 1.23x faster                                                  |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                                 |
| raytrace                   | 312 ms                                                 | 263 ms: 1.19x faster                                                  |
| logging_format             | 7.23 us                                                | 6.11 us: 1.18x faster                                                 |
| go                         | 139 ms                                                 | 119 ms: 1.18x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.51 us: 1.17x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.21 ms: 1.16x faster                                                 |
| chaos                      | 67.0 ms                                                | 58.7 ms: 1.14x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                                  |
| regex_compile              | 148 ms                                                 | 131 ms: 1.13x faster                                                  |
| tornado_http               | 103 ms                                                 | 90.7 ms: 1.13x faster                                                 |
| generators                 | 31.2 ms                                                | 27.7 ms: 1.13x faster                                                 |
| nbody                      | 97.0 ms                                                | 86.0 ms: 1.13x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 73.6 ms: 1.11x faster                                                 |
| sympy_str                  | 300 ms                                                 | 270 ms: 1.11x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 2.10 sec: 1.11x faster                                                |
| unpickle_pure_python       | 230 us                                                 | 210 us: 1.09x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 19.6 ms: 1.09x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 68.7 ms: 1.09x faster                                                 |
| float                      | 84.7 ms                                                | 77.5 ms: 1.09x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 717 ms: 1.08x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 301 us: 1.08x faster                                                  |
| bench_thread_pool          | 842 us                                                 | 787 us: 1.07x faster                                                  |
| 2to3                       | 274 ms                                                 | 257 ms: 1.07x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.74 ms: 1.07x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.07x faster                                                |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.06x faster                                                 |
| spectral_norm              | 115 ms                                                 | 108 ms: 1.06x faster                                                  |
| scimark_fft                | 382 ms                                                 | 360 ms: 1.06x faster                                                  |
| mako                       | 11.9 ms                                                | 11.2 ms: 1.06x faster                                                 |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.06x faster                                                 |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                  |
| async_generators           | 463 ms                                                 | 445 ms: 1.04x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.66 sec: 1.04x faster                                                |
| xml_etree_process          | 61.7 ms                                                | 59.4 ms: 1.04x faster                                                 |
| sympy_expand               | 478 ms                                                 | 461 ms: 1.04x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 86.0 ms: 1.04x faster                                                 |
| fannkuch                   | 417 ms                                                 | 403 ms: 1.03x faster                                                  |
| nqueens                    | 83.3 ms                                                | 80.7 ms: 1.03x faster                                                 |
| logging_silent             | 104 ns                                                 | 101 ns: 1.03x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 155 ms: 1.03x faster                                                  |
| scimark_sor                | 129 ms                                                 | 126 ms: 1.03x faster                                                  |
| pyflate                    | 482 ms                                                 | 471 ms: 1.02x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.02x faster                                                  |
| asyncio_tcp                | 491 ms                                                 | 479 ms: 1.02x faster                                                  |
| coroutines                 | 23.2 ms                                                | 22.7 ms: 1.02x faster                                                 |
| hexiom                     | 6.41 ms                                                | 6.29 ms: 1.02x faster                                                 |
| sqlglot_optimize           | 54.8 ms                                                | 53.8 ms: 1.02x faster                                                 |
| gc_traversal               | 3.79 ms                                                | 3.72 ms: 1.02x faster                                                 |
| django_template            | 34.6 ms                                                | 34.0 ms: 1.02x faster                                                 |
| sqlglot_normalize          | 110 ms                                                 | 109 ms: 1.01x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 106 ms: 1.01x faster                                                  |
| pidigits                   | 187 ms                                                 | 186 ms: 1.00x faster                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x slower                                                |
| mdp                        | 2.63 sec                                               | 2.64 sec: 1.00x slower                                                |
| richards_super             | 51.5 ms                                                | 51.8 ms: 1.01x slower                                                 |
| json_loads                 | 28.5 us                                                | 28.7 us: 1.01x slower                                                 |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                 |
| json                       | 5.26 ms                                                | 5.32 ms: 1.01x slower                                                 |
| asyncio_websockets         | 551 ms                                                 | 559 ms: 1.01x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 161 us: 1.02x slower                                                  |
| regex_effbot               | 3.61 ms                                                | 3.77 ms: 1.04x slower                                                 |
| regex_dna                  | 212 ms                                                 | 222 ms: 1.05x slower                                                  |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 26.1 ms: 1.13x slower                                                 |
| telco                      | 7.10 ms                                                | 8.34 ms: 1.18x slower                                                 |
| coverage                   | 72.7 ms                                                | 85.7 ms: 1.18x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.76 ms: 1.19x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (3): richards, bench_mp_pool, pycparser
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240904-3.14.0a0-2fa7b0e/bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.98x