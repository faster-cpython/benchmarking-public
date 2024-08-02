# Results vs. 3.12.0

- fork: faster-cpython
- ref: specialize_binary_op
- machine: linux-x86_64
- commit hash: 881df50
- commit date: 2024-05-23
- overall geometric mean: 1.03x faster
- HPT reliability: 99.92%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 271 ms: 1.01x faster                                                            |
| chameleon      | 7.41 ms                                                | 7.03 ms: 1.05x faster                                                           |
| docutils       | 2.77 sec                                               | 2.78 sec: 1.01x slower                                                          |
| tornado_http   | 103 ms                                                 | 94.1 ms: 1.09x faster                                                           |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 349 ms: 1.29x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 451 ms: 1.28x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 464 ms: 1.25x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 950 ms: 1.24x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 583 ms: 1.24x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 933 ms: 1.24x faster                                                            |
| async_tree_none            | 472 ms                                                 | 383 ms: 1.23x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 613 ms: 1.18x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 78.5 ms: 1.08x faster                                                           |
| pidigits       | 187 ms                                                 | 191 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 133 ms: 1.12x faster                                                            |
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                                            |
| regex_v8       | 23.1 ms                                                | 24.2 ms: 1.05x slower                                                           |
| regex_effbot   | 3.61 ms                                                | 3.85 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.18 sec: 1.07x faster                                                          |
| pickle_pure_python   | 324 us                                                 | 309 us: 1.05x faster                                                            |
| unpickle             | 15.9 us                                                | 15.2 us: 1.04x faster                                                           |
| xml_etree_generate   | 89.2 ms                                                | 85.8 ms: 1.04x faster                                                           |
| unpickle_pure_python | 230 us                                                 | 222 us: 1.04x faster                                                            |
| xml_etree_process    | 61.7 ms                                                | 60.0 ms: 1.03x faster                                                           |
| pickle_dict          | 35.5 us                                                | 35.9 us: 1.01x slower                                                           |
| unpickle_list        | 5.29 us                                                | 5.35 us: 1.01x slower                                                           |
| json_dumps           | 10.4 ms                                                | 10.6 ms: 1.02x slower                                                           |
| json_loads           | 28.5 us                                                | 29.1 us: 1.02x slower                                                           |
| pickle_list          | 5.08 us                                                | 5.19 us: 1.02x slower                                                           |
| pickle               | 11.6 us                                                | 12.0 us: 1.04x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.11 ms: 1.02x slower                                                           |
| python_startup         | 9.55 ms                                                | 10.4 ms: 1.09x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako           | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                           |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                           |
| async_tree_none_tg         | 450 ms                                                 | 349 ms: 1.29x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 451 ms: 1.28x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 464 ms: 1.25x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 950 ms: 1.24x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 583 ms: 1.24x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 933 ms: 1.24x faster                                                            |
| async_tree_none            | 472 ms                                                 | 383 ms: 1.23x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 613 ms: 1.18x faster                                                            |
| pathlib                    | 19.3 ms                                                | 16.6 ms: 1.17x faster                                                           |
| deltablue                  | 3.72 ms                                                | 3.23 ms: 1.15x faster                                                           |
| logging_format             | 7.23 us                                                | 6.39 us: 1.13x faster                                                           |
| crypto_pyaes               | 81.9 ms                                                | 72.4 ms: 1.13x faster                                                           |
| raytrace                   | 312 ms                                                 | 277 ms: 1.13x faster                                                            |
| regex_compile              | 148 ms                                                 | 133 ms: 1.12x faster                                                            |
| logging_simple             | 6.46 us                                                | 5.82 us: 1.11x faster                                                           |
| sympy_sum                  | 169 ms                                                 | 155 ms: 1.09x faster                                                            |
| tornado_http               | 103 ms                                                 | 94.1 ms: 1.09x faster                                                           |
| chaos                      | 67.0 ms                                                | 61.7 ms: 1.09x faster                                                           |
| float                      | 84.7 ms                                                | 78.5 ms: 1.08x faster                                                           |
| scimark_monte_carlo        | 75.1 ms                                                | 69.6 ms: 1.08x faster                                                           |
| sympy_str                  | 300 ms                                                 | 279 ms: 1.07x faster                                                            |
| tomli_loads                | 2.33 sec                                               | 2.18 sec: 1.07x faster                                                          |
| mako                       | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                           |
| spectral_norm              | 115 ms                                                 | 108 ms: 1.07x faster                                                            |
| chameleon                  | 7.41 ms                                                | 7.03 ms: 1.05x faster                                                           |
| generators                 | 31.2 ms                                                | 29.7 ms: 1.05x faster                                                           |
| sympy_integrate            | 21.4 ms                                                | 20.4 ms: 1.05x faster                                                           |
| pickle_pure_python         | 324 us                                                 | 309 us: 1.05x faster                                                            |
| dulwich_log                | 68.5 ms                                                | 65.6 ms: 1.04x faster                                                           |
| unpickle                   | 15.9 us                                                | 15.2 us: 1.04x faster                                                           |
| sqlglot_transpile          | 1.68 ms                                                | 1.62 ms: 1.04x faster                                                           |
| async_generators           | 463 ms                                                 | 444 ms: 1.04x faster                                                            |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                                           |
| xml_etree_generate         | 89.2 ms                                                | 85.8 ms: 1.04x faster                                                           |
| unpickle_pure_python       | 230 us                                                 | 222 us: 1.04x faster                                                            |
| pprint_safe_repr           | 776 ms                                                 | 748 ms: 1.04x faster                                                            |
| xml_etree_process          | 61.7 ms                                                | 60.0 ms: 1.03x faster                                                           |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                            |
| pprint_pformat             | 1.57 sec                                               | 1.53 sec: 1.03x faster                                                          |
| nqueens                    | 83.3 ms                                                | 81.3 ms: 1.02x faster                                                           |
| deepcopy_reduce            | 3.35 us                                                | 3.27 us: 1.02x faster                                                           |
| pyflate                    | 482 ms                                                 | 472 ms: 1.02x faster                                                            |
| sympy_expand               | 478 ms                                                 | 468 ms: 1.02x faster                                                            |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                          |
| fannkuch                   | 417 ms                                                 | 410 ms: 1.02x faster                                                            |
| deepcopy                   | 371 us                                                 | 365 us: 1.02x faster                                                            |
| deepcopy_memo              | 40.7 us                                                | 40.0 us: 1.02x faster                                                           |
| hexiom                     | 6.41 ms                                                | 6.32 ms: 1.01x faster                                                           |
| 2to3                       | 274 ms                                                 | 271 ms: 1.01x faster                                                            |
| bench_thread_pool          | 842 us                                                 | 831 us: 1.01x faster                                                            |
| sqlglot_normalize          | 110 ms                                                 | 109 ms: 1.01x faster                                                            |
| bench_mp_pool              | 24.0 ms                                                | 23.8 ms: 1.01x faster                                                           |
| logging_silent             | 104 ns                                                 | 104 ns: 1.01x faster                                                            |
| gc_traversal               | 3.79 ms                                                | 3.78 ms: 1.01x faster                                                           |
| sqlglot_optimize           | 54.8 ms                                                | 54.6 ms: 1.00x faster                                                           |
| mdp                        | 2.63 sec                                               | 2.64 sec: 1.00x slower                                                          |
| docutils                   | 2.77 sec                                               | 2.78 sec: 1.01x slower                                                          |
| json                       | 5.26 ms                                                | 5.32 ms: 1.01x slower                                                           |
| pickle_dict                | 35.5 us                                                | 35.9 us: 1.01x slower                                                           |
| unpickle_list              | 5.29 us                                                | 5.35 us: 1.01x slower                                                           |
| pidigits                   | 187 ms                                                 | 191 ms: 1.02x slower                                                            |
| json_dumps                 | 10.4 ms                                                | 10.6 ms: 1.02x slower                                                           |
| json_loads                 | 28.5 us                                                | 29.1 us: 1.02x slower                                                           |
| go                         | 139 ms                                                 | 142 ms: 1.02x slower                                                            |
| scimark_fft                | 382 ms                                                 | 390 ms: 1.02x slower                                                            |
| pickle_list                | 5.08 us                                                | 5.19 us: 1.02x slower                                                           |
| python_startup_no_site     | 6.94 ms                                                | 7.11 ms: 1.02x slower                                                           |
| scimark_sor                | 129 ms                                                 | 133 ms: 1.03x slower                                                            |
| typing_runtime_protocols   | 158 us                                                 | 163 us: 1.03x slower                                                            |
| asyncio_websockets         | 551 ms                                                 | 569 ms: 1.03x slower                                                            |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.85 sec: 1.03x slower                                                          |
| pickle                     | 11.6 us                                                | 12.0 us: 1.04x slower                                                           |
| asyncio_tcp                | 491 ms                                                 | 509 ms: 1.04x slower                                                            |
| regex_dna                  | 212 ms                                                 | 221 ms: 1.04x slower                                                            |
| sqlite_synth               | 2.83 us                                                | 2.96 us: 1.04x slower                                                           |
| richards                   | 45.8 ms                                                | 47.9 ms: 1.04x slower                                                           |
| regex_v8                   | 23.1 ms                                                | 24.2 ms: 1.05x slower                                                           |
| coroutines                 | 23.2 ms                                                | 24.3 ms: 1.05x slower                                                           |
| richards_super             | 51.5 ms                                                | 54.1 ms: 1.05x slower                                                           |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.31 ms: 1.05x slower                                                           |
| regex_effbot               | 3.61 ms                                                | 3.85 ms: 1.07x slower                                                           |
| python_startup             | 9.55 ms                                                | 10.4 ms: 1.09x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 1.78 ms: 1.20x slower                                                           |
| telco                      | 7.10 ms                                                | 8.57 ms: 1.21x slower                                                           |
| coverage                   | 72.7 ms                                                | 92.4 ms: 1.27x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                    |

Benchmark hidden because not significant (6): dask, xml_etree_iterparse, nbody, scimark_lu, django_template, xml_etree_parse
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240523-3.14.0a0-881df50/bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.92% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.97x