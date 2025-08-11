# Results vs. 3.12.0

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: linux-x86_64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.036x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 287 ms: 1.01x slower                                                        |
| docutils       | 2.87 sec                                                     | 2.91 sec: 1.01x slower                                                      |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io              | 1.04 sec                                                     | 624 ms: 1.67x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 326 ms: 1.67x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 635 ms: 1.66x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 329 ms: 1.64x faster                                                        |
| async_tree_none            | 452 ms                                                       | 280 ms: 1.61x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 268 ms: 1.60x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 499 ms: 1.39x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 504 ms: 1.38x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.57x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 65.4 ms: 1.17x faster                                                       |
| pidigits       | 265 ms                                                       | 255 ms: 1.04x faster                                                        |
| nbody          | 88.0 ms                                                      | 101 ms: 1.15x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 133 ms: 1.08x faster                                                        |
| regex_dna      | 239 ms                                                       | 222 ms: 1.07x faster                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.84 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 1.91 sec: 1.13x faster                                                      |
| unpickle_pure_python | 210 us                                                       | 192 us: 1.09x faster                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 79.4 ms: 1.08x faster                                                       |
| xml_etree_process    | 58.4 ms                                                      | 55.1 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 97.2 ms: 1.06x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 138 ms: 1.04x faster                                                        |
| unpickle             | 14.8 us                                                      | 14.7 us: 1.01x faster                                                       |
| json_dumps           | 10.2 ms                                                      | 10.2 ms: 1.00x faster                                                       |
| json_loads           | 24.4 us                                                      | 25.3 us: 1.04x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 332 us: 1.04x slower                                                        |
| pickle_dict          | 32.5 us                                                      | 34.6 us: 1.06x slower                                                       |
| unpickle_list        | 4.66 us                                                      | 5.06 us: 1.09x slower                                                       |
| pickle               | 10.5 us                                                      | 12.2 us: 1.16x slower                                                       |
| pickle_list          | 4.43 us                                                      | 5.18 us: 1.17x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.83 ms: 1.02x slower                                                       |
| python_startup         | 11.6 ms                                                      | 15.3 ms: 1.32x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 34.9 ms: 1.09x faster                                                       |
| mako            | 10.0 ms                                                      | 9.86 ms: 1.01x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.05x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.29 sec: 1.99x faster                                                      |
| async_tree_io              | 1.04 sec                                                     | 624 ms: 1.67x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 326 ms: 1.67x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 635 ms: 1.66x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 329 ms: 1.64x faster                                                        |
| async_tree_none            | 452 ms                                                       | 280 ms: 1.61x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 268 ms: 1.60x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 499 ms: 1.39x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 504 ms: 1.38x faster                                                        |
| richards                   | 45.7 ms                                                      | 33.9 ms: 1.35x faster                                                       |
| deepcopy_memo              | 36.8 us                                                      | 27.5 us: 1.34x faster                                                       |
| deepcopy                   | 368 us                                                       | 279 us: 1.32x faster                                                        |
| richards_super             | 51.3 ms                                                      | 40.0 ms: 1.28x faster                                                       |
| comprehensions             | 21.9 us                                                      | 17.4 us: 1.26x faster                                                       |
| generators                 | 37.4 ms                                                      | 31.5 ms: 1.19x faster                                                       |
| go                         | 150 ms                                                       | 126 ms: 1.19x faster                                                        |
| float                      | 76.6 ms                                                      | 65.4 ms: 1.17x faster                                                       |
| spectral_norm              | 91.6 ms                                                      | 78.6 ms: 1.17x faster                                                       |
| logging_format             | 7.48 us                                                      | 6.49 us: 1.15x faster                                                       |
| deltablue                  | 3.24 ms                                                      | 2.84 ms: 1.14x faster                                                       |
| pathlib                    | 18.9 ms                                                      | 16.7 ms: 1.13x faster                                                       |
| logging_simple             | 6.71 us                                                      | 5.93 us: 1.13x faster                                                       |
| tomli_loads                | 2.16 sec                                                     | 1.91 sec: 1.13x faster                                                      |
| deepcopy_reduce            | 3.37 us                                                      | 2.99 us: 1.13x faster                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.50 sec: 1.10x faster                                                      |
| pprint_safe_repr           | 807 ms                                                       | 733 ms: 1.10x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 62.8 ms: 1.10x faster                                                       |
| dulwich_log                | 65.4 ms                                                      | 59.5 ms: 1.10x faster                                                       |
| django_template            | 38.2 ms                                                      | 34.9 ms: 1.09x faster                                                       |
| unpickle_pure_python       | 210 us                                                       | 192 us: 1.09x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 79.4 ms: 1.08x faster                                                       |
| unpack_sequence            | 53.2 ns                                                      | 49.0 ns: 1.08x faster                                                       |
| regex_compile              | 144 ms                                                       | 133 ms: 1.08x faster                                                        |
| pyflate                    | 439 ms                                                       | 405 ms: 1.08x faster                                                        |
| chaos                      | 64.0 ms                                                      | 59.4 ms: 1.08x faster                                                       |
| regex_dna                  | 239 ms                                                       | 222 ms: 1.07x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 151 ms: 1.07x faster                                                        |
| scimark_sor                | 109 ms                                                       | 102 ms: 1.07x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 22.4 ms: 1.07x faster                                                       |
| meteor_contest             | 128 ms                                                       | 121 ms: 1.06x faster                                                        |
| xml_etree_process          | 58.4 ms                                                      | 55.1 ms: 1.06x faster                                                       |
| raytrace                   | 298 ms                                                       | 281 ms: 1.06x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 97.2 ms: 1.06x faster                                                       |
| xml_etree_parse            | 144 ms                                                       | 138 ms: 1.04x faster                                                        |
| pidigits                   | 265 ms                                                       | 255 ms: 1.04x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 95.1 ms: 1.04x faster                                                       |
| sympy_str                  | 302 ms                                                       | 292 ms: 1.03x faster                                                        |
| logging_silent             | 94.4 ns                                                      | 91.8 ns: 1.03x faster                                                       |
| asyncio_tcp                | 378 ms                                                       | 369 ms: 1.03x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 78.4 ms: 1.02x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 22.7 ms: 1.01x faster                                                       |
| mako                       | 10.0 ms                                                      | 9.86 ms: 1.01x faster                                                       |
| unpickle                   | 14.8 us                                                      | 14.7 us: 1.01x faster                                                       |
| json_dumps                 | 10.2 ms                                                      | 10.2 ms: 1.00x faster                                                       |
| 2to3                       | 285 ms                                                       | 287 ms: 1.01x slower                                                        |
| docutils                   | 2.87 sec                                                     | 2.91 sec: 1.01x slower                                                      |
| scimark_fft                | 301 ms                                                       | 306 ms: 1.01x slower                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.83 us: 1.02x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 8.83 ms: 1.02x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.17 ms: 1.04x slower                                                       |
| bench_thread_pool          | 950 us                                                       | 984 us: 1.04x slower                                                        |
| json_loads                 | 24.4 us                                                      | 25.3 us: 1.04x slower                                                       |
| sympy_expand               | 484 ms                                                       | 503 ms: 1.04x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 93.5 ms: 1.04x slower                                                       |
| fannkuch                   | 350 ms                                                       | 364 ms: 1.04x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 332 us: 1.04x slower                                                        |
| pickle_dict                | 32.5 us                                                      | 34.6 us: 1.06x slower                                                       |
| json                       | 5.12 ms                                                      | 5.45 ms: 1.06x slower                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.84 ms: 1.08x slower                                                       |
| unpickle_list              | 4.66 us                                                      | 5.06 us: 1.09x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 169 us: 1.12x slower                                                        |
| async_generators           | 390 ms                                                       | 442 ms: 1.13x slower                                                        |
| nbody                      | 88.0 ms                                                      | 101 ms: 1.15x slower                                                        |
| pickle                     | 10.5 us                                                      | 12.2 us: 1.16x slower                                                       |
| pickle_list                | 4.43 us                                                      | 5.18 us: 1.17x slower                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.99 ms: 1.19x slower                                                       |
| coverage                   | 66.7 ms                                                      | 82.7 ms: 1.24x slower                                                       |
| python_startup             | 11.6 ms                                                      | 15.3 ms: 1.32x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.92 ms: 1.84x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 6.55 ms: 1.88x slower                                                       |
| telco                      | 6.96 ms                                                      | 160 ms: 22.91x slower                                                       |
| bench_mp_pool              | 4.76 ms                                                      | 1.61 sec: 337.58x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.04x slower                                                                |

Benchmark hidden because not significant (4): asyncio_websockets, pycparser, asyncio_tcp_ssl, regex_v8
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.036x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.14x