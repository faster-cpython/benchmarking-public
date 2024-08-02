# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a4
- machine: linux-x86_64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.01x faster \*
- HPT reliability: 72.82%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 276 ms: 1.01x slower                                       |
| chameleon      | 7.41 ms                                                | 6.75 ms: 1.10x faster                                      |
| docutils       | 2.77 sec                                               | 2.64 sec: 1.05x faster                                     |
| tornado_http   | 103 ms                                                 | 96.9 ms: 1.06x faster                                      |
| Geometric mean | (ref)                                                  | 1.05x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|---------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none           | 472 ms                                                 | 439 ms: 1.07x faster                                       |
| async_tree_memoization    | 578 ms                                                 | 568 ms: 1.02x faster                                       |
| async_tree_cpu_io_mixed   | 726 ms                                                 | 716 ms: 1.01x faster                                       |
| async_tree_none_tg        | 450 ms                                                 | 452 ms: 1.01x slower                                       |
| async_tree_io_tg          | 1.18 sec                                               | 1.20 sec: 1.01x slower                                     |
| async_tree_io             | 1.16 sec                                               | 1.18 sec: 1.02x slower                                     |
| async_tree_memoization_tg | 575 ms                                                 | 592 ms: 1.03x slower                                       |
| Geometric mean            | (ref)                                                  | 1.00x faster                                               |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 187 ms                                                 | 188 ms: 1.01x slower                                       |
| float          | 84.7 ms                                                | 86.1 ms: 1.02x slower                                      |
| nbody          | 97.0 ms                                                | 102 ms: 1.05x slower                                       |
| Geometric mean | (ref)                                                  | 1.03x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 141 ms: 1.06x faster                                       |
| regex_effbot   | 3.61 ms                                                | 3.57 ms: 1.01x faster                                      |
| regex_dna      | 212 ms                                                 | 225 ms: 1.06x slower                                       |
| regex_v8       | 23.1 ms                                                | 25.1 ms: 1.09x slower                                      |
| Geometric mean | (ref)                                                  | 1.02x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 324 us                                                 | 296 us: 1.10x faster                                       |
| xml_etree_process    | 61.7 ms                                                | 57.9 ms: 1.07x faster                                      |
| tomli_loads          | 2.33 sec                                               | 2.19 sec: 1.06x faster                                     |
| pickle_dict          | 35.5 us                                                | 33.6 us: 1.06x faster                                      |
| unpickle             | 15.9 us                                                | 15.1 us: 1.05x faster                                      |
| json_loads           | 28.5 us                                                | 27.3 us: 1.04x faster                                      |
| xml_etree_generate   | 89.2 ms                                                | 85.7 ms: 1.04x faster                                      |
| unpickle_list        | 5.29 us                                                | 5.11 us: 1.04x faster                                      |
| pickle               | 11.6 us                                                | 11.4 us: 1.02x faster                                      |
| xml_etree_parse      | 159 ms                                                 | 157 ms: 1.02x faster                                       |
| unpickle_pure_python | 230 us                                                 | 228 us: 1.01x faster                                       |
| xml_etree_iterparse  | 107 ms                                                 | 108 ms: 1.01x slower                                       |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                      |
| Geometric mean       | (ref)                                                  | 1.03x faster                                               |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 9.55 ms                                                | 10.3 ms: 1.08x slower                                      |
| python_startup_no_site | 6.94 ms                                                | 8.95 ms: 1.29x slower                                      |
| Geometric mean         | (ref)                                                  | 1.18x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 11.9 ms                                                | 12.4 ms: 1.04x slower                                      |

All benchmarks:
===============

