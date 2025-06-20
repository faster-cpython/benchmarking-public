# Results vs. 3.12.0

- fork: python
- ref: 0f866cbfefd797b4dae2
- machine: linux-x86_64
- commit hash: 0f866cb
- commit date: 2025-06-10
- overall geometric mean: 1.125x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 260 ms: 1.05x faster                                                  |
| docutils       | 2.77 sec                                               | 2.64 sec: 1.05x faster                                                |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 598 ms: 1.93x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 617 ms: 1.92x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 315 ms: 1.83x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.81x faster                                                  |
| async_tree_none            | 472 ms                                                 | 263 ms: 1.79x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 490 ms: 1.48x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 499 ms: 1.45x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 65.1 ms: 1.30x faster                                                 |
| nbody          | 97.0 ms                                                | 94.5 ms: 1.03x faster                                                 |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.31 ms: 1.09x faster                                                 |
| regex_dna      | 212 ms                                                 | 200 ms: 1.06x faster                                                  |
| regex_v8       | 23.1 ms                                                | 22.4 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.90 sec: 1.23x faster                                                |
| unpickle_pure_python | 230 us                                                 | 201 us: 1.15x faster                                                  |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 80.0 ms: 1.11x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 56.0 ms: 1.10x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 98.5 ms: 1.08x faster                                                 |
| json_dumps           | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (2): pickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.96 ms: 1.00x slower                                                 |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.28x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.6 ms: 1.12x faster                                                 |
| django_template | 34.6 ms                                                | 32.5 ms: 1.06x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.24 sec: 2.12x faster                                                |
| async_tree_io              | 1.16 sec                                               | 598 ms: 1.93x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 617 ms: 1.92x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 315 ms: 1.83x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.81x faster                                                  |
| async_tree_none            | 472 ms                                                 | 263 ms: 1.79x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 490 ms: 1.48x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 499 ms: 1.45x faster                                                  |
| deepcopy                   | 371 us                                                 | 258 us: 1.44x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 29.5 us: 1.38x faster                                                 |
| richards                   | 45.8 ms                                                | 33.9 ms: 1.35x faster                                                 |
| float                      | 84.7 ms                                                | 65.1 ms: 1.30x faster                                                 |
| richards_super             | 51.5 ms                                                | 39.9 ms: 1.29x faster                                                 |
| comprehensions             | 21.8 us                                                | 17.1 us: 1.27x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 1.90 sec: 1.23x faster                                                |
| deltablue                  | 3.72 ms                                                | 3.11 ms: 1.20x faster                                                 |
| pyflate                    | 482 ms                                                 | 412 ms: 1.17x faster                                                  |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 201 us: 1.15x faster                                                  |
| pathlib                    | 19.3 ms                                                | 16.9 ms: 1.15x faster                                                 |
| go                         | 139 ms                                                 | 122 ms: 1.14x faster                                                  |
| scimark_fft                | 382 ms                                                 | 335 ms: 1.14x faster                                                  |
| raytrace                   | 312 ms                                                 | 275 ms: 1.13x faster                                                  |
| spectral_norm              | 115 ms                                                 | 101 ms: 1.13x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 60.6 ms: 1.13x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.13x faster                                                  |
| mako                       | 11.9 ms                                                | 10.6 ms: 1.12x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 80.0 ms: 1.11x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 67.5 ms: 1.11x faster                                                 |
| sympy_integrate            | 21.4 ms                                                | 19.4 ms: 1.10x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 56.0 ms: 1.10x faster                                                 |
| sympy_str                  | 300 ms                                                 | 273 ms: 1.10x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.31 ms: 1.09x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 98.5 ms: 1.08x faster                                                 |
| logging_format             | 7.23 us                                                | 6.69 us: 1.08x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 75.8 ms: 1.08x faster                                                 |
| chaos                      | 67.0 ms                                                | 62.2 ms: 1.08x faster                                                 |
| django_template            | 34.6 ms                                                | 32.5 ms: 1.06x faster                                                 |
| scimark_sor                | 129 ms                                                 | 122 ms: 1.06x faster                                                  |
| logging_simple             | 6.46 us                                                | 6.08 us: 1.06x faster                                                 |
| regex_dna                  | 212 ms                                                 | 200 ms: 1.06x faster                                                  |
| 2to3                       | 274 ms                                                 | 260 ms: 1.05x faster                                                  |
| pycparser                  | 1.18 sec                                               | 1.12 sec: 1.05x faster                                                |
| async_generators           | 463 ms                                                 | 441 ms: 1.05x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.64 sec: 1.05x faster                                                |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                  |
| regex_v8                   | 23.1 ms                                                | 22.4 ms: 1.03x faster                                                 |
| nbody                      | 97.0 ms                                                | 94.5 ms: 1.03x faster                                                 |
| sympy_expand               | 478 ms                                                 | 468 ms: 1.02x faster                                                  |
| fannkuch                   | 417 ms                                                 | 411 ms: 1.01x faster                                                  |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.00 ms: 1.01x faster                                                 |
| generators                 | 31.2 ms                                                | 31.0 ms: 1.01x faster                                                 |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                  |
| python_startup_no_site     | 6.94 ms                                                | 6.96 ms: 1.00x slower                                                 |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                  |
| nqueens                    | 83.3 ms                                                | 83.9 ms: 1.01x slower                                                 |
| hexiom                     | 6.41 ms                                                | 6.52 ms: 1.02x slower                                                 |
| pprint_safe_repr           | 776 ms                                                 | 825 ms: 1.06x slower                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.68 sec: 1.07x slower                                                |
| json_dumps                 | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 171 us: 1.08x slower                                                  |
| coroutines                 | 23.2 ms                                                | 25.1 ms: 1.08x slower                                                 |
| telco                      | 7.10 ms                                                | 7.92 ms: 1.12x slower                                                 |
| coverage                   | 72.7 ms                                                | 87.7 ms: 1.21x slower                                                 |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.28x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 4.92 ms: 1.30x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 2.59 ms: 1.75x slower                                                 |
| logging_silent             | 104 ns                                                 | 470 ns: 4.50x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                          |

Benchmark hidden because not significant (4): pickle_pure_python, scimark_lu, json, json_loads
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250610-3.15.0a0-0f866cb-JIT/bm-20250610-linux-x86_64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.125x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.15x