# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_binary_op_swa
- machine: linux-x86_64
- commit hash: 50038ae
- commit date: 2024-12-06
- overall geometric mean: 1.093x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241206-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-50038ae |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 259 ms: 1.06x faster                                                         |
| docutils       | 2.77 sec                                               | 2.68 sec: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241206-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-50038ae |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 619 ms: 1.91x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 620 ms: 1.87x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 319 ms: 1.80x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 256 ms: 1.76x faster                                                         |
| async_tree_none            | 472 ms                                                 | 272 ms: 1.73x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 343 ms: 1.68x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 491 ms: 1.48x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 507 ms: 1.43x faster                                                         |
| Geometric mean             | (ref)                                                  | 1.70x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241206-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-50038ae |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 76.8 ms: 1.10x faster                                                        |
| nbody          | 97.0 ms                                                | 94.2 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241206-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-50038ae |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 130 ms: 1.14x faster                                                         |
| regex_effbot   | 3.61 ms                                                | 3.47 ms: 1.04x faster                                                        |
| regex_dna      | 212 ms                                                 | 217 ms: 1.02x slower                                                         |
| regex_v8       | 23.1 ms                                                | 25.2 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241206-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-50038ae |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                       |
| unpickle_pure_python | 230 us                                                 | 197 us: 1.17x faster                                                         |
| xml_etree_parse      | 159 ms                                                 | 138 ms: 1.16x faster                                                         |
| xml_etree_iterparse  | 107 ms                                                 | 94.7 ms: 1.13x faster                                                        |
| xml_etree_process    | 61.7 ms                                                | 54.9 ms: 1.12x faster                                                        |
| xml_etree_generate   | 89.2 ms                                                | 80.5 ms: 1.11x faster                                                        |
| json_loads           | 28.5 us                                                | 26.1 us: 1.09x faster                                                        |
| json_dumps           | 10.4 ms                                                | 11.1 ms: 1.07x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                                 |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241206-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-50038ae |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.03 ms: 1.01x slower                                                        |
| python_startup         | 9.55 ms                                                | 12.7 ms: 1.33x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241206-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-50038ae |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.1 ms: 1.18x faster                                                        |
| django_template | 34.6 ms                                                | 33.9 ms: 1.02x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241206-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-50038ae |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 619 ms: 1.91x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 620 ms: 1.87x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 319 ms: 1.80x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 256 ms: 1.76x faster                                                         |
| async_tree_none            | 472 ms                                                 | 272 ms: 1.73x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 343 ms: 1.68x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 491 ms: 1.48x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 507 ms: 1.43x faster                                                         |
| deepcopy_memo              | 40.7 us                                                | 29.2 us: 1.39x faster                                                        |
| deepcopy                   | 371 us                                                 | 269 us: 1.38x faster                                                         |
| comprehensions             | 21.8 us                                                | 17.3 us: 1.26x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.72 us: 1.23x faster                                                        |
| richards                   | 45.8 ms                                                | 38.0 ms: 1.21x faster                                                        |
| tomli_loads                | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                       |
| mako                       | 11.9 ms                                                | 10.1 ms: 1.18x faster                                                        |
| pathlib                    | 19.3 ms                                                | 16.4 ms: 1.18x faster                                                        |
| unpickle_pure_python       | 230 us                                                 | 197 us: 1.17x faster                                                         |
| richards_super             | 51.5 ms                                                | 44.1 ms: 1.17x faster                                                        |
| deltablue                  | 3.72 ms                                                | 3.19 ms: 1.16x faster                                                        |
| xml_etree_parse            | 159 ms                                                 | 138 ms: 1.16x faster                                                         |
| crypto_pyaes               | 81.9 ms                                                | 70.8 ms: 1.16x faster                                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 65.9 ms: 1.14x faster                                                        |
| regex_compile              | 148 ms                                                 | 130 ms: 1.14x faster                                                         |
| sqlalchemy_declarative     | 147 ms                                                 | 129 ms: 1.14x faster                                                         |
| logging_format             | 7.23 us                                                | 6.41 us: 1.13x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                 | 94.7 ms: 1.13x faster                                                        |
| xml_etree_process          | 61.7 ms                                                | 54.9 ms: 1.12x faster                                                        |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.6 ms: 1.12x faster                                                        |
| scimark_fft                | 382 ms                                                 | 341 ms: 1.12x faster                                                         |
| xml_etree_generate         | 89.2 ms                                                | 80.5 ms: 1.11x faster                                                        |
| float                      | 84.7 ms                                                | 76.8 ms: 1.10x faster                                                        |
| json_loads                 | 28.5 us                                                | 26.1 us: 1.09x faster                                                        |
| logging_simple             | 6.46 us                                                | 5.92 us: 1.09x faster                                                        |
| pprint_safe_repr           | 776 ms                                                 | 713 ms: 1.09x faster                                                         |
| sympy_sum                  | 169 ms                                                 | 156 ms: 1.09x faster                                                         |
| json                       | 5.26 ms                                                | 4.89 ms: 1.08x faster                                                        |
| scimark_sor                | 129 ms                                                 | 121 ms: 1.07x faster                                                         |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.06x faster                                                       |
| 2to3                       | 274 ms                                                 | 259 ms: 1.06x faster                                                         |
| sympy_str                  | 300 ms                                                 | 283 ms: 1.06x faster                                                         |
| chaos                      | 67.0 ms                                                | 63.4 ms: 1.06x faster                                                        |
| fannkuch                   | 417 ms                                                 | 396 ms: 1.05x faster                                                         |
| raytrace                   | 312 ms                                                 | 298 ms: 1.05x faster                                                         |
| pyflate                    | 482 ms                                                 | 461 ms: 1.05x faster                                                         |
| regex_effbot               | 3.61 ms                                                | 3.47 ms: 1.04x faster                                                        |
| logging_silent             | 104 ns                                                 | 101 ns: 1.04x faster                                                         |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.04x faster                                                         |
| sympy_integrate            | 21.4 ms                                                | 20.7 ms: 1.03x faster                                                        |
| go                         | 139 ms                                                 | 135 ms: 1.03x faster                                                         |
| docutils                   | 2.77 sec                                               | 2.68 sec: 1.03x faster                                                       |
| nbody                      | 97.0 ms                                                | 94.2 ms: 1.03x faster                                                        |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                         |
| sqlglot_transpile          | 1.68 ms                                                | 1.64 ms: 1.03x faster                                                        |
| async_generators           | 463 ms                                                 | 451 ms: 1.03x faster                                                         |
| sqlglot_parse              | 1.36 ms                                                | 1.33 ms: 1.03x faster                                                        |
| mdp                        | 2.63 sec                                               | 2.57 sec: 1.02x faster                                                       |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.02x faster                                                       |
| django_template            | 34.6 ms                                                | 33.9 ms: 1.02x faster                                                        |
| sympy_expand               | 478 ms                                                 | 474 ms: 1.01x faster                                                         |
| dulwich_log                | 68.5 ms                                                | 68.2 ms: 1.00x faster                                                        |
| sqlglot_normalize          | 110 ms                                                 | 110 ms: 1.00x faster                                                         |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                         |
| sqlglot_optimize           | 54.8 ms                                                | 55.4 ms: 1.01x slower                                                        |
| python_startup_no_site     | 6.94 ms                                                | 7.03 ms: 1.01x slower                                                        |
| regex_dna                  | 212 ms                                                 | 217 ms: 1.02x slower                                                         |
| coroutines                 | 23.2 ms                                                | 23.9 ms: 1.03x slower                                                        |
| bench_thread_pool          | 842 us                                                 | 875 us: 1.04x slower                                                         |
| spectral_norm              | 115 ms                                                 | 121 ms: 1.06x slower                                                         |
| json_dumps                 | 10.4 ms                                                | 11.1 ms: 1.07x slower                                                        |
| typing_runtime_protocols   | 158 us                                                 | 170 us: 1.08x slower                                                         |
| telco                      | 7.10 ms                                                | 7.64 ms: 1.08x slower                                                        |
| regex_v8                   | 23.1 ms                                                | 25.2 ms: 1.09x slower                                                        |
| nqueens                    | 83.3 ms                                                | 91.4 ms: 1.10x slower                                                        |
| hexiom                     | 6.41 ms                                                | 7.13 ms: 1.11x slower                                                        |
| generators                 | 31.2 ms                                                | 36.4 ms: 1.16x slower                                                        |
| coverage                   | 72.7 ms                                                | 86.3 ms: 1.19x slower                                                        |
| gc_traversal               | 3.79 ms                                                | 4.80 ms: 1.26x slower                                                        |
| python_startup             | 9.55 ms                                                | 12.7 ms: 1.33x slower                                                        |
| create_gc_cycles           | 1.48 ms                                                | 2.46 ms: 1.67x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 80.9 ms: 3.37x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                                 |

Benchmark hidden because not significant (4): pickle_pure_python, sqlite_synth, pidigits, scimark_sparse_mat_mult
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241206-3.14.0a2+-50038ae-JIT/bm-20241206-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-50038ae.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.093x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.10x