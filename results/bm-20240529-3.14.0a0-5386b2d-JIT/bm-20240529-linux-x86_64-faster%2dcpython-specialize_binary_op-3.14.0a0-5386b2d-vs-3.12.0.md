# Results vs. 3.12.0

- fork: faster-cpython
- ref: specialize_binary_op
- machine: linux-x86_64
- commit hash: 5386b2d
- commit date: 2024-05-29
- overall geometric mean: 1.03x faster
- HPT reliability: 91.82%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240529-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-5386b2d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 279 ms: 1.02x slower                                                            |
| docutils       | 2.77 sec                                               | 2.92 sec: 1.06x slower                                                          |
| tornado_http   | 103 ms                                                 | 96.6 ms: 1.06x faster                                                           |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240529-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-5386b2d |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 334 ms: 1.35x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 444 ms: 1.29x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 942 ms: 1.26x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 464 ms: 1.24x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 584 ms: 1.24x faster                                                            |
| async_tree_none            | 472 ms                                                 | 384 ms: 1.23x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 958 ms: 1.21x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 615 ms: 1.18x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.25x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240529-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-5386b2d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 80.8 ms: 1.20x faster                                                           |
| float          | 84.7 ms                                                | 71.7 ms: 1.18x faster                                                           |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240529-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-5386b2d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 137 ms: 1.08x faster                                                            |
| regex_effbot   | 3.61 ms                                                | 3.69 ms: 1.02x slower                                                           |
| regex_v8       | 23.1 ms                                                | 24.1 ms: 1.04x slower                                                           |
| regex_dna      | 212 ms                                                 | 229 ms: 1.08x slower                                                            |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240529-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-5386b2d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.09 sec: 1.12x faster                                                          |
| xml_etree_generate   | 89.2 ms                                                | 82.0 ms: 1.09x faster                                                           |
| pickle_pure_python   | 324 us                                                 | 300 us: 1.08x faster                                                            |
| unpickle             | 15.9 us                                                | 14.7 us: 1.08x faster                                                           |
| xml_etree_parse      | 159 ms                                                 | 150 ms: 1.07x faster                                                            |
| xml_etree_iterparse  | 107 ms                                                 | 100 ms: 1.06x faster                                                            |
| xml_etree_process    | 61.7 ms                                                | 58.2 ms: 1.06x faster                                                           |
| unpickle_pure_python | 230 us                                                 | 222 us: 1.03x faster                                                            |
| json_dumps           | 10.4 ms                                                | 10.4 ms: 1.00x slower                                                           |
| json_loads           | 28.5 us                                                | 28.7 us: 1.01x slower                                                           |
| pickle_dict          | 35.5 us                                                | 36.0 us: 1.01x slower                                                           |
| pickle_list          | 5.08 us                                                | 5.26 us: 1.03x slower                                                           |
| unpickle_list        | 5.29 us                                                | 5.48 us: 1.04x slower                                                           |
| pickle               | 11.6 us                                                | 12.1 us: 1.04x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240529-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-5386b2d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.59 ms: 1.09x slower                                                           |
| python_startup         | 9.55 ms                                                | 11.1 ms: 1.16x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240529-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-5386b2d |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.2 ms: 1.17x faster                                                           |
| django_template | 34.6 ms                                                | 36.1 ms: 1.04x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240529-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-5386b2d |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 334 ms: 1.35x faster                                                            |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                           |
| async_tree_memoization_tg  | 575 ms                                                 | 444 ms: 1.29x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 942 ms: 1.26x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 464 ms: 1.24x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 584 ms: 1.24x faster                                                            |
| async_tree_none            | 472 ms                                                 | 384 ms: 1.23x faster                                                            |
| crypto_pyaes               | 81.9 ms                                                | 67.6 ms: 1.21x faster                                                           |
| async_tree_io              | 1.16 sec                                               | 958 ms: 1.21x faster                                                            |
| scimark_monte_carlo        | 75.1 ms                                                | 62.5 ms: 1.20x faster                                                           |
| nbody                      | 97.0 ms                                                | 80.8 ms: 1.20x faster                                                           |
| float                      | 84.7 ms                                                | 71.7 ms: 1.18x faster                                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 615 ms: 1.18x faster                                                            |
| mako                       | 11.9 ms                                                | 10.2 ms: 1.17x faster                                                           |
| fannkuch                   | 417 ms                                                 | 356 ms: 1.17x faster                                                            |
| pathlib                    | 19.3 ms                                                | 16.6 ms: 1.17x faster                                                           |
| logging_format             | 7.23 us                                                | 6.20 us: 1.17x faster                                                           |
| logging_simple             | 6.46 us                                                | 5.65 us: 1.14x faster                                                           |
| scimark_fft                | 382 ms                                                 | 335 ms: 1.14x faster                                                            |
| chaos                      | 67.0 ms                                                | 58.9 ms: 1.14x faster                                                           |
| tomli_loads                | 2.33 sec                                               | 2.09 sec: 1.12x faster                                                          |
| pprint_safe_repr           | 776 ms                                                 | 705 ms: 1.10x faster                                                            |
| richards                   | 45.8 ms                                                | 41.7 ms: 1.10x faster                                                           |
| raytrace                   | 312 ms                                                 | 284 ms: 1.10x faster                                                            |
| xml_etree_generate         | 89.2 ms                                                | 82.0 ms: 1.09x faster                                                           |
| pprint_pformat             | 1.57 sec                                               | 1.45 sec: 1.08x faster                                                          |
| regex_compile              | 148 ms                                                 | 137 ms: 1.08x faster                                                            |
| pickle_pure_python         | 324 us                                                 | 300 us: 1.08x faster                                                            |
| pyflate                    | 482 ms                                                 | 448 ms: 1.08x faster                                                            |
| richards_super             | 51.5 ms                                                | 47.9 ms: 1.08x faster                                                           |
| unpickle                   | 15.9 us                                                | 14.7 us: 1.08x faster                                                           |
| xml_etree_parse            | 159 ms                                                 | 150 ms: 1.07x faster                                                            |
| xml_etree_iterparse        | 107 ms                                                 | 100 ms: 1.06x faster                                                            |
| tornado_http               | 103 ms                                                 | 96.6 ms: 1.06x faster                                                           |
| xml_etree_process          | 61.7 ms                                                | 58.2 ms: 1.06x faster                                                           |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.82 ms: 1.05x faster                                                           |
| unpickle_pure_python       | 230 us                                                 | 222 us: 1.03x faster                                                            |
| generators                 | 31.2 ms                                                | 30.3 ms: 1.03x faster                                                           |
| coroutines                 | 23.2 ms                                                | 22.5 ms: 1.03x faster                                                           |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                            |
| sqlglot_parse              | 1.36 ms                                                | 1.34 ms: 1.01x faster                                                           |
| pycparser                  | 1.18 sec                                               | 1.17 sec: 1.01x faster                                                          |
| sqlglot_transpile          | 1.68 ms                                                | 1.67 ms: 1.01x faster                                                           |
| json_dumps                 | 10.4 ms                                                | 10.4 ms: 1.00x slower                                                           |
| json_loads                 | 28.5 us                                                | 28.7 us: 1.01x slower                                                           |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                                            |
| deepcopy                   | 371 us                                                 | 374 us: 1.01x slower                                                            |
| async_generators           | 463 ms                                                 | 468 ms: 1.01x slower                                                            |
| dulwich_log                | 68.5 ms                                                | 69.3 ms: 1.01x slower                                                           |
| pickle_dict                | 35.5 us                                                | 36.0 us: 1.01x slower                                                           |
| dask                       | 372 ms                                                 | 378 ms: 1.02x slower                                                            |
| 2to3                       | 274 ms                                                 | 279 ms: 1.02x slower                                                            |
| regex_effbot               | 3.61 ms                                                | 3.69 ms: 1.02x slower                                                           |
| deltablue                  | 3.72 ms                                                | 3.80 ms: 1.02x slower                                                           |
| sympy_sum                  | 169 ms                                                 | 173 ms: 1.02x slower                                                            |
| spectral_norm              | 115 ms                                                 | 118 ms: 1.02x slower                                                            |
| sqlite_synth               | 2.83 us                                                | 2.90 us: 1.03x slower                                                           |
| asyncio_websockets         | 551 ms                                                 | 567 ms: 1.03x slower                                                            |
| logging_silent             | 104 ns                                                 | 108 ns: 1.03x slower                                                            |
| bench_thread_pool          | 842 us                                                 | 870 us: 1.03x slower                                                            |
| sqlglot_normalize          | 110 ms                                                 | 114 ms: 1.03x slower                                                            |
| pickle_list                | 5.08 us                                                | 5.26 us: 1.03x slower                                                           |
| unpickle_list              | 5.29 us                                                | 5.48 us: 1.04x slower                                                           |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.86 sec: 1.04x slower                                                          |
| hexiom                     | 6.41 ms                                                | 6.67 ms: 1.04x slower                                                           |
| regex_v8                   | 23.1 ms                                                | 24.1 ms: 1.04x slower                                                           |
| nqueens                    | 83.3 ms                                                | 86.7 ms: 1.04x slower                                                           |
| sqlglot_optimize           | 54.8 ms                                                | 57.1 ms: 1.04x slower                                                           |
| pickle                     | 11.6 us                                                | 12.1 us: 1.04x slower                                                           |
| mdp                        | 2.63 sec                                               | 2.74 sec: 1.04x slower                                                          |
| django_template            | 34.6 ms                                                | 36.1 ms: 1.04x slower                                                           |
| sympy_integrate            | 21.4 ms                                                | 22.5 ms: 1.05x slower                                                           |
| scimark_sor                | 129 ms                                                 | 136 ms: 1.05x slower                                                            |
| asyncio_tcp                | 491 ms                                                 | 518 ms: 1.06x slower                                                            |
| docutils                   | 2.77 sec                                               | 2.92 sec: 1.06x slower                                                          |
| go                         | 139 ms                                                 | 148 ms: 1.06x slower                                                            |
| sympy_expand               | 478 ms                                                 | 509 ms: 1.06x slower                                                            |
| gc_traversal               | 3.79 ms                                                | 4.04 ms: 1.07x slower                                                           |
| regex_dna                  | 212 ms                                                 | 229 ms: 1.08x slower                                                            |
| typing_runtime_protocols   | 158 us                                                 | 171 us: 1.08x slower                                                            |
| scimark_lu                 | 118 ms                                                 | 128 ms: 1.08x slower                                                            |
| python_startup_no_site     | 6.94 ms                                                | 7.59 ms: 1.09x slower                                                           |
| telco                      | 7.10 ms                                                | 8.16 ms: 1.15x slower                                                           |
| python_startup             | 9.55 ms                                                | 11.1 ms: 1.16x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 1.80 ms: 1.22x slower                                                           |
| coverage                   | 72.7 ms                                                | 93.8 ms: 1.29x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                    |

Benchmark hidden because not significant (5): deepcopy_memo, bench_mp_pool, json, sympy_str, deepcopy_reduce
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240529-3.14.0a0-5386b2d-JIT/bm-20240529-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-5386b2d.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 91.82% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x