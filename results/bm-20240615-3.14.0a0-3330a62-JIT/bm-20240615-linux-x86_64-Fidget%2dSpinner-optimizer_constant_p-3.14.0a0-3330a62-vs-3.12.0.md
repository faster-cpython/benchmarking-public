# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: optimizer_constant_p
- machine: linux-x86_64
- commit hash: 3330a62
- commit date: 2024-06-15
- overall geometric mean: 1.05x faster
- HPT reliability: 96.63%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240615-linux-x86_64-Fidget%2dSpinner-optimizer_constant_p-3.14.0a0-3330a62 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 281 ms: 1.02x slower                                                            |
| docutils       | 2.77 sec                                               | 2.92 sec: 1.05x slower                                                          |
| tornado_http   | 103 ms                                                 | 96.2 ms: 1.07x faster                                                           |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240615-linux-x86_64-Fidget%2dSpinner-optimizer_constant_p-3.14.0a0-3330a62 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 346 ms: 1.30x faster                                                            |
| async_tree_none            | 472 ms                                                 | 374 ms: 1.26x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 459 ms: 1.25x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 582 ms: 1.25x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 949 ms: 1.22x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 492 ms: 1.17x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 620 ms: 1.17x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 1.02 sec: 1.16x faster                                                          |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240615-linux-x86_64-Fidget%2dSpinner-optimizer_constant_p-3.14.0a0-3330a62 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 80.4 ms: 1.21x faster                                                           |
| float          | 84.7 ms                                                | 71.9 ms: 1.18x faster                                                           |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240615-linux-x86_64-Fidget%2dSpinner-optimizer_constant_p-3.14.0a0-3330a62 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 137 ms: 1.09x faster                                                            |
| regex_effbot   | 3.61 ms                                                | 3.59 ms: 1.01x faster                                                           |
| regex_v8       | 23.1 ms                                                | 23.7 ms: 1.02x slower                                                           |
| regex_dna      | 212 ms                                                 | 226 ms: 1.06x slower                                                            |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240615-linux-x86_64-Fidget%2dSpinner-optimizer_constant_p-3.14.0a0-3330a62 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.98 sec: 1.18x faster                                                          |
| pickle_pure_python   | 324 us                                                 | 295 us: 1.10x faster                                                            |
| xml_etree_generate   | 89.2 ms                                                | 82.5 ms: 1.08x faster                                                           |
| xml_etree_process    | 61.7 ms                                                | 58.2 ms: 1.06x faster                                                           |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.05x faster                                                            |
| xml_etree_parse      | 159 ms                                                 | 152 ms: 1.05x faster                                                            |
| unpickle             | 15.9 us                                                | 15.1 us: 1.05x faster                                                           |
| unpickle_pure_python | 230 us                                                 | 221 us: 1.04x faster                                                            |
| unpickle_list        | 5.29 us                                                | 5.25 us: 1.01x faster                                                           |
| pickle_dict          | 35.5 us                                                | 35.4 us: 1.00x faster                                                           |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                           |
| json_loads           | 28.5 us                                                | 28.9 us: 1.01x slower                                                           |
| pickle_list          | 5.08 us                                                | 5.19 us: 1.02x slower                                                           |
| pickle               | 11.6 us                                                | 12.2 us: 1.05x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240615-linux-x86_64-Fidget%2dSpinner-optimizer_constant_p-3.14.0a0-3330a62 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.65 ms: 1.10x slower                                                           |
| python_startup         | 9.55 ms                                                | 11.2 ms: 1.17x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.14x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240615-linux-x86_64-Fidget%2dSpinner-optimizer_constant_p-3.14.0a0-3330a62 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.0 ms: 1.18x faster                                                           |
| django_template | 34.6 ms                                                | 37.0 ms: 1.07x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240615-linux-x86_64-Fidget%2dSpinner-optimizer_constant_p-3.14.0a0-3330a62 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 28.9 us: 1.41x faster                                                           |
| deepcopy                   | 371 us                                                 | 272 us: 1.37x faster                                                            |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                           |
| async_tree_none_tg         | 450 ms                                                 | 346 ms: 1.30x faster                                                            |
| async_tree_none            | 472 ms                                                 | 374 ms: 1.26x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 459 ms: 1.25x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 582 ms: 1.25x faster                                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.74 us: 1.22x faster                                                           |
| scimark_monte_carlo        | 75.1 ms                                                | 61.7 ms: 1.22x faster                                                           |
| async_tree_io              | 1.16 sec                                               | 949 ms: 1.22x faster                                                            |
| scimark_fft                | 382 ms                                                 | 315 ms: 1.21x faster                                                            |
| nbody                      | 97.0 ms                                                | 80.4 ms: 1.21x faster                                                           |
| crypto_pyaes               | 81.9 ms                                                | 68.2 ms: 1.20x faster                                                           |
| mako                       | 11.9 ms                                                | 10.0 ms: 1.18x faster                                                           |
| tomli_loads                | 2.33 sec                                               | 1.98 sec: 1.18x faster                                                          |
| float                      | 84.7 ms                                                | 71.9 ms: 1.18x faster                                                           |
| async_tree_memoization     | 578 ms                                                 | 492 ms: 1.17x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 620 ms: 1.17x faster                                                            |
| pathlib                    | 19.3 ms                                                | 16.5 ms: 1.17x faster                                                           |
| async_tree_io_tg           | 1.18 sec                                               | 1.02 sec: 1.16x faster                                                          |
| fannkuch                   | 417 ms                                                 | 361 ms: 1.16x faster                                                            |
| logging_format             | 7.23 us                                                | 6.30 us: 1.15x faster                                                           |
| logging_simple             | 6.46 us                                                | 5.63 us: 1.15x faster                                                           |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.44 ms: 1.14x faster                                                           |
| raytrace                   | 312 ms                                                 | 276 ms: 1.13x faster                                                            |
| chaos                      | 67.0 ms                                                | 59.8 ms: 1.12x faster                                                           |
| pyflate                    | 482 ms                                                 | 437 ms: 1.10x faster                                                            |
| spectral_norm              | 115 ms                                                 | 104 ms: 1.10x faster                                                            |
| pickle_pure_python         | 324 us                                                 | 295 us: 1.10x faster                                                            |
| pprint_safe_repr           | 776 ms                                                 | 711 ms: 1.09x faster                                                            |
| regex_compile              | 148 ms                                                 | 137 ms: 1.09x faster                                                            |
| pprint_pformat             | 1.57 sec                                               | 1.45 sec: 1.08x faster                                                          |
| xml_etree_generate         | 89.2 ms                                                | 82.5 ms: 1.08x faster                                                           |
| richards                   | 45.8 ms                                                | 42.9 ms: 1.07x faster                                                           |
| tornado_http               | 103 ms                                                 | 96.2 ms: 1.07x faster                                                           |
| xml_etree_process          | 61.7 ms                                                | 58.2 ms: 1.06x faster                                                           |
| richards_super             | 51.5 ms                                                | 48.8 ms: 1.06x faster                                                           |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                            |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.05x faster                                                            |
| xml_etree_parse            | 159 ms                                                 | 152 ms: 1.05x faster                                                            |
| unpickle                   | 15.9 us                                                | 15.1 us: 1.05x faster                                                           |
| unpickle_pure_python       | 230 us                                                 | 221 us: 1.04x faster                                                            |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                                           |
| generators                 | 31.2 ms                                                | 30.2 ms: 1.03x faster                                                           |
| deltablue                  | 3.72 ms                                                | 3.61 ms: 1.03x faster                                                           |
| sqlglot_transpile          | 1.68 ms                                                | 1.64 ms: 1.02x faster                                                           |
| mdp                        | 2.63 sec                                               | 2.58 sec: 1.02x faster                                                          |
| unpickle_list              | 5.29 us                                                | 5.25 us: 1.01x faster                                                           |
| regex_effbot               | 3.61 ms                                                | 3.59 ms: 1.01x faster                                                           |
| pickle_dict                | 35.5 us                                                | 35.4 us: 1.00x faster                                                           |
| dulwich_log                | 68.5 ms                                                | 68.7 ms: 1.00x slower                                                           |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                            |
| sympy_sum                  | 169 ms                                                 | 170 ms: 1.01x slower                                                            |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                           |
| sqlite_synth               | 2.83 us                                                | 2.86 us: 1.01x slower                                                           |
| async_generators           | 463 ms                                                 | 469 ms: 1.01x slower                                                            |
| json_loads                 | 28.5 us                                                | 28.9 us: 1.01x slower                                                           |
| coroutines                 | 23.2 ms                                                | 23.5 ms: 1.02x slower                                                           |
| pycparser                  | 1.18 sec                                               | 1.20 sec: 1.02x slower                                                          |
| pickle_list                | 5.08 us                                                | 5.19 us: 1.02x slower                                                           |
| logging_silent             | 104 ns                                                 | 107 ns: 1.02x slower                                                            |
| 2to3                       | 274 ms                                                 | 281 ms: 1.02x slower                                                            |
| dask                       | 372 ms                                                 | 380 ms: 1.02x slower                                                            |
| regex_v8                   | 23.1 ms                                                | 23.7 ms: 1.02x slower                                                           |
| asyncio_websockets         | 551 ms                                                 | 565 ms: 1.03x slower                                                            |
| gc_traversal               | 3.79 ms                                                | 3.90 ms: 1.03x slower                                                           |
| hexiom                     | 6.41 ms                                                | 6.63 ms: 1.03x slower                                                           |
| scimark_sor                | 129 ms                                                 | 134 ms: 1.04x slower                                                            |
| bench_thread_pool          | 842 us                                                 | 873 us: 1.04x slower                                                            |
| sqlglot_normalize          | 110 ms                                                 | 114 ms: 1.04x slower                                                            |
| sqlglot_optimize           | 54.8 ms                                                | 56.9 ms: 1.04x slower                                                           |
| json                       | 5.26 ms                                                | 5.46 ms: 1.04x slower                                                           |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.86 sec: 1.04x slower                                                          |
| nqueens                    | 83.3 ms                                                | 86.7 ms: 1.04x slower                                                           |
| sympy_integrate            | 21.4 ms                                                | 22.4 ms: 1.05x slower                                                           |
| pickle                     | 11.6 us                                                | 12.2 us: 1.05x slower                                                           |
| docutils                   | 2.77 sec                                               | 2.92 sec: 1.05x slower                                                          |
| go                         | 139 ms                                                 | 147 ms: 1.05x slower                                                            |
| asyncio_tcp                | 491 ms                                                 | 520 ms: 1.06x slower                                                            |
| scimark_lu                 | 118 ms                                                 | 126 ms: 1.06x slower                                                            |
| regex_dna                  | 212 ms                                                 | 226 ms: 1.06x slower                                                            |
| sympy_expand               | 478 ms                                                 | 509 ms: 1.06x slower                                                            |
| django_template            | 34.6 ms                                                | 37.0 ms: 1.07x slower                                                           |
| typing_runtime_protocols   | 158 us                                                 | 170 us: 1.08x slower                                                            |
| python_startup_no_site     | 6.94 ms                                                | 7.65 ms: 1.10x slower                                                           |
| telco                      | 7.10 ms                                                | 8.09 ms: 1.14x slower                                                           |
| python_startup             | 9.55 ms                                                | 11.2 ms: 1.17x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 1.80 ms: 1.22x slower                                                           |
| coverage                   | 72.7 ms                                                | 95.0 ms: 1.31x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                                    |

Benchmark hidden because not significant (2): bench_mp_pool, sympy_str
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240615-3.14.0a0-3330a62-JIT/bm-20240615-linux-x86_64-Fidget%2dSpinner-optimizer_constant_p-3.14.0a0-3330a62.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 96.63% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x