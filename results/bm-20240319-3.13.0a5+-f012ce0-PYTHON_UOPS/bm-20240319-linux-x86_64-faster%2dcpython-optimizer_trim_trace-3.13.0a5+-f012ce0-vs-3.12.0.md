# Results vs. 3.12.0

- fork: faster-cpython
- ref: optimizer_trim_trace
- machine: linux-x86_64
- commit hash: f012ce0
- commit date: 2024-03-19
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: 0.94x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240319-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-f012ce0 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 299 ms: 1.09x slower                                                             |
| chameleon      | 7.41 ms                                                | 7.35 ms: 1.01x faster                                                            |
| docutils       | 2.77 sec                                               | 2.92 sec: 1.05x slower                                                           |
| tornado_http   | 103 ms                                                 | 105 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240319-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-f012ce0 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 726 ms                                                 | 748 ms: 1.03x slower                                                             |
| async_tree_memoization     | 578 ms                                                 | 599 ms: 1.04x slower                                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 761 ms: 1.05x slower                                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 603 ms: 1.05x slower                                                             |
| async_tree_none_tg         | 450 ms                                                 | 476 ms: 1.06x slower                                                             |
| async_tree_io_tg           | 1.18 sec                                               | 1.27 sec: 1.07x slower                                                           |
| async_tree_io              | 1.16 sec                                               | 1.25 sec: 1.08x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.05x slower                                                                     |

