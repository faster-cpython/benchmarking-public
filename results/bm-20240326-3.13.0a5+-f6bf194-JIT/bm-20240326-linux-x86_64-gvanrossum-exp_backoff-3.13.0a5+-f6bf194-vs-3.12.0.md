# Results vs. 3.12.0

- fork: gvanrossum
- ref: exp_backoff
- machine: linux-x86_64
- commit hash: f6bf194
- commit date: 2024-03-26
- overall geometric mean: 1.02x faster
- HPT reliability: 85.87%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-f6bf194 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 279 ms: 1.02x slower                                              |
| chameleon      | 7.41 ms                                                | 7.17 ms: 1.03x faster                                             |
| docutils       | 2.77 sec                                               | 2.84 sec: 1.02x slower                                            |
| tornado_http   | 103 ms                                                 | 96.5 ms: 1.06x faster                                             |
| Geometric mean | (ref)                                                  | 1.01x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-f6bf194 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 341 ms: 1.32x faster                                              |
| async_tree_io_tg           | 1.18 sec                                               | 918 ms: 1.29x faster                                              |
| async_tree_memoization_tg  | 575 ms                                                 | 448 ms: 1.28x faster                                              |
| async_tree_memoization     | 578 ms                                                 | 459 ms: 1.26x faster                                              |
| async_tree_io              | 1.16 sec                                               | 920 ms: 1.26x faster                                              |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 583 ms: 1.24x faster                                              |
| async_tree_none            | 472 ms                                                 | 386 ms: 1.22x faster                                              |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 599 ms: 1.21x faster                                              |
| Geometric mean             | (ref)                                                  | 1.26x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-f6bf194 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 84.7 ms                                                | 77.5 ms: 1.09x faster                                             |
| nbody          | 97.0 ms                                                | 92.2 ms: 1.05x faster                                             |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                  | 1.04x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-f6bf194 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 139 ms: 1.07x faster                                              |
| regex_effbot   | 3.61 ms                                                | 3.77 ms: 1.04x slower                                             |
| regex_dna      | 212 ms                                                 | 227 ms: 1.07x slower                                              |
| regex_v8       | 23.1 ms                                                | 25.7 ms: 1.11x slower                                             |
| Geometric mean | (ref)                                                  | 1.04x slower                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-f6bf194 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.06 sec: 1.13x faster                                            |
| pickle_pure_python   | 324 us                                                 | 305 us: 1.06x faster                                              |
| pickle_dict          | 35.5 us                                                | 33.5 us: 1.06x faster                                             |
| xml_etree_process    | 61.7 ms                                                | 60.1 ms: 1.03x faster                                             |
| pickle_list          | 5.08 us                                                | 4.95 us: 1.03x faster                                             |
| xml_etree_generate   | 89.2 ms                                                | 86.9 ms: 1.03x faster                                             |
| unpickle_pure_python | 230 us                                                 | 232 us: 1.01x slower                                              |
| json_loads           | 28.5 us                                                | 28.7 us: 1.01x slower                                             |
| xml_etree_parse      | 159 ms                                                 | 161 ms: 1.01x slower                                              |
| json_dumps           | 10.4 ms                                                | 10.6 ms: 1.02x slower                                             |
| unpickle_list        | 5.29 us                                                | 5.43 us: 1.03x slower                                             |
| pickle               | 11.6 us                                                | 12.0 us: 1.04x slower                                             |
| unpickle             | 15.9 us                                                | 17.0 us: 1.07x slower                                             |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                      |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-f6bf194 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 9.55 ms                                                | 11.0 ms: 1.15x slower                                             |
| python_startup_no_site | 6.94 ms                                                | 9.48 ms: 1.37x slower                                             |
| Geometric mean         | (ref)                                                  | 1.25x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-f6bf194 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.9 ms: 1.09x faster                                             |
| django_template | 34.6 ms                                                | 35.8 ms: 1.03x slower                                             |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-f6bf194 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| typing_runtime_protocols   | 158 us                                                 | 114 us: 1.38x faster                                              |
| async_tree_none_tg         | 450 ms                                                 | 341 ms: 1.32x faster                                              |
| async_tree_io_tg           | 1.18 sec                                               | 918 ms: 1.29x faster                                              |
| async_tree_memoization_tg  | 575 ms                                                 | 448 ms: 1.28x faster                                              |
| async_tree_memoization     | 578 ms                                                 | 459 ms: 1.26x faster                                              |
| async_tree_io              | 1.16 sec                                               | 920 ms: 1.26x faster                                              |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 583 ms: 1.24x faster                                              |
| async_tree_none            | 472 ms                                                 | 386 ms: 1.22x faster                                              |
| comprehensions             | 21.8 us                                                | 18.0 us: 1.21x faster                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 599 ms: 1.21x faster                                              |
| raytrace                   | 312 ms                                                 | 275 ms: 1.13x faster                                              |
| tomli_loads                | 2.33 sec                                               | 2.06 sec: 1.13x faster                                            |
| deltablue                  | 3.72 ms                                                | 3.32 ms: 1.12x faster                                             |
| scimark_fft                | 382 ms                                                 | 344 ms: 1.11x faster                                              |
| mako                       | 11.9 ms                                                | 10.9 ms: 1.09x faster                                             |
| float                      | 84.7 ms                                                | 77.5 ms: 1.09x faster                                             |
| logging_format             | 7.23 us                                                | 6.66 us: 1.09x faster                                             |
| crypto_pyaes               | 81.9 ms                                                | 75.5 ms: 1.08x faster                                             |
| mypy2                      | 830 ms                                                 | 766 ms: 1.08x faster                                              |
| logging_simple             | 6.46 us                                                | 6.02 us: 1.07x faster                                             |
| regex_compile              | 148 ms                                                 | 139 ms: 1.07x faster                                              |
| tornado_http               | 103 ms                                                 | 96.5 ms: 1.06x faster                                             |
| pickle_pure_python         | 324 us                                                 | 305 us: 1.06x faster                                              |
| deepcopy_reduce            | 3.35 us                                                | 3.15 us: 1.06x faster                                             |
| pickle_dict                | 35.5 us                                                | 33.5 us: 1.06x faster                                             |
| chaos                      | 67.0 ms                                                | 63.3 ms: 1.06x faster                                             |
| scimark_monte_carlo        | 75.1 ms                                                | 71.3 ms: 1.05x faster                                             |
| nbody                      | 97.0 ms                                                | 92.2 ms: 1.05x faster                                             |
| unpack_sequence            | 54.0 ns                                                | 51.5 ns: 1.05x faster                                             |
| deepcopy_memo              | 40.7 us                                                | 39.0 us: 1.04x faster                                             |
| fannkuch                   | 417 ms                                                 | 401 ms: 1.04x faster                                              |
| richards                   | 45.8 ms                                                | 44.1 ms: 1.04x faster                                             |
| sympy_sum                  | 169 ms                                                 | 163 ms: 1.04x faster                                              |
| sympy_str                  | 300 ms                                                 | 289 ms: 1.04x faster                                              |
| scimark_sor                | 129 ms                                                 | 124 ms: 1.04x faster                                              |
| chameleon                  | 7.41 ms                                                | 7.17 ms: 1.03x faster                                             |
| deepcopy                   | 371 us                                                 | 359 us: 1.03x faster                                              |
| generators                 | 31.2 ms                                                | 30.3 ms: 1.03x faster                                             |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.03x faster                                              |
| xml_etree_process          | 61.7 ms                                                | 60.1 ms: 1.03x faster                                             |
| pickle_list                | 5.08 us                                                | 4.95 us: 1.03x faster                                             |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.93 ms: 1.03x faster                                             |
| xml_etree_generate         | 89.2 ms                                                | 86.9 ms: 1.03x faster                                             |
| sqlglot_parse              | 1.36 ms                                                | 1.33 ms: 1.02x faster                                             |
| pathlib                    | 19.3 ms                                                | 18.9 ms: 1.02x faster                                             |
| sqlglot_transpile          | 1.68 ms                                                | 1.65 ms: 1.02x faster                                             |
| pprint_safe_repr           | 776 ms                                                 | 762 ms: 1.02x faster                                              |
| richards_super             | 51.5 ms                                                | 50.7 ms: 1.02x faster                                             |
| meteor_contest             | 112 ms                                                 | 111 ms: 1.01x faster                                              |
| sympy_integrate            | 21.4 ms                                                | 21.3 ms: 1.00x faster                                             |
| pyflate                    | 482 ms                                                 | 486 ms: 1.01x slower                                              |
| unpickle_pure_python       | 230 us                                                 | 232 us: 1.01x slower                                              |
| json_loads                 | 28.5 us                                                | 28.7 us: 1.01x slower                                             |
| mdp                        | 2.63 sec                                               | 2.66 sec: 1.01x slower                                            |
| async_generators           | 463 ms                                                 | 468 ms: 1.01x slower                                              |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                              |
| xml_etree_parse            | 159 ms                                                 | 161 ms: 1.01x slower                                              |
| spectral_norm              | 115 ms                                                 | 116 ms: 1.01x slower                                              |
| bench_thread_pool          | 842 us                                                 | 852 us: 1.01x slower                                              |
| dask                       | 372 ms                                                 | 376 ms: 1.01x slower                                              |
| 2to3                       | 274 ms                                                 | 279 ms: 1.02x slower                                              |
| gc_traversal               | 3.79 ms                                                | 3.86 ms: 1.02x slower                                             |
| sqlglot_normalize          | 110 ms                                                 | 112 ms: 1.02x slower                                              |
| coroutines                 | 23.2 ms                                                | 23.6 ms: 1.02x slower                                             |
| sqlite_synth               | 2.83 us                                                | 2.89 us: 1.02x slower                                             |
| json_dumps                 | 10.4 ms                                                | 10.6 ms: 1.02x slower                                             |
| docutils                   | 2.77 sec                                               | 2.84 sec: 1.02x slower                                            |
| unpickle_list              | 5.29 us                                                | 5.43 us: 1.03x slower                                             |
| sympy_expand               | 478 ms                                                 | 491 ms: 1.03x slower                                              |
| asyncio_tcp                | 491 ms                                                 | 506 ms: 1.03x slower                                              |
| json                       | 5.26 ms                                                | 5.42 ms: 1.03x slower                                             |
| django_template            | 34.6 ms                                                | 35.8 ms: 1.03x slower                                             |
| asyncio_websockets         | 551 ms                                                 | 570 ms: 1.03x slower                                              |
| sqlglot_optimize           | 54.8 ms                                                | 56.7 ms: 1.03x slower                                             |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.85 sec: 1.04x slower                                            |
| pickle                     | 11.6 us                                                | 12.0 us: 1.04x slower                                             |
| regex_effbot               | 3.61 ms                                                | 3.77 ms: 1.04x slower                                             |
| gunicorn                   | 1.24 ms                                                | 1.30 ms: 1.05x slower                                             |
| pycparser                  | 1.18 sec                                               | 1.24 sec: 1.05x slower                                            |
| aiohttp                    | 1.15 ms                                                | 1.21 ms: 1.05x slower                                             |
| nqueens                    | 83.3 ms                                                | 87.9 ms: 1.06x slower                                             |
| go                         | 139 ms                                                 | 148 ms: 1.06x slower                                              |
| hexiom                     | 6.41 ms                                                | 6.87 ms: 1.07x slower                                             |
| regex_dna                  | 212 ms                                                 | 227 ms: 1.07x slower                                              |
| unpickle                   | 15.9 us                                                | 17.0 us: 1.07x slower                                             |
| regex_v8                   | 23.1 ms                                                | 25.7 ms: 1.11x slower                                             |
| create_gc_cycles           | 1.48 ms                                                | 1.69 ms: 1.14x slower                                             |
| python_startup             | 9.55 ms                                                | 11.0 ms: 1.15x slower                                             |
| telco                      | 7.10 ms                                                | 8.58 ms: 1.21x slower                                             |
| python_startup_no_site     | 6.94 ms                                                | 9.48 ms: 1.37x slower                                             |
| coverage                   | 72.7 ms                                                | 100 ms: 1.38x slower                                              |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                      |

Benchmark hidden because not significant (5): pprint_pformat, bench_mp_pool, dulwich_log, logging_silent, xml_etree_iterparse
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240326-3.13.0a5+-f6bf194-JIT/bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-f6bf194.json: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 85.87% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: 1.02x