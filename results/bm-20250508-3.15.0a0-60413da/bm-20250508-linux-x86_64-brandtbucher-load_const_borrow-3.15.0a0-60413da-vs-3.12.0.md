# Results vs. 3.12.0

- fork: brandtbucher
- ref: load_const_borrow
- machine: linux-x86_64
- commit hash: 60413da
- commit date: 2025-05-08
- overall geometric mean: 1.075x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 257 ms: 1.07x faster                                                     |
| docutils       | 2.77 sec                                               | 2.61 sec: 1.06x faster                                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 600 ms: 1.93x faster                                                     |
| async_tree_io_tg           | 1.18 sec                                               | 626 ms: 1.89x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 311 ms: 1.85x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 315 ms: 1.84x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.82x faster                                                     |
| async_tree_none            | 472 ms                                                 | 263 ms: 1.80x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 482 ms: 1.51x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 493 ms: 1.47x faster                                                     |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 72.6 ms: 1.17x faster                                                    |
| nbody          | 97.0 ms                                                | 96.0 ms: 1.01x faster                                                    |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                     |
| Geometric mean | (ref)                                                  | 1.06x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                     |
| regex_effbot   | 3.61 ms                                                | 3.19 ms: 1.13x faster                                                    |
| regex_dna      | 212 ms                                                 | 204 ms: 1.04x faster                                                     |
| regex_v8       | 23.1 ms                                                | 23.4 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                  | 1.08x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.03 sec: 1.15x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                 | 97.6 ms: 1.09x faster                                                    |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                     |
| xml_etree_generate   | 89.2 ms                                                | 85.4 ms: 1.04x faster                                                    |
| xml_etree_process    | 61.7 ms                                                | 60.2 ms: 1.02x faster                                                    |
| pickle_pure_python   | 324 us                                                 | 319 us: 1.02x faster                                                     |
| json_loads           | 28.5 us                                                | 30.3 us: 1.06x slower                                                    |
| json_dumps           | 10.4 ms                                                | 11.8 ms: 1.14x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.91 ms: 1.00x faster                                                    |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.28x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.7 ms: 1.06x faster                                                    |
| mako            | 11.9 ms                                                | 11.9 ms: 1.00x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.23 sec: 2.14x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 600 ms: 1.93x faster                                                     |
| async_tree_io_tg           | 1.18 sec                                               | 626 ms: 1.89x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 311 ms: 1.85x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 315 ms: 1.84x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.82x faster                                                     |
| async_tree_none            | 472 ms                                                 | 263 ms: 1.80x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 482 ms: 1.51x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 493 ms: 1.47x faster                                                     |
| deepcopy                   | 371 us                                                 | 262 us: 1.42x faster                                                     |
| deepcopy_memo              | 40.7 us                                                | 29.5 us: 1.38x faster                                                    |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.29x faster                                                    |
| go                         | 139 ms                                                 | 115 ms: 1.22x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                | 2.81 us: 1.19x faster                                                    |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                     |
| float                      | 84.7 ms                                                | 72.6 ms: 1.17x faster                                                    |
| tomli_loads                | 2.33 sec                                               | 2.03 sec: 1.15x faster                                                   |
| raytrace                   | 312 ms                                                 | 273 ms: 1.14x faster                                                     |
| dulwich_log                | 68.5 ms                                                | 60.1 ms: 1.14x faster                                                    |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.13x faster                                                     |
| regex_effbot               | 3.61 ms                                                | 3.19 ms: 1.13x faster                                                    |
| async_generators           | 463 ms                                                 | 410 ms: 1.13x faster                                                     |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                     |
| sympy_integrate            | 21.4 ms                                                | 19.1 ms: 1.12x faster                                                    |
| sympy_str                  | 300 ms                                                 | 268 ms: 1.12x faster                                                     |
| chaos                      | 67.0 ms                                                | 59.8 ms: 1.12x faster                                                    |
| scimark_monte_carlo        | 75.1 ms                                                | 67.7 ms: 1.11x faster                                                    |
| crypto_pyaes               | 81.9 ms                                                | 73.8 ms: 1.11x faster                                                    |
| spectral_norm              | 115 ms                                                 | 104 ms: 1.10x faster                                                     |
| pathlib                    | 19.3 ms                                                | 17.6 ms: 1.10x faster                                                    |
| xml_etree_iterparse        | 107 ms                                                 | 97.6 ms: 1.09x faster                                                    |
| deltablue                  | 3.72 ms                                                | 3.40 ms: 1.09x faster                                                    |
| pyflate                    | 482 ms                                                 | 448 ms: 1.08x faster                                                     |
| 2to3                       | 274 ms                                                 | 257 ms: 1.07x faster                                                     |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.07x faster                                                     |
| scimark_sor                | 129 ms                                                 | 121 ms: 1.07x faster                                                     |
| pprint_safe_repr           | 776 ms                                                 | 730 ms: 1.06x faster                                                     |
| docutils                   | 2.77 sec                                               | 2.61 sec: 1.06x faster                                                   |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                     |
| logging_simple             | 6.46 us                                                | 6.10 us: 1.06x faster                                                    |
| django_template            | 34.6 ms                                                | 32.7 ms: 1.06x faster                                                    |
| logging_format             | 7.23 us                                                | 6.85 us: 1.06x faster                                                    |
| richards                   | 45.8 ms                                                | 43.4 ms: 1.06x faster                                                    |
| generators                 | 31.2 ms                                                | 29.7 ms: 1.05x faster                                                    |
| xml_etree_generate         | 89.2 ms                                                | 85.4 ms: 1.04x faster                                                    |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.04x faster                                                   |
| sympy_expand               | 478 ms                                                 | 458 ms: 1.04x faster                                                     |
| richards_super             | 51.5 ms                                                | 49.6 ms: 1.04x faster                                                    |
| regex_dna                  | 212 ms                                                 | 204 ms: 1.04x faster                                                     |
| xml_etree_process          | 61.7 ms                                                | 60.2 ms: 1.02x faster                                                    |
| fannkuch                   | 417 ms                                                 | 407 ms: 1.02x faster                                                     |
| scimark_fft                | 382 ms                                                 | 374 ms: 1.02x faster                                                     |
| nqueens                    | 83.3 ms                                                | 81.5 ms: 1.02x faster                                                    |
| hexiom                     | 6.41 ms                                                | 6.29 ms: 1.02x faster                                                    |
| pickle_pure_python         | 324 us                                                 | 319 us: 1.02x faster                                                     |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                     |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.00 ms: 1.01x faster                                                    |
| nbody                      | 97.0 ms                                                | 96.0 ms: 1.01x faster                                                    |
| pycparser                  | 1.18 sec                                               | 1.17 sec: 1.01x faster                                                   |
| python_startup_no_site     | 6.94 ms                                                | 6.91 ms: 1.00x faster                                                    |
| mako                       | 11.9 ms                                                | 11.9 ms: 1.00x faster                                                    |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                     |
| regex_v8                   | 23.1 ms                                                | 23.4 ms: 1.01x slower                                                    |
| json                       | 5.26 ms                                                | 5.36 ms: 1.02x slower                                                    |
| bench_thread_pool          | 842 us                                                 | 886 us: 1.05x slower                                                     |
| coroutines                 | 23.2 ms                                                | 24.4 ms: 1.05x slower                                                    |
| json_loads                 | 28.5 us                                                | 30.3 us: 1.06x slower                                                    |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.06x slower                                                     |
| telco                      | 7.10 ms                                                | 8.03 ms: 1.13x slower                                                    |
| json_dumps                 | 10.4 ms                                                | 11.8 ms: 1.14x slower                                                    |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.28x slower                                                    |
| gc_traversal               | 3.79 ms                                                | 4.91 ms: 1.29x slower                                                    |
| create_gc_cycles           | 1.48 ms                                                | 2.56 ms: 1.73x slower                                                    |
| dask                       | 372 ms                                                 | 915 ms: 2.46x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 93.3 ms: 3.89x slower                                                    |
| logging_silent             | 104 ns                                                 | 481 ns: 4.60x slower                                                     |
| coverage                   | 72.7 ms                                                | 419 ms: 5.77x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                             |

Benchmark hidden because not significant (2): asyncio_websockets, sqlite_synth
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (24) of results/bm-20250508-3.15.0a0-60413da/bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.075x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.13x