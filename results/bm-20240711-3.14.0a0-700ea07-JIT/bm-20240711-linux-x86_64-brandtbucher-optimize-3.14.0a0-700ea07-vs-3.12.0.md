# Results vs. 3.12.0

- fork: brandtbucher
- ref: optimize
- machine: linux-x86_64
- commit hash: 700ea07
- commit date: 2024-07-11
- overall geometric mean: 1.05x faster
- HPT reliability: 99.90%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 270 ms: 1.01x faster                                            |
| docutils       | 2.77 sec                                               | 2.96 sec: 1.07x slower                                          |
| tornado_http   | 103 ms                                                 | 91.9 ms: 1.12x faster                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 383 ms: 1.50x faster                                            |
| async_tree_none_tg         | 450 ms                                                 | 307 ms: 1.46x faster                                            |
| async_tree_none            | 472 ms                                                 | 329 ms: 1.43x faster                                            |
| async_tree_memoization     | 578 ms                                                 | 411 ms: 1.41x faster                                            |
| async_tree_io_tg           | 1.18 sec                                               | 859 ms: 1.38x faster                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 549 ms: 1.32x faster                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 567 ms: 1.28x faster                                            |
| async_tree_io              | 1.16 sec                                               | 909 ms: 1.27x faster                                            |
| Geometric mean             | (ref)                                                  | 1.38x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 84.7 ms                                                | 78.7 ms: 1.08x faster                                           |
| nbody          | 97.0 ms                                                | 92.2 ms: 1.05x faster                                           |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                            |
| Geometric mean | (ref)                                                  | 1.04x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 135 ms: 1.10x faster                                            |
| regex_effbot   | 3.61 ms                                                | 3.64 ms: 1.01x slower                                           |
| regex_v8       | 23.1 ms                                                | 24.1 ms: 1.04x slower                                           |
| regex_dna      | 212 ms                                                 | 228 ms: 1.08x slower                                            |
| Geometric mean | (ref)                                                  | 1.01x slower                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle_pure_python   | 324 us                                                 | 304 us: 1.07x faster                                            |
| unpickle_pure_python | 230 us                                                 | 220 us: 1.05x faster                                            |
| tomli_loads          | 2.33 sec                                               | 2.24 sec: 1.04x faster                                          |
| json_loads           | 28.5 us                                                | 27.6 us: 1.03x faster                                           |
| xml_etree_generate   | 89.2 ms                                                | 86.9 ms: 1.03x faster                                           |
| xml_etree_process    | 61.7 ms                                                | 60.6 ms: 1.02x faster                                           |
| xml_etree_iterparse  | 107 ms                                                 | 108 ms: 1.01x slower                                            |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                    |

