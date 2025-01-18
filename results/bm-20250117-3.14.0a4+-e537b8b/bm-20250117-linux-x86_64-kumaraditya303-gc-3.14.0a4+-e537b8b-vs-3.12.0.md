# Results vs. 3.12.0

- fork: kumaraditya303
- ref: gc
- machine: linux-x86_64
- commit hash: e537b8b
- commit date: 2025-01-17
- overall geometric mean: 1.118x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 253 ms: 1.08x faster                                         |
| docutils       | 2.77 sec                                               | 2.59 sec: 1.07x faster                                       |
| Geometric mean | (ref)                                                  | 1.08x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 584 ms: 2.02x faster                                         |
| async_tree_io              | 1.16 sec                                               | 604 ms: 1.91x faster                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 305 ms: 1.89x faster                                         |
| async_tree_none_tg         | 450 ms                                                 | 244 ms: 1.84x faster                                         |
| async_tree_none            | 472 ms                                                 | 259 ms: 1.82x faster                                         |
| async_tree_memoization     | 578 ms                                                 | 324 ms: 1.78x faster                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 458 ms: 1.58x faster                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 482 ms: 1.51x faster                                         |
| Geometric mean             | (ref)                                                  | 1.79x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.3 ms: 1.20x faster                                        |
| nbody          | 97.0 ms                                                | 94.3 ms: 1.03x faster                                        |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                         |
| Geometric mean | (ref)                                                  | 1.08x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 125 ms: 1.18x faster                                         |
| regex_effbot   | 3.61 ms                                                | 3.29 ms: 1.10x faster                                        |
| regex_dna      | 212 ms                                                 | 211 ms: 1.01x faster                                         |
| regex_v8       | 23.1 ms                                                | 26.1 ms: 1.13x slower                                        |
| Geometric mean | (ref)                                                  | 1.04x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.94 sec: 1.20x faster                                       |
| xml_etree_parse      | 159 ms                                                 | 139 ms: 1.15x faster                                         |
| xml_etree_iterparse  | 107 ms                                                 | 97.7 ms: 1.09x faster                                        |
| unpickle_pure_python | 230 us                                                 | 218 us: 1.06x faster                                         |
| xml_etree_generate   | 89.2 ms                                                | 84.5 ms: 1.05x faster                                        |
| xml_etree_process    | 61.7 ms                                                | 59.1 ms: 1.04x faster                                        |
| pickle_pure_python   | 324 us                                                 | 321 us: 1.01x faster                                         |
| json_loads           | 28.5 us                                                | 29.8 us: 1.05x slower                                        |
| json_dumps           | 10.4 ms                                                | 12.0 ms: 1.16x slower                                        |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.05 ms: 1.02x slower                                        |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                        |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.9 ms: 1.09x faster                                        |
| mako            | 11.9 ms                                                | 11.2 ms: 1.06x faster                                        |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 584 ms: 2.02x faster                                         |
| async_tree_io              | 1.16 sec                                               | 604 ms: 1.91x faster                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 305 ms: 1.89x faster                                         |
| async_tree_none_tg         | 450 ms                                                 | 244 ms: 1.84x faster                                         |
| async_tree_none            | 472 ms                                                 | 259 ms: 1.82x faster                                         |
| async_tree_memoization     | 578 ms                                                 | 324 ms: 1.78x faster                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 458 ms: 1.58x faster                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 482 ms: 1.51x faster                                         |
| deepcopy                   | 371 us                                                 | 256 us: 1.45x faster                                         |
| deepcopy_memo              | 40.7 us                                                | 30.4 us: 1.34x faster                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.60 us: 1.29x faster                                        |
| comprehensions             | 21.8 us                                                | 17.0 us: 1.28x faster                                        |
| spectral_norm              | 115 ms                                                 | 93.5 ms: 1.23x faster                                        |
| async_generators           | 463 ms                                                 | 382 ms: 1.21x faster                                         |
| float                      | 84.7 ms                                                | 70.3 ms: 1.20x faster                                        |
| logging_format             | 7.23 us                                                | 6.01 us: 1.20x faster                                        |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                        |
| tomli_loads                | 2.33 sec                                               | 1.94 sec: 1.20x faster                                       |
| go                         | 139 ms                                                 | 117 ms: 1.20x faster                                         |
| logging_simple             | 6.46 us                                                | 5.41 us: 1.19x faster                                        |
| regex_compile              | 148 ms                                                 | 125 ms: 1.18x faster                                         |
| sympy_sum                  | 169 ms                                                 | 146 ms: 1.16x faster                                         |
| deltablue                  | 3.72 ms                                                | 3.22 ms: 1.15x faster                                        |
| raytrace                   | 312 ms                                                 | 271 ms: 1.15x faster                                         |
| chaos                      | 67.0 ms                                                | 58.1 ms: 1.15x faster                                        |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.2 ms: 1.15x faster                                        |
| xml_etree_parse            | 159 ms                                                 | 139 ms: 1.15x faster                                         |
| sqlalchemy_declarative     | 147 ms                                                 | 128 ms: 1.14x faster                                         |
| crypto_pyaes               | 81.9 ms                                                | 71.7 ms: 1.14x faster                                        |
| sympy_str                  | 300 ms                                                 | 263 ms: 1.14x faster                                         |
| generators                 | 31.2 ms                                                | 28.0 ms: 1.12x faster                                        |
| scimark_fft                | 382 ms                                                 | 343 ms: 1.11x faster                                         |
| scimark_monte_carlo        | 75.1 ms                                                | 68.1 ms: 1.10x faster                                        |
| regex_effbot               | 3.61 ms                                                | 3.29 ms: 1.10x faster                                        |
| xml_etree_iterparse        | 107 ms                                                 | 97.7 ms: 1.09x faster                                        |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.63 ms: 1.09x faster                                        |
| sympy_integrate            | 21.4 ms                                                | 19.7 ms: 1.09x faster                                        |
| sqlglot_parse              | 1.36 ms                                                | 1.25 ms: 1.09x faster                                        |
| django_template            | 34.6 ms                                                | 31.9 ms: 1.09x faster                                        |
| 2to3                       | 274 ms                                                 | 253 ms: 1.08x faster                                         |
| sqlglot_transpile          | 1.68 ms                                                | 1.56 ms: 1.08x faster                                        |
| pprint_safe_repr           | 776 ms                                                 | 719 ms: 1.08x faster                                         |
| dulwich_log                | 68.5 ms                                                | 63.8 ms: 1.07x faster                                        |
| sympy_expand               | 478 ms                                                 | 446 ms: 1.07x faster                                         |
| docutils                   | 2.77 sec                                               | 2.59 sec: 1.07x faster                                       |
| mdp                        | 2.63 sec                                               | 2.47 sec: 1.06x faster                                       |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                       |
| scimark_sor                | 129 ms                                                 | 122 ms: 1.06x faster                                         |
| mako                       | 11.9 ms                                                | 11.2 ms: 1.06x faster                                        |
| unpickle_pure_python       | 230 us                                                 | 218 us: 1.06x faster                                         |
| richards                   | 45.8 ms                                                | 43.4 ms: 1.06x faster                                        |
| xml_etree_generate         | 89.2 ms                                                | 84.5 ms: 1.05x faster                                        |
| sqlglot_normalize          | 110 ms                                                 | 105 ms: 1.05x faster                                         |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                         |
| sqlglot_optimize           | 54.8 ms                                                | 52.4 ms: 1.05x faster                                        |
| xml_etree_process          | 61.7 ms                                                | 59.1 ms: 1.04x faster                                        |
| nqueens                    | 83.3 ms                                                | 79.8 ms: 1.04x faster                                        |
| fannkuch                   | 417 ms                                                 | 401 ms: 1.04x faster                                         |
| richards_super             | 51.5 ms                                                | 49.9 ms: 1.03x faster                                        |
| nbody                      | 97.0 ms                                                | 94.3 ms: 1.03x faster                                        |
| hexiom                     | 6.41 ms                                                | 6.24 ms: 1.03x faster                                        |
| sqlite_synth               | 2.83 us                                                | 2.77 us: 1.02x faster                                        |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                         |
| pyflate                    | 482 ms                                                 | 474 ms: 1.02x faster                                         |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                       |
| pickle_pure_python         | 324 us                                                 | 321 us: 1.01x faster                                         |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                        |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                         |
| regex_dna                  | 212 ms                                                 | 211 ms: 1.01x faster                                         |
| logging_silent             | 104 ns                                                 | 106 ns: 1.01x slower                                         |
| typing_runtime_protocols   | 158 us                                                 | 160 us: 1.01x slower                                         |
| python_startup_no_site     | 6.94 ms                                                | 7.05 ms: 1.02x slower                                        |
| bench_thread_pool          | 842 us                                                 | 863 us: 1.03x slower                                         |
| json_loads                 | 28.5 us                                                | 29.8 us: 1.05x slower                                        |
| telco                      | 7.10 ms                                                | 7.77 ms: 1.09x slower                                        |
| regex_v8                   | 23.1 ms                                                | 26.1 ms: 1.13x slower                                        |
| json_dumps                 | 10.4 ms                                                | 12.0 ms: 1.16x slower                                        |
| coverage                   | 72.7 ms                                                | 90.7 ms: 1.25x slower                                        |
| gc_traversal               | 3.79 ms                                                | 4.78 ms: 1.26x slower                                        |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                        |
| create_gc_cycles           | 1.48 ms                                                | 2.45 ms: 1.66x slower                                        |
| bench_mp_pool              | 24.0 ms                                                | 81.2 ms: 3.38x slower                                        |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                 |

Benchmark hidden because not significant (2): asyncio_websockets, json
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250117-3.14.0a4+-e537b8b/bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.118x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.09x