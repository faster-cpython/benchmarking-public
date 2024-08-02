# Results vs. 3.12.0

- fork: faster-cpython
- ref: flag_object_maybe_in
- machine: linux-x86_64
- commit hash: bb874c3
- commit date: 2024-06-07
- overall geometric mean: 1.03x faster
- HPT reliability: 99.76%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240607-linux-x86_64-faster%2dcpython-flag_object_maybe_in-3.14.0a0-bb874c3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 272 ms: 1.01x faster                                                            |
| docutils       | 2.77 sec                                               | 2.78 sec: 1.00x slower                                                          |
| tornado_http   | 103 ms                                                 | 94.8 ms: 1.08x faster                                                           |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240607-linux-x86_64-faster%2dcpython-flag_object_maybe_in-3.14.0a0-bb874c3 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 344 ms: 1.31x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 448 ms: 1.28x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 927 ms: 1.28x faster                                                            |
| async_tree_none            | 472 ms                                                 | 378 ms: 1.25x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 596 ms: 1.22x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 478 ms: 1.21x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 957 ms: 1.21x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 632 ms: 1.15x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240607-linux-x86_64-faster%2dcpython-flag_object_maybe_in-3.14.0a0-bb874c3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 79.7 ms: 1.06x faster                                                           |
| pidigits       | 187 ms                                                 | 190 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240607-linux-x86_64-faster%2dcpython-flag_object_maybe_in-3.14.0a0-bb874c3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 135 ms: 1.10x faster                                                            |
| regex_effbot   | 3.61 ms                                                | 3.74 ms: 1.04x slower                                                           |
| regex_dna      | 212 ms                                                 | 222 ms: 1.05x slower                                                            |
| regex_v8       | 23.1 ms                                                | 24.8 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240607-linux-x86_64-faster%2dcpython-flag_object_maybe_in-3.14.0a0-bb874c3 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.21 sec: 1.06x faster                                                          |
| pickle_dict          | 35.5 us                                                | 33.7 us: 1.06x faster                                                           |
| unpickle             | 15.9 us                                                | 15.2 us: 1.04x faster                                                           |
| pickle_pure_python   | 324 us                                                 | 312 us: 1.04x faster                                                            |
| unpickle_pure_python | 230 us                                                 | 223 us: 1.03x faster                                                            |
| xml_etree_generate   | 89.2 ms                                                | 87.3 ms: 1.02x faster                                                           |
| xml_etree_process    | 61.7 ms                                                | 61.1 ms: 1.01x faster                                                           |
| pickle               | 11.6 us                                                | 11.6 us: 1.00x slower                                                           |
| json_loads           | 28.5 us                                                | 28.8 us: 1.01x slower                                                           |
| xml_etree_iterparse  | 107 ms                                                 | 108 ms: 1.01x slower                                                            |
| pickle_list          | 5.08 us                                                | 5.15 us: 1.01x slower                                                           |
| unpickle_list        | 5.29 us                                                | 5.38 us: 1.02x slower                                                           |
| json_dumps           | 10.4 ms                                                | 10.6 ms: 1.02x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240607-linux-x86_64-faster%2dcpython-flag_object_maybe_in-3.14.0a0-bb874c3 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.12 ms: 1.03x slower                                                           |
| python_startup         | 9.55 ms                                                | 10.7 ms: 1.12x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240607-linux-x86_64-faster%2dcpython-flag_object_maybe_in-3.14.0a0-bb874c3 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.5 ms: 1.04x faster                                                           |
| django_template | 34.6 ms                                                | 35.3 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240607-linux-x86_64-faster%2dcpython-flag_object_maybe_in-3.14.0a0-bb874c3 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 344 ms: 1.31x faster                                                            |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.30x faster                                                           |
| async_tree_memoization_tg  | 575 ms                                                 | 448 ms: 1.28x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 927 ms: 1.28x faster                                                            |
| async_tree_none            | 472 ms                                                 | 378 ms: 1.25x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 596 ms: 1.22x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 478 ms: 1.21x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 957 ms: 1.21x faster                                                            |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.20x faster                                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 632 ms: 1.15x faster                                                            |
| raytrace                   | 312 ms                                                 | 273 ms: 1.14x faster                                                            |
| logging_format             | 7.23 us                                                | 6.48 us: 1.12x faster                                                           |
| deltablue                  | 3.72 ms                                                | 3.34 ms: 1.11x faster                                                           |
| logging_simple             | 6.46 us                                                | 5.87 us: 1.10x faster                                                           |
| regex_compile              | 148 ms                                                 | 135 ms: 1.10x faster                                                            |
| chaos                      | 67.0 ms                                                | 61.4 ms: 1.09x faster                                                           |
| tornado_http               | 103 ms                                                 | 94.8 ms: 1.08x faster                                                           |
| sympy_sum                  | 169 ms                                                 | 157 ms: 1.08x faster                                                            |
| scimark_monte_carlo        | 75.1 ms                                                | 70.3 ms: 1.07x faster                                                           |
| sympy_str                  | 300 ms                                                 | 281 ms: 1.06x faster                                                            |
| float                      | 84.7 ms                                                | 79.7 ms: 1.06x faster                                                           |
| crypto_pyaes               | 81.9 ms                                                | 77.2 ms: 1.06x faster                                                           |
| tomli_loads                | 2.33 sec                                               | 2.21 sec: 1.06x faster                                                          |
| pickle_dict                | 35.5 us                                                | 33.7 us: 1.06x faster                                                           |
| generators                 | 31.2 ms                                                | 29.6 ms: 1.05x faster                                                           |
| dulwich_log                | 68.5 ms                                                | 65.6 ms: 1.04x faster                                                           |
| unpickle                   | 15.9 us                                                | 15.2 us: 1.04x faster                                                           |
| pickle_pure_python         | 324 us                                                 | 312 us: 1.04x faster                                                            |
| sympy_integrate            | 21.4 ms                                                | 20.7 ms: 1.04x faster                                                           |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                                           |
| mako                       | 11.9 ms                                                | 11.5 ms: 1.04x faster                                                           |
| sqlglot_transpile          | 1.68 ms                                                | 1.63 ms: 1.03x faster                                                           |
| unpickle_pure_python       | 230 us                                                 | 223 us: 1.03x faster                                                            |
| async_generators           | 463 ms                                                 | 449 ms: 1.03x faster                                                            |
| nqueens                    | 83.3 ms                                                | 81.2 ms: 1.03x faster                                                           |
| xml_etree_generate         | 89.2 ms                                                | 87.3 ms: 1.02x faster                                                           |
| logging_silent             | 104 ns                                                 | 102 ns: 1.02x faster                                                            |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                          |
| mdp                        | 2.63 sec                                               | 2.59 sec: 1.02x faster                                                          |
| deepcopy_reduce            | 3.35 us                                                | 3.29 us: 1.02x faster                                                           |
| scimark_fft                | 382 ms                                                 | 376 ms: 1.02x faster                                                            |
| fannkuch                   | 417 ms                                                 | 411 ms: 1.01x faster                                                            |
| scimark_sor                | 129 ms                                                 | 127 ms: 1.01x faster                                                            |
| meteor_contest             | 112 ms                                                 | 111 ms: 1.01x faster                                                            |
| deepcopy_memo              | 40.7 us                                                | 40.2 us: 1.01x faster                                                           |
| hexiom                     | 6.41 ms                                                | 6.35 ms: 1.01x faster                                                           |
| xml_etree_process          | 61.7 ms                                                | 61.1 ms: 1.01x faster                                                           |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.01 ms: 1.01x faster                                                           |
| pprint_safe_repr           | 776 ms                                                 | 770 ms: 1.01x faster                                                            |
| sympy_expand               | 478 ms                                                 | 475 ms: 1.01x faster                                                            |
| 2to3                       | 274 ms                                                 | 272 ms: 1.01x faster                                                            |
| deepcopy                   | 371 us                                                 | 369 us: 1.01x faster                                                            |
| bench_mp_pool              | 24.0 ms                                                | 23.9 ms: 1.00x faster                                                           |
| bench_thread_pool          | 842 us                                                 | 840 us: 1.00x faster                                                            |
| gc_traversal               | 3.79 ms                                                | 3.79 ms: 1.00x faster                                                           |
| docutils                   | 2.77 sec                                               | 2.78 sec: 1.00x slower                                                          |
| pickle                     | 11.6 us                                                | 11.6 us: 1.00x slower                                                           |
| scimark_lu                 | 118 ms                                                 | 119 ms: 1.01x slower                                                            |
| sqlglot_normalize          | 110 ms                                                 | 111 ms: 1.01x slower                                                            |
| coroutines                 | 23.2 ms                                                | 23.3 ms: 1.01x slower                                                           |
| json_loads                 | 28.5 us                                                | 28.8 us: 1.01x slower                                                           |
| xml_etree_iterparse        | 107 ms                                                 | 108 ms: 1.01x slower                                                            |
| pickle_list                | 5.08 us                                                | 5.15 us: 1.01x slower                                                           |
| sqlglot_optimize           | 54.8 ms                                                | 55.6 ms: 1.01x slower                                                           |
| pidigits                   | 187 ms                                                 | 190 ms: 1.02x slower                                                            |
| unpickle_list              | 5.29 us                                                | 5.38 us: 1.02x slower                                                           |
| asyncio_tcp                | 491 ms                                                 | 500 ms: 1.02x slower                                                            |
| django_template            | 34.6 ms                                                | 35.3 ms: 1.02x slower                                                           |
| json_dumps                 | 10.4 ms                                                | 10.6 ms: 1.02x slower                                                           |
| json                       | 5.26 ms                                                | 5.38 ms: 1.02x slower                                                           |
| python_startup_no_site     | 6.94 ms                                                | 7.12 ms: 1.03x slower                                                           |
| spectral_norm              | 115 ms                                                 | 118 ms: 1.03x slower                                                            |
| asyncio_websockets         | 551 ms                                                 | 567 ms: 1.03x slower                                                            |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.84 sec: 1.03x slower                                                          |
| sqlite_synth               | 2.83 us                                                | 2.93 us: 1.03x slower                                                           |
| regex_effbot               | 3.61 ms                                                | 3.74 ms: 1.04x slower                                                           |
| typing_runtime_protocols   | 158 us                                                 | 165 us: 1.04x slower                                                            |
| regex_dna                  | 212 ms                                                 | 222 ms: 1.05x slower                                                            |
| go                         | 139 ms                                                 | 146 ms: 1.05x slower                                                            |
| pyflate                    | 482 ms                                                 | 514 ms: 1.06x slower                                                            |
| regex_v8                   | 23.1 ms                                                | 24.8 ms: 1.07x slower                                                           |
| richards                   | 45.8 ms                                                | 49.4 ms: 1.08x slower                                                           |
| richards_super             | 51.5 ms                                                | 56.0 ms: 1.09x slower                                                           |
| python_startup             | 9.55 ms                                                | 10.7 ms: 1.12x slower                                                           |
| telco                      | 7.10 ms                                                | 8.41 ms: 1.19x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 1.77 ms: 1.20x slower                                                           |
| coverage                   | 72.7 ms                                                | 92.4 ms: 1.27x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                    |

Benchmark hidden because not significant (4): dask, pprint_pformat, xml_etree_parse, nbody
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240607-3.14.0a0-bb874c3/bm-20240607-linux-x86_64-faster%2dcpython-flag_object_maybe_in-3.14.0a0-bb874c3.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.76% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.97x