Benchmark hidden because not significant (2): xml_etree_parse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.06 ms: 1.02x slower                                           |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                           |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| mako           | 11.9 ms                                                | 11.5 ms: 1.04x faster                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                    |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 383 ms: 1.50x faster                                            |
| async_tree_none_tg         | 450 ms                                                 | 307 ms: 1.46x faster                                            |
| async_tree_none            | 472 ms                                                 | 329 ms: 1.43x faster                                            |
| async_tree_memoization     | 578 ms                                                 | 411 ms: 1.41x faster                                            |
| deepcopy                   | 371 us                                                 | 269 us: 1.38x faster                                            |
| async_tree_io_tg           | 1.18 sec                                               | 859 ms: 1.38x faster                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 549 ms: 1.32x faster                                            |
| deepcopy_memo              | 40.7 us                                                | 31.1 us: 1.31x faster                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 567 ms: 1.28x faster                                            |
| async_tree_io              | 1.16 sec                                               | 909 ms: 1.27x faster                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.65 us: 1.26x faster                                           |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                           |
| comprehensions             | 21.8 us                                                | 18.0 us: 1.21x faster                                           |
| logging_format             | 7.23 us                                                | 6.06 us: 1.19x faster                                           |
| logging_simple             | 6.46 us                                                | 5.46 us: 1.18x faster                                           |
| raytrace                   | 312 ms                                                 | 265 ms: 1.18x faster                                            |
| deltablue                  | 3.72 ms                                                | 3.28 ms: 1.13x faster                                           |
| crypto_pyaes               | 81.9 ms                                                | 72.9 ms: 1.12x faster                                           |
| tornado_http               | 103 ms                                                 | 91.9 ms: 1.12x faster                                           |
| chaos                      | 67.0 ms                                                | 60.2 ms: 1.11x faster                                           |
| regex_compile              | 148 ms                                                 | 135 ms: 1.10x faster                                            |
| scimark_monte_carlo        | 75.1 ms                                                | 69.4 ms: 1.08x faster                                           |
| float                      | 84.7 ms                                                | 78.7 ms: 1.08x faster                                           |
| sympy_sum                  | 169 ms                                                 | 157 ms: 1.08x faster                                            |
| sympy_str                  | 300 ms                                                 | 280 ms: 1.07x faster                                            |
| pickle_pure_python         | 324 us                                                 | 304 us: 1.07x faster                                            |
| dulwich_log                | 68.5 ms                                                | 64.9 ms: 1.06x faster                                           |
| nbody                      | 97.0 ms                                                | 92.2 ms: 1.05x faster                                           |
| unpickle_pure_python       | 230 us                                                 | 220 us: 1.05x faster                                            |
| sqlglot_parse              | 1.36 ms                                                | 1.30 ms: 1.04x faster                                           |
| tomli_loads                | 2.33 sec                                               | 2.24 sec: 1.04x faster                                          |
| sqlglot_transpile          | 1.68 ms                                                | 1.62 ms: 1.04x faster                                           |
| pprint_safe_repr           | 776 ms                                                 | 747 ms: 1.04x faster                                            |
| mako                       | 11.9 ms                                                | 11.5 ms: 1.04x faster                                           |
| scimark_fft                | 382 ms                                                 | 369 ms: 1.03x faster                                            |
| scimark_sor                | 129 ms                                                 | 125 ms: 1.03x faster                                            |
| json_loads                 | 28.5 us                                                | 27.6 us: 1.03x faster                                           |
| dask                       | 372 ms                                                 | 361 ms: 1.03x faster                                            |
| sympy_integrate            | 21.4 ms                                                | 20.8 ms: 1.03x faster                                           |
| pprint_pformat             | 1.57 sec                                               | 1.52 sec: 1.03x faster                                          |
| xml_etree_generate         | 89.2 ms                                                | 86.9 ms: 1.03x faster                                           |
| bench_thread_pool          | 842 us                                                 | 821 us: 1.03x faster                                            |
| sympy_expand               | 478 ms                                                 | 466 ms: 1.03x faster                                            |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                            |
| gc_traversal               | 3.79 ms                                                | 3.73 ms: 1.02x faster                                           |
| xml_etree_process          | 61.7 ms                                                | 60.6 ms: 1.02x faster                                           |
| 2to3                       | 274 ms                                                 | 270 ms: 1.01x faster                                            |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.01x faster                                            |
| meteor_contest             | 112 ms                                                 | 111 ms: 1.01x faster                                            |
| fannkuch                   | 417 ms                                                 | 414 ms: 1.01x faster                                            |
| async_generators           | 463 ms                                                 | 461 ms: 1.00x faster                                            |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                            |
| pyflate                    | 482 ms                                                 | 485 ms: 1.01x slower                                            |
| regex_effbot               | 3.61 ms                                                | 3.64 ms: 1.01x slower                                           |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                          |
| logging_silent             | 104 ns                                                 | 106 ns: 1.01x slower                                            |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                            |
| xml_etree_iterparse        | 107 ms                                                 | 108 ms: 1.01x slower                                            |
| python_startup_no_site     | 6.94 ms                                                | 7.06 ms: 1.02x slower                                           |
| richards                   | 45.8 ms                                                | 47.0 ms: 1.03x slower                                           |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.20 ms: 1.03x slower                                           |
| coroutines                 | 23.2 ms                                                | 24.0 ms: 1.03x slower                                           |
| go                         | 139 ms                                                 | 145 ms: 1.04x slower                                            |
| richards_super             | 51.5 ms                                                | 53.5 ms: 1.04x slower                                           |
| regex_v8                   | 23.1 ms                                                | 24.1 ms: 1.04x slower                                           |
| typing_runtime_protocols   | 158 us                                                 | 165 us: 1.05x slower                                            |
| mdp                        | 2.63 sec                                               | 2.77 sec: 1.05x slower                                          |
| sqlglot_optimize           | 54.8 ms                                                | 58.0 ms: 1.06x slower                                           |
| docutils                   | 2.77 sec                                               | 2.96 sec: 1.07x slower                                          |
| regex_dna                  | 212 ms                                                 | 228 ms: 1.08x slower                                            |
| nqueens                    | 83.3 ms                                                | 90.6 ms: 1.09x slower                                           |
| hexiom                     | 6.41 ms                                                | 7.05 ms: 1.10x slower                                           |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                           |
| telco                      | 7.10 ms                                                | 8.30 ms: 1.17x slower                                           |
| create_gc_cycles           | 1.48 ms                                                | 1.74 ms: 1.18x slower                                           |
| coverage                   | 72.7 ms                                                | 92.7 ms: 1.28x slower                                           |
| generators                 | 31.2 ms                                                | 45.8 ms: 1.47x slower                                           |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                    |

Benchmark hidden because not significant (8): json, django_template, xml_etree_parse, asyncio_tcp, bench_mp_pool, json_dumps, pycparser, sqlglot_normalize
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240711-3.14.0a0-700ea07-JIT/bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.90% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x