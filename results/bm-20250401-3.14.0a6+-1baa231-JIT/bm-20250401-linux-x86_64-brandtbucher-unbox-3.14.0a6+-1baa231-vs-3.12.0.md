# Results vs. 3.12.0

- fork: brandtbucher
- ref: unbox
- machine: linux-x86_64
- commit hash: 1baa231
- commit date: 2025-04-01
- overall geometric mean: 1.093x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 270 ms: 1.02x faster                                          |
| docutils       | 2.77 sec                                               | 2.73 sec: 1.01x faster                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 637 ms: 1.86x faster                                          |
| async_tree_io              | 1.16 sec                                               | 634 ms: 1.82x faster                                          |
| async_tree_memoization     | 578 ms                                                 | 323 ms: 1.79x faster                                          |
| async_tree_none            | 472 ms                                                 | 267 ms: 1.77x faster                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 328 ms: 1.75x faster                                          |
| async_tree_none_tg         | 450 ms                                                 | 259 ms: 1.74x faster                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 486 ms: 1.49x faster                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 497 ms: 1.46x faster                                          |
| Geometric mean             | (ref)                                                  | 1.70x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.7 ms: 1.22x faster                                         |
| nbody          | 97.0 ms                                                | 91.3 ms: 1.06x faster                                         |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                          |
| Geometric mean | (ref)                                                  | 1.09x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.19 ms: 1.13x faster                                         |
| regex_compile  | 148 ms                                                 | 133 ms: 1.11x faster                                          |
| regex_v8       | 23.1 ms                                                | 22.5 ms: 1.03x faster                                         |
| regex_dna      | 212 ms                                                 | 215 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                  | 1.06x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.79 sec: 1.30x faster                                        |
| xml_etree_parse      | 159 ms                                                 | 142 ms: 1.12x faster                                          |
| xml_etree_generate   | 89.2 ms                                                | 83.5 ms: 1.07x faster                                         |
| xml_etree_iterparse  | 107 ms                                                 | 100 ms: 1.07x faster                                          |
| xml_etree_process    | 61.7 ms                                                | 58.8 ms: 1.05x faster                                         |
| unpickle_pure_python | 230 us                                                 | 231 us: 1.00x slower                                          |
| pickle_pure_python   | 324 us                                                 | 334 us: 1.03x slower                                          |
| json_dumps           | 10.4 ms                                                | 11.5 ms: 1.10x slower                                         |
| json_loads           | 28.5 us                                                | 31.9 us: 1.12x slower                                         |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.21 ms: 1.18x slower                                         |
| python_startup         | 9.55 ms                                                | 13.2 ms: 1.38x slower                                         |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 33.1 ms: 1.04x faster                                         |
| mako            | 11.9 ms                                                | 11.8 ms: 1.01x faster                                         |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.27 sec: 2.07x faster                                        |
| async_tree_io_tg           | 1.18 sec                                               | 637 ms: 1.86x faster                                          |
| async_tree_io              | 1.16 sec                                               | 634 ms: 1.82x faster                                          |
| async_tree_memoization     | 578 ms                                                 | 323 ms: 1.79x faster                                          |
| async_tree_none            | 472 ms                                                 | 267 ms: 1.77x faster                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 328 ms: 1.75x faster                                          |
| async_tree_none_tg         | 450 ms                                                 | 259 ms: 1.74x faster                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 486 ms: 1.49x faster                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 497 ms: 1.46x faster                                          |
| deepcopy                   | 371 us                                                 | 266 us: 1.40x faster                                          |
| deepcopy_memo              | 40.7 us                                                | 29.9 us: 1.36x faster                                         |
| tomli_loads                | 2.33 sec                                               | 1.79 sec: 1.30x faster                                        |
| float                      | 84.7 ms                                                | 69.7 ms: 1.22x faster                                         |
| richards                   | 45.8 ms                                                | 38.0 ms: 1.20x faster                                         |
| deepcopy_reduce            | 3.35 us                                                | 2.82 us: 1.19x faster                                         |
| logging_format             | 7.23 us                                                | 6.12 us: 1.18x faster                                         |
| richards_super             | 51.5 ms                                                | 44.1 ms: 1.17x faster                                         |
| logging_simple             | 6.46 us                                                | 5.56 us: 1.16x faster                                         |
| scimark_fft                | 382 ms                                                 | 329 ms: 1.16x faster                                          |
| spectral_norm              | 115 ms                                                 | 99.5 ms: 1.15x faster                                         |
| pathlib                    | 19.3 ms                                                | 16.8 ms: 1.15x faster                                         |
| chaos                      | 67.0 ms                                                | 58.9 ms: 1.14x faster                                         |
| regex_effbot               | 3.61 ms                                                | 3.19 ms: 1.13x faster                                         |
| xml_etree_parse            | 159 ms                                                 | 142 ms: 1.12x faster                                          |
| coroutines                 | 23.2 ms                                                | 20.7 ms: 1.12x faster                                         |
| regex_compile              | 148 ms                                                 | 133 ms: 1.11x faster                                          |
| raytrace                   | 312 ms                                                 | 281 ms: 1.11x faster                                          |
| deltablue                  | 3.72 ms                                                | 3.34 ms: 1.11x faster                                         |
| comprehensions             | 21.8 us                                                | 19.6 us: 1.11x faster                                         |
| dulwich_log                | 68.5 ms                                                | 61.9 ms: 1.11x faster                                         |
| sympy_sum                  | 169 ms                                                 | 154 ms: 1.10x faster                                          |
| generators                 | 31.2 ms                                                | 28.5 ms: 1.09x faster                                         |
| sqlalchemy_declarative     | 147 ms                                                 | 135 ms: 1.09x faster                                          |
| async_generators           | 463 ms                                                 | 426 ms: 1.09x faster                                          |
| scimark_monte_carlo        | 75.1 ms                                                | 69.8 ms: 1.08x faster                                         |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.5 ms: 1.07x faster                                         |
| xml_etree_generate         | 89.2 ms                                                | 83.5 ms: 1.07x faster                                         |
| xml_etree_iterparse        | 107 ms                                                 | 100 ms: 1.07x faster                                          |
| sympy_str                  | 300 ms                                                 | 281 ms: 1.07x faster                                          |
| nbody                      | 97.0 ms                                                | 91.3 ms: 1.06x faster                                         |
| sympy_integrate            | 21.4 ms                                                | 20.4 ms: 1.05x faster                                         |
| xml_etree_process          | 61.7 ms                                                | 58.8 ms: 1.05x faster                                         |
| django_template            | 34.6 ms                                                | 33.1 ms: 1.04x faster                                         |
| regex_v8                   | 23.1 ms                                                | 22.5 ms: 1.03x faster                                         |
| pyflate                    | 482 ms                                                 | 470 ms: 1.03x faster                                          |
| 2to3                       | 274 ms                                                 | 270 ms: 1.02x faster                                          |
| sqlite_synth               | 2.83 us                                                | 2.79 us: 1.02x faster                                         |
| docutils                   | 2.77 sec                                               | 2.73 sec: 1.01x faster                                        |
| go                         | 139 ms                                                 | 138 ms: 1.01x faster                                          |
| mako                       | 11.9 ms                                                | 11.8 ms: 1.01x faster                                         |
| logging_silent             | 104 ns                                                 | 103 ns: 1.01x faster                                          |
| meteor_contest             | 112 ms                                                 | 112 ms: 1.01x faster                                          |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                          |
| unpickle_pure_python       | 230 us                                                 | 231 us: 1.00x slower                                          |
| regex_dna                  | 212 ms                                                 | 215 ms: 1.01x slower                                          |
| sympy_expand               | 478 ms                                                 | 487 ms: 1.02x slower                                          |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.21 ms: 1.03x slower                                         |
| pickle_pure_python         | 324 us                                                 | 334 us: 1.03x slower                                          |
| fannkuch                   | 417 ms                                                 | 431 ms: 1.03x slower                                          |
| nqueens                    | 83.3 ms                                                | 86.4 ms: 1.04x slower                                         |
| json                       | 5.26 ms                                                | 5.46 ms: 1.04x slower                                         |
| pprint_safe_repr           | 776 ms                                                 | 805 ms: 1.04x slower                                          |
| pprint_pformat             | 1.57 sec                                               | 1.63 sec: 1.04x slower                                        |
| scimark_lu                 | 118 ms                                                 | 124 ms: 1.05x slower                                          |
| pycparser                  | 1.18 sec                                               | 1.25 sec: 1.06x slower                                        |
| bench_thread_pool          | 842 us                                                 | 897 us: 1.07x slower                                          |
| crypto_pyaes               | 81.9 ms                                                | 87.4 ms: 1.07x slower                                         |
| hexiom                     | 6.41 ms                                                | 6.96 ms: 1.09x slower                                         |
| scimark_sor                | 129 ms                                                 | 141 ms: 1.10x slower                                          |
| json_dumps                 | 10.4 ms                                                | 11.5 ms: 1.10x slower                                         |
| typing_runtime_protocols   | 158 us                                                 | 174 us: 1.10x slower                                          |
| json_loads                 | 28.5 us                                                | 31.9 us: 1.12x slower                                         |
| telco                      | 7.10 ms                                                | 8.06 ms: 1.13x slower                                         |
| coverage                   | 72.7 ms                                                | 85.2 ms: 1.17x slower                                         |
| python_startup_no_site     | 6.94 ms                                                | 8.21 ms: 1.18x slower                                         |
| gc_traversal               | 3.79 ms                                                | 5.06 ms: 1.33x slower                                         |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.38x slower                                         |
| create_gc_cycles           | 1.48 ms                                                | 2.49 ms: 1.69x slower                                         |
| bench_mp_pool              | 24.0 ms                                                | 83.7 ms: 3.49x slower                                         |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                  |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250401-3.14.0a6+-1baa231-JIT/bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.093x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.12x