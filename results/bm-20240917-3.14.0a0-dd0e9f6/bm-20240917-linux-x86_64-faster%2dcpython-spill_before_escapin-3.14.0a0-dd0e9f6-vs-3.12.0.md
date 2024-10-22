# Results vs. 3.12.0

- fork: faster-cpython
- ref: spill_before_escapin
- machine: linux-x86_64
- commit hash: dd0e9f6
- commit date: 2024-09-17
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240917-linux-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-dd0e9f6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 256 ms: 1.07x faster                                                            |
| docutils       | 2.77 sec                                               | 2.67 sec: 1.04x faster                                                          |
| tornado_http   | 103 ms                                                 | 90.2 ms: 1.14x faster                                                           |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240917-linux-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-dd0e9f6 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 315 ms: 1.50x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 391 ms: 1.47x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 394 ms: 1.47x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 313 ms: 1.44x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 878 ms: 1.35x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 874 ms: 1.32x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 551 ms: 1.32x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 560 ms: 1.30x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.39x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240917-linux-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-dd0e9f6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 86.2 ms: 1.13x faster                                                           |
| float          | 84.7 ms                                                | 77.0 ms: 1.10x faster                                                           |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240917-linux-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-dd0e9f6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                            |
| regex_dna      | 212 ms                                                 | 228 ms: 1.08x slower                                                            |
| regex_effbot   | 3.61 ms                                                | 3.89 ms: 1.08x slower                                                           |
| regex_v8       | 23.1 ms                                                | 25.3 ms: 1.09x slower                                                           |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240917-linux-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-dd0e9f6 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.08 sec: 1.12x faster                                                          |
| pickle_pure_python   | 324 us                                                 | 299 us: 1.08x faster                                                            |
| unpickle             | 15.9 us                                                | 14.7 us: 1.08x faster                                                           |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.07x faster                                                            |
| pickle_list          | 5.08 us                                                | 4.78 us: 1.06x faster                                                           |
| json_loads           | 28.5 us                                                | 26.8 us: 1.06x faster                                                           |
| xml_etree_generate   | 89.2 ms                                                | 84.8 ms: 1.05x faster                                                           |
| xml_etree_process    | 61.7 ms                                                | 58.8 ms: 1.05x faster                                                           |
| pickle_dict          | 35.5 us                                                | 34.1 us: 1.04x faster                                                           |
| pickle               | 11.6 us                                                | 11.3 us: 1.03x faster                                                           |
| xml_etree_parse      | 159 ms                                                 | 155 ms: 1.03x faster                                                            |
| xml_etree_iterparse  | 107 ms                                                 | 104 ms: 1.03x faster                                                            |
| unpickle_list        | 5.29 us                                                | 5.17 us: 1.02x faster                                                           |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                           |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240917-linux-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-dd0e9f6 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.98 ms: 1.01x slower                                                           |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240917-linux-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-dd0e9f6 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.5 ms: 1.04x faster                                                           |
| django_template | 34.6 ms                                                | 34.1 ms: 1.02x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240917-linux-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-dd0e9f6 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 315 ms: 1.50x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 391 ms: 1.47x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 394 ms: 1.47x faster                                                            |
| deepcopy                   | 371 us                                                 | 256 us: 1.45x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 313 ms: 1.44x faster                                                            |
| deepcopy_memo              | 40.7 us                                                | 30.1 us: 1.35x faster                                                           |
| async_tree_io_tg           | 1.18 sec                                               | 878 ms: 1.35x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 874 ms: 1.32x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 551 ms: 1.32x faster                                                            |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.31x faster                                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 560 ms: 1.30x faster                                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.66 us: 1.26x faster                                                           |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                                           |
| raytrace                   | 312 ms                                                 | 265 ms: 1.18x faster                                                            |
| logging_format             | 7.23 us                                                | 6.25 us: 1.16x faster                                                           |
| unpack_sequence            | 54.0 ns                                                | 46.7 ns: 1.16x faster                                                           |
| go                         | 139 ms                                                 | 121 ms: 1.15x faster                                                            |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                                            |
| logging_simple             | 6.46 us                                                | 5.61 us: 1.15x faster                                                           |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                            |
| tornado_http               | 103 ms                                                 | 90.2 ms: 1.14x faster                                                           |
| deltablue                  | 3.72 ms                                                | 3.28 ms: 1.13x faster                                                           |
| generators                 | 31.2 ms                                                | 27.6 ms: 1.13x faster                                                           |
| crypto_pyaes               | 81.9 ms                                                | 72.4 ms: 1.13x faster                                                           |
| chaos                      | 67.0 ms                                                | 59.3 ms: 1.13x faster                                                           |
| nbody                      | 97.0 ms                                                | 86.2 ms: 1.13x faster                                                           |
| tomli_loads                | 2.33 sec                                               | 2.08 sec: 1.12x faster                                                          |
| sympy_str                  | 300 ms                                                 | 269 ms: 1.11x faster                                                            |
| scimark_monte_carlo        | 75.1 ms                                                | 67.8 ms: 1.11x faster                                                           |
| float                      | 84.7 ms                                                | 77.0 ms: 1.10x faster                                                           |
| sympy_integrate            | 21.4 ms                                                | 19.6 ms: 1.09x faster                                                           |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.65 ms: 1.09x faster                                                           |
| pickle_pure_python         | 324 us                                                 | 299 us: 1.08x faster                                                            |
| pprint_safe_repr           | 776 ms                                                 | 719 ms: 1.08x faster                                                            |
| async_generators           | 463 ms                                                 | 430 ms: 1.08x faster                                                            |
| unpickle                   | 15.9 us                                                | 14.7 us: 1.08x faster                                                           |
| 2to3                       | 274 ms                                                 | 256 ms: 1.07x faster                                                            |
| json                       | 5.26 ms                                                | 4.91 ms: 1.07x faster                                                           |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.07x faster                                                           |
| bench_thread_pool          | 842 us                                                 | 789 us: 1.07x faster                                                            |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.07x faster                                                            |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.07x faster                                                           |
| pickle_list                | 5.08 us                                                | 4.78 us: 1.06x faster                                                           |
| json_loads                 | 28.5 us                                                | 26.8 us: 1.06x faster                                                           |
| dulwich_log                | 68.5 ms                                                | 64.6 ms: 1.06x faster                                                           |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                                          |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                            |
| xml_etree_generate         | 89.2 ms                                                | 84.8 ms: 1.05x faster                                                           |
| xml_etree_process          | 61.7 ms                                                | 58.8 ms: 1.05x faster                                                           |
| fannkuch                   | 417 ms                                                 | 397 ms: 1.05x faster                                                            |
| pyflate                    | 482 ms                                                 | 461 ms: 1.05x faster                                                            |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.05x faster                                                            |
| mdp                        | 2.63 sec                                               | 2.52 sec: 1.04x faster                                                          |
| scimark_sor                | 129 ms                                                 | 124 ms: 1.04x faster                                                            |
| scimark_fft                | 382 ms                                                 | 366 ms: 1.04x faster                                                            |
| sympy_expand               | 478 ms                                                 | 458 ms: 1.04x faster                                                            |
| nqueens                    | 83.3 ms                                                | 79.9 ms: 1.04x faster                                                           |
| pickle_dict                | 35.5 us                                                | 34.1 us: 1.04x faster                                                           |
| docutils                   | 2.77 sec                                               | 2.67 sec: 1.04x faster                                                          |
| mako                       | 11.9 ms                                                | 11.5 ms: 1.04x faster                                                           |
| spectral_norm              | 115 ms                                                 | 111 ms: 1.03x faster                                                            |
| pickle                     | 11.6 us                                                | 11.3 us: 1.03x faster                                                           |
| hexiom                     | 6.41 ms                                                | 6.23 ms: 1.03x faster                                                           |
| xml_etree_parse            | 159 ms                                                 | 155 ms: 1.03x faster                                                            |
| gc_traversal               | 3.79 ms                                                | 3.69 ms: 1.03x faster                                                           |
| logging_silent             | 104 ns                                                 | 102 ns: 1.03x faster                                                            |
| xml_etree_iterparse        | 107 ms                                                 | 104 ms: 1.03x faster                                                            |
| sqlglot_optimize           | 54.8 ms                                                | 53.4 ms: 1.03x faster                                                           |
| unpickle_list              | 5.29 us                                                | 5.17 us: 1.02x faster                                                           |
| sqlglot_normalize          | 110 ms                                                 | 108 ms: 1.02x faster                                                            |
| asyncio_tcp                | 491 ms                                                 | 482 ms: 1.02x faster                                                            |
| django_template            | 34.6 ms                                                | 34.1 ms: 1.02x faster                                                           |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                           |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                            |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x slower                                                          |
| python_startup_no_site     | 6.94 ms                                                | 6.98 ms: 1.01x slower                                                           |
| sqlite_synth               | 2.83 us                                                | 2.86 us: 1.01x slower                                                           |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                                            |
| coroutines                 | 23.2 ms                                                | 23.7 ms: 1.02x slower                                                           |
| richards                   | 45.8 ms                                                | 46.9 ms: 1.02x slower                                                           |
| richards_super             | 51.5 ms                                                | 52.9 ms: 1.03x slower                                                           |
| regex_dna                  | 212 ms                                                 | 228 ms: 1.08x slower                                                            |
| regex_effbot               | 3.61 ms                                                | 3.89 ms: 1.08x slower                                                           |
| regex_v8                   | 23.1 ms                                                | 25.3 ms: 1.09x slower                                                           |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 1.72 ms: 1.17x slower                                                           |
| coverage                   | 72.7 ms                                                | 85.5 ms: 1.18x slower                                                           |
| telco                      | 7.10 ms                                                | 8.36 ms: 1.18x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                    |

Benchmark hidden because not significant (3): bench_mp_pool, pycparser, typing_runtime_protocols
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240917-3.14.0a0-dd0e9f6/bm-20240917-linux-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-dd0e9f6.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 0.97x