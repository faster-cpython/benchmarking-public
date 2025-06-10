# Results vs. 3.12.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 0f866cb
- commit date: 2025-06-10
- overall geometric mean: 1.098x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 274 ms                                                 | 262 ms: 1.05x faster                                  |
| docutils       | 2.77 sec                                               | 2.66 sec: 1.04x faster                                |
| Geometric mean | (ref)                                                  | 1.04x faster                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 599 ms: 1.93x faster                                  |
| async_tree_io_tg           | 1.18 sec                                               | 623 ms: 1.90x faster                                  |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.83x faster                                  |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                  |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.80x faster                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 492 ms: 1.47x faster                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 499 ms: 1.45x faster                                  |
| Geometric mean             | (ref)                                                  | 1.75x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| float          | 84.7 ms                                                | 65.9 ms: 1.29x faster                                 |
| nbody          | 97.0 ms                                                | 94.6 ms: 1.03x faster                                 |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                  |
| regex_effbot   | 3.61 ms                                                | 3.25 ms: 1.11x faster                                 |
| regex_dna      | 212 ms                                                 | 199 ms: 1.06x faster                                  |
| regex_v8       | 23.1 ms                                                | 22.6 ms: 1.02x faster                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.90 sec: 1.23x faster                                |
| unpickle_pure_python | 230 us                                                 | 201 us: 1.14x faster                                  |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                  |
| xml_etree_generate   | 89.2 ms                                                | 81.0 ms: 1.10x faster                                 |
| xml_etree_process    | 61.7 ms                                                | 56.3 ms: 1.10x faster                                 |
| xml_etree_iterparse  | 107 ms                                                 | 98.2 ms: 1.09x faster                                 |
| json_dumps           | 10.4 ms                                                | 11.2 ms: 1.08x slower                                 |
| Geometric mean       | (ref)                                                  | 1.08x faster                                          |

