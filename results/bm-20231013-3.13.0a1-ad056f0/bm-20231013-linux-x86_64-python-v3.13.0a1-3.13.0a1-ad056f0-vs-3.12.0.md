
# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a1
- machine: linux-x86_64
- commit hash: ad056f0
- commit date: 2023-10-13
- overall geometric mean: 1.02x faster \*
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 269 ms: 1.02x faster                                       |
| chameleon      | 7.41 ms                                                | 7.07 ms: 1.05x faster                                      |
| docutils       | 2.77 sec                                               | 2.64 sec: 1.05x faster                                     |
| tornado_http   | 103 ms                                                 | 96.0 ms: 1.07x faster                                      |
| Geometric mean | (ref)                                                  | 1.05x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 437 ms: 1.08x faster                                       |
| async_tree_memoization     | 578 ms                                                 | 564 ms: 1.03x faster                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 712 ms: 1.02x faster                                       |
| async_tree_none_tg         | 450 ms                                                 | 453 ms: 1.01x slower                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 741 ms: 1.02x slower                                       |
| async_tree_io              | 1.16 sec                                               | 1.19 sec: 1.03x slower                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 595 ms: 1.04x slower                                       |
| async_tree_io_tg           | 1.18 sec                                               | 1.23 sec: 1.04x slower                                     |
| Geometric mean             | (ref)                                                  | 1.00x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 88.6 ms: 1.09x faster                                      |
| float          | 84.7 ms                                                | 81.6 ms: 1.04x faster                                      |
| pidigits       | 187 ms                                                 | 195 ms: 1.04x slower                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 138 ms: 1.07x faster                                       |
| regex_effbot   | 3.61 ms                                                | 3.67 ms: 1.02x slower                                      |
| regex_v8       | 23.1 ms                                                | 24.7 ms: 1.07x slower                                      |
| Geometric mean | (ref)                                                  | 1.00x slower                                               |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.15 sec: 1.08x faster                                     |
| pickle_pure_python   | 324 us                                                 | 300 us: 1.08x faster                                       |
| unpickle             | 15.9 us                                                | 14.9 us: 1.06x faster                                      |
| unpickle_list        | 5.29 us                                                | 5.05 us: 1.05x faster                                      |
| unpickle_pure_python | 230 us                                                 | 222 us: 1.04x faster                                       |
| xml_etree_process    | 61.7 ms                                                | 59.9 ms: 1.03x faster                                      |
| pickle_dict          | 35.5 us                                                | 34.6 us: 1.03x faster                                      |
| xml_etree_generate   | 89.2 ms                                                | 86.9 ms: 1.03x faster                                      |
| json_loads           | 28.5 us                                                | 27.8 us: 1.02x faster                                      |
| xml_etree_parse      | 159 ms                                                 | 157 ms: 1.01x faster                                       |
| xml_etree_iterparse  | 107 ms                                                 | 106 ms: 1.01x faster                                       |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                      |
| Geometric mean       | (ref)                                                  | 1.03x faster                                               |

