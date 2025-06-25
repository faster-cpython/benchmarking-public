# Results vs. 3.12.0

- fork: python
- ref: fea5ccc55d8486300beb
- machine: linux-x86_64
- commit hash: fea5ccc
- commit date: 2025-06-24
- overall geometric mean: 1.130x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250624-linux-x86_64-python-fea5ccc55d8486300beb-3.15.0a0-fea5ccc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 260 ms: 1.06x faster                                                  |
| docutils       | 2.77 sec                                               | 2.63 sec: 1.05x faster                                                |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250624-linux-x86_64-python-fea5ccc55d8486300beb-3.15.0a0-fea5ccc |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 616 ms: 1.92x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 603 ms: 1.92x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                  |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.80x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 492 ms: 1.48x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 502 ms: 1.45x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250624-linux-x86_64-python-fea5ccc55d8486300beb-3.15.0a0-fea5ccc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 66.2 ms: 1.28x faster                                                 |
| pidigits       | 187 ms                                                 | 188 ms: 1.01x slower                                                  |
| nbody          | 97.0 ms                                                | 97.5 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250624-linux-x86_64-python-fea5ccc55d8486300beb-3.15.0a0-fea5ccc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.17 ms: 1.14x faster                                                 |
| regex_dna      | 212 ms                                                 | 200 ms: 1.06x faster                                                  |
| regex_v8       | 23.1 ms                                                | 22.1 ms: 1.05x faster                                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250624-linux-x86_64-python-fea5ccc55d8486300beb-3.15.0a0-fea5ccc |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.82 sec: 1.28x faster                                                |
| unpickle_pure_python | 230 us                                                 | 202 us: 1.14x faster                                                  |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 80.3 ms: 1.11x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 56.2 ms: 1.10x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 98.7 ms: 1.08x faster                                                 |
| json_loads           | 28.5 us                                                | 28.1 us: 1.01x faster                                                 |
| json_dumps           | 10.4 ms                                                | 11.1 ms: 1.07x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250624-linux-x86_64-python-fea5ccc55d8486300beb-3.15.0a0-fea5ccc |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.95 ms: 1.00x slower                                                 |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.28x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250624-linux-x86_64-python-fea5ccc55d8486300beb-3.15.0a0-fea5ccc |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.0 ms: 1.09x faster                                                 |
| django_template | 34.6 ms                                                | 32.6 ms: 1.06x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250624-linux-x86_64-python-fea5ccc55d8486300beb-3.15.0a0-fea5ccc |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.24 sec: 2.12x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 616 ms: 1.92x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 603 ms: 1.92x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                  |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.80x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 492 ms: 1.48x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 502 ms: 1.45x faster                                                  |
| deepcopy                   | 371 us                                                 | 260 us: 1.43x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 29.3 us: 1.39x faster                                                 |
| richards                   | 45.8 ms                                                | 33.2 ms: 1.38x faster                                                 |
| richards_super             | 51.5 ms                                                | 39.2 ms: 1.31x faster                                                 |
| float                      | 84.7 ms                                                | 66.2 ms: 1.28x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 1.82 sec: 1.28x faster                                                |
| comprehensions             | 21.8 us                                                | 17.2 us: 1.26x faster                                                 |
| scimark_fft                | 382 ms                                                 | 314 ms: 1.22x faster                                                  |
| spectral_norm              | 115 ms                                                 | 94.8 ms: 1.21x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.78 us: 1.20x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.10 ms: 1.20x faster                                                 |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                  |
| go                         | 139 ms                                                 | 121 ms: 1.16x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 59.4 ms: 1.15x faster                                                 |
| pyflate                    | 482 ms                                                 | 420 ms: 1.15x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 202 us: 1.14x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 66.0 ms: 1.14x faster                                                 |
| pathlib                    | 19.3 ms                                                | 17.0 ms: 1.14x faster                                                 |
| regex_effbot               | 3.61 ms                                                | 3.17 ms: 1.14x faster                                                 |
| raytrace                   | 312 ms                                                 | 275 ms: 1.13x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.13x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 80.3 ms: 1.11x faster                                                 |
| sympy_integrate            | 21.4 ms                                                | 19.3 ms: 1.11x faster                                                 |
| sympy_str                  | 300 ms                                                 | 272 ms: 1.10x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 56.2 ms: 1.10x faster                                                 |
| chaos                      | 67.0 ms                                                | 61.6 ms: 1.09x faster                                                 |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.09x faster                                                  |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.09x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 98.7 ms: 1.08x faster                                                 |
| async_generators           | 463 ms                                                 | 434 ms: 1.07x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 76.8 ms: 1.07x faster                                                 |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                  |
| django_template            | 34.6 ms                                                | 32.6 ms: 1.06x faster                                                 |
| regex_dna                  | 212 ms                                                 | 200 ms: 1.06x faster                                                  |
| logging_format             | 7.23 us                                                | 6.83 us: 1.06x faster                                                 |
| 2to3                       | 274 ms                                                 | 260 ms: 1.06x faster                                                  |
| pycparser                  | 1.18 sec                                               | 1.12 sec: 1.05x faster                                                |
| docutils                   | 2.77 sec                                               | 2.63 sec: 1.05x faster                                                |
| logging_simple             | 6.46 us                                                | 6.16 us: 1.05x faster                                                 |
| regex_v8                   | 23.1 ms                                                | 22.1 ms: 1.05x faster                                                 |
| fannkuch                   | 417 ms                                                 | 403 ms: 1.03x faster                                                  |
| generators                 | 31.2 ms                                                | 30.3 ms: 1.03x faster                                                 |
| sympy_expand               | 478 ms                                                 | 470 ms: 1.02x faster                                                  |
| json_loads                 | 28.5 us                                                | 28.1 us: 1.01x faster                                                 |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                                 |
| python_startup_no_site     | 6.94 ms                                                | 6.95 ms: 1.00x slower                                                 |
| pidigits                   | 187 ms                                                 | 188 ms: 1.01x slower                                                  |
| nbody                      | 97.0 ms                                                | 97.5 ms: 1.01x slower                                                 |
| nqueens                    | 83.3 ms                                                | 83.9 ms: 1.01x slower                                                 |
| hexiom                     | 6.41 ms                                                | 6.49 ms: 1.01x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                                  |
| pprint_safe_repr           | 776 ms                                                 | 822 ms: 1.06x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 11.1 ms: 1.07x slower                                                 |
| coroutines                 | 23.2 ms                                                | 24.9 ms: 1.08x slower                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.70 sec: 1.08x slower                                                |
| telco                      | 7.10 ms                                                | 7.73 ms: 1.09x slower                                                 |
| coverage                   | 72.7 ms                                                | 87.5 ms: 1.20x slower                                                 |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.28x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 4.93 ms: 1.30x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 2.59 ms: 1.75x slower                                                 |
| logging_silent             | 104 ns                                                 | 479 ns: 4.59x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.11x faster                                                          |

Benchmark hidden because not significant (5): scimark_sparse_mat_mult, pickle_pure_python, scimark_lu, asyncio_websockets, json
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250624-3.15.0a0-fea5ccc-JIT/bm-20250624-linux-x86_64-python-fea5ccc55d8486300beb-3.15.0a0-fea5ccc.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.130x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.15x