Benchmark hidden because not significant (2): json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.96 ms: 1.00x slower                                 |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.28x slower                                 |
| Geometric mean         | (ref)                                                  | 1.13x slower                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.7 ms: 1.12x faster                                 |
| django_template | 34.6 ms                                                | 33.1 ms: 1.04x faster                                 |
| Geometric mean  | (ref)                                                  | 1.08x faster                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.25 sec: 2.11x faster                                |
| async_tree_io              | 1.16 sec                                               | 599 ms: 1.93x faster                                  |
| async_tree_io_tg           | 1.18 sec                                               | 623 ms: 1.90x faster                                  |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.83x faster                                  |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                  |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.80x faster                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 492 ms: 1.47x faster                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 499 ms: 1.45x faster                                  |
| deepcopy                   | 371 us                                                 | 258 us: 1.44x faster                                  |
| deepcopy_memo              | 40.7 us                                                | 29.7 us: 1.37x faster                                 |
| richards                   | 45.8 ms                                                | 34.3 ms: 1.34x faster                                 |
| richards_super             | 51.5 ms                                                | 39.6 ms: 1.30x faster                                 |
| float                      | 84.7 ms                                                | 65.9 ms: 1.29x faster                                 |
| comprehensions             | 21.8 us                                                | 17.0 us: 1.28x faster                                 |
| tomli_loads                | 2.33 sec                                               | 1.90 sec: 1.23x faster                                |
| deepcopy_reduce            | 3.35 us                                                | 2.80 us: 1.20x faster                                 |
| deltablue                  | 3.72 ms                                                | 3.13 ms: 1.19x faster                                 |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                  |
| scimark_fft                | 382 ms                                                 | 332 ms: 1.15x faster                                  |
| unpickle_pure_python       | 230 us                                                 | 201 us: 1.14x faster                                  |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                  |
| pyflate                    | 482 ms                                                 | 424 ms: 1.14x faster                                  |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.12x faster                                  |
| pathlib                    | 19.3 ms                                                | 17.2 ms: 1.12x faster                                 |
| go                         | 139 ms                                                 | 124 ms: 1.12x faster                                  |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                  |
| raytrace                   | 312 ms                                                 | 280 ms: 1.12x faster                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 67.3 ms: 1.12x faster                                 |
| mako                       | 11.9 ms                                                | 10.7 ms: 1.12x faster                                 |
| regex_effbot               | 3.61 ms                                                | 3.25 ms: 1.11x faster                                 |
| dulwich_log                | 68.5 ms                                                | 62.1 ms: 1.10x faster                                 |
| xml_etree_generate         | 89.2 ms                                                | 81.0 ms: 1.10x faster                                 |
| sympy_integrate            | 21.4 ms                                                | 19.5 ms: 1.10x faster                                 |
| sympy_str                  | 300 ms                                                 | 273 ms: 1.10x faster                                  |
| xml_etree_process          | 61.7 ms                                                | 56.3 ms: 1.10x faster                                 |
| xml_etree_iterparse        | 107 ms                                                 | 98.2 ms: 1.09x faster                                 |
| async_generators           | 463 ms                                                 | 434 ms: 1.07x faster                                  |
| crypto_pyaes               | 81.9 ms                                                | 76.8 ms: 1.07x faster                                 |
| regex_dna                  | 212 ms                                                 | 199 ms: 1.06x faster                                  |
| logging_format             | 7.23 us                                                | 6.84 us: 1.06x faster                                 |
| chaos                      | 67.0 ms                                                | 63.7 ms: 1.05x faster                                 |
| logging_simple             | 6.46 us                                                | 6.16 us: 1.05x faster                                 |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                  |
| 2to3                       | 274 ms                                                 | 262 ms: 1.05x faster                                  |
| scimark_sor                | 129 ms                                                 | 124 ms: 1.04x faster                                  |
| django_template            | 34.6 ms                                                | 33.1 ms: 1.04x faster                                 |
| docutils                   | 2.77 sec                                               | 2.66 sec: 1.04x faster                                |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.04x faster                                |
| nbody                      | 97.0 ms                                                | 94.6 ms: 1.03x faster                                 |
| regex_v8                   | 23.1 ms                                                | 22.6 ms: 1.02x faster                                 |
| sympy_expand               | 478 ms                                                 | 468 ms: 1.02x faster                                  |
| generators                 | 31.2 ms                                                | 30.6 ms: 1.02x faster                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.96 ms: 1.02x faster                                 |
| sqlite_synth               | 2.83 us                                                | 2.79 us: 1.02x faster                                 |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                  |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                  |
| python_startup_no_site     | 6.94 ms                                                | 6.96 ms: 1.00x slower                                 |
| nqueens                    | 83.3 ms                                                | 83.6 ms: 1.00x slower                                 |
| scimark_lu                 | 118 ms                                                 | 120 ms: 1.01x slower                                  |
| pprint_safe_repr           | 776 ms                                                 | 815 ms: 1.05x slower                                  |
| json_dumps                 | 10.4 ms                                                | 11.2 ms: 1.08x slower                                 |
| pprint_pformat             | 1.57 sec                                               | 1.69 sec: 1.08x slower                                |
| typing_runtime_protocols   | 158 us                                                 | 172 us: 1.09x slower                                  |
| coroutines                 | 23.2 ms                                                | 25.3 ms: 1.09x slower                                 |
| telco                      | 7.10 ms                                                | 7.89 ms: 1.11x slower                                 |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.28x slower                                 |
| gc_traversal               | 3.79 ms                                                | 5.01 ms: 1.32x slower                                 |
| create_gc_cycles           | 1.48 ms                                                | 2.60 ms: 1.76x slower                                 |
| logging_silent             | 104 ns                                                 | 475 ns: 4.55x slower                                  |
| coverage                   | 72.7 ms                                                | 424 ms: 5.84x slower                                  |
| Geometric mean             | (ref)                                                  | 1.07x faster                                          |

Benchmark hidden because not significant (5): hexiom, json_loads, fannkuch, pickle_pure_python, json
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250610-3.15.0a0-0f866cb-JIT/bm-20250610-linux-x86_64-python-main-3.15.0a0-0f866cb.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.098x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.15x