# Results vs. 3.12.0

- fork: faster-cpython
- ref: exponential_backoff_
- machine: linux-x86_64
- commit hash: bdf272d
- commit date: 2024-03-19
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 0.95x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240319-linux-x86_64-faster%2dcpython-exponential_backoff_-3.13.0a5+-bdf272d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 300 ms: 1.09x slower                                                             |
| chameleon      | 7.41 ms                                                | 7.14 ms: 1.04x faster                                                            |
| docutils       | 2.77 sec                                               | 2.86 sec: 1.03x slower                                                           |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                     |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240319-linux-x86_64-faster%2dcpython-exponential_backoff_-3.13.0a5+-bdf272d |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 726 ms                                                 | 747 ms: 1.03x slower                                                             |
| async_tree_memoization     | 578 ms                                                 | 596 ms: 1.03x slower                                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 599 ms: 1.04x slower                                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 760 ms: 1.05x slower                                                             |
| async_tree_none_tg         | 450 ms                                                 | 472 ms: 1.05x slower                                                             |
| async_tree_io_tg           | 1.18 sec                                               | 1.25 sec: 1.06x slower                                                           |
| async_tree_io              | 1.16 sec                                               | 1.23 sec: 1.06x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.04x slower                                                                     |

Benchmark hidden because not significant (1): async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240319-linux-x86_64-faster%2dcpython-exponential_backoff_-3.13.0a5+-bdf272d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 187 ms                                                 | 191 ms: 1.02x slower                                                             |
| float          | 84.7 ms                                                | 93.9 ms: 1.11x slower                                                            |
| nbody          | 97.0 ms                                                | 121 ms: 1.25x slower                                                             |
| Geometric mean | (ref)                                                  | 1.12x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240319-linux-x86_64-faster%2dcpython-exponential_backoff_-3.13.0a5+-bdf272d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.56 ms: 1.02x faster                                                            |
| regex_dna      | 212 ms                                                 | 219 ms: 1.03x slower                                                             |
| regex_v8       | 23.1 ms                                                | 24.5 ms: 1.06x slower                                                            |
| regex_compile  | 148 ms                                                 | 175 ms: 1.18x slower                                                             |
| Geometric mean | (ref)                                                  | 1.06x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240319-linux-x86_64-faster%2dcpython-exponential_backoff_-3.13.0a5+-bdf272d |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_list        | 5.29 us                                                | 4.94 us: 1.07x faster                                                            |
| pickle_dict          | 35.5 us                                                | 33.6 us: 1.06x faster                                                            |
| pickle_pure_python   | 324 us                                                 | 313 us: 1.04x faster                                                             |
| pickle_list          | 5.08 us                                                | 5.02 us: 1.01x faster                                                            |
| json_loads           | 28.5 us                                                | 28.3 us: 1.01x faster                                                            |
| unpickle             | 15.9 us                                                | 15.8 us: 1.01x faster                                                            |
| pickle               | 11.6 us                                                | 11.7 us: 1.01x slower                                                            |
| xml_etree_parse      | 159 ms                                                 | 163 ms: 1.02x slower                                                             |
| json_dumps           | 10.4 ms                                                | 10.7 ms: 1.03x slower                                                            |
| xml_etree_process    | 61.7 ms                                                | 63.6 ms: 1.03x slower                                                            |
| xml_etree_generate   | 89.2 ms                                                | 92.5 ms: 1.04x slower                                                            |
| tomli_loads          | 2.33 sec                                               | 2.46 sec: 1.06x slower                                                           |
| xml_etree_iterparse  | 107 ms                                                 | 113 ms: 1.06x slower                                                             |
| unpickle_pure_python | 230 us                                                 | 277 us: 1.21x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240319-linux-x86_64-faster%2dcpython-exponential_backoff_-3.13.0a5+-bdf272d |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                            |
| python_startup_no_site | 6.94 ms                                                | 9.07 ms: 1.31x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.20x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240319-linux-x86_64-faster%2dcpython-exponential_backoff_-3.13.0a5+-bdf272d |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 35.0 ms: 1.01x slower                                                            |
| mako            | 11.9 ms                                                | 13.2 ms: 1.11x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.06x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240319-linux-x86_64-faster%2dcpython-exponential_backoff_-3.13.0a5+-bdf272d |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols   | 158 us                                                 | 115 us: 1.37x faster                                                             |
| unpickle_list              | 5.29 us                                                | 4.94 us: 1.07x faster                                                            |
| pickle_dict                | 35.5 us                                                | 33.6 us: 1.06x faster                                                            |
| generators                 | 31.2 ms                                                | 29.8 ms: 1.05x faster                                                            |
| deepcopy_reduce            | 3.35 us                                                | 3.20 us: 1.05x faster                                                            |
| chameleon                  | 7.41 ms                                                | 7.14 ms: 1.04x faster                                                            |
| pickle_pure_python         | 324 us                                                 | 313 us: 1.04x faster                                                             |
| logging_format             | 7.23 us                                                | 7.08 us: 1.02x faster                                                            |
| comprehensions             | 21.8 us                                                | 21.3 us: 1.02x faster                                                            |
| regex_effbot               | 3.61 ms                                                | 3.56 ms: 1.02x faster                                                            |
| pickle_list                | 5.08 us                                                | 5.02 us: 1.01x faster                                                            |
| logging_simple             | 6.46 us                                                | 6.38 us: 1.01x faster                                                            |
| coroutines                 | 23.2 ms                                                | 22.9 ms: 1.01x faster                                                            |
| deepcopy                   | 371 us                                                 | 368 us: 1.01x faster                                                             |
| sympy_sum                  | 169 ms                                                 | 168 ms: 1.01x faster                                                             |
| json_loads                 | 28.5 us                                                | 28.3 us: 1.01x faster                                                            |
| unpickle                   | 15.9 us                                                | 15.8 us: 1.01x faster                                                            |
| logging_silent             | 104 ns                                                 | 105 ns: 1.00x slower                                                             |
| sympy_integrate            | 21.4 ms                                                | 21.5 ms: 1.00x slower                                                            |
| pickle                     | 11.6 us                                                | 11.7 us: 1.01x slower                                                            |
| django_template            | 34.6 ms                                                | 35.0 ms: 1.01x slower                                                            |
| dask                       | 372 ms                                                 | 377 ms: 1.01x slower                                                             |
| sympy_str                  | 300 ms                                                 | 304 ms: 1.01x slower                                                             |
| pathlib                    | 19.3 ms                                                | 19.7 ms: 1.02x slower                                                            |
| pidigits                   | 187 ms                                                 | 191 ms: 1.02x slower                                                             |
| xml_etree_parse            | 159 ms                                                 | 163 ms: 1.02x slower                                                             |
| asyncio_websockets         | 551 ms                                                 | 564 ms: 1.02x slower                                                             |
| mdp                        | 2.63 sec                                               | 2.70 sec: 1.02x slower                                                           |
| json_dumps                 | 10.4 ms                                                | 10.7 ms: 1.03x slower                                                            |
| async_generators           | 463 ms                                                 | 476 ms: 1.03x slower                                                             |
| deltablue                  | 3.72 ms                                                | 3.83 ms: 1.03x slower                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 747 ms: 1.03x slower                                                             |
| bench_thread_pool          | 842 us                                                 | 867 us: 1.03x slower                                                             |
| xml_etree_process          | 61.7 ms                                                | 63.6 ms: 1.03x slower                                                            |
| gc_traversal               | 3.79 ms                                                | 3.91 ms: 1.03x slower                                                            |
| async_tree_memoization     | 578 ms                                                 | 596 ms: 1.03x slower                                                             |
| regex_dna                  | 212 ms                                                 | 219 ms: 1.03x slower                                                             |
| docutils                   | 2.77 sec                                               | 2.86 sec: 1.03x slower                                                           |
| asyncio_tcp                | 491 ms                                                 | 508 ms: 1.03x slower                                                             |
| sqlglot_normalize          | 110 ms                                                 | 114 ms: 1.03x slower                                                             |
| xml_etree_generate         | 89.2 ms                                                | 92.5 ms: 1.04x slower                                                            |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.85 sec: 1.04x slower                                                           |
| sqlite_synth               | 2.83 us                                                | 2.95 us: 1.04x slower                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 599 ms: 1.04x slower                                                             |
| create_gc_cycles           | 1.48 ms                                                | 1.54 ms: 1.04x slower                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 760 ms: 1.05x slower                                                             |
| async_tree_none_tg         | 450 ms                                                 | 472 ms: 1.05x slower                                                             |
| gunicorn                   | 1.24 ms                                                | 1.30 ms: 1.05x slower                                                            |
| aiohttp                    | 1.15 ms                                                | 1.21 ms: 1.05x slower                                                            |
| sqlglot_parse              | 1.36 ms                                                | 1.44 ms: 1.06x slower                                                            |
| tomli_loads                | 2.33 sec                                               | 2.46 sec: 1.06x slower                                                           |
| regex_v8                   | 23.1 ms                                                | 24.5 ms: 1.06x slower                                                            |
| meteor_contest             | 112 ms                                                 | 119 ms: 1.06x slower                                                             |
| deepcopy_memo              | 40.7 us                                                | 43.2 us: 1.06x slower                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 1.25 sec: 1.06x slower                                                           |
| xml_etree_iterparse        | 107 ms                                                 | 113 ms: 1.06x slower                                                             |
| sqlglot_transpile          | 1.68 ms                                                | 1.79 ms: 1.06x slower                                                            |
| async_tree_io              | 1.16 sec                                               | 1.23 sec: 1.06x slower                                                           |
| dulwich_log                | 68.5 ms                                                | 73.4 ms: 1.07x slower                                                            |
| sympy_expand               | 478 ms                                                 | 516 ms: 1.08x slower                                                             |
| crypto_pyaes               | 81.9 ms                                                | 88.8 ms: 1.08x slower                                                            |
| unpack_sequence            | 54.0 ns                                                | 58.9 ns: 1.09x slower                                                            |
| 2to3                       | 274 ms                                                 | 300 ms: 1.09x slower                                                             |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                            |
| pycparser                  | 1.18 sec                                               | 1.30 sec: 1.10x slower                                                           |
| mypy2                      | 830 ms                                                 | 914 ms: 1.10x slower                                                             |
| float                      | 84.7 ms                                                | 93.9 ms: 1.11x slower                                                            |
| mako                       | 11.9 ms                                                | 13.2 ms: 1.11x slower                                                            |
| raytrace                   | 312 ms                                                 | 346 ms: 1.11x slower                                                             |
| sqlglot_optimize           | 54.8 ms                                                | 61.2 ms: 1.12x slower                                                            |
| chaos                      | 67.0 ms                                                | 76.1 ms: 1.14x slower                                                            |
| pprint_safe_repr           | 776 ms                                                 | 887 ms: 1.14x slower                                                             |
| fannkuch                   | 417 ms                                                 | 481 ms: 1.15x slower                                                             |
| scimark_sor                | 129 ms                                                 | 149 ms: 1.16x slower                                                             |
| scimark_fft                | 382 ms                                                 | 444 ms: 1.16x slower                                                             |
| scimark_monte_carlo        | 75.1 ms                                                | 87.6 ms: 1.17x slower                                                            |
| pprint_pformat             | 1.57 sec                                               | 1.85 sec: 1.18x slower                                                           |
| regex_compile              | 148 ms                                                 | 175 ms: 1.18x slower                                                             |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.99 ms: 1.19x slower                                                            |
| nqueens                    | 83.3 ms                                                | 100 ms: 1.20x slower                                                             |
| unpickle_pure_python       | 230 us                                                 | 277 us: 1.21x slower                                                             |
| richards_super             | 51.5 ms                                                | 62.3 ms: 1.21x slower                                                            |
| pyflate                    | 482 ms                                                 | 590 ms: 1.22x slower                                                             |
| richards                   | 45.8 ms                                                | 56.1 ms: 1.22x slower                                                            |
| go                         | 139 ms                                                 | 172 ms: 1.23x slower                                                             |
| spectral_norm              | 115 ms                                                 | 142 ms: 1.23x slower                                                             |
| nbody                      | 97.0 ms                                                | 121 ms: 1.25x slower                                                             |
| telco                      | 7.10 ms                                                | 9.02 ms: 1.27x slower                                                            |
| python_startup_no_site     | 6.94 ms                                                | 9.07 ms: 1.31x slower                                                            |
| coverage                   | 72.7 ms                                                | 99.2 ms: 1.36x slower                                                            |
| scimark_lu                 | 118 ms                                                 | 162 ms: 1.37x slower                                                             |
| hexiom                     | 6.41 ms                                                | 8.92 ms: 1.39x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.07x slower                                                                     |

Benchmark hidden because not significant (4): async_tree_none, bench_mp_pool, tornado_http, json
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240319-3.13.0a5+-bdf272d-PYTHON_UOPS/bm-20240319-linux-x86_64-faster%2dcpython-exponential_backoff_-3.13.0a5+-bdf272d.json: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x


# Memory

- memory change: 0.95x