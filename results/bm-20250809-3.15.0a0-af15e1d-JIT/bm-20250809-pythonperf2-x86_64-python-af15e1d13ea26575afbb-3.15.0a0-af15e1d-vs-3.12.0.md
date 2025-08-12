# Results vs. 3.12.0

- fork: python
- ref: af15e1d13ea26575afbb
- machine: linux-x86_64
- commit hash: af15e1d
- commit date: 2025-08-09
- overall geometric mean: 1.041x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf2-x86_64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 285 ms: 1.00x faster                                                        |
| docutils       | 2.87 sec                                                     | 2.90 sec: 1.01x slower                                                      |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf2-x86_64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io              | 1.04 sec                                                     | 623 ms: 1.67x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 637 ms: 1.65x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 330 ms: 1.65x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 333 ms: 1.62x faster                                                        |
| async_tree_none            | 452 ms                                                       | 281 ms: 1.60x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 271 ms: 1.59x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 504 ms: 1.38x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 507 ms: 1.38x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.56x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf2-x86_64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 64.2 ms: 1.19x faster                                                       |
| pidigits       | 265 ms                                                       | 255 ms: 1.04x faster                                                        |
| nbody          | 88.0 ms                                                      | 99.6 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf2-x86_64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 132 ms: 1.09x faster                                                        |
| regex_dna      | 239 ms                                                       | 226 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf2-x86_64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 1.90 sec: 1.14x faster                                                      |
| unpickle_pure_python | 210 us                                                       | 193 us: 1.09x faster                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 80.8 ms: 1.07x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 97.9 ms: 1.05x faster                                                       |
| xml_etree_process    | 58.4 ms                                                      | 55.8 ms: 1.05x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 139 ms: 1.04x faster                                                        |
| json_dumps           | 10.2 ms                                                      | 10.1 ms: 1.01x faster                                                       |
| pickle_pure_python   | 318 us                                                       | 327 us: 1.03x slower                                                        |
| json_loads           | 24.4 us                                                      | 25.2 us: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf2-x86_64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.81 ms: 1.02x slower                                                       |
| python_startup         | 11.6 ms                                                      | 15.3 ms: 1.32x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf2-x86_64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 34.7 ms: 1.10x faster                                                       |
| mako            | 10.0 ms                                                      | 9.72 ms: 1.03x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.06x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250809-pythonperf2-x86_64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.28 sec: 2.01x faster                                                      |
| async_tree_io              | 1.04 sec                                                     | 623 ms: 1.67x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 637 ms: 1.65x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 330 ms: 1.65x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 333 ms: 1.62x faster                                                        |
| async_tree_none            | 452 ms                                                       | 281 ms: 1.60x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 271 ms: 1.59x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 504 ms: 1.38x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 507 ms: 1.38x faster                                                        |
| deepcopy                   | 368 us                                                       | 272 us: 1.36x faster                                                        |
| richards                   | 45.7 ms                                                      | 34.2 ms: 1.34x faster                                                       |
| deepcopy_memo              | 36.8 us                                                      | 27.7 us: 1.33x faster                                                       |
| richards_super             | 51.3 ms                                                      | 40.2 ms: 1.28x faster                                                       |
| comprehensions             | 21.9 us                                                      | 17.3 us: 1.27x faster                                                       |
| generators                 | 37.4 ms                                                      | 29.7 ms: 1.26x faster                                                       |
| float                      | 76.6 ms                                                      | 64.2 ms: 1.19x faster                                                       |
| go                         | 150 ms                                                       | 126 ms: 1.19x faster                                                        |
| spectral_norm              | 91.6 ms                                                      | 78.8 ms: 1.16x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.95 us: 1.14x faster                                                       |
| tomli_loads                | 2.16 sec                                                     | 1.90 sec: 1.14x faster                                                      |
| pathlib                    | 18.9 ms                                                      | 16.7 ms: 1.13x faster                                                       |
| deltablue                  | 3.24 ms                                                      | 2.89 ms: 1.12x faster                                                       |
| logging_format             | 7.48 us                                                      | 6.70 us: 1.12x faster                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 62.1 ms: 1.11x faster                                                       |
| logging_simple             | 6.71 us                                                      | 6.09 us: 1.10x faster                                                       |
| dulwich_log                | 65.4 ms                                                      | 59.4 ms: 1.10x faster                                                       |
| django_template            | 38.2 ms                                                      | 34.7 ms: 1.10x faster                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.51 sec: 1.09x faster                                                      |
| regex_compile              | 144 ms                                                       | 132 ms: 1.09x faster                                                        |
| chaos                      | 64.0 ms                                                      | 58.9 ms: 1.09x faster                                                       |
| unpickle_pure_python       | 210 us                                                       | 193 us: 1.09x faster                                                        |
| pyflate                    | 439 ms                                                       | 406 ms: 1.08x faster                                                        |
| scimark_sor                | 109 ms                                                       | 101 ms: 1.08x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 22.2 ms: 1.08x faster                                                       |
| pprint_safe_repr           | 807 ms                                                       | 749 ms: 1.08x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 151 ms: 1.07x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 80.8 ms: 1.07x faster                                                       |
| raytrace                   | 298 ms                                                       | 282 ms: 1.06x faster                                                        |
| regex_dna                  | 239 ms                                                       | 226 ms: 1.05x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 93.9 ms: 1.05x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 97.9 ms: 1.05x faster                                                       |
| meteor_contest             | 128 ms                                                       | 122 ms: 1.05x faster                                                        |
| xml_etree_process          | 58.4 ms                                                      | 55.8 ms: 1.05x faster                                                       |
| sympy_str                  | 302 ms                                                       | 289 ms: 1.05x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 76.9 ms: 1.04x faster                                                       |
| xml_etree_parse            | 144 ms                                                       | 139 ms: 1.04x faster                                                        |
| pidigits                   | 265 ms                                                       | 255 ms: 1.04x faster                                                        |
| mako                       | 10.0 ms                                                      | 9.72 ms: 1.03x faster                                                       |
| logging_silent             | 94.4 ns                                                      | 91.9 ns: 1.03x faster                                                       |
| pycparser                  | 1.23 sec                                                     | 1.21 sec: 1.02x faster                                                      |
| coroutines                 | 23.0 ms                                                      | 22.5 ms: 1.02x faster                                                       |
| asyncio_websockets         | 387 ms                                                       | 381 ms: 1.01x faster                                                        |
| json_dumps                 | 10.2 ms                                                      | 10.1 ms: 1.01x faster                                                       |
| 2to3                       | 285 ms                                                       | 285 ms: 1.00x faster                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.79 us: 1.00x slower                                                       |
| docutils                   | 2.87 sec                                                     | 2.90 sec: 1.01x slower                                                      |
| python_startup_no_site     | 8.64 ms                                                      | 8.81 ms: 1.02x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.10 ms: 1.02x slower                                                       |
| sympy_expand               | 484 ms                                                       | 497 ms: 1.03x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 92.3 ms: 1.03x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 327 us: 1.03x slower                                                        |
| json_loads                 | 24.4 us                                                      | 25.2 us: 1.03x slower                                                       |
| fannkuch                   | 350 ms                                                       | 371 ms: 1.06x slower                                                        |
| json                       | 5.12 ms                                                      | 5.43 ms: 1.06x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 170 us: 1.12x slower                                                        |
| nbody                      | 88.0 ms                                                      | 99.6 ms: 1.13x slower                                                       |
| async_generators           | 390 ms                                                       | 448 ms: 1.15x slower                                                        |
| coverage                   | 66.7 ms                                                      | 77.9 ms: 1.17x slower                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.91 ms: 1.17x slower                                                       |
| python_startup             | 11.6 ms                                                      | 15.3 ms: 1.32x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.92 ms: 1.84x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 6.79 ms: 1.95x slower                                                       |
| telco                      | 6.96 ms                                                      | 158 ms: 22.69x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (3): scimark_fft, regex_effbot, regex_v8
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250809-3.15.0a0-af15e1d-JIT/bm-20250809-pythonperf2-x86_64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.041x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.14x