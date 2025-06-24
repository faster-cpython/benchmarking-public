# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_hot
- machine: linux-x86_64
- commit hash: a987be7
- commit date: 2025-06-23
- overall geometric mean: 1.135x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 259 ms: 1.06x faster                                              |
| docutils       | 2.77 sec                                               | 2.64 sec: 1.05x faster                                            |
| Geometric mean | (ref)                                                  | 1.05x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 598 ms: 1.93x faster                                              |
| async_tree_io_tg           | 1.18 sec                                               | 616 ms: 1.92x faster                                              |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                              |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                              |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                              |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                              |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 490 ms: 1.48x faster                                              |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 495 ms: 1.47x faster                                              |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 84.7 ms                                                | 65.0 ms: 1.30x faster                                             |
| nbody          | 97.0 ms                                                | 96.0 ms: 1.01x faster                                             |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                              |
| Geometric mean | (ref)                                                  | 1.10x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                              |
| regex_effbot   | 3.61 ms                                                | 3.25 ms: 1.11x faster                                             |
| regex_dna      | 212 ms                                                 | 199 ms: 1.07x faster                                              |
| regex_v8       | 23.1 ms                                                | 22.5 ms: 1.03x faster                                             |
| Geometric mean | (ref)                                                  | 1.09x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.86 sec: 1.26x faster                                            |
| unpickle_pure_python | 230 us                                                 | 195 us: 1.18x faster                                              |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                              |
| xml_etree_generate   | 89.2 ms                                                | 80.0 ms: 1.11x faster                                             |
| xml_etree_process    | 61.7 ms                                                | 55.4 ms: 1.11x faster                                             |
| xml_etree_iterparse  | 107 ms                                                 | 98.3 ms: 1.09x faster                                             |
| pickle_pure_python   | 324 us                                                 | 320 us: 1.01x faster                                              |
| json_loads           | 28.5 us                                                | 28.2 us: 1.01x faster                                             |
| json_dumps           | 10.4 ms                                                | 10.9 ms: 1.05x slower                                             |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.93 ms: 1.00x faster                                             |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.27x slower                                             |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.4 ms: 1.14x faster                                             |
| django_template | 34.6 ms                                                | 32.4 ms: 1.07x faster                                             |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.25 sec: 2.11x faster                                            |
| async_tree_io              | 1.16 sec                                               | 598 ms: 1.93x faster                                              |
| async_tree_io_tg           | 1.18 sec                                               | 616 ms: 1.92x faster                                              |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                              |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                              |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                              |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                              |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 490 ms: 1.48x faster                                              |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 495 ms: 1.47x faster                                              |
| deepcopy                   | 371 us                                                 | 259 us: 1.43x faster                                              |
| richards                   | 45.8 ms                                                | 32.9 ms: 1.39x faster                                             |
| deepcopy_memo              | 40.7 us                                                | 29.8 us: 1.37x faster                                             |
| richards_super             | 51.5 ms                                                | 38.6 ms: 1.34x faster                                             |
| comprehensions             | 21.8 us                                                | 16.3 us: 1.33x faster                                             |
| float                      | 84.7 ms                                                | 65.0 ms: 1.30x faster                                             |
| tomli_loads                | 2.33 sec                                               | 1.86 sec: 1.26x faster                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.73 us: 1.23x faster                                             |
| deltablue                  | 3.72 ms                                                | 3.06 ms: 1.21x faster                                             |
| go                         | 139 ms                                                 | 117 ms: 1.19x faster                                              |
| pyflate                    | 482 ms                                                 | 406 ms: 1.19x faster                                              |
| unpickle_pure_python       | 230 us                                                 | 195 us: 1.18x faster                                              |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                              |
| scimark_fft                | 382 ms                                                 | 328 ms: 1.17x faster                                              |
| dulwich_log                | 68.5 ms                                                | 59.6 ms: 1.15x faster                                             |
| raytrace                   | 312 ms                                                 | 273 ms: 1.14x faster                                              |
| pathlib                    | 19.3 ms                                                | 17.0 ms: 1.14x faster                                             |
| mako                       | 11.9 ms                                                | 10.4 ms: 1.14x faster                                             |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                              |
| scimark_monte_carlo        | 75.1 ms                                                | 66.5 ms: 1.13x faster                                             |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.13x faster                                              |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.12x faster                                              |
| xml_etree_generate         | 89.2 ms                                                | 80.0 ms: 1.11x faster                                             |
| xml_etree_process          | 61.7 ms                                                | 55.4 ms: 1.11x faster                                             |
| regex_effbot               | 3.61 ms                                                | 3.25 ms: 1.11x faster                                             |
| sympy_integrate            | 21.4 ms                                                | 19.4 ms: 1.11x faster                                             |
| sympy_str                  | 300 ms                                                 | 271 ms: 1.10x faster                                              |
| crypto_pyaes               | 81.9 ms                                                | 74.4 ms: 1.10x faster                                             |
| xml_etree_iterparse        | 107 ms                                                 | 98.3 ms: 1.09x faster                                             |
| chaos                      | 67.0 ms                                                | 62.3 ms: 1.07x faster                                             |
| async_generators           | 463 ms                                                 | 431 ms: 1.07x faster                                              |
| logging_format             | 7.23 us                                                | 6.74 us: 1.07x faster                                             |
| django_template            | 34.6 ms                                                | 32.4 ms: 1.07x faster                                             |
| regex_dna                  | 212 ms                                                 | 199 ms: 1.07x faster                                              |
| 2to3                       | 274 ms                                                 | 259 ms: 1.06x faster                                              |
| logging_simple             | 6.46 us                                                | 6.11 us: 1.06x faster                                             |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                              |
| scimark_sor                | 129 ms                                                 | 123 ms: 1.05x faster                                              |
| pycparser                  | 1.18 sec                                               | 1.12 sec: 1.05x faster                                            |
| docutils                   | 2.77 sec                                               | 2.64 sec: 1.05x faster                                            |
| fannkuch                   | 417 ms                                                 | 403 ms: 1.04x faster                                              |
| regex_v8                   | 23.1 ms                                                | 22.5 ms: 1.03x faster                                             |
| generators                 | 31.2 ms                                                | 30.4 ms: 1.03x faster                                             |
| sympy_expand               | 478 ms                                                 | 466 ms: 1.03x faster                                              |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.94 ms: 1.02x faster                                             |
| hexiom                     | 6.41 ms                                                | 6.30 ms: 1.02x faster                                             |
| pickle_pure_python         | 324 us                                                 | 320 us: 1.01x faster                                              |
| json_loads                 | 28.5 us                                                | 28.2 us: 1.01x faster                                             |
| nbody                      | 97.0 ms                                                | 96.0 ms: 1.01x faster                                             |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                             |
| nqueens                    | 83.3 ms                                                | 82.6 ms: 1.01x faster                                             |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                              |
| python_startup_no_site     | 6.94 ms                                                | 6.93 ms: 1.00x faster                                             |
| scimark_lu                 | 118 ms                                                 | 119 ms: 1.01x slower                                              |
| pprint_safe_repr           | 776 ms                                                 | 804 ms: 1.04x slower                                              |
| json_dumps                 | 10.4 ms                                                | 10.9 ms: 1.05x slower                                             |
| pprint_pformat             | 1.57 sec                                               | 1.64 sec: 1.05x slower                                            |
| telco                      | 7.10 ms                                                | 7.59 ms: 1.07x slower                                             |
| typing_runtime_protocols   | 158 us                                                 | 169 us: 1.07x slower                                              |
| coroutines                 | 23.2 ms                                                | 24.9 ms: 1.07x slower                                             |
| coverage                   | 72.7 ms                                                | 87.0 ms: 1.20x slower                                             |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.27x slower                                             |
| gc_traversal               | 3.79 ms                                                | 4.97 ms: 1.31x slower                                             |
| create_gc_cycles           | 1.48 ms                                                | 2.60 ms: 1.76x slower                                             |
| logging_silent             | 104 ns                                                 | 472 ns: 4.52x slower                                              |
| Geometric mean             | (ref)                                                  | 1.11x faster                                                      |

Benchmark hidden because not significant (2): json, asyncio_websockets
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250623-3.15.0a0-a987be7-JIT/bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.135x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.15x