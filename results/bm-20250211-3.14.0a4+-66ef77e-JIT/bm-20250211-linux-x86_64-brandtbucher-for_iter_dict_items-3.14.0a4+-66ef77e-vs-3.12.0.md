# Results vs. 3.12.0

- fork: brandtbucher
- ref: for_iter_dict_items
- machine: linux-x86_64
- commit hash: 66ef77e
- commit date: 2025-02-11
- overall geometric mean: 1.109x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-66ef77e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 259 ms: 1.06x faster                                                        |
| docutils       | 2.77 sec                                               | 2.67 sec: 1.04x faster                                                      |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-66ef77e |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 614 ms: 1.93x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 620 ms: 1.86x faster                                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 326 ms: 1.77x faster                                                        |
| async_tree_none            | 472 ms                                                 | 267 ms: 1.76x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 258 ms: 1.74x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 481 ms: 1.51x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 493 ms: 1.47x faster                                                        |
| Geometric mean             | (ref)                                                  | 1.73x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-66ef77e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.9 ms: 1.19x faster                                                       |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-66ef77e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 125 ms: 1.18x faster                                                        |
| regex_effbot   | 3.61 ms                                                | 3.20 ms: 1.13x faster                                                       |
| regex_dna      | 212 ms                                                 | 206 ms: 1.03x faster                                                        |
| regex_v8       | 23.1 ms                                                | 23.9 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-66ef77e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.85 sec: 1.26x faster                                                      |
| unpickle_pure_python | 230 us                                                 | 198 us: 1.16x faster                                                        |
| xml_etree_parse      | 159 ms                                                 | 138 ms: 1.16x faster                                                        |
| xml_etree_generate   | 89.2 ms                                                | 78.2 ms: 1.14x faster                                                       |
| xml_etree_process    | 61.7 ms                                                | 55.1 ms: 1.12x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                 | 95.8 ms: 1.11x faster                                                       |
| pickle_pure_python   | 324 us                                                 | 314 us: 1.03x faster                                                        |
| json_dumps           | 10.4 ms                                                | 11.9 ms: 1.14x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                                |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-66ef77e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                       |
| python_startup         | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-66ef77e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.97 ms: 1.19x faster                                                       |
| django_template | 34.6 ms                                                | 31.7 ms: 1.09x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-66ef77e |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 614 ms: 1.93x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 620 ms: 1.86x faster                                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 326 ms: 1.77x faster                                                        |
| async_tree_none            | 472 ms                                                 | 267 ms: 1.76x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 258 ms: 1.74x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 481 ms: 1.51x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 493 ms: 1.47x faster                                                        |
| deepcopy                   | 371 us                                                 | 261 us: 1.42x faster                                                        |
| deepcopy_memo              | 40.7 us                                                | 30.3 us: 1.34x faster                                                       |
| tomli_loads                | 2.33 sec                                               | 1.85 sec: 1.26x faster                                                      |
| comprehensions             | 21.8 us                                                | 17.4 us: 1.25x faster                                                       |
| deepcopy_reduce            | 3.35 us                                                | 2.70 us: 1.24x faster                                                       |
| scimark_fft                | 382 ms                                                 | 311 ms: 1.23x faster                                                        |
| spectral_norm              | 115 ms                                                 | 94.9 ms: 1.21x faster                                                       |
| float                      | 84.7 ms                                                | 70.9 ms: 1.19x faster                                                       |
| mako                       | 11.9 ms                                                | 9.97 ms: 1.19x faster                                                       |
| logging_format             | 7.23 us                                                | 6.10 us: 1.19x faster                                                       |
| crypto_pyaes               | 81.9 ms                                                | 69.1 ms: 1.19x faster                                                       |
| regex_compile              | 148 ms                                                 | 125 ms: 1.18x faster                                                        |
| pathlib                    | 19.3 ms                                                | 16.4 ms: 1.18x faster                                                       |
| logging_simple             | 6.46 us                                                | 5.52 us: 1.17x faster                                                       |
| unpickle_pure_python       | 230 us                                                 | 198 us: 1.16x faster                                                        |
| xml_etree_parse            | 159 ms                                                 | 138 ms: 1.16x faster                                                        |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.39 ms: 1.15x faster                                                       |
| scimark_monte_carlo        | 75.1 ms                                                | 65.6 ms: 1.15x faster                                                       |
| chaos                      | 67.0 ms                                                | 58.6 ms: 1.14x faster                                                       |
| xml_etree_generate         | 89.2 ms                                                | 78.2 ms: 1.14x faster                                                       |
| raytrace                   | 312 ms                                                 | 277 ms: 1.13x faster                                                        |
| regex_effbot               | 3.61 ms                                                | 3.20 ms: 1.13x faster                                                       |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                                        |
| async_generators           | 463 ms                                                 | 412 ms: 1.12x faster                                                        |
| xml_etree_process          | 61.7 ms                                                | 55.1 ms: 1.12x faster                                                       |
| generators                 | 31.2 ms                                                | 27.9 ms: 1.12x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                 | 95.8 ms: 1.11x faster                                                       |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.9 ms: 1.10x faster                                                       |
| django_template            | 34.6 ms                                                | 31.7 ms: 1.09x faster                                                       |
| deltablue                  | 3.72 ms                                                | 3.43 ms: 1.08x faster                                                       |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.08x faster                                                        |
| go                         | 139 ms                                                 | 129 ms: 1.08x faster                                                        |
| sympy_sum                  | 169 ms                                                 | 157 ms: 1.08x faster                                                        |
| sympy_str                  | 300 ms                                                 | 281 ms: 1.07x faster                                                        |
| pycparser                  | 1.18 sec                                               | 1.11 sec: 1.06x faster                                                      |
| 2to3                       | 274 ms                                                 | 259 ms: 1.06x faster                                                        |
| sympy_integrate            | 21.4 ms                                                | 20.2 ms: 1.06x faster                                                       |
| fannkuch                   | 417 ms                                                 | 394 ms: 1.06x faster                                                        |
| pyflate                    | 482 ms                                                 | 462 ms: 1.04x faster                                                        |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                                       |
| richards                   | 45.8 ms                                                | 44.0 ms: 1.04x faster                                                       |
| sqlite_synth               | 2.83 us                                                | 2.72 us: 1.04x faster                                                       |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                        |
| dulwich_log                | 68.5 ms                                                | 66.0 ms: 1.04x faster                                                       |
| docutils                   | 2.77 sec                                               | 2.67 sec: 1.04x faster                                                      |
| sqlglot_transpile          | 1.68 ms                                                | 1.63 ms: 1.03x faster                                                       |
| regex_dna                  | 212 ms                                                 | 206 ms: 1.03x faster                                                        |
| pickle_pure_python         | 324 us                                                 | 314 us: 1.03x faster                                                        |
| mdp                        | 2.63 sec                                               | 2.56 sec: 1.03x faster                                                      |
| richards_super             | 51.5 ms                                                | 50.1 ms: 1.03x faster                                                       |
| pprint_pformat             | 1.57 sec                                               | 1.53 sec: 1.02x faster                                                      |
| json                       | 5.26 ms                                                | 5.13 ms: 1.02x faster                                                       |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                                        |
| pprint_safe_repr           | 776 ms                                                 | 760 ms: 1.02x faster                                                        |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                        |
| sqlglot_normalize          | 110 ms                                                 | 110 ms: 1.01x faster                                                        |
| sympy_expand               | 478 ms                                                 | 482 ms: 1.01x slower                                                        |
| coroutines                 | 23.2 ms                                                | 23.4 ms: 1.01x slower                                                       |
| sqlglot_optimize           | 54.8 ms                                                | 55.4 ms: 1.01x slower                                                       |
| python_startup_no_site     | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                       |
| logging_silent             | 104 ns                                                 | 107 ns: 1.02x slower                                                        |
| typing_runtime_protocols   | 158 us                                                 | 162 us: 1.02x slower                                                        |
| regex_v8                   | 23.1 ms                                                | 23.9 ms: 1.03x slower                                                       |
| bench_thread_pool          | 842 us                                                 | 888 us: 1.06x slower                                                        |
| telco                      | 7.10 ms                                                | 7.61 ms: 1.07x slower                                                       |
| hexiom                     | 6.41 ms                                                | 6.93 ms: 1.08x slower                                                       |
| nqueens                    | 83.3 ms                                                | 90.0 ms: 1.08x slower                                                       |
| json_dumps                 | 10.4 ms                                                | 11.9 ms: 1.14x slower                                                       |
| coverage                   | 72.7 ms                                                | 89.1 ms: 1.23x slower                                                       |
| gc_traversal               | 3.79 ms                                                | 4.99 ms: 1.32x slower                                                       |
| python_startup             | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                       |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.67x slower                                                       |
| bench_mp_pool              | 24.0 ms                                                | 81.4 ms: 3.39x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                                |

Benchmark hidden because not significant (3): asyncio_websockets, json_loads, nbody
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250211-3.14.0a4+-66ef77e-JIT/bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-66ef77e.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.109x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.11x