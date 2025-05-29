# Results vs. 3.12.0

- fork: mdboom
- ref: early_tail_call_load
- machine: linux-x86_64
- commit hash: e9c43a0
- commit date: 2025-02-12
- overall geometric mean: 1.157x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 244 ms: 1.13x faster                                                   |
| docutils       | 2.77 sec                                               | 2.51 sec: 1.10x faster                                                 |
| Geometric mean | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 599 ms: 1.93x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 616 ms: 1.92x faster                                                   |
| async_tree_none            | 472 ms                                                 | 252 ms: 1.87x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 311 ms: 1.86x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 244 ms: 1.84x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 313 ms: 1.84x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 478 ms: 1.52x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 487 ms: 1.49x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.78x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 64.1 ms: 1.32x faster                                                  |
| nbody          | 97.0 ms                                                | 80.5 ms: 1.20x faster                                                  |
| pidigits       | 187 ms                                                 | 202 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                  | 1.14x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 119 ms: 1.25x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.13 ms: 1.16x faster                                                  |
| regex_dna      | 212 ms                                                 | 198 ms: 1.07x faster                                                   |
| regex_v8       | 23.1 ms                                                | 24.9 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.86 sec: 1.25x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 206 us: 1.12x faster                                                   |
| xml_etree_process    | 61.7 ms                                                | 56.9 ms: 1.09x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 299 us: 1.08x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 83.8 ms: 1.06x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.06x faster                                                   |
| json_loads           | 28.5 us                                                | 30.8 us: 1.08x slower                                                  |
| json_dumps           | 10.4 ms                                                | 12.5 ms: 1.20x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.95 ms: 1.00x slower                                                  |
| python_startup         | 9.55 ms                                                | 12.6 ms: 1.32x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.15x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 30.1 ms: 1.15x faster                                                  |
| mako            | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 599 ms: 1.93x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 616 ms: 1.92x faster                                                   |
| async_tree_none            | 472 ms                                                 | 252 ms: 1.87x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 311 ms: 1.86x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 244 ms: 1.84x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 313 ms: 1.84x faster                                                   |
| deepcopy                   | 371 us                                                 | 240 us: 1.54x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 478 ms: 1.52x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 487 ms: 1.49x faster                                                   |
| comprehensions             | 21.8 us                                                | 14.9 us: 1.46x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 28.2 us: 1.44x faster                                                  |
| scimark_fft                | 382 ms                                                 | 279 ms: 1.37x faster                                                   |
| spectral_norm              | 115 ms                                                 | 84.1 ms: 1.37x faster                                                  |
| pathlib                    | 19.3 ms                                                | 14.4 ms: 1.34x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.52 us: 1.33x faster                                                  |
| float                      | 84.7 ms                                                | 64.1 ms: 1.32x faster                                                  |
| deltablue                  | 3.72 ms                                                | 2.85 ms: 1.30x faster                                                  |
| go                         | 139 ms                                                 | 107 ms: 1.30x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 58.7 ms: 1.28x faster                                                  |
| chaos                      | 67.0 ms                                                | 52.7 ms: 1.27x faster                                                  |
| logging_silent             | 104 ns                                                 | 82.3 ns: 1.27x faster                                                  |
| raytrace                   | 312 ms                                                 | 249 ms: 1.26x faster                                                   |
| tomli_loads                | 2.33 sec                                               | 1.86 sec: 1.25x faster                                                 |
| regex_compile              | 148 ms                                                 | 119 ms: 1.25x faster                                                   |
| logging_format             | 7.23 us                                                | 5.83 us: 1.24x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.07 ms: 1.24x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 66.5 ms: 1.23x faster                                                  |
| sqlalchemy_imperative      | 18.7 ms                                                | 15.2 ms: 1.23x faster                                                  |
| async_generators           | 463 ms                                                 | 378 ms: 1.23x faster                                                   |
| pyflate                    | 482 ms                                                 | 394 ms: 1.22x faster                                                   |
| logging_simple             | 6.46 us                                                | 5.28 us: 1.22x faster                                                  |
| scimark_sor                | 129 ms                                                 | 106 ms: 1.22x faster                                                   |
| sympy_sum                  | 169 ms                                                 | 139 ms: 1.22x faster                                                   |
| sqlalchemy_declarative     | 147 ms                                                 | 121 ms: 1.21x faster                                                   |
| nbody                      | 97.0 ms                                                | 80.5 ms: 1.20x faster                                                  |
| sympy_str                  | 300 ms                                                 | 251 ms: 1.19x faster                                                   |
| sqlglot_parse              | 1.36 ms                                                | 1.14 ms: 1.19x faster                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.44 ms: 1.17x faster                                                  |
| richards                   | 45.8 ms                                                | 39.3 ms: 1.17x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.13 ms: 1.16x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 18.6 ms: 1.15x faster                                                  |
| django_template            | 34.6 ms                                                | 30.1 ms: 1.15x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 60.1 ms: 1.14x faster                                                  |
| generators                 | 31.2 ms                                                | 27.7 ms: 1.13x faster                                                  |
| 2to3                       | 274 ms                                                 | 244 ms: 1.13x faster                                                   |
| richards_super             | 51.5 ms                                                | 45.8 ms: 1.13x faster                                                  |
| hexiom                     | 6.41 ms                                                | 5.70 ms: 1.13x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 206 us: 1.12x faster                                                   |
| sympy_expand               | 478 ms                                                 | 428 ms: 1.12x faster                                                   |
| scimark_lu                 | 118 ms                                                 | 106 ms: 1.12x faster                                                   |
| nqueens                    | 83.3 ms                                                | 74.8 ms: 1.11x faster                                                  |
| coroutines                 | 23.2 ms                                                | 21.0 ms: 1.11x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.51 sec: 1.10x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 713 ms: 1.09x faster                                                   |
| fannkuch                   | 417 ms                                                 | 384 ms: 1.09x faster                                                   |
| xml_etree_process          | 61.7 ms                                                | 56.9 ms: 1.09x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 299 us: 1.08x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.45 sec: 1.08x faster                                                 |
| sqlglot_optimize           | 54.8 ms                                                | 50.8 ms: 1.08x faster                                                  |
| pycparser                  | 1.18 sec                                               | 1.09 sec: 1.08x faster                                                 |
| regex_dna                  | 212 ms                                                 | 198 ms: 1.07x faster                                                   |
| typing_runtime_protocols   | 158 us                                                 | 147 us: 1.07x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 83.8 ms: 1.06x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.06x faster                                                   |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                  |
| sqlite_synth               | 2.83 us                                                | 2.70 us: 1.05x faster                                                  |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                   |
| bench_thread_pool          | 842 us                                                 | 813 us: 1.04x faster                                                   |
| mdp                        | 2.63 sec                                               | 2.61 sec: 1.01x faster                                                 |
| python_startup_no_site     | 6.94 ms                                                | 6.95 ms: 1.00x slower                                                  |
| telco                      | 7.10 ms                                                | 7.18 ms: 1.01x slower                                                  |
| json                       | 5.26 ms                                                | 5.43 ms: 1.03x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 24.9 ms: 1.08x slower                                                  |
| pidigits                   | 187 ms                                                 | 202 ms: 1.08x slower                                                   |
| json_loads                 | 28.5 us                                                | 30.8 us: 1.08x slower                                                  |
| coverage                   | 72.7 ms                                                | 80.6 ms: 1.11x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 12.5 ms: 1.20x slower                                                  |
| python_startup             | 9.55 ms                                                | 12.6 ms: 1.32x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 5.04 ms: 1.33x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.54 ms: 1.72x slower                                                  |
| sqlglot_normalize          | 110 ms                                                 | 265 ms: 2.40x slower                                                   |
| bench_mp_pool              | 24.0 ms                                                | 79.0 ms: 3.29x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.14x faster                                                           |

Benchmark hidden because not significant (2): xml_etree_parse, asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250212-3.14.0a4+-e9c43a0-CLANG/bm-20250212-linux-x86_64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.157x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: 1.10x