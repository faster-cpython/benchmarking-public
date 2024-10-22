# Results vs. 3.12.0

- fork: brandtbucher
- ref: exit_operand
- machine: linux-x86_64
- commit hash: d4c66d7
- commit date: 2024-07-24
- overall geometric mean: 1.07x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240724-linux-x86_64-brandtbucher-exit_operand-3.14.0a0-d4c66d7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 274 ms: 1.00x faster                                                |
| docutils       | 2.77 sec                                               | 2.91 sec: 1.05x slower                                              |
| tornado_http   | 103 ms                                                 | 94.1 ms: 1.09x faster                                               |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240724-linux-x86_64-brandtbucher-exit_operand-3.14.0a0-d4c66d7 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 299 ms: 1.50x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 391 ms: 1.47x faster                                                |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 420 ms: 1.38x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 860 ms: 1.38x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 533 ms: 1.36x faster                                                |
| async_tree_io              | 1.16 sec                                               | 891 ms: 1.30x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 565 ms: 1.29x faster                                                |
| Geometric mean             | (ref)                                                  | 1.39x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240724-linux-x86_64-brandtbucher-exit_operand-3.14.0a0-d4c66d7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 80.4 ms: 1.21x faster                                               |
| float          | 84.7 ms                                                | 70.8 ms: 1.20x faster                                               |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                  | 1.13x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240724-linux-x86_64-brandtbucher-exit_operand-3.14.0a0-d4c66d7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 139 ms: 1.07x faster                                                |
| regex_dna      | 212 ms                                                 | 229 ms: 1.08x slower                                                |
| regex_effbot   | 3.61 ms                                                | 3.94 ms: 1.09x slower                                               |
| regex_v8       | 23.1 ms                                                | 25.3 ms: 1.09x slower                                               |
| Geometric mean | (ref)                                                  | 1.05x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240724-linux-x86_64-brandtbucher-exit_operand-3.14.0a0-d4c66d7 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.97 sec: 1.18x faster                                              |
| xml_etree_generate   | 89.2 ms                                                | 80.7 ms: 1.10x faster                                               |
| pickle_pure_python   | 324 us                                                 | 298 us: 1.09x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.08x faster                                                |
| xml_etree_process    | 61.7 ms                                                | 57.9 ms: 1.07x faster                                               |
| xml_etree_iterparse  | 107 ms                                                 | 100 ms: 1.06x faster                                                |
| unpickle_pure_python | 230 us                                                 | 218 us: 1.05x faster                                                |
| json_loads           | 28.5 us                                                | 28.2 us: 1.01x faster                                               |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                        |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240724-linux-x86_64-brandtbucher-exit_operand-3.14.0a0-d4c66d7 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.19 ms: 1.04x slower                                               |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                               |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240724-linux-x86_64-brandtbucher-exit_operand-3.14.0a0-d4c66d7 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.79 ms: 1.21x faster                                               |
| django_template | 34.6 ms                                                | 35.9 ms: 1.04x slower                                               |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240724-linux-x86_64-brandtbucher-exit_operand-3.14.0a0-d4c66d7 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 299 ms: 1.50x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 391 ms: 1.47x faster                                                |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                                |
| deepcopy_memo              | 40.7 us                                                | 29.4 us: 1.38x faster                                               |
| async_tree_memoization     | 578 ms                                                 | 420 ms: 1.38x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 860 ms: 1.38x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 533 ms: 1.36x faster                                                |
| deepcopy                   | 371 us                                                 | 277 us: 1.34x faster                                                |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                               |
| async_tree_io              | 1.16 sec                                               | 891 ms: 1.30x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 565 ms: 1.29x faster                                                |
| scimark_monte_carlo        | 75.1 ms                                                | 60.9 ms: 1.23x faster                                               |
| scimark_fft                | 382 ms                                                 | 313 ms: 1.22x faster                                                |
| mako                       | 11.9 ms                                                | 9.79 ms: 1.21x faster                                               |
| nbody                      | 97.0 ms                                                | 80.4 ms: 1.21x faster                                               |
| crypto_pyaes               | 81.9 ms                                                | 68.0 ms: 1.20x faster                                               |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                               |
| float                      | 84.7 ms                                                | 70.8 ms: 1.20x faster                                               |
| logging_format             | 7.23 us                                                | 6.10 us: 1.18x faster                                               |
| tomli_loads                | 2.33 sec                                               | 1.97 sec: 1.18x faster                                              |
| deepcopy_reduce            | 3.35 us                                                | 2.85 us: 1.17x faster                                               |
| logging_simple             | 6.46 us                                                | 5.54 us: 1.17x faster                                               |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.36 ms: 1.16x faster                                               |
| chaos                      | 67.0 ms                                                | 58.3 ms: 1.15x faster                                               |
| raytrace                   | 312 ms                                                 | 274 ms: 1.14x faster                                                |
| fannkuch                   | 417 ms                                                 | 368 ms: 1.13x faster                                                |
| richards                   | 45.8 ms                                                | 41.0 ms: 1.12x faster                                               |
| spectral_norm              | 115 ms                                                 | 104 ms: 1.11x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 80.7 ms: 1.10x faster                                               |
| pyflate                    | 482 ms                                                 | 437 ms: 1.10x faster                                                |
| richards_super             | 51.5 ms                                                | 47.1 ms: 1.09x faster                                               |
| tornado_http               | 103 ms                                                 | 94.1 ms: 1.09x faster                                               |
| pickle_pure_python         | 324 us                                                 | 298 us: 1.09x faster                                                |
| pprint_safe_repr           | 776 ms                                                 | 715 ms: 1.08x faster                                                |
| pprint_pformat             | 1.57 sec                                               | 1.45 sec: 1.08x faster                                              |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.08x faster                                                |
| xml_etree_process          | 61.7 ms                                                | 57.9 ms: 1.07x faster                                               |
| regex_compile              | 148 ms                                                 | 139 ms: 1.07x faster                                                |
| xml_etree_iterparse        | 107 ms                                                 | 100 ms: 1.06x faster                                                |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.06x faster                                               |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                |
| generators                 | 31.2 ms                                                | 29.4 ms: 1.06x faster                                               |
| unpickle_pure_python       | 230 us                                                 | 218 us: 1.05x faster                                                |
| sqlglot_transpile          | 1.68 ms                                                | 1.61 ms: 1.04x faster                                               |
| mdp                        | 2.63 sec                                               | 2.55 sec: 1.03x faster                                              |
| deltablue                  | 3.72 ms                                                | 3.64 ms: 1.02x faster                                               |
| gc_traversal               | 3.79 ms                                                | 3.72 ms: 1.02x faster                                               |
| dask                       | 372 ms                                                 | 366 ms: 1.02x faster                                                |
| json                       | 5.26 ms                                                | 5.18 ms: 1.02x faster                                               |
| json_loads                 | 28.5 us                                                | 28.2 us: 1.01x faster                                               |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                                |
| bench_thread_pool          | 842 us                                                 | 834 us: 1.01x faster                                                |
| 2to3                       | 274 ms                                                 | 274 ms: 1.00x faster                                                |
| logging_silent             | 104 ns                                                 | 105 ns: 1.00x slower                                                |
| scimark_sor                | 129 ms                                                 | 130 ms: 1.00x slower                                                |
| async_generators           | 463 ms                                                 | 465 ms: 1.00x slower                                                |
| sympy_sum                  | 169 ms                                                 | 170 ms: 1.01x slower                                                |
| asyncio_websockets         | 551 ms                                                 | 557 ms: 1.01x slower                                                |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                              |
| dulwich_log                | 68.5 ms                                                | 69.8 ms: 1.02x slower                                               |
| sqlglot_optimize           | 54.8 ms                                                | 56.1 ms: 1.02x slower                                               |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.02x slower                                                |
| asyncio_tcp                | 491 ms                                                 | 505 ms: 1.03x slower                                                |
| hexiom                     | 6.41 ms                                                | 6.62 ms: 1.03x slower                                               |
| django_template            | 34.6 ms                                                | 35.9 ms: 1.04x slower                                               |
| python_startup_no_site     | 6.94 ms                                                | 7.19 ms: 1.04x slower                                               |
| sympy_integrate            | 21.4 ms                                                | 22.3 ms: 1.04x slower                                               |
| docutils                   | 2.77 sec                                               | 2.91 sec: 1.05x slower                                              |
| sympy_expand               | 478 ms                                                 | 506 ms: 1.06x slower                                                |
| go                         | 139 ms                                                 | 148 ms: 1.06x slower                                                |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.07x slower                                                |
| nqueens                    | 83.3 ms                                                | 88.7 ms: 1.07x slower                                               |
| scimark_lu                 | 118 ms                                                 | 127 ms: 1.07x slower                                                |
| regex_dna                  | 212 ms                                                 | 229 ms: 1.08x slower                                                |
| regex_effbot               | 3.61 ms                                                | 3.94 ms: 1.09x slower                                               |
| regex_v8                   | 23.1 ms                                                | 25.3 ms: 1.09x slower                                               |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                               |
| telco                      | 7.10 ms                                                | 7.91 ms: 1.11x slower                                               |
| create_gc_cycles           | 1.48 ms                                                | 1.75 ms: 1.19x slower                                               |
| coverage                   | 72.7 ms                                                | 90.9 ms: 1.25x slower                                               |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                        |

Benchmark hidden because not significant (5): pycparser, sympy_str, coroutines, json_dumps, bench_mp_pool
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240724-3.14.0a0-d4c66d7-JIT/bm-20240724-linux-x86_64-brandtbucher-exit_operand-3.14.0a0-d4c66d7.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.03x