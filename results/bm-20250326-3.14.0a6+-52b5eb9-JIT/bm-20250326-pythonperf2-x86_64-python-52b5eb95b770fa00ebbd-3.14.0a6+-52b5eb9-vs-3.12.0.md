# Results vs. 3.12.0

- fork: python
- ref: 52b5eb95b770fa00ebbd
- machine: linux-x86_64
- commit hash: 52b5eb9
- commit date: 2025-03-26
- overall geometric mean: 1.031x faster
- HPT reliability: 95.48%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-pythonperf2-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 289 ms: 1.01x slower                                                         |
| docutils       | 2.87 sec                                                     | 2.98 sec: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-pythonperf2-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 330 ms: 1.64x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 639 ms: 1.63x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 646 ms: 1.63x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 341 ms: 1.60x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 277 ms: 1.55x faster                                                         |
| async_tree_none            | 452 ms                                                       | 294 ms: 1.53x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 505 ms: 1.38x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 524 ms: 1.33x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.53x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-pythonperf2-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 64.6 ms: 1.19x faster                                                        |
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                         |
| nbody          | 88.0 ms                                                      | 93.0 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-pythonperf2-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.12 ms: 1.14x faster                                                        |
| regex_compile  | 144 ms                                                       | 137 ms: 1.05x faster                                                         |
| regex_dna      | 239 ms                                                       | 233 ms: 1.02x faster                                                         |
| regex_v8       | 23.6 ms                                                      | 23.2 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-pythonperf2-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 96.0 ms: 1.07x faster                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 81.4 ms: 1.06x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 137 ms: 1.05x faster                                                         |
| tomli_loads          | 2.16 sec                                                     | 2.07 sec: 1.04x faster                                                       |
| xml_etree_process    | 58.4 ms                                                      | 57.2 ms: 1.02x faster                                                        |
| unpickle_pure_python | 210 us                                                       | 217 us: 1.04x slower                                                         |
| pickle_pure_python   | 318 us                                                       | 344 us: 1.08x slower                                                         |
| json_loads           | 24.4 us                                                      | 26.7 us: 1.10x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 11.6 ms: 1.14x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-pythonperf2-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 10.5 ms: 1.22x slower                                                        |
| python_startup         | 11.6 ms                                                      | 16.4 ms: 1.41x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-pythonperf2-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 37.3 ms: 1.02x faster                                                        |
| mako            | 10.0 ms                                                      | 10.6 ms: 1.06x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.02x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-pythonperf2-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 330 ms: 1.64x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 639 ms: 1.63x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 646 ms: 1.63x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 341 ms: 1.60x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 277 ms: 1.55x faster                                                         |
| async_tree_none            | 452 ms                                                       | 294 ms: 1.53x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 505 ms: 1.38x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 524 ms: 1.33x faster                                                         |
| deepcopy_memo              | 36.8 us                                                      | 28.5 us: 1.29x faster                                                        |
| generators                 | 37.4 ms                                                      | 29.2 ms: 1.28x faster                                                        |
| deepcopy                   | 368 us                                                       | 289 us: 1.27x faster                                                         |
| float                      | 76.6 ms                                                      | 64.6 ms: 1.19x faster                                                        |
| richards                   | 45.7 ms                                                      | 39.3 ms: 1.16x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.12 ms: 1.14x faster                                                        |
| richards_super             | 51.3 ms                                                      | 45.2 ms: 1.13x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 2.97 us: 1.13x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 17.4 ms: 1.08x faster                                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 147 ms: 1.08x faster                                                         |
| coroutines                 | 23.0 ms                                                      | 21.4 ms: 1.08x faster                                                        |
| comprehensions             | 21.9 us                                                      | 20.4 us: 1.07x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 96.0 ms: 1.07x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 81.4 ms: 1.06x faster                                                        |
| logging_format             | 7.48 us                                                      | 7.07 us: 1.06x faster                                                        |
| regex_compile              | 144 ms                                                       | 137 ms: 1.05x faster                                                         |
| dulwich_log                | 65.4 ms                                                      | 62.1 ms: 1.05x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 154 ms: 1.05x faster                                                         |
| xml_etree_parse            | 144 ms                                                       | 137 ms: 1.05x faster                                                         |
| deltablue                  | 3.24 ms                                                      | 3.09 ms: 1.05x faster                                                        |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                         |
| logging_simple             | 6.71 us                                                      | 6.42 us: 1.04x faster                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.07 sec: 1.04x faster                                                       |
| sympy_integrate            | 23.9 ms                                                      | 23.3 ms: 1.03x faster                                                        |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.3 ms: 1.03x faster                                                        |
| go                         | 150 ms                                                       | 146 ms: 1.03x faster                                                         |
| django_template            | 38.2 ms                                                      | 37.3 ms: 1.02x faster                                                        |
| spectral_norm              | 91.6 ms                                                      | 89.5 ms: 1.02x faster                                                        |
| regex_dna                  | 239 ms                                                       | 233 ms: 1.02x faster                                                         |
| xml_etree_process          | 58.4 ms                                                      | 57.2 ms: 1.02x faster                                                        |
| sympy_str                  | 302 ms                                                       | 296 ms: 1.02x faster                                                         |
| regex_v8                   | 23.6 ms                                                      | 23.2 ms: 1.02x faster                                                        |
| mdp                        | 2.57 sec                                                     | 2.52 sec: 1.02x faster                                                       |
| logging_silent             | 94.4 ns                                                      | 93.5 ns: 1.01x faster                                                        |
| asyncio_websockets         | 387 ms                                                       | 384 ms: 1.01x faster                                                         |
| scimark_sor                | 109 ms                                                       | 108 ms: 1.00x faster                                                         |
| scimark_monte_carlo        | 69.0 ms                                                      | 68.8 ms: 1.00x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.67 sec: 1.01x slower                                                       |
| sqlite_synth               | 2.77 us                                                      | 2.80 us: 1.01x slower                                                        |
| 2to3                       | 285 ms                                                       | 289 ms: 1.01x slower                                                         |
| pprint_safe_repr           | 807 ms                                                       | 821 ms: 1.02x slower                                                         |
| meteor_contest             | 128 ms                                                       | 131 ms: 1.02x slower                                                         |
| pyflate                    | 439 ms                                                       | 451 ms: 1.03x slower                                                         |
| pycparser                  | 1.23 sec                                                     | 1.27 sec: 1.03x slower                                                       |
| bench_thread_pool          | 950 us                                                       | 980 us: 1.03x slower                                                         |
| unpickle_pure_python       | 210 us                                                       | 217 us: 1.04x slower                                                         |
| docutils                   | 2.87 sec                                                     | 2.98 sec: 1.04x slower                                                       |
| chaos                      | 64.0 ms                                                      | 66.5 ms: 1.04x slower                                                        |
| scimark_fft                | 301 ms                                                       | 313 ms: 1.04x slower                                                         |
| crypto_pyaes               | 80.3 ms                                                      | 83.6 ms: 1.04x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 94.1 ms: 1.05x slower                                                        |
| json                       | 5.12 ms                                                      | 5.40 ms: 1.05x slower                                                        |
| nbody                      | 88.0 ms                                                      | 93.0 ms: 1.06x slower                                                        |
| sympy_expand               | 484 ms                                                       | 515 ms: 1.06x slower                                                         |
| mako                       | 10.0 ms                                                      | 10.6 ms: 1.06x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 344 us: 1.08x slower                                                         |
| json_loads                 | 24.4 us                                                      | 26.7 us: 1.10x slower                                                        |
| async_generators           | 390 ms                                                       | 443 ms: 1.13x slower                                                         |
| json_dumps                 | 10.2 ms                                                      | 11.6 ms: 1.14x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.80 ms: 1.14x slower                                                        |
| telco                      | 6.96 ms                                                      | 7.94 ms: 1.14x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 177 us: 1.16x slower                                                         |
| fannkuch                   | 350 ms                                                       | 408 ms: 1.17x slower                                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.93 ms: 1.17x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 10.5 ms: 1.22x slower                                                        |
| coverage                   | 66.7 ms                                                      | 82.1 ms: 1.23x slower                                                        |
| python_startup             | 11.6 ms                                                      | 16.4 ms: 1.41x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.70 ms: 1.70x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 6.14 ms: 1.77x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 1.28 sec: 269.53x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.04x slower                                                                 |

Benchmark hidden because not significant (2): raytrace, scimark_lu
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250326-3.14.0a6+-52b5eb9-JIT/bm-20250326-pythonperf2-x86_64-python-52b5eb95b770fa00ebbd-3.14.0a6+-52b5eb9.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.031x faster

# HPT report

- Reliability score: 95.48% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x