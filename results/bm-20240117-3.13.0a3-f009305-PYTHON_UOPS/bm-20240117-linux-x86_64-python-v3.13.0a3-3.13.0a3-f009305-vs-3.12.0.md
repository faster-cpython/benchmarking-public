
# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a3
- machine: linux-x86_64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 282 ms: 1.03x slower                                       |
| chameleon      | 7.41 ms                                                | 7.24 ms: 1.02x faster                                      |
| docutils       | 2.77 sec                                               | 2.71 sec: 1.02x faster                                     |
| tornado_http   | 103 ms                                                 | 97.8 ms: 1.05x faster                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|---------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none           | 472 ms                                                 | 448 ms: 1.05x faster                                       |
| async_tree_memoization_tg | 575 ms                                                 | 587 ms: 1.02x slower                                       |
| async_tree_io_tg          | 1.18 sec                                               | 1.21 sec: 1.02x slower                                     |
| async_tree_io             | 1.16 sec                                               | 1.20 sec: 1.04x slower                                     |
| Geometric mean            | (ref)                                                  | 1.00x slower                                               |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 187 ms                                                 | 190 ms: 1.01x slower                                       |
| float          | 84.7 ms                                                | 94.1 ms: 1.11x slower                                      |
| nbody          | 97.0 ms                                                | 119 ms: 1.23x slower                                       |
| Geometric mean | (ref)                                                  | 1.11x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 153 ms: 1.03x slower                                       |
| regex_effbot   | 3.61 ms                                                | 3.74 ms: 1.04x slower                                      |
| regex_v8       | 23.1 ms                                                | 24.6 ms: 1.06x slower                                      |
| regex_dna      | 212 ms                                                 | 228 ms: 1.07x slower                                       |
| Geometric mean | (ref)                                                  | 1.05x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 324 us                                                 | 301 us: 1.08x faster                                       |
| unpickle_list        | 5.29 us                                                | 5.14 us: 1.03x faster                                      |
| pickle_dict          | 35.5 us                                                | 35.0 us: 1.01x faster                                      |
| json_loads           | 28.5 us                                                | 28.2 us: 1.01x faster                                      |
| xml_etree_process    | 61.7 ms                                                | 61.1 ms: 1.01x faster                                      |
| xml_etree_generate   | 89.2 ms                                                | 89.5 ms: 1.00x slower                                      |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                      |
| unpickle             | 15.9 us                                                | 16.1 us: 1.02x slower                                      |
| unpickle_pure_python | 230 us                                                 | 234 us: 1.02x slower                                       |
| pickle               | 11.6 us                                                | 11.8 us: 1.02x slower                                      |
| pickle_list          | 5.08 us                                                | 5.24 us: 1.03x slower                                      |
| xml_etree_iterparse  | 107 ms                                                 | 112 ms: 1.05x slower                                       |
| tomli_loads          | 2.33 sec                                               | 2.61 sec: 1.12x slower                                     |
| Geometric mean       | (ref)                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 9.55 ms                                                | 10.1 ms: 1.06x slower                                      |
| python_startup_no_site | 6.94 ms                                                | 8.72 ms: 1.26x slower                                      |
| Geometric mean         | (ref)                                                  | 1.15x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 11.9 ms                                                | 14.2 ms: 1.19x slower                                      |

All benchmarks:
===============

