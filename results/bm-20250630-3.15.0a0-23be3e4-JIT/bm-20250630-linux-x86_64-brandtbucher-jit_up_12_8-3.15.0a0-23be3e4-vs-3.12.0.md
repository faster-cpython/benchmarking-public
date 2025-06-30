# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_up_12_8
- machine: linux-x86_64
- commit hash: 23be3e4
- commit date: 2025-06-30
- overall geometric mean: 1.139x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_8-3.15.0a0-23be3e4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 261 ms: 1.05x faster                                               |
| docutils       | 2.77 sec                                               | 2.66 sec: 1.04x faster                                             |
| Geometric mean | (ref)                                                  | 1.05x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_8-3.15.0a0-23be3e4 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 606 ms: 1.91x faster                                               |
| async_tree_io_tg           | 1.18 sec                                               | 629 ms: 1.88x faster                                               |
| async_tree_memoization     | 578 ms                                                 | 315 ms: 1.84x faster                                               |
| async_tree_memoization_tg  | 575 ms                                                 | 318 ms: 1.80x faster                                               |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                               |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.78x faster                                               |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 495 ms: 1.47x faster                                               |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 501 ms: 1.45x faster                                               |
| Geometric mean             | (ref)                                                  | 1.73x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_8-3.15.0a0-23be3e4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 66.2 ms: 1.28x faster                                              |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                               |
| nbody          | 97.0 ms                                                | 101 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                  | 1.07x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_8-3.15.0a0-23be3e4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                               |
| regex_effbot   | 3.61 ms                                                | 3.45 ms: 1.05x faster                                              |
| regex_dna      | 212 ms                                                 | 208 ms: 1.02x faster                                               |
| regex_v8       | 23.1 ms                                                | 23.0 ms: 1.01x faster                                              |
| Geometric mean | (ref)                                                  | 1.06x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_8-3.15.0a0-23be3e4 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.83 sec: 1.27x faster                                             |
| unpickle_pure_python | 230 us                                                 | 190 us: 1.21x faster                                               |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                               |
| xml_etree_generate   | 89.2 ms                                                | 80.0 ms: 1.11x faster                                              |
| xml_etree_process    | 61.7 ms                                                | 55.7 ms: 1.11x faster                                              |
| xml_etree_iterparse  | 107 ms                                                 | 98.4 ms: 1.09x faster                                              |
| pickle_pure_python   | 324 us                                                 | 322 us: 1.01x faster                                               |
| json_loads           | 28.5 us                                                | 28.7 us: 1.01x slower                                              |
| json_dumps           | 10.4 ms                                                | 11.2 ms: 1.08x slower                                              |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_8-3.15.0a0-23be3e4 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.96 ms: 1.00x slower                                              |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.28x slower                                              |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_8-3.15.0a0-23be3e4 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.4 ms: 1.14x faster                                              |
| django_template | 34.6 ms                                                | 32.6 ms: 1.06x faster                                              |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_8-3.15.0a0-23be3e4 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.23 sec: 2.14x faster                                             |
| async_tree_io              | 1.16 sec                                               | 606 ms: 1.91x faster                                               |
| async_tree_io_tg           | 1.18 sec                                               | 629 ms: 1.88x faster                                               |
| async_tree_memoization     | 578 ms                                                 | 315 ms: 1.84x faster                                               |
| async_tree_memoization_tg  | 575 ms                                                 | 318 ms: 1.80x faster                                               |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                               |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.78x faster                                               |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 495 ms: 1.47x faster                                               |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 501 ms: 1.45x faster                                               |
| deepcopy                   | 371 us                                                 | 261 us: 1.42x faster                                               |
| deepcopy_memo              | 40.7 us                                                | 29.7 us: 1.37x faster                                              |
| richards                   | 45.8 ms                                                | 33.7 ms: 1.36x faster                                              |
| richards_super             | 51.5 ms                                                | 38.0 ms: 1.36x faster                                              |
| comprehensions             | 21.8 us                                                | 16.3 us: 1.33x faster                                              |
| float                      | 84.7 ms                                                | 66.2 ms: 1.28x faster                                              |
| tomli_loads                | 2.33 sec                                               | 1.83 sec: 1.27x faster                                             |
| spectral_norm              | 115 ms                                                 | 91.0 ms: 1.26x faster                                              |
| deepcopy_reduce            | 3.35 us                                                | 2.70 us: 1.24x faster                                              |
| scimark_fft                | 382 ms                                                 | 311 ms: 1.23x faster                                               |
| deltablue                  | 3.72 ms                                                | 3.03 ms: 1.23x faster                                              |
| go                         | 139 ms                                                 | 115 ms: 1.22x faster                                               |
| unpickle_pure_python       | 230 us                                                 | 190 us: 1.21x faster                                               |
| pyflate                    | 482 ms                                                 | 413 ms: 1.17x faster                                               |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                               |
| raytrace                   | 312 ms                                                 | 269 ms: 1.16x faster                                               |
| scimark_monte_carlo        | 75.1 ms                                                | 65.2 ms: 1.15x faster                                              |
| dulwich_log                | 68.5 ms                                                | 59.7 ms: 1.15x faster                                              |
| logging_format             | 7.23 us                                                | 6.32 us: 1.14x faster                                              |
| pathlib                    | 19.3 ms                                                | 16.9 ms: 1.14x faster                                              |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                               |
| mako                       | 11.9 ms                                                | 10.4 ms: 1.14x faster                                              |
| logging_simple             | 6.46 us                                                | 5.70 us: 1.13x faster                                              |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.12x faster                                               |
| xml_etree_generate         | 89.2 ms                                                | 80.0 ms: 1.11x faster                                              |
| pprint_safe_repr           | 776 ms                                                 | 697 ms: 1.11x faster                                               |
| xml_etree_process          | 61.7 ms                                                | 55.7 ms: 1.11x faster                                              |
| sympy_integrate            | 21.4 ms                                                | 19.5 ms: 1.10x faster                                              |
| sympy_str                  | 300 ms                                                 | 273 ms: 1.10x faster                                               |
| chaos                      | 67.0 ms                                                | 61.2 ms: 1.09x faster                                              |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.09x faster                                               |
| xml_etree_iterparse        | 107 ms                                                 | 98.4 ms: 1.09x faster                                              |
| crypto_pyaes               | 81.9 ms                                                | 75.6 ms: 1.08x faster                                              |
| pprint_pformat             | 1.57 sec                                               | 1.45 sec: 1.08x faster                                             |
| django_template            | 34.6 ms                                                | 32.6 ms: 1.06x faster                                              |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                               |
| async_generators           | 463 ms                                                 | 437 ms: 1.06x faster                                               |
| pycparser                  | 1.18 sec                                               | 1.11 sec: 1.06x faster                                             |
| 2to3                       | 274 ms                                                 | 261 ms: 1.05x faster                                               |
| fannkuch                   | 417 ms                                                 | 396 ms: 1.05x faster                                               |
| regex_effbot               | 3.61 ms                                                | 3.45 ms: 1.05x faster                                              |
| docutils                   | 2.77 sec                                               | 2.66 sec: 1.04x faster                                             |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.90 ms: 1.03x faster                                              |
| hexiom                     | 6.41 ms                                                | 6.24 ms: 1.03x faster                                              |
| sympy_expand               | 478 ms                                                 | 468 ms: 1.02x faster                                               |
| regex_dna                  | 212 ms                                                 | 208 ms: 1.02x faster                                               |
| sqlite_synth               | 2.83 us                                                | 2.78 us: 1.02x faster                                              |
| pickle_pure_python         | 324 us                                                 | 322 us: 1.01x faster                                               |
| regex_v8                   | 23.1 ms                                                | 23.0 ms: 1.01x faster                                              |
| python_startup_no_site     | 6.94 ms                                                | 6.96 ms: 1.00x slower                                              |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                               |
| generators                 | 31.2 ms                                                | 31.4 ms: 1.01x slower                                              |
| json_loads                 | 28.5 us                                                | 28.7 us: 1.01x slower                                              |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                               |
| logging_silent             | 104 ns                                                 | 105 ns: 1.01x slower                                               |
| scimark_lu                 | 118 ms                                                 | 121 ms: 1.02x slower                                               |
| nbody                      | 97.0 ms                                                | 101 ms: 1.04x slower                                               |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.07x slower                                               |
| coroutines                 | 23.2 ms                                                | 24.9 ms: 1.07x slower                                              |
| json_dumps                 | 10.4 ms                                                | 11.2 ms: 1.08x slower                                              |
| telco                      | 7.10 ms                                                | 7.68 ms: 1.08x slower                                              |
| coverage                   | 72.7 ms                                                | 87.8 ms: 1.21x slower                                              |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.28x slower                                              |
| gc_traversal               | 3.79 ms                                                | 4.95 ms: 1.31x slower                                              |
| create_gc_cycles           | 1.48 ms                                                | 2.60 ms: 1.76x slower                                              |
| Geometric mean             | (ref)                                                  | 1.14x faster                                                       |

Benchmark hidden because not significant (2): nqueens, json
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250630-3.15.0a0-23be3e4-JIT/bm-20250630-linux-x86_64-brandtbucher-jit_up_12_8-3.15.0a0-23be3e4.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.139x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.15x