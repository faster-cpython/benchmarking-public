# Results vs. 3.12.0

- fork: faster-cpython
- ref: deferred_rc_overhead
- machine: linux-x86_64
- commit hash: f748355
- commit date: 2024-05-31
- overall geometric mean: 1.03x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240531-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-f748355 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 270 ms: 1.01x faster                                                            |
| docutils       | 2.77 sec                                               | 2.79 sec: 1.01x slower                                                          |
| tornado_http   | 103 ms                                                 | 93.9 ms: 1.09x faster                                                           |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240531-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-f748355 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 447 ms: 1.29x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 350 ms: 1.28x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 934 ms: 1.27x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 583 ms: 1.24x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 468 ms: 1.23x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 947 ms: 1.22x faster                                                            |
| async_tree_none            | 472 ms                                                 | 388 ms: 1.22x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 621 ms: 1.17x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240531-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-f748355 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 89.1 ms: 1.09x faster                                                           |
| float          | 84.7 ms                                                | 79.5 ms: 1.07x faster                                                           |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240531-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-f748355 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 134 ms: 1.11x faster                                                            |
| regex_dna      | 212 ms                                                 | 228 ms: 1.07x slower                                                            |
| regex_v8       | 23.1 ms                                                | 26.0 ms: 1.12x slower                                                           |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240531-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-f748355 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.18 sec: 1.07x faster                                                          |
| pickle_pure_python   | 324 us                                                 | 303 us: 1.07x faster                                                            |
| unpickle_pure_python | 230 us                                                 | 218 us: 1.05x faster                                                            |
| xml_etree_process    | 61.7 ms                                                | 60.3 ms: 1.02x faster                                                           |
| xml_etree_generate   | 89.2 ms                                                | 87.1 ms: 1.02x faster                                                           |
| json_loads           | 28.5 us                                                | 28.8 us: 1.01x slower                                                           |
| pickle_dict          | 35.5 us                                                | 35.9 us: 1.01x slower                                                           |
| json_dumps           | 10.4 ms                                                | 10.6 ms: 1.02x slower                                                           |
| unpickle_list        | 5.29 us                                                | 5.41 us: 1.02x slower                                                           |
| pickle               | 11.6 us                                                | 12.0 us: 1.04x slower                                                           |
| pickle_list          | 5.08 us                                                | 5.30 us: 1.04x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (3): unpickle, xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240531-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-f748355 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                           |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240531-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-f748355 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.7 ms: 1.02x faster                                                           |
| django_template | 34.6 ms                                                | 35.3 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240531-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-f748355 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| comprehensions             | 21.8 us                                                | 16.8 us: 1.29x faster                                                           |
| async_tree_memoization_tg  | 575 ms                                                 | 447 ms: 1.29x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 350 ms: 1.28x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 934 ms: 1.27x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 583 ms: 1.24x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 468 ms: 1.23x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 947 ms: 1.22x faster                                                            |
| async_tree_none            | 472 ms                                                 | 388 ms: 1.22x faster                                                            |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.19x faster                                                           |
| raytrace                   | 312 ms                                                 | 265 ms: 1.18x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 621 ms: 1.17x faster                                                            |
| logging_format             | 7.23 us                                                | 6.31 us: 1.15x faster                                                           |
| logging_simple             | 6.46 us                                                | 5.68 us: 1.14x faster                                                           |
| deltablue                  | 3.72 ms                                                | 3.27 ms: 1.14x faster                                                           |
| generators                 | 31.2 ms                                                | 27.8 ms: 1.12x faster                                                           |
| regex_compile              | 148 ms                                                 | 134 ms: 1.11x faster                                                            |
| chaos                      | 67.0 ms                                                | 60.9 ms: 1.10x faster                                                           |
| tornado_http               | 103 ms                                                 | 93.9 ms: 1.09x faster                                                           |
| sympy_sum                  | 169 ms                                                 | 155 ms: 1.09x faster                                                            |
| nbody                      | 97.0 ms                                                | 89.1 ms: 1.09x faster                                                           |
| crypto_pyaes               | 81.9 ms                                                | 75.9 ms: 1.08x faster                                                           |
| logging_silent             | 104 ns                                                 | 97.2 ns: 1.07x faster                                                           |
| scimark_monte_carlo        | 75.1 ms                                                | 70.1 ms: 1.07x faster                                                           |
| tomli_loads                | 2.33 sec                                               | 2.18 sec: 1.07x faster                                                          |
| pickle_pure_python         | 324 us                                                 | 303 us: 1.07x faster                                                            |
| sympy_str                  | 300 ms                                                 | 280 ms: 1.07x faster                                                            |
| float                      | 84.7 ms                                                | 79.5 ms: 1.07x faster                                                           |
| gc_traversal               | 3.79 ms                                                | 3.59 ms: 1.06x faster                                                           |
| unpickle_pure_python       | 230 us                                                 | 218 us: 1.05x faster                                                            |
| sympy_integrate            | 21.4 ms                                                | 20.4 ms: 1.05x faster                                                           |
| dulwich_log                | 68.5 ms                                                | 65.8 ms: 1.04x faster                                                           |
| sqlglot_transpile          | 1.68 ms                                                | 1.62 ms: 1.04x faster                                                           |
| deepcopy_memo              | 40.7 us                                                | 39.3 us: 1.04x faster                                                           |
| async_generators           | 463 ms                                                 | 447 ms: 1.03x faster                                                            |
| hexiom                     | 6.41 ms                                                | 6.21 ms: 1.03x faster                                                           |
| pyflate                    | 482 ms                                                 | 467 ms: 1.03x faster                                                            |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                                           |
| pprint_safe_repr           | 776 ms                                                 | 752 ms: 1.03x faster                                                            |
| scimark_sor                | 129 ms                                                 | 126 ms: 1.03x faster                                                            |
| fannkuch                   | 417 ms                                                 | 406 ms: 1.03x faster                                                            |
| coroutines                 | 23.2 ms                                                | 22.6 ms: 1.03x faster                                                           |
| xml_etree_process          | 61.7 ms                                                | 60.3 ms: 1.02x faster                                                           |
| xml_etree_generate         | 89.2 ms                                                | 87.1 ms: 1.02x faster                                                           |
| scimark_fft                | 382 ms                                                 | 374 ms: 1.02x faster                                                            |
| mako                       | 11.9 ms                                                | 11.7 ms: 1.02x faster                                                           |
| sympy_expand               | 478 ms                                                 | 469 ms: 1.02x faster                                                            |
| mdp                        | 2.63 sec                                               | 2.58 sec: 1.02x faster                                                          |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                                            |
| pprint_pformat             | 1.57 sec                                               | 1.54 sec: 1.02x faster                                                          |
| meteor_contest             | 112 ms                                                 | 111 ms: 1.02x faster                                                            |
| 2to3                       | 274 ms                                                 | 270 ms: 1.01x faster                                                            |
| bench_thread_pool          | 842 us                                                 | 830 us: 1.01x faster                                                            |
| deepcopy                   | 371 us                                                 | 366 us: 1.01x faster                                                            |
| nqueens                    | 83.3 ms                                                | 82.4 ms: 1.01x faster                                                           |
| deepcopy_reduce            | 3.35 us                                                | 3.31 us: 1.01x faster                                                           |
| bench_mp_pool              | 24.0 ms                                                | 23.9 ms: 1.00x faster                                                           |
| sqlglot_optimize           | 54.8 ms                                                | 55.1 ms: 1.01x slower                                                           |
| docutils                   | 2.77 sec                                               | 2.79 sec: 1.01x slower                                                          |
| json_loads                 | 28.5 us                                                | 28.8 us: 1.01x slower                                                           |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                                            |
| json                       | 5.26 ms                                                | 5.31 ms: 1.01x slower                                                           |
| pickle_dict                | 35.5 us                                                | 35.9 us: 1.01x slower                                                           |
| spectral_norm              | 115 ms                                                 | 116 ms: 1.01x slower                                                            |
| python_startup_no_site     | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                           |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.15 ms: 1.02x slower                                                           |
| django_template            | 34.6 ms                                                | 35.3 ms: 1.02x slower                                                           |
| json_dumps                 | 10.4 ms                                                | 10.6 ms: 1.02x slower                                                           |
| unpickle_list              | 5.29 us                                                | 5.41 us: 1.02x slower                                                           |
| asyncio_websockets         | 551 ms                                                 | 566 ms: 1.03x slower                                                            |
| pycparser                  | 1.18 sec                                               | 1.21 sec: 1.03x slower                                                          |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.84 sec: 1.03x slower                                                          |
| asyncio_tcp                | 491 ms                                                 | 505 ms: 1.03x slower                                                            |
| pickle                     | 11.6 us                                                | 12.0 us: 1.04x slower                                                           |
| sqlite_synth               | 2.83 us                                                | 2.95 us: 1.04x slower                                                           |
| pickle_list                | 5.08 us                                                | 5.30 us: 1.04x slower                                                           |
| go                         | 139 ms                                                 | 146 ms: 1.05x slower                                                            |
| typing_runtime_protocols   | 158 us                                                 | 165 us: 1.05x slower                                                            |
| richards_super             | 51.5 ms                                                | 55.2 ms: 1.07x slower                                                           |
| richards                   | 45.8 ms                                                | 49.1 ms: 1.07x slower                                                           |
| regex_dna                  | 212 ms                                                 | 228 ms: 1.07x slower                                                            |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                           |
| regex_v8                   | 23.1 ms                                                | 26.0 ms: 1.12x slower                                                           |
| telco                      | 7.10 ms                                                | 8.45 ms: 1.19x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 1.78 ms: 1.21x slower                                                           |
| coverage                   | 72.7 ms                                                | 92.3 ms: 1.27x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                    |

Benchmark hidden because not significant (5): unpickle, xml_etree_iterparse, sqlglot_normalize, xml_etree_parse, regex_effbot
Ignored benchmarks (8) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240531-3.14.0a0-f748355/bm-20240531-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-f748355.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.97x