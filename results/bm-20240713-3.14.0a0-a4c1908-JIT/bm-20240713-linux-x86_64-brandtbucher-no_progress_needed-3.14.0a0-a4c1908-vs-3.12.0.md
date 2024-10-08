# Results vs. 3.12.0

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: a4c1908
- commit date: 2024-07-13
- overall geometric mean: 1.09x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 275 ms: 1.00x slower                                                      |
| docutils       | 2.77 sec                                               | 2.92 sec: 1.05x slower                                                    |
| tornado_http   | 103 ms                                                 | 92.2 ms: 1.11x faster                                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 379 ms: 1.52x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 301 ms: 1.50x faster                                                      |
| async_tree_none            | 472 ms                                                 | 327 ms: 1.44x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 411 ms: 1.40x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 846 ms: 1.40x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 845 ms: 1.37x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 545 ms: 1.33x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 569 ms: 1.27x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.40x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.5 ms: 1.22x faster                                                     |
| nbody          | 97.0 ms                                                | 80.5 ms: 1.20x faster                                                     |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.14x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 137 ms: 1.08x faster                                                      |
| regex_effbot   | 3.61 ms                                                | 3.75 ms: 1.04x slower                                                     |
| regex_dna      | 212 ms                                                 | 228 ms: 1.08x slower                                                      |
| regex_v8       | 23.1 ms                                                | 25.4 ms: 1.10x slower                                                     |
| Geometric mean | (ref)                                                  | 1.03x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.87 sec: 1.25x faster                                                    |
| xml_etree_generate   | 89.2 ms                                                | 81.9 ms: 1.09x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                 | 98.4 ms: 1.09x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.08x faster                                                      |
| unpickle_pure_python | 230 us                                                 | 213 us: 1.08x faster                                                      |
| xml_etree_process    | 61.7 ms                                                | 57.6 ms: 1.07x faster                                                     |
| pickle_pure_python   | 324 us                                                 | 308 us: 1.05x faster                                                      |
| json_loads           | 28.5 us                                                | 27.6 us: 1.03x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                              |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.13 ms: 1.03x slower                                                     |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.0 ms: 1.19x faster                                                     |
| django_template | 34.6 ms                                                | 34.9 ms: 1.01x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 379 ms: 1.52x faster                                                      |
| deepcopy_memo              | 40.7 us                                                | 27.1 us: 1.50x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 301 ms: 1.50x faster                                                      |
| async_tree_none            | 472 ms                                                 | 327 ms: 1.44x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 411 ms: 1.40x faster                                                      |
| deepcopy                   | 371 us                                                 | 265 us: 1.40x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 846 ms: 1.40x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 845 ms: 1.37x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 545 ms: 1.33x faster                                                      |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.30x faster                                                     |
| richards                   | 45.8 ms                                                | 35.9 ms: 1.28x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 569 ms: 1.27x faster                                                      |
| richards_super             | 51.5 ms                                                | 40.8 ms: 1.26x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                | 2.68 us: 1.25x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 1.87 sec: 1.25x faster                                                    |
| crypto_pyaes               | 81.9 ms                                                | 66.6 ms: 1.23x faster                                                     |
| scimark_fft                | 382 ms                                                 | 311 ms: 1.23x faster                                                      |
| float                      | 84.7 ms                                                | 69.5 ms: 1.22x faster                                                     |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                                     |
| nbody                      | 97.0 ms                                                | 80.5 ms: 1.20x faster                                                     |
| scimark_monte_carlo        | 75.1 ms                                                | 62.4 ms: 1.20x faster                                                     |
| logging_format             | 7.23 us                                                | 6.04 us: 1.20x faster                                                     |
| mako                       | 11.9 ms                                                | 10.0 ms: 1.19x faster                                                     |
| logging_simple             | 6.46 us                                                | 5.45 us: 1.18x faster                                                     |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.31 ms: 1.17x faster                                                     |
| fannkuch                   | 417 ms                                                 | 359 ms: 1.16x faster                                                      |
| chaos                      | 67.0 ms                                                | 57.8 ms: 1.16x faster                                                     |
| raytrace                   | 312 ms                                                 | 273 ms: 1.15x faster                                                      |
| tornado_http               | 103 ms                                                 | 92.2 ms: 1.11x faster                                                     |
| spectral_norm              | 115 ms                                                 | 104 ms: 1.11x faster                                                      |
| pyflate                    | 482 ms                                                 | 437 ms: 1.10x faster                                                      |
| xml_etree_generate         | 89.2 ms                                                | 81.9 ms: 1.09x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                 | 98.4 ms: 1.09x faster                                                     |
| regex_compile              | 148 ms                                                 | 137 ms: 1.08x faster                                                      |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.08x faster                                                      |
| unpickle_pure_python       | 230 us                                                 | 213 us: 1.08x faster                                                      |
| deltablue                  | 3.72 ms                                                | 3.45 ms: 1.08x faster                                                     |
| xml_etree_process          | 61.7 ms                                                | 57.6 ms: 1.07x faster                                                     |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.06x faster                                                     |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                      |
| pickle_pure_python         | 324 us                                                 | 308 us: 1.05x faster                                                      |
| dulwich_log                | 68.5 ms                                                | 65.2 ms: 1.05x faster                                                     |
| pprint_safe_repr           | 776 ms                                                 | 740 ms: 1.05x faster                                                      |
| generators                 | 31.2 ms                                                | 29.8 ms: 1.05x faster                                                     |
| mdp                        | 2.63 sec                                               | 2.54 sec: 1.04x faster                                                    |
| sympy_str                  | 300 ms                                                 | 289 ms: 1.04x faster                                                      |
| json_loads                 | 28.5 us                                                | 27.6 us: 1.03x faster                                                     |
| dask                       | 372 ms                                                 | 361 ms: 1.03x faster                                                      |
| logging_silent             | 104 ns                                                 | 101 ns: 1.03x faster                                                      |
| sqlglot_transpile          | 1.68 ms                                                | 1.64 ms: 1.03x faster                                                     |
| pprint_pformat             | 1.57 sec                                               | 1.53 sec: 1.03x faster                                                    |
| async_generators           | 463 ms                                                 | 452 ms: 1.02x faster                                                      |
| bench_thread_pool          | 842 us                                                 | 827 us: 1.02x faster                                                      |
| sympy_sum                  | 169 ms                                                 | 166 ms: 1.02x faster                                                      |
| json                       | 5.26 ms                                                | 5.17 ms: 1.02x faster                                                     |
| scimark_sor                | 129 ms                                                 | 128 ms: 1.01x faster                                                      |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                      |
| 2to3                       | 274 ms                                                 | 275 ms: 1.00x slower                                                      |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                      |
| django_template            | 34.6 ms                                                | 34.9 ms: 1.01x slower                                                     |
| pycparser                  | 1.18 sec                                               | 1.19 sec: 1.01x slower                                                    |
| sqlglot_normalize          | 110 ms                                                 | 112 ms: 1.01x slower                                                      |
| gc_traversal               | 3.79 ms                                                | 3.85 ms: 1.01x slower                                                     |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                    |
| sympy_integrate            | 21.4 ms                                                | 21.7 ms: 1.02x slower                                                     |
| sqlglot_optimize           | 54.8 ms                                                | 56.2 ms: 1.03x slower                                                     |
| python_startup_no_site     | 6.94 ms                                                | 7.13 ms: 1.03x slower                                                     |
| asyncio_tcp                | 491 ms                                                 | 507 ms: 1.03x slower                                                      |
| sympy_expand               | 478 ms                                                 | 494 ms: 1.03x slower                                                      |
| go                         | 139 ms                                                 | 145 ms: 1.04x slower                                                      |
| regex_effbot               | 3.61 ms                                                | 3.75 ms: 1.04x slower                                                     |
| nqueens                    | 83.3 ms                                                | 86.5 ms: 1.04x slower                                                     |
| hexiom                     | 6.41 ms                                                | 6.73 ms: 1.05x slower                                                     |
| docutils                   | 2.77 sec                                               | 2.92 sec: 1.05x slower                                                    |
| typing_runtime_protocols   | 158 us                                                 | 169 us: 1.07x slower                                                      |
| regex_dna                  | 212 ms                                                 | 228 ms: 1.08x slower                                                      |
| regex_v8                   | 23.1 ms                                                | 25.4 ms: 1.10x slower                                                     |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                     |
| telco                      | 7.10 ms                                                | 7.88 ms: 1.11x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 1.78 ms: 1.20x slower                                                     |
| coverage                   | 72.7 ms                                                | 92.2 ms: 1.27x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                              |

Benchmark hidden because not significant (4): bench_mp_pool, json_dumps, coroutines, scimark_lu
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240713-3.14.0a0-a4c1908-JIT/bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.04x