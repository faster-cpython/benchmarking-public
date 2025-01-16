# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: tail_call
- machine: linux-x86_64
- commit hash: df5d01c
- commit date: 2025-01-16
- overall geometric mean: 1.082x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250116-pythonperf2-x86_64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 274 ms: 1.04x faster                                                        |
| docutils       | 2.87 sec                                                     | 2.85 sec: 1.00x faster                                                      |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250116-pythonperf2-x86_64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 613 ms: 1.72x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 315 ms: 1.72x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 610 ms: 1.71x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 257 ms: 1.68x faster                                                        |
| async_tree_none            | 452 ms                                                       | 271 ms: 1.67x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 334 ms: 1.63x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 517 ms: 1.35x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 532 ms: 1.31x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.59x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250116-pythonperf2-x86_64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 66.9 ms: 1.15x faster                                                       |
| pidigits       | 265 ms                                                       | 285 ms: 1.08x slower                                                        |
| nbody          | 88.0 ms                                                      | 101 ms: 1.15x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250116-pythonperf2-x86_64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 2.98 ms: 1.20x faster                                                       |
| regex_compile  | 144 ms                                                       | 134 ms: 1.07x faster                                                        |
| regex_dna      | 239 ms                                                       | 226 ms: 1.05x faster                                                        |
| regex_v8       | 23.6 ms                                                      | 26.5 ms: 1.12x slower                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250116-pythonperf2-x86_64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 79.0 ms: 1.09x faster                                                       |
| tomli_loads          | 2.16 sec                                                     | 1.99 sec: 1.09x faster                                                      |
| xml_etree_process    | 58.4 ms                                                      | 55.6 ms: 1.05x faster                                                       |
| unpickle_pure_python | 210 us                                                       | 202 us: 1.04x faster                                                        |
| pickle_pure_python   | 318 us                                                       | 311 us: 1.02x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 102 ms: 1.01x faster                                                        |
| json_loads           | 24.4 us                                                      | 25.2 us: 1.03x slower                                                       |
| xml_etree_parse      | 144 ms                                                       | 162 ms: 1.12x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 11.6 ms: 1.13x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250116-pythonperf2-x86_64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.02 ms: 1.04x slower                                                       |
| python_startup         | 11.6 ms                                                      | 16.0 ms: 1.37x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250116-pythonperf2-x86_64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 34.0 ms: 1.12x faster                                                       |
| mako            | 10.0 ms                                                      | 10.9 ms: 1.09x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250116-pythonperf2-x86_64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 613 ms: 1.72x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 315 ms: 1.72x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 610 ms: 1.71x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 257 ms: 1.68x faster                                                        |
| async_tree_none            | 452 ms                                                       | 271 ms: 1.67x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 334 ms: 1.63x faster                                                        |
| deepcopy                   | 368 us                                                       | 263 us: 1.40x faster                                                        |
| comprehensions             | 21.9 us                                                      | 15.8 us: 1.39x faster                                                       |
| deepcopy_memo              | 36.8 us                                                      | 27.0 us: 1.36x faster                                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 517 ms: 1.35x faster                                                        |
| generators                 | 37.4 ms                                                      | 28.5 ms: 1.31x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 532 ms: 1.31x faster                                                        |
| go                         | 150 ms                                                       | 117 ms: 1.28x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 54.8 ms: 1.26x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.75 us: 1.23x faster                                                       |
| pathlib                    | 18.9 ms                                                      | 15.6 ms: 1.21x faster                                                       |
| regex_effbot               | 3.57 ms                                                      | 2.98 ms: 1.20x faster                                                       |
| scimark_lu                 | 98.8 ms                                                      | 82.5 ms: 1.20x faster                                                       |
| raytrace                   | 298 ms                                                       | 254 ms: 1.17x faster                                                        |
| scimark_fft                | 301 ms                                                       | 258 ms: 1.17x faster                                                        |
| scimark_sor                | 109 ms                                                       | 95.1 ms: 1.15x faster                                                       |
| float                      | 76.6 ms                                                      | 66.9 ms: 1.15x faster                                                       |
| logging_silent             | 94.4 ns                                                      | 82.8 ns: 1.14x faster                                                       |
| spectral_norm              | 91.6 ms                                                      | 80.7 ms: 1.13x faster                                                       |
| django_template            | 38.2 ms                                                      | 34.0 ms: 1.12x faster                                                       |
| logging_format             | 7.48 us                                                      | 6.71 us: 1.12x faster                                                       |
| sqlalchemy_declarative     | 159 ms                                                       | 143 ms: 1.12x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.05 us: 1.11x faster                                                       |
| chaos                      | 64.0 ms                                                      | 58.1 ms: 1.10x faster                                                       |
| sympy_sum                  | 162 ms                                                       | 148 ms: 1.10x faster                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.26 ms: 1.10x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 79.0 ms: 1.09x faster                                                       |
| richards                   | 45.7 ms                                                      | 42.1 ms: 1.09x faster                                                       |
| tomli_loads                | 2.16 sec                                                     | 1.99 sec: 1.09x faster                                                      |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 3.88 ms: 1.08x faster                                                       |
| pyflate                    | 439 ms                                                       | 405 ms: 1.08x faster                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.65 ms: 1.08x faster                                                       |
| sympy_str                  | 302 ms                                                       | 282 ms: 1.07x faster                                                        |
| sqlalchemy_imperative      | 18.7 ms                                                      | 17.5 ms: 1.07x faster                                                       |
| regex_compile              | 144 ms                                                       | 134 ms: 1.07x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 75.1 ms: 1.07x faster                                                       |
| sympy_integrate            | 23.9 ms                                                      | 22.5 ms: 1.06x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 21.6 ms: 1.06x faster                                                       |
| richards_super             | 51.3 ms                                                      | 48.4 ms: 1.06x faster                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.57 sec: 1.06x faster                                                      |
| hexiom                     | 5.96 ms                                                      | 5.65 ms: 1.06x faster                                                       |
| regex_dna                  | 239 ms                                                       | 226 ms: 1.05x faster                                                        |
| bench_thread_pool          | 950 us                                                       | 901 us: 1.05x faster                                                        |
| pprint_safe_repr           | 807 ms                                                       | 767 ms: 1.05x faster                                                        |
| xml_etree_process          | 58.4 ms                                                      | 55.6 ms: 1.05x faster                                                       |
| 2to3                       | 285 ms                                                       | 274 ms: 1.04x faster                                                        |
| deltablue                  | 3.24 ms                                                      | 3.12 ms: 1.04x faster                                                       |
| unpickle_pure_python       | 210 us                                                       | 202 us: 1.04x faster                                                        |
| nqueens                    | 89.9 ms                                                      | 86.9 ms: 1.03x faster                                                       |
| pickle_pure_python         | 318 us                                                       | 311 us: 1.02x faster                                                        |
| pycparser                  | 1.23 sec                                                     | 1.21 sec: 1.02x faster                                                      |
| xml_etree_iterparse        | 103 ms                                                       | 102 ms: 1.01x faster                                                        |
| asyncio_websockets         | 387 ms                                                       | 383 ms: 1.01x faster                                                        |
| dulwich_log                | 65.4 ms                                                      | 64.9 ms: 1.01x faster                                                       |
| docutils                   | 2.87 sec                                                     | 2.85 sec: 1.00x faster                                                      |
| sqlglot_optimize           | 57.5 ms                                                      | 57.3 ms: 1.00x faster                                                       |
| meteor_contest             | 128 ms                                                       | 128 ms: 1.00x faster                                                        |
| sympy_expand               | 484 ms                                                       | 483 ms: 1.00x faster                                                        |
| mdp                        | 2.57 sec                                                     | 2.60 sec: 1.01x slower                                                      |
| json                       | 5.12 ms                                                      | 5.24 ms: 1.02x slower                                                       |
| fannkuch                   | 350 ms                                                       | 359 ms: 1.03x slower                                                        |
| json_loads                 | 24.4 us                                                      | 25.2 us: 1.03x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 9.02 ms: 1.04x slower                                                       |
| pidigits                   | 265 ms                                                       | 285 ms: 1.08x slower                                                        |
| async_generators           | 390 ms                                                       | 421 ms: 1.08x slower                                                        |
| telco                      | 6.96 ms                                                      | 7.54 ms: 1.08x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 165 us: 1.08x slower                                                        |
| mako                       | 10.0 ms                                                      | 10.9 ms: 1.09x slower                                                       |
| coverage                   | 66.7 ms                                                      | 73.2 ms: 1.10x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 26.5 ms: 1.12x slower                                                       |
| xml_etree_parse            | 144 ms                                                       | 162 ms: 1.12x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 11.6 ms: 1.13x slower                                                       |
| nbody                      | 88.0 ms                                                      | 101 ms: 1.15x slower                                                        |
| python_startup             | 11.6 ms                                                      | 16.0 ms: 1.37x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 5.72 ms: 1.65x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.87 ms: 1.81x slower                                                       |
| bench_mp_pool              | 4.76 ms                                                      | 1.54 sec: 323.95x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (2): sqlglot_normalize, sqlite_synth
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250116-3.14.0a4+-df5d01c-CLANG/bm-20250116-pythonperf2-x86_64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.082x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.08x