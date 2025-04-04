# Results vs. 3.12.0

- fork: brandtbucher
- ref: negative_subscr
- machine: linux-x86_64
- commit hash: 6a93886
- commit date: 2025-04-03
- overall geometric mean: 1.127x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 249 ms: 1.10x faster                                                    |
| docutils       | 2.77 sec                                               | 2.60 sec: 1.07x faster                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 614 ms: 1.93x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 616 ms: 1.88x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                    |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                    |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 477 ms: 1.52x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 490 ms: 1.48x faster                                                    |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.1 ms: 1.23x faster                                                   |
| nbody          | 97.0 ms                                                | 93.9 ms: 1.03x faster                                                   |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                  | 1.08x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.18x faster                                                    |
| regex_effbot   | 3.61 ms                                                | 3.31 ms: 1.09x faster                                                   |
| regex_v8       | 23.1 ms                                                | 23.0 ms: 1.01x faster                                                   |
| regex_dna      | 212 ms                                                 | 219 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                  | 1.06x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.92 sec: 1.21x faster                                                  |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                 | 99.1 ms: 1.08x faster                                                   |
| unpickle_pure_python | 230 us                                                 | 214 us: 1.07x faster                                                    |
| xml_etree_generate   | 89.2 ms                                                | 83.6 ms: 1.07x faster                                                   |
| xml_etree_process    | 61.7 ms                                                | 58.5 ms: 1.06x faster                                                   |
| pickle_pure_python   | 324 us                                                 | 319 us: 1.01x faster                                                    |
| json_loads           | 28.5 us                                                | 29.8 us: 1.05x slower                                                   |
| json_dumps           | 10.4 ms                                                | 11.4 ms: 1.10x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.18 ms: 1.18x slower                                                   |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.38x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.9 ms: 1.08x faster                                                   |
| mako            | 11.9 ms                                                | 11.4 ms: 1.04x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.22 sec: 2.15x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 614 ms: 1.93x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 616 ms: 1.88x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                    |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                    |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 477 ms: 1.52x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 490 ms: 1.48x faster                                                    |
| deepcopy                   | 371 us                                                 | 251 us: 1.48x faster                                                    |
| deepcopy_memo              | 40.7 us                                                | 28.9 us: 1.41x faster                                                   |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                | 2.61 us: 1.28x faster                                                   |
| go                         | 139 ms                                                 | 112 ms: 1.24x faster                                                    |
| float                      | 84.7 ms                                                | 69.1 ms: 1.23x faster                                                   |
| tomli_loads                | 2.33 sec                                               | 1.92 sec: 1.21x faster                                                  |
| raytrace                   | 312 ms                                                 | 259 ms: 1.21x faster                                                    |
| regex_compile              | 148 ms                                                 | 126 ms: 1.18x faster                                                    |
| chaos                      | 67.0 ms                                                | 56.8 ms: 1.18x faster                                                   |
| logging_format             | 7.23 us                                                | 6.15 us: 1.18x faster                                                   |
| pathlib                    | 19.3 ms                                                | 16.5 ms: 1.17x faster                                                   |
| dulwich_log                | 68.5 ms                                                | 58.6 ms: 1.17x faster                                                   |
| logging_simple             | 6.46 us                                                | 5.53 us: 1.17x faster                                                   |
| spectral_norm              | 115 ms                                                 | 98.7 ms: 1.16x faster                                                   |
| async_generators           | 463 ms                                                 | 398 ms: 1.16x faster                                                    |
| scimark_monte_carlo        | 75.1 ms                                                | 65.8 ms: 1.14x faster                                                   |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.13x faster                                                    |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                    |
| scimark_fft                | 382 ms                                                 | 339 ms: 1.13x faster                                                    |
| crypto_pyaes               | 81.9 ms                                                | 73.1 ms: 1.12x faster                                                   |
| sympy_str                  | 300 ms                                                 | 268 ms: 1.12x faster                                                    |
| sympy_integrate            | 21.4 ms                                                | 19.2 ms: 1.12x faster                                                   |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                                    |
| scimark_sor                | 129 ms                                                 | 116 ms: 1.11x faster                                                    |
| deltablue                  | 3.72 ms                                                | 3.34 ms: 1.11x faster                                                   |
| 2to3                       | 274 ms                                                 | 249 ms: 1.10x faster                                                    |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.1 ms: 1.10x faster                                                   |
| regex_effbot               | 3.61 ms                                                | 3.31 ms: 1.09x faster                                                   |
| django_template            | 34.6 ms                                                | 31.9 ms: 1.08x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 99.1 ms: 1.08x faster                                                   |
| pprint_safe_repr           | 776 ms                                                 | 722 ms: 1.07x faster                                                    |
| unpickle_pure_python       | 230 us                                                 | 214 us: 1.07x faster                                                    |
| richards                   | 45.8 ms                                                | 42.9 ms: 1.07x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.07x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.60 sec: 1.07x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 83.6 ms: 1.07x faster                                                   |
| pyflate                    | 482 ms                                                 | 453 ms: 1.07x faster                                                    |
| logging_silent             | 104 ns                                                 | 98.3 ns: 1.06x faster                                                   |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                    |
| xml_etree_process          | 61.7 ms                                                | 58.5 ms: 1.06x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.81 ms: 1.05x faster                                                   |
| richards_super             | 51.5 ms                                                | 49.2 ms: 1.05x faster                                                   |
| mako                       | 11.9 ms                                                | 11.4 ms: 1.04x faster                                                   |
| sympy_expand               | 478 ms                                                 | 458 ms: 1.04x faster                                                    |
| nbody                      | 97.0 ms                                                | 93.9 ms: 1.03x faster                                                   |
| sqlite_synth               | 2.83 us                                                | 2.75 us: 1.03x faster                                                   |
| hexiom                     | 6.41 ms                                                | 6.24 ms: 1.03x faster                                                   |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                                    |
| generators                 | 31.2 ms                                                | 30.7 ms: 1.02x faster                                                   |
| nqueens                    | 83.3 ms                                                | 81.9 ms: 1.02x faster                                                   |
| pickle_pure_python         | 324 us                                                 | 319 us: 1.01x faster                                                    |
| fannkuch                   | 417 ms                                                 | 413 ms: 1.01x faster                                                    |
| regex_v8                   | 23.1 ms                                                | 23.0 ms: 1.01x faster                                                   |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                    |
| coroutines                 | 23.2 ms                                                | 23.4 ms: 1.01x slower                                                   |
| json                       | 5.26 ms                                                | 5.36 ms: 1.02x slower                                                   |
| regex_dna                  | 212 ms                                                 | 219 ms: 1.03x slower                                                    |
| typing_runtime_protocols   | 158 us                                                 | 163 us: 1.03x slower                                                    |
| json_loads                 | 28.5 us                                                | 29.8 us: 1.05x slower                                                   |
| bench_thread_pool          | 842 us                                                 | 883 us: 1.05x slower                                                    |
| json_dumps                 | 10.4 ms                                                | 11.4 ms: 1.10x slower                                                   |
| telco                      | 7.10 ms                                                | 7.87 ms: 1.11x slower                                                   |
| coverage                   | 72.7 ms                                                | 85.6 ms: 1.18x slower                                                   |
| python_startup_no_site     | 6.94 ms                                                | 8.18 ms: 1.18x slower                                                   |
| gc_traversal               | 3.79 ms                                                | 5.07 ms: 1.33x slower                                                   |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.38x slower                                                   |
| create_gc_cycles           | 1.48 ms                                                | 2.48 ms: 1.68x slower                                                   |
| bench_mp_pool              | 24.0 ms                                                | 83.2 ms: 3.46x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.11x faster                                                            |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250403-3.14.0a6+-6a93886/bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.127x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.11x