| Benchmark                 | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|---------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols  | 158 us                                                 | 117 us: 1.35x faster                                       |
| unpack_sequence           | 54.0 ns                                                | 42.4 ns: 1.27x faster                                      |
| pickle_pure_python        | 324 us                                                 | 301 us: 1.08x faster                                       |
| generators                | 31.2 ms                                                | 29.3 ms: 1.06x faster                                      |
| deepcopy_reduce           | 3.35 us                                                | 3.15 us: 1.06x faster                                      |
| pathlib                   | 19.3 ms                                                | 18.3 ms: 1.06x faster                                      |
| async_tree_none           | 472 ms                                                 | 448 ms: 1.05x faster                                       |
| tornado_http              | 103 ms                                                 | 97.8 ms: 1.05x faster                                      |
| sympy_sum                 | 169 ms                                                 | 161 ms: 1.05x faster                                       |
| logging_simple            | 6.46 us                                                | 6.20 us: 1.04x faster                                      |
| raytrace                  | 312 ms                                                 | 302 ms: 1.03x faster                                       |
| deepcopy                  | 371 us                                                 | 359 us: 1.03x faster                                       |
| unpickle_list             | 5.29 us                                                | 5.14 us: 1.03x faster                                      |
| gc_traversal              | 3.79 ms                                                | 3.69 ms: 1.03x faster                                      |
| chameleon                 | 7.41 ms                                                | 7.24 ms: 1.02x faster                                      |
| logging_format            | 7.23 us                                                | 7.07 us: 1.02x faster                                      |
| logging_silent            | 104 ns                                                 | 102 ns: 1.02x faster                                       |
| coroutines                | 23.2 ms                                                | 22.7 ms: 1.02x faster                                      |
| docutils                  | 2.77 sec                                               | 2.71 sec: 1.02x faster                                     |
| sqlglot_parse             | 1.36 ms                                                | 1.34 ms: 1.02x faster                                      |
| pickle_dict               | 35.5 us                                                | 35.0 us: 1.01x faster                                      |
| json                      | 5.26 ms                                                | 5.19 ms: 1.01x faster                                      |
| sympy_integrate           | 21.4 ms                                                | 21.1 ms: 1.01x faster                                      |
| json_loads                | 28.5 us                                                | 28.2 us: 1.01x faster                                      |
| xml_etree_process         | 61.7 ms                                                | 61.1 ms: 1.01x faster                                      |
| comprehensions            | 21.8 us                                                | 21.6 us: 1.01x faster                                      |
| sqlglot_transpile         | 1.68 ms                                                | 1.67 ms: 1.01x faster                                      |
| async_generators          | 463 ms                                                 | 461 ms: 1.00x faster                                       |
| asyncio_tcp               | 491 ms                                                 | 492 ms: 1.00x slower                                       |
| xml_etree_generate        | 89.2 ms                                                | 89.5 ms: 1.00x slower                                      |
| create_gc_cycles          | 1.48 ms                                                | 1.49 ms: 1.01x slower                                      |
| dulwich_log               | 68.5 ms                                                | 69.0 ms: 1.01x slower                                      |
| bench_thread_pool         | 842 us                                                 | 848 us: 1.01x slower                                       |
| json_dumps                | 10.4 ms                                                | 10.5 ms: 1.01x slower                                      |
| scimark_lu                | 118 ms                                                 | 119 ms: 1.01x slower                                       |
| meteor_contest            | 112 ms                                                 | 114 ms: 1.01x slower                                       |
| pidigits                  | 187 ms                                                 | 190 ms: 1.01x slower                                       |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.81 sec: 1.01x slower                                     |
| pycparser                 | 1.18 sec                                               | 1.19 sec: 1.01x slower                                     |
| mdp                       | 2.63 sec                                               | 2.67 sec: 1.01x slower                                     |
| unpickle                  | 15.9 us                                                | 16.1 us: 1.02x slower                                      |
| unpickle_pure_python      | 230 us                                                 | 234 us: 1.02x slower                                       |
| pickle                    | 11.6 us                                                | 11.8 us: 1.02x slower                                      |
| async_tree_memoization_tg | 575 ms                                                 | 587 ms: 1.02x slower                                       |
| async_tree_io_tg          | 1.18 sec                                               | 1.21 sec: 1.02x slower                                     |
| 2to3                      | 274 ms                                                 | 282 ms: 1.03x slower                                       |
| sqlite_synth              | 2.83 us                                                | 2.91 us: 1.03x slower                                      |
| regex_compile             | 148 ms                                                 | 153 ms: 1.03x slower                                       |
| pickle_list               | 5.08 us                                                | 5.24 us: 1.03x slower                                      |
| scimark_sor               | 129 ms                                                 | 134 ms: 1.04x slower                                       |
| sympy_expand              | 478 ms                                                 | 495 ms: 1.04x slower                                       |
| regex_effbot              | 3.61 ms                                                | 3.74 ms: 1.04x slower                                      |
| crypto_pyaes              | 81.9 ms                                                | 85.0 ms: 1.04x slower                                      |
| async_tree_io             | 1.16 sec                                               | 1.20 sec: 1.04x slower                                     |
| xml_etree_iterparse       | 107 ms                                                 | 112 ms: 1.05x slower                                       |
| pprint_safe_repr          | 776 ms                                                 | 816 ms: 1.05x slower                                       |
| richards                  | 45.8 ms                                                | 48.3 ms: 1.05x slower                                      |
| sqlglot_normalize         | 110 ms                                                 | 116 ms: 1.06x slower                                       |
| python_startup            | 9.55 ms                                                | 10.1 ms: 1.06x slower                                      |
| richards_super            | 51.5 ms                                                | 54.7 ms: 1.06x slower                                      |
| regex_v8                  | 23.1 ms                                                | 24.6 ms: 1.06x slower                                      |
| sqlglot_optimize          | 54.8 ms                                                | 58.4 ms: 1.07x slower                                      |
| regex_dna                 | 212 ms                                                 | 228 ms: 1.07x slower                                       |
| pprint_pformat            | 1.57 sec                                               | 1.70 sec: 1.08x slower                                     |
| scimark_monte_carlo       | 75.1 ms                                                | 81.4 ms: 1.08x slower                                      |
| fannkuch                  | 417 ms                                                 | 454 ms: 1.09x slower                                       |
| chaos                     | 67.0 ms                                                | 73.6 ms: 1.10x slower                                      |
| pyflate                   | 482 ms                                                 | 536 ms: 1.11x slower                                       |
| float                     | 84.7 ms                                                | 94.1 ms: 1.11x slower                                      |
| go                        | 139 ms                                                 | 156 ms: 1.12x slower                                       |
| tomli_loads               | 2.33 sec                                               | 2.61 sec: 1.12x slower                                     |
| nqueens                   | 83.3 ms                                                | 95.4 ms: 1.15x slower                                      |
| mako                      | 11.9 ms                                                | 14.2 ms: 1.19x slower                                      |
| scimark_fft               | 382 ms                                                 | 457 ms: 1.20x slower                                       |
| telco                     | 7.10 ms                                                | 8.62 ms: 1.21x slower                                      |
| nbody                     | 97.0 ms                                                | 119 ms: 1.23x slower                                       |
| python_startup_no_site    | 6.94 ms                                                | 8.72 ms: 1.26x slower                                      |
| scimark_sparse_mat_mult   | 5.06 ms                                                | 6.38 ms: 1.26x slower                                      |
| deltablue                 | 3.72 ms                                                | 4.85 ms: 1.31x slower                                      |
| coverage                  | 72.7 ms                                                | 95.0 ms: 1.31x slower                                      |
| spectral_norm             | 115 ms                                                 | 154 ms: 1.34x slower                                       |
| hexiom                    | 6.41 ms                                                | 8.65 ms: 1.35x slower                                      |
| Geometric mean            | (ref)                                                  | 1.03x slower                                               |

Benchmark hidden because not significant (11): async_tree_cpu_io_mixed, dask, async_tree_memoization, async_tree_none_tg, xml_etree_parse, bench_mp_pool, asyncio_websockets, deepcopy_memo, async_tree_cpu_io_mixed_tg, sympy_str, mypy2
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, django_template, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 0.93x