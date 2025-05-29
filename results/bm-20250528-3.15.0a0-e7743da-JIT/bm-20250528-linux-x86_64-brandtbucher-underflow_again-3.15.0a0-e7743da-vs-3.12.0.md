# Results vs. 3.12.0

- fork: brandtbucher
- ref: underflow_again
- machine: linux-x86_64
- commit hash: e7743da
- commit date: 2025-05-28
- overall geometric mean: 1.623x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250528-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-e7743da |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 260 ms: 1.05x faster                                                   |
| docutils       | 2.77 sec                                               | 1.02 sec: 2.72x faster                                                 |
| Geometric mean | (ref)                                                  | 1.69x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250528-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-e7743da |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 608 ms: 1.90x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 634 ms: 1.86x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.82x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 320 ms: 1.80x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.77x faster                                                   |
| async_tree_none            | 472 ms                                                 | 268 ms: 1.76x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 501 ms: 1.45x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 507 ms: 1.43x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.72x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250528-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-e7743da |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 64.6 ms: 1.31x faster                                                  |
| nbody          | 97.0 ms                                                | 89.0 ms: 1.09x faster                                                  |
| pidigits       | 187 ms                                                 | 191 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250528-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-e7743da |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.08 ms: 1.17x faster                                                  |
| regex_dna      | 212 ms                                                 | 189 ms: 1.12x faster                                                   |
| regex_v8       | 23.1 ms                                                | 22.0 ms: 1.05x faster                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250528-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-e7743da |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 200 us: 1.15x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 97.5 ms: 1.10x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 82.0 ms: 1.09x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 57.0 ms: 1.08x faster                                                  |
| json_loads           | 28.5 us                                                | 29.9 us: 1.05x slower                                                  |
| json_dumps           | 10.4 ms                                                | 11.1 ms: 1.07x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                           |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250528-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-e7743da |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.95 ms: 1.00x slower                                                  |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.28x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250528-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-e7743da |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.6 ms: 1.12x faster                                                  |
| django_template | 34.6 ms                                                | 32.6 ms: 1.06x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250528-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-e7743da |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pprint_pformat             | 1.57 sec                                               | 1.45 us: 1080340.06x faster                                            |
| pprint_safe_repr           | 776 ms                                                 | 861 ns: 901015.42x faster                                              |
| docutils                   | 2.77 sec                                               | 1.02 sec: 2.72x faster                                                 |
| mdp                        | 2.63 sec                                               | 1.24 sec: 2.12x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 608 ms: 1.90x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 634 ms: 1.86x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.82x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 320 ms: 1.80x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.77x faster                                                   |
| async_tree_none            | 472 ms                                                 | 268 ms: 1.76x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 501 ms: 1.45x faster                                                   |
| deepcopy                   | 371 us                                                 | 259 us: 1.43x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 507 ms: 1.43x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 29.6 us: 1.37x faster                                                  |
| float                      | 84.7 ms                                                | 64.6 ms: 1.31x faster                                                  |
| richards                   | 45.8 ms                                                | 35.7 ms: 1.28x faster                                                  |
| comprehensions             | 21.8 us                                                | 17.1 us: 1.27x faster                                                  |
| richards_super             | 51.5 ms                                                | 41.4 ms: 1.24x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.78 us: 1.20x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.12 ms: 1.19x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                 |
| regex_effbot               | 3.61 ms                                                | 3.08 ms: 1.17x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 200 us: 1.15x faster                                                   |
| scimark_fft                | 382 ms                                                 | 336 ms: 1.14x faster                                                   |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                   |
| raytrace                   | 312 ms                                                 | 277 ms: 1.13x faster                                                   |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.13x faster                                                   |
| mako                       | 11.9 ms                                                | 10.6 ms: 1.12x faster                                                  |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.12x faster                                                   |
| regex_dna                  | 212 ms                                                 | 189 ms: 1.12x faster                                                   |
| pathlib                    | 19.3 ms                                                | 17.3 ms: 1.12x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 19.4 ms: 1.11x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 62.0 ms: 1.11x faster                                                  |
| sympy_str                  | 300 ms                                                 | 271 ms: 1.10x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 74.5 ms: 1.10x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 68.4 ms: 1.10x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 97.5 ms: 1.10x faster                                                  |
| pyflate                    | 482 ms                                                 | 441 ms: 1.10x faster                                                   |
| nbody                      | 97.0 ms                                                | 89.0 ms: 1.09x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 82.0 ms: 1.09x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 57.0 ms: 1.08x faster                                                  |
| async_generators           | 463 ms                                                 | 428 ms: 1.08x faster                                                   |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                                   |
| chaos                      | 67.0 ms                                                | 62.7 ms: 1.07x faster                                                  |
| scimark_sor                | 129 ms                                                 | 122 ms: 1.06x faster                                                   |
| django_template            | 34.6 ms                                                | 32.6 ms: 1.06x faster                                                  |
| 2to3                       | 274 ms                                                 | 260 ms: 1.05x faster                                                   |
| regex_v8                   | 23.1 ms                                                | 22.0 ms: 1.05x faster                                                  |
| generators                 | 31.2 ms                                                | 29.9 ms: 1.05x faster                                                  |
| logging_format             | 7.23 us                                                | 6.98 us: 1.04x faster                                                  |
| logging_simple             | 6.46 us                                                | 6.24 us: 1.03x faster                                                  |
| go                         | 139 ms                                                 | 135 ms: 1.03x faster                                                   |
| sympy_expand               | 478 ms                                                 | 466 ms: 1.03x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.95 ms: 1.02x faster                                                  |
| fannkuch                   | 417 ms                                                 | 412 ms: 1.01x faster                                                   |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                   |
| python_startup_no_site     | 6.94 ms                                                | 6.95 ms: 1.00x slower                                                  |
| hexiom                     | 6.41 ms                                                | 6.47 ms: 1.01x slower                                                  |
| nqueens                    | 83.3 ms                                                | 84.3 ms: 1.01x slower                                                  |
| pidigits                   | 187 ms                                                 | 191 ms: 1.02x slower                                                   |
| json_loads                 | 28.5 us                                                | 29.9 us: 1.05x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.06x slower                                                   |
| json_dumps                 | 10.4 ms                                                | 11.1 ms: 1.07x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 897 us: 1.07x slower                                                   |
| telco                      | 7.10 ms                                                | 7.91 ms: 1.11x slower                                                  |
| coroutines                 | 23.2 ms                                                | 26.0 ms: 1.12x slower                                                  |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.28x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 5.11 ms: 1.35x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.59 ms: 1.75x slower                                                  |
| dask                       | 372 ms                                                 | 927 ms: 2.49x slower                                                   |
| bench_mp_pool              | 24.0 ms                                                | 92.9 ms: 3.87x slower                                                  |
| logging_silent             | 104 ns                                                 | 475 ns: 4.55x slower                                                   |
| coverage                   | 72.7 ms                                                | 426 ms: 5.86x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.50x faster                                                           |

Benchmark hidden because not significant (4): pycparser, json, asyncio_websockets, pickle_pure_python
Ignored benchmarks (20) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, regex_compile, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (24) of results/bm-20250528-3.15.0a0-e7743da-JIT/bm-20250528-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-e7743da.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.623x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.14x