Benchmark hidden because not significant (2): pickle_list, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.87 ms: 1.01x faster                                      |
| python_startup         | 9.55 ms                                                | 10.1 ms: 1.05x slower                                      |
| Geometric mean         | (ref)                                                  | 1.02x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 11.9 ms                                                | 11.2 ms: 1.06x faster                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| raytrace                   | 312 ms                                                 | 274 ms: 1.14x faster                                       |
| crypto_pyaes               | 81.9 ms                                                | 71.8 ms: 1.14x faster                                      |
| logging_format             | 7.23 us                                                | 6.47 us: 1.12x faster                                      |
| deltablue                  | 3.72 ms                                                | 3.34 ms: 1.11x faster                                      |
| nbody                      | 97.0 ms                                                | 88.6 ms: 1.09x faster                                      |
| logging_simple             | 6.46 us                                                | 5.90 us: 1.09x faster                                      |
| chaos                      | 67.0 ms                                                | 61.7 ms: 1.09x faster                                      |
| tomli_loads                | 2.33 sec                                               | 2.15 sec: 1.08x faster                                     |
| sympy_sum                  | 169 ms                                                 | 156 ms: 1.08x faster                                       |
| pickle_pure_python         | 324 us                                                 | 300 us: 1.08x faster                                       |
| scimark_monte_carlo        | 75.1 ms                                                | 69.5 ms: 1.08x faster                                      |
| async_tree_none            | 472 ms                                                 | 437 ms: 1.08x faster                                       |
| regex_compile              | 148 ms                                                 | 138 ms: 1.07x faster                                       |
| tornado_http               | 103 ms                                                 | 96.0 ms: 1.07x faster                                      |
| sympy_str                  | 300 ms                                                 | 281 ms: 1.07x faster                                       |
| deepcopy_reduce            | 3.35 us                                                | 3.14 us: 1.07x faster                                      |
| unpickle                   | 15.9 us                                                | 14.9 us: 1.06x faster                                      |
| sympy_integrate            | 21.4 ms                                                | 20.2 ms: 1.06x faster                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.06x faster                                      |
| unpack_sequence            | 54.0 ns                                                | 51.0 ns: 1.06x faster                                      |
| mako                       | 11.9 ms                                                | 11.2 ms: 1.06x faster                                      |
| sympy_expand               | 478 ms                                                 | 452 ms: 1.06x faster                                       |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.79 ms: 1.05x faster                                      |
| deepcopy_memo              | 40.7 us                                                | 38.7 us: 1.05x faster                                      |
| deepcopy                   | 371 us                                                 | 353 us: 1.05x faster                                       |
| docutils                   | 2.77 sec                                               | 2.64 sec: 1.05x faster                                     |
| sqlglot_transpile          | 1.68 ms                                                | 1.60 ms: 1.05x faster                                      |
| scimark_sor                | 129 ms                                                 | 123 ms: 1.05x faster                                       |
| chameleon                  | 7.41 ms                                                | 7.07 ms: 1.05x faster                                      |
| unpickle_list              | 5.29 us                                                | 5.05 us: 1.05x faster                                      |
| comprehensions             | 21.8 us                                                | 20.8 us: 1.05x faster                                      |
| spectral_norm              | 115 ms                                                 | 110 ms: 1.04x faster                                       |
| generators                 | 31.2 ms                                                | 29.9 ms: 1.04x faster                                      |
| hexiom                     | 6.41 ms                                                | 6.16 ms: 1.04x faster                                      |
| float                      | 84.7 ms                                                | 81.6 ms: 1.04x faster                                      |
| fannkuch                   | 417 ms                                                 | 402 ms: 1.04x faster                                       |
| unpickle_pure_python       | 230 us                                                 | 222 us: 1.04x faster                                       |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                       |
| scimark_fft                | 382 ms                                                 | 369 ms: 1.03x faster                                       |
| bench_thread_pool          | 842 us                                                 | 815 us: 1.03x faster                                       |
| pprint_safe_repr           | 776 ms                                                 | 752 ms: 1.03x faster                                       |
| xml_etree_process          | 61.7 ms                                                | 59.9 ms: 1.03x faster                                      |
| pickle_dict                | 35.5 us                                                | 34.6 us: 1.03x faster                                      |
| pprint_pformat             | 1.57 sec                                               | 1.53 sec: 1.03x faster                                     |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                       |
| xml_etree_generate         | 89.2 ms                                                | 86.9 ms: 1.03x faster                                      |
| async_tree_memoization     | 578 ms                                                 | 564 ms: 1.03x faster                                       |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.03x faster                                       |
| json_loads                 | 28.5 us                                                | 27.8 us: 1.02x faster                                      |
| async_generators           | 463 ms                                                 | 453 ms: 1.02x faster                                       |
| dulwich_log                | 68.5 ms                                                | 67.1 ms: 1.02x faster                                      |
| 2to3                       | 274 ms                                                 | 269 ms: 1.02x faster                                       |
| pyflate                    | 482 ms                                                 | 473 ms: 1.02x faster                                       |
| json                       | 5.26 ms                                                | 5.16 ms: 1.02x faster                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 712 ms: 1.02x faster                                       |
| sqlglot_optimize           | 54.8 ms                                                | 53.9 ms: 1.02x faster                                      |
| nqueens                    | 83.3 ms                                                | 81.9 ms: 1.02x faster                                      |
| asyncio_tcp                | 491 ms                                                 | 484 ms: 1.01x faster                                       |
| typing_runtime_protocols   | 158 us                                                 | 156 us: 1.01x faster                                       |
| xml_etree_parse            | 159 ms                                                 | 157 ms: 1.01x faster                                       |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                      |
| xml_etree_iterparse        | 107 ms                                                 | 106 ms: 1.01x faster                                       |
| python_startup_no_site     | 6.94 ms                                                | 6.87 ms: 1.01x faster                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x slower                                     |
| async_tree_none_tg         | 450 ms                                                 | 453 ms: 1.01x slower                                       |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                      |
| coroutines                 | 23.2 ms                                                | 23.4 ms: 1.01x slower                                      |
| go                         | 139 ms                                                 | 141 ms: 1.01x slower                                       |
| regex_effbot               | 3.61 ms                                                | 3.67 ms: 1.02x slower                                      |
| gc_traversal               | 3.79 ms                                                | 3.87 ms: 1.02x slower                                      |
| pycparser                  | 1.18 sec                                               | 1.20 sec: 1.02x slower                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 741 ms: 1.02x slower                                       |
| logging_silent             | 104 ns                                                 | 107 ns: 1.02x slower                                       |
| async_tree_io              | 1.16 sec                                               | 1.19 sec: 1.03x slower                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 595 ms: 1.04x slower                                       |
| async_tree_io_tg           | 1.18 sec                                               | 1.23 sec: 1.04x slower                                     |
| pidigits                   | 187 ms                                                 | 195 ms: 1.04x slower                                       |
| mdp                        | 2.63 sec                                               | 2.74 sec: 1.04x slower                                     |
| python_startup             | 9.55 ms                                                | 10.1 ms: 1.05x slower                                      |
| richards                   | 45.8 ms                                                | 48.6 ms: 1.06x slower                                      |
| richards_super             | 51.5 ms                                                | 55.0 ms: 1.07x slower                                      |
| regex_v8                   | 23.1 ms                                                | 24.7 ms: 1.07x slower                                      |
| telco                      | 7.10 ms                                                | 8.17 ms: 1.15x slower                                      |
| coverage                   | 72.7 ms                                                | 94.4 ms: 1.30x slower                                      |
| Geometric mean             | (ref)                                                  | 1.02x faster                                               |

Benchmark hidden because not significant (7): create_gc_cycles, bench_mp_pool, asyncio_websockets, pathlib, regex_dna, pickle_list, pickle
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, django_template, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: 0.91x