Benchmark hidden because not significant (1): async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240319-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-f012ce0 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 187 ms                                                 | 191 ms: 1.02x slower                                                             |
| float          | 84.7 ms                                                | 97.7 ms: 1.15x slower                                                            |
| nbody          | 97.0 ms                                                | 125 ms: 1.29x slower                                                             |
| Geometric mean | (ref)                                                  | 1.15x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240319-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-f012ce0 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.68 ms: 1.02x slower                                                            |
| regex_dna      | 212 ms                                                 | 227 ms: 1.07x slower                                                             |
| regex_v8       | 23.1 ms                                                | 25.2 ms: 1.09x slower                                                            |
| regex_compile  | 148 ms                                                 | 178 ms: 1.20x slower                                                             |
| Geometric mean | (ref)                                                  | 1.09x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240319-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-f012ce0 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_pure_python   | 324 us                                                 | 309 us: 1.05x faster                                                             |
| unpickle_list        | 5.29 us                                                | 5.07 us: 1.04x faster                                                            |
| json_loads           | 28.5 us                                                | 27.9 us: 1.02x faster                                                            |
| pickle_dict          | 35.5 us                                                | 35.6 us: 1.00x slower                                                            |
| unpickle             | 15.9 us                                                | 16.0 us: 1.01x slower                                                            |
| pickle_list          | 5.08 us                                                | 5.19 us: 1.02x slower                                                            |
| xml_etree_parse      | 159 ms                                                 | 163 ms: 1.02x slower                                                             |
| json_dumps           | 10.4 ms                                                | 10.7 ms: 1.03x slower                                                            |
| xml_etree_process    | 61.7 ms                                                | 63.5 ms: 1.03x slower                                                            |
| xml_etree_generate   | 89.2 ms                                                | 92.7 ms: 1.04x slower                                                            |
| xml_etree_iterparse  | 107 ms                                                 | 113 ms: 1.06x slower                                                             |
| tomli_loads          | 2.33 sec                                               | 2.48 sec: 1.06x slower                                                           |
| unpickle_pure_python | 230 us                                                 | 278 us: 1.21x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.03x slower                                                                     |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240319-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-f012ce0 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                            |
| python_startup_no_site | 6.94 ms                                                | 9.08 ms: 1.31x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.20x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240319-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-f012ce0 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 37.6 ms: 1.09x slower                                                            |
| mako            | 11.9 ms                                                | 13.7 ms: 1.15x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.12x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240319-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-f012ce0 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols   | 158 us                                                 | 118 us: 1.34x faster                                                             |
| generators                 | 31.2 ms                                                | 29.6 ms: 1.06x faster                                                            |
| pickle_pure_python         | 324 us                                                 | 309 us: 1.05x faster                                                             |
| unpickle_list              | 5.29 us                                                | 5.07 us: 1.04x faster                                                            |
| json_loads                 | 28.5 us                                                | 27.9 us: 1.02x faster                                                            |
| coroutines                 | 23.2 ms                                                | 22.7 ms: 1.02x faster                                                            |
| unpack_sequence            | 54.0 ns                                                | 53.1 ns: 1.02x faster                                                            |
| deepcopy_reduce            | 3.35 us                                                | 3.30 us: 1.01x faster                                                            |
| json                       | 5.26 ms                                                | 5.20 ms: 1.01x faster                                                            |
| deepcopy                   | 371 us                                                 | 367 us: 1.01x faster                                                             |
| chameleon                  | 7.41 ms                                                | 7.35 ms: 1.01x faster                                                            |
| logging_silent             | 104 ns                                                 | 105 ns: 1.00x slower                                                             |
| pickle_dict                | 35.5 us                                                | 35.6 us: 1.00x slower                                                            |
| sympy_sum                  | 169 ms                                                 | 170 ms: 1.01x slower                                                             |
| unpickle                   | 15.9 us                                                | 16.0 us: 1.01x slower                                                            |
| tornado_http               | 103 ms                                                 | 105 ms: 1.02x slower                                                             |
| dask                       | 372 ms                                                 | 379 ms: 1.02x slower                                                             |
| regex_effbot               | 3.61 ms                                                | 3.68 ms: 1.02x slower                                                            |
| pidigits                   | 187 ms                                                 | 191 ms: 1.02x slower                                                             |
| pickle_list                | 5.08 us                                                | 5.19 us: 1.02x slower                                                            |
| asyncio_websockets         | 551 ms                                                 | 563 ms: 1.02x slower                                                             |
| pathlib                    | 19.3 ms                                                | 19.8 ms: 1.02x slower                                                            |
| xml_etree_parse            | 159 ms                                                 | 163 ms: 1.02x slower                                                             |
| mdp                        | 2.63 sec                                               | 2.70 sec: 1.03x slower                                                           |
| json_dumps                 | 10.4 ms                                                | 10.7 ms: 1.03x slower                                                            |
| sympy_str                  | 300 ms                                                 | 308 ms: 1.03x slower                                                             |
| xml_etree_process          | 61.7 ms                                                | 63.5 ms: 1.03x slower                                                            |
| bench_thread_pool          | 842 us                                                 | 866 us: 1.03x slower                                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 748 ms: 1.03x slower                                                             |
| async_generators           | 463 ms                                                 | 477 ms: 1.03x slower                                                             |
| async_tree_memoization     | 578 ms                                                 | 599 ms: 1.04x slower                                                             |
| comprehensions             | 21.8 us                                                | 22.6 us: 1.04x slower                                                            |
| deepcopy_memo              | 40.7 us                                                | 42.2 us: 1.04x slower                                                            |
| deltablue                  | 3.72 ms                                                | 3.86 ms: 1.04x slower                                                            |
| asyncio_tcp                | 491 ms                                                 | 510 ms: 1.04x slower                                                             |
| xml_etree_generate         | 89.2 ms                                                | 92.7 ms: 1.04x slower                                                            |
| sympy_integrate            | 21.4 ms                                                | 22.3 ms: 1.04x slower                                                            |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.86 sec: 1.04x slower                                                           |
| sqlite_synth               | 2.83 us                                                | 2.96 us: 1.04x slower                                                            |
| gc_traversal               | 3.79 ms                                                | 3.96 ms: 1.04x slower                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 761 ms: 1.05x slower                                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 603 ms: 1.05x slower                                                             |
| docutils                   | 2.77 sec                                               | 2.92 sec: 1.05x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 1.56 ms: 1.05x slower                                                            |
| async_tree_none_tg         | 450 ms                                                 | 476 ms: 1.06x slower                                                             |
| gunicorn                   | 1.24 ms                                                | 1.32 ms: 1.06x slower                                                            |
| meteor_contest             | 112 ms                                                 | 119 ms: 1.06x slower                                                             |
| xml_etree_iterparse        | 107 ms                                                 | 113 ms: 1.06x slower                                                             |
| sqlglot_parse              | 1.36 ms                                                | 1.45 ms: 1.06x slower                                                            |
| sqlglot_transpile          | 1.68 ms                                                | 1.79 ms: 1.06x slower                                                            |
| tomli_loads                | 2.33 sec                                               | 2.48 sec: 1.06x slower                                                           |
| aiohttp                    | 1.15 ms                                                | 1.22 ms: 1.06x slower                                                            |
| regex_dna                  | 212 ms                                                 | 227 ms: 1.07x slower                                                             |
| async_tree_io_tg           | 1.18 sec                                               | 1.27 sec: 1.07x slower                                                           |
| dulwich_log                | 68.5 ms                                                | 73.6 ms: 1.07x slower                                                            |
| crypto_pyaes               | 81.9 ms                                                | 88.2 ms: 1.08x slower                                                            |
| async_tree_io              | 1.16 sec                                               | 1.25 sec: 1.08x slower                                                           |
| sympy_expand               | 478 ms                                                 | 517 ms: 1.08x slower                                                             |
| django_template            | 34.6 ms                                                | 37.6 ms: 1.09x slower                                                            |
| sqlglot_normalize          | 110 ms                                                 | 120 ms: 1.09x slower                                                             |
| regex_v8                   | 23.1 ms                                                | 25.2 ms: 1.09x slower                                                            |
| 2to3                       | 274 ms                                                 | 299 ms: 1.09x slower                                                             |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                            |
| raytrace                   | 312 ms                                                 | 345 ms: 1.10x slower                                                             |
| mypy2                      | 830 ms                                                 | 923 ms: 1.11x slower                                                             |
| pycparser                  | 1.18 sec                                               | 1.31 sec: 1.11x slower                                                           |
| scimark_sor                | 129 ms                                                 | 144 ms: 1.12x slower                                                             |
| sqlglot_optimize           | 54.8 ms                                                | 61.2 ms: 1.12x slower                                                            |
| chaos                      | 67.0 ms                                                | 75.7 ms: 1.13x slower                                                            |
| scimark_fft                | 382 ms                                                 | 437 ms: 1.15x slower                                                             |
| mako                       | 11.9 ms                                                | 13.7 ms: 1.15x slower                                                            |
| float                      | 84.7 ms                                                | 97.7 ms: 1.15x slower                                                            |
| fannkuch                   | 417 ms                                                 | 481 ms: 1.15x slower                                                             |
| pprint_safe_repr           | 776 ms                                                 | 901 ms: 1.16x slower                                                             |
| scimark_monte_carlo        | 75.1 ms                                                | 89.3 ms: 1.19x slower                                                            |
| regex_compile              | 148 ms                                                 | 178 ms: 1.20x slower                                                             |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 6.07 ms: 1.20x slower                                                            |
| richards_super             | 51.5 ms                                                | 62.0 ms: 1.20x slower                                                            |
| pprint_pformat             | 1.57 sec                                               | 1.89 sec: 1.20x slower                                                           |
| unpickle_pure_python       | 230 us                                                 | 278 us: 1.21x slower                                                             |
| richards                   | 45.8 ms                                                | 55.7 ms: 1.22x slower                                                            |
| pyflate                    | 482 ms                                                 | 589 ms: 1.22x slower                                                             |
| spectral_norm              | 115 ms                                                 | 140 ms: 1.22x slower                                                             |
| nqueens                    | 83.3 ms                                                | 103 ms: 1.24x slower                                                             |
| telco                      | 7.10 ms                                                | 8.85 ms: 1.25x slower                                                            |
| go                         | 139 ms                                                 | 180 ms: 1.29x slower                                                             |
| nbody                      | 97.0 ms                                                | 125 ms: 1.29x slower                                                             |
| python_startup_no_site     | 6.94 ms                                                | 9.08 ms: 1.31x slower                                                            |
| coverage                   | 72.7 ms                                                | 97.0 ms: 1.33x slower                                                            |
| scimark_lu                 | 118 ms                                                 | 168 ms: 1.42x slower                                                             |
| hexiom                     | 6.41 ms                                                | 9.27 ms: 1.45x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.08x slower                                                                     |

Benchmark hidden because not significant (5): async_tree_none, logging_simple, pickle, bench_mp_pool, logging_format
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240319-3.13.0a5+-f012ce0-PYTHON_UOPS/bm-20240319-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-f012ce0.json: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.05x


# Memory

- memory change: 0.94x