# Results vs. 3.12.0

- fork: python
- ref: v3.13.0
- machine: linux-x86_64
- commit hash: 60403a5
- commit date: 2024-10-07
- overall geometric mean: 1.017x slower
- HPT reliability: 84.11%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 293 ms: 1.03x slower                                         |
| chameleon      | 7.23 ms                                                      | 7.55 ms: 1.04x slower                                        |
| docutils       | 2.87 sec                                                     | 2.83 sec: 1.01x faster                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                 |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 831 ms: 1.27x faster                                         |
| async_tree_none_tg         | 431 ms                                                       | 346 ms: 1.24x faster                                         |
| async_tree_io              | 1.04 sec                                                     | 843 ms: 1.24x faster                                         |
| async_tree_none            | 452 ms                                                       | 376 ms: 1.20x faster                                         |
| async_tree_memoization     | 544 ms                                                       | 453 ms: 1.20x faster                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 581 ms: 1.20x faster                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 466 ms: 1.16x faster                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 604 ms: 1.15x faster                                         |
| Geometric mean             | (ref)                                                        | 1.21x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 252 ms: 1.05x faster                                         |
| float          | 76.6 ms                                                      | 81.3 ms: 1.06x slower                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 143 ms: 1.01x faster                                         |
| regex_effbot   | 3.57 ms                                                      | 3.67 ms: 1.03x slower                                        |
| regex_dna      | 239 ms                                                       | 247 ms: 1.03x slower                                         |
| regex_v8       | 23.6 ms                                                      | 26.1 ms: 1.11x slower                                        |
| Geometric mean | (ref)                                                        | 1.04x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 86.5 ms: 1.00x slower                                        |
| json_loads           | 24.4 us                                                      | 24.7 us: 1.01x slower                                        |
| pickle_pure_python   | 318 us                                                       | 323 us: 1.01x slower                                         |
| unpickle_pure_python | 210 us                                                       | 217 us: 1.04x slower                                         |
| xml_etree_parse      | 144 ms                                                       | 150 ms: 1.04x slower                                         |
| xml_etree_process    | 58.4 ms                                                      | 61.2 ms: 1.05x slower                                        |
| json_dumps           | 10.2 ms                                                      | 11.1 ms: 1.09x slower                                        |
| tomli_loads          | 2.16 sec                                                     | 2.46 sec: 1.14x slower                                       |
| Geometric mean       | (ref)                                                        | 1.04x slower                                                 |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.96 ms: 1.04x slower                                        |
| python_startup         | 11.6 ms                                                      | 15.9 ms: 1.37x slower                                        |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 36.4 ms: 1.05x faster                                        |
| mako            | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                        |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| comprehensions             | 21.9 us                                                      | 17.0 us: 1.29x faster                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 831 ms: 1.27x faster                                         |
| async_tree_none_tg         | 431 ms                                                       | 346 ms: 1.24x faster                                         |
| async_tree_io              | 1.04 sec                                                     | 843 ms: 1.24x faster                                         |
| async_tree_none            | 452 ms                                                       | 376 ms: 1.20x faster                                         |
| async_tree_memoization     | 544 ms                                                       | 453 ms: 1.20x faster                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 581 ms: 1.20x faster                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 466 ms: 1.16x faster                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 604 ms: 1.15x faster                                         |
| generators                 | 37.4 ms                                                      | 33.6 ms: 1.11x faster                                        |
| crypto_pyaes               | 80.3 ms                                                      | 73.3 ms: 1.10x faster                                        |
| raytrace                   | 298 ms                                                       | 273 ms: 1.09x faster                                         |
| logging_format             | 7.48 us                                                      | 6.94 us: 1.08x faster                                        |
| pathlib                    | 18.9 ms                                                      | 17.5 ms: 1.08x faster                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 148 ms: 1.07x faster                                         |
| coroutines                 | 23.0 ms                                                      | 21.6 ms: 1.07x faster                                        |
| chaos                      | 64.0 ms                                                      | 60.2 ms: 1.06x faster                                        |
| pidigits                   | 265 ms                                                       | 252 ms: 1.05x faster                                         |
| logging_simple             | 6.71 us                                                      | 6.39 us: 1.05x faster                                        |
| django_template            | 38.2 ms                                                      | 36.4 ms: 1.05x faster                                        |
| sympy_sum                  | 162 ms                                                       | 155 ms: 1.05x faster                                         |
| scimark_monte_carlo        | 69.0 ms                                                      | 66.1 ms: 1.04x faster                                        |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.3 ms: 1.03x faster                                        |
| sympy_integrate            | 23.9 ms                                                      | 23.6 ms: 1.02x faster                                        |
| docutils                   | 2.87 sec                                                     | 2.83 sec: 1.01x faster                                       |
| sympy_str                  | 302 ms                                                       | 298 ms: 1.01x faster                                         |
| mdp                        | 2.57 sec                                                     | 2.54 sec: 1.01x faster                                       |
| regex_compile              | 144 ms                                                       | 143 ms: 1.01x faster                                         |
| gunicorn                   | 1.00 ms                                                      | 992 us: 1.01x faster                                         |
| xml_etree_generate         | 86.1 ms                                                      | 86.5 ms: 1.00x slower                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.79 ms: 1.01x slower                                        |
| nqueens                    | 89.9 ms                                                      | 90.7 ms: 1.01x slower                                        |
| meteor_contest             | 128 ms                                                       | 130 ms: 1.01x slower                                         |
| json_loads                 | 24.4 us                                                      | 24.7 us: 1.01x slower                                        |
| pickle_pure_python         | 318 us                                                       | 323 us: 1.01x slower                                         |
| sqlglot_parse              | 1.38 ms                                                      | 1.40 ms: 1.02x slower                                        |
| 2to3                       | 285 ms                                                       | 293 ms: 1.03x slower                                         |
| regex_effbot               | 3.57 ms                                                      | 3.67 ms: 1.03x slower                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 59.3 ms: 1.03x slower                                        |
| sqlglot_normalize          | 116 ms                                                       | 119 ms: 1.03x slower                                         |
| regex_dna                  | 239 ms                                                       | 247 ms: 1.03x slower                                         |
| mako                       | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                        |
| logging_silent             | 94.4 ns                                                      | 97.9 ns: 1.04x slower                                        |
| python_startup_no_site     | 8.64 ms                                                      | 8.96 ms: 1.04x slower                                        |
| unpickle_pure_python       | 210 us                                                       | 217 us: 1.04x slower                                         |
| fannkuch                   | 350 ms                                                       | 363 ms: 1.04x slower                                         |
| pprint_pformat             | 1.65 sec                                                     | 1.72 sec: 1.04x slower                                       |
| dulwich_log                | 65.4 ms                                                      | 68.2 ms: 1.04x slower                                        |
| pprint_safe_repr           | 807 ms                                                       | 843 ms: 1.04x slower                                         |
| xml_etree_parse            | 144 ms                                                       | 150 ms: 1.04x slower                                         |
| chameleon                  | 7.23 ms                                                      | 7.55 ms: 1.04x slower                                        |
| sqlite_synth               | 2.77 us                                                      | 2.91 us: 1.05x slower                                        |
| xml_etree_process          | 58.4 ms                                                      | 61.2 ms: 1.05x slower                                        |
| deepcopy_memo              | 36.8 us                                                      | 38.6 us: 1.05x slower                                        |
| deepcopy_reduce            | 3.37 us                                                      | 3.54 us: 1.05x slower                                        |
| sympy_expand               | 484 ms                                                       | 509 ms: 1.05x slower                                         |
| deltablue                  | 3.24 ms                                                      | 3.42 ms: 1.06x slower                                        |
| spectral_norm              | 91.6 ms                                                      | 97.0 ms: 1.06x slower                                        |
| float                      | 76.6 ms                                                      | 81.3 ms: 1.06x slower                                        |
| deepcopy                   | 368 us                                                       | 392 us: 1.06x slower                                         |
| bench_mp_pool              | 4.76 ms                                                      | 5.12 ms: 1.08x slower                                        |
| go                         | 150 ms                                                       | 162 ms: 1.08x slower                                         |
| json_dumps                 | 10.2 ms                                                      | 11.1 ms: 1.09x slower                                        |
| scimark_fft                | 301 ms                                                       | 328 ms: 1.09x slower                                         |
| hexiom                     | 5.96 ms                                                      | 6.55 ms: 1.10x slower                                        |
| regex_v8                   | 23.6 ms                                                      | 26.1 ms: 1.11x slower                                        |
| json                       | 5.12 ms                                                      | 5.69 ms: 1.11x slower                                        |
| typing_runtime_protocols   | 152 us                                                       | 169 us: 1.11x slower                                         |
| scimark_sor                | 109 ms                                                       | 123 ms: 1.13x slower                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.77 ms: 1.13x slower                                        |
| tomli_loads                | 2.16 sec                                                     | 2.46 sec: 1.14x slower                                       |
| pyflate                    | 439 ms                                                       | 503 ms: 1.15x slower                                         |
| richards                   | 45.7 ms                                                      | 52.9 ms: 1.16x slower                                        |
| richards_super             | 51.3 ms                                                      | 59.6 ms: 1.16x slower                                        |
| async_generators           | 390 ms                                                       | 457 ms: 1.17x slower                                         |
| coverage                   | 66.7 ms                                                      | 80.0 ms: 1.20x slower                                        |
| telco                      | 6.96 ms                                                      | 8.79 ms: 1.26x slower                                        |
| gc_traversal               | 3.48 ms                                                      | 4.74 ms: 1.36x slower                                        |
| python_startup             | 11.6 ms                                                      | 15.9 ms: 1.37x slower                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.68 ms: 1.69x slower                                        |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                 |

Benchmark hidden because not significant (7): bench_thread_pool, tornado_http, scimark_lu, xml_etree_iterparse, asyncio_websockets, pycparser, nbody
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.017x slower

# HPT report

- Reliability score: 84.11% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.03x