# Results vs. 3.12.0

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: 190fbfa
- commit date: 2024-07-14
- overall geometric mean: 1.07x faster
- HPT reliability: 99.86%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 273 ms: 1.00x faster                                                      |
| docutils       | 2.77 sec                                               | 2.98 sec: 1.08x slower                                                    |
| tornado_http   | 103 ms                                                 | 98.3 ms: 1.04x faster                                                     |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 383 ms: 1.50x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 305 ms: 1.47x faster                                                      |
| async_tree_none            | 472 ms                                                 | 328 ms: 1.44x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 412 ms: 1.40x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 867 ms: 1.36x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 545 ms: 1.33x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 566 ms: 1.28x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 910 ms: 1.27x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.38x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 77.0 ms: 1.26x faster                                                     |
| float          | 84.7 ms                                                | 70.4 ms: 1.20x faster                                                     |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                      |
| Geometric mean | (ref)                                                  | 1.15x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 132 ms: 1.12x faster                                                      |
| regex_v8       | 23.1 ms                                                | 23.7 ms: 1.02x slower                                                     |
| regex_dna      | 212 ms                                                 | 219 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.93 sec: 1.21x faster                                                    |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.08x faster                                                      |
| unpickle_pure_python | 230 us                                                 | 215 us: 1.07x faster                                                      |
| pickle_pure_python   | 324 us                                                 | 304 us: 1.07x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 84.3 ms: 1.06x faster                                                     |
| xml_etree_process    | 61.7 ms                                                | 58.6 ms: 1.05x faster                                                     |
| json_loads           | 28.5 us                                                | 27.5 us: 1.04x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                 | 103 ms: 1.03x faster                                                      |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                              |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.13 ms: 1.03x slower                                                     |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.96 ms: 1.19x faster                                                     |
| django_template | 34.6 ms                                                | 40.4 ms: 1.17x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 26.6 us: 1.53x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 383 ms: 1.50x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 305 ms: 1.47x faster                                                      |
| async_tree_none            | 472 ms                                                 | 328 ms: 1.44x faster                                                      |
| deepcopy                   | 371 us                                                 | 258 us: 1.44x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 412 ms: 1.40x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 867 ms: 1.36x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 545 ms: 1.33x faster                                                      |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 566 ms: 1.28x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 910 ms: 1.27x faster                                                      |
| nbody                      | 97.0 ms                                                | 77.0 ms: 1.26x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                | 2.68 us: 1.25x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 66.7 ms: 1.23x faster                                                     |
| scimark_fft                | 382 ms                                                 | 313 ms: 1.22x faster                                                      |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.21x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 1.93 sec: 1.21x faster                                                    |
| float                      | 84.7 ms                                                | 70.4 ms: 1.20x faster                                                     |
| chaos                      | 67.0 ms                                                | 56.0 ms: 1.20x faster                                                     |
| mako                       | 11.9 ms                                                | 9.96 ms: 1.19x faster                                                     |
| logging_format             | 7.23 us                                                | 6.09 us: 1.19x faster                                                     |
| scimark_monte_carlo        | 75.1 ms                                                | 63.4 ms: 1.18x faster                                                     |
| richards                   | 45.8 ms                                                | 39.1 ms: 1.17x faster                                                     |
| logging_simple             | 6.46 us                                                | 5.54 us: 1.17x faster                                                     |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.36 ms: 1.16x faster                                                     |
| raytrace                   | 312 ms                                                 | 269 ms: 1.16x faster                                                      |
| spectral_norm              | 115 ms                                                 | 101 ms: 1.14x faster                                                      |
| fannkuch                   | 417 ms                                                 | 366 ms: 1.14x faster                                                      |
| richards_super             | 51.5 ms                                                | 45.3 ms: 1.14x faster                                                     |
| regex_compile              | 148 ms                                                 | 132 ms: 1.12x faster                                                      |
| deltablue                  | 3.72 ms                                                | 3.42 ms: 1.09x faster                                                     |
| pprint_safe_repr           | 776 ms                                                 | 715 ms: 1.09x faster                                                      |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.08x faster                                                      |
| pyflate                    | 482 ms                                                 | 449 ms: 1.07x faster                                                      |
| pprint_pformat             | 1.57 sec                                               | 1.46 sec: 1.07x faster                                                    |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.07x faster                                                     |
| unpickle_pure_python       | 230 us                                                 | 215 us: 1.07x faster                                                      |
| pickle_pure_python         | 324 us                                                 | 304 us: 1.07x faster                                                      |
| xml_etree_generate         | 89.2 ms                                                | 84.3 ms: 1.06x faster                                                     |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                      |
| xml_etree_process          | 61.7 ms                                                | 58.6 ms: 1.05x faster                                                     |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.05x faster                                                    |
| tornado_http               | 103 ms                                                 | 98.3 ms: 1.04x faster                                                     |
| sqlglot_transpile          | 1.68 ms                                                | 1.62 ms: 1.04x faster                                                     |
| json_loads                 | 28.5 us                                                | 27.5 us: 1.04x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                 | 103 ms: 1.03x faster                                                      |
| json                       | 5.26 ms                                                | 5.10 ms: 1.03x faster                                                     |
| dulwich_log                | 68.5 ms                                                | 66.7 ms: 1.03x faster                                                     |
| logging_silent             | 104 ns                                                 | 102 ns: 1.02x faster                                                      |
| scimark_sor                | 129 ms                                                 | 127 ms: 1.02x faster                                                      |
| gc_traversal               | 3.79 ms                                                | 3.73 ms: 1.02x faster                                                     |
| sympy_sum                  | 169 ms                                                 | 168 ms: 1.01x faster                                                      |
| 2to3                       | 274 ms                                                 | 273 ms: 1.00x faster                                                      |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                      |
| go                         | 139 ms                                                 | 140 ms: 1.01x slower                                                      |
| scimark_lu                 | 118 ms                                                 | 119 ms: 1.01x slower                                                      |
| asyncio_websockets         | 551 ms                                                 | 557 ms: 1.01x slower                                                      |
| hexiom                     | 6.41 ms                                                | 6.52 ms: 1.02x slower                                                     |
| bench_thread_pool          | 842 us                                                 | 857 us: 1.02x slower                                                      |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.02x slower                                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.82 sec: 1.02x slower                                                    |
| sympy_expand               | 478 ms                                                 | 489 ms: 1.02x slower                                                      |
| regex_v8                   | 23.1 ms                                                | 23.7 ms: 1.02x slower                                                     |
| python_startup_no_site     | 6.94 ms                                                | 7.13 ms: 1.03x slower                                                     |
| dask                       | 372 ms                                                 | 384 ms: 1.03x slower                                                      |
| regex_dna                  | 212 ms                                                 | 219 ms: 1.04x slower                                                      |
| mdp                        | 2.63 sec                                               | 2.74 sec: 1.04x slower                                                    |
| sqlglot_optimize           | 54.8 ms                                                | 57.3 ms: 1.05x slower                                                     |
| asyncio_tcp                | 491 ms                                                 | 518 ms: 1.06x slower                                                      |
| docutils                   | 2.77 sec                                               | 2.98 sec: 1.08x slower                                                    |
| typing_runtime_protocols   | 158 us                                                 | 171 us: 1.08x slower                                                      |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                     |
| async_generators           | 463 ms                                                 | 514 ms: 1.11x slower                                                      |
| telco                      | 7.10 ms                                                | 8.00 ms: 1.13x slower                                                     |
| django_template            | 34.6 ms                                                | 40.4 ms: 1.17x slower                                                     |
| nqueens                    | 83.3 ms                                                | 97.5 ms: 1.17x slower                                                     |
| sympy_integrate            | 21.4 ms                                                | 25.3 ms: 1.18x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 1.76 ms: 1.19x slower                                                     |
| coroutines                 | 23.2 ms                                                | 27.6 ms: 1.19x slower                                                     |
| coverage                   | 72.7 ms                                                | 92.4 ms: 1.27x slower                                                     |
| generators                 | 31.2 ms                                                | 56.1 ms: 1.80x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                              |

Benchmark hidden because not significant (4): bench_mp_pool, regex_effbot, sympy_str, json_dumps
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240714-3.14.0a0-190fbfa-JIT/bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.86% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x