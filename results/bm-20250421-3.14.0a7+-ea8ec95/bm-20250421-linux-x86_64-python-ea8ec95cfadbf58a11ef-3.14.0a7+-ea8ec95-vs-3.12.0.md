# Results vs. 3.12.0

- fork: python
- ref: ea8ec95cfadbf58a11ef
- machine: linux-x86_64
- commit hash: ea8ec95
- commit date: 2025-04-21
- overall geometric mean: 1.119x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 252 ms: 1.09x faster                                                   |
| docutils       | 2.77 sec                                               | 2.61 sec: 1.06x faster                                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 617 ms: 1.92x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 614 ms: 1.88x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                   |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 254 ms: 1.77x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 483 ms: 1.50x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 483 ms: 1.50x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.6 ms: 1.20x faster                                                  |
| nbody          | 97.0 ms                                                | 96.1 ms: 1.01x faster                                                  |
| pidigits       | 187 ms                                                 | 194 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.18x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.13 ms: 1.15x faster                                                  |
| regex_v8       | 23.1 ms                                                | 22.3 ms: 1.04x faster                                                  |
| regex_dna      | 212 ms                                                 | 205 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 98.7 ms: 1.08x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 85.7 ms: 1.04x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 314 us: 1.03x faster                                                   |
| xml_etree_process    | 61.7 ms                                                | 59.9 ms: 1.03x faster                                                  |
| json_loads           | 28.5 us                                                | 30.1 us: 1.06x slower                                                  |
| json_dumps           | 10.4 ms                                                | 11.7 ms: 1.12x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.20 ms: 1.18x slower                                                  |
| python_startup         | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.6 ms: 1.10x faster                                                  |
| mako            | 11.9 ms                                                | 11.8 ms: 1.01x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.22 sec: 2.16x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 617 ms: 1.92x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 614 ms: 1.88x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                   |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 254 ms: 1.77x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 483 ms: 1.50x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 483 ms: 1.50x faster                                                   |
| deepcopy                   | 371 us                                                 | 251 us: 1.48x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 28.5 us: 1.43x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.9 us: 1.29x faster                                                  |
| go                         | 139 ms                                                 | 112 ms: 1.25x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                                  |
| float                      | 84.7 ms                                                | 70.6 ms: 1.20x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                 |
| raytrace                   | 312 ms                                                 | 263 ms: 1.19x faster                                                   |
| chaos                      | 67.0 ms                                                | 56.7 ms: 1.18x faster                                                  |
| regex_compile              | 148 ms                                                 | 126 ms: 1.18x faster                                                   |
| logging_format             | 7.23 us                                                | 6.18 us: 1.17x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.52 us: 1.17x faster                                                  |
| async_generators           | 463 ms                                                 | 401 ms: 1.16x faster                                                   |
| regex_effbot               | 3.61 ms                                                | 3.13 ms: 1.15x faster                                                  |
| pathlib                    | 19.3 ms                                                | 16.8 ms: 1.15x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 59.8 ms: 1.15x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                                   |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 66.2 ms: 1.14x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 19.0 ms: 1.13x faster                                                  |
| sympy_str                  | 300 ms                                                 | 267 ms: 1.12x faster                                                   |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 73.5 ms: 1.11x faster                                                  |
| django_template            | 34.6 ms                                                | 31.6 ms: 1.10x faster                                                  |
| spectral_norm              | 115 ms                                                 | 105 ms: 1.09x faster                                                   |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.1 ms: 1.09x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.41 ms: 1.09x faster                                                  |
| 2to3                       | 274 ms                                                 | 252 ms: 1.09x faster                                                   |
| pprint_safe_repr           | 776 ms                                                 | 714 ms: 1.09x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 98.7 ms: 1.08x faster                                                  |
| pyflate                    | 482 ms                                                 | 446 ms: 1.08x faster                                                   |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.08x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.46 sec: 1.08x faster                                                 |
| logging_silent             | 104 ns                                                 | 97.2 ns: 1.07x faster                                                  |
| generators                 | 31.2 ms                                                | 29.1 ms: 1.07x faster                                                  |
| scimark_fft                | 382 ms                                                 | 360 ms: 1.06x faster                                                   |
| docutils                   | 2.77 sec                                               | 2.61 sec: 1.06x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                   |
| sympy_expand               | 478 ms                                                 | 455 ms: 1.05x faster                                                   |
| richards                   | 45.8 ms                                                | 43.7 ms: 1.05x faster                                                  |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 85.7 ms: 1.04x faster                                                  |
| regex_v8                   | 23.1 ms                                                | 22.3 ms: 1.04x faster                                                  |
| regex_dna                  | 212 ms                                                 | 205 ms: 1.03x faster                                                   |
| nqueens                    | 83.3 ms                                                | 80.8 ms: 1.03x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 314 us: 1.03x faster                                                   |
| richards_super             | 51.5 ms                                                | 50.0 ms: 1.03x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 59.9 ms: 1.03x faster                                                  |
| hexiom                     | 6.41 ms                                                | 6.23 ms: 1.03x faster                                                  |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                 |
| mako                       | 11.9 ms                                                | 11.8 ms: 1.01x faster                                                  |
| nbody                      | 97.0 ms                                                | 96.1 ms: 1.01x faster                                                  |
| sqlite_synth               | 2.83 us                                                | 2.81 us: 1.01x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 119 ms: 1.00x slower                                                   |
| fannkuch                   | 417 ms                                                 | 420 ms: 1.01x slower                                                   |
| pidigits                   | 187 ms                                                 | 194 ms: 1.04x slower                                                   |
| json                       | 5.26 ms                                                | 5.49 ms: 1.04x slower                                                  |
| coroutines                 | 23.2 ms                                                | 24.3 ms: 1.05x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 882 us: 1.05x slower                                                   |
| json_loads                 | 28.5 us                                                | 30.1 us: 1.06x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 169 us: 1.07x slower                                                   |
| telco                      | 7.10 ms                                                | 7.91 ms: 1.11x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 11.7 ms: 1.12x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 8.20 ms: 1.18x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 4.78 ms: 1.26x slower                                                  |
| coverage                   | 72.7 ms                                                | 93.4 ms: 1.28x slower                                                  |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.48 ms: 1.68x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 81.9 ms: 3.41x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                           |

Benchmark hidden because not significant (2): scimark_sparse_mat_mult, asyncio_websockets
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250421-3.14.0a7+-ea8ec95/bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.119x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.11x