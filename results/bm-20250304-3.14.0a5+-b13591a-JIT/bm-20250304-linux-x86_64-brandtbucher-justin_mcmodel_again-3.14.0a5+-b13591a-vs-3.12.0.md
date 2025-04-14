# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_mcmodel_again
- machine: linux-x86_64
- commit hash: b13591a
- commit date: 2025-03-04
- overall geometric mean: 1.111x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250304-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-b13591a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 260 ms: 1.06x faster                                                         |
| docutils       | 2.77 sec                                               | 2.66 sec: 1.04x faster                                                       |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250304-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-b13591a |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 610 ms: 1.89x faster                                                         |
| async_tree_io_tg           | 1.18 sec                                               | 627 ms: 1.89x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                         |
| async_tree_none            | 472 ms                                                 | 264 ms: 1.78x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 332 ms: 1.74x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 485 ms: 1.50x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 494 ms: 1.47x faster                                                         |
| Geometric mean             | (ref)                                                  | 1.73x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250304-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-b13591a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.0 ms: 1.23x faster                                                        |
| nbody          | 97.0 ms                                                | 86.7 ms: 1.12x faster                                                        |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250304-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-b13591a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.16x faster                                                         |
| regex_effbot   | 3.61 ms                                                | 3.46 ms: 1.04x faster                                                        |
| regex_dna      | 212 ms                                                 | 225 ms: 1.06x slower                                                         |
| regex_v8       | 23.1 ms                                                | 25.6 ms: 1.11x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250304-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-b13591a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.88 sec: 1.24x faster                                                       |
| xml_etree_generate   | 89.2 ms                                                | 79.1 ms: 1.13x faster                                                        |
| unpickle_pure_python | 230 us                                                 | 206 us: 1.12x faster                                                         |
| xml_etree_process    | 61.7 ms                                                | 55.2 ms: 1.12x faster                                                        |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                                         |
| xml_etree_iterparse  | 107 ms                                                 | 99.0 ms: 1.08x faster                                                        |
| json_loads           | 28.5 us                                                | 29.8 us: 1.05x slower                                                        |
| json_dumps           | 10.4 ms                                                | 11.3 ms: 1.09x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                                 |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250304-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-b13591a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.12 ms: 1.03x slower                                                        |
| python_startup         | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.18x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250304-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-b13591a |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.5 ms: 1.13x faster                                                        |
| django_template | 34.6 ms                                                | 31.8 ms: 1.09x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.11x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250304-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-b13591a |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 610 ms: 1.89x faster                                                         |
| async_tree_io_tg           | 1.18 sec                                               | 627 ms: 1.89x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                         |
| async_tree_none            | 472 ms                                                 | 264 ms: 1.78x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 332 ms: 1.74x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 485 ms: 1.50x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 494 ms: 1.47x faster                                                         |
| deepcopy                   | 371 us                                                 | 259 us: 1.43x faster                                                         |
| deepcopy_memo              | 40.7 us                                                | 29.4 us: 1.38x faster                                                        |
| tomli_loads                | 2.33 sec                                               | 1.88 sec: 1.24x faster                                                       |
| deepcopy_reduce            | 3.35 us                                                | 2.70 us: 1.24x faster                                                        |
| comprehensions             | 21.8 us                                                | 17.6 us: 1.24x faster                                                        |
| scimark_fft                | 382 ms                                                 | 310 ms: 1.23x faster                                                         |
| float                      | 84.7 ms                                                | 69.0 ms: 1.23x faster                                                        |
| spectral_norm              | 115 ms                                                 | 95.4 ms: 1.20x faster                                                        |
| go                         | 139 ms                                                 | 118 ms: 1.18x faster                                                         |
| logging_simple             | 6.46 us                                                | 5.49 us: 1.18x faster                                                        |
| logging_format             | 7.23 us                                                | 6.15 us: 1.18x faster                                                        |
| regex_compile              | 148 ms                                                 | 127 ms: 1.16x faster                                                         |
| pathlib                    | 19.3 ms                                                | 16.8 ms: 1.15x faster                                                        |
| raytrace                   | 312 ms                                                 | 272 ms: 1.15x faster                                                         |
| mako                       | 11.9 ms                                                | 10.5 ms: 1.13x faster                                                        |
| chaos                      | 67.0 ms                                                | 59.2 ms: 1.13x faster                                                        |
| sqlalchemy_declarative     | 147 ms                                                 | 130 ms: 1.13x faster                                                         |
| xml_etree_generate         | 89.2 ms                                                | 79.1 ms: 1.13x faster                                                        |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.13x faster                                                         |
| deltablue                  | 3.72 ms                                                | 3.30 ms: 1.13x faster                                                        |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.7 ms: 1.12x faster                                                        |
| unpickle_pure_python       | 230 us                                                 | 206 us: 1.12x faster                                                         |
| nbody                      | 97.0 ms                                                | 86.7 ms: 1.12x faster                                                        |
| xml_etree_process          | 61.7 ms                                                | 55.2 ms: 1.12x faster                                                        |
| async_generators           | 463 ms                                                 | 414 ms: 1.12x faster                                                         |
| generators                 | 31.2 ms                                                | 28.1 ms: 1.11x faster                                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 67.8 ms: 1.11x faster                                                        |
| crypto_pyaes               | 81.9 ms                                                | 74.0 ms: 1.11x faster                                                        |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                                         |
| sympy_str                  | 300 ms                                                 | 274 ms: 1.09x faster                                                         |
| django_template            | 34.6 ms                                                | 31.8 ms: 1.09x faster                                                        |
| pyflate                    | 482 ms                                                 | 445 ms: 1.08x faster                                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.69 ms: 1.08x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                 | 99.0 ms: 1.08x faster                                                        |
| pprint_safe_repr           | 776 ms                                                 | 725 ms: 1.07x faster                                                         |
| sympy_integrate            | 21.4 ms                                                | 20.1 ms: 1.06x faster                                                        |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.06x faster                                                        |
| sqlglot_transpile          | 1.68 ms                                                | 1.59 ms: 1.06x faster                                                        |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                                       |
| 2to3                       | 274 ms                                                 | 260 ms: 1.06x faster                                                         |
| mdp                        | 2.63 sec                                               | 2.49 sec: 1.06x faster                                                       |
| scimark_sor                | 129 ms                                                 | 123 ms: 1.05x faster                                                         |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                         |
| richards                   | 45.8 ms                                                | 43.9 ms: 1.04x faster                                                        |
| sqlglot_normalize          | 110 ms                                                 | 106 ms: 1.04x faster                                                         |
| regex_effbot               | 3.61 ms                                                | 3.46 ms: 1.04x faster                                                        |
| docutils                   | 2.77 sec                                               | 2.66 sec: 1.04x faster                                                       |
| sqlite_synth               | 2.83 us                                                | 2.73 us: 1.04x faster                                                        |
| fannkuch                   | 417 ms                                                 | 404 ms: 1.03x faster                                                         |
| sqlglot_optimize           | 54.8 ms                                                | 53.2 ms: 1.03x faster                                                        |
| nqueens                    | 83.3 ms                                                | 81.0 ms: 1.03x faster                                                        |
| dulwich_log                | 68.5 ms                                                | 66.8 ms: 1.03x faster                                                        |
| richards_super             | 51.5 ms                                                | 50.5 ms: 1.02x faster                                                        |
| sympy_expand               | 478 ms                                                 | 469 ms: 1.02x faster                                                         |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.01x faster                                                       |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.01x faster                                                         |
| hexiom                     | 6.41 ms                                                | 6.36 ms: 1.01x faster                                                        |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                         |
| json                       | 5.26 ms                                                | 5.31 ms: 1.01x slower                                                        |
| logging_silent             | 104 ns                                                 | 107 ns: 1.02x slower                                                         |
| typing_runtime_protocols   | 158 us                                                 | 161 us: 1.02x slower                                                         |
| python_startup_no_site     | 6.94 ms                                                | 7.12 ms: 1.03x slower                                                        |
| coroutines                 | 23.2 ms                                                | 23.9 ms: 1.03x slower                                                        |
| bench_thread_pool          | 842 us                                                 | 874 us: 1.04x slower                                                         |
| json_loads                 | 28.5 us                                                | 29.8 us: 1.05x slower                                                        |
| regex_dna                  | 212 ms                                                 | 225 ms: 1.06x slower                                                         |
| telco                      | 7.10 ms                                                | 7.69 ms: 1.08x slower                                                        |
| json_dumps                 | 10.4 ms                                                | 11.3 ms: 1.09x slower                                                        |
| regex_v8                   | 23.1 ms                                                | 25.6 ms: 1.11x slower                                                        |
| coverage                   | 72.7 ms                                                | 85.2 ms: 1.17x slower                                                        |
| gc_traversal               | 3.79 ms                                                | 4.63 ms: 1.22x slower                                                        |
| python_startup             | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                        |
| create_gc_cycles           | 1.48 ms                                                | 2.43 ms: 1.64x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 81.8 ms: 3.41x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                                 |

Benchmark hidden because not significant (2): asyncio_websockets, pickle_pure_python
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250304-3.14.0a5+-b13591a-JIT/bm-20250304-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-b13591a.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.111x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.10x