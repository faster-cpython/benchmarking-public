# Results vs. 3.12.0

- fork: python
- ref: v3.13.1
- machine: linux-x86_64
- commit hash: 0671451
- commit date: 2024-12-03
- overall geometric mean: 1.015x slower
- HPT reliability: 74.77%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241203-pythonperf2-x86_64-python-v3.13.1-3.13.1-0671451 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 293 ms: 1.03x slower                                         |
| chameleon      | 7.23 ms                                                      | 7.48 ms: 1.03x slower                                        |
| docutils       | 2.87 sec                                                     | 2.82 sec: 1.02x faster                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                 |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241203-pythonperf2-x86_64-python-v3.13.1-3.13.1-0671451 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 824 ms: 1.28x faster                                         |
| async_tree_none_tg         | 431 ms                                                       | 337 ms: 1.28x faster                                         |
| async_tree_io              | 1.04 sec                                                     | 836 ms: 1.25x faster                                         |
| async_tree_none            | 452 ms                                                       | 374 ms: 1.21x faster                                         |
| async_tree_memoization     | 544 ms                                                       | 454 ms: 1.20x faster                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 452 ms: 1.20x faster                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 604 ms: 1.15x faster                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 607 ms: 1.15x faster                                         |
| Geometric mean             | (ref)                                                        | 1.21x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241203-pythonperf2-x86_64-python-v3.13.1-3.13.1-0671451 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 252 ms: 1.05x faster                                         |
| float          | 76.6 ms                                                      | 79.7 ms: 1.04x slower                                        |
| Geometric mean | (ref)                                                        | 1.00x faster                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241203-pythonperf2-x86_64-python-v3.13.1-3.13.1-0671451 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.51 ms: 1.02x faster                                        |
| regex_compile  | 144 ms                                                       | 143 ms: 1.01x faster                                         |
| regex_dna      | 239 ms                                                       | 250 ms: 1.05x slower                                         |
| regex_v8       | 23.6 ms                                                      | 25.9 ms: 1.10x slower                                        |
| Geometric mean | (ref)                                                        | 1.03x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241203-pythonperf2-x86_64-python-v3.13.1-3.13.1-0671451 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 101 ms: 1.01x faster                                         |
| unpickle_pure_python | 210 us                                                       | 211 us: 1.01x slower                                         |
| xml_etree_generate   | 86.1 ms                                                      | 87.5 ms: 1.02x slower                                        |
| pickle_pure_python   | 318 us                                                       | 326 us: 1.02x slower                                         |
| xml_etree_parse      | 144 ms                                                       | 149 ms: 1.04x slower                                         |
| json_loads           | 24.4 us                                                      | 25.3 us: 1.04x slower                                        |
| tomli_loads          | 2.16 sec                                                     | 2.25 sec: 1.04x slower                                       |
| xml_etree_process    | 58.4 ms                                                      | 61.5 ms: 1.05x slower                                        |
| json_dumps           | 10.2 ms                                                      | 11.0 ms: 1.08x slower                                        |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241203-pythonperf2-x86_64-python-v3.13.1-3.13.1-0671451 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.02 ms: 1.04x slower                                        |
| python_startup         | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                        |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241203-pythonperf2-x86_64-python-v3.13.1-3.13.1-0671451 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 36.3 ms: 1.05x faster                                        |
| mako            | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                        |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241203-pythonperf2-x86_64-python-v3.13.1-3.13.1-0671451 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 824 ms: 1.28x faster                                         |
| async_tree_none_tg         | 431 ms                                                       | 337 ms: 1.28x faster                                         |
| async_tree_io              | 1.04 sec                                                     | 836 ms: 1.25x faster                                         |
| comprehensions             | 21.9 us                                                      | 17.6 us: 1.24x faster                                        |
| async_tree_none            | 452 ms                                                       | 374 ms: 1.21x faster                                         |
| async_tree_memoization     | 544 ms                                                       | 454 ms: 1.20x faster                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 452 ms: 1.20x faster                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 604 ms: 1.15x faster                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 607 ms: 1.15x faster                                         |
| generators                 | 37.4 ms                                                      | 32.8 ms: 1.14x faster                                        |
| raytrace                   | 298 ms                                                       | 268 ms: 1.11x faster                                         |
| coroutines                 | 23.0 ms                                                      | 20.9 ms: 1.10x faster                                        |
| crypto_pyaes               | 80.3 ms                                                      | 73.5 ms: 1.09x faster                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 147 ms: 1.08x faster                                         |
| chaos                      | 64.0 ms                                                      | 59.2 ms: 1.08x faster                                        |
| pathlib                    | 18.9 ms                                                      | 17.6 ms: 1.08x faster                                        |
| django_template            | 38.2 ms                                                      | 36.3 ms: 1.05x faster                                        |
| pidigits                   | 265 ms                                                       | 252 ms: 1.05x faster                                         |
| scimark_monte_carlo        | 69.0 ms                                                      | 65.8 ms: 1.05x faster                                        |
| sympy_sum                  | 162 ms                                                       | 156 ms: 1.04x faster                                         |
| logging_format             | 7.48 us                                                      | 7.22 us: 1.04x faster                                        |
| mdp                        | 2.57 sec                                                     | 2.49 sec: 1.03x faster                                       |
| nqueens                    | 89.9 ms                                                      | 87.4 ms: 1.03x faster                                        |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.3 ms: 1.02x faster                                        |
| sympy_integrate            | 23.9 ms                                                      | 23.5 ms: 1.02x faster                                        |
| regex_effbot               | 3.57 ms                                                      | 3.51 ms: 1.02x faster                                        |
| docutils                   | 2.87 sec                                                     | 2.82 sec: 1.02x faster                                       |
| xml_etree_iterparse        | 103 ms                                                       | 101 ms: 1.01x faster                                         |
| gunicorn                   | 1.00 ms                                                      | 990 us: 1.01x faster                                         |
| sympy_str                  | 302 ms                                                       | 299 ms: 1.01x faster                                         |
| logging_simple             | 6.71 us                                                      | 6.65 us: 1.01x faster                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.37 ms: 1.01x faster                                        |
| regex_compile              | 144 ms                                                       | 143 ms: 1.01x faster                                         |
| unpickle_pure_python       | 210 us                                                       | 211 us: 1.01x slower                                         |
| scimark_lu                 | 98.8 ms                                                      | 99.8 ms: 1.01x slower                                        |
| asyncio_websockets         | 387 ms                                                       | 392 ms: 1.01x slower                                         |
| meteor_contest             | 128 ms                                                       | 130 ms: 1.01x slower                                         |
| xml_etree_generate         | 86.1 ms                                                      | 87.5 ms: 1.02x slower                                        |
| logging_silent             | 94.4 ns                                                      | 96.2 ns: 1.02x slower                                        |
| dulwich_log                | 65.4 ms                                                      | 66.8 ms: 1.02x slower                                        |
| pickle_pure_python         | 318 us                                                       | 326 us: 1.02x slower                                         |
| sqlglot_normalize          | 116 ms                                                       | 119 ms: 1.03x slower                                         |
| 2to3                       | 285 ms                                                       | 293 ms: 1.03x slower                                         |
| sqlglot_optimize           | 57.5 ms                                                      | 59.4 ms: 1.03x slower                                        |
| pprint_safe_repr           | 807 ms                                                       | 835 ms: 1.03x slower                                         |
| chameleon                  | 7.23 ms                                                      | 7.48 ms: 1.03x slower                                        |
| xml_etree_parse            | 144 ms                                                       | 149 ms: 1.04x slower                                         |
| mako                       | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                        |
| json_loads                 | 24.4 us                                                      | 25.3 us: 1.04x slower                                        |
| tomli_loads                | 2.16 sec                                                     | 2.25 sec: 1.04x slower                                       |
| float                      | 76.6 ms                                                      | 79.7 ms: 1.04x slower                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.72 sec: 1.04x slower                                       |
| deltablue                  | 3.24 ms                                                      | 3.38 ms: 1.04x slower                                        |
| python_startup_no_site     | 8.64 ms                                                      | 9.02 ms: 1.04x slower                                        |
| regex_dna                  | 239 ms                                                       | 250 ms: 1.05x slower                                         |
| spectral_norm              | 91.6 ms                                                      | 96.2 ms: 1.05x slower                                        |
| xml_etree_process          | 58.4 ms                                                      | 61.5 ms: 1.05x slower                                        |
| sqlite_synth               | 2.77 us                                                      | 2.93 us: 1.05x slower                                        |
| fannkuch                   | 350 ms                                                       | 370 ms: 1.06x slower                                         |
| sympy_expand               | 484 ms                                                       | 512 ms: 1.06x slower                                         |
| deepcopy_reduce            | 3.37 us                                                      | 3.58 us: 1.06x slower                                        |
| bench_mp_pool              | 4.76 ms                                                      | 5.08 ms: 1.07x slower                                        |
| hexiom                     | 5.96 ms                                                      | 6.38 ms: 1.07x slower                                        |
| json_dumps                 | 10.2 ms                                                      | 11.0 ms: 1.08x slower                                        |
| deepcopy_memo              | 36.8 us                                                      | 39.8 us: 1.08x slower                                        |
| go                         | 150 ms                                                       | 162 ms: 1.08x slower                                         |
| json                       | 5.12 ms                                                      | 5.54 ms: 1.08x slower                                        |
| scimark_fft                | 301 ms                                                       | 326 ms: 1.08x slower                                         |
| deepcopy                   | 368 us                                                       | 401 us: 1.09x slower                                         |
| regex_v8                   | 23.6 ms                                                      | 25.9 ms: 1.10x slower                                        |
| pyflate                    | 439 ms                                                       | 495 ms: 1.13x slower                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.76 ms: 1.13x slower                                        |
| richards                   | 45.7 ms                                                      | 52.0 ms: 1.14x slower                                        |
| async_generators           | 390 ms                                                       | 445 ms: 1.14x slower                                         |
| scimark_sor                | 109 ms                                                       | 125 ms: 1.15x slower                                         |
| richards_super             | 51.3 ms                                                      | 58.9 ms: 1.15x slower                                        |
| typing_runtime_protocols   | 152 us                                                       | 175 us: 1.15x slower                                         |
| coverage                   | 66.7 ms                                                      | 82.7 ms: 1.24x slower                                        |
| telco                      | 6.96 ms                                                      | 8.93 ms: 1.28x slower                                        |
| python_startup             | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                        |
| gc_traversal               | 3.48 ms                                                      | 4.94 ms: 1.42x slower                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.68 ms: 1.69x slower                                        |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                 |

Benchmark hidden because not significant (5): bench_thread_pool, tornado_http, sqlglot_transpile, pycparser, nbody
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20241203-3.13.1-0671451/bm-20241203-pythonperf2-x86_64-python-v3.13.1-3.13.1-0671451.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.015x slower

# HPT report

- Reliability score: 74.77% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.03x