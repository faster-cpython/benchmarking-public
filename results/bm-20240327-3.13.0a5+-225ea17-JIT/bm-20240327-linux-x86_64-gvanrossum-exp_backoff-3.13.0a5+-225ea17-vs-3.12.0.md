# Results vs. 3.12.0

- fork: gvanrossum
- ref: exp_backoff
- machine: linux-x86_64
- commit hash: 225ea17
- commit date: 2024-03-27
- overall geometric mean: 1.00x faster
- HPT reliability: 54.94%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-225ea17 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 279 ms: 1.02x slower                                              |
| chameleon      | 7.41 ms                                                | 7.21 ms: 1.03x faster                                             |
| docutils       | 2.77 sec                                               | 2.89 sec: 1.05x slower                                            |
| tornado_http   | 103 ms                                                 | 96.6 ms: 1.06x faster                                             |
| Geometric mean | (ref)                                                  | 1.01x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-225ea17 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 341 ms: 1.32x faster                                              |
| async_tree_io_tg           | 1.18 sec                                               | 923 ms: 1.28x faster                                              |
| async_tree_memoization_tg  | 575 ms                                                 | 451 ms: 1.27x faster                                              |
| async_tree_memoization     | 578 ms                                                 | 459 ms: 1.26x faster                                              |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 583 ms: 1.24x faster                                              |
| async_tree_io              | 1.16 sec                                               | 942 ms: 1.23x faster                                              |
| async_tree_none            | 472 ms                                                 | 390 ms: 1.21x faster                                              |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 601 ms: 1.21x faster                                              |
| Geometric mean             | (ref)                                                  | 1.25x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-225ea17 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 84.7 ms                                                | 77.8 ms: 1.09x faster                                             |
| nbody          | 97.0 ms                                                | 91.9 ms: 1.05x faster                                             |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                  | 1.04x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-225ea17 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 146 ms: 1.02x faster                                              |
| regex_effbot   | 3.61 ms                                                | 3.81 ms: 1.05x slower                                             |
| regex_dna      | 212 ms                                                 | 229 ms: 1.08x slower                                              |
| regex_v8       | 23.1 ms                                                | 26.1 ms: 1.13x slower                                             |
| Geometric mean | (ref)                                                  | 1.06x slower                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-225ea17 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.07 sec: 1.13x faster                                            |
| pickle_pure_python   | 324 us                                                 | 308 us: 1.05x faster                                              |
| xml_etree_process    | 61.7 ms                                                | 60.5 ms: 1.02x faster                                             |
| unpickle_list        | 5.29 us                                                | 5.24 us: 1.01x faster                                             |
| xml_etree_generate   | 89.2 ms                                                | 88.6 ms: 1.01x faster                                             |
| xml_etree_iterparse  | 107 ms                                                 | 108 ms: 1.01x slower                                              |
| xml_etree_parse      | 159 ms                                                 | 162 ms: 1.02x slower                                              |
| json_dumps           | 10.4 ms                                                | 10.6 ms: 1.02x slower                                             |
| json_loads           | 28.5 us                                                | 29.1 us: 1.02x slower                                             |
| unpickle             | 15.9 us                                                | 16.4 us: 1.04x slower                                             |
| pickle_list          | 5.08 us                                                | 5.30 us: 1.04x slower                                             |
| pickle_dict          | 35.5 us                                                | 37.2 us: 1.05x slower                                             |
| pickle               | 11.6 us                                                | 12.3 us: 1.06x slower                                             |
| unpickle_pure_python | 230 us                                                 | 246 us: 1.07x slower                                              |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-225ea17 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 9.55 ms                                                | 11.1 ms: 1.16x slower                                             |
| python_startup_no_site | 6.94 ms                                                | 9.55 ms: 1.38x slower                                             |
| Geometric mean         | (ref)                                                  | 1.26x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-225ea17 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.8 ms: 1.11x faster                                             |
| django_template | 34.6 ms                                                | 35.9 ms: 1.04x slower                                             |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-225ea17 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| typing_runtime_protocols   | 158 us                                                 | 115 us: 1.37x faster                                              |
| async_tree_none_tg         | 450 ms                                                 | 341 ms: 1.32x faster                                              |
| async_tree_io_tg           | 1.18 sec                                               | 923 ms: 1.28x faster                                              |
| async_tree_memoization_tg  | 575 ms                                                 | 451 ms: 1.27x faster                                              |
| async_tree_memoization     | 578 ms                                                 | 459 ms: 1.26x faster                                              |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 583 ms: 1.24x faster                                              |
| async_tree_io              | 1.16 sec                                               | 942 ms: 1.23x faster                                              |
| async_tree_none            | 472 ms                                                 | 390 ms: 1.21x faster                                              |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 601 ms: 1.21x faster                                              |
| comprehensions             | 21.8 us                                                | 18.2 us: 1.20x faster                                             |
| tomli_loads                | 2.33 sec                                               | 2.07 sec: 1.13x faster                                            |
| mako                       | 11.9 ms                                                | 10.8 ms: 1.11x faster                                             |
| scimark_fft                | 382 ms                                                 | 348 ms: 1.10x faster                                              |
| crypto_pyaes               | 81.9 ms                                                | 74.9 ms: 1.09x faster                                             |
| float                      | 84.7 ms                                                | 77.8 ms: 1.09x faster                                             |
| logging_format             | 7.23 us                                                | 6.68 us: 1.08x faster                                             |
| logging_simple             | 6.46 us                                                | 5.98 us: 1.08x faster                                             |
| fannkuch                   | 417 ms                                                 | 389 ms: 1.07x faster                                              |
| raytrace                   | 312 ms                                                 | 293 ms: 1.07x faster                                              |
| tornado_http               | 103 ms                                                 | 96.6 ms: 1.06x faster                                             |
| chaos                      | 67.0 ms                                                | 63.3 ms: 1.06x faster                                             |
| nbody                      | 97.0 ms                                                | 91.9 ms: 1.05x faster                                             |
| pickle_pure_python         | 324 us                                                 | 308 us: 1.05x faster                                              |
| scimark_monte_carlo        | 75.1 ms                                                | 71.6 ms: 1.05x faster                                             |
| deepcopy_reduce            | 3.35 us                                                | 3.21 us: 1.04x faster                                             |
| deepcopy                   | 371 us                                                 | 356 us: 1.04x faster                                              |
| pprint_safe_repr           | 776 ms                                                 | 748 ms: 1.04x faster                                              |
| generators                 | 31.2 ms                                                | 30.2 ms: 1.04x faster                                             |
| deepcopy_memo              | 40.7 us                                                | 39.3 us: 1.04x faster                                             |
| chameleon                  | 7.41 ms                                                | 7.21 ms: 1.03x faster                                             |
| sympy_str                  | 300 ms                                                 | 293 ms: 1.02x faster                                              |
| xml_etree_process          | 61.7 ms                                                | 60.5 ms: 1.02x faster                                             |
| pprint_pformat             | 1.57 sec                                               | 1.54 sec: 1.02x faster                                            |
| pathlib                    | 19.3 ms                                                | 19.0 ms: 1.02x faster                                             |
| regex_compile              | 148 ms                                                 | 146 ms: 1.02x faster                                              |
| sqlglot_parse              | 1.36 ms                                                | 1.34 ms: 1.02x faster                                             |
| sympy_sum                  | 169 ms                                                 | 167 ms: 1.01x faster                                              |
| meteor_contest             | 112 ms                                                 | 111 ms: 1.01x faster                                              |
| sqlglot_transpile          | 1.68 ms                                                | 1.66 ms: 1.01x faster                                             |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.00 ms: 1.01x faster                                             |
| unpickle_list              | 5.29 us                                                | 5.24 us: 1.01x faster                                             |
| xml_etree_generate         | 89.2 ms                                                | 88.6 ms: 1.01x faster                                             |
| pyflate                    | 482 ms                                                 | 485 ms: 1.01x slower                                              |
| mdp                        | 2.63 sec                                               | 2.65 sec: 1.01x slower                                            |
| logging_silent             | 104 ns                                                 | 105 ns: 1.01x slower                                              |
| async_generators           | 463 ms                                                 | 467 ms: 1.01x slower                                              |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                              |
| sqlite_synth               | 2.83 us                                                | 2.87 us: 1.01x slower                                             |
| xml_etree_iterparse        | 107 ms                                                 | 108 ms: 1.01x slower                                              |
| spectral_norm              | 115 ms                                                 | 117 ms: 1.02x slower                                              |
| xml_etree_parse            | 159 ms                                                 | 162 ms: 1.02x slower                                              |
| bench_thread_pool          | 842 us                                                 | 856 us: 1.02x slower                                              |
| 2to3                       | 274 ms                                                 | 279 ms: 1.02x slower                                              |
| json_dumps                 | 10.4 ms                                                | 10.6 ms: 1.02x slower                                             |
| sqlglot_normalize          | 110 ms                                                 | 112 ms: 1.02x slower                                              |
| json_loads                 | 28.5 us                                                | 29.1 us: 1.02x slower                                             |
| sympy_integrate            | 21.4 ms                                                | 21.9 ms: 1.02x slower                                             |
| richards_super             | 51.5 ms                                                | 52.8 ms: 1.02x slower                                             |
| richards                   | 45.8 ms                                                | 47.0 ms: 1.03x slower                                             |
| asyncio_websockets         | 551 ms                                                 | 570 ms: 1.03x slower                                              |
| dulwich_log                | 68.5 ms                                                | 70.8 ms: 1.03x slower                                             |
| unpickle                   | 15.9 us                                                | 16.4 us: 1.04x slower                                             |
| scimark_sor                | 129 ms                                                 | 134 ms: 1.04x slower                                              |
| asyncio_tcp                | 491 ms                                                 | 508 ms: 1.04x slower                                              |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.85 sec: 1.04x slower                                            |
| django_template            | 34.6 ms                                                | 35.9 ms: 1.04x slower                                             |
| gc_traversal               | 3.79 ms                                                | 3.95 ms: 1.04x slower                                             |
| sympy_expand               | 478 ms                                                 | 497 ms: 1.04x slower                                              |
| pickle_list                | 5.08 us                                                | 5.30 us: 1.04x slower                                             |
| json                       | 5.26 ms                                                | 5.50 ms: 1.05x slower                                             |
| docutils                   | 2.77 sec                                               | 2.89 sec: 1.05x slower                                            |
| pickle_dict                | 35.5 us                                                | 37.2 us: 1.05x slower                                             |
| regex_effbot               | 3.61 ms                                                | 3.81 ms: 1.05x slower                                             |
| aiohttp                    | 1.15 ms                                                | 1.21 ms: 1.06x slower                                             |
| gunicorn                   | 1.24 ms                                                | 1.31 ms: 1.06x slower                                             |
| sqlglot_optimize           | 54.8 ms                                                | 58.0 ms: 1.06x slower                                             |
| pycparser                  | 1.18 sec                                               | 1.25 sec: 1.06x slower                                            |
| deltablue                  | 3.72 ms                                                | 3.94 ms: 1.06x slower                                             |
| pickle                     | 11.6 us                                                | 12.3 us: 1.06x slower                                             |
| nqueens                    | 83.3 ms                                                | 88.7 ms: 1.06x slower                                             |
| unpickle_pure_python       | 230 us                                                 | 246 us: 1.07x slower                                              |
| regex_dna                  | 212 ms                                                 | 229 ms: 1.08x slower                                              |
| go                         | 139 ms                                                 | 154 ms: 1.10x slower                                              |
| hexiom                     | 6.41 ms                                                | 7.12 ms: 1.11x slower                                             |
| regex_v8                   | 23.1 ms                                                | 26.1 ms: 1.13x slower                                             |
| scimark_lu                 | 118 ms                                                 | 134 ms: 1.13x slower                                              |
| create_gc_cycles           | 1.48 ms                                                | 1.70 ms: 1.15x slower                                             |
| python_startup             | 9.55 ms                                                | 11.1 ms: 1.16x slower                                             |
| telco                      | 7.10 ms                                                | 8.82 ms: 1.24x slower                                             |
| coverage                   | 72.7 ms                                                | 97.9 ms: 1.35x slower                                             |
| python_startup_no_site     | 6.94 ms                                                | 9.55 ms: 1.38x slower                                             |
| unpack_sequence            | 54.0 ns                                                | 86.4 ns: 1.60x slower                                             |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                      |

Benchmark hidden because not significant (4): mypy2, coroutines, bench_mp_pool, dask
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240327-3.13.0a5+-225ea17-JIT/bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-225ea17.json: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 54.94% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 1.03x