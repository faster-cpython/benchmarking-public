# Results vs. 3.12.0

- fork: nascheme
- ref: pgo_benchmark_task
- machine: linux-x86_64
- commit hash: 8dd8862
- commit date: 2025-02-28
- overall geometric mean: 1.064x faster
- HPT reliability: 99.90%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 289 ms: 1.01x slower                                                         |
| docutils       | 2.87 sec                                                     | 2.89 sec: 1.01x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 312 ms: 1.73x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 611 ms: 1.72x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 609 ms: 1.71x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 321 ms: 1.70x faster                                                         |
| async_tree_none            | 452 ms                                                       | 266 ms: 1.70x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 259 ms: 1.67x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 482 ms: 1.45x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 494 ms: 1.41x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.63x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 70.1 ms: 1.09x faster                                                        |
| pidigits       | 265 ms                                                       | 261 ms: 1.02x faster                                                         |
| nbody          | 88.0 ms                                                      | 91.2 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 2.52 ms: 1.42x faster                                                        |
| regex_dna      | 239 ms                                                       | 192 ms: 1.24x faster                                                         |
| regex_compile  | 144 ms                                                       | 138 ms: 1.04x faster                                                         |
| regex_v8       | 23.6 ms                                                      | 24.3 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                        | 1.16x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 144 ms                                                       | 124 ms: 1.16x faster                                                         |
| xml_etree_iterparse  | 103 ms                                                       | 91.8 ms: 1.12x faster                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 80.6 ms: 1.07x faster                                                        |
| xml_etree_process    | 58.4 ms                                                      | 57.1 ms: 1.02x faster                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.18 sec: 1.01x slower                                                       |
| json_loads           | 24.4 us                                                      | 24.8 us: 1.02x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 325 us: 1.02x slower                                                         |
| unpickle_pure_python | 210 us                                                       | 216 us: 1.03x slower                                                         |
| json_dumps           | 10.2 ms                                                      | 11.1 ms: 1.09x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.16 ms: 1.06x slower                                                        |
| python_startup         | 11.6 ms                                                      | 16.4 ms: 1.41x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.22x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 37.2 ms: 1.03x faster                                                        |
| mako            | 10.0 ms                                                      | 10.8 ms: 1.08x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.02x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 312 ms: 1.73x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 611 ms: 1.72x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 609 ms: 1.71x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 321 ms: 1.70x faster                                                         |
| async_tree_none            | 452 ms                                                       | 266 ms: 1.70x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 259 ms: 1.67x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 482 ms: 1.45x faster                                                         |
| regex_effbot               | 3.57 ms                                                      | 2.52 ms: 1.42x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 494 ms: 1.41x faster                                                         |
| deepcopy                   | 368 us                                                       | 276 us: 1.33x faster                                                         |
| generators                 | 37.4 ms                                                      | 28.1 ms: 1.33x faster                                                        |
| comprehensions             | 21.9 us                                                      | 16.8 us: 1.30x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 28.9 us: 1.27x faster                                                        |
| regex_dna                  | 239 ms                                                       | 192 ms: 1.24x faster                                                         |
| scimark_monte_carlo        | 69.0 ms                                                      | 56.5 ms: 1.22x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 2.86 us: 1.18x faster                                                        |
| go                         | 150 ms                                                       | 129 ms: 1.16x faster                                                         |
| xml_etree_parse            | 144 ms                                                       | 124 ms: 1.16x faster                                                         |
| coroutines                 | 23.0 ms                                                      | 20.0 ms: 1.15x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 16.6 ms: 1.14x faster                                                        |
| meteor_contest             | 128 ms                                                       | 114 ms: 1.12x faster                                                         |
| xml_etree_iterparse        | 103 ms                                                       | 91.8 ms: 1.12x faster                                                        |
| float                      | 76.6 ms                                                      | 70.1 ms: 1.09x faster                                                        |
| spectral_norm              | 91.6 ms                                                      | 83.8 ms: 1.09x faster                                                        |
| raytrace                   | 298 ms                                                       | 273 ms: 1.09x faster                                                         |
| sqlalchemy_declarative     | 159 ms                                                       | 146 ms: 1.09x faster                                                         |
| pprint_pformat             | 1.65 sec                                                     | 1.54 sec: 1.07x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 80.6 ms: 1.07x faster                                                        |
| pprint_safe_repr           | 807 ms                                                       | 757 ms: 1.07x faster                                                         |
| scimark_fft                | 301 ms                                                       | 284 ms: 1.06x faster                                                         |
| chaos                      | 64.0 ms                                                      | 60.5 ms: 1.06x faster                                                        |
| mdp                        | 2.57 sec                                                     | 2.43 sec: 1.06x faster                                                       |
| scimark_lu                 | 98.8 ms                                                      | 94.6 ms: 1.04x faster                                                        |
| regex_compile              | 144 ms                                                       | 138 ms: 1.04x faster                                                         |
| crypto_pyaes               | 80.3 ms                                                      | 77.6 ms: 1.04x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 157 ms: 1.03x faster                                                         |
| django_template            | 38.2 ms                                                      | 37.2 ms: 1.03x faster                                                        |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.3 ms: 1.02x faster                                                        |
| xml_etree_process          | 58.4 ms                                                      | 57.1 ms: 1.02x faster                                                        |
| nqueens                    | 89.9 ms                                                      | 88.2 ms: 1.02x faster                                                        |
| pyflate                    | 439 ms                                                       | 431 ms: 1.02x faster                                                         |
| pidigits                   | 265 ms                                                       | 261 ms: 1.02x faster                                                         |
| fannkuch                   | 350 ms                                                       | 346 ms: 1.01x faster                                                         |
| logging_format             | 7.48 us                                                      | 7.40 us: 1.01x faster                                                        |
| sympy_str                  | 302 ms                                                       | 299 ms: 1.01x faster                                                         |
| sympy_integrate            | 23.9 ms                                                      | 23.7 ms: 1.01x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.66 us: 1.01x faster                                                        |
| asyncio_websockets         | 387 ms                                                       | 385 ms: 1.01x faster                                                         |
| tomli_loads                | 2.16 sec                                                     | 2.18 sec: 1.01x slower                                                       |
| docutils                   | 2.87 sec                                                     | 2.89 sec: 1.01x slower                                                       |
| richards                   | 45.7 ms                                                      | 46.3 ms: 1.01x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.03 ms: 1.01x slower                                                        |
| 2to3                       | 285 ms                                                       | 289 ms: 1.01x slower                                                         |
| sqlglot_transpile          | 1.78 ms                                                      | 1.80 ms: 1.02x slower                                                        |
| json_loads                 | 24.4 us                                                      | 24.8 us: 1.02x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.40 ms: 1.02x slower                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.82 us: 1.02x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 325 us: 1.02x slower                                                         |
| sqlglot_optimize           | 57.5 ms                                                      | 58.9 ms: 1.02x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.27 sec: 1.03x slower                                                       |
| deltablue                  | 3.24 ms                                                      | 3.33 ms: 1.03x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 24.3 ms: 1.03x slower                                                        |
| async_generators           | 390 ms                                                       | 402 ms: 1.03x slower                                                         |
| unpickle_pure_python       | 210 us                                                       | 216 us: 1.03x slower                                                         |
| richards_super             | 51.3 ms                                                      | 53.2 ms: 1.04x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 97.7 ns: 1.04x slower                                                        |
| nbody                      | 88.0 ms                                                      | 91.2 ms: 1.04x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.38 ms: 1.04x slower                                                        |
| sqlglot_normalize          | 116 ms                                                       | 121 ms: 1.04x slower                                                         |
| sympy_expand               | 484 ms                                                       | 507 ms: 1.05x slower                                                         |
| bench_thread_pool          | 950 us                                                       | 1.00 ms: 1.05x slower                                                        |
| dulwich_log                | 65.4 ms                                                      | 69.2 ms: 1.06x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 9.16 ms: 1.06x slower                                                        |
| mako                       | 10.0 ms                                                      | 10.8 ms: 1.08x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 11.1 ms: 1.09x slower                                                        |
| telco                      | 6.96 ms                                                      | 7.59 ms: 1.09x slower                                                        |
| json                       | 5.12 ms                                                      | 5.65 ms: 1.10x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 171 us: 1.13x slower                                                         |
| coverage                   | 66.7 ms                                                      | 83.3 ms: 1.25x slower                                                        |
| python_startup             | 11.6 ms                                                      | 16.4 ms: 1.41x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 5.46 ms: 1.57x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.80 ms: 1.76x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 853 ms: 179.12x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): scimark_sor
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250228-3.14.0a5+-8dd8862/bm-20250228-pythonperf2-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.064x faster

# HPT report

- Reliability score: 99.90% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x