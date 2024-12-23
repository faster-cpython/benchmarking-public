# Results vs. 3.12.0

- fork: python
- ref: 2a66dd33dfc0b845042d
- machine: linux-x86_64
- commit hash: 2a66dd3
- commit date: 2024-12-20
- overall geometric mean: 1.191x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x slower
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 386 ms: 1.35x slower                                                         |
| docutils       | 2.87 sec                                                     | 3.12 sec: 1.09x slower                                                       |
| Geometric mean | (ref)                                                        | 1.21x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 745 ms: 1.41x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 322 ms: 1.34x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 783 ms: 1.33x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 413 ms: 1.31x faster                                                         |
| async_tree_none            | 452 ms                                                       | 360 ms: 1.26x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 445 ms: 1.22x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 577 ms: 1.21x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 610 ms: 1.14x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.27x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 247 ms: 1.07x faster                                                         |
| float          | 76.6 ms                                                      | 108 ms: 1.42x slower                                                         |
| nbody          | 88.0 ms                                                      | 129 ms: 1.47x slower                                                         |
| Geometric mean | (ref)                                                        | 1.25x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.29 ms: 1.09x faster                                                        |
| regex_dna      | 239 ms                                                       | 242 ms: 1.02x slower                                                         |
| regex_v8       | 23.6 ms                                                      | 26.4 ms: 1.12x slower                                                        |
| regex_compile  | 144 ms                                                       | 173 ms: 1.20x slower                                                         |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 92.5 ms: 1.11x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 134 ms: 1.07x faster                                                         |
| json_loads           | 24.4 us                                                      | 27.6 us: 1.13x slower                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 99.6 ms: 1.16x slower                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.62 sec: 1.21x slower                                                       |
| xml_etree_process    | 58.4 ms                                                      | 75.7 ms: 1.30x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 14.3 ms: 1.40x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 321 us: 1.53x slower                                                         |
| pickle_pure_python   | 318 us                                                       | 506 us: 1.59x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.22x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 12.2 ms: 1.41x slower                                                        |
| python_startup         | 11.6 ms                                                      | 19.6 ms: 1.69x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.54x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 53.9 ms: 1.41x slower                                                        |
| mako            | 10.0 ms                                                      | 19.6 ms: 1.96x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.66x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 745 ms: 1.41x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 322 ms: 1.34x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 783 ms: 1.33x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 413 ms: 1.31x faster                                                         |
| async_tree_none            | 452 ms                                                       | 360 ms: 1.26x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 445 ms: 1.22x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 577 ms: 1.21x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 610 ms: 1.14x faster                                                         |
| xml_etree_iterparse        | 103 ms                                                       | 92.5 ms: 1.11x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 17.3 ms: 1.09x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.29 ms: 1.09x faster                                                        |
| deepcopy                   | 368 us                                                       | 343 us: 1.07x faster                                                         |
| pidigits                   | 265 ms                                                       | 247 ms: 1.07x faster                                                         |
| xml_etree_parse            | 144 ms                                                       | 134 ms: 1.07x faster                                                         |
| sqlite_synth               | 2.77 us                                                      | 2.67 us: 1.04x faster                                                        |
| asyncio_websockets         | 387 ms                                                       | 378 ms: 1.02x faster                                                         |
| coroutines                 | 23.0 ms                                                      | 23.1 ms: 1.01x slower                                                        |
| regex_dna                  | 239 ms                                                       | 242 ms: 1.02x slower                                                         |
| generators                 | 37.4 ms                                                      | 38.6 ms: 1.03x slower                                                        |
| json                       | 5.12 ms                                                      | 5.47 ms: 1.07x slower                                                        |
| deepcopy_memo              | 36.8 us                                                      | 39.4 us: 1.07x slower                                                        |
| docutils                   | 2.87 sec                                                     | 3.12 sec: 1.09x slower                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 3.70 us: 1.10x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 3.87 ms: 1.11x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 26.4 ms: 1.12x slower                                                        |
| spectral_norm              | 91.6 ms                                                      | 102 ms: 1.12x slower                                                         |
| mdp                        | 2.57 sec                                                     | 2.88 sec: 1.12x slower                                                       |
| scimark_fft                | 301 ms                                                       | 341 ms: 1.13x slower                                                         |
| json_loads                 | 24.4 us                                                      | 27.6 us: 1.13x slower                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 99.6 ms: 1.16x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.46 sec: 1.18x slower                                                       |
| dulwich_log                | 65.4 ms                                                      | 78.4 ms: 1.20x slower                                                        |
| regex_compile              | 144 ms                                                       | 173 ms: 1.20x slower                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                      | 22.6 ms: 1.21x slower                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.62 sec: 1.21x slower                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 98.6 ms: 1.23x slower                                                        |
| meteor_contest             | 128 ms                                                       | 158 ms: 1.23x slower                                                         |
| comprehensions             | 21.9 us                                                      | 27.1 us: 1.24x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 111 ms: 1.24x slower                                                         |
| sqlglot_normalize          | 116 ms                                                       | 146 ms: 1.26x slower                                                         |
| sqlglot_optimize           | 57.5 ms                                                      | 72.5 ms: 1.26x slower                                                        |
| sympy_integrate            | 23.9 ms                                                      | 30.2 ms: 1.26x slower                                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 204 ms: 1.28x slower                                                         |
| pprint_safe_repr           | 807 ms                                                       | 1.03 sec: 1.28x slower                                                       |
| xml_etree_process          | 58.4 ms                                                      | 75.7 ms: 1.30x slower                                                        |
| logging_format             | 7.48 us                                                      | 9.71 us: 1.30x slower                                                        |
| logging_simple             | 6.71 us                                                      | 8.79 us: 1.31x slower                                                        |
| pprint_pformat             | 1.65 sec                                                     | 2.17 sec: 1.31x slower                                                       |
| async_generators           | 390 ms                                                       | 515 ms: 1.32x slower                                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.60 ms: 1.33x slower                                                        |
| sympy_str                  | 302 ms                                                       | 403 ms: 1.33x slower                                                         |
| telco                      | 6.96 ms                                                      | 9.42 ms: 1.35x slower                                                        |
| 2to3                       | 285 ms                                                       | 386 ms: 1.35x slower                                                         |
| scimark_lu                 | 98.8 ms                                                      | 135 ms: 1.37x slower                                                         |
| json_dumps                 | 10.2 ms                                                      | 14.3 ms: 1.40x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 12.2 ms: 1.41x slower                                                        |
| django_template            | 38.2 ms                                                      | 53.9 ms: 1.41x slower                                                        |
| float                      | 76.6 ms                                                      | 108 ms: 1.42x slower                                                         |
| fannkuch                   | 350 ms                                                       | 497 ms: 1.42x slower                                                         |
| nbody                      | 88.0 ms                                                      | 129 ms: 1.47x slower                                                         |
| pyflate                    | 439 ms                                                       | 646 ms: 1.47x slower                                                         |
| typing_runtime_protocols   | 152 us                                                       | 224 us: 1.48x slower                                                         |
| sympy_sum                  | 162 ms                                                       | 240 ms: 1.48x slower                                                         |
| chaos                      | 64.0 ms                                                      | 95.2 ms: 1.49x slower                                                        |
| sympy_expand               | 484 ms                                                       | 734 ms: 1.52x slower                                                         |
| unpickle_pure_python       | 210 us                                                       | 321 us: 1.53x slower                                                         |
| richards_super             | 51.3 ms                                                      | 78.9 ms: 1.54x slower                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 107 ms: 1.55x slower                                                         |
| richards                   | 45.7 ms                                                      | 71.3 ms: 1.56x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 9.31 ms: 1.56x slower                                                        |
| mypy2                      | 830 ms                                                       | 1.31 sec: 1.58x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 2.82 ms: 1.59x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 506 us: 1.59x slower                                                         |
| raytrace                   | 298 ms                                                       | 480 ms: 1.61x slower                                                         |
| coverage                   | 66.7 ms                                                      | 108 ms: 1.62x slower                                                         |
| go                         | 150 ms                                                       | 244 ms: 1.63x slower                                                         |
| bench_thread_pool          | 950 us                                                       | 1.55 ms: 1.63x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.68 ms: 1.68x slower                                                        |
| python_startup             | 11.6 ms                                                      | 19.6 ms: 1.69x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 162 ns: 1.72x slower                                                         |
| sqlglot_parse              | 1.38 ms                                                      | 2.37 ms: 1.72x slower                                                        |
| scimark_sor                | 109 ms                                                       | 195 ms: 1.79x slower                                                         |
| mako                       | 10.0 ms                                                      | 19.6 ms: 1.96x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 7.15 ms: 2.21x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 53.7 ms: 11.27x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.28x slower                                                                 |
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241220-3.14.0a3+-2a66dd3-NOGIL/bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.191x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.19x
- 95% likely to have a slowdown of 1.17x
- 99% likely to have a slowdown of 1.13x

# Memory
- memory change: 1.25x