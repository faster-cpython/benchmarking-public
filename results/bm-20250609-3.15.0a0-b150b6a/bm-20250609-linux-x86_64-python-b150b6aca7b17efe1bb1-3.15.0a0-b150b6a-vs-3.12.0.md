# Results vs. 3.12.0

- fork: python
- ref: b150b6aca7b17efe1bb1
- machine: linux-x86_64
- commit hash: b150b6a
- commit date: 2025-06-09
- overall geometric mean: 1.091x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250609-linux-x86_64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 255 ms: 1.08x faster                                                  |
| docutils       | 2.77 sec                                               | 2.58 sec: 1.07x faster                                                |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250609-linux-x86_64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 602 ms: 1.92x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 632 ms: 1.87x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 313 ms: 1.84x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 317 ms: 1.82x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                                  |
| async_tree_none            | 472 ms                                                 | 264 ms: 1.79x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 486 ms: 1.49x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 495 ms: 1.47x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250609-linux-x86_64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 72.8 ms: 1.16x faster                                                 |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                  |
| nbody          | 97.0 ms                                                | 102 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250609-linux-x86_64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.07 ms: 1.17x faster                                                 |
| regex_dna      | 212 ms                                                 | 181 ms: 1.17x faster                                                  |
| regex_compile  | 148 ms                                                 | 127 ms: 1.16x faster                                                  |
| regex_v8       | 23.1 ms                                                | 22.0 ms: 1.05x faster                                                 |
| Geometric mean | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250609-linux-x86_64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.03 sec: 1.15x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 143 ms: 1.12x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 99.4 ms: 1.07x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 220 us: 1.05x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 85.5 ms: 1.04x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 60.0 ms: 1.03x faster                                                 |
| json_loads           | 28.5 us                                                | 28.2 us: 1.01x faster                                                 |
| pickle_pure_python   | 324 us                                                 | 322 us: 1.01x faster                                                  |
| json_dumps           | 10.4 ms                                                | 11.2 ms: 1.07x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250609-linux-x86_64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.90 ms: 1.01x faster                                                 |
| python_startup         | 9.55 ms                                                | 12.1 ms: 1.27x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250609-linux-x86_64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.6 ms: 1.06x faster                                                 |
| mako            | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250609-linux-x86_64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.23 sec: 2.15x faster                                                |
| async_tree_io              | 1.16 sec                                               | 602 ms: 1.92x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 632 ms: 1.87x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 313 ms: 1.84x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 317 ms: 1.82x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                                  |
| async_tree_none            | 472 ms                                                 | 264 ms: 1.79x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 486 ms: 1.49x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 495 ms: 1.47x faster                                                  |
| deepcopy                   | 371 us                                                 | 255 us: 1.45x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 29.1 us: 1.40x faster                                                 |
| comprehensions             | 21.8 us                                                | 16.2 us: 1.35x faster                                                 |
| go                         | 139 ms                                                 | 112 ms: 1.25x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.77 us: 1.21x faster                                                 |
| regex_effbot               | 3.61 ms                                                | 3.07 ms: 1.17x faster                                                 |
| regex_dna                  | 212 ms                                                 | 181 ms: 1.17x faster                                                  |
| regex_compile              | 148 ms                                                 | 127 ms: 1.16x faster                                                  |
| float                      | 84.7 ms                                                | 72.8 ms: 1.16x faster                                                 |
| pathlib                    | 19.3 ms                                                | 16.8 ms: 1.15x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 2.03 sec: 1.15x faster                                                |
| raytrace                   | 312 ms                                                 | 272 ms: 1.15x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 59.9 ms: 1.14x faster                                                 |
| async_generators           | 463 ms                                                 | 406 ms: 1.14x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.14x faster                                                  |
| sympy_str                  | 300 ms                                                 | 266 ms: 1.13x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 19.0 ms: 1.13x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 143 ms: 1.12x faster                                                  |
| pyflate                    | 482 ms                                                 | 433 ms: 1.11x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 68.6 ms: 1.10x faster                                                 |
| chaos                      | 67.0 ms                                                | 61.9 ms: 1.08x faster                                                 |
| 2to3                       | 274 ms                                                 | 255 ms: 1.08x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 76.1 ms: 1.08x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 99.4 ms: 1.07x faster                                                 |
| docutils                   | 2.77 sec                                               | 2.58 sec: 1.07x faster                                                |
| logging_simple             | 6.46 us                                                | 6.05 us: 1.07x faster                                                 |
| pycparser                  | 1.18 sec                                               | 1.11 sec: 1.06x faster                                                |
| django_template            | 34.6 ms                                                | 32.6 ms: 1.06x faster                                                 |
| scimark_sor                | 129 ms                                                 | 122 ms: 1.06x faster                                                  |
| sympy_expand               | 478 ms                                                 | 451 ms: 1.06x faster                                                  |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.51 ms: 1.06x faster                                                 |
| logging_format             | 7.23 us                                                | 6.84 us: 1.06x faster                                                 |
| hexiom                     | 6.41 ms                                                | 6.08 ms: 1.06x faster                                                 |
| spectral_norm              | 115 ms                                                 | 109 ms: 1.05x faster                                                  |
| richards                   | 45.8 ms                                                | 43.6 ms: 1.05x faster                                                 |
| regex_v8                   | 23.1 ms                                                | 22.0 ms: 1.05x faster                                                 |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 220 us: 1.05x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 85.5 ms: 1.04x faster                                                 |
| generators                 | 31.2 ms                                                | 29.9 ms: 1.04x faster                                                 |
| richards_super             | 51.5 ms                                                | 49.8 ms: 1.03x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 60.0 ms: 1.03x faster                                                 |
| nqueens                    | 83.3 ms                                                | 81.1 ms: 1.03x faster                                                 |
| scimark_fft                | 382 ms                                                 | 373 ms: 1.03x faster                                                  |
| json_loads                 | 28.5 us                                                | 28.2 us: 1.01x faster                                                 |
| fannkuch                   | 417 ms                                                 | 413 ms: 1.01x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 322 us: 1.01x faster                                                  |
| python_startup_no_site     | 6.94 ms                                                | 6.90 ms: 1.01x faster                                                 |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                  |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                  |
| scimark_lu                 | 118 ms                                                 | 119 ms: 1.01x slower                                                  |
| pprint_safe_repr           | 776 ms                                                 | 797 ms: 1.03x slower                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.64 sec: 1.04x slower                                                |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                                  |
| nbody                      | 97.0 ms                                                | 102 ms: 1.06x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 11.2 ms: 1.07x slower                                                 |
| coroutines                 | 23.2 ms                                                | 25.8 ms: 1.11x slower                                                 |
| telco                      | 7.10 ms                                                | 7.95 ms: 1.12x slower                                                 |
| python_startup             | 9.55 ms                                                | 12.1 ms: 1.27x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 5.00 ms: 1.32x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 2.59 ms: 1.75x slower                                                 |
| logging_silent             | 104 ns                                                 | 475 ns: 4.54x slower                                                  |
| coverage                   | 72.7 ms                                                | 426 ms: 5.86x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (3): json, scimark_sparse_mat_mult, sqlite_synth
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250609-3.15.0a0-b150b6a/bm-20250609-linux-x86_64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.091x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.13x