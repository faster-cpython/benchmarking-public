# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_up_10_6
- machine: linux-x86_64
- commit hash: 89bbf67
- commit date: 2025-03-29
- overall geometric mean: 1.111x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_6-3.14.0a6+-89bbf67 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 267 ms: 1.03x faster                                                |
| docutils       | 2.77 sec                                               | 2.70 sec: 1.02x faster                                              |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_6-3.14.0a6+-89bbf67 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 621 ms: 1.90x faster                                                |
| async_tree_io              | 1.16 sec                                               | 616 ms: 1.88x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 315 ms: 1.83x faster                                                |
| async_tree_none            | 472 ms                                                 | 260 ms: 1.82x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.78x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 477 ms: 1.52x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 492 ms: 1.47x faster                                                |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_6-3.14.0a6+-89bbf67 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 64.8 ms: 1.31x faster                                               |
| nbody          | 97.0 ms                                                | 86.6 ms: 1.12x faster                                               |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                  | 1.14x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_6-3.14.0a6+-89bbf67 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.08 ms: 1.17x faster                                               |
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                |
| regex_v8       | 23.1 ms                                                | 22.7 ms: 1.02x faster                                               |
| regex_dna      | 212 ms                                                 | 211 ms: 1.00x faster                                                |
| Geometric mean | (ref)                                                  | 1.08x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_6-3.14.0a6+-89bbf67 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.89 sec: 1.23x faster                                              |
| xml_etree_parse      | 159 ms                                                 | 139 ms: 1.14x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 80.2 ms: 1.11x faster                                               |
| unpickle_pure_python | 230 us                                                 | 211 us: 1.09x faster                                                |
| xml_etree_process    | 61.7 ms                                                | 56.7 ms: 1.09x faster                                               |
| xml_etree_iterparse  | 107 ms                                                 | 98.7 ms: 1.08x faster                                               |
| pickle_pure_python   | 324 us                                                 | 328 us: 1.01x slower                                                |
| json_loads           | 28.5 us                                                | 30.1 us: 1.06x slower                                               |
| json_dumps           | 10.4 ms                                                | 11.5 ms: 1.11x slower                                               |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_6-3.14.0a6+-89bbf67 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.23 ms: 1.19x slower                                               |
| python_startup         | 9.55 ms                                                | 13.2 ms: 1.38x slower                                               |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_6-3.14.0a6+-89bbf67 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.8 ms: 1.09x faster                                               |
| mako            | 11.9 ms                                                | 11.1 ms: 1.08x faster                                               |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_6-3.14.0a6+-89bbf67 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 621 ms: 1.90x faster                                                |
| async_tree_io              | 1.16 sec                                               | 616 ms: 1.88x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 315 ms: 1.83x faster                                                |
| async_tree_none            | 472 ms                                                 | 260 ms: 1.82x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.78x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 477 ms: 1.52x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 492 ms: 1.47x faster                                                |
| deepcopy                   | 371 us                                                 | 265 us: 1.40x faster                                                |
| deepcopy_memo              | 40.7 us                                                | 29.1 us: 1.40x faster                                               |
| float                      | 84.7 ms                                                | 64.8 ms: 1.31x faster                                               |
| tomli_loads                | 2.33 sec                                               | 1.89 sec: 1.23x faster                                              |
| richards                   | 45.8 ms                                                | 37.2 ms: 1.23x faster                                               |
| deltablue                  | 3.72 ms                                                | 3.03 ms: 1.22x faster                                               |
| deepcopy_reduce            | 3.35 us                                                | 2.74 us: 1.22x faster                                               |
| scimark_fft                | 382 ms                                                 | 313 ms: 1.22x faster                                                |
| richards_super             | 51.5 ms                                                | 42.8 ms: 1.20x faster                                               |
| comprehensions             | 21.8 us                                                | 18.4 us: 1.19x faster                                               |
| logging_format             | 7.23 us                                                | 6.11 us: 1.18x faster                                               |
| spectral_norm              | 115 ms                                                 | 97.4 ms: 1.18x faster                                               |
| regex_effbot               | 3.61 ms                                                | 3.08 ms: 1.17x faster                                               |
| raytrace                   | 312 ms                                                 | 267 ms: 1.17x faster                                                |
| logging_simple             | 6.46 us                                                | 5.55 us: 1.16x faster                                               |
| pathlib                    | 19.3 ms                                                | 16.7 ms: 1.16x faster                                               |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                |
| xml_etree_parse            | 159 ms                                                 | 139 ms: 1.14x faster                                                |
| dulwich_log                | 68.5 ms                                                | 61.0 ms: 1.12x faster                                               |
| nbody                      | 97.0 ms                                                | 86.6 ms: 1.12x faster                                               |
| chaos                      | 67.0 ms                                                | 59.8 ms: 1.12x faster                                               |
| async_generators           | 463 ms                                                 | 415 ms: 1.11x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 80.2 ms: 1.11x faster                                               |
| scimark_monte_carlo        | 75.1 ms                                                | 68.5 ms: 1.10x faster                                               |
| sympy_sum                  | 169 ms                                                 | 155 ms: 1.09x faster                                                |
| unpickle_pure_python       | 230 us                                                 | 211 us: 1.09x faster                                                |
| xml_etree_process          | 61.7 ms                                                | 56.7 ms: 1.09x faster                                               |
| django_template            | 34.6 ms                                                | 31.8 ms: 1.09x faster                                               |
| pyflate                    | 482 ms                                                 | 443 ms: 1.09x faster                                                |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.09x faster                                                |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.65 ms: 1.09x faster                                               |
| xml_etree_iterparse        | 107 ms                                                 | 98.7 ms: 1.08x faster                                               |
| go                         | 139 ms                                                 | 129 ms: 1.08x faster                                                |
| crypto_pyaes               | 81.9 ms                                                | 76.0 ms: 1.08x faster                                               |
| mako                       | 11.9 ms                                                | 11.1 ms: 1.08x faster                                               |
| generators                 | 31.2 ms                                                | 29.0 ms: 1.07x faster                                               |
| sympy_str                  | 300 ms                                                 | 279 ms: 1.07x faster                                                |
| sqlalchemy_declarative     | 147 ms                                                 | 138 ms: 1.07x faster                                                |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.6 ms: 1.06x faster                                               |
| sympy_integrate            | 21.4 ms                                                | 20.4 ms: 1.05x faster                                               |
| mdp                        | 2.63 sec                                               | 2.51 sec: 1.05x faster                                              |
| logging_silent             | 104 ns                                                 | 100 ns: 1.04x faster                                                |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.04x faster                                              |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.04x faster                                                |
| 2to3                       | 274 ms                                                 | 267 ms: 1.03x faster                                                |
| sqlite_synth               | 2.83 us                                                | 2.76 us: 1.03x faster                                               |
| docutils                   | 2.77 sec                                               | 2.70 sec: 1.02x faster                                              |
| pprint_safe_repr           | 776 ms                                                 | 759 ms: 1.02x faster                                                |
| regex_v8                   | 23.1 ms                                                | 22.7 ms: 1.02x faster                                               |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                |
| regex_dna                  | 212 ms                                                 | 211 ms: 1.00x faster                                                |
| coroutines                 | 23.2 ms                                                | 23.4 ms: 1.01x slower                                               |
| json                       | 5.26 ms                                                | 5.31 ms: 1.01x slower                                               |
| scimark_lu                 | 118 ms                                                 | 119 ms: 1.01x slower                                                |
| pickle_pure_python         | 324 us                                                 | 328 us: 1.01x slower                                                |
| fannkuch                   | 417 ms                                                 | 422 ms: 1.01x slower                                                |
| nqueens                    | 83.3 ms                                                | 86.3 ms: 1.04x slower                                               |
| json_loads                 | 28.5 us                                                | 30.1 us: 1.06x slower                                               |
| bench_thread_pool          | 842 us                                                 | 889 us: 1.06x slower                                                |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.06x slower                                                |
| hexiom                     | 6.41 ms                                                | 7.04 ms: 1.10x slower                                               |
| json_dumps                 | 10.4 ms                                                | 11.5 ms: 1.11x slower                                               |
| telco                      | 7.10 ms                                                | 8.16 ms: 1.15x slower                                               |
| python_startup_no_site     | 6.94 ms                                                | 8.23 ms: 1.19x slower                                               |
| coverage                   | 72.7 ms                                                | 86.2 ms: 1.19x slower                                               |
| gc_traversal               | 3.79 ms                                                | 4.82 ms: 1.27x slower                                               |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.38x slower                                               |
| create_gc_cycles           | 1.48 ms                                                | 2.49 ms: 1.69x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 83.4 ms: 3.47x slower                                               |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                        |

Benchmark hidden because not significant (3): sympy_expand, asyncio_websockets, pprint_pformat
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250329-3.14.0a6+-89bbf67-JIT/bm-20250329-linux-x86_64-brandtbucher-jit_up_10_6-3.14.0a6+-89bbf67.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.111x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.12x