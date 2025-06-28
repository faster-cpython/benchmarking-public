# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_nops
- machine: linux-x86_64
- commit hash: b40ad57
- commit date: 2025-06-27
- overall geometric mean: 1.136x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 259 ms: 1.06x faster                                            |
| docutils       | 2.77 sec                                               | 2.64 sec: 1.05x faster                                          |
| Geometric mean | (ref)                                                  | 1.05x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 601 ms: 1.92x faster                                            |
| async_tree_io_tg           | 1.18 sec                                               | 639 ms: 1.85x faster                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 312 ms: 1.84x faster                                            |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                            |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                            |
| async_tree_none            | 472 ms                                                 | 263 ms: 1.79x faster                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 490 ms: 1.48x faster                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 496 ms: 1.46x faster                                            |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 84.7 ms                                                | 66.1 ms: 1.28x faster                                           |
| pidigits       | 187 ms                                                 | 188 ms: 1.01x slower                                            |
| Geometric mean | (ref)                                                  | 1.08x faster                                                    |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                            |
| regex_effbot   | 3.61 ms                                                | 3.25 ms: 1.11x faster                                           |
| regex_dna      | 212 ms                                                 | 211 ms: 1.01x faster                                            |
| Geometric mean | (ref)                                                  | 1.07x faster                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.85 sec: 1.26x faster                                          |
| unpickle_pure_python | 230 us                                                 | 201 us: 1.14x faster                                            |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                            |
| xml_etree_generate   | 89.2 ms                                                | 80.5 ms: 1.11x faster                                           |
| xml_etree_process    | 61.7 ms                                                | 56.3 ms: 1.10x faster                                           |
| xml_etree_iterparse  | 107 ms                                                 | 99.0 ms: 1.08x faster                                           |
| json_loads           | 28.5 us                                                | 28.2 us: 1.01x faster                                           |
| json_dumps           | 10.4 ms                                                | 11.0 ms: 1.05x slower                                           |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                    |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.93 ms: 1.00x faster                                           |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.27x slower                                           |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.8 ms: 1.10x faster                                           |
| django_template | 34.6 ms                                                | 32.8 ms: 1.06x faster                                           |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.24 sec: 2.13x faster                                          |
| async_tree_io              | 1.16 sec                                               | 601 ms: 1.92x faster                                            |
| async_tree_io_tg           | 1.18 sec                                               | 639 ms: 1.85x faster                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 312 ms: 1.84x faster                                            |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                            |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                            |
| async_tree_none            | 472 ms                                                 | 263 ms: 1.79x faster                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 490 ms: 1.48x faster                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 496 ms: 1.46x faster                                            |
| deepcopy                   | 371 us                                                 | 256 us: 1.45x faster                                            |
| deepcopy_memo              | 40.7 us                                                | 29.2 us: 1.39x faster                                           |
| richards                   | 45.8 ms                                                | 33.3 ms: 1.38x faster                                           |
| richards_super             | 51.5 ms                                                | 38.5 ms: 1.34x faster                                           |
| comprehensions             | 21.8 us                                                | 17.0 us: 1.28x faster                                           |
| float                      | 84.7 ms                                                | 66.1 ms: 1.28x faster                                           |
| tomli_loads                | 2.33 sec                                               | 1.85 sec: 1.26x faster                                          |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                           |
| spectral_norm              | 115 ms                                                 | 93.6 ms: 1.23x faster                                           |
| deltablue                  | 3.72 ms                                                | 3.12 ms: 1.19x faster                                           |
| go                         | 139 ms                                                 | 118 ms: 1.18x faster                                            |
| scimark_fft                | 382 ms                                                 | 324 ms: 1.18x faster                                            |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                            |
| pyflate                    | 482 ms                                                 | 416 ms: 1.16x faster                                            |
| dulwich_log                | 68.5 ms                                                | 59.3 ms: 1.16x faster                                           |
| logging_format             | 7.23 us                                                | 6.28 us: 1.15x faster                                           |
| raytrace                   | 312 ms                                                 | 273 ms: 1.14x faster                                            |
| logging_simple             | 6.46 us                                                | 5.65 us: 1.14x faster                                           |
| unpickle_pure_python       | 230 us                                                 | 201 us: 1.14x faster                                            |
| scimark_monte_carlo        | 75.1 ms                                                | 65.8 ms: 1.14x faster                                           |
| pathlib                    | 19.3 ms                                                | 17.0 ms: 1.14x faster                                           |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                            |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.13x faster                                            |
| regex_effbot               | 3.61 ms                                                | 3.25 ms: 1.11x faster                                           |
| xml_etree_generate         | 89.2 ms                                                | 80.5 ms: 1.11x faster                                           |
| sympy_integrate            | 21.4 ms                                                | 19.3 ms: 1.11x faster                                           |
| mako                       | 11.9 ms                                                | 10.8 ms: 1.10x faster                                           |
| sympy_str                  | 300 ms                                                 | 272 ms: 1.10x faster                                            |
| chaos                      | 67.0 ms                                                | 60.9 ms: 1.10x faster                                           |
| xml_etree_process          | 61.7 ms                                                | 56.3 ms: 1.10x faster                                           |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.09x faster                                            |
| crypto_pyaes               | 81.9 ms                                                | 75.7 ms: 1.08x faster                                           |
| xml_etree_iterparse        | 107 ms                                                 | 99.0 ms: 1.08x faster                                           |
| async_generators           | 463 ms                                                 | 429 ms: 1.08x faster                                            |
| pprint_safe_repr           | 776 ms                                                 | 722 ms: 1.07x faster                                            |
| pycparser                  | 1.18 sec                                               | 1.11 sec: 1.06x faster                                          |
| 2to3                       | 274 ms                                                 | 259 ms: 1.06x faster                                            |
| django_template            | 34.6 ms                                                | 32.8 ms: 1.06x faster                                           |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                            |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.05x faster                                          |
| docutils                   | 2.77 sec                                               | 2.64 sec: 1.05x faster                                          |
| logging_silent             | 104 ns                                                 | 102 ns: 1.03x faster                                            |
| sympy_expand               | 478 ms                                                 | 467 ms: 1.02x faster                                            |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.95 ms: 1.02x faster                                           |
| hexiom                     | 6.41 ms                                                | 6.32 ms: 1.01x faster                                           |
| json_loads                 | 28.5 us                                                | 28.2 us: 1.01x faster                                           |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                           |
| fannkuch                   | 417 ms                                                 | 414 ms: 1.01x faster                                            |
| regex_dna                  | 212 ms                                                 | 211 ms: 1.01x faster                                            |
| python_startup_no_site     | 6.94 ms                                                | 6.93 ms: 1.00x faster                                           |
| pidigits                   | 187 ms                                                 | 188 ms: 1.01x slower                                            |
| nqueens                    | 83.3 ms                                                | 84.0 ms: 1.01x slower                                           |
| scimark_lu                 | 118 ms                                                 | 120 ms: 1.01x slower                                            |
| generators                 | 31.2 ms                                                | 32.0 ms: 1.02x slower                                           |
| json_dumps                 | 10.4 ms                                                | 11.0 ms: 1.05x slower                                           |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                            |
| coroutines                 | 23.2 ms                                                | 24.7 ms: 1.06x slower                                           |
| telco                      | 7.10 ms                                                | 7.77 ms: 1.09x slower                                           |
| coverage                   | 72.7 ms                                                | 87.8 ms: 1.21x slower                                           |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.27x slower                                           |
| gc_traversal               | 3.79 ms                                                | 4.96 ms: 1.31x slower                                           |
| create_gc_cycles           | 1.48 ms                                                | 2.58 ms: 1.74x slower                                           |
| Geometric mean             | (ref)                                                  | 1.13x faster                                                    |

Benchmark hidden because not significant (5): json, nbody, regex_v8, asyncio_websockets, pickle_pure_python
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250627-3.15.0a0-b40ad57-JIT/bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.136x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.15x