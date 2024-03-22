# Results vs. 3.12.0

- fork: gvanrossum
- ref: exp_backoff
- machine: linux-x86_64
- commit hash: 716c0c6
- commit date: 2024-03-21
- overall geometric mean: 1.24x slower
- HPT reliability: 99.93%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-716c0c6 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 304 ms: 1.11x slower                                              |
| chameleon      | 7.41 ms                                                | 6.98 ms: 1.06x faster                                             |
| docutils       | 2.77 sec                                               | 4.82 sec: 1.74x slower                                            |
| tornado_http   | 103 ms                                                 | 101 ms: 1.02x faster                                              |
| Geometric mean | (ref)                                                  | 1.16x slower                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-716c0c6 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 726 ms                                                 | 4.17 sec: 5.75x slower                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 4.55 sec: 6.28x slower                                            |
| async_tree_none            | 472 ms                                                 | 3.39 sec: 7.18x slower                                            |
| async_tree_memoization     | 578 ms                                                 | 4.37 sec: 7.56x slower                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 4.65 sec: 8.09x slower                                            |
| async_tree_none_tg         | 450 ms                                                 | 3.70 sec: 8.22x slower                                            |
| async_tree_io              | 1.16 sec                                               | 13.1 sec: 11.34x slower                                           |
| async_tree_io_tg           | 1.18 sec                                               | 13.9 sec: 11.76x slower                                           |
| Geometric mean             | (ref)                                                  | 8.04x slower                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-716c0c6 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 94.2 ms: 1.03x faster                                             |
| pidigits       | 187 ms                                                 | 190 ms: 1.01x slower                                              |
| float          | 84.7 ms                                                | 143 ms: 1.68x slower                                              |
| Geometric mean | (ref)                                                  | 1.18x slower                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-716c0c6 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 142 ms: 1.05x faster                                              |
| regex_dna      | 212 ms                                                 | 218 ms: 1.03x slower                                              |
| regex_v8       | 23.1 ms                                                | 24.2 ms: 1.04x slower                                             |
| regex_effbot   | 3.61 ms                                                | 3.81 ms: 1.06x slower                                             |
| Geometric mean | (ref)                                                  | 1.02x slower                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-716c0c6 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.10 sec: 1.11x faster                                            |
| pickle_pure_python   | 324 us                                                 | 303 us: 1.07x faster                                              |
| pickle_list          | 5.08 us                                                | 4.80 us: 1.06x faster                                             |
| pickle_dict          | 35.5 us                                                | 34.5 us: 1.03x faster                                             |
| json_loads           | 28.5 us                                                | 27.7 us: 1.03x faster                                             |
| unpickle             | 15.9 us                                                | 15.5 us: 1.02x faster                                             |
| pickle               | 11.6 us                                                | 11.6 us: 1.00x faster                                             |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                             |
| unpickle_pure_python | 230 us                                                 | 241 us: 1.05x slower                                              |
| xml_etree_process    | 61.7 ms                                                | 68.8 ms: 1.11x slower                                             |
| xml_etree_generate   | 89.2 ms                                                | 99.6 ms: 1.12x slower                                             |
| xml_etree_parse      | 159 ms                                                 | 216 ms: 1.35x slower                                              |
| xml_etree_iterparse  | 107 ms                                                 | 163 ms: 1.53x slower                                              |
| Geometric mean       | (ref)                                                  | 1.05x slower                                                      |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-716c0c6 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 9.55 ms                                                | 11.8 ms: 1.24x slower                                             |
| python_startup_no_site | 6.94 ms                                                | 10.1 ms: 1.46x slower                                             |
| Geometric mean         | (ref)                                                  | 1.34x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-716c0c6 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.1 ms: 1.07x faster                                             |
| django_template | 34.6 ms                                                | 36.0 ms: 1.04x slower                                             |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-716c0c6 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| typing_runtime_protocols   | 158 us                                                 | 111 us: 1.42x faster                                              |
| comprehensions             | 21.8 us                                                | 17.6 us: 1.24x faster                                             |
| scimark_fft                | 382 ms                                                 | 341 ms: 1.12x faster                                              |
| logging_format             | 7.23 us                                                | 6.47 us: 1.12x faster                                             |
| tomli_loads                | 2.33 sec                                               | 2.10 sec: 1.11x faster                                            |
| logging_simple             | 6.46 us                                                | 5.85 us: 1.10x faster                                             |
| raytrace                   | 312 ms                                                 | 284 ms: 1.10x faster                                              |
| scimark_monte_carlo        | 75.1 ms                                                | 69.5 ms: 1.08x faster                                             |
| crypto_pyaes               | 81.9 ms                                                | 76.3 ms: 1.07x faster                                             |
| pickle_pure_python         | 324 us                                                 | 303 us: 1.07x faster                                              |
| mako                       | 11.9 ms                                                | 11.1 ms: 1.07x faster                                             |
| chameleon                  | 7.41 ms                                                | 6.98 ms: 1.06x faster                                             |
| pickle_list                | 5.08 us                                                | 4.80 us: 1.06x faster                                             |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.79 ms: 1.06x faster                                             |
| deepcopy_reduce            | 3.35 us                                                | 3.18 us: 1.05x faster                                             |
| regex_compile              | 148 ms                                                 | 142 ms: 1.05x faster                                              |
| deepcopy_memo              | 40.7 us                                                | 39.0 us: 1.04x faster                                             |
| sympy_str                  | 300 ms                                                 | 288 ms: 1.04x faster                                              |
| chaos                      | 67.0 ms                                                | 64.5 ms: 1.04x faster                                             |
| deepcopy                   | 371 us                                                 | 358 us: 1.04x faster                                              |
| richards                   | 45.8 ms                                                | 44.3 ms: 1.04x faster                                             |
| generators                 | 31.2 ms                                                | 30.2 ms: 1.03x faster                                             |
| pprint_safe_repr           | 776 ms                                                 | 751 ms: 1.03x faster                                              |
| richards_super             | 51.5 ms                                                | 50.0 ms: 1.03x faster                                             |
| pickle_dict                | 35.5 us                                                | 34.5 us: 1.03x faster                                             |
| nbody                      | 97.0 ms                                                | 94.2 ms: 1.03x faster                                             |
| pprint_pformat             | 1.57 sec                                               | 1.52 sec: 1.03x faster                                            |
| json_loads                 | 28.5 us                                                | 27.7 us: 1.03x faster                                             |
| logging_silent             | 104 ns                                                 | 102 ns: 1.03x faster                                              |
| sympy_sum                  | 169 ms                                                 | 165 ms: 1.03x faster                                              |
| unpickle                   | 15.9 us                                                | 15.5 us: 1.02x faster                                             |
| fannkuch                   | 417 ms                                                 | 407 ms: 1.02x faster                                              |
| tornado_http               | 103 ms                                                 | 101 ms: 1.02x faster                                              |
| meteor_contest             | 112 ms                                                 | 111 ms: 1.02x faster                                              |
| gc_traversal               | 3.79 ms                                                | 3.74 ms: 1.02x faster                                             |
| pathlib                    | 19.3 ms                                                | 19.1 ms: 1.01x faster                                             |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                             |
| pickle                     | 11.6 us                                                | 11.6 us: 1.00x faster                                             |
| bench_thread_pool          | 842 us                                                 | 847 us: 1.01x slower                                              |
| dulwich_log                | 68.5 ms                                                | 69.0 ms: 1.01x slower                                             |
| sqlite_synth               | 2.83 us                                                | 2.86 us: 1.01x slower                                             |
| create_gc_cycles           | 1.48 ms                                                | 1.49 ms: 1.01x slower                                             |
| pidigits                   | 187 ms                                                 | 190 ms: 1.01x slower                                              |
| json                       | 5.26 ms                                                | 5.32 ms: 1.01x slower                                             |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                             |
| scimark_sor                | 129 ms                                                 | 131 ms: 1.02x slower                                              |
| pyflate                    | 482 ms                                                 | 493 ms: 1.02x slower                                              |
| regex_dna                  | 212 ms                                                 | 218 ms: 1.03x slower                                              |
| sympy_expand               | 478 ms                                                 | 491 ms: 1.03x slower                                              |
| sqlglot_normalize          | 110 ms                                                 | 114 ms: 1.03x slower                                              |
| asyncio_websockets         | 551 ms                                                 | 570 ms: 1.03x slower                                              |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.85 sec: 1.04x slower                                            |
| asyncio_tcp                | 491 ms                                                 | 509 ms: 1.04x slower                                              |
| django_template            | 34.6 ms                                                | 36.0 ms: 1.04x slower                                             |
| regex_v8                   | 23.1 ms                                                | 24.2 ms: 1.04x slower                                             |
| unpickle_pure_python       | 230 us                                                 | 241 us: 1.05x slower                                              |
| deltablue                  | 3.72 ms                                                | 3.90 ms: 1.05x slower                                             |
| regex_effbot               | 3.61 ms                                                | 3.81 ms: 1.06x slower                                             |
| sqlglot_parse              | 1.36 ms                                                | 1.44 ms: 1.06x slower                                             |
| nqueens                    | 83.3 ms                                                | 88.4 ms: 1.06x slower                                             |
| sqlglot_transpile          | 1.68 ms                                                | 1.80 ms: 1.07x slower                                             |
| sqlglot_optimize           | 54.8 ms                                                | 58.8 ms: 1.07x slower                                             |
| mdp                        | 2.63 sec                                               | 2.86 sec: 1.09x slower                                            |
| hexiom                     | 6.41 ms                                                | 6.96 ms: 1.09x slower                                             |
| scimark_lu                 | 118 ms                                                 | 129 ms: 1.09x slower                                              |
| gunicorn                   | 1.24 ms                                                | 1.36 ms: 1.10x slower                                             |
| aiohttp                    | 1.15 ms                                                | 1.27 ms: 1.10x slower                                             |
| 2to3                       | 274 ms                                                 | 304 ms: 1.11x slower                                              |
| go                         | 139 ms                                                 | 155 ms: 1.11x slower                                              |
| xml_etree_process          | 61.7 ms                                                | 68.8 ms: 1.11x slower                                             |
| xml_etree_generate         | 89.2 ms                                                | 99.6 ms: 1.12x slower                                             |
| telco                      | 7.10 ms                                                | 8.43 ms: 1.19x slower                                             |
| async_generators           | 463 ms                                                 | 556 ms: 1.20x slower                                              |
| python_startup             | 9.55 ms                                                | 11.8 ms: 1.24x slower                                             |
| pycparser                  | 1.18 sec                                               | 1.47 sec: 1.25x slower                                            |
| coverage                   | 72.7 ms                                                | 96.9 ms: 1.33x slower                                             |
| xml_etree_parse            | 159 ms                                                 | 216 ms: 1.35x slower                                              |
| python_startup_no_site     | 6.94 ms                                                | 10.1 ms: 1.46x slower                                             |
| xml_etree_iterparse        | 107 ms                                                 | 163 ms: 1.53x slower                                              |
| float                      | 84.7 ms                                                | 143 ms: 1.68x slower                                              |
| unpack_sequence            | 54.0 ns                                                | 91.8 ns: 1.70x slower                                             |
| docutils                   | 2.77 sec                                               | 4.82 sec: 1.74x slower                                            |
| dask                       | 372 ms                                                 | 759 ms: 2.04x slower                                              |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 4.17 sec: 5.75x slower                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 4.55 sec: 6.28x slower                                            |
| async_tree_none            | 472 ms                                                 | 3.39 sec: 7.18x slower                                            |
| async_tree_memoization     | 578 ms                                                 | 4.37 sec: 7.56x slower                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 4.65 sec: 8.09x slower                                            |
| async_tree_none_tg         | 450 ms                                                 | 3.70 sec: 8.22x slower                                            |
| async_tree_io              | 1.16 sec                                               | 13.1 sec: 11.34x slower                                           |
| async_tree_io_tg           | 1.18 sec                                               | 13.9 sec: 11.76x slower                                           |
| Geometric mean             | (ref)                                                  | 1.24x slower                                                      |

Benchmark hidden because not significant (5): unpickle_list, sympy_integrate, bench_mp_pool, spectral_norm, mypy2
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240321-3.13.0a5+-716c0c6-JIT/bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-716c0c6.json: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 99.93% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x


# Memory

- memory change: 1.06x