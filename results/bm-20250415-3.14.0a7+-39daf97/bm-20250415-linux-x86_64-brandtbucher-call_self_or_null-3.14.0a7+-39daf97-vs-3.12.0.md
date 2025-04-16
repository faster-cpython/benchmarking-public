# Results vs. 3.12.0

- fork: brandtbucher
- ref: call_self_or_null
- machine: linux-x86_64
- commit hash: 39daf97
- commit date: 2025-04-15
- overall geometric mean: 1.134x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250415-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-39daf97 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 249 ms: 1.10x faster                                                      |
| docutils       | 2.77 sec                                               | 2.56 sec: 1.08x faster                                                    |
| Geometric mean | (ref)                                                  | 1.09x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250415-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-39daf97 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 621 ms: 1.91x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 621 ms: 1.86x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 316 ms: 1.83x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 321 ms: 1.79x faster                                                      |
| async_tree_none            | 472 ms                                                 | 264 ms: 1.79x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 254 ms: 1.77x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 482 ms: 1.50x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 485 ms: 1.50x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250415-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-39daf97 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 72.7 ms: 1.16x faster                                                     |
| nbody          | 97.0 ms                                                | 88.4 ms: 1.10x faster                                                     |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.09x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250415-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-39daf97 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 125 ms: 1.18x faster                                                      |
| regex_effbot   | 3.61 ms                                                | 3.19 ms: 1.13x faster                                                     |
| regex_dna      | 212 ms                                                 | 207 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.08x faster                                                              |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250415-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-39daf97 |
|---------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads         | 2.33 sec                                               | 1.95 sec: 1.20x faster                                                    |
| xml_etree_parse     | 159 ms                                                 | 142 ms: 1.13x faster                                                      |
| xml_etree_iterparse | 107 ms                                                 | 98.1 ms: 1.09x faster                                                     |
| xml_etree_generate  | 89.2 ms                                                | 82.9 ms: 1.07x faster                                                     |
| xml_etree_process   | 61.7 ms                                                | 57.8 ms: 1.07x faster                                                     |
| pickle_pure_python  | 324 us                                                 | 318 us: 1.02x faster                                                      |
| json_loads          | 28.5 us                                                | 29.8 us: 1.05x slower                                                     |
| json_dumps          | 10.4 ms                                                | 11.4 ms: 1.10x slower                                                     |
| Geometric mean      | (ref)                                                  | 1.05x faster                                                              |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250415-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-39daf97 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.18 ms: 1.18x slower                                                     |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250415-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-39daf97 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.8 ms: 1.10x faster                                                     |
| django_template | 34.6 ms                                                | 31.9 ms: 1.08x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250415-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-39daf97 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.21 sec: 2.18x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 621 ms: 1.91x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 621 ms: 1.86x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 316 ms: 1.83x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 321 ms: 1.79x faster                                                      |
| async_tree_none            | 472 ms                                                 | 264 ms: 1.79x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 254 ms: 1.77x faster                                                      |
| deepcopy                   | 371 us                                                 | 244 us: 1.52x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 482 ms: 1.50x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 485 ms: 1.50x faster                                                      |
| deepcopy_memo              | 40.7 us                                                | 28.1 us: 1.45x faster                                                     |
| comprehensions             | 21.8 us                                                | 16.4 us: 1.33x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                | 2.59 us: 1.29x faster                                                     |
| go                         | 139 ms                                                 | 111 ms: 1.26x faster                                                      |
| tomli_loads                | 2.33 sec                                               | 1.95 sec: 1.20x faster                                                    |
| logging_format             | 7.23 us                                                | 6.05 us: 1.20x faster                                                     |
| regex_compile              | 148 ms                                                 | 125 ms: 1.18x faster                                                      |
| spectral_norm              | 115 ms                                                 | 97.8 ms: 1.18x faster                                                     |
| logging_simple             | 6.46 us                                                | 5.54 us: 1.17x faster                                                     |
| float                      | 84.7 ms                                                | 72.7 ms: 1.16x faster                                                     |
| scimark_monte_carlo        | 75.1 ms                                                | 64.9 ms: 1.16x faster                                                     |
| async_generators           | 463 ms                                                 | 400 ms: 1.16x faster                                                      |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                                      |
| chaos                      | 67.0 ms                                                | 58.3 ms: 1.15x faster                                                     |
| dulwich_log                | 68.5 ms                                                | 59.7 ms: 1.15x faster                                                     |
| pathlib                    | 19.3 ms                                                | 16.9 ms: 1.15x faster                                                     |
| scimark_fft                | 382 ms                                                 | 335 ms: 1.14x faster                                                      |
| sympy_str                  | 300 ms                                                 | 265 ms: 1.13x faster                                                      |
| regex_effbot               | 3.61 ms                                                | 3.19 ms: 1.13x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 72.6 ms: 1.13x faster                                                     |
| xml_etree_parse            | 159 ms                                                 | 142 ms: 1.13x faster                                                      |
| sqlalchemy_declarative     | 147 ms                                                 | 132 ms: 1.12x faster                                                      |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.8 ms: 1.12x faster                                                     |
| sympy_integrate            | 21.4 ms                                                | 19.3 ms: 1.11x faster                                                     |
| deltablue                  | 3.72 ms                                                | 3.35 ms: 1.11x faster                                                     |
| mako                       | 11.9 ms                                                | 10.8 ms: 1.10x faster                                                     |
| raytrace                   | 312 ms                                                 | 283 ms: 1.10x faster                                                      |
| 2to3                       | 274 ms                                                 | 249 ms: 1.10x faster                                                      |
| richards                   | 45.8 ms                                                | 41.7 ms: 1.10x faster                                                     |
| nbody                      | 97.0 ms                                                | 88.4 ms: 1.10x faster                                                     |
| generators                 | 31.2 ms                                                | 28.5 ms: 1.10x faster                                                     |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.10x faster                                                      |
| logging_silent             | 104 ns                                                 | 95.8 ns: 1.09x faster                                                     |
| pyflate                    | 482 ms                                                 | 442 ms: 1.09x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                 | 98.1 ms: 1.09x faster                                                     |
| django_template            | 34.6 ms                                                | 31.9 ms: 1.08x faster                                                     |
| docutils                   | 2.77 sec                                               | 2.56 sec: 1.08x faster                                                    |
| richards_super             | 51.5 ms                                                | 47.8 ms: 1.08x faster                                                     |
| xml_etree_generate         | 89.2 ms                                                | 82.9 ms: 1.07x faster                                                     |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                                      |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.71 ms: 1.07x faster                                                     |
| xml_etree_process          | 61.7 ms                                                | 57.8 ms: 1.07x faster                                                     |
| pprint_safe_repr           | 776 ms                                                 | 726 ms: 1.07x faster                                                      |
| sympy_expand               | 478 ms                                                 | 449 ms: 1.07x faster                                                      |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.07x faster                                                    |
| pycparser                  | 1.18 sec                                               | 1.11 sec: 1.06x faster                                                    |
| hexiom                     | 6.41 ms                                                | 6.08 ms: 1.05x faster                                                     |
| nqueens                    | 83.3 ms                                                | 79.3 ms: 1.05x faster                                                     |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.03x faster                                                      |
| regex_dna                  | 212 ms                                                 | 207 ms: 1.02x faster                                                      |
| sqlite_synth               | 2.83 us                                                | 2.77 us: 1.02x faster                                                     |
| pickle_pure_python         | 324 us                                                 | 318 us: 1.02x faster                                                      |
| fannkuch                   | 417 ms                                                 | 410 ms: 1.02x faster                                                      |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                      |
| coroutines                 | 23.2 ms                                                | 23.3 ms: 1.01x slower                                                     |
| json                       | 5.26 ms                                                | 5.40 ms: 1.03x slower                                                     |
| typing_runtime_protocols   | 158 us                                                 | 163 us: 1.03x slower                                                      |
| bench_thread_pool          | 842 us                                                 | 873 us: 1.04x slower                                                      |
| json_loads                 | 28.5 us                                                | 29.8 us: 1.05x slower                                                     |
| telco                      | 7.10 ms                                                | 7.71 ms: 1.09x slower                                                     |
| json_dumps                 | 10.4 ms                                                | 11.4 ms: 1.10x slower                                                     |
| coverage                   | 72.7 ms                                                | 83.5 ms: 1.15x slower                                                     |
| python_startup_no_site     | 6.94 ms                                                | 8.18 ms: 1.18x slower                                                     |
| gc_traversal               | 3.79 ms                                                | 4.82 ms: 1.27x slower                                                     |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 2.45 ms: 1.66x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 82.1 ms: 3.42x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.11x faster                                                              |

Benchmark hidden because not significant (3): unpickle_pure_python, regex_v8, asyncio_websockets
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250415-3.14.0a7+-39daf97/bm-20250415-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-39daf97.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.134x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.10x