| Benchmark                 | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|---------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols  | 158 us                                                 | 110 us: 1.44x faster                                       |
| unpack_sequence           | 54.0 ns                                                | 44.9 ns: 1.20x faster                                      |
| comprehensions            | 21.8 us                                                | 18.2 us: 1.20x faster                                      |
| logging_format            | 7.23 us                                                | 6.30 us: 1.15x faster                                      |
| logging_simple            | 6.46 us                                                | 5.74 us: 1.13x faster                                      |
| deltablue                 | 3.72 ms                                                | 3.32 ms: 1.12x faster                                      |
| raytrace                  | 312 ms                                                 | 280 ms: 1.12x faster                                       |
| deepcopy_reduce           | 3.35 us                                                | 3.04 us: 1.10x faster                                      |
| chameleon                 | 7.41 ms                                                | 6.75 ms: 1.10x faster                                      |
| pickle_pure_python        | 324 us                                                 | 296 us: 1.10x faster                                       |
| sympy_sum                 | 169 ms                                                 | 157 ms: 1.08x faster                                       |
| async_tree_none           | 472 ms                                                 | 439 ms: 1.07x faster                                       |
| deepcopy                  | 371 us                                                 | 345 us: 1.07x faster                                       |
| generators                | 31.2 ms                                                | 29.1 ms: 1.07x faster                                      |
| deepcopy_memo             | 40.7 us                                                | 38.1 us: 1.07x faster                                      |
| pathlib                   | 19.3 ms                                                | 18.1 ms: 1.07x faster                                      |
| sympy_str                 | 300 ms                                                 | 281 ms: 1.07x faster                                       |
| xml_etree_process         | 61.7 ms                                                | 57.9 ms: 1.07x faster                                      |
| tomli_loads               | 2.33 sec                                               | 2.19 sec: 1.06x faster                                     |
| sqlglot_parse             | 1.36 ms                                                | 1.28 ms: 1.06x faster                                      |
| scimark_sor               | 129 ms                                                 | 122 ms: 1.06x faster                                       |
| tornado_http              | 103 ms                                                 | 96.9 ms: 1.06x faster                                      |
| pickle_dict               | 35.5 us                                                | 33.6 us: 1.06x faster                                      |
| regex_compile             | 148 ms                                                 | 141 ms: 1.06x faster                                       |
| sympy_integrate           | 21.4 ms                                                | 20.3 ms: 1.05x faster                                      |
| unpickle                  | 15.9 us                                                | 15.1 us: 1.05x faster                                      |
| scimark_lu                | 118 ms                                                 | 112 ms: 1.05x faster                                       |
| docutils                  | 2.77 sec                                               | 2.64 sec: 1.05x faster                                     |
| sqlglot_transpile         | 1.68 ms                                                | 1.61 ms: 1.05x faster                                      |
| json_loads                | 28.5 us                                                | 27.3 us: 1.04x faster                                      |
| scimark_fft               | 382 ms                                                 | 366 ms: 1.04x faster                                       |
| xml_etree_generate        | 89.2 ms                                                | 85.7 ms: 1.04x faster                                      |
| unpickle_list             | 5.29 us                                                | 5.11 us: 1.04x faster                                      |
| crypto_pyaes              | 81.9 ms                                                | 79.1 ms: 1.03x faster                                      |
| sqlglot_normalize         | 110 ms                                                 | 107 ms: 1.03x faster                                       |
| logging_silent            | 104 ns                                                 | 101 ns: 1.03x faster                                       |
| json                      | 5.26 ms                                                | 5.12 ms: 1.03x faster                                      |
| meteor_contest            | 112 ms                                                 | 110 ms: 1.02x faster                                       |
| richards                  | 45.8 ms                                                | 44.8 ms: 1.02x faster                                      |
| pickle                    | 11.6 us                                                | 11.4 us: 1.02x faster                                      |
| async_tree_memoization    | 578 ms                                                 | 568 ms: 1.02x faster                                       |
| xml_etree_parse           | 159 ms                                                 | 157 ms: 1.02x faster                                       |
| scimark_monte_carlo       | 75.1 ms                                                | 74.0 ms: 1.01x faster                                      |
| async_tree_cpu_io_mixed   | 726 ms                                                 | 716 ms: 1.01x faster                                       |
| richards_super            | 51.5 ms                                                | 50.8 ms: 1.01x faster                                      |
| regex_effbot              | 3.61 ms                                                | 3.57 ms: 1.01x faster                                      |
| unpickle_pure_python      | 230 us                                                 | 228 us: 1.01x faster                                       |
| gc_traversal              | 3.79 ms                                                | 3.76 ms: 1.01x faster                                      |
| bench_thread_pool         | 842 us                                                 | 836 us: 1.01x faster                                       |
| sqlite_synth              | 2.83 us                                                | 2.82 us: 1.00x faster                                      |
| dulwich_log               | 68.5 ms                                                | 68.2 ms: 1.00x faster                                      |
| sqlglot_optimize          | 54.8 ms                                                | 55.1 ms: 1.01x slower                                      |
| async_tree_none_tg        | 450 ms                                                 | 452 ms: 1.01x slower                                       |
| pidigits                  | 187 ms                                                 | 188 ms: 1.01x slower                                       |
| 2to3                      | 274 ms                                                 | 276 ms: 1.01x slower                                       |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.01x slower                                     |
| xml_etree_iterparse       | 107 ms                                                 | 108 ms: 1.01x slower                                       |
| fannkuch                  | 417 ms                                                 | 422 ms: 1.01x slower                                       |
| create_gc_cycles          | 1.48 ms                                                | 1.49 ms: 1.01x slower                                      |
| asyncio_tcp               | 491 ms                                                 | 497 ms: 1.01x slower                                       |
| async_tree_io_tg          | 1.18 sec                                               | 1.20 sec: 1.01x slower                                     |
| json_dumps                | 10.4 ms                                                | 10.5 ms: 1.01x slower                                      |
| float                     | 84.7 ms                                                | 86.1 ms: 1.02x slower                                      |
| async_tree_io             | 1.16 sec                                               | 1.18 sec: 1.02x slower                                     |
| coroutines                | 23.2 ms                                                | 23.7 ms: 1.02x slower                                      |
| pprint_pformat            | 1.57 sec                                               | 1.61 sec: 1.03x slower                                     |
| async_tree_memoization_tg | 575 ms                                                 | 592 ms: 1.03x slower                                       |
| chaos                     | 67.0 ms                                                | 69.1 ms: 1.03x slower                                      |
| pycparser                 | 1.18 sec                                               | 1.22 sec: 1.03x slower                                     |
| mako                      | 11.9 ms                                                | 12.4 ms: 1.04x slower                                      |
| go                        | 139 ms                                                 | 146 ms: 1.05x slower                                       |
| nbody                     | 97.0 ms                                                | 102 ms: 1.05x slower                                       |
| scimark_sparse_mat_mult   | 5.06 ms                                                | 5.35 ms: 1.06x slower                                      |
| mdp                       | 2.63 sec                                               | 2.78 sec: 1.06x slower                                     |
| regex_dna                 | 212 ms                                                 | 225 ms: 1.06x slower                                       |
| pyflate                   | 482 ms                                                 | 514 ms: 1.07x slower                                       |
| nqueens                   | 83.3 ms                                                | 89.8 ms: 1.08x slower                                      |
| python_startup            | 9.55 ms                                                | 10.3 ms: 1.08x slower                                      |
| regex_v8                  | 23.1 ms                                                | 25.1 ms: 1.09x slower                                      |
| spectral_norm             | 115 ms                                                 | 132 ms: 1.14x slower                                       |
| telco                     | 7.10 ms                                                | 8.40 ms: 1.18x slower                                      |
| hexiom                    | 6.41 ms                                                | 7.72 ms: 1.20x slower                                      |
| python_startup_no_site    | 6.94 ms                                                | 8.95 ms: 1.29x slower                                      |
| coverage                  | 72.7 ms                                                | 95.8 ms: 1.32x slower                                      |
| dask                      | 372 ms                                                 | 527 ms: 1.42x slower                                       |
| Geometric mean            | (ref)                                                  | 1.01x faster                                               |

Benchmark hidden because not significant (8): pickle_list, pprint_safe_repr, bench_mp_pool, asyncio_websockets, async_generators, async_tree_cpu_io_mixed_tg, sympy_expand, mypy2
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, django_template, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 72.82% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 0.97x