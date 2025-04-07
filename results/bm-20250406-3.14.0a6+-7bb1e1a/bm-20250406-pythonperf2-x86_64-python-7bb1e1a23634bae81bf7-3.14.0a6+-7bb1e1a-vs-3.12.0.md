# Results vs. 3.12.0

- fork: python
- ref: 7bb1e1a23634bae81bf7
- machine: linux-x86_64
- commit hash: 7bb1e1a
- commit date: 2025-04-06
- overall geometric mean: 1.061x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250406-pythonperf2-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 275 ms: 1.04x faster                                                         |
| docutils       | 2.87 sec                                                     | 2.86 sec: 1.00x faster                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250406-pythonperf2-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization     | 544 ms                                                       | 328 ms: 1.66x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 636 ms: 1.66x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 629 ms: 1.66x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 335 ms: 1.61x faster                                                         |
| async_tree_none            | 452 ms                                                       | 284 ms: 1.59x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 275 ms: 1.57x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 507 ms: 1.38x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 509 ms: 1.37x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.56x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250406-pythonperf2-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 69.1 ms: 1.11x faster                                                        |
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                         |
| nbody          | 88.0 ms                                                      | 93.9 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250406-pythonperf2-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.03 ms: 1.18x faster                                                        |
| regex_compile  | 144 ms                                                       | 134 ms: 1.08x faster                                                         |
| regex_dna      | 239 ms                                                       | 232 ms: 1.03x faster                                                         |
| regex_v8       | 23.6 ms                                                      | 24.4 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250406-pythonperf2-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 95.5 ms: 1.08x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 135 ms: 1.06x faster                                                         |
| tomli_loads          | 2.16 sec                                                     | 2.05 sec: 1.05x faster                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 84.3 ms: 1.02x faster                                                        |
| xml_etree_process    | 58.4 ms                                                      | 59.6 ms: 1.02x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 215 us: 1.03x slower                                                         |
| pickle_pure_python   | 318 us                                                       | 332 us: 1.04x slower                                                         |
| json_loads           | 24.4 us                                                      | 26.7 us: 1.10x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 11.3 ms: 1.10x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250406-pythonperf2-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 10.5 ms: 1.21x slower                                                        |
| python_startup         | 11.6 ms                                                      | 16.4 ms: 1.41x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250406-pythonperf2-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.8 ms: 1.06x faster                                                        |
| mako            | 10.0 ms                                                      | 10.9 ms: 1.09x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250406-pythonperf2-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.29 sec: 1.99x faster                                                       |
| async_tree_memoization     | 544 ms                                                       | 328 ms: 1.66x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 636 ms: 1.66x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 629 ms: 1.66x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 335 ms: 1.61x faster                                                         |
| async_tree_none            | 452 ms                                                       | 284 ms: 1.59x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 275 ms: 1.57x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 507 ms: 1.38x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 509 ms: 1.37x faster                                                         |
| generators                 | 37.4 ms                                                      | 28.1 ms: 1.33x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 28.0 us: 1.32x faster                                                        |
| deepcopy                   | 368 us                                                       | 281 us: 1.31x faster                                                         |
| comprehensions             | 21.9 us                                                      | 17.4 us: 1.26x faster                                                        |
| go                         | 150 ms                                                       | 124 ms: 1.21x faster                                                         |
| regex_effbot               | 3.57 ms                                                      | 3.03 ms: 1.18x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 2.90 us: 1.16x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 59.4 ms: 1.16x faster                                                        |
| float                      | 76.6 ms                                                      | 69.1 ms: 1.11x faster                                                        |
| logging_format             | 7.48 us                                                      | 6.81 us: 1.10x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.13 us: 1.09x faster                                                        |
| chaos                      | 64.0 ms                                                      | 58.5 ms: 1.09x faster                                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 146 ms: 1.09x faster                                                         |
| pathlib                    | 18.9 ms                                                      | 17.3 ms: 1.09x faster                                                        |
| raytrace                   | 298 ms                                                       | 273 ms: 1.09x faster                                                         |
| coroutines                 | 23.0 ms                                                      | 21.2 ms: 1.08x faster                                                        |
| regex_compile              | 144 ms                                                       | 134 ms: 1.08x faster                                                         |
| sympy_integrate            | 23.9 ms                                                      | 22.2 ms: 1.08x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 95.5 ms: 1.08x faster                                                        |
| django_template            | 38.2 ms                                                      | 35.8 ms: 1.06x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 135 ms: 1.06x faster                                                         |
| sympy_sum                  | 162 ms                                                       | 153 ms: 1.06x faster                                                         |
| sympy_str                  | 302 ms                                                       | 286 ms: 1.06x faster                                                         |
| tomli_loads                | 2.16 sec                                                     | 2.05 sec: 1.05x faster                                                       |
| spectral_norm              | 91.6 ms                                                      | 87.3 ms: 1.05x faster                                                        |
| dulwich_log                | 65.4 ms                                                      | 62.4 ms: 1.05x faster                                                        |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                         |
| pyflate                    | 439 ms                                                       | 422 ms: 1.04x faster                                                         |
| 2to3                       | 285 ms                                                       | 275 ms: 1.04x faster                                                         |
| pprint_pformat             | 1.65 sec                                                     | 1.59 sec: 1.04x faster                                                       |
| pprint_safe_repr           | 807 ms                                                       | 779 ms: 1.04x faster                                                         |
| scimark_sor                | 109 ms                                                       | 105 ms: 1.04x faster                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.1 ms: 1.03x faster                                                        |
| regex_dna                  | 239 ms                                                       | 232 ms: 1.03x faster                                                         |
| xml_etree_generate         | 86.1 ms                                                      | 84.3 ms: 1.02x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 79.1 ms: 1.02x faster                                                        |
| logging_silent             | 94.4 ns                                                      | 92.9 ns: 1.02x faster                                                        |
| meteor_contest             | 128 ms                                                       | 126 ms: 1.02x faster                                                         |
| docutils                   | 2.87 sec                                                     | 2.86 sec: 1.00x faster                                                       |
| deltablue                  | 3.24 ms                                                      | 3.25 ms: 1.00x slower                                                        |
| scimark_fft                | 301 ms                                                       | 303 ms: 1.01x slower                                                         |
| sympy_expand               | 484 ms                                                       | 488 ms: 1.01x slower                                                         |
| sqlite_synth               | 2.77 us                                                      | 2.82 us: 1.02x slower                                                        |
| bench_thread_pool          | 950 us                                                       | 968 us: 1.02x slower                                                         |
| richards_super             | 51.3 ms                                                      | 52.4 ms: 1.02x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 59.6 ms: 1.02x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 215 us: 1.03x slower                                                         |
| regex_v8                   | 23.6 ms                                                      | 24.4 ms: 1.03x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.16 ms: 1.03x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 332 us: 1.04x slower                                                         |
| nqueens                    | 89.9 ms                                                      | 93.7 ms: 1.04x slower                                                        |
| async_generators           | 390 ms                                                       | 411 ms: 1.05x slower                                                         |
| fannkuch                   | 350 ms                                                       | 371 ms: 1.06x slower                                                         |
| nbody                      | 88.0 ms                                                      | 93.9 ms: 1.07x slower                                                        |
| json                       | 5.12 ms                                                      | 5.50 ms: 1.07x slower                                                        |
| mako                       | 10.0 ms                                                      | 10.9 ms: 1.09x slower                                                        |
| json_loads                 | 24.4 us                                                      | 26.7 us: 1.10x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 11.3 ms: 1.10x slower                                                        |
| telco                      | 6.96 ms                                                      | 7.85 ms: 1.13x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 171 us: 1.13x slower                                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.77 ms: 1.13x slower                                                        |
| coverage                   | 66.7 ms                                                      | 79.8 ms: 1.20x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 10.5 ms: 1.21x slower                                                        |
| python_startup             | 11.6 ms                                                      | 16.4 ms: 1.41x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.79 ms: 1.75x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 6.39 ms: 1.84x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 1.19 sec: 250.39x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (4): scimark_lu, pycparser, asyncio_websockets, richards
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250406-3.14.0a6+-7bb1e1a/bm-20250406-pythonperf2-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.061x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.05x