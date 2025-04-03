# Results vs. 3.12.0

- fork: brandtbucher
- ref: unbox
- machine: linux-x86_64
- commit hash: 07c4777
- commit date: 2025-04-03
- overall geometric mean: 1.103x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-brandtbucher-unbox-3.14.0a6+-07c4777 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 260 ms: 1.06x faster                                          |
| docutils       | 2.77 sec                                               | 2.62 sec: 1.06x faster                                        |
| Geometric mean | (ref)                                                  | 1.06x faster                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-brandtbucher-unbox-3.14.0a6+-07c4777 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 633 ms: 1.87x faster                                          |
| async_tree_io              | 1.16 sec                                               | 631 ms: 1.83x faster                                          |
| async_tree_memoization     | 578 ms                                                 | 322 ms: 1.79x faster                                          |
| async_tree_none            | 472 ms                                                 | 265 ms: 1.78x faster                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 323 ms: 1.78x faster                                          |
| async_tree_none_tg         | 450 ms                                                 | 254 ms: 1.77x faster                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.51x faster                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 489 ms: 1.48x faster                                          |
| Geometric mean             | (ref)                                                  | 1.72x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-brandtbucher-unbox-3.14.0a6+-07c4777 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 84.7 ms                                                | 74.1 ms: 1.14x faster                                         |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                          |
| nbody          | 97.0 ms                                                | 100 ms: 1.03x slower                                          |
| Geometric mean | (ref)                                                  | 1.03x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-brandtbucher-unbox-3.14.0a6+-07c4777 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 131 ms: 1.13x faster                                          |
| regex_effbot   | 3.61 ms                                                | 3.25 ms: 1.11x faster                                         |
| regex_v8       | 23.1 ms                                                | 22.7 ms: 1.02x faster                                         |
| regex_dna      | 212 ms                                                 | 220 ms: 1.04x slower                                          |
| Geometric mean | (ref)                                                  | 1.06x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-brandtbucher-unbox-3.14.0a6+-07c4777 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.86 sec: 1.25x faster                                        |
| xml_etree_parse      | 159 ms                                                 | 142 ms: 1.12x faster                                          |
| xml_etree_iterparse  | 107 ms                                                 | 99.5 ms: 1.07x faster                                         |
| xml_etree_generate   | 89.2 ms                                                | 85.2 ms: 1.05x faster                                         |
| unpickle_pure_python | 230 us                                                 | 222 us: 1.04x faster                                          |
| xml_etree_process    | 61.7 ms                                                | 59.8 ms: 1.03x faster                                         |
| json_dumps           | 10.4 ms                                                | 11.3 ms: 1.09x slower                                         |
| json_loads           | 28.5 us                                                | 34.2 us: 1.20x slower                                         |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                  |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-brandtbucher-unbox-3.14.0a6+-07c4777 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.20 ms: 1.18x slower                                         |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.38x slower                                         |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-brandtbucher-unbox-3.14.0a6+-07c4777 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.4 ms: 1.07x faster                                         |
| mako            | 11.9 ms                                                | 11.6 ms: 1.02x faster                                         |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-brandtbucher-unbox-3.14.0a6+-07c4777 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.25 sec: 2.11x faster                                        |
| async_tree_io_tg           | 1.18 sec                                               | 633 ms: 1.87x faster                                          |
| async_tree_io              | 1.16 sec                                               | 631 ms: 1.83x faster                                          |
| async_tree_memoization     | 578 ms                                                 | 322 ms: 1.79x faster                                          |
| async_tree_none            | 472 ms                                                 | 265 ms: 1.78x faster                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 323 ms: 1.78x faster                                          |
| async_tree_none_tg         | 450 ms                                                 | 254 ms: 1.77x faster                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.51x faster                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 489 ms: 1.48x faster                                          |
| deepcopy                   | 371 us                                                 | 260 us: 1.43x faster                                          |
| deepcopy_memo              | 40.7 us                                                | 30.4 us: 1.34x faster                                         |
| comprehensions             | 21.8 us                                                | 17.2 us: 1.27x faster                                         |
| tomli_loads                | 2.33 sec                                               | 1.86 sec: 1.25x faster                                        |
| spectral_norm              | 115 ms                                                 | 92.5 ms: 1.24x faster                                         |
| deepcopy_reduce            | 3.35 us                                                | 2.71 us: 1.24x faster                                         |
| async_generators           | 463 ms                                                 | 394 ms: 1.17x faster                                          |
| go                         | 139 ms                                                 | 120 ms: 1.17x faster                                          |
| chaos                      | 67.0 ms                                                | 57.5 ms: 1.17x faster                                         |
| logging_format             | 7.23 us                                                | 6.21 us: 1.16x faster                                         |
| pathlib                    | 19.3 ms                                                | 16.7 ms: 1.16x faster                                         |
| dulwich_log                | 68.5 ms                                                | 59.4 ms: 1.15x faster                                         |
| raytrace                   | 312 ms                                                 | 272 ms: 1.15x faster                                          |
| logging_simple             | 6.46 us                                                | 5.64 us: 1.14x faster                                         |
| float                      | 84.7 ms                                                | 74.1 ms: 1.14x faster                                         |
| deltablue                  | 3.72 ms                                                | 3.26 ms: 1.14x faster                                         |
| regex_compile              | 148 ms                                                 | 131 ms: 1.13x faster                                          |
| xml_etree_parse            | 159 ms                                                 | 142 ms: 1.12x faster                                          |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                          |
| regex_effbot               | 3.61 ms                                                | 3.25 ms: 1.11x faster                                         |
| sqlalchemy_declarative     | 147 ms                                                 | 132 ms: 1.11x faster                                          |
| scimark_monte_carlo        | 75.1 ms                                                | 68.2 ms: 1.10x faster                                         |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.0 ms: 1.10x faster                                         |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.10x faster                                          |
| sympy_str                  | 300 ms                                                 | 274 ms: 1.09x faster                                          |
| coroutines                 | 23.2 ms                                                | 21.2 ms: 1.09x faster                                         |
| sympy_integrate            | 21.4 ms                                                | 19.8 ms: 1.08x faster                                         |
| generators                 | 31.2 ms                                                | 28.9 ms: 1.08x faster                                         |
| xml_etree_iterparse        | 107 ms                                                 | 99.5 ms: 1.07x faster                                         |
| logging_silent             | 104 ns                                                 | 97.6 ns: 1.07x faster                                         |
| django_template            | 34.6 ms                                                | 32.4 ms: 1.07x faster                                         |
| docutils                   | 2.77 sec                                               | 2.62 sec: 1.06x faster                                        |
| 2to3                       | 274 ms                                                 | 260 ms: 1.06x faster                                          |
| pyflate                    | 482 ms                                                 | 461 ms: 1.05x faster                                          |
| hexiom                     | 6.41 ms                                                | 6.13 ms: 1.05x faster                                         |
| xml_etree_generate         | 89.2 ms                                                | 85.2 ms: 1.05x faster                                         |
| unpickle_pure_python       | 230 us                                                 | 222 us: 1.04x faster                                          |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                          |
| xml_etree_process          | 61.7 ms                                                | 59.8 ms: 1.03x faster                                         |
| mako                       | 11.9 ms                                                | 11.6 ms: 1.02x faster                                         |
| regex_v8                   | 23.1 ms                                                | 22.7 ms: 1.02x faster                                         |
| sympy_expand               | 478 ms                                                 | 470 ms: 1.02x faster                                          |
| richards                   | 45.8 ms                                                | 45.3 ms: 1.01x faster                                         |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                          |
| crypto_pyaes               | 81.9 ms                                                | 82.1 ms: 1.00x slower                                         |
| scimark_fft                | 382 ms                                                 | 384 ms: 1.01x slower                                          |
| pprint_safe_repr           | 776 ms                                                 | 782 ms: 1.01x slower                                          |
| pprint_pformat             | 1.57 sec                                               | 1.59 sec: 1.02x slower                                        |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.15 ms: 1.02x slower                                         |
| pycparser                  | 1.18 sec                                               | 1.20 sec: 1.02x slower                                        |
| nbody                      | 97.0 ms                                                | 100 ms: 1.03x slower                                          |
| regex_dna                  | 212 ms                                                 | 220 ms: 1.04x slower                                          |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                          |
| fannkuch                   | 417 ms                                                 | 435 ms: 1.04x slower                                          |
| scimark_lu                 | 118 ms                                                 | 124 ms: 1.05x slower                                          |
| bench_thread_pool          | 842 us                                                 | 885 us: 1.05x slower                                          |
| json_dumps                 | 10.4 ms                                                | 11.3 ms: 1.09x slower                                         |
| json                       | 5.26 ms                                                | 5.86 ms: 1.11x slower                                         |
| telco                      | 7.10 ms                                                | 7.94 ms: 1.12x slower                                         |
| coverage                   | 72.7 ms                                                | 84.7 ms: 1.17x slower                                         |
| python_startup_no_site     | 6.94 ms                                                | 8.20 ms: 1.18x slower                                         |
| json_loads                 | 28.5 us                                                | 34.2 us: 1.20x slower                                         |
| gc_traversal               | 3.79 ms                                                | 4.91 ms: 1.29x slower                                         |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.38x slower                                         |
| create_gc_cycles           | 1.48 ms                                                | 2.49 ms: 1.68x slower                                         |
| bench_mp_pool              | 24.0 ms                                                | 83.6 ms: 3.48x slower                                         |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                  |

Benchmark hidden because not significant (5): pickle_pure_python, asyncio_websockets, richards_super, nqueens, sqlite_synth
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250403-3.14.0a6+-07c4777/bm-20250403-linux-x86_64-brandtbucher-unbox-3.14.0a6+-07c4777.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.103x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.11x