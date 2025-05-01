# Results vs. 3.12.0

- fork: python
- ref: feac343d1aeef9edce91
- machine: linux-x86_64
- commit hash: feac343
- commit date: 2025-05-01
- overall geometric mean: 1.110x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250501-linux-x86_64-python-feac343d1aeef9edce91-3.14.0a7+-feac343 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 255 ms: 1.08x faster                                                   |
| docutils       | 2.77 sec                                               | 2.62 sec: 1.05x faster                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250501-linux-x86_64-python-feac343d1aeef9edce91-3.14.0a7+-feac343 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 594 ms: 1.95x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 611 ms: 1.93x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 306 ms: 1.88x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                                   |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.80x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 491 ms: 1.48x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 498 ms: 1.46x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.76x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250501-linux-x86_64-python-feac343d1aeef9edce91-3.14.0a7+-feac343 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 71.1 ms: 1.19x faster                                                  |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                   |
| nbody          | 97.0 ms                                                | 98.0 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250501-linux-x86_64-python-feac343d1aeef9edce91-3.14.0a7+-feac343 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.32 ms: 1.09x faster                                                  |
| regex_dna      | 212 ms                                                 | 206 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250501-linux-x86_64-python-feac343d1aeef9edce91-3.14.0a7+-feac343 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.02 sec: 1.15x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 99.2 ms: 1.08x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 220 us: 1.05x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 86.1 ms: 1.04x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 60.2 ms: 1.03x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 320 us: 1.01x faster                                                   |
| json_loads           | 28.5 us                                                | 30.5 us: 1.07x slower                                                  |
| json_dumps           | 10.4 ms                                                | 12.0 ms: 1.15x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250501-linux-x86_64-python-feac343d1aeef9edce91-3.14.0a7+-feac343 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.91 ms: 1.00x faster                                                  |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250501-linux-x86_64-python-feac343d1aeef9edce91-3.14.0a7+-feac343 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.4 ms: 1.07x faster                                                  |
| mako            | 11.9 ms                                                | 11.7 ms: 1.02x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250501-linux-x86_64-python-feac343d1aeef9edce91-3.14.0a7+-feac343 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.24 sec: 2.11x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 594 ms: 1.95x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 611 ms: 1.93x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 306 ms: 1.88x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                                   |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.80x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 491 ms: 1.48x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 498 ms: 1.46x faster                                                   |
| deepcopy                   | 371 us                                                 | 257 us: 1.44x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 28.8 us: 1.42x faster                                                  |
| comprehensions             | 21.8 us                                                | 17.1 us: 1.28x faster                                                  |
| go                         | 139 ms                                                 | 113 ms: 1.24x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                | 2.72 us: 1.23x faster                                                  |
| float                      | 84.7 ms                                                | 71.1 ms: 1.19x faster                                                  |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                   |
| logging_simple             | 6.46 us                                                | 5.57 us: 1.16x faster                                                  |
| logging_format             | 7.23 us                                                | 6.26 us: 1.15x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 2.02 sec: 1.15x faster                                                 |
| raytrace                   | 312 ms                                                 | 272 ms: 1.15x faster                                                   |
| dulwich_log                | 68.5 ms                                                | 60.1 ms: 1.14x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                   |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.13x faster                                                   |
| async_generators           | 463 ms                                                 | 411 ms: 1.13x faster                                                   |
| chaos                      | 67.0 ms                                                | 59.6 ms: 1.12x faster                                                  |
| sympy_str                  | 300 ms                                                 | 268 ms: 1.12x faster                                                   |
| sympy_integrate            | 21.4 ms                                                | 19.2 ms: 1.12x faster                                                  |
| pathlib                    | 19.3 ms                                                | 17.4 ms: 1.12x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 67.9 ms: 1.11x faster                                                  |
| sqlalchemy_declarative     | 147 ms                                                 | 133 ms: 1.11x faster                                                   |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.1 ms: 1.09x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.32 ms: 1.09x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 75.9 ms: 1.08x faster                                                  |
| 2to3                       | 274 ms                                                 | 255 ms: 1.08x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 99.2 ms: 1.08x faster                                                  |
| generators                 | 31.2 ms                                                | 29.0 ms: 1.08x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.45 ms: 1.08x faster                                                  |
| pyflate                    | 482 ms                                                 | 451 ms: 1.07x faster                                                   |
| django_template            | 34.6 ms                                                | 32.4 ms: 1.07x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 729 ms: 1.06x faster                                                   |
| scimark_sor                | 129 ms                                                 | 122 ms: 1.06x faster                                                   |
| logging_silent             | 104 ns                                                 | 98.7 ns: 1.06x faster                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.06x faster                                                 |
| docutils                   | 2.77 sec                                               | 2.62 sec: 1.05x faster                                                 |
| spectral_norm              | 115 ms                                                 | 109 ms: 1.05x faster                                                   |
| richards                   | 45.8 ms                                                | 43.7 ms: 1.05x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 220 us: 1.05x faster                                                   |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                   |
| sympy_expand               | 478 ms                                                 | 458 ms: 1.04x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 86.1 ms: 1.04x faster                                                  |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.03x faster                                                 |
| richards_super             | 51.5 ms                                                | 49.8 ms: 1.03x faster                                                  |
| regex_dna                  | 212 ms                                                 | 206 ms: 1.03x faster                                                   |
| xml_etree_process          | 61.7 ms                                                | 60.2 ms: 1.03x faster                                                  |
| hexiom                     | 6.41 ms                                                | 6.31 ms: 1.02x faster                                                  |
| mako                       | 11.9 ms                                                | 11.7 ms: 1.02x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 320 us: 1.01x faster                                                   |
| nqueens                    | 83.3 ms                                                | 82.3 ms: 1.01x faster                                                  |
| scimark_fft                | 382 ms                                                 | 378 ms: 1.01x faster                                                   |
| python_startup_no_site     | 6.94 ms                                                | 6.91 ms: 1.00x faster                                                  |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                   |
| fannkuch                   | 417 ms                                                 | 421 ms: 1.01x slower                                                   |
| nbody                      | 97.0 ms                                                | 98.0 ms: 1.01x slower                                                  |
| sqlite_synth               | 2.83 us                                                | 2.87 us: 1.01x slower                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.18 ms: 1.02x slower                                                  |
| json                       | 5.26 ms                                                | 5.52 ms: 1.05x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 892 us: 1.06x slower                                                   |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.07x slower                                                   |
| json_loads                 | 28.5 us                                                | 30.5 us: 1.07x slower                                                  |
| coroutines                 | 23.2 ms                                                | 25.3 ms: 1.09x slower                                                  |
| telco                      | 7.10 ms                                                | 7.93 ms: 1.12x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 12.0 ms: 1.15x slower                                                  |
| coverage                   | 72.7 ms                                                | 93.3 ms: 1.28x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 4.89 ms: 1.29x slower                                                  |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.48 ms: 1.68x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 82.6 ms: 3.44x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                           |

Benchmark hidden because not significant (3): regex_v8, scimark_lu, asyncio_websockets
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250501-3.14.0a7+-feac343/bm-20250501-linux-x86_64-python-feac343d1aeef9edce91-3.14.0a7+-feac343.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.110x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.11x