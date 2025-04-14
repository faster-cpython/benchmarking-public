# Results vs. 3.12.0

- fork: brandtbucher
- ref: keep_stack_pointer
- machine: linux-x86_64
- commit hash: b3d84fd
- commit date: 2025-03-26
- overall geometric mean: 1.110x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 258 ms: 1.06x faster                                                       |
| docutils       | 2.77 sec                                               | 2.63 sec: 1.05x faster                                                     |
| Geometric mean | (ref)                                                  | 1.06x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 615 ms: 1.92x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 612 ms: 1.89x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 310 ms: 1.86x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 309 ms: 1.86x faster                                                       |
| async_tree_none            | 472 ms                                                 | 256 ms: 1.84x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 247 ms: 1.82x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 469 ms: 1.55x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 485 ms: 1.50x faster                                                       |
| Geometric mean             | (ref)                                                  | 1.77x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.9 ms: 1.21x faster                                                      |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                       |
| nbody          | 97.0 ms                                                | 97.6 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                  | 1.07x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                       |
| regex_effbot   | 3.61 ms                                                | 3.31 ms: 1.09x faster                                                      |
| regex_v8       | 23.1 ms                                                | 23.8 ms: 1.03x slower                                                      |
| regex_dna      | 212 ms                                                 | 225 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                 | 99.4 ms: 1.07x faster                                                      |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                       |
| xml_etree_generate   | 89.2 ms                                                | 84.9 ms: 1.05x faster                                                      |
| xml_etree_process    | 61.7 ms                                                | 59.3 ms: 1.04x faster                                                      |
| pickle_pure_python   | 324 us                                                 | 314 us: 1.03x faster                                                       |
| json_loads           | 28.5 us                                                | 29.9 us: 1.05x slower                                                      |
| json_dumps           | 10.4 ms                                                | 11.6 ms: 1.11x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.28 ms: 1.19x slower                                                      |
| python_startup         | 9.55 ms                                                | 13.3 ms: 1.39x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.29x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.3 ms: 1.10x faster                                                      |
| mako            | 11.9 ms                                                | 11.2 ms: 1.06x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 615 ms: 1.92x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 612 ms: 1.89x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 310 ms: 1.86x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 309 ms: 1.86x faster                                                       |
| async_tree_none            | 472 ms                                                 | 256 ms: 1.84x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 247 ms: 1.82x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 469 ms: 1.55x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 485 ms: 1.50x faster                                                       |
| deepcopy                   | 371 us                                                 | 257 us: 1.45x faster                                                       |
| deepcopy_memo              | 40.7 us                                                | 29.0 us: 1.41x faster                                                      |
| comprehensions             | 21.8 us                                                | 17.0 us: 1.28x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                                      |
| go                         | 139 ms                                                 | 114 ms: 1.22x faster                                                       |
| float                      | 84.7 ms                                                | 69.9 ms: 1.21x faster                                                      |
| tomli_loads                | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                     |
| deltablue                  | 3.72 ms                                                | 3.15 ms: 1.18x faster                                                      |
| raytrace                   | 312 ms                                                 | 265 ms: 1.18x faster                                                       |
| spectral_norm              | 115 ms                                                 | 97.6 ms: 1.18x faster                                                      |
| logging_simple             | 6.46 us                                                | 5.50 us: 1.17x faster                                                      |
| async_generators           | 463 ms                                                 | 395 ms: 1.17x faster                                                       |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                       |
| logging_format             | 7.23 us                                                | 6.19 us: 1.17x faster                                                      |
| pathlib                    | 19.3 ms                                                | 16.7 ms: 1.16x faster                                                      |
| chaos                      | 67.0 ms                                                | 58.2 ms: 1.15x faster                                                      |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                       |
| scimark_monte_carlo        | 75.1 ms                                                | 66.9 ms: 1.12x faster                                                      |
| crypto_pyaes               | 81.9 ms                                                | 73.1 ms: 1.12x faster                                                      |
| sqlalchemy_declarative     | 147 ms                                                 | 132 ms: 1.11x faster                                                       |
| django_template            | 34.6 ms                                                | 31.3 ms: 1.10x faster                                                      |
| sympy_str                  | 300 ms                                                 | 272 ms: 1.10x faster                                                       |
| dulwich_log                | 68.5 ms                                                | 62.3 ms: 1.10x faster                                                      |
| generators                 | 31.2 ms                                                | 28.4 ms: 1.10x faster                                                      |
| scimark_fft                | 382 ms                                                 | 349 ms: 1.09x faster                                                       |
| regex_effbot               | 3.61 ms                                                | 3.31 ms: 1.09x faster                                                      |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.09x faster                                                       |
| sympy_sum                  | 169 ms                                                 | 155 ms: 1.09x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                 | 99.4 ms: 1.07x faster                                                      |
| pprint_safe_repr           | 776 ms                                                 | 723 ms: 1.07x faster                                                       |
| sympy_integrate            | 21.4 ms                                                | 20.0 ms: 1.07x faster                                                      |
| logging_silent             | 104 ns                                                 | 97.5 ns: 1.07x faster                                                      |
| 2to3                       | 274 ms                                                 | 258 ms: 1.06x faster                                                       |
| mako                       | 11.9 ms                                                | 11.2 ms: 1.06x faster                                                      |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                       |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                                     |
| pyflate                    | 482 ms                                                 | 456 ms: 1.06x faster                                                       |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.78 ms: 1.06x faster                                                      |
| mdp                        | 2.63 sec                                               | 2.50 sec: 1.05x faster                                                     |
| docutils                   | 2.77 sec                                               | 2.63 sec: 1.05x faster                                                     |
| xml_etree_generate         | 89.2 ms                                                | 84.9 ms: 1.05x faster                                                      |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                       |
| richards                   | 45.8 ms                                                | 43.9 ms: 1.04x faster                                                      |
| sympy_expand               | 478 ms                                                 | 459 ms: 1.04x faster                                                       |
| xml_etree_process          | 61.7 ms                                                | 59.3 ms: 1.04x faster                                                      |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.04x faster                                                     |
| pickle_pure_python         | 324 us                                                 | 314 us: 1.03x faster                                                       |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.02x faster                                                       |
| hexiom                     | 6.41 ms                                                | 6.27 ms: 1.02x faster                                                      |
| richards_super             | 51.5 ms                                                | 50.6 ms: 1.02x faster                                                      |
| sqlalchemy_imperative      | 18.7 ms                                                | 18.4 ms: 1.02x faster                                                      |
| nqueens                    | 83.3 ms                                                | 82.3 ms: 1.01x faster                                                      |
| sqlite_synth               | 2.83 us                                                | 2.81 us: 1.01x faster                                                      |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                       |
| coroutines                 | 23.2 ms                                                | 23.3 ms: 1.01x slower                                                      |
| nbody                      | 97.0 ms                                                | 97.6 ms: 1.01x slower                                                      |
| typing_runtime_protocols   | 158 us                                                 | 160 us: 1.01x slower                                                       |
| fannkuch                   | 417 ms                                                 | 425 ms: 1.02x slower                                                       |
| regex_v8                   | 23.1 ms                                                | 23.8 ms: 1.03x slower                                                      |
| json_loads                 | 28.5 us                                                | 29.9 us: 1.05x slower                                                      |
| bench_thread_pool          | 842 us                                                 | 889 us: 1.06x slower                                                       |
| regex_dna                  | 212 ms                                                 | 225 ms: 1.06x slower                                                       |
| telco                      | 7.10 ms                                                | 7.81 ms: 1.10x slower                                                      |
| json_dumps                 | 10.4 ms                                                | 11.6 ms: 1.11x slower                                                      |
| python_startup_no_site     | 6.94 ms                                                | 8.28 ms: 1.19x slower                                                      |
| gc_traversal               | 3.79 ms                                                | 4.79 ms: 1.26x slower                                                      |
| coverage                   | 72.7 ms                                                | 92.6 ms: 1.27x slower                                                      |
| python_startup             | 9.55 ms                                                | 13.3 ms: 1.39x slower                                                      |
| create_gc_cycles           | 1.48 ms                                                | 2.46 ms: 1.67x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 85.3 ms: 3.55x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                               |

Benchmark hidden because not significant (2): asyncio_websockets, json
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250326-3.14.0a6+-b3d84fd/bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.110x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.10x