# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a2
- machine: linux-x86_64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.084x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: 0.86x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 311 ms: 1.06x slower                                             |
| chameleon      | 7.49 ms                                                      | 7.90 ms: 1.05x slower                                            |
| docutils       | 2.81 sec                                                     | 2.93 sec: 1.05x slower                                           |
| tornado_http   | 119 ms                                                       | 124 ms: 1.04x slower                                             |
| Geometric mean | (ref)                                                        | 1.05x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| asyncio_websockets         | 395 ms                                                       | 387 ms: 1.02x faster                                             |
| async_generators           | 364 ms                                                       | 377 ms: 1.04x slower                                             |
| coroutines                 | 21.6 ms                                                      | 22.6 ms: 1.05x slower                                            |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 711 ms: 1.19x slower                                             |
| async_tree_none            | 370 ms                                                       | 447 ms: 1.21x slower                                             |
| async_tree_memoization     | 447 ms                                                       | 561 ms: 1.25x slower                                             |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 725 ms: 1.26x slower                                             |
| async_tree_memoization_tg  | 458 ms                                                       | 586 ms: 1.28x slower                                             |
| async_tree_io              | 832 ms                                                       | 1.09 sec: 1.32x slower                                           |
| async_tree_none_tg         | 342 ms                                                       | 453 ms: 1.33x slower                                             |
| async_tree_io_tg           | 823 ms                                                       | 1.11 sec: 1.35x slower                                           |
| Geometric mean             | (ref)                                                        | 1.20x slower                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pidigits       | 252 ms                                                       | 267 ms: 1.06x slower                                             |
| float          | 81.6 ms                                                      | 92.5 ms: 1.13x slower                                            |
| nbody          | 92.1 ms                                                      | 112 ms: 1.22x slower                                             |
| Geometric mean | (ref)                                                        | 1.14x slower                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_dna      | 238 ms                                                       | 249 ms: 1.05x slower                                             |
| regex_compile  | 143 ms                                                       | 172 ms: 1.20x slower                                             |
| Geometric mean | (ref)                                                        | 1.06x slower                                                     |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_pure_python   | 322 us                                                       | 312 us: 1.03x faster                                             |
| json_dumps           | 10.8 ms                                                      | 10.7 ms: 1.01x faster                                            |
| json_loads           | 24.7 us                                                      | 25.3 us: 1.02x slower                                            |
| xml_etree_generate   | 85.2 ms                                                      | 90.1 ms: 1.06x slower                                            |
| unpickle_pure_python | 216 us                                                       | 231 us: 1.07x slower                                             |
| tomli_loads          | 2.43 sec                                                     | 2.61 sec: 1.07x slower                                           |
| xml_etree_parse      | 144 ms                                                       | 157 ms: 1.09x slower                                             |
| xml_etree_iterparse  | 99.8 ms                                                      | 117 ms: 1.17x slower                                             |
| Geometric mean       | (ref)                                                        | 1.05x slower                                                     |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 12.9 ms: 1.21x faster                                            |
| python_startup_no_site | 8.93 ms                                                      | 11.3 ms: 1.27x slower                                            |
| Geometric mean         | (ref)                                                        | 1.02x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako      | 10.3 ms                                                      | 13.6 ms: 1.32x slower                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| create_gc_cycles           | 2.65 ms                                                      | 1.61 ms: 1.65x faster                                            |
| typing_runtime_protocols   | 176 us                                                       | 133 us: 1.32x faster                                             |
| python_startup             | 15.6 ms                                                      | 12.9 ms: 1.21x faster                                            |
| gc_traversal               | 4.48 ms                                                      | 3.76 ms: 1.19x faster                                            |
| mypy2                      | 1.02 sec                                                     | 893 ms: 1.15x faster                                             |
| coverage                   | 84.5 ms                                                      | 78.8 ms: 1.07x faster                                            |
| json                       | 5.62 ms                                                      | 5.30 ms: 1.06x faster                                            |
| deepcopy                   | 388 us                                                       | 366 us: 1.06x faster                                             |
| deepcopy_reduce            | 3.49 us                                                      | 3.35 us: 1.04x faster                                            |
| telco                      | 8.77 ms                                                      | 8.47 ms: 1.04x faster                                            |
| richards_super             | 60.2 ms                                                      | 58.4 ms: 1.03x faster                                            |
| pickle_pure_python         | 322 us                                                       | 312 us: 1.03x faster                                             |
| asyncio_websockets         | 395 ms                                                       | 387 ms: 1.02x faster                                             |
| richards                   | 52.5 ms                                                      | 51.6 ms: 1.02x faster                                            |
| json_dumps                 | 10.8 ms                                                      | 10.7 ms: 1.01x faster                                            |
| deepcopy_memo              | 38.9 us                                                      | 38.6 us: 1.01x faster                                            |
| logging_silent             | 97.5 ns                                                      | 98.7 ns: 1.01x slower                                            |
| json_loads                 | 24.7 us                                                      | 25.3 us: 1.02x slower                                            |
| generators                 | 33.9 ms                                                      | 35.0 ms: 1.03x slower                                            |
| async_generators           | 364 ms                                                       | 377 ms: 1.04x slower                                             |
| pycparser                  | 1.28 sec                                                     | 1.33 sec: 1.04x slower                                           |
| tornado_http               | 119 ms                                                       | 124 ms: 1.04x slower                                             |
| mdp                        | 2.53 sec                                                     | 2.63 sec: 1.04x slower                                           |
| sqlglot_normalize          | 119 ms                                                       | 124 ms: 1.04x slower                                             |
| docutils                   | 2.81 sec                                                     | 2.93 sec: 1.05x slower                                           |
| regex_dna                  | 238 ms                                                       | 249 ms: 1.05x slower                                             |
| coroutines                 | 21.6 ms                                                      | 22.6 ms: 1.05x slower                                            |
| meteor_contest             | 130 ms                                                       | 137 ms: 1.05x slower                                             |
| pprint_safe_repr           | 835 ms                                                       | 880 ms: 1.05x slower                                             |
| chameleon                  | 7.49 ms                                                      | 7.90 ms: 1.05x slower                                            |
| xml_etree_generate         | 85.2 ms                                                      | 90.1 ms: 1.06x slower                                            |
| sympy_expand               | 506 ms                                                       | 535 ms: 1.06x slower                                             |
| bench_thread_pool          | 929 us                                                       | 985 us: 1.06x slower                                             |
| pidigits                   | 252 ms                                                       | 267 ms: 1.06x slower                                             |
| 2to3                       | 293 ms                                                       | 311 ms: 1.06x slower                                             |
| logging_format             | 6.95 us                                                      | 7.40 us: 1.06x slower                                            |
| sympy_integrate            | 23.4 ms                                                      | 24.9 ms: 1.07x slower                                            |
| pprint_pformat             | 1.70 sec                                                     | 1.81 sec: 1.07x slower                                           |
| unpickle_pure_python       | 216 us                                                       | 231 us: 1.07x slower                                             |
| tomli_loads                | 2.43 sec                                                     | 2.61 sec: 1.07x slower                                           |
| go                         | 167 ms                                                       | 179 ms: 1.07x slower                                             |
| sqlglot_transpile          | 1.76 ms                                                      | 1.90 ms: 1.08x slower                                            |
| sqlglot_optimize           | 58.7 ms                                                      | 63.2 ms: 1.08x slower                                            |
| scimark_lu                 | 97.4 ms                                                      | 105 ms: 1.08x slower                                             |
| logging_simple             | 6.28 us                                                      | 6.80 us: 1.08x slower                                            |
| sympy_str                  | 297 ms                                                       | 322 ms: 1.09x slower                                             |
| sympy_sum                  | 154 ms                                                       | 167 ms: 1.09x slower                                             |
| sqlglot_parse              | 1.37 ms                                                      | 1.49 ms: 1.09x slower                                            |
| xml_etree_parse            | 144 ms                                                       | 157 ms: 1.09x slower                                             |
| crypto_pyaes               | 73.5 ms                                                      | 80.6 ms: 1.10x slower                                            |
| dulwich_log                | 65.5 ms                                                      | 72.0 ms: 1.10x slower                                            |
| pathlib                    | 17.4 ms                                                      | 19.3 ms: 1.11x slower                                            |
| raytrace                   | 267 ms                                                       | 299 ms: 1.12x slower                                             |
| pyflate                    | 493 ms                                                       | 557 ms: 1.13x slower                                             |
| float                      | 81.6 ms                                                      | 92.5 ms: 1.13x slower                                            |
| nqueens                    | 92.3 ms                                                      | 105 ms: 1.14x slower                                             |
| xml_etree_iterparse        | 99.8 ms                                                      | 117 ms: 1.17x slower                                             |
| fannkuch                   | 384 ms                                                       | 453 ms: 1.18x slower                                             |
| scimark_sor                | 125 ms                                                       | 149 ms: 1.19x slower                                             |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 711 ms: 1.19x slower                                             |
| regex_compile              | 143 ms                                                       | 172 ms: 1.20x slower                                             |
| async_tree_none            | 370 ms                                                       | 447 ms: 1.21x slower                                             |
| chaos                      | 60.6 ms                                                      | 73.3 ms: 1.21x slower                                            |
| nbody                      | 92.1 ms                                                      | 112 ms: 1.22x slower                                             |
| async_tree_memoization     | 447 ms                                                       | 561 ms: 1.25x slower                                             |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 725 ms: 1.26x slower                                             |
| python_startup_no_site     | 8.93 ms                                                      | 11.3 ms: 1.27x slower                                            |
| async_tree_memoization_tg  | 458 ms                                                       | 586 ms: 1.28x slower                                             |
| async_tree_io              | 832 ms                                                       | 1.09 sec: 1.32x slower                                           |
| mako                       | 10.3 ms                                                      | 13.6 ms: 1.32x slower                                            |
| async_tree_none_tg         | 342 ms                                                       | 453 ms: 1.33x slower                                             |
| scimark_monte_carlo        | 65.2 ms                                                      | 87.4 ms: 1.34x slower                                            |
| comprehensions             | 17.3 us                                                      | 23.3 us: 1.35x slower                                            |
| async_tree_io_tg           | 823 ms                                                       | 1.11 sec: 1.35x slower                                           |
| scimark_fft                | 298 ms                                                       | 407 ms: 1.36x slower                                             |
| hexiom                     | 6.47 ms                                                      | 9.10 ms: 1.41x slower                                            |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 6.01 ms: 1.43x slower                                            |
| deltablue                  | 3.38 ms                                                      | 4.98 ms: 1.47x slower                                            |
| spectral_norm              | 97.4 ms                                                      | 144 ms: 1.47x slower                                             |
| Geometric mean             | (ref)                                                        | 1.09x slower                                                     |

Benchmark hidden because not significant (4): bench_mp_pool, regex_v8, regex_effbot, xml_etree_process
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, connected_components, django_template, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, pylint, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, thrift
Ignored benchmarks (10) of results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json: asyncio_tcp, asyncio_tcp_ssl, dask, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.084x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: 0.86x