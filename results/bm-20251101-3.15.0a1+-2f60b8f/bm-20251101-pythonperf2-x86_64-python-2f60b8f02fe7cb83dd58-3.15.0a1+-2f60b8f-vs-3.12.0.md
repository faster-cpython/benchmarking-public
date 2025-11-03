# Results vs. 3.12.0

- fork: python
- ref: 2f60b8f02fe7cb83dd58
- machine: linux-x86_64
- commit hash: 2f60b8f
- commit date: 2025-11-01
- overall geometric mean: 1.061x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 276 ms: 1.03x faster                                                         |
| docutils       | 2.87 sec                                                     | 2.84 sec: 1.01x faster                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 558 ms: 1.89x faster                                                         |
| async_tree_none            | 452 ms                                                       | 243 ms: 1.86x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 568 ms: 1.83x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 296 ms: 1.83x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 301 ms: 1.80x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 249 ms: 1.73x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 474 ms: 1.47x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 476 ms: 1.46x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.73x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 64.8 ms: 1.18x faster                                                        |
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                         |
| nbody          | 88.0 ms                                                      | 89.7 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 132 ms: 1.09x faster                                                         |
| regex_dna      | 239 ms                                                       | 222 ms: 1.08x faster                                                         |
| regex_effbot   | 3.57 ms                                                      | 3.48 ms: 1.03x faster                                                        |
| regex_v8       | 23.6 ms                                                      | 23.8 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 86.2 ms: 1.19x faster                                                        |
| tomli_loads          | 2.16 sec                                                     | 1.97 sec: 1.10x faster                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 81.1 ms: 1.06x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 136 ms: 1.06x faster                                                         |
| pickle_dict          | 32.5 us                                                      | 31.8 us: 1.02x faster                                                        |
| unpickle_pure_python | 210 us                                                       | 206 us: 1.02x faster                                                         |
| xml_etree_process    | 58.4 ms                                                      | 57.4 ms: 1.02x faster                                                        |
| json_dumps           | 10.2 ms                                                      | 10.1 ms: 1.01x faster                                                        |
| pickle_pure_python   | 318 us                                                       | 322 us: 1.01x slower                                                         |
| json_loads           | 24.4 us                                                      | 25.2 us: 1.04x slower                                                        |
| unpickle_list        | 4.66 us                                                      | 5.04 us: 1.08x slower                                                        |
| pickle_list          | 4.43 us                                                      | 4.88 us: 1.10x slower                                                        |
| pickle               | 10.5 us                                                      | 12.3 us: 1.17x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.67 ms: 1.00x slower                                                        |
| python_startup         | 11.6 ms                                                      | 15.0 ms: 1.29x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.14x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 34.9 ms: 1.09x faster                                                        |
| mako            | 10.0 ms                                                      | 10.7 ms: 1.07x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.25 sec: 2.05x faster                                                       |
| async_tree_io_tg           | 1.05 sec                                                     | 558 ms: 1.89x faster                                                         |
| async_tree_none            | 452 ms                                                       | 243 ms: 1.86x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 568 ms: 1.83x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 296 ms: 1.83x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 301 ms: 1.80x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 249 ms: 1.73x faster                                                         |
| deepcopy_memo              | 36.8 us                                                      | 24.9 us: 1.48x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 474 ms: 1.47x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 476 ms: 1.46x faster                                                         |
| deepcopy                   | 368 us                                                       | 264 us: 1.40x faster                                                         |
| comprehensions             | 21.9 us                                                      | 16.2 us: 1.35x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 14.8 ms: 1.28x faster                                                        |
| go                         | 150 ms                                                       | 118 ms: 1.27x faster                                                         |
| generators                 | 37.4 ms                                                      | 29.8 ms: 1.25x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 86.2 ms: 1.19x faster                                                        |
| float                      | 76.6 ms                                                      | 64.8 ms: 1.18x faster                                                        |
| unpack_sequence            | 53.2 ns                                                      | 45.3 ns: 1.17x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 59.1 ms: 1.17x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 2.90 us: 1.16x faster                                                        |
| logging_format             | 7.48 us                                                      | 6.49 us: 1.15x faster                                                        |
| chaos                      | 64.0 ms                                                      | 55.7 ms: 1.15x faster                                                        |
| logging_simple             | 6.71 us                                                      | 5.90 us: 1.14x faster                                                        |
| raytrace                   | 298 ms                                                       | 268 ms: 1.11x faster                                                         |
| dulwich_log                | 65.4 ms                                                      | 59.0 ms: 1.11x faster                                                        |
| spectral_norm              | 91.6 ms                                                      | 82.9 ms: 1.11x faster                                                        |
| scimark_sor                | 109 ms                                                       | 98.6 ms: 1.10x faster                                                        |
| tomli_loads                | 2.16 sec                                                     | 1.97 sec: 1.10x faster                                                       |
| django_template            | 38.2 ms                                                      | 34.9 ms: 1.09x faster                                                        |
| regex_compile              | 144 ms                                                       | 132 ms: 1.09x faster                                                         |
| sympy_integrate            | 23.9 ms                                                      | 21.9 ms: 1.09x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 149 ms: 1.09x faster                                                         |
| pyflate                    | 439 ms                                                       | 405 ms: 1.08x faster                                                         |
| scimark_lu                 | 98.8 ms                                                      | 91.6 ms: 1.08x faster                                                        |
| meteor_contest             | 128 ms                                                       | 119 ms: 1.08x faster                                                         |
| regex_dna                  | 239 ms                                                       | 222 ms: 1.08x faster                                                         |
| crypto_pyaes               | 80.3 ms                                                      | 74.9 ms: 1.07x faster                                                        |
| scimark_fft                | 301 ms                                                       | 281 ms: 1.07x faster                                                         |
| xml_etree_generate         | 86.1 ms                                                      | 81.1 ms: 1.06x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 136 ms: 1.06x faster                                                         |
| pprint_pformat             | 1.65 sec                                                     | 1.57 sec: 1.05x faster                                                       |
| sympy_str                  | 302 ms                                                       | 287 ms: 1.05x faster                                                         |
| hexiom                     | 5.96 ms                                                      | 5.67 ms: 1.05x faster                                                        |
| pprint_safe_repr           | 807 ms                                                       | 771 ms: 1.05x faster                                                         |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                         |
| deltablue                  | 3.24 ms                                                      | 3.12 ms: 1.04x faster                                                        |
| richards                   | 45.7 ms                                                      | 44.2 ms: 1.04x faster                                                        |
| 2to3                       | 285 ms                                                       | 276 ms: 1.03x faster                                                         |
| regex_effbot               | 3.57 ms                                                      | 3.48 ms: 1.03x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 22.4 ms: 1.03x faster                                                        |
| richards_super             | 51.3 ms                                                      | 50.1 ms: 1.02x faster                                                        |
| pickle_dict                | 32.5 us                                                      | 31.8 us: 1.02x faster                                                        |
| asyncio_tcp                | 378 ms                                                       | 370 ms: 1.02x faster                                                         |
| bench_thread_pool          | 950 us                                                       | 929 us: 1.02x faster                                                         |
| unpickle_pure_python       | 210 us                                                       | 206 us: 1.02x faster                                                         |
| xml_etree_process          | 58.4 ms                                                      | 57.4 ms: 1.02x faster                                                        |
| logging_silent             | 94.4 ns                                                      | 93.0 ns: 1.01x faster                                                        |
| docutils                   | 2.87 sec                                                     | 2.84 sec: 1.01x faster                                                       |
| pycparser                  | 1.23 sec                                                     | 1.22 sec: 1.01x faster                                                       |
| json_dumps                 | 10.2 ms                                                      | 10.1 ms: 1.01x faster                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 8.67 ms: 1.00x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 23.8 ms: 1.01x slower                                                        |
| sympy_expand               | 484 ms                                                       | 490 ms: 1.01x slower                                                         |
| pickle_pure_python         | 318 us                                                       | 322 us: 1.01x slower                                                         |
| nbody                      | 88.0 ms                                                      | 89.7 ms: 1.02x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 91.7 ms: 1.02x slower                                                        |
| fannkuch                   | 350 ms                                                       | 358 ms: 1.02x slower                                                         |
| sqlite_synth               | 2.77 us                                                      | 2.84 us: 1.02x slower                                                        |
| json_loads                 | 24.4 us                                                      | 25.2 us: 1.04x slower                                                        |
| json                       | 5.12 ms                                                      | 5.34 ms: 1.04x slower                                                        |
| asyncio_websockets         | 387 ms                                                       | 409 ms: 1.06x slower                                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.49 ms: 1.07x slower                                                        |
| mako                       | 10.0 ms                                                      | 10.7 ms: 1.07x slower                                                        |
| unpickle_list              | 4.66 us                                                      | 5.04 us: 1.08x slower                                                        |
| async_generators           | 390 ms                                                       | 426 ms: 1.09x slower                                                         |
| typing_runtime_protocols   | 152 us                                                       | 167 us: 1.10x slower                                                         |
| pickle_list                | 4.43 us                                                      | 4.88 us: 1.10x slower                                                        |
| pickle                     | 10.5 us                                                      | 12.3 us: 1.17x slower                                                        |
| coverage                   | 66.7 ms                                                      | 79.9 ms: 1.20x slower                                                        |
| python_startup             | 11.6 ms                                                      | 15.0 ms: 1.29x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 6.14 ms: 1.76x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.86 ms: 1.80x slower                                                        |
| telco                      | 6.96 ms                                                      | 152 ms: 21.85x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 2.57 sec: 538.85x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                                 |

Benchmark hidden because not significant (2): asyncio_tcp_ssl, unpickle
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20251101-3.15.0a1+-2f60b8f/bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.061x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.13x