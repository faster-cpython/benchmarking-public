# Results vs. 3.12.0

- fork: brandtbucher
- ref: nojit
- machine: linux-x86_64
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.047x faster
- HPT reliability: 99.68%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 282 ms: 1.01x faster                                                |
| docutils       | 2.87 sec                                                     | 2.88 sec: 1.00x slower                                              |
| Geometric mean | (ref)                                                        | 1.00x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 620 ms: 1.70x faster                                                |
| async_tree_memoization_tg  | 540 ms                                                       | 323 ms: 1.67x faster                                                |
| async_tree_io              | 1.04 sec                                                     | 629 ms: 1.66x faster                                                |
| async_tree_none_tg         | 431 ms                                                       | 267 ms: 1.62x faster                                                |
| async_tree_none            | 452 ms                                                       | 282 ms: 1.60x faster                                                |
| async_tree_memoization     | 544 ms                                                       | 344 ms: 1.58x faster                                                |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 494 ms: 1.41x faster                                                |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 511 ms: 1.36x faster                                                |
| Geometric mean             | (ref)                                                        | 1.57x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 71.8 ms: 1.07x faster                                               |
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                |
| nbody          | 88.0 ms                                                      | 89.3 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                        | 1.03x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.26 ms: 1.10x faster                                               |
| regex_compile  | 144 ms                                                       | 136 ms: 1.06x faster                                                |
| regex_dna      | 239 ms                                                       | 244 ms: 1.02x slower                                                |
| regex_v8       | 23.6 ms                                                      | 26.4 ms: 1.12x slower                                               |
| Geometric mean | (ref)                                                        | 1.00x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 97.3 ms: 1.06x faster                                               |
| tomli_loads          | 2.16 sec                                                     | 2.07 sec: 1.04x faster                                              |
| xml_etree_generate   | 86.1 ms                                                      | 83.3 ms: 1.03x faster                                               |
| xml_etree_parse      | 144 ms                                                       | 139 ms: 1.03x faster                                                |
| json_loads           | 24.4 us                                                      | 23.6 us: 1.03x faster                                               |
| unpickle_pure_python | 210 us                                                       | 207 us: 1.01x faster                                                |
| xml_etree_process    | 58.4 ms                                                      | 58.8 ms: 1.01x slower                                               |
| pickle_pure_python   | 318 us                                                       | 328 us: 1.03x slower                                                |
| json_dumps           | 10.2 ms                                                      | 11.4 ms: 1.12x slower                                               |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.01 ms: 1.04x slower                                               |
| python_startup         | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                               |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.9 ms: 1.06x faster                                               |
| mako            | 10.0 ms                                                      | 10.9 ms: 1.09x slower                                               |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 620 ms: 1.70x faster                                                |
| async_tree_memoization_tg  | 540 ms                                                       | 323 ms: 1.67x faster                                                |
| async_tree_io              | 1.04 sec                                                     | 629 ms: 1.66x faster                                                |
| async_tree_none_tg         | 431 ms                                                       | 267 ms: 1.62x faster                                                |
| async_tree_none            | 452 ms                                                       | 282 ms: 1.60x faster                                                |
| async_tree_memoization     | 544 ms                                                       | 344 ms: 1.58x faster                                                |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 494 ms: 1.41x faster                                                |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 511 ms: 1.36x faster                                                |
| generators                 | 37.4 ms                                                      | 28.4 ms: 1.32x faster                                               |
| deepcopy                   | 368 us                                                       | 281 us: 1.31x faster                                                |
| comprehensions             | 21.9 us                                                      | 17.5 us: 1.25x faster                                               |
| deepcopy_memo              | 36.8 us                                                      | 30.0 us: 1.23x faster                                               |
| go                         | 150 ms                                                       | 126 ms: 1.19x faster                                                |
| pathlib                    | 18.9 ms                                                      | 16.3 ms: 1.16x faster                                               |
| deepcopy_reduce            | 3.37 us                                                      | 2.94 us: 1.15x faster                                               |
| sqlalchemy_declarative     | 159 ms                                                       | 143 ms: 1.12x faster                                                |
| crypto_pyaes               | 80.3 ms                                                      | 72.1 ms: 1.11x faster                                               |
| scimark_monte_carlo        | 69.0 ms                                                      | 62.0 ms: 1.11x faster                                               |
| raytrace                   | 298 ms                                                       | 268 ms: 1.11x faster                                                |
| coroutines                 | 23.0 ms                                                      | 20.9 ms: 1.10x faster                                               |
| regex_effbot               | 3.57 ms                                                      | 3.26 ms: 1.10x faster                                               |
| float                      | 76.6 ms                                                      | 71.8 ms: 1.07x faster                                               |
| sympy_sum                  | 162 ms                                                       | 152 ms: 1.07x faster                                                |
| django_template            | 38.2 ms                                                      | 35.9 ms: 1.06x faster                                               |
| regex_compile              | 144 ms                                                       | 136 ms: 1.06x faster                                                |
| pprint_pformat             | 1.65 sec                                                     | 1.57 sec: 1.06x faster                                              |
| xml_etree_iterparse        | 103 ms                                                       | 97.3 ms: 1.06x faster                                               |
| logging_format             | 7.48 us                                                      | 7.08 us: 1.06x faster                                               |
| logging_simple             | 6.71 us                                                      | 6.39 us: 1.05x faster                                               |
| scimark_lu                 | 98.8 ms                                                      | 94.1 ms: 1.05x faster                                               |
| pprint_safe_repr           | 807 ms                                                       | 770 ms: 1.05x faster                                                |
| sqlalchemy_imperative      | 18.7 ms                                                      | 17.9 ms: 1.05x faster                                               |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                |
| tomli_loads                | 2.16 sec                                                     | 2.07 sec: 1.04x faster                                              |
| sympy_str                  | 302 ms                                                       | 290 ms: 1.04x faster                                                |
| bench_thread_pool          | 950 us                                                       | 915 us: 1.04x faster                                                |
| mdp                        | 2.57 sec                                                     | 2.48 sec: 1.04x faster                                              |
| sympy_integrate            | 23.9 ms                                                      | 23.1 ms: 1.04x faster                                               |
| xml_etree_generate         | 86.1 ms                                                      | 83.3 ms: 1.03x faster                                               |
| xml_etree_parse            | 144 ms                                                       | 139 ms: 1.03x faster                                                |
| chaos                      | 64.0 ms                                                      | 61.9 ms: 1.03x faster                                               |
| sqlglot_parse              | 1.38 ms                                                      | 1.33 ms: 1.03x faster                                               |
| json_loads                 | 24.4 us                                                      | 23.6 us: 1.03x faster                                               |
| sqlglot_transpile          | 1.78 ms                                                      | 1.73 ms: 1.03x faster                                               |
| meteor_contest             | 128 ms                                                       | 126 ms: 1.02x faster                                                |
| spectral_norm              | 91.6 ms                                                      | 90.0 ms: 1.02x faster                                               |
| unpickle_pure_python       | 210 us                                                       | 207 us: 1.01x faster                                                |
| sqlglot_normalize          | 116 ms                                                       | 114 ms: 1.01x faster                                                |
| 2to3                       | 285 ms                                                       | 282 ms: 1.01x faster                                                |
| scimark_fft                | 301 ms                                                       | 298 ms: 1.01x faster                                                |
| asyncio_websockets         | 387 ms                                                       | 385 ms: 1.01x faster                                                |
| docutils                   | 2.87 sec                                                     | 2.88 sec: 1.00x slower                                              |
| nqueens                    | 89.9 ms                                                      | 90.5 ms: 1.01x slower                                               |
| xml_etree_process          | 58.4 ms                                                      | 58.8 ms: 1.01x slower                                               |
| dulwich_log                | 65.4 ms                                                      | 65.9 ms: 1.01x slower                                               |
| richards_super             | 51.3 ms                                                      | 51.9 ms: 1.01x slower                                               |
| nbody                      | 88.0 ms                                                      | 89.3 ms: 1.02x slower                                               |
| scimark_sor                | 109 ms                                                       | 111 ms: 1.02x slower                                                |
| regex_dna                  | 239 ms                                                       | 244 ms: 1.02x slower                                                |
| hexiom                     | 5.96 ms                                                      | 6.09 ms: 1.02x slower                                               |
| sympy_expand               | 484 ms                                                       | 497 ms: 1.03x slower                                                |
| sqlite_synth               | 2.77 us                                                      | 2.86 us: 1.03x slower                                               |
| pickle_pure_python         | 318 us                                                       | 328 us: 1.03x slower                                                |
| pyflate                    | 439 ms                                                       | 453 ms: 1.03x slower                                                |
| logging_silent             | 94.4 ns                                                      | 98.3 ns: 1.04x slower                                               |
| fannkuch                   | 350 ms                                                       | 365 ms: 1.04x slower                                                |
| python_startup_no_site     | 8.64 ms                                                      | 9.01 ms: 1.04x slower                                               |
| deltablue                  | 3.24 ms                                                      | 3.38 ms: 1.04x slower                                               |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.45 ms: 1.06x slower                                               |
| mako                       | 10.0 ms                                                      | 10.9 ms: 1.09x slower                                               |
| async_generators           | 390 ms                                                       | 431 ms: 1.10x slower                                                |
| json_dumps                 | 10.2 ms                                                      | 11.4 ms: 1.12x slower                                               |
| regex_v8                   | 23.6 ms                                                      | 26.4 ms: 1.12x slower                                               |
| telco                      | 6.96 ms                                                      | 7.92 ms: 1.14x slower                                               |
| typing_runtime_protocols   | 152 us                                                       | 175 us: 1.15x slower                                                |
| coverage                   | 66.7 ms                                                      | 77.4 ms: 1.16x slower                                               |
| mypy2                      | 830 ms                                                       | 1.02 sec: 1.23x slower                                              |
| python_startup             | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                               |
| create_gc_cycles           | 1.59 ms                                                      | 2.75 ms: 1.73x slower                                               |
| gc_traversal               | 3.48 ms                                                      | 6.06 ms: 1.74x slower                                               |
| bench_mp_pool              | 4.76 ms                                                      | 1.58 sec: 330.70x slower                                            |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                        |

Benchmark hidden because not significant (4): json, sqlglot_optimize, pycparser, richards
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250107-3.14.0a3+-f098037/bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.047x faster

# HPT report

- Reliability score: 99.68% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x