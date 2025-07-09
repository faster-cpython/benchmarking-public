# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_oz
- machine: linux-x86_64
- commit hash: 6448067
- commit date: 2025-06-28
- overall geometric mean: 1.053x faster
- HPT reliability: 99.75%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 286 ms: 1.00x slower                                                |
| docutils       | 2.87 sec                                                     | 2.91 sec: 1.02x slower                                              |
| Geometric mean | (ref)                                                        | 1.01x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 627 ms: 1.68x faster                                                |
| async_tree_io              | 1.04 sec                                                     | 627 ms: 1.66x faster                                                |
| async_tree_memoization     | 544 ms                                                       | 332 ms: 1.64x faster                                                |
| async_tree_memoization_tg  | 540 ms                                                       | 330 ms: 1.64x faster                                                |
| async_tree_none            | 452 ms                                                       | 284 ms: 1.59x faster                                                |
| async_tree_none_tg         | 431 ms                                                       | 272 ms: 1.59x faster                                                |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 503 ms: 1.38x faster                                                |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 506 ms: 1.38x faster                                                |
| Geometric mean             | (ref)                                                        | 1.56x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 66.0 ms: 1.16x faster                                               |
| pidigits       | 265 ms                                                       | 258 ms: 1.03x faster                                                |
| nbody          | 88.0 ms                                                      | 102 ms: 1.16x slower                                                |
| Geometric mean | (ref)                                                        | 1.01x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_dna      | 239 ms                                                       | 220 ms: 1.08x faster                                                |
| regex_compile  | 144 ms                                                       | 137 ms: 1.05x faster                                                |
| regex_v8       | 23.6 ms                                                      | 23.0 ms: 1.03x faster                                               |
| regex_effbot   | 3.57 ms                                                      | 3.49 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                        | 1.05x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 95.9 ms: 1.07x faster                                               |
| xml_etree_parse      | 144 ms                                                       | 136 ms: 1.06x faster                                                |
| xml_etree_generate   | 86.1 ms                                                      | 82.9 ms: 1.04x faster                                               |
| tomli_loads          | 2.16 sec                                                     | 2.11 sec: 1.02x faster                                              |
| xml_etree_process    | 58.4 ms                                                      | 58.0 ms: 1.01x faster                                               |
| unpickle_pure_python | 210 us                                                       | 215 us: 1.03x slower                                                |
| json_loads           | 24.4 us                                                      | 25.1 us: 1.03x slower                                               |
| pickle_pure_python   | 318 us                                                       | 340 us: 1.07x slower                                                |
| json_dumps           | 10.2 ms                                                      | 11.2 ms: 1.10x slower                                               |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.85 ms: 1.02x slower                                               |
| python_startup         | 11.6 ms                                                      | 15.3 ms: 1.32x slower                                               |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 36.2 ms: 1.05x faster                                               |
| mako            | 10.0 ms                                                      | 11.0 ms: 1.10x slower                                               |
| Geometric mean  | (ref)                                                        | 1.02x slower                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.31 sec: 1.96x faster                                              |
| async_tree_io_tg           | 1.05 sec                                                     | 627 ms: 1.68x faster                                                |
| async_tree_io              | 1.04 sec                                                     | 627 ms: 1.66x faster                                                |
| async_tree_memoization     | 544 ms                                                       | 332 ms: 1.64x faster                                                |
| async_tree_memoization_tg  | 540 ms                                                       | 330 ms: 1.64x faster                                                |
| async_tree_none            | 452 ms                                                       | 284 ms: 1.59x faster                                                |
| async_tree_none_tg         | 431 ms                                                       | 272 ms: 1.59x faster                                                |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 503 ms: 1.38x faster                                                |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 506 ms: 1.38x faster                                                |
| deepcopy                   | 368 us                                                       | 281 us: 1.31x faster                                                |
| deepcopy_memo              | 36.8 us                                                      | 28.3 us: 1.30x faster                                               |
| richards                   | 45.7 ms                                                      | 35.8 ms: 1.28x faster                                               |
| generators                 | 37.4 ms                                                      | 29.5 ms: 1.27x faster                                               |
| richards_super             | 51.3 ms                                                      | 41.8 ms: 1.23x faster                                               |
| comprehensions             | 21.9 us                                                      | 18.4 us: 1.19x faster                                               |
| float                      | 76.6 ms                                                      | 66.0 ms: 1.16x faster                                               |
| go                         | 150 ms                                                       | 131 ms: 1.14x faster                                                |
| logging_format             | 7.48 us                                                      | 6.62 us: 1.13x faster                                               |
| deepcopy_reduce            | 3.37 us                                                      | 2.99 us: 1.13x faster                                               |
| dulwich_log                | 65.4 ms                                                      | 58.7 ms: 1.11x faster                                               |
| pathlib                    | 18.9 ms                                                      | 17.0 ms: 1.11x faster                                               |
| logging_simple             | 6.71 us                                                      | 6.05 us: 1.11x faster                                               |
| regex_dna                  | 239 ms                                                       | 220 ms: 1.08x faster                                                |
| deltablue                  | 3.24 ms                                                      | 3.01 ms: 1.08x faster                                               |
| chaos                      | 64.0 ms                                                      | 59.6 ms: 1.07x faster                                               |
| scimark_monte_carlo        | 69.0 ms                                                      | 64.3 ms: 1.07x faster                                               |
| xml_etree_iterparse        | 103 ms                                                       | 95.9 ms: 1.07x faster                                               |
| sympy_sum                  | 162 ms                                                       | 152 ms: 1.06x faster                                                |
| sympy_integrate            | 23.9 ms                                                      | 22.5 ms: 1.06x faster                                               |
| scimark_sor                | 109 ms                                                       | 103 ms: 1.06x faster                                                |
| xml_etree_parse            | 144 ms                                                       | 136 ms: 1.06x faster                                                |
| django_template            | 38.2 ms                                                      | 36.2 ms: 1.05x faster                                               |
| regex_compile              | 144 ms                                                       | 137 ms: 1.05x faster                                                |
| xml_etree_generate         | 86.1 ms                                                      | 82.9 ms: 1.04x faster                                               |
| raytrace                   | 298 ms                                                       | 288 ms: 1.03x faster                                                |
| sympy_str                  | 302 ms                                                       | 292 ms: 1.03x faster                                                |
| scimark_lu                 | 98.8 ms                                                      | 95.7 ms: 1.03x faster                                               |
| pyflate                    | 439 ms                                                       | 425 ms: 1.03x faster                                                |
| coroutines                 | 23.0 ms                                                      | 22.3 ms: 1.03x faster                                               |
| pidigits                   | 265 ms                                                       | 258 ms: 1.03x faster                                                |
| regex_v8                   | 23.6 ms                                                      | 23.0 ms: 1.03x faster                                               |
| regex_effbot               | 3.57 ms                                                      | 3.49 ms: 1.02x faster                                               |
| tomli_loads                | 2.16 sec                                                     | 2.11 sec: 1.02x faster                                              |
| meteor_contest             | 128 ms                                                       | 126 ms: 1.02x faster                                                |
| pprint_pformat             | 1.65 sec                                                     | 1.64 sec: 1.01x faster                                              |
| xml_etree_process          | 58.4 ms                                                      | 58.0 ms: 1.01x faster                                               |
| 2to3                       | 285 ms                                                       | 286 ms: 1.00x slower                                                |
| sqlite_synth               | 2.77 us                                                      | 2.81 us: 1.01x slower                                               |
| docutils                   | 2.87 sec                                                     | 2.91 sec: 1.02x slower                                              |
| pycparser                  | 1.23 sec                                                     | 1.26 sec: 1.02x slower                                              |
| python_startup_no_site     | 8.64 ms                                                      | 8.85 ms: 1.02x slower                                               |
| unpickle_pure_python       | 210 us                                                       | 215 us: 1.03x slower                                                |
| json_loads                 | 24.4 us                                                      | 25.1 us: 1.03x slower                                               |
| sympy_expand               | 484 ms                                                       | 500 ms: 1.03x slower                                                |
| crypto_pyaes               | 80.3 ms                                                      | 83.3 ms: 1.04x slower                                               |
| json                       | 5.12 ms                                                      | 5.31 ms: 1.04x slower                                               |
| pickle_pure_python         | 318 us                                                       | 340 us: 1.07x slower                                                |
| nqueens                    | 89.9 ms                                                      | 96.6 ms: 1.08x slower                                               |
| hexiom                     | 5.96 ms                                                      | 6.52 ms: 1.09x slower                                               |
| json_dumps                 | 10.2 ms                                                      | 11.2 ms: 1.10x slower                                               |
| mako                       | 10.0 ms                                                      | 11.0 ms: 1.10x slower                                               |
| spectral_norm              | 91.6 ms                                                      | 102 ms: 1.12x slower                                                |
| typing_runtime_protocols   | 152 us                                                       | 172 us: 1.13x slower                                                |
| scimark_fft                | 301 ms                                                       | 343 ms: 1.14x slower                                                |
| async_generators           | 390 ms                                                       | 448 ms: 1.15x slower                                                |
| nbody                      | 88.0 ms                                                      | 102 ms: 1.16x slower                                                |
| telco                      | 6.96 ms                                                      | 8.14 ms: 1.17x slower                                               |
| coverage                   | 66.7 ms                                                      | 78.9 ms: 1.18x slower                                               |
| fannkuch                   | 350 ms                                                       | 437 ms: 1.25x slower                                                |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.44 ms: 1.29x slower                                               |
| python_startup             | 11.6 ms                                                      | 15.3 ms: 1.32x slower                                               |
| create_gc_cycles           | 1.59 ms                                                      | 2.83 ms: 1.78x slower                                               |
| gc_traversal               | 3.48 ms                                                      | 6.47 ms: 1.86x slower                                               |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                        |

Benchmark hidden because not significant (3): asyncio_websockets, logging_silent, pprint_safe_repr
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250628-3.15.0a0-6448067-JIT/bm-20250628-pythonperf2-x86_64-brandtbucher-jit_oz-3.15.0a0-6448067.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.053x faster

# HPT report

- Reliability score: 99.75% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.14x