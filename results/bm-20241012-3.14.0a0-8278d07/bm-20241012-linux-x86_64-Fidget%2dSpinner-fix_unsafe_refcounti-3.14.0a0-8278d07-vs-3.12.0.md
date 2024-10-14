# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: fix_unsafe_refcounti
- machine: linux-x86_64
- commit hash: 8278d07
- commit date: 2024-10-12
- overall geometric mean: 1.07x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 252 ms: 1.09x faster                                                            |
| docutils       | 2.77 sec                                               | 2.63 sec: 1.05x faster                                                          |
| tornado_http   | 103 ms                                                 | 89.9 ms: 1.14x faster                                                           |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization     | 578 ms                                                 | 391 ms: 1.48x faster                                                            |
| async_tree_none            | 472 ms                                                 | 320 ms: 1.47x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 309 ms: 1.45x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 403 ms: 1.43x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 546 ms: 1.33x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 915 ms: 1.29x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 562 ms: 1.29x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 929 ms: 1.24x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.37x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 88.9 ms: 1.09x faster                                                           |
| float          | 84.7 ms                                                | 77.8 ms: 1.09x faster                                                           |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                            |
| regex_dna      | 212 ms                                                 | 217 ms: 1.02x slower                                                            |
| regex_v8       | 23.1 ms                                                | 24.9 ms: 1.08x slower                                                           |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.10 sec: 1.11x faster                                                          |
| unpickle_pure_python | 230 us                                                 | 215 us: 1.07x faster                                                            |
| json_loads           | 28.5 us                                                | 26.8 us: 1.06x faster                                                           |
| pickle_pure_python   | 324 us                                                 | 306 us: 1.06x faster                                                            |
| unpickle             | 15.9 us                                                | 15.2 us: 1.04x faster                                                           |
| xml_etree_generate   | 89.2 ms                                                | 85.5 ms: 1.04x faster                                                           |
| xml_etree_process    | 61.7 ms                                                | 59.4 ms: 1.04x faster                                                           |
| pickle_dict          | 35.5 us                                                | 34.5 us: 1.03x faster                                                           |
| xml_etree_parse      | 159 ms                                                 | 155 ms: 1.03x faster                                                            |
| xml_etree_iterparse  | 107 ms                                                 | 105 ms: 1.02x faster                                                            |
| pickle               | 11.6 us                                                | 11.4 us: 1.02x faster                                                           |
| pickle_list          | 5.08 us                                                | 5.14 us: 1.01x slower                                                           |
| unpickle_list        | 5.29 us                                                | 5.43 us: 1.03x slower                                                           |
| json_dumps           | 10.4 ms                                                | 11.8 ms: 1.14x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.03 ms: 1.01x slower                                                           |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.5 ms: 1.04x faster                                                           |
| django_template | 34.6 ms                                                | 33.8 ms: 1.02x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization     | 578 ms                                                 | 391 ms: 1.48x faster                                                            |
| async_tree_none            | 472 ms                                                 | 320 ms: 1.47x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 309 ms: 1.45x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 403 ms: 1.43x faster                                                            |
| deepcopy                   | 371 us                                                 | 262 us: 1.42x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 546 ms: 1.33x faster                                                            |
| deepcopy_memo              | 40.7 us                                                | 30.7 us: 1.33x faster                                                           |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                           |
| async_tree_io_tg           | 1.18 sec                                               | 915 ms: 1.29x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 562 ms: 1.29x faster                                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.66 us: 1.26x faster                                                           |
| async_tree_io              | 1.16 sec                                               | 929 ms: 1.24x faster                                                            |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                                           |
| raytrace                   | 312 ms                                                 | 262 ms: 1.19x faster                                                            |
| generators                 | 31.2 ms                                                | 26.3 ms: 1.19x faster                                                           |
| go                         | 139 ms                                                 | 119 ms: 1.17x faster                                                            |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                            |
| deltablue                  | 3.72 ms                                                | 3.21 ms: 1.16x faster                                                           |
| logging_format             | 7.23 us                                                | 6.28 us: 1.15x faster                                                           |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                                            |
| logging_simple             | 6.46 us                                                | 5.63 us: 1.15x faster                                                           |
| tornado_http               | 103 ms                                                 | 89.9 ms: 1.14x faster                                                           |
| chaos                      | 67.0 ms                                                | 58.9 ms: 1.14x faster                                                           |
| crypto_pyaes               | 81.9 ms                                                | 73.0 ms: 1.12x faster                                                           |
| sympy_str                  | 300 ms                                                 | 268 ms: 1.12x faster                                                            |
| tomli_loads                | 2.33 sec                                               | 2.10 sec: 1.11x faster                                                          |
| scimark_monte_carlo        | 75.1 ms                                                | 68.3 ms: 1.10x faster                                                           |
| nbody                      | 97.0 ms                                                | 88.9 ms: 1.09x faster                                                           |
| 2to3                       | 274 ms                                                 | 252 ms: 1.09x faster                                                            |
| float                      | 84.7 ms                                                | 77.8 ms: 1.09x faster                                                           |
| sympy_integrate            | 21.4 ms                                                | 19.8 ms: 1.08x faster                                                           |
| async_generators           | 463 ms                                                 | 431 ms: 1.07x faster                                                            |
| unpack_sequence            | 54.0 ns                                                | 50.4 ns: 1.07x faster                                                           |
| unpickle_pure_python       | 230 us                                                 | 215 us: 1.07x faster                                                            |
| pprint_safe_repr           | 776 ms                                                 | 727 ms: 1.07x faster                                                            |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.06x faster                                                           |
| json_loads                 | 28.5 us                                                | 26.8 us: 1.06x faster                                                           |
| sympy_expand               | 478 ms                                                 | 451 ms: 1.06x faster                                                            |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.06x faster                                                           |
| pickle_pure_python         | 324 us                                                 | 306 us: 1.06x faster                                                            |
| dulwich_log                | 68.5 ms                                                | 64.8 ms: 1.06x faster                                                           |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                                          |
| spectral_norm              | 115 ms                                                 | 109 ms: 1.05x faster                                                            |
| docutils                   | 2.77 sec                                               | 2.63 sec: 1.05x faster                                                          |
| scimark_fft                | 382 ms                                                 | 363 ms: 1.05x faster                                                            |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                            |
| fannkuch                   | 417 ms                                                 | 399 ms: 1.05x faster                                                            |
| unpickle                   | 15.9 us                                                | 15.2 us: 1.04x faster                                                           |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.04x faster                                                          |
| sqlglot_normalize          | 110 ms                                                 | 106 ms: 1.04x faster                                                            |
| xml_etree_generate         | 89.2 ms                                                | 85.5 ms: 1.04x faster                                                           |
| json                       | 5.26 ms                                                | 5.06 ms: 1.04x faster                                                           |
| scimark_sor                | 129 ms                                                 | 124 ms: 1.04x faster                                                            |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.04x faster                                                            |
| xml_etree_process          | 61.7 ms                                                | 59.4 ms: 1.04x faster                                                           |
| nqueens                    | 83.3 ms                                                | 80.2 ms: 1.04x faster                                                           |
| mako                       | 11.9 ms                                                | 11.5 ms: 1.04x faster                                                           |
| sqlglot_optimize           | 54.8 ms                                                | 53.1 ms: 1.03x faster                                                           |
| pyflate                    | 482 ms                                                 | 468 ms: 1.03x faster                                                            |
| pickle_dict                | 35.5 us                                                | 34.5 us: 1.03x faster                                                           |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.92 ms: 1.03x faster                                                           |
| xml_etree_parse            | 159 ms                                                 | 155 ms: 1.03x faster                                                            |
| django_template            | 34.6 ms                                                | 33.8 ms: 1.02x faster                                                           |
| mdp                        | 2.63 sec                                               | 2.57 sec: 1.02x faster                                                          |
| asyncio_tcp                | 491 ms                                                 | 480 ms: 1.02x faster                                                            |
| hexiom                     | 6.41 ms                                                | 6.29 ms: 1.02x faster                                                           |
| xml_etree_iterparse        | 107 ms                                                 | 105 ms: 1.02x faster                                                            |
| pickle                     | 11.6 us                                                | 11.4 us: 1.02x faster                                                           |
| logging_silent             | 104 ns                                                 | 103 ns: 1.01x faster                                                            |
| bench_thread_pool          | 842 us                                                 | 844 us: 1.00x slower                                                            |
| sqlite_synth               | 2.83 us                                                | 2.86 us: 1.01x slower                                                           |
| pickle_list                | 5.08 us                                                | 5.14 us: 1.01x slower                                                           |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                                            |
| python_startup_no_site     | 6.94 ms                                                | 7.03 ms: 1.01x slower                                                           |
| richards                   | 45.8 ms                                                | 46.7 ms: 1.02x slower                                                           |
| regex_dna                  | 212 ms                                                 | 217 ms: 1.02x slower                                                            |
| typing_runtime_protocols   | 158 us                                                 | 162 us: 1.02x slower                                                            |
| richards_super             | 51.5 ms                                                | 52.9 ms: 1.03x slower                                                           |
| unpickle_list              | 5.29 us                                                | 5.43 us: 1.03x slower                                                           |
| gc_traversal               | 3.79 ms                                                | 3.92 ms: 1.03x slower                                                           |
| regex_v8                   | 23.1 ms                                                | 24.9 ms: 1.08x slower                                                           |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                           |
| telco                      | 7.10 ms                                                | 7.93 ms: 1.12x slower                                                           |
| json_dumps                 | 10.4 ms                                                | 11.8 ms: 1.14x slower                                                           |
| coverage                   | 72.7 ms                                                | 84.7 ms: 1.17x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 1.79 ms: 1.21x slower                                                           |
| bench_mp_pool              | 24.0 ms                                                | 56.0 ms: 2.33x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                                    |

Benchmark hidden because not significant (4): asyncio_tcp_ssl, pidigits, regex_effbot, coroutines
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241012-3.14.0a0-8278d07/bm-20241012-linux-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 0.97x