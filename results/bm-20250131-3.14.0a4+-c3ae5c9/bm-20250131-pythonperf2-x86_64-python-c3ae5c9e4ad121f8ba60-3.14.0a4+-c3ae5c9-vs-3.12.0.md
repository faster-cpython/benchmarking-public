# Results vs. 3.12.0

- fork: python
- ref: c3ae5c9e4ad121f8ba60
- machine: linux-x86_64
- commit hash: c3ae5c9
- commit date: 2025-01-31
- overall geometric mean: 1.056x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250131-pythonperf2-x86_64-python-c3ae5c9e4ad121f8ba60-3.14.0a4+-c3ae5c9 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 279 ms: 1.02x faster                                                         |
| docutils       | 2.87 sec                                                     | 2.85 sec: 1.01x faster                                                       |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250131-pythonperf2-x86_64-python-c3ae5c9e4ad121f8ba60-3.14.0a4+-c3ae5c9 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 643 ms: 1.64x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 651 ms: 1.60x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 338 ms: 1.60x faster                                                         |
| async_tree_none            | 452 ms                                                       | 286 ms: 1.58x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 349 ms: 1.56x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 279 ms: 1.54x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 510 ms: 1.37x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 517 ms: 1.35x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.52x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250131-pythonperf2-x86_64-python-c3ae5c9e4ad121f8ba60-3.14.0a4+-c3ae5c9 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 69.7 ms: 1.10x faster                                                        |
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250131-pythonperf2-x86_64-python-c3ae5c9e4ad121f8ba60-3.14.0a4+-c3ae5c9 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.20 ms: 1.12x faster                                                        |
| regex_compile  | 144 ms                                                       | 134 ms: 1.08x faster                                                         |
| regex_dna      | 239 ms                                                       | 238 ms: 1.00x faster                                                         |
| regex_v8       | 23.6 ms                                                      | 26.0 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250131-pythonperf2-x86_64-python-c3ae5c9e4ad121f8ba60-3.14.0a4+-c3ae5c9 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 1.99 sec: 1.09x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 97.2 ms: 1.06x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 136 ms: 1.05x faster                                                         |
| xml_etree_generate   | 86.1 ms                                                      | 82.9 ms: 1.04x faster                                                        |
| unpickle_pure_python | 210 us                                                       | 205 us: 1.02x faster                                                         |
| xml_etree_process    | 58.4 ms                                                      | 57.9 ms: 1.01x faster                                                        |
| pickle_pure_python   | 318 us                                                       | 327 us: 1.03x slower                                                         |
| json_loads           | 24.4 us                                                      | 26.4 us: 1.09x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 11.6 ms: 1.13x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250131-pythonperf2-x86_64-python-c3ae5c9e4ad121f8ba60-3.14.0a4+-c3ae5c9 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.00 ms: 1.04x slower                                                        |
| python_startup         | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250131-pythonperf2-x86_64-python-c3ae5c9e4ad121f8ba60-3.14.0a4+-c3ae5c9 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 34.9 ms: 1.09x faster                                                        |
| mako            | 10.0 ms                                                      | 10.7 ms: 1.07x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250131-pythonperf2-x86_64-python-c3ae5c9e4ad121f8ba60-3.14.0a4+-c3ae5c9 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 643 ms: 1.64x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 651 ms: 1.60x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 338 ms: 1.60x faster                                                         |
| async_tree_none            | 452 ms                                                       | 286 ms: 1.58x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 349 ms: 1.56x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 279 ms: 1.54x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 510 ms: 1.37x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 517 ms: 1.35x faster                                                         |
| comprehensions             | 21.9 us                                                      | 16.6 us: 1.32x faster                                                        |
| deepcopy                   | 368 us                                                       | 281 us: 1.31x faster                                                         |
| generators                 | 37.4 ms                                                      | 29.0 ms: 1.29x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 29.7 us: 1.24x faster                                                        |
| go                         | 150 ms                                                       | 124 ms: 1.21x faster                                                         |
| pathlib                    | 18.9 ms                                                      | 15.6 ms: 1.21x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 2.90 us: 1.16x faster                                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 141 ms: 1.13x faster                                                         |
| regex_effbot               | 3.57 ms                                                      | 3.20 ms: 1.12x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 62.0 ms: 1.11x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 20.8 ms: 1.11x faster                                                        |
| raytrace                   | 298 ms                                                       | 271 ms: 1.10x faster                                                         |
| float                      | 76.6 ms                                                      | 69.7 ms: 1.10x faster                                                        |
| django_template            | 38.2 ms                                                      | 34.9 ms: 1.09x faster                                                        |
| logging_format             | 7.48 us                                                      | 6.84 us: 1.09x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 73.6 ms: 1.09x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 149 ms: 1.09x faster                                                         |
| tomli_loads                | 2.16 sec                                                     | 1.99 sec: 1.09x faster                                                       |
| spectral_norm              | 91.6 ms                                                      | 84.5 ms: 1.08x faster                                                        |
| chaos                      | 64.0 ms                                                      | 59.0 ms: 1.08x faster                                                        |
| regex_compile              | 144 ms                                                       | 134 ms: 1.08x faster                                                         |
| logging_simple             | 6.71 us                                                      | 6.23 us: 1.08x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 97.2 ms: 1.06x faster                                                        |
| sympy_str                  | 302 ms                                                       | 286 ms: 1.06x faster                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                      | 17.7 ms: 1.06x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 136 ms: 1.05x faster                                                         |
| mdp                        | 2.57 sec                                                     | 2.44 sec: 1.05x faster                                                       |
| sympy_integrate            | 23.9 ms                                                      | 22.8 ms: 1.05x faster                                                        |
| nqueens                    | 89.9 ms                                                      | 85.7 ms: 1.05x faster                                                        |
| bench_thread_pool          | 950 us                                                       | 907 us: 1.05x faster                                                         |
| scimark_lu                 | 98.8 ms                                                      | 94.6 ms: 1.04x faster                                                        |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                         |
| sqlglot_parse              | 1.38 ms                                                      | 1.32 ms: 1.04x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 82.9 ms: 1.04x faster                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.71 ms: 1.04x faster                                                        |
| meteor_contest             | 128 ms                                                       | 124 ms: 1.04x faster                                                         |
| pprint_pformat             | 1.65 sec                                                     | 1.60 sec: 1.03x faster                                                       |
| pprint_safe_repr           | 807 ms                                                       | 783 ms: 1.03x faster                                                         |
| sqlglot_normalize          | 116 ms                                                       | 113 ms: 1.02x faster                                                         |
| 2to3                       | 285 ms                                                       | 279 ms: 1.02x faster                                                         |
| sqlglot_optimize           | 57.5 ms                                                      | 56.2 ms: 1.02x faster                                                        |
| unpickle_pure_python       | 210 us                                                       | 205 us: 1.02x faster                                                         |
| pyflate                    | 439 ms                                                       | 429 ms: 1.02x faster                                                         |
| xml_etree_process          | 58.4 ms                                                      | 57.9 ms: 1.01x faster                                                        |
| scimark_sor                | 109 ms                                                       | 108 ms: 1.01x faster                                                         |
| docutils                   | 2.87 sec                                                     | 2.85 sec: 1.01x faster                                                       |
| regex_dna                  | 239 ms                                                       | 238 ms: 1.00x faster                                                         |
| hexiom                     | 5.96 ms                                                      | 5.97 ms: 1.00x slower                                                        |
| sympy_expand               | 484 ms                                                       | 489 ms: 1.01x slower                                                         |
| deltablue                  | 3.24 ms                                                      | 3.27 ms: 1.01x slower                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.81 us: 1.01x slower                                                        |
| dulwich_log                | 65.4 ms                                                      | 66.3 ms: 1.01x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 96.8 ns: 1.03x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 327 us: 1.03x slower                                                         |
| async_generators           | 390 ms                                                       | 404 ms: 1.03x slower                                                         |
| python_startup_no_site     | 8.64 ms                                                      | 9.00 ms: 1.04x slower                                                        |
| fannkuch                   | 350 ms                                                       | 365 ms: 1.04x slower                                                         |
| mako                       | 10.0 ms                                                      | 10.7 ms: 1.07x slower                                                        |
| json                       | 5.12 ms                                                      | 5.53 ms: 1.08x slower                                                        |
| json_loads                 | 24.4 us                                                      | 26.4 us: 1.09x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 26.0 ms: 1.10x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 167 us: 1.10x slower                                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.65 ms: 1.10x slower                                                        |
| telco                      | 6.96 ms                                                      | 7.86 ms: 1.13x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 11.6 ms: 1.13x slower                                                        |
| coverage                   | 66.7 ms                                                      | 76.7 ms: 1.15x slower                                                        |
| python_startup             | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.82 ms: 1.77x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 6.55 ms: 1.88x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 993 ms: 208.41x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (6): nbody, richards, scimark_fft, richards_super, asyncio_websockets, pycparser
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250131-3.14.0a4+-c3ae5c9/bm-20250131-pythonperf2-x86_64-python-c3ae5c9e4ad121f8ba60-3.14.0a4+-c3ae5c9.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.056x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.04x