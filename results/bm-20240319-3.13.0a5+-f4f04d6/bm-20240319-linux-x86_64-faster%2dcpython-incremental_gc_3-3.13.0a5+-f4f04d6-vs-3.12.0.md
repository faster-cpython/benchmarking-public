# Results vs. 3.12.0

- fork: faster-cpython
- ref: incremental_gc_3
- machine: linux-x86_64
- commit hash: f4f04d6
- commit date: 2024-03-19
- overall geometric mean: 1.21x slower
- HPT reliability: 68.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240319-linux-x86_64-faster%2dcpython-incremental_gc_3-3.13.0a5+-f4f04d6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 294 ms: 1.07x slower                                                         |
| chameleon      | 7.41 ms                                                | 6.94 ms: 1.07x faster                                                        |
| docutils       | 2.77 sec                                               | 4.66 sec: 1.68x slower                                                       |
| tornado_http   | 103 ms                                                 | 99.0 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                  | 1.13x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240319-linux-x86_64-faster%2dcpython-incremental_gc_3-3.13.0a5+-f4f04d6 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 726 ms                                                 | 4.17 sec: 5.75x slower                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 4.58 sec: 6.31x slower                                                       |
| async_tree_none            | 472 ms                                                 | 3.42 sec: 7.25x slower                                                       |
| async_tree_memoization     | 578 ms                                                 | 4.43 sec: 7.66x slower                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 4.73 sec: 8.23x slower                                                       |
| async_tree_none_tg         | 450 ms                                                 | 3.78 sec: 8.41x slower                                                       |
| async_tree_io              | 1.16 sec                                               | 13.3 sec: 11.48x slower                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 14.3 sec: 12.07x slower                                                      |
| Geometric mean             | (ref)                                                  | 8.14x slower                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240319-linux-x86_64-faster%2dcpython-incremental_gc_3-3.13.0a5+-f4f04d6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 91.7 ms: 1.06x faster                                                        |
| pidigits       | 187 ms                                                 | 190 ms: 1.01x slower                                                         |
| float          | 84.7 ms                                                | 144 ms: 1.70x slower                                                         |
| Geometric mean | (ref)                                                  | 1.18x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240319-linux-x86_64-faster%2dcpython-incremental_gc_3-3.13.0a5+-f4f04d6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 134 ms: 1.11x faster                                                         |
| regex_effbot   | 3.61 ms                                                | 3.69 ms: 1.02x slower                                                        |
| regex_dna      | 212 ms                                                 | 228 ms: 1.08x slower                                                         |
| regex_v8       | 23.1 ms                                                | 26.6 ms: 1.15x slower                                                        |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240319-linux-x86_64-faster%2dcpython-incremental_gc_3-3.13.0a5+-f4f04d6 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 324 us                                                 | 297 us: 1.09x faster                                                         |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.06x faster                                                         |
| tomli_loads          | 2.33 sec                                               | 2.20 sec: 1.06x faster                                                       |
| unpickle_list        | 5.29 us                                                | 5.11 us: 1.04x faster                                                        |
| unpickle             | 15.9 us                                                | 15.4 us: 1.03x faster                                                        |
| json_loads           | 28.5 us                                                | 28.1 us: 1.02x faster                                                        |
| pickle_dict          | 35.5 us                                                | 35.0 us: 1.01x faster                                                        |
| json_dumps           | 10.4 ms                                                | 10.6 ms: 1.02x slower                                                        |
| pickle               | 11.6 us                                                | 11.9 us: 1.03x slower                                                        |
| pickle_list          | 5.08 us                                                | 5.33 us: 1.05x slower                                                        |
| xml_etree_process    | 61.7 ms                                                | 67.9 ms: 1.10x slower                                                        |
| xml_etree_generate   | 89.2 ms                                                | 98.4 ms: 1.10x slower                                                        |
| xml_etree_parse      | 159 ms                                                 | 217 ms: 1.36x slower                                                         |
| xml_etree_iterparse  | 107 ms                                                 | 165 ms: 1.55x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.05x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240319-linux-x86_64-faster%2dcpython-incremental_gc_3-3.13.0a5+-f4f04d6 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                        |
| python_startup_no_site | 6.94 ms                                                | 8.85 ms: 1.28x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.19x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240319-linux-x86_64-faster%2dcpython-incremental_gc_3-3.13.0a5+-f4f04d6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako           | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240319-linux-x86_64-faster%2dcpython-incremental_gc_3-3.13.0a5+-f4f04d6 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols   | 158 us                                                 | 114 us: 1.39x faster                                                         |
| comprehensions             | 21.8 us                                                | 16.1 us: 1.35x faster                                                        |
| raytrace                   | 312 ms                                                 | 263 ms: 1.19x faster                                                         |
| crypto_pyaes               | 81.9 ms                                                | 71.9 ms: 1.14x faster                                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 66.9 ms: 1.12x faster                                                        |
| logging_format             | 7.23 us                                                | 6.51 us: 1.11x faster                                                        |
| regex_compile              | 148 ms                                                 | 134 ms: 1.11x faster                                                         |
| deepcopy_memo              | 40.7 us                                                | 36.8 us: 1.11x faster                                                        |
| logging_simple             | 6.46 us                                                | 5.85 us: 1.10x faster                                                        |
| sympy_sum                  | 169 ms                                                 | 153 ms: 1.10x faster                                                         |
| chaos                      | 67.0 ms                                                | 60.8 ms: 1.10x faster                                                        |
| sympy_str                  | 300 ms                                                 | 274 ms: 1.09x faster                                                         |
| pickle_pure_python         | 324 us                                                 | 297 us: 1.09x faster                                                         |
| sympy_integrate            | 21.4 ms                                                | 19.9 ms: 1.08x faster                                                        |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.08x faster                                                         |
| deepcopy                   | 371 us                                                 | 345 us: 1.08x faster                                                         |
| deepcopy_reduce            | 3.35 us                                                | 3.11 us: 1.08x faster                                                        |
| mako                       | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                        |
| logging_silent             | 104 ns                                                 | 97.5 ns: 1.07x faster                                                        |
| generators                 | 31.2 ms                                                | 29.2 ms: 1.07x faster                                                        |
| chameleon                  | 7.41 ms                                                | 6.94 ms: 1.07x faster                                                        |
| gc_traversal               | 3.79 ms                                                | 3.56 ms: 1.07x faster                                                        |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.06x faster                                                         |
| nbody                      | 97.0 ms                                                | 91.7 ms: 1.06x faster                                                        |
| pprint_safe_repr           | 776 ms                                                 | 734 ms: 1.06x faster                                                         |
| tomli_loads                | 2.33 sec                                               | 2.20 sec: 1.06x faster                                                       |
| spectral_norm              | 115 ms                                                 | 109 ms: 1.05x faster                                                         |
| hexiom                     | 6.41 ms                                                | 6.10 ms: 1.05x faster                                                        |
| pyflate                    | 482 ms                                                 | 461 ms: 1.05x faster                                                         |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.04x faster                                                       |
| scimark_fft                | 382 ms                                                 | 366 ms: 1.04x faster                                                         |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.04x faster                                                         |
| deltablue                  | 3.72 ms                                                | 3.57 ms: 1.04x faster                                                        |
| pathlib                    | 19.3 ms                                                | 18.6 ms: 1.04x faster                                                        |
| tornado_http               | 103 ms                                                 | 99.0 ms: 1.04x faster                                                        |
| unpickle_list              | 5.29 us                                                | 5.11 us: 1.04x faster                                                        |
| sympy_expand               | 478 ms                                                 | 463 ms: 1.03x faster                                                         |
| unpickle                   | 15.9 us                                                | 15.4 us: 1.03x faster                                                        |
| nqueens                    | 83.3 ms                                                | 80.8 ms: 1.03x faster                                                        |
| fannkuch                   | 417 ms                                                 | 406 ms: 1.03x faster                                                         |
| meteor_contest             | 112 ms                                                 | 110 ms: 1.02x faster                                                         |
| sqlglot_normalize          | 110 ms                                                 | 108 ms: 1.02x faster                                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.95 ms: 1.02x faster                                                        |
| bench_thread_pool          | 842 us                                                 | 824 us: 1.02x faster                                                         |
| coroutines                 | 23.2 ms                                                | 22.8 ms: 1.02x faster                                                        |
| richards                   | 45.8 ms                                                | 45.1 ms: 1.02x faster                                                        |
| json_loads                 | 28.5 us                                                | 28.1 us: 1.02x faster                                                        |
| pickle_dict                | 35.5 us                                                | 35.0 us: 1.01x faster                                                        |
| bench_mp_pool              | 24.0 ms                                                | 23.7 ms: 1.01x faster                                                        |
| dulwich_log                | 68.5 ms                                                | 68.1 ms: 1.01x faster                                                        |
| mdp                        | 2.63 sec                                               | 2.62 sec: 1.00x faster                                                       |
| create_gc_cycles           | 1.48 ms                                                | 1.49 ms: 1.01x slower                                                        |
| pidigits                   | 187 ms                                                 | 190 ms: 1.01x slower                                                         |
| richards_super             | 51.5 ms                                                | 52.3 ms: 1.02x slower                                                        |
| json_dumps                 | 10.4 ms                                                | 10.6 ms: 1.02x slower                                                        |
| regex_effbot               | 3.61 ms                                                | 3.69 ms: 1.02x slower                                                        |
| sqlglot_optimize           | 54.8 ms                                                | 56.1 ms: 1.02x slower                                                        |
| asyncio_tcp                | 491 ms                                                 | 502 ms: 1.02x slower                                                         |
| pickle                     | 11.6 us                                                | 11.9 us: 1.03x slower                                                        |
| asyncio_websockets         | 551 ms                                                 | 568 ms: 1.03x slower                                                         |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.84 sec: 1.03x slower                                                       |
| sqlite_synth               | 2.83 us                                                | 2.93 us: 1.03x slower                                                        |
| pickle_list                | 5.08 us                                                | 5.33 us: 1.05x slower                                                        |
| unpack_sequence            | 54.0 ns                                                | 56.9 ns: 1.05x slower                                                        |
| gunicorn                   | 1.24 ms                                                | 1.33 ms: 1.07x slower                                                        |
| aiohttp                    | 1.15 ms                                                | 1.23 ms: 1.07x slower                                                        |
| 2to3                       | 274 ms                                                 | 294 ms: 1.07x slower                                                         |
| regex_dna                  | 212 ms                                                 | 228 ms: 1.08x slower                                                         |
| sqlglot_parse              | 1.36 ms                                                | 1.49 ms: 1.09x slower                                                        |
| xml_etree_process          | 61.7 ms                                                | 67.9 ms: 1.10x slower                                                        |
| xml_etree_generate         | 89.2 ms                                                | 98.4 ms: 1.10x slower                                                        |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                        |
| sqlglot_transpile          | 1.68 ms                                                | 1.86 ms: 1.11x slower                                                        |
| regex_v8                   | 23.1 ms                                                | 26.6 ms: 1.15x slower                                                        |
| async_generators           | 463 ms                                                 | 536 ms: 1.16x slower                                                         |
| telco                      | 7.10 ms                                                | 8.63 ms: 1.22x slower                                                        |
| python_startup_no_site     | 6.94 ms                                                | 8.85 ms: 1.28x slower                                                        |
| pycparser                  | 1.18 sec                                               | 1.52 sec: 1.29x slower                                                       |
| coverage                   | 72.7 ms                                                | 96.1 ms: 1.32x slower                                                        |
| xml_etree_parse            | 159 ms                                                 | 217 ms: 1.36x slower                                                         |
| xml_etree_iterparse        | 107 ms                                                 | 165 ms: 1.55x slower                                                         |
| docutils                   | 2.77 sec                                               | 4.66 sec: 1.68x slower                                                       |
| float                      | 84.7 ms                                                | 144 ms: 1.70x slower                                                         |
| dask                       | 372 ms                                                 | 756 ms: 2.03x slower                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 4.17 sec: 5.75x slower                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 4.58 sec: 6.31x slower                                                       |
| async_tree_none            | 472 ms                                                 | 3.42 sec: 7.25x slower                                                       |
| async_tree_memoization     | 578 ms                                                 | 4.43 sec: 7.66x slower                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 4.73 sec: 8.23x slower                                                       |
| async_tree_none_tg         | 450 ms                                                 | 3.78 sec: 8.41x slower                                                       |
| async_tree_io              | 1.16 sec                                               | 13.3 sec: 11.48x slower                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 14.3 sec: 12.07x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.21x slower                                                                 |

Benchmark hidden because not significant (4): mypy2, json, django_template, go
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240319-3.13.0a5+-f4f04d6/bm-20240319-linux-x86_64-faster%2dcpython-incremental_gc_3-3.13.0a5+-f4f04d6.json: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 68.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 0.93x