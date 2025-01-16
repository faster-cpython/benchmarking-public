# Results vs. 3.12.0

- fork: mdboom
- ref: tail_call_no_preserv
- machine: linux-x86_64
- commit hash: 09f3d0f
- commit date: 2025-01-16
- overall geometric mean: 1.046x faster
- HPT reliability: 95.61%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4+-09f3d0f |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 282 ms: 1.01x faster                                                         |
| docutils       | 2.87 sec                                                     | 2.89 sec: 1.01x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4+-09f3d0f |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 621 ms: 1.70x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 323 ms: 1.67x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 629 ms: 1.66x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 266 ms: 1.62x faster                                                         |
| async_tree_none            | 452 ms                                                       | 283 ms: 1.60x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 347 ms: 1.57x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 522 ms: 1.34x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 543 ms: 1.28x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.55x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4+-09f3d0f |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 71.9 ms: 1.07x faster                                                        |
| nbody          | 88.0 ms                                                      | 89.2 ms: 1.01x slower                                                        |
| pidigits       | 265 ms                                                       | 286 ms: 1.08x slower                                                         |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4+-09f3d0f |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.00 ms: 1.19x faster                                                        |
| regex_dna      | 239 ms                                                       | 223 ms: 1.07x faster                                                         |
| regex_compile  | 144 ms                                                       | 138 ms: 1.04x faster                                                         |
| regex_v8       | 23.6 ms                                                      | 27.2 ms: 1.15x slower                                                        |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4+-09f3d0f |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 80.9 ms: 1.07x faster                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.06 sec: 1.05x faster                                                       |
| xml_etree_process    | 58.4 ms                                                      | 57.6 ms: 1.01x faster                                                        |
| pickle_pure_python   | 318 us                                                       | 325 us: 1.02x slower                                                         |
| xml_etree_iterparse  | 103 ms                                                       | 105 ms: 1.02x slower                                                         |
| unpickle_pure_python | 210 us                                                       | 216 us: 1.03x slower                                                         |
| json_loads           | 24.4 us                                                      | 25.2 us: 1.03x slower                                                        |
| xml_etree_parse      | 144 ms                                                       | 161 ms: 1.12x slower                                                         |
| json_dumps           | 10.2 ms                                                      | 11.7 ms: 1.14x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4+-09f3d0f |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.06 ms: 1.05x slower                                                        |
| python_startup         | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4+-09f3d0f |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 37.2 ms: 1.03x faster                                                        |
| mako            | 10.0 ms                                                      | 11.3 ms: 1.13x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.05x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4+-09f3d0f |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 621 ms: 1.70x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 323 ms: 1.67x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 629 ms: 1.66x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 266 ms: 1.62x faster                                                         |
| async_tree_none            | 452 ms                                                       | 283 ms: 1.60x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 347 ms: 1.57x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 522 ms: 1.34x faster                                                         |
| deepcopy                   | 368 us                                                       | 279 us: 1.32x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 543 ms: 1.28x faster                                                         |
| deepcopy_memo              | 36.8 us                                                      | 28.9 us: 1.27x faster                                                        |
| comprehensions             | 21.9 us                                                      | 17.4 us: 1.26x faster                                                        |
| generators                 | 37.4 ms                                                      | 30.6 ms: 1.22x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 57.5 ms: 1.20x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 15.8 ms: 1.20x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 2.82 us: 1.19x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.00 ms: 1.19x faster                                                        |
| go                         | 150 ms                                                       | 128 ms: 1.17x faster                                                         |
| raytrace                   | 298 ms                                                       | 267 ms: 1.12x faster                                                         |
| scimark_lu                 | 98.8 ms                                                      | 89.2 ms: 1.11x faster                                                        |
| scimark_fft                | 301 ms                                                       | 272 ms: 1.10x faster                                                         |
| sqlalchemy_declarative     | 159 ms                                                       | 145 ms: 1.10x faster                                                         |
| logging_simple             | 6.71 us                                                      | 6.10 us: 1.10x faster                                                        |
| logging_format             | 7.48 us                                                      | 6.83 us: 1.10x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 150 ms: 1.08x faster                                                         |
| regex_dna                  | 239 ms                                                       | 223 ms: 1.07x faster                                                         |
| float                      | 76.6 ms                                                      | 71.9 ms: 1.07x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 80.9 ms: 1.07x faster                                                        |
| sqlalchemy_imperative      | 18.7 ms                                                      | 17.7 ms: 1.06x faster                                                        |
| richards                   | 45.7 ms                                                      | 43.3 ms: 1.06x faster                                                        |
| logging_silent             | 94.4 ns                                                      | 89.9 ns: 1.05x faster                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.06 sec: 1.05x faster                                                       |
| scimark_sor                | 109 ms                                                       | 104 ms: 1.05x faster                                                         |
| chaos                      | 64.0 ms                                                      | 61.4 ms: 1.04x faster                                                        |
| regex_compile              | 144 ms                                                       | 138 ms: 1.04x faster                                                         |
| sympy_integrate            | 23.9 ms                                                      | 23.0 ms: 1.04x faster                                                        |
| sympy_str                  | 302 ms                                                       | 292 ms: 1.04x faster                                                         |
| coroutines                 | 23.0 ms                                                      | 22.3 ms: 1.03x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 78.1 ms: 1.03x faster                                                        |
| richards_super             | 51.3 ms                                                      | 49.9 ms: 1.03x faster                                                        |
| django_template            | 38.2 ms                                                      | 37.2 ms: 1.03x faster                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.10 ms: 1.03x faster                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.35 ms: 1.02x faster                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.74 ms: 1.02x faster                                                        |
| bench_thread_pool          | 950 us                                                       | 930 us: 1.02x faster                                                         |
| spectral_norm              | 91.6 ms                                                      | 90.0 ms: 1.02x faster                                                        |
| pyflate                    | 439 ms                                                       | 431 ms: 1.02x faster                                                         |
| xml_etree_process          | 58.4 ms                                                      | 57.6 ms: 1.01x faster                                                        |
| 2to3                       | 285 ms                                                       | 282 ms: 1.01x faster                                                         |
| docutils                   | 2.87 sec                                                     | 2.89 sec: 1.01x slower                                                       |
| pprint_safe_repr           | 807 ms                                                       | 817 ms: 1.01x slower                                                         |
| asyncio_websockets         | 387 ms                                                       | 392 ms: 1.01x slower                                                         |
| nbody                      | 88.0 ms                                                      | 89.2 ms: 1.01x slower                                                        |
| json                       | 5.12 ms                                                      | 5.22 ms: 1.02x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 325 us: 1.02x slower                                                         |
| pycparser                  | 1.23 sec                                                     | 1.26 sec: 1.02x slower                                                       |
| sqlite_synth               | 2.77 us                                                      | 2.84 us: 1.02x slower                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 105 ms: 1.02x slower                                                         |
| hexiom                     | 5.96 ms                                                      | 6.12 ms: 1.03x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 3.33 ms: 1.03x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 216 us: 1.03x slower                                                         |
| mdp                        | 2.57 sec                                                     | 2.65 sec: 1.03x slower                                                       |
| sympy_expand               | 484 ms                                                       | 500 ms: 1.03x slower                                                         |
| json_loads                 | 24.4 us                                                      | 25.2 us: 1.03x slower                                                        |
| sqlglot_normalize          | 116 ms                                                       | 120 ms: 1.03x slower                                                         |
| sqlglot_optimize           | 57.5 ms                                                      | 59.6 ms: 1.04x slower                                                        |
| meteor_contest             | 128 ms                                                       | 133 ms: 1.04x slower                                                         |
| fannkuch                   | 350 ms                                                       | 366 ms: 1.05x slower                                                         |
| nqueens                    | 89.9 ms                                                      | 94.1 ms: 1.05x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 9.06 ms: 1.05x slower                                                        |
| pidigits                   | 265 ms                                                       | 286 ms: 1.08x slower                                                         |
| async_generators           | 390 ms                                                       | 429 ms: 1.10x slower                                                         |
| xml_etree_parse            | 144 ms                                                       | 161 ms: 1.12x slower                                                         |
| mako                       | 10.0 ms                                                      | 11.3 ms: 1.13x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 172 us: 1.14x slower                                                         |
| coverage                   | 66.7 ms                                                      | 75.9 ms: 1.14x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 11.7 ms: 1.14x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 27.2 ms: 1.15x slower                                                        |
| telco                      | 6.96 ms                                                      | 8.03 ms: 1.15x slower                                                        |
| python_startup             | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 5.34 ms: 1.53x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.89 ms: 1.82x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 1.36 sec: 285.96x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                                 |

Benchmark hidden because not significant (2): pprint_pformat, dulwich_log
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250116-3.14.0a4+-09f3d0f-CLANG/bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4+-09f3d0f.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.046x faster

# HPT report

- Reliability score: 95.61% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x