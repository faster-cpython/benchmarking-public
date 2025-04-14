# Results vs. 3.12.0

- fork: brandtbucher
- ref: for_iter_dict_items
- machine: linux-x86_64
- commit hash: 46bc2a6
- commit date: 2025-02-11
- overall geometric mean: 1.110x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-46bc2a6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 258 ms: 1.06x faster                                                        |
| docutils       | 2.77 sec                                               | 2.66 sec: 1.04x faster                                                      |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-46bc2a6 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 613 ms: 1.93x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 622 ms: 1.86x faster                                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 318 ms: 1.81x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 328 ms: 1.76x faster                                                        |
| async_tree_none            | 472 ms                                                 | 268 ms: 1.76x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 259 ms: 1.73x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 494 ms: 1.47x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 502 ms: 1.45x faster                                                        |
| Geometric mean             | (ref)                                                  | 1.71x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-46bc2a6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.1 ms: 1.23x faster                                                       |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-46bc2a6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 125 ms: 1.18x faster                                                        |
| regex_effbot   | 3.61 ms                                                | 3.20 ms: 1.13x faster                                                       |
| regex_dna      | 212 ms                                                 | 207 ms: 1.02x faster                                                        |
| regex_v8       | 23.1 ms                                                | 23.8 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-46bc2a6 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.82 sec: 1.28x faster                                                      |
| unpickle_pure_python | 230 us                                                 | 199 us: 1.16x faster                                                        |
| xml_etree_parse      | 159 ms                                                 | 139 ms: 1.15x faster                                                        |
| xml_etree_generate   | 89.2 ms                                                | 78.2 ms: 1.14x faster                                                       |
| xml_etree_process    | 61.7 ms                                                | 54.9 ms: 1.12x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                 | 95.9 ms: 1.11x faster                                                       |
| pickle_pure_python   | 324 us                                                 | 316 us: 1.02x faster                                                        |
| json_loads           | 28.5 us                                                | 28.9 us: 1.02x slower                                                       |
| json_dumps           | 10.4 ms                                                | 12.0 ms: 1.16x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-46bc2a6 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.04 ms: 1.02x slower                                                       |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-46bc2a6 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.0 ms: 1.18x faster                                                       |
| django_template | 34.6 ms                                                | 32.5 ms: 1.06x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.12x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-46bc2a6 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 613 ms: 1.93x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 622 ms: 1.86x faster                                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 318 ms: 1.81x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 328 ms: 1.76x faster                                                        |
| async_tree_none            | 472 ms                                                 | 268 ms: 1.76x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 259 ms: 1.73x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 494 ms: 1.47x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 502 ms: 1.45x faster                                                        |
| deepcopy                   | 371 us                                                 | 260 us: 1.42x faster                                                        |
| deepcopy_memo              | 40.7 us                                                | 30.8 us: 1.32x faster                                                       |
| tomli_loads                | 2.33 sec                                               | 1.82 sec: 1.28x faster                                                      |
| comprehensions             | 21.8 us                                                | 17.2 us: 1.27x faster                                                       |
| spectral_norm              | 115 ms                                                 | 90.9 ms: 1.26x faster                                                       |
| float                      | 84.7 ms                                                | 69.1 ms: 1.23x faster                                                       |
| scimark_fft                | 382 ms                                                 | 312 ms: 1.22x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.74 us: 1.22x faster                                                       |
| logging_format             | 7.23 us                                                | 6.00 us: 1.20x faster                                                       |
| pathlib                    | 19.3 ms                                                | 16.3 ms: 1.19x faster                                                       |
| mako                       | 11.9 ms                                                | 10.0 ms: 1.18x faster                                                       |
| crypto_pyaes               | 81.9 ms                                                | 69.1 ms: 1.18x faster                                                       |
| regex_compile              | 148 ms                                                 | 125 ms: 1.18x faster                                                        |
| logging_simple             | 6.46 us                                                | 5.47 us: 1.18x faster                                                       |
| unpickle_pure_python       | 230 us                                                 | 199 us: 1.16x faster                                                        |
| chaos                      | 67.0 ms                                                | 58.3 ms: 1.15x faster                                                       |
| xml_etree_parse            | 159 ms                                                 | 139 ms: 1.15x faster                                                        |
| xml_etree_generate         | 89.2 ms                                                | 78.2 ms: 1.14x faster                                                       |
| scimark_monte_carlo        | 75.1 ms                                                | 66.0 ms: 1.14x faster                                                       |
| async_generators           | 463 ms                                                 | 410 ms: 1.13x faster                                                        |
| raytrace                   | 312 ms                                                 | 277 ms: 1.13x faster                                                        |
| regex_effbot               | 3.61 ms                                                | 3.20 ms: 1.13x faster                                                       |
| xml_etree_process          | 61.7 ms                                                | 54.9 ms: 1.12x faster                                                       |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                                        |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.52 ms: 1.12x faster                                                       |
| generators                 | 31.2 ms                                                | 28.0 ms: 1.11x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                 | 95.9 ms: 1.11x faster                                                       |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.9 ms: 1.11x faster                                                       |
| deltablue                  | 3.72 ms                                                | 3.38 ms: 1.10x faster                                                       |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.10x faster                                                        |
| pyflate                    | 482 ms                                                 | 441 ms: 1.10x faster                                                        |
| sympy_sum                  | 169 ms                                                 | 156 ms: 1.08x faster                                                        |
| sympy_str                  | 300 ms                                                 | 280 ms: 1.07x faster                                                        |
| 2to3                       | 274 ms                                                 | 258 ms: 1.06x faster                                                        |
| django_template            | 34.6 ms                                                | 32.5 ms: 1.06x faster                                                       |
| go                         | 139 ms                                                 | 131 ms: 1.06x faster                                                        |
| sympy_integrate            | 21.4 ms                                                | 20.3 ms: 1.06x faster                                                       |
| fannkuch                   | 417 ms                                                 | 396 ms: 1.05x faster                                                        |
| pycparser                  | 1.18 sec                                               | 1.12 sec: 1.05x faster                                                      |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.05x faster                                                        |
| sqlglot_transpile          | 1.68 ms                                                | 1.61 ms: 1.04x faster                                                       |
| sqlite_synth               | 2.83 us                                                | 2.72 us: 1.04x faster                                                       |
| docutils                   | 2.77 sec                                               | 2.66 sec: 1.04x faster                                                      |
| richards                   | 45.8 ms                                                | 44.1 ms: 1.04x faster                                                       |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.04x faster                                                        |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                                       |
| dulwich_log                | 68.5 ms                                                | 66.4 ms: 1.03x faster                                                       |
| richards_super             | 51.5 ms                                                | 50.1 ms: 1.03x faster                                                       |
| mdp                        | 2.63 sec                                               | 2.56 sec: 1.03x faster                                                      |
| pickle_pure_python         | 324 us                                                 | 316 us: 1.02x faster                                                        |
| regex_dna                  | 212 ms                                                 | 207 ms: 1.02x faster                                                        |
| json                       | 5.26 ms                                                | 5.14 ms: 1.02x faster                                                       |
| pprint_safe_repr           | 776 ms                                                 | 760 ms: 1.02x faster                                                        |
| coroutines                 | 23.2 ms                                                | 22.7 ms: 1.02x faster                                                       |
| sqlglot_normalize          | 110 ms                                                 | 109 ms: 1.01x faster                                                        |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                        |
| sympy_expand               | 478 ms                                                 | 481 ms: 1.01x slower                                                        |
| sqlglot_optimize           | 54.8 ms                                                | 55.2 ms: 1.01x slower                                                       |
| logging_silent             | 104 ns                                                 | 106 ns: 1.01x slower                                                        |
| python_startup_no_site     | 6.94 ms                                                | 7.04 ms: 1.02x slower                                                       |
| json_loads                 | 28.5 us                                                | 28.9 us: 1.02x slower                                                       |
| regex_v8                   | 23.1 ms                                                | 23.8 ms: 1.03x slower                                                       |
| typing_runtime_protocols   | 158 us                                                 | 163 us: 1.03x slower                                                        |
| bench_thread_pool          | 842 us                                                 | 886 us: 1.05x slower                                                        |
| nqueens                    | 83.3 ms                                                | 89.2 ms: 1.07x slower                                                       |
| hexiom                     | 6.41 ms                                                | 6.93 ms: 1.08x slower                                                       |
| telco                      | 7.10 ms                                                | 7.71 ms: 1.09x slower                                                       |
| json_dumps                 | 10.4 ms                                                | 12.0 ms: 1.16x slower                                                       |
| coverage                   | 72.7 ms                                                | 89.0 ms: 1.22x slower                                                       |
| gc_traversal               | 3.79 ms                                                | 4.94 ms: 1.30x slower                                                       |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                       |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.67x slower                                                       |
| bench_mp_pool              | 24.0 ms                                                | 81.0 ms: 3.37x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                                |

Benchmark hidden because not significant (3): nbody, pprint_pformat, asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250211-3.14.0a4+-46bc2a6-JIT/bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-46bc2a6.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.110x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.11x