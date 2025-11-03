# Results vs. 3.12.0

- fork: python
- ref: 2f60b8f02fe7cb83dd58
- machine: linux-x86_64
- commit hash: 2f60b8f
- commit date: 2025-11-01
- overall geometric mean: 1.056x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 280 ms: 1.02x faster                                                         |
| docutils       | 2.87 sec                                                     | 2.88 sec: 1.00x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 576 ms: 1.83x faster                                                         |
| async_tree_none            | 452 ms                                                       | 248 ms: 1.82x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 578 ms: 1.80x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 306 ms: 1.78x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 315 ms: 1.72x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 255 ms: 1.69x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 476 ms: 1.46x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 480 ms: 1.45x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.69x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 65.3 ms: 1.17x faster                                                        |
| pidigits       | 265 ms                                                       | 255 ms: 1.04x faster                                                         |
| nbody          | 88.0 ms                                                      | 92.7 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 132 ms: 1.09x faster                                                         |
| regex_dna      | 239 ms                                                       | 228 ms: 1.05x faster                                                         |
| regex_effbot   | 3.57 ms                                                      | 3.51 ms: 1.02x faster                                                        |
| regex_v8       | 23.6 ms                                                      | 23.5 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 85.4 ms: 1.20x faster                                                        |
| tomli_loads          | 2.16 sec                                                     | 1.90 sec: 1.14x faster                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 78.7 ms: 1.10x faster                                                        |
| unpickle_pure_python | 210 us                                                       | 194 us: 1.08x faster                                                         |
| xml_etree_parse      | 144 ms                                                       | 133 ms: 1.08x faster                                                         |
| xml_etree_process    | 58.4 ms                                                      | 55.4 ms: 1.05x faster                                                        |
| json_dumps           | 10.2 ms                                                      | 10.2 ms: 1.01x faster                                                        |
| json_loads           | 24.4 us                                                      | 25.0 us: 1.03x slower                                                        |
| pickle_dict          | 32.5 us                                                      | 33.6 us: 1.03x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 329 us: 1.03x slower                                                         |
| unpickle_list        | 4.66 us                                                      | 5.04 us: 1.08x slower                                                        |
| pickle_list          | 4.43 us                                                      | 4.98 us: 1.12x slower                                                        |
| pickle               | 10.5 us                                                      | 12.5 us: 1.18x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.74 ms: 1.01x slower                                                        |
| python_startup         | 11.6 ms                                                      | 15.0 ms: 1.29x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.14x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 34.8 ms: 1.10x faster                                                        |
| mako            | 10.0 ms                                                      | 9.74 ms: 1.03x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.06x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.27 sec: 2.02x faster                                                       |
| async_tree_io_tg           | 1.05 sec                                                     | 576 ms: 1.83x faster                                                         |
| async_tree_none            | 452 ms                                                       | 248 ms: 1.82x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 578 ms: 1.80x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 306 ms: 1.78x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 315 ms: 1.72x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 255 ms: 1.69x faster                                                         |
| deepcopy_memo              | 36.8 us                                                      | 24.0 us: 1.53x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 476 ms: 1.46x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 480 ms: 1.45x faster                                                         |
| deepcopy                   | 368 us                                                       | 267 us: 1.38x faster                                                         |
| comprehensions             | 21.9 us                                                      | 17.0 us: 1.29x faster                                                        |
| generators                 | 37.4 ms                                                      | 29.4 ms: 1.27x faster                                                        |
| go                         | 150 ms                                                       | 119 ms: 1.26x faster                                                         |
| pathlib                    | 18.9 ms                                                      | 15.1 ms: 1.25x faster                                                        |
| richards                   | 45.7 ms                                                      | 37.9 ms: 1.21x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 85.4 ms: 1.20x faster                                                        |
| float                      | 76.6 ms                                                      | 65.3 ms: 1.17x faster                                                        |
| richards_super             | 51.3 ms                                                      | 43.8 ms: 1.17x faster                                                        |
| logging_format             | 7.48 us                                                      | 6.44 us: 1.16x faster                                                        |
| logging_simple             | 6.71 us                                                      | 5.86 us: 1.14x faster                                                        |
| tomli_loads                | 2.16 sec                                                     | 1.90 sec: 1.14x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.97 us: 1.13x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.46 sec: 1.13x faster                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 61.6 ms: 1.12x faster                                                        |
| chaos                      | 64.0 ms                                                      | 57.4 ms: 1.11x faster                                                        |
| pyflate                    | 439 ms                                                       | 394 ms: 1.11x faster                                                         |
| pprint_safe_repr           | 807 ms                                                       | 730 ms: 1.11x faster                                                         |
| dulwich_log                | 65.4 ms                                                      | 59.3 ms: 1.10x faster                                                        |
| django_template            | 38.2 ms                                                      | 34.8 ms: 1.10x faster                                                        |
| raytrace                   | 298 ms                                                       | 272 ms: 1.10x faster                                                         |
| spectral_norm              | 91.6 ms                                                      | 83.7 ms: 1.10x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 78.7 ms: 1.10x faster                                                        |
| scimark_fft                | 301 ms                                                       | 276 ms: 1.09x faster                                                         |
| regex_compile              | 144 ms                                                       | 132 ms: 1.09x faster                                                         |
| scimark_sor                | 109 ms                                                       | 100 ms: 1.08x faster                                                         |
| unpickle_pure_python       | 210 us                                                       | 194 us: 1.08x faster                                                         |
| xml_etree_parse            | 144 ms                                                       | 133 ms: 1.08x faster                                                         |
| sympy_integrate            | 23.9 ms                                                      | 22.3 ms: 1.07x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 151 ms: 1.07x faster                                                         |
| xml_etree_process          | 58.4 ms                                                      | 55.4 ms: 1.05x faster                                                        |
| meteor_contest             | 128 ms                                                       | 122 ms: 1.05x faster                                                         |
| crypto_pyaes               | 80.3 ms                                                      | 76.8 ms: 1.05x faster                                                        |
| regex_dna                  | 239 ms                                                       | 228 ms: 1.05x faster                                                         |
| pidigits                   | 265 ms                                                       | 255 ms: 1.04x faster                                                         |
| sympy_str                  | 302 ms                                                       | 292 ms: 1.03x faster                                                         |
| mako                       | 10.0 ms                                                      | 9.74 ms: 1.03x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 96.2 ms: 1.03x faster                                                        |
| pycparser                  | 1.23 sec                                                     | 1.21 sec: 1.02x faster                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.51 ms: 1.02x faster                                                        |
| 2to3                       | 285 ms                                                       | 280 ms: 1.02x faster                                                         |
| asyncio_tcp                | 378 ms                                                       | 372 ms: 1.02x faster                                                         |
| logging_silent             | 94.4 ns                                                      | 93.0 ns: 1.01x faster                                                        |
| hexiom                     | 5.96 ms                                                      | 5.88 ms: 1.01x faster                                                        |
| deltablue                  | 3.24 ms                                                      | 3.20 ms: 1.01x faster                                                        |
| json_dumps                 | 10.2 ms                                                      | 10.2 ms: 1.01x faster                                                        |
| regex_v8                   | 23.6 ms                                                      | 23.5 ms: 1.00x faster                                                        |
| docutils                   | 2.87 sec                                                     | 2.88 sec: 1.00x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 8.74 ms: 1.01x slower                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.84 us: 1.02x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 91.9 ms: 1.02x slower                                                        |
| json_loads                 | 24.4 us                                                      | 25.0 us: 1.03x slower                                                        |
| sympy_expand               | 484 ms                                                       | 500 ms: 1.03x slower                                                         |
| pickle_dict                | 32.5 us                                                      | 33.6 us: 1.03x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 329 us: 1.03x slower                                                         |
| nbody                      | 88.0 ms                                                      | 92.7 ms: 1.05x slower                                                        |
| asyncio_websockets         | 387 ms                                                       | 411 ms: 1.06x slower                                                         |
| json                       | 5.12 ms                                                      | 5.44 ms: 1.06x slower                                                        |
| fannkuch                   | 350 ms                                                       | 375 ms: 1.07x slower                                                         |
| unpickle_list              | 4.66 us                                                      | 5.04 us: 1.08x slower                                                        |
| pickle_list                | 4.43 us                                                      | 4.98 us: 1.12x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.74 ms: 1.13x slower                                                        |
| async_generators           | 390 ms                                                       | 444 ms: 1.14x slower                                                         |
| typing_runtime_protocols   | 152 us                                                       | 173 us: 1.14x slower                                                         |
| coverage                   | 66.7 ms                                                      | 78.5 ms: 1.18x slower                                                        |
| pickle                     | 10.5 us                                                      | 12.5 us: 1.18x slower                                                        |
| python_startup             | 11.6 ms                                                      | 15.0 ms: 1.29x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.94 ms: 1.85x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 6.88 ms: 1.98x slower                                                        |
| telco                      | 6.96 ms                                                      | 156 ms: 22.38x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 1.33 sec: 280.00x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                                 |

Benchmark hidden because not significant (5): unpack_sequence, bench_thread_pool, coroutines, unpickle, asyncio_tcp_ssl
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20251101-3.15.0a1+-2f60b8f-JIT/bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.056x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.15x