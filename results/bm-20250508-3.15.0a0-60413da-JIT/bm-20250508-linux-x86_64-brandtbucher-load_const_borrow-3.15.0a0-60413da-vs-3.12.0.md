# Results vs. 3.12.0

- fork: brandtbucher
- ref: load_const_borrow
- machine: linux-x86_64
- commit hash: 60413da
- commit date: 2025-05-08
- overall geometric mean: 1.087x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 263 ms: 1.04x faster                                                     |
| docutils       | 2.77 sec                                               | 2.66 sec: 1.04x faster                                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 600 ms: 1.93x faster                                                     |
| async_tree_io_tg           | 1.18 sec                                               | 636 ms: 1.86x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 311 ms: 1.85x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.81x faster                                                     |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.80x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 480 ms: 1.51x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 487 ms: 1.49x faster                                                     |
| Geometric mean             | (ref)                                                  | 1.76x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 64.2 ms: 1.32x faster                                                    |
| nbody          | 97.0 ms                                                | 89.5 ms: 1.08x faster                                                    |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x slower                                                     |
| Geometric mean | (ref)                                                  | 1.13x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.01 ms: 1.20x faster                                                    |
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                     |
| regex_dna      | 212 ms                                                 | 197 ms: 1.08x faster                                                     |
| regex_v8       | 23.1 ms                                                | 22.7 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                  | 1.11x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.87 sec: 1.25x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 142 ms: 1.12x faster                                                     |
| unpickle_pure_python | 230 us                                                 | 205 us: 1.12x faster                                                     |
| xml_etree_generate   | 89.2 ms                                                | 80.4 ms: 1.11x faster                                                    |
| xml_etree_process    | 61.7 ms                                                | 56.0 ms: 1.10x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                 | 98.5 ms: 1.08x faster                                                    |
| pickle_pure_python   | 324 us                                                 | 329 us: 1.02x slower                                                     |
| json_loads           | 28.5 us                                                | 29.7 us: 1.04x slower                                                    |
| json_dumps           | 10.4 ms                                                | 11.9 ms: 1.14x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.96 ms: 1.00x slower                                                    |
| python_startup         | 9.55 ms                                                | 12.3 ms: 1.28x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                    |
| django_template | 34.6 ms                                                | 32.6 ms: 1.06x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.25 sec: 2.11x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 600 ms: 1.93x faster                                                     |
| async_tree_io_tg           | 1.18 sec                                               | 636 ms: 1.86x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 311 ms: 1.85x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.81x faster                                                     |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.80x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 480 ms: 1.51x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 487 ms: 1.49x faster                                                     |
| deepcopy                   | 371 us                                                 | 259 us: 1.43x faster                                                     |
| richards                   | 45.8 ms                                                | 34.2 ms: 1.34x faster                                                    |
| deepcopy_memo              | 40.7 us                                                | 30.4 us: 1.34x faster                                                    |
| richards_super             | 51.5 ms                                                | 38.6 ms: 1.34x faster                                                    |
| float                      | 84.7 ms                                                | 64.2 ms: 1.32x faster                                                    |
| tomli_loads                | 2.33 sec                                               | 1.87 sec: 1.25x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                | 2.73 us: 1.22x faster                                                    |
| comprehensions             | 21.8 us                                                | 17.9 us: 1.22x faster                                                    |
| deltablue                  | 3.72 ms                                                | 3.08 ms: 1.20x faster                                                    |
| regex_effbot               | 3.61 ms                                                | 3.01 ms: 1.20x faster                                                    |
| scimark_fft                | 382 ms                                                 | 320 ms: 1.19x faster                                                     |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                     |
| spectral_norm              | 115 ms                                                 | 99.3 ms: 1.16x faster                                                    |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.13x faster                                                     |
| raytrace                   | 312 ms                                                 | 276 ms: 1.13x faster                                                     |
| xml_etree_parse            | 159 ms                                                 | 142 ms: 1.12x faster                                                     |
| unpickle_pure_python       | 230 us                                                 | 205 us: 1.12x faster                                                     |
| scimark_monte_carlo        | 75.1 ms                                                | 67.3 ms: 1.12x faster                                                    |
| dulwich_log                | 68.5 ms                                                | 61.6 ms: 1.11x faster                                                    |
| go                         | 139 ms                                                 | 126 ms: 1.11x faster                                                     |
| pathlib                    | 19.3 ms                                                | 17.4 ms: 1.11x faster                                                    |
| xml_etree_generate         | 89.2 ms                                                | 80.4 ms: 1.11x faster                                                    |
| sympy_integrate            | 21.4 ms                                                | 19.4 ms: 1.10x faster                                                    |
| xml_etree_process          | 61.7 ms                                                | 56.0 ms: 1.10x faster                                                    |
| sympy_str                  | 300 ms                                                 | 273 ms: 1.10x faster                                                     |
| chaos                      | 67.0 ms                                                | 61.1 ms: 1.10x faster                                                    |
| async_generators           | 463 ms                                                 | 426 ms: 1.09x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 75.5 ms: 1.08x faster                                                    |
| nbody                      | 97.0 ms                                                | 89.5 ms: 1.08x faster                                                    |
| xml_etree_iterparse        | 107 ms                                                 | 98.5 ms: 1.08x faster                                                    |
| pyflate                    | 482 ms                                                 | 447 ms: 1.08x faster                                                     |
| regex_dna                  | 212 ms                                                 | 197 ms: 1.08x faster                                                     |
| mako                       | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                    |
| pprint_safe_repr           | 776 ms                                                 | 728 ms: 1.07x faster                                                     |
| scimark_sor                | 129 ms                                                 | 121 ms: 1.06x faster                                                     |
| django_template            | 34.6 ms                                                | 32.6 ms: 1.06x faster                                                    |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                     |
| 2to3                       | 274 ms                                                 | 263 ms: 1.04x faster                                                     |
| logging_format             | 7.23 us                                                | 6.93 us: 1.04x faster                                                    |
| logging_simple             | 6.46 us                                                | 6.20 us: 1.04x faster                                                    |
| docutils                   | 2.77 sec                                               | 2.66 sec: 1.04x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.52 sec: 1.03x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.92 ms: 1.03x faster                                                    |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.03x faster                                                   |
| regex_v8                   | 23.1 ms                                                | 22.7 ms: 1.02x faster                                                    |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                                    |
| fannkuch                   | 417 ms                                                 | 413 ms: 1.01x faster                                                     |
| sympy_expand               | 478 ms                                                 | 474 ms: 1.01x faster                                                     |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x slower                                                     |
| python_startup_no_site     | 6.94 ms                                                | 6.96 ms: 1.00x slower                                                    |
| generators                 | 31.2 ms                                                | 31.3 ms: 1.00x slower                                                    |
| pickle_pure_python         | 324 us                                                 | 329 us: 1.02x slower                                                     |
| nqueens                    | 83.3 ms                                                | 85.1 ms: 1.02x slower                                                    |
| json_loads                 | 28.5 us                                                | 29.7 us: 1.04x slower                                                    |
| hexiom                     | 6.41 ms                                                | 6.72 ms: 1.05x slower                                                    |
| typing_runtime_protocols   | 158 us                                                 | 170 us: 1.08x slower                                                     |
| bench_thread_pool          | 842 us                                                 | 907 us: 1.08x slower                                                     |
| coroutines                 | 23.2 ms                                                | 25.1 ms: 1.08x slower                                                    |
| telco                      | 7.10 ms                                                | 7.77 ms: 1.09x slower                                                    |
| json_dumps                 | 10.4 ms                                                | 11.9 ms: 1.14x slower                                                    |
| python_startup             | 9.55 ms                                                | 12.3 ms: 1.28x slower                                                    |
| gc_traversal               | 3.79 ms                                                | 4.94 ms: 1.30x slower                                                    |
| create_gc_cycles           | 1.48 ms                                                | 2.56 ms: 1.73x slower                                                    |
| dask                       | 372 ms                                                 | 928 ms: 2.50x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 93.7 ms: 3.90x slower                                                    |
| logging_silent             | 104 ns                                                 | 476 ns: 4.56x slower                                                     |
| coverage                   | 72.7 ms                                                | 430 ms: 5.92x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                             |

Benchmark hidden because not significant (3): scimark_lu, asyncio_websockets, json
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (24) of results/bm-20250508-3.15.0a0-60413da-JIT/bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.087x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.14x