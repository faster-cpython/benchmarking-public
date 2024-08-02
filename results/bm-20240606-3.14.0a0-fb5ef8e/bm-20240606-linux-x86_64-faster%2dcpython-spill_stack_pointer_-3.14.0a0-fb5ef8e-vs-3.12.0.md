# Results vs. 3.12.0

- fork: faster-cpython
- ref: spill_stack_pointer_
- machine: linux-x86_64
- commit hash: fb5ef8e
- commit date: 2024-06-06
- overall geometric mean: 1.03x faster
- HPT reliability: 99.85%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240606-linux-x86_64-faster%2dcpython-spill_stack_pointer_-3.14.0a0-fb5ef8e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 271 ms: 1.01x faster                                                            |
| docutils       | 2.77 sec                                               | 2.80 sec: 1.01x slower                                                          |
| tornado_http   | 103 ms                                                 | 94.9 ms: 1.08x faster                                                           |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240606-linux-x86_64-faster%2dcpython-spill_stack_pointer_-3.14.0a0-fb5ef8e |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 350 ms: 1.28x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 449 ms: 1.28x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 583 ms: 1.25x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 952 ms: 1.24x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 477 ms: 1.21x faster                                                            |
| async_tree_none            | 472 ms                                                 | 391 ms: 1.21x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 960 ms: 1.20x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 621 ms: 1.17x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240606-linux-x86_64-faster%2dcpython-spill_stack_pointer_-3.14.0a0-fb5ef8e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 79.3 ms: 1.07x faster                                                           |
| nbody          | 97.0 ms                                                | 92.1 ms: 1.05x faster                                                           |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240606-linux-x86_64-faster%2dcpython-spill_stack_pointer_-3.14.0a0-fb5ef8e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 136 ms: 1.09x faster                                                            |
| regex_effbot   | 3.61 ms                                                | 3.67 ms: 1.02x slower                                                           |
| regex_dna      | 212 ms                                                 | 223 ms: 1.05x slower                                                            |
| regex_v8       | 23.1 ms                                                | 24.8 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240606-linux-x86_64-faster%2dcpython-spill_stack_pointer_-3.14.0a0-fb5ef8e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 324 us                                                 | 302 us: 1.07x faster                                                            |
| tomli_loads          | 2.33 sec                                               | 2.19 sec: 1.06x faster                                                          |
| unpickle             | 15.9 us                                                | 15.3 us: 1.04x faster                                                           |
| unpickle_pure_python | 230 us                                                 | 223 us: 1.03x faster                                                            |
| xml_etree_generate   | 89.2 ms                                                | 87.0 ms: 1.02x faster                                                           |
| xml_etree_process    | 61.7 ms                                                | 60.3 ms: 1.02x faster                                                           |
| pickle_list          | 5.08 us                                                | 5.04 us: 1.01x faster                                                           |
| pickle_dict          | 35.5 us                                                | 35.3 us: 1.01x faster                                                           |
| pickle               | 11.6 us                                                | 11.7 us: 1.01x slower                                                           |
| json_loads           | 28.5 us                                                | 28.8 us: 1.01x slower                                                           |
| json_dumps           | 10.4 ms                                                | 10.6 ms: 1.02x slower                                                           |
| unpickle_list        | 5.29 us                                                | 5.40 us: 1.02x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240606-linux-x86_64-faster%2dcpython-spill_stack_pointer_-3.14.0a0-fb5ef8e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.13 ms: 1.03x slower                                                           |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240606-linux-x86_64-faster%2dcpython-spill_stack_pointer_-3.14.0a0-fb5ef8e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.9 ms: 1.09x faster                                                           |
| django_template | 34.6 ms                                                | 36.1 ms: 1.04x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240606-linux-x86_64-faster%2dcpython-spill_stack_pointer_-3.14.0a0-fb5ef8e |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| comprehensions             | 21.8 us                                                | 16.9 us: 1.29x faster                                                           |
| async_tree_none_tg         | 450 ms                                                 | 350 ms: 1.28x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 449 ms: 1.28x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 583 ms: 1.25x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 952 ms: 1.24x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 477 ms: 1.21x faster                                                            |
| async_tree_none            | 472 ms                                                 | 391 ms: 1.21x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 960 ms: 1.20x faster                                                            |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                                           |
| raytrace                   | 312 ms                                                 | 264 ms: 1.18x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 621 ms: 1.17x faster                                                            |
| deltablue                  | 3.72 ms                                                | 3.26 ms: 1.14x faster                                                           |
| generators                 | 31.2 ms                                                | 27.9 ms: 1.12x faster                                                           |
| logging_format             | 7.23 us                                                | 6.55 us: 1.10x faster                                                           |
| chaos                      | 67.0 ms                                                | 60.8 ms: 1.10x faster                                                           |
| logging_simple             | 6.46 us                                                | 5.89 us: 1.10x faster                                                           |
| scimark_monte_carlo        | 75.1 ms                                                | 68.5 ms: 1.10x faster                                                           |
| regex_compile              | 148 ms                                                 | 136 ms: 1.09x faster                                                            |
| mako                       | 11.9 ms                                                | 10.9 ms: 1.09x faster                                                           |
| tornado_http               | 103 ms                                                 | 94.9 ms: 1.08x faster                                                           |
| sympy_sum                  | 169 ms                                                 | 157 ms: 1.08x faster                                                            |
| pickle_pure_python         | 324 us                                                 | 302 us: 1.07x faster                                                            |
| crypto_pyaes               | 81.9 ms                                                | 76.4 ms: 1.07x faster                                                           |
| float                      | 84.7 ms                                                | 79.3 ms: 1.07x faster                                                           |
| tomli_loads                | 2.33 sec                                               | 2.19 sec: 1.06x faster                                                          |
| sympy_str                  | 300 ms                                                 | 282 ms: 1.06x faster                                                            |
| nbody                      | 97.0 ms                                                | 92.1 ms: 1.05x faster                                                           |
| fannkuch                   | 417 ms                                                 | 399 ms: 1.05x faster                                                            |
| sympy_integrate            | 21.4 ms                                                | 20.5 ms: 1.04x faster                                                           |
| pprint_safe_repr           | 776 ms                                                 | 745 ms: 1.04x faster                                                            |
| dulwich_log                | 68.5 ms                                                | 65.8 ms: 1.04x faster                                                           |
| hexiom                     | 6.41 ms                                                | 6.16 ms: 1.04x faster                                                           |
| unpickle                   | 15.9 us                                                | 15.3 us: 1.04x faster                                                           |
| unpickle_pure_python       | 230 us                                                 | 223 us: 1.03x faster                                                            |
| deepcopy_memo              | 40.7 us                                                | 39.5 us: 1.03x faster                                                           |
| sqlglot_transpile          | 1.68 ms                                                | 1.64 ms: 1.03x faster                                                           |
| pprint_pformat             | 1.57 sec                                               | 1.53 sec: 1.03x faster                                                          |
| nqueens                    | 83.3 ms                                                | 81.3 ms: 1.03x faster                                                           |
| xml_etree_generate         | 89.2 ms                                                | 87.0 ms: 1.02x faster                                                           |
| scimark_sor                | 129 ms                                                 | 126 ms: 1.02x faster                                                            |
| xml_etree_process          | 61.7 ms                                                | 60.3 ms: 1.02x faster                                                           |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                                            |
| sqlglot_parse              | 1.36 ms                                                | 1.34 ms: 1.02x faster                                                           |
| meteor_contest             | 112 ms                                                 | 110 ms: 1.02x faster                                                            |
| bench_thread_pool          | 842 us                                                 | 828 us: 1.02x faster                                                            |
| deepcopy_reduce            | 3.35 us                                                | 3.30 us: 1.02x faster                                                           |
| deepcopy                   | 371 us                                                 | 366 us: 1.01x faster                                                            |
| 2to3                       | 274 ms                                                 | 271 ms: 1.01x faster                                                            |
| async_generators           | 463 ms                                                 | 458 ms: 1.01x faster                                                            |
| pickle_list                | 5.08 us                                                | 5.04 us: 1.01x faster                                                           |
| pycparser                  | 1.18 sec                                               | 1.17 sec: 1.01x faster                                                          |
| scimark_fft                | 382 ms                                                 | 379 ms: 1.01x faster                                                            |
| logging_silent             | 104 ns                                                 | 104 ns: 1.01x faster                                                            |
| pickle_dict                | 35.5 us                                                | 35.3 us: 1.01x faster                                                           |
| sqlglot_normalize          | 110 ms                                                 | 111 ms: 1.00x slower                                                            |
| pyflate                    | 482 ms                                                 | 486 ms: 1.01x slower                                                            |
| pickle                     | 11.6 us                                                | 11.7 us: 1.01x slower                                                           |
| sqlglot_optimize           | 54.8 ms                                                | 55.4 ms: 1.01x slower                                                           |
| json_loads                 | 28.5 us                                                | 28.8 us: 1.01x slower                                                           |
| spectral_norm              | 115 ms                                                 | 116 ms: 1.01x slower                                                            |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                                            |
| docutils                   | 2.77 sec                                               | 2.80 sec: 1.01x slower                                                          |
| regex_effbot               | 3.61 ms                                                | 3.67 ms: 1.02x slower                                                           |
| json_dumps                 | 10.4 ms                                                | 10.6 ms: 1.02x slower                                                           |
| unpickle_list              | 5.29 us                                                | 5.40 us: 1.02x slower                                                           |
| asyncio_websockets         | 551 ms                                                 | 564 ms: 1.02x slower                                                            |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.17 ms: 1.02x slower                                                           |
| json                       | 5.26 ms                                                | 5.39 ms: 1.02x slower                                                           |
| python_startup_no_site     | 6.94 ms                                                | 7.13 ms: 1.03x slower                                                           |
| mdp                        | 2.63 sec                                               | 2.71 sec: 1.03x slower                                                          |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.85 sec: 1.03x slower                                                          |
| asyncio_tcp                | 491 ms                                                 | 509 ms: 1.04x slower                                                            |
| go                         | 139 ms                                                 | 145 ms: 1.04x slower                                                            |
| django_template            | 34.6 ms                                                | 36.1 ms: 1.04x slower                                                           |
| sqlite_synth               | 2.83 us                                                | 2.97 us: 1.05x slower                                                           |
| richards_super             | 51.5 ms                                                | 54.0 ms: 1.05x slower                                                           |
| regex_dna                  | 212 ms                                                 | 223 ms: 1.05x slower                                                            |
| richards                   | 45.8 ms                                                | 48.3 ms: 1.05x slower                                                           |
| gc_traversal               | 3.79 ms                                                | 4.00 ms: 1.05x slower                                                           |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.07x slower                                                            |
| regex_v8                   | 23.1 ms                                                | 24.8 ms: 1.07x slower                                                           |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                           |
| telco                      | 7.10 ms                                                | 8.50 ms: 1.20x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 1.80 ms: 1.22x slower                                                           |
| coverage                   | 72.7 ms                                                | 94.2 ms: 1.30x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                    |

Benchmark hidden because not significant (6): xml_etree_parse, sympy_expand, bench_mp_pool, coroutines, xml_etree_iterparse, dask
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240606-3.14.0a0-fb5ef8e/bm-20240606-linux-x86_64-faster%2dcpython-spill_stack_pointer_-3.14.0a0-fb5ef8e.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.85% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.97x