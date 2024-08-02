# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a2
- machine: linux-x86_64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.09x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: 0.94x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 311 ms: 1.07x slower                                             |
| chameleon      | 7.40 ms                                                          | 7.90 ms: 1.07x slower                                            |
| docutils       | 2.98 sec                                                         | 2.93 sec: 1.02x faster                                           |
| tornado_http   | 119 ms                                                           | 124 ms: 1.04x slower                                             |
| Geometric mean | (ref)                                                            | 1.04x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 604 ms                                                           | 711 ms: 1.18x slower                                             |
| async_tree_memoization     | 460 ms                                                           | 561 ms: 1.22x slower                                             |
| async_tree_none            | 365 ms                                                           | 447 ms: 1.22x slower                                             |
| async_tree_io_tg           | 900 ms                                                           | 1.11 sec: 1.24x slower                                           |
| async_tree_io              | 873 ms                                                           | 1.09 sec: 1.25x slower                                           |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 725 ms: 1.27x slower                                             |
| async_tree_none_tg         | 340 ms                                                           | 453 ms: 1.33x slower                                             |
| async_tree_memoization_tg  | 421 ms                                                           | 586 ms: 1.39x slower                                             |
| Geometric mean             | (ref)                                                            | 1.26x slower                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| pidigits       | 254 ms                                                           | 267 ms: 1.05x slower                                             |
| float          | 80.2 ms                                                          | 92.5 ms: 1.15x slower                                            |
| nbody          | 87.8 ms                                                          | 112 ms: 1.28x slower                                             |
| Geometric mean | (ref)                                                            | 1.16x slower                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_v8       | 26.0 ms                                                          | 24.9 ms: 1.04x faster                                            |
| regex_effbot   | 3.40 ms                                                          | 3.51 ms: 1.03x slower                                            |
| regex_compile  | 144 ms                                                           | 172 ms: 1.19x slower                                             |
| Geometric mean | (ref)                                                            | 1.04x slower                                                     |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle               | 10.6 us                                                          | 9.98 us: 1.06x faster                                            |
| pickle_list          | 4.44 us                                                          | 4.27 us: 1.04x faster                                            |
| pickle_dict          | 32.8 us                                                          | 31.8 us: 1.03x faster                                            |
| unpickle             | 15.7 us                                                          | 15.2 us: 1.03x faster                                            |
| unpickle_list        | 4.70 us                                                          | 4.56 us: 1.03x faster                                            |
| json_dumps           | 10.8 ms                                                          | 10.7 ms: 1.01x faster                                            |
| json_loads           | 25.0 us                                                          | 25.3 us: 1.01x slower                                            |
| pickle_pure_python   | 307 us                                                           | 312 us: 1.02x slower                                             |
| xml_etree_process    | 59.7 ms                                                          | 60.9 ms: 1.02x slower                                            |
| unpickle_pure_python | 224 us                                                           | 231 us: 1.03x slower                                             |
| xml_etree_generate   | 85.7 ms                                                          | 90.1 ms: 1.05x slower                                            |
| tomli_loads          | 2.40 sec                                                         | 2.61 sec: 1.08x slower                                           |
| xml_etree_parse      | 144 ms                                                           | 157 ms: 1.10x slower                                             |
| xml_etree_iterparse  | 103 ms                                                           | 117 ms: 1.14x slower                                             |
| Geometric mean       | (ref)                                                            | 1.02x slower                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 12.9 ms: 1.02x faster                                            |
| python_startup_no_site | 8.85 ms                                                          | 11.3 ms: 1.28x slower                                            |
| Geometric mean         | (ref)                                                            | 1.12x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako      | 10.4 ms                                                          | 13.6 ms: 1.31x slower                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols   | 171 us                                                           | 133 us: 1.28x faster                                             |
| gc_traversal               | 4.69 ms                                                          | 3.76 ms: 1.25x faster                                            |
| create_gc_cycles           | 2.00 ms                                                          | 1.61 ms: 1.24x faster                                            |
| pickle                     | 10.6 us                                                          | 9.98 us: 1.06x faster                                            |
| coverage                   | 83.5 ms                                                          | 78.8 ms: 1.06x faster                                            |
| richards_super             | 61.2 ms                                                          | 58.4 ms: 1.05x faster                                            |
| regex_v8                   | 26.0 ms                                                          | 24.9 ms: 1.04x faster                                            |
| pickle_list                | 4.44 us                                                          | 4.27 us: 1.04x faster                                            |
| richards                   | 53.4 ms                                                          | 51.6 ms: 1.03x faster                                            |
| pickle_dict                | 32.8 us                                                          | 31.8 us: 1.03x faster                                            |
| unpickle                   | 15.7 us                                                          | 15.2 us: 1.03x faster                                            |
| unpickle_list              | 4.70 us                                                          | 4.56 us: 1.03x faster                                            |
| deepcopy                   | 377 us                                                           | 366 us: 1.03x faster                                             |
| python_startup             | 13.2 ms                                                          | 12.9 ms: 1.02x faster                                            |
| asyncio_websockets         | 395 ms                                                           | 387 ms: 1.02x faster                                             |
| docutils                   | 2.98 sec                                                         | 2.93 sec: 1.02x faster                                           |
| asyncio_tcp                | 378 ms                                                           | 373 ms: 1.01x faster                                             |
| deepcopy_reduce            | 3.39 us                                                          | 3.35 us: 1.01x faster                                            |
| json                       | 5.35 ms                                                          | 5.30 ms: 1.01x faster                                            |
| json_dumps                 | 10.8 ms                                                          | 10.7 ms: 1.01x faster                                            |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.59 sec: 1.00x slower                                           |
| json_loads                 | 25.0 us                                                          | 25.3 us: 1.01x slower                                            |
| sqlite_synth               | 2.80 us                                                          | 2.83 us: 1.01x slower                                            |
| pickle_pure_python         | 307 us                                                           | 312 us: 1.02x slower                                             |
| xml_etree_process          | 59.7 ms                                                          | 60.9 ms: 1.02x slower                                            |
| logging_silent             | 96.3 ns                                                          | 98.7 ns: 1.03x slower                                            |
| coroutines                 | 22.0 ms                                                          | 22.6 ms: 1.03x slower                                            |
| unpickle_pure_python       | 224 us                                                           | 231 us: 1.03x slower                                             |
| sqlglot_normalize          | 120 ms                                                           | 124 ms: 1.03x slower                                             |
| regex_effbot               | 3.40 ms                                                          | 3.51 ms: 1.03x slower                                            |
| deepcopy_memo              | 37.3 us                                                          | 38.6 us: 1.04x slower                                            |
| tornado_http               | 119 ms                                                           | 124 ms: 1.04x slower                                             |
| async_generators           | 363 ms                                                           | 377 ms: 1.04x slower                                             |
| logging_format             | 7.11 us                                                          | 7.40 us: 1.04x slower                                            |
| generators                 | 33.5 ms                                                          | 35.0 ms: 1.04x slower                                            |
| xml_etree_generate         | 85.7 ms                                                          | 90.1 ms: 1.05x slower                                            |
| dask                       | 391 ms                                                           | 411 ms: 1.05x slower                                             |
| pidigits                   | 254 ms                                                           | 267 ms: 1.05x slower                                             |
| sqlglot_optimize           | 59.5 ms                                                          | 63.2 ms: 1.06x slower                                            |
| logging_simple             | 6.40 us                                                          | 6.80 us: 1.06x slower                                            |
| meteor_contest             | 128 ms                                                           | 137 ms: 1.07x slower                                             |
| sqlglot_parse              | 1.39 ms                                                          | 1.49 ms: 1.07x slower                                            |
| chameleon                  | 7.40 ms                                                          | 7.90 ms: 1.07x slower                                            |
| 2to3                       | 291 ms                                                           | 311 ms: 1.07x slower                                             |
| sympy_expand               | 501 ms                                                           | 535 ms: 1.07x slower                                             |
| dulwich_log                | 67.3 ms                                                          | 72.0 ms: 1.07x slower                                            |
| mdp                        | 2.46 sec                                                         | 2.63 sec: 1.07x slower                                           |
| sqlglot_transpile          | 1.76 ms                                                          | 1.90 ms: 1.08x slower                                            |
| sympy_integrate            | 23.2 ms                                                          | 24.9 ms: 1.08x slower                                            |
| pprint_safe_repr           | 818 ms                                                           | 880 ms: 1.08x slower                                             |
| scimark_lu                 | 97.5 ms                                                          | 105 ms: 1.08x slower                                             |
| sympy_sum                  | 155 ms                                                           | 167 ms: 1.08x slower                                             |
| tomli_loads                | 2.40 sec                                                         | 2.61 sec: 1.08x slower                                           |
| bench_thread_pool          | 908 us                                                           | 985 us: 1.08x slower                                             |
| go                         | 165 ms                                                           | 179 ms: 1.08x slower                                             |
| pycparser                  | 1.22 sec                                                         | 1.33 sec: 1.09x slower                                           |
| pprint_pformat             | 1.66 sec                                                         | 1.81 sec: 1.09x slower                                           |
| sympy_str                  | 295 ms                                                           | 322 ms: 1.09x slower                                             |
| crypto_pyaes               | 73.6 ms                                                          | 80.6 ms: 1.10x slower                                            |
| xml_etree_parse            | 144 ms                                                           | 157 ms: 1.10x slower                                             |
| pathlib                    | 17.1 ms                                                          | 19.3 ms: 1.13x slower                                            |
| xml_etree_iterparse        | 103 ms                                                           | 117 ms: 1.14x slower                                             |
| raytrace                   | 260 ms                                                           | 299 ms: 1.15x slower                                             |
| float                      | 80.2 ms                                                          | 92.5 ms: 1.15x slower                                            |
| pyflate                    | 482 ms                                                           | 557 ms: 1.16x slower                                             |
| mypy2                      | 764 ms                                                           | 893 ms: 1.17x slower                                             |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 711 ms: 1.18x slower                                             |
| nqueens                    | 88.4 ms                                                          | 105 ms: 1.19x slower                                             |
| regex_compile              | 144 ms                                                           | 172 ms: 1.19x slower                                             |
| async_tree_memoization     | 460 ms                                                           | 561 ms: 1.22x slower                                             |
| async_tree_none            | 365 ms                                                           | 447 ms: 1.22x slower                                             |
| chaos                      | 59.6 ms                                                          | 73.3 ms: 1.23x slower                                            |
| async_tree_io_tg           | 900 ms                                                           | 1.11 sec: 1.24x slower                                           |
| async_tree_io              | 873 ms                                                           | 1.09 sec: 1.25x slower                                           |
| scimark_sor                | 119 ms                                                           | 149 ms: 1.25x slower                                             |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 725 ms: 1.27x slower                                             |
| nbody                      | 87.8 ms                                                          | 112 ms: 1.28x slower                                             |
| python_startup_no_site     | 8.85 ms                                                          | 11.3 ms: 1.28x slower                                            |
| fannkuch                   | 353 ms                                                           | 453 ms: 1.28x slower                                             |
| scimark_fft                | 312 ms                                                           | 407 ms: 1.30x slower                                             |
| mako                       | 10.4 ms                                                          | 13.6 ms: 1.31x slower                                            |
| async_tree_none_tg         | 340 ms                                                           | 453 ms: 1.33x slower                                             |
| scimark_monte_carlo        | 65.5 ms                                                          | 87.4 ms: 1.33x slower                                            |
| comprehensions             | 17.0 us                                                          | 23.3 us: 1.38x slower                                            |
| async_tree_memoization_tg  | 421 ms                                                           | 586 ms: 1.39x slower                                             |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 6.01 ms: 1.40x slower                                            |
| hexiom                     | 6.35 ms                                                          | 9.10 ms: 1.43x slower                                            |
| deltablue                  | 3.37 ms                                                          | 4.98 ms: 1.47x slower                                            |
| spectral_norm              | 97.3 ms                                                          | 144 ms: 1.48x slower                                             |
| Geometric mean             | (ref)                                                            | 1.09x slower                                                     |

Benchmark hidden because not significant (3): bench_mp_pool, regex_dna, telco
Ignored benchmarks (10) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift
Ignored benchmarks (1) of results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: 0.94x