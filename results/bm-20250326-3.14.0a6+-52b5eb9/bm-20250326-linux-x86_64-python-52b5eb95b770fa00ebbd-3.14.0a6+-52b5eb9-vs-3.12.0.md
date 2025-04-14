# Results vs. 3.12.0

- fork: python
- ref: 52b5eb95b770fa00ebbd
- machine: linux-x86_64
- commit hash: 52b5eb9
- commit date: 2025-03-26
- overall geometric mean: 1.110x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 258 ms: 1.06x faster                                                   |
| docutils       | 2.77 sec                                               | 2.63 sec: 1.05x faster                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 610 ms: 1.94x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 612 ms: 1.89x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 311 ms: 1.86x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 309 ms: 1.86x faster                                                   |
| async_tree_none            | 472 ms                                                 | 257 ms: 1.84x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 246 ms: 1.82x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 470 ms: 1.54x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 487 ms: 1.49x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.77x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.5 ms: 1.20x faster                                                  |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                   |
| nbody          | 97.0 ms                                                | 97.3 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.47 ms: 1.04x faster                                                  |
| regex_v8       | 23.1 ms                                                | 23.0 ms: 1.01x faster                                                  |
| regex_dna      | 212 ms                                                 | 224 ms: 1.06x slower                                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.97 sec: 1.18x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 142 ms: 1.12x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 99.0 ms: 1.08x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 218 us: 1.05x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 85.2 ms: 1.05x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 59.3 ms: 1.04x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 319 us: 1.01x faster                                                   |
| json_loads           | 28.5 us                                                | 30.0 us: 1.05x slower                                                  |
| json_dumps           | 10.4 ms                                                | 11.7 ms: 1.13x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.19 ms: 1.18x slower                                                  |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.0 ms: 1.08x faster                                                  |
| mako            | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 610 ms: 1.94x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 612 ms: 1.89x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 311 ms: 1.86x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 309 ms: 1.86x faster                                                   |
| async_tree_none            | 472 ms                                                 | 257 ms: 1.84x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 246 ms: 1.82x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 470 ms: 1.54x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 487 ms: 1.49x faster                                                   |
| deepcopy                   | 371 us                                                 | 259 us: 1.43x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 29.3 us: 1.39x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.9 us: 1.29x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                                  |
| float                      | 84.7 ms                                                | 70.5 ms: 1.20x faster                                                  |
| go                         | 139 ms                                                 | 117 ms: 1.19x faster                                                   |
| async_generators           | 463 ms                                                 | 389 ms: 1.19x faster                                                   |
| tomli_loads                | 2.33 sec                                               | 1.97 sec: 1.18x faster                                                 |
| dulwich_log                | 68.5 ms                                                | 58.1 ms: 1.18x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.16 ms: 1.18x faster                                                  |
| raytrace                   | 312 ms                                                 | 265 ms: 1.18x faster                                                   |
| logging_format             | 7.23 us                                                | 6.16 us: 1.17x faster                                                  |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                   |
| logging_simple             | 6.46 us                                                | 5.56 us: 1.16x faster                                                  |
| spectral_norm              | 115 ms                                                 | 99.0 ms: 1.16x faster                                                  |
| pathlib                    | 19.3 ms                                                | 16.7 ms: 1.16x faster                                                  |
| chaos                      | 67.0 ms                                                | 58.8 ms: 1.14x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.14x faster                                                   |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                                   |
| xml_etree_parse            | 159 ms                                                 | 142 ms: 1.12x faster                                                   |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.7 ms: 1.12x faster                                                  |
| sympy_str                  | 300 ms                                                 | 268 ms: 1.12x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 68.0 ms: 1.10x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 74.5 ms: 1.10x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 19.5 ms: 1.10x faster                                                  |
| generators                 | 31.2 ms                                                | 28.6 ms: 1.09x faster                                                  |
| pyflate                    | 482 ms                                                 | 442 ms: 1.09x faster                                                   |
| django_template            | 34.6 ms                                                | 32.0 ms: 1.08x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 99.0 ms: 1.08x faster                                                  |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.08x faster                                                   |
| scimark_fft                | 382 ms                                                 | 355 ms: 1.08x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.72 ms: 1.07x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 727 ms: 1.07x faster                                                   |
| 2to3                       | 274 ms                                                 | 258 ms: 1.06x faster                                                   |
| mdp                        | 2.63 sec                                               | 2.48 sec: 1.06x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.06x faster                                                 |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 218 us: 1.05x faster                                                   |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                   |
| docutils                   | 2.77 sec                                               | 2.63 sec: 1.05x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 85.2 ms: 1.05x faster                                                  |
| logging_silent             | 104 ns                                                 | 99.9 ns: 1.05x faster                                                  |
| sympy_expand               | 478 ms                                                 | 458 ms: 1.04x faster                                                   |
| regex_effbot               | 3.61 ms                                                | 3.47 ms: 1.04x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 59.3 ms: 1.04x faster                                                  |
| richards                   | 45.8 ms                                                | 44.5 ms: 1.03x faster                                                  |
| sqlite_synth               | 2.83 us                                                | 2.75 us: 1.03x faster                                                  |
| hexiom                     | 6.41 ms                                                | 6.25 ms: 1.03x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 319 us: 1.01x faster                                                   |
| richards_super             | 51.5 ms                                                | 51.0 ms: 1.01x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                   |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                   |
| nqueens                    | 83.3 ms                                                | 82.7 ms: 1.01x faster                                                  |
| regex_v8                   | 23.1 ms                                                | 23.0 ms: 1.01x faster                                                  |
| nbody                      | 97.0 ms                                                | 97.3 ms: 1.00x slower                                                  |
| json                       | 5.26 ms                                                | 5.32 ms: 1.01x slower                                                  |
| coroutines                 | 23.2 ms                                                | 23.5 ms: 1.01x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 161 us: 1.02x slower                                                   |
| bench_thread_pool          | 842 us                                                 | 870 us: 1.03x slower                                                   |
| json_loads                 | 28.5 us                                                | 30.0 us: 1.05x slower                                                  |
| regex_dna                  | 212 ms                                                 | 224 ms: 1.06x slower                                                   |
| telco                      | 7.10 ms                                                | 7.93 ms: 1.12x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 11.7 ms: 1.13x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 8.19 ms: 1.18x slower                                                  |
| coverage                   | 72.7 ms                                                | 91.9 ms: 1.26x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 4.84 ms: 1.28x slower                                                  |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.50 ms: 1.69x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 82.9 ms: 3.45x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                           |

Benchmark hidden because not significant (3): pycparser, fannkuch, asyncio_websockets
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250326-3.14.0a6+-52b5eb9/bm-20250326-linux-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.110x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.10x