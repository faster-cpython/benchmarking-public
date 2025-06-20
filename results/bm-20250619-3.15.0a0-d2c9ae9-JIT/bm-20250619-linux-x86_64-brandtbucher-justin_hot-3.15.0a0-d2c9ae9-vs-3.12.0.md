# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_hot
- machine: linux-x86_64
- commit hash: d2c9ae9
- commit date: 2025-06-19
- overall geometric mean: 1.119x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 260 ms: 1.05x faster                                              |
| docutils       | 2.77 sec                                               | 2.65 sec: 1.04x faster                                            |
| Geometric mean | (ref)                                                  | 1.05x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 599 ms: 1.93x faster                                              |
| async_tree_io_tg           | 1.18 sec                                               | 614 ms: 1.93x faster                                              |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                              |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                              |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.81x faster                                              |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                              |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 490 ms: 1.48x faster                                              |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 498 ms: 1.46x faster                                              |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 84.7 ms                                                | 66.3 ms: 1.28x faster                                             |
| nbody          | 97.0 ms                                                | 95.0 ms: 1.02x faster                                             |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                              |
| Geometric mean | (ref)                                                  | 1.09x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                              |
| regex_effbot   | 3.61 ms                                                | 3.32 ms: 1.09x faster                                             |
| regex_v8       | 23.1 ms                                                | 22.8 ms: 1.02x faster                                             |
| regex_dna      | 212 ms                                                 | 219 ms: 1.03x slower                                              |
| Geometric mean | (ref)                                                  | 1.06x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.92 sec: 1.22x faster                                            |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                              |
| unpickle_pure_python | 230 us                                                 | 205 us: 1.12x faster                                              |
| xml_etree_generate   | 89.2 ms                                                | 80.8 ms: 1.10x faster                                             |
| xml_etree_process    | 61.7 ms                                                | 56.2 ms: 1.10x faster                                             |
| xml_etree_iterparse  | 107 ms                                                 | 98.3 ms: 1.09x faster                                             |
| json_loads           | 28.5 us                                                | 28.8 us: 1.01x slower                                             |
| json_dumps           | 10.4 ms                                                | 11.0 ms: 1.06x slower                                             |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                      |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.96 ms: 1.00x slower                                             |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.28x slower                                             |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.8 ms: 1.10x faster                                             |
| django_template | 34.6 ms                                                | 32.7 ms: 1.06x faster                                             |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.25 sec: 2.11x faster                                            |
| async_tree_io              | 1.16 sec                                               | 599 ms: 1.93x faster                                              |
| async_tree_io_tg           | 1.18 sec                                               | 614 ms: 1.93x faster                                              |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                              |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                              |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.81x faster                                              |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                              |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 490 ms: 1.48x faster                                              |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 498 ms: 1.46x faster                                              |
| deepcopy                   | 371 us                                                 | 260 us: 1.43x faster                                              |
| deepcopy_memo              | 40.7 us                                                | 29.8 us: 1.37x faster                                             |
| richards                   | 45.8 ms                                                | 34.2 ms: 1.34x faster                                             |
| richards_super             | 51.5 ms                                                | 39.3 ms: 1.31x faster                                             |
| float                      | 84.7 ms                                                | 66.3 ms: 1.28x faster                                             |
| comprehensions             | 21.8 us                                                | 17.4 us: 1.25x faster                                             |
| deepcopy_reduce            | 3.35 us                                                | 2.72 us: 1.23x faster                                             |
| tomli_loads                | 2.33 sec                                               | 1.92 sec: 1.22x faster                                            |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                              |
| deltablue                  | 3.72 ms                                                | 3.22 ms: 1.15x faster                                             |
| dulwich_log                | 68.5 ms                                                | 59.6 ms: 1.15x faster                                             |
| pathlib                    | 19.3 ms                                                | 16.9 ms: 1.14x faster                                             |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                              |
| scimark_fft                | 382 ms                                                 | 336 ms: 1.14x faster                                              |
| go                         | 139 ms                                                 | 123 ms: 1.13x faster                                              |
| unpickle_pure_python       | 230 us                                                 | 205 us: 1.12x faster                                              |
| raytrace                   | 312 ms                                                 | 278 ms: 1.12x faster                                              |
| scimark_monte_carlo        | 75.1 ms                                                | 67.0 ms: 1.12x faster                                             |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                              |
| pyflate                    | 482 ms                                                 | 432 ms: 1.12x faster                                              |
| xml_etree_generate         | 89.2 ms                                                | 80.8 ms: 1.10x faster                                             |
| mako                       | 11.9 ms                                                | 10.8 ms: 1.10x faster                                             |
| xml_etree_process          | 61.7 ms                                                | 56.2 ms: 1.10x faster                                             |
| sympy_str                  | 300 ms                                                 | 273 ms: 1.10x faster                                              |
| sympy_integrate            | 21.4 ms                                                | 19.5 ms: 1.10x faster                                             |
| spectral_norm              | 115 ms                                                 | 105 ms: 1.09x faster                                              |
| regex_effbot               | 3.61 ms                                                | 3.32 ms: 1.09x faster                                             |
| xml_etree_iterparse        | 107 ms                                                 | 98.3 ms: 1.09x faster                                             |
| crypto_pyaes               | 81.9 ms                                                | 76.0 ms: 1.08x faster                                             |
| chaos                      | 67.0 ms                                                | 62.4 ms: 1.07x faster                                             |
| async_generators           | 463 ms                                                 | 433 ms: 1.07x faster                                              |
| scimark_sor                | 129 ms                                                 | 121 ms: 1.07x faster                                              |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                              |
| django_template            | 34.6 ms                                                | 32.7 ms: 1.06x faster                                             |
| pycparser                  | 1.18 sec                                               | 1.12 sec: 1.06x faster                                            |
| 2to3                       | 274 ms                                                 | 260 ms: 1.05x faster                                              |
| logging_format             | 7.23 us                                                | 6.89 us: 1.05x faster                                             |
| docutils                   | 2.77 sec                                               | 2.65 sec: 1.04x faster                                            |
| logging_simple             | 6.46 us                                                | 6.21 us: 1.04x faster                                             |
| generators                 | 31.2 ms                                                | 30.5 ms: 1.02x faster                                             |
| nbody                      | 97.0 ms                                                | 95.0 ms: 1.02x faster                                             |
| sympy_expand               | 478 ms                                                 | 469 ms: 1.02x faster                                              |
| regex_v8                   | 23.1 ms                                                | 22.8 ms: 1.02x faster                                             |
| sqlite_synth               | 2.83 us                                                | 2.79 us: 1.01x faster                                             |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                              |
| python_startup_no_site     | 6.94 ms                                                | 6.96 ms: 1.00x slower                                             |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                              |
| nqueens                    | 83.3 ms                                                | 84.0 ms: 1.01x slower                                             |
| json_loads                 | 28.5 us                                                | 28.8 us: 1.01x slower                                             |
| hexiom                     | 6.41 ms                                                | 6.53 ms: 1.02x slower                                             |
| regex_dna                  | 212 ms                                                 | 219 ms: 1.03x slower                                              |
| coroutines                 | 23.2 ms                                                | 24.3 ms: 1.05x slower                                             |
| json_dumps                 | 10.4 ms                                                | 11.0 ms: 1.06x slower                                             |
| pprint_safe_repr           | 776 ms                                                 | 839 ms: 1.08x slower                                              |
| typing_runtime_protocols   | 158 us                                                 | 171 us: 1.08x slower                                              |
| telco                      | 7.10 ms                                                | 7.80 ms: 1.10x slower                                             |
| pprint_pformat             | 1.57 sec                                               | 1.73 sec: 1.10x slower                                            |
| coverage                   | 72.7 ms                                                | 88.1 ms: 1.21x slower                                             |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.28x slower                                             |
| gc_traversal               | 3.79 ms                                                | 4.93 ms: 1.30x slower                                             |
| create_gc_cycles           | 1.48 ms                                                | 2.59 ms: 1.76x slower                                             |
| logging_silent             | 104 ns                                                 | 474 ns: 4.54x slower                                              |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                      |

Benchmark hidden because not significant (5): scimark_sparse_mat_mult, fannkuch, pickle_pure_python, scimark_lu, json
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250619-3.15.0a0-d2c9ae9-JIT/bm-20250619-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.119x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.15x