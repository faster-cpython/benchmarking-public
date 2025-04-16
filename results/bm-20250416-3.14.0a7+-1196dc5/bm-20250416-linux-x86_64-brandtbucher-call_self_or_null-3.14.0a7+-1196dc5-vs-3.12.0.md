# Results vs. 3.12.0

- fork: brandtbucher
- ref: call_self_or_null
- machine: linux-x86_64
- commit hash: 1196dc5
- commit date: 2025-04-16
- overall geometric mean: 1.120x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-1196dc5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 250 ms: 1.10x faster                                                      |
| docutils       | 2.77 sec                                               | 2.59 sec: 1.07x faster                                                    |
| Geometric mean | (ref)                                                  | 1.08x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-1196dc5 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 623 ms: 1.90x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 624 ms: 1.85x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 318 ms: 1.82x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 320 ms: 1.79x faster                                                      |
| async_tree_none            | 472 ms                                                 | 263 ms: 1.79x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.78x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 480 ms: 1.51x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 485 ms: 1.50x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-1196dc5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 73.0 ms: 1.16x faster                                                     |
| pidigits       | 187 ms                                                 | 194 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                  | 1.04x faster                                                              |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-1196dc5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                      |
| regex_effbot   | 3.61 ms                                                | 3.25 ms: 1.11x faster                                                     |
| regex_v8       | 23.1 ms                                                | 22.6 ms: 1.02x faster                                                     |
| regex_dna      | 212 ms                                                 | 212 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                  | 1.07x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-1196dc5 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                    |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                 | 98.7 ms: 1.08x faster                                                     |
| xml_etree_generate   | 89.2 ms                                                | 84.1 ms: 1.06x faster                                                     |
| xml_etree_process    | 61.7 ms                                                | 58.7 ms: 1.05x faster                                                     |
| pickle_pure_python   | 324 us                                                 | 318 us: 1.02x faster                                                      |
| unpickle_pure_python | 230 us                                                 | 231 us: 1.01x slower                                                      |
| json_loads           | 28.5 us                                                | 29.4 us: 1.03x slower                                                     |
| json_dumps           | 10.4 ms                                                | 11.4 ms: 1.10x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-1196dc5 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.24 ms: 1.19x slower                                                     |
| python_startup         | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-1196dc5 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.6 ms: 1.09x faster                                                     |
| mako            | 11.9 ms                                                | 11.0 ms: 1.09x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-1196dc5 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.20 sec: 2.19x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 623 ms: 1.90x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 624 ms: 1.85x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 318 ms: 1.82x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 320 ms: 1.79x faster                                                      |
| async_tree_none            | 472 ms                                                 | 263 ms: 1.79x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.78x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 480 ms: 1.51x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 485 ms: 1.50x faster                                                      |
| deepcopy                   | 371 us                                                 | 249 us: 1.49x faster                                                      |
| deepcopy_memo              | 40.7 us                                                | 28.4 us: 1.44x faster                                                     |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.30x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                | 2.63 us: 1.27x faster                                                     |
| go                         | 139 ms                                                 | 113 ms: 1.24x faster                                                      |
| tomli_loads                | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                    |
| logging_format             | 7.23 us                                                | 6.12 us: 1.18x faster                                                     |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                      |
| float                      | 84.7 ms                                                | 73.0 ms: 1.16x faster                                                     |
| async_generators           | 463 ms                                                 | 400 ms: 1.16x faster                                                      |
| logging_simple             | 6.46 us                                                | 5.62 us: 1.15x faster                                                     |
| scimark_monte_carlo        | 75.1 ms                                                | 65.6 ms: 1.15x faster                                                     |
| dulwich_log                | 68.5 ms                                                | 60.0 ms: 1.14x faster                                                     |
| pathlib                    | 19.3 ms                                                | 16.9 ms: 1.14x faster                                                     |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                                      |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                      |
| sympy_str                  | 300 ms                                                 | 265 ms: 1.13x faster                                                      |
| crypto_pyaes               | 81.9 ms                                                | 72.8 ms: 1.12x faster                                                     |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.11x faster                                                      |
| sqlalchemy_declarative     | 147 ms                                                 | 132 ms: 1.11x faster                                                      |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.8 ms: 1.11x faster                                                     |
| regex_effbot               | 3.61 ms                                                | 3.25 ms: 1.11x faster                                                     |
| sympy_integrate            | 21.4 ms                                                | 19.4 ms: 1.10x faster                                                     |
| chaos                      | 67.0 ms                                                | 60.7 ms: 1.10x faster                                                     |
| 2to3                       | 274 ms                                                 | 250 ms: 1.10x faster                                                      |
| django_template            | 34.6 ms                                                | 31.6 ms: 1.09x faster                                                     |
| deltablue                  | 3.72 ms                                                | 3.40 ms: 1.09x faster                                                     |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.09x faster                                                      |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.09x faster                                                     |
| richards                   | 45.8 ms                                                | 42.2 ms: 1.09x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                 | 98.7 ms: 1.08x faster                                                     |
| scimark_fft                | 382 ms                                                 | 355 ms: 1.08x faster                                                      |
| pprint_safe_repr           | 776 ms                                                 | 726 ms: 1.07x faster                                                      |
| docutils                   | 2.77 sec                                               | 2.59 sec: 1.07x faster                                                    |
| generators                 | 31.2 ms                                                | 29.3 ms: 1.07x faster                                                     |
| pyflate                    | 482 ms                                                 | 452 ms: 1.07x faster                                                      |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.07x faster                                                    |
| raytrace                   | 312 ms                                                 | 293 ms: 1.07x faster                                                      |
| richards_super             | 51.5 ms                                                | 48.3 ms: 1.07x faster                                                     |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.74 ms: 1.07x faster                                                     |
| sympy_expand               | 478 ms                                                 | 448 ms: 1.07x faster                                                      |
| logging_silent             | 104 ns                                                 | 98.5 ns: 1.06x faster                                                     |
| xml_etree_generate         | 89.2 ms                                                | 84.1 ms: 1.06x faster                                                     |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                      |
| xml_etree_process          | 61.7 ms                                                | 58.7 ms: 1.05x faster                                                     |
| hexiom                     | 6.41 ms                                                | 6.24 ms: 1.03x faster                                                     |
| nqueens                    | 83.3 ms                                                | 81.3 ms: 1.02x faster                                                     |
| regex_v8                   | 23.1 ms                                                | 22.6 ms: 1.02x faster                                                     |
| pickle_pure_python         | 324 us                                                 | 318 us: 1.02x faster                                                      |
| pycparser                  | 1.18 sec                                               | 1.17 sec: 1.01x faster                                                    |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                                     |
| fannkuch                   | 417 ms                                                 | 415 ms: 1.01x faster                                                      |
| regex_dna                  | 212 ms                                                 | 212 ms: 1.00x faster                                                      |
| unpickle_pure_python       | 230 us                                                 | 231 us: 1.01x slower                                                      |
| json_loads                 | 28.5 us                                                | 29.4 us: 1.03x slower                                                     |
| pidigits                   | 187 ms                                                 | 194 ms: 1.04x slower                                                      |
| coroutines                 | 23.2 ms                                                | 24.2 ms: 1.05x slower                                                     |
| bench_thread_pool          | 842 us                                                 | 886 us: 1.05x slower                                                      |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                                      |
| telco                      | 7.10 ms                                                | 7.79 ms: 1.10x slower                                                     |
| json_dumps                 | 10.4 ms                                                | 11.4 ms: 1.10x slower                                                     |
| coverage                   | 72.7 ms                                                | 86.3 ms: 1.19x slower                                                     |
| python_startup_no_site     | 6.94 ms                                                | 8.24 ms: 1.19x slower                                                     |
| gc_traversal               | 3.79 ms                                                | 5.05 ms: 1.33x slower                                                     |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 2.48 ms: 1.68x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 81.7 ms: 3.40x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                              |

Benchmark hidden because not significant (4): nbody, json, asyncio_websockets, scimark_lu
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250416-3.14.0a7+-1196dc5/bm-20250416-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-1196dc5.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.120x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.11x