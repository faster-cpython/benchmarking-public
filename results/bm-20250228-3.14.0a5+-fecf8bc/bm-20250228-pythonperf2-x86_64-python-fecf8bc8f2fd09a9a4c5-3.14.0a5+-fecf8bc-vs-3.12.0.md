# Results vs. 3.12.0

- fork: python
- ref: fecf8bc8f2fd09a9a4c5
- machine: linux-x86_64
- commit hash: fecf8bc
- commit date: 2025-02-28
- overall geometric mean: 1.036x faster
- HPT reliability: 98.44%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf2-x86_64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 284 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                 |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf2-x86_64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 646 ms: 1.63x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 641 ms: 1.63x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 335 ms: 1.61x faster                                                         |
| async_tree_none            | 452 ms                                                       | 286 ms: 1.58x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 348 ms: 1.56x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 277 ms: 1.56x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 507 ms: 1.38x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 519 ms: 1.34x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.53x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf2-x86_64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 69.9 ms: 1.10x faster                                                        |
| pidigits       | 265 ms                                                       | 255 ms: 1.04x faster                                                         |
| nbody          | 88.0 ms                                                      | 101 ms: 1.15x slower                                                         |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf2-x86_64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.05 ms: 1.17x faster                                                        |
| regex_compile  | 144 ms                                                       | 135 ms: 1.07x faster                                                         |
| regex_v8       | 23.6 ms                                                      | 26.0 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf2-x86_64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 97.3 ms: 1.06x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 138 ms: 1.05x faster                                                         |
| xml_etree_generate   | 86.1 ms                                                      | 83.4 ms: 1.03x faster                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.11 sec: 1.03x faster                                                       |
| unpickle_pure_python | 210 us                                                       | 212 us: 1.01x slower                                                         |
| xml_etree_process    | 58.4 ms                                                      | 60.0 ms: 1.03x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 333 us: 1.05x slower                                                         |
| json_loads           | 24.4 us                                                      | 26.1 us: 1.07x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 11.6 ms: 1.13x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf2-x86_64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.15 ms: 1.06x slower                                                        |
| python_startup         | 11.6 ms                                                      | 16.3 ms: 1.40x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.22x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf2-x86_64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 36.3 ms: 1.05x faster                                                        |
| mako            | 10.0 ms                                                      | 10.9 ms: 1.08x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.02x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf2-x86_64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 646 ms: 1.63x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 641 ms: 1.63x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 335 ms: 1.61x faster                                                         |
| async_tree_none            | 452 ms                                                       | 286 ms: 1.58x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 348 ms: 1.56x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 277 ms: 1.56x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 507 ms: 1.38x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 519 ms: 1.34x faster                                                         |
| generators                 | 37.4 ms                                                      | 28.4 ms: 1.32x faster                                                        |
| deepcopy                   | 368 us                                                       | 281 us: 1.31x faster                                                         |
| comprehensions             | 21.9 us                                                      | 17.3 us: 1.27x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 29.9 us: 1.23x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.05 ms: 1.17x faster                                                        |
| go                         | 150 ms                                                       | 129 ms: 1.16x faster                                                         |
| deepcopy_reduce            | 3.37 us                                                      | 2.95 us: 1.14x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 16.5 ms: 1.14x faster                                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 145 ms: 1.10x faster                                                         |
| float                      | 76.6 ms                                                      | 69.9 ms: 1.10x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 21.2 ms: 1.08x faster                                                        |
| regex_compile              | 144 ms                                                       | 135 ms: 1.07x faster                                                         |
| logging_format             | 7.48 us                                                      | 7.00 us: 1.07x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 152 ms: 1.07x faster                                                         |
| raytrace                   | 298 ms                                                       | 280 ms: 1.07x faster                                                         |
| xml_etree_iterparse        | 103 ms                                                       | 97.3 ms: 1.06x faster                                                        |
| chaos                      | 64.0 ms                                                      | 60.6 ms: 1.06x faster                                                        |
| django_template            | 38.2 ms                                                      | 36.3 ms: 1.05x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 65.8 ms: 1.05x faster                                                        |
| sqlalchemy_imperative      | 18.7 ms                                                      | 17.9 ms: 1.05x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.41 us: 1.05x faster                                                        |
| spectral_norm              | 91.6 ms                                                      | 87.6 ms: 1.05x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 138 ms: 1.05x faster                                                         |
| crypto_pyaes               | 80.3 ms                                                      | 76.9 ms: 1.04x faster                                                        |
| sympy_str                  | 302 ms                                                       | 290 ms: 1.04x faster                                                         |
| pidigits                   | 265 ms                                                       | 255 ms: 1.04x faster                                                         |
| sympy_integrate            | 23.9 ms                                                      | 23.0 ms: 1.04x faster                                                        |
| meteor_contest             | 128 ms                                                       | 124 ms: 1.03x faster                                                         |
| xml_etree_generate         | 86.1 ms                                                      | 83.4 ms: 1.03x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.61 sec: 1.03x faster                                                       |
| mdp                        | 2.57 sec                                                     | 2.50 sec: 1.03x faster                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.11 sec: 1.03x faster                                                       |
| pprint_safe_repr           | 807 ms                                                       | 797 ms: 1.01x faster                                                         |
| sqlglot_transpile          | 1.78 ms                                                      | 1.76 ms: 1.01x faster                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.36 ms: 1.01x faster                                                        |
| asyncio_websockets         | 387 ms                                                       | 385 ms: 1.01x faster                                                         |
| 2to3                       | 285 ms                                                       | 284 ms: 1.00x faster                                                         |
| unpickle_pure_python       | 210 us                                                       | 212 us: 1.01x slower                                                         |
| scimark_sor                | 109 ms                                                       | 111 ms: 1.01x slower                                                         |
| sqlite_synth               | 2.77 us                                                      | 2.81 us: 1.01x slower                                                        |
| scimark_lu                 | 98.8 ms                                                      | 100 ms: 1.02x slower                                                         |
| pyflate                    | 439 ms                                                       | 449 ms: 1.02x slower                                                         |
| sqlglot_optimize           | 57.5 ms                                                      | 58.9 ms: 1.03x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.11 ms: 1.03x slower                                                        |
| richards                   | 45.7 ms                                                      | 47.0 ms: 1.03x slower                                                        |
| sympy_expand               | 484 ms                                                       | 497 ms: 1.03x slower                                                         |
| xml_etree_process          | 58.4 ms                                                      | 60.0 ms: 1.03x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 92.4 ms: 1.03x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 3.35 ms: 1.04x slower                                                        |
| richards_super             | 51.3 ms                                                      | 53.2 ms: 1.04x slower                                                        |
| sqlglot_normalize          | 116 ms                                                       | 120 ms: 1.04x slower                                                         |
| logging_silent             | 94.4 ns                                                      | 98.0 ns: 1.04x slower                                                        |
| fannkuch                   | 350 ms                                                       | 364 ms: 1.04x slower                                                         |
| dulwich_log                | 65.4 ms                                                      | 68.1 ms: 1.04x slower                                                        |
| async_generators           | 390 ms                                                       | 407 ms: 1.04x slower                                                         |
| json                       | 5.12 ms                                                      | 5.34 ms: 1.04x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 333 us: 1.05x slower                                                         |
| python_startup_no_site     | 8.64 ms                                                      | 9.15 ms: 1.06x slower                                                        |
| json_loads                 | 24.4 us                                                      | 26.1 us: 1.07x slower                                                        |
| mako                       | 10.0 ms                                                      | 10.9 ms: 1.08x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 26.0 ms: 1.10x slower                                                        |
| scimark_fft                | 301 ms                                                       | 333 ms: 1.11x slower                                                         |
| typing_runtime_protocols   | 152 us                                                       | 169 us: 1.12x slower                                                         |
| json_dumps                 | 10.2 ms                                                      | 11.6 ms: 1.13x slower                                                        |
| nbody                      | 88.0 ms                                                      | 101 ms: 1.15x slower                                                         |
| telco                      | 6.96 ms                                                      | 8.09 ms: 1.16x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.97 ms: 1.18x slower                                                        |
| coverage                   | 66.7 ms                                                      | 84.5 ms: 1.27x slower                                                        |
| python_startup             | 11.6 ms                                                      | 16.3 ms: 1.40x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.69 ms: 1.69x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 6.27 ms: 1.80x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 1.29 sec: 271.56x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                                 |

Benchmark hidden because not significant (4): regex_dna, docutils, pycparser, bench_thread_pool
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250228-3.14.0a5+-fecf8bc/bm-20250228-pythonperf2-x86_64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.036x faster

# HPT report

- Reliability score: 98.44% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x