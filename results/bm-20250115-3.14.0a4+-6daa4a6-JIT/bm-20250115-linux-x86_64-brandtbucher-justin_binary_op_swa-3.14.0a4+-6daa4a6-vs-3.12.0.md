# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_binary_op_swa
- machine: linux-x86_64
- commit hash: 6daa4a6
- commit date: 2025-01-15
- overall geometric mean: 1.102x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4+-6daa4a6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 260 ms: 1.06x faster                                                         |
| docutils       | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4+-6daa4a6 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 595 ms: 1.99x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 616 ms: 1.88x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 310 ms: 1.86x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.79x faster                                                         |
| async_tree_none            | 472 ms                                                 | 266 ms: 1.77x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 332 ms: 1.74x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 474 ms: 1.53x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 500 ms: 1.45x faster                                                         |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4+-6daa4a6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.1 ms: 1.23x faster                                                        |
| nbody          | 97.0 ms                                                | 85.2 ms: 1.14x faster                                                        |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4+-6daa4a6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.12 ms: 1.16x faster                                                        |
| regex_compile  | 148 ms                                                 | 130 ms: 1.15x faster                                                         |
| regex_dna      | 212 ms                                                 | 203 ms: 1.04x faster                                                         |
| regex_v8       | 23.1 ms                                                | 24.2 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4+-6daa4a6 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.83 sec: 1.27x faster                                                       |
| xml_etree_parse      | 159 ms                                                 | 136 ms: 1.18x faster                                                         |
| unpickle_pure_python | 230 us                                                 | 196 us: 1.17x faster                                                         |
| xml_etree_generate   | 89.2 ms                                                | 77.9 ms: 1.14x faster                                                        |
| xml_etree_process    | 61.7 ms                                                | 54.8 ms: 1.13x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                 | 94.9 ms: 1.13x faster                                                        |
| pickle_pure_python   | 324 us                                                 | 316 us: 1.02x faster                                                         |
| json_loads           | 28.5 us                                                | 29.8 us: 1.04x slower                                                        |
| json_dumps           | 10.4 ms                                                | 11.6 ms: 1.12x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4+-6daa4a6 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.11 ms: 1.02x slower                                                        |
| python_startup         | 9.55 ms                                                | 12.9 ms: 1.36x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.18x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4+-6daa4a6 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.94 ms: 1.20x faster                                                        |
| django_template | 34.6 ms                                                | 34.1 ms: 1.01x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4+-6daa4a6 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 595 ms: 1.99x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 616 ms: 1.88x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 310 ms: 1.86x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.79x faster                                                         |
| async_tree_none            | 472 ms                                                 | 266 ms: 1.77x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 332 ms: 1.74x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 474 ms: 1.53x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 500 ms: 1.45x faster                                                         |
| deepcopy                   | 371 us                                                 | 272 us: 1.37x faster                                                         |
| deepcopy_memo              | 40.7 us                                                | 30.3 us: 1.35x faster                                                        |
| tomli_loads                | 2.33 sec                                               | 1.83 sec: 1.27x faster                                                       |
| comprehensions             | 21.8 us                                                | 17.2 us: 1.26x faster                                                        |
| float                      | 84.7 ms                                                | 69.1 ms: 1.23x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.78 us: 1.21x faster                                                        |
| scimark_fft                | 382 ms                                                 | 319 ms: 1.20x faster                                                         |
| mako                       | 11.9 ms                                                | 9.94 ms: 1.20x faster                                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 63.0 ms: 1.19x faster                                                        |
| pathlib                    | 19.3 ms                                                | 16.3 ms: 1.19x faster                                                        |
| xml_etree_parse            | 159 ms                                                 | 136 ms: 1.18x faster                                                         |
| unpickle_pure_python       | 230 us                                                 | 196 us: 1.17x faster                                                         |
| regex_effbot               | 3.61 ms                                                | 3.12 ms: 1.16x faster                                                        |
| deltablue                  | 3.72 ms                                                | 3.24 ms: 1.15x faster                                                        |
| regex_compile              | 148 ms                                                 | 130 ms: 1.15x faster                                                         |
| xml_etree_generate         | 89.2 ms                                                | 77.9 ms: 1.14x faster                                                        |
| crypto_pyaes               | 81.9 ms                                                | 71.6 ms: 1.14x faster                                                        |
| logging_format             | 7.23 us                                                | 6.33 us: 1.14x faster                                                        |
| async_generators           | 463 ms                                                 | 407 ms: 1.14x faster                                                         |
| nbody                      | 97.0 ms                                                | 85.2 ms: 1.14x faster                                                        |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.47 ms: 1.13x faster                                                        |
| xml_etree_process          | 61.7 ms                                                | 54.8 ms: 1.13x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                 | 94.9 ms: 1.13x faster                                                        |
| scimark_sor                | 129 ms                                                 | 115 ms: 1.12x faster                                                         |
| logging_simple             | 6.46 us                                                | 5.76 us: 1.12x faster                                                        |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                                         |
| pyflate                    | 482 ms                                                 | 435 ms: 1.11x faster                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.2 ms: 1.09x faster                                                        |
| spectral_norm              | 115 ms                                                 | 106 ms: 1.08x faster                                                         |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.07x faster                                                        |
| raytrace                   | 312 ms                                                 | 291 ms: 1.07x faster                                                         |
| sympy_sum                  | 169 ms                                                 | 158 ms: 1.07x faster                                                         |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.06x faster                                                        |
| chaos                      | 67.0 ms                                                | 63.1 ms: 1.06x faster                                                        |
| sympy_str                  | 300 ms                                                 | 283 ms: 1.06x faster                                                         |
| 2to3                       | 274 ms                                                 | 260 ms: 1.06x faster                                                         |
| fannkuch                   | 417 ms                                                 | 396 ms: 1.05x faster                                                         |
| richards                   | 45.8 ms                                                | 43.7 ms: 1.05x faster                                                        |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.05x faster                                                       |
| regex_dna                  | 212 ms                                                 | 203 ms: 1.04x faster                                                         |
| sqlite_synth               | 2.83 us                                                | 2.74 us: 1.03x faster                                                        |
| pprint_safe_repr           | 776 ms                                                 | 752 ms: 1.03x faster                                                         |
| mdp                        | 2.63 sec                                               | 2.55 sec: 1.03x faster                                                       |
| richards_super             | 51.5 ms                                                | 49.9 ms: 1.03x faster                                                        |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                         |
| sympy_integrate            | 21.4 ms                                                | 20.8 ms: 1.03x faster                                                        |
| docutils                   | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                       |
| go                         | 139 ms                                                 | 136 ms: 1.03x faster                                                         |
| pickle_pure_python         | 324 us                                                 | 316 us: 1.02x faster                                                         |
| pprint_pformat             | 1.57 sec                                               | 1.53 sec: 1.02x faster                                                       |
| django_template            | 34.6 ms                                                | 34.1 ms: 1.01x faster                                                        |
| sqlglot_normalize          | 110 ms                                                 | 109 ms: 1.01x faster                                                         |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                         |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                         |
| dulwich_log                | 68.5 ms                                                | 68.3 ms: 1.00x faster                                                        |
| python_startup_no_site     | 6.94 ms                                                | 7.11 ms: 1.02x slower                                                        |
| logging_silent             | 104 ns                                                 | 107 ns: 1.03x slower                                                         |
| regex_v8                   | 23.1 ms                                                | 24.2 ms: 1.04x slower                                                        |
| json_loads                 | 28.5 us                                                | 29.8 us: 1.04x slower                                                        |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                                         |
| bench_thread_pool          | 842 us                                                 | 897 us: 1.07x slower                                                         |
| telco                      | 7.10 ms                                                | 7.70 ms: 1.08x slower                                                        |
| nqueens                    | 83.3 ms                                                | 91.6 ms: 1.10x slower                                                        |
| hexiom                     | 6.41 ms                                                | 7.17 ms: 1.12x slower                                                        |
| json_dumps                 | 10.4 ms                                                | 11.6 ms: 1.12x slower                                                        |
| generators                 | 31.2 ms                                                | 37.8 ms: 1.21x slower                                                        |
| coverage                   | 72.7 ms                                                | 90.0 ms: 1.24x slower                                                        |
| gc_traversal               | 3.79 ms                                                | 5.04 ms: 1.33x slower                                                        |
| python_startup             | 9.55 ms                                                | 12.9 ms: 1.36x slower                                                        |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.67x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 81.6 ms: 3.40x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                 |

Benchmark hidden because not significant (5): sympy_expand, asyncio_websockets, sqlglot_optimize, coroutines, json
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250115-3.14.0a4+-6daa4a6-JIT/bm-20250115-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a4+-6daa4a6.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.102x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.10x