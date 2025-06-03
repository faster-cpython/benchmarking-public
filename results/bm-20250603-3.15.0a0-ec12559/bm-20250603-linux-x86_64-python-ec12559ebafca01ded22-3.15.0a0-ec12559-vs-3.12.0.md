# Results vs. 3.12.0

- fork: python
- ref: ec12559ebafca01ded22
- machine: linux-x86_64
- commit hash: ec12559
- commit date: 2025-06-03
- overall geometric mean: 1.089x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 255 ms: 1.08x faster                                                  |
| docutils       | 2.77 sec                                               | 2.58 sec: 1.07x faster                                                |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 601 ms: 1.93x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 634 ms: 1.87x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 315 ms: 1.84x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 318 ms: 1.80x faster                                                  |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.78x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 488 ms: 1.49x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 494 ms: 1.47x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 71.5 ms: 1.18x faster                                                 |
| nbody          | 97.0 ms                                                | 98.1 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.16x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.22 ms: 1.12x faster                                                 |
| regex_dna      | 212 ms                                                 | 194 ms: 1.10x faster                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.01 sec: 1.16x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 142 ms: 1.12x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 99.4 ms: 1.07x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 220 us: 1.04x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 85.9 ms: 1.04x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 60.0 ms: 1.03x faster                                                 |
| json_loads           | 28.5 us                                                | 27.9 us: 1.02x faster                                                 |
| pickle_pure_python   | 324 us                                                 | 319 us: 1.01x faster                                                  |
| json_dumps           | 10.4 ms                                                | 10.9 ms: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.95 ms: 1.00x slower                                                 |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.28x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.4 ms: 1.07x faster                                                 |
| mako            | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.23 sec: 2.13x faster                                                |
| async_tree_io              | 1.16 sec                                               | 601 ms: 1.93x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 634 ms: 1.87x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 315 ms: 1.84x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 318 ms: 1.80x faster                                                  |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.78x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 488 ms: 1.49x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 494 ms: 1.47x faster                                                  |
| deepcopy                   | 371 us                                                 | 257 us: 1.45x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 29.3 us: 1.39x faster                                                 |
| comprehensions             | 21.8 us                                                | 16.0 us: 1.36x faster                                                 |
| go                         | 139 ms                                                 | 112 ms: 1.25x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.73 us: 1.23x faster                                                 |
| float                      | 84.7 ms                                                | 71.5 ms: 1.18x faster                                                 |
| regex_compile              | 148 ms                                                 | 127 ms: 1.16x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 2.01 sec: 1.16x faster                                                |
| raytrace                   | 312 ms                                                 | 270 ms: 1.15x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 59.7 ms: 1.15x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.14x faster                                                  |
| pathlib                    | 19.3 ms                                                | 17.2 ms: 1.13x faster                                                 |
| sympy_integrate            | 21.4 ms                                                | 19.0 ms: 1.13x faster                                                 |
| sympy_str                  | 300 ms                                                 | 267 ms: 1.12x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.22 ms: 1.12x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 142 ms: 1.12x faster                                                  |
| pyflate                    | 482 ms                                                 | 432 ms: 1.12x faster                                                  |
| async_generators           | 463 ms                                                 | 416 ms: 1.11x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 67.9 ms: 1.11x faster                                                 |
| chaos                      | 67.0 ms                                                | 61.0 ms: 1.10x faster                                                 |
| regex_dna                  | 212 ms                                                 | 194 ms: 1.10x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 75.5 ms: 1.08x faster                                                 |
| 2to3                       | 274 ms                                                 | 255 ms: 1.08x faster                                                  |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.07x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 99.4 ms: 1.07x faster                                                 |
| docutils                   | 2.77 sec                                               | 2.58 sec: 1.07x faster                                                |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                                  |
| django_template            | 34.6 ms                                                | 32.4 ms: 1.07x faster                                                 |
| logging_format             | 7.23 us                                                | 6.81 us: 1.06x faster                                                 |
| hexiom                     | 6.41 ms                                                | 6.04 ms: 1.06x faster                                                 |
| sympy_expand               | 478 ms                                                 | 452 ms: 1.06x faster                                                  |
| richards                   | 45.8 ms                                                | 43.4 ms: 1.06x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.52 ms: 1.05x faster                                                 |
| spectral_norm              | 115 ms                                                 | 109 ms: 1.05x faster                                                  |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                 |
| logging_simple             | 6.46 us                                                | 6.17 us: 1.05x faster                                                 |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.04x faster                                                |
| unpickle_pure_python       | 230 us                                                 | 220 us: 1.04x faster                                                  |
| richards_super             | 51.5 ms                                                | 49.6 ms: 1.04x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 85.9 ms: 1.04x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 60.0 ms: 1.03x faster                                                 |
| generators                 | 31.2 ms                                                | 30.5 ms: 1.02x faster                                                 |
| nqueens                    | 83.3 ms                                                | 81.6 ms: 1.02x faster                                                 |
| json                       | 5.26 ms                                                | 5.15 ms: 1.02x faster                                                 |
| json_loads                 | 28.5 us                                                | 27.9 us: 1.02x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 319 us: 1.01x faster                                                  |
| scimark_fft                | 382 ms                                                 | 380 ms: 1.01x faster                                                  |
| python_startup_no_site     | 6.94 ms                                                | 6.95 ms: 1.00x slower                                                 |
| nbody                      | 97.0 ms                                                | 98.1 ms: 1.01x slower                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.12 ms: 1.01x slower                                                 |
| sqlite_synth               | 2.83 us                                                | 2.87 us: 1.01x slower                                                 |
| json_dumps                 | 10.4 ms                                                | 10.9 ms: 1.05x slower                                                 |
| pprint_safe_repr           | 776 ms                                                 | 812 ms: 1.05x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.66 sec: 1.06x slower                                                |
| coroutines                 | 23.2 ms                                                | 26.0 ms: 1.12x slower                                                 |
| telco                      | 7.10 ms                                                | 7.96 ms: 1.12x slower                                                 |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.28x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 5.00 ms: 1.32x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 2.57 ms: 1.74x slower                                                 |
| logging_silent             | 104 ns                                                 | 475 ns: 4.55x slower                                                  |
| coverage                   | 72.7 ms                                                | 426 ms: 5.86x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (5): asyncio_websockets, fannkuch, pidigits, regex_v8, scimark_lu
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250603-3.15.0a0-ec12559/bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.089x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.13x