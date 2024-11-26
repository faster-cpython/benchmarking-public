# Results vs. 3.12.0

- fork: python
- ref: v3.13.0rc1
- machine: linux-x86_64
- commit hash: e4a3e78
- commit date: 2024-07-31
- overall geometric mean: 1.000x slower
- HPT reliability: 81.76%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.94x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 289 ms: 1.01x slower                                               |
| chameleon      | 7.23 ms                                                      | 7.33 ms: 1.01x slower                                              |
| docutils       | 2.87 sec                                                     | 2.97 sec: 1.04x slower                                             |
| tornado_http   | 121 ms                                                       | 118 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                        | 1.01x slower                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 346 ms: 1.25x faster                                               |
| async_tree_memoization_tg  | 540 ms                                                       | 440 ms: 1.23x faster                                               |
| async_tree_none            | 452 ms                                                       | 368 ms: 1.23x faster                                               |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 580 ms: 1.20x faster                                               |
| async_tree_memoization     | 544 ms                                                       | 466 ms: 1.17x faster                                               |
| async_tree_io              | 1.04 sec                                                     | 895 ms: 1.16x faster                                               |
| async_tree_io_tg           | 1.05 sec                                                     | 911 ms: 1.16x faster                                               |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 612 ms: 1.14x faster                                               |
| Geometric mean             | (ref)                                                        | 1.19x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                               |
| nbody          | 88.0 ms                                                      | 92.0 ms: 1.05x slower                                              |
| float          | 76.6 ms                                                      | 80.3 ms: 1.05x slower                                              |
| Geometric mean | (ref)                                                        | 1.02x slower                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.39 ms: 1.05x faster                                              |
| regex_compile  | 144 ms                                                       | 143 ms: 1.01x faster                                               |
| regex_dna      | 239 ms                                                       | 245 ms: 1.03x slower                                               |
| regex_v8       | 23.6 ms                                                      | 26.4 ms: 1.12x slower                                              |
| Geometric mean | (ref)                                                        | 1.02x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| xml_etree_parse      | 144 ms                                                       | 141 ms: 1.02x faster                                               |
| json_loads           | 24.4 us                                                      | 24.1 us: 1.01x faster                                              |
| pickle_pure_python   | 318 us                                                       | 317 us: 1.00x faster                                               |
| tomli_loads          | 2.16 sec                                                     | 2.19 sec: 1.02x slower                                             |
| unpickle_pure_python | 210 us                                                       | 213 us: 1.02x slower                                               |
| xml_etree_process    | 58.4 ms                                                      | 61.0 ms: 1.04x slower                                              |
| json_dumps           | 10.2 ms                                                      | 11.2 ms: 1.10x slower                                              |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                       |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.98 ms: 1.04x slower                                              |
| python_startup         | 11.6 ms                                                      | 13.3 ms: 1.15x slower                                              |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 39.3 ms: 1.03x slower                                              |
| mako            | 10.0 ms                                                      | 10.5 ms: 1.05x slower                                              |
| Geometric mean  | (ref)                                                        | 1.04x slower                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| comprehensions             | 21.9 us                                                      | 17.2 us: 1.28x faster                                              |
| async_tree_none_tg         | 431 ms                                                       | 346 ms: 1.25x faster                                               |
| async_tree_memoization_tg  | 540 ms                                                       | 440 ms: 1.23x faster                                               |
| async_tree_none            | 452 ms                                                       | 368 ms: 1.23x faster                                               |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 580 ms: 1.20x faster                                               |
| async_tree_memoization     | 544 ms                                                       | 466 ms: 1.17x faster                                               |
| async_tree_io              | 1.04 sec                                                     | 895 ms: 1.16x faster                                               |
| async_tree_io_tg           | 1.05 sec                                                     | 911 ms: 1.16x faster                                               |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 612 ms: 1.14x faster                                               |
| raytrace                   | 298 ms                                                       | 265 ms: 1.12x faster                                               |
| generators                 | 37.4 ms                                                      | 33.9 ms: 1.11x faster                                              |
| pathlib                    | 18.9 ms                                                      | 17.2 ms: 1.10x faster                                              |
| crypto_pyaes               | 80.3 ms                                                      | 73.1 ms: 1.10x faster                                              |
| mypy2                      | 830 ms                                                       | 769 ms: 1.08x faster                                               |
| coroutines                 | 23.0 ms                                                      | 21.3 ms: 1.08x faster                                              |
| logging_format             | 7.48 us                                                      | 6.99 us: 1.07x faster                                              |
| chaos                      | 64.0 ms                                                      | 60.1 ms: 1.07x faster                                              |
| regex_effbot               | 3.57 ms                                                      | 3.39 ms: 1.05x faster                                              |
| async_generators           | 390 ms                                                       | 370 ms: 1.05x faster                                               |
| bench_thread_pool          | 950 us                                                       | 907 us: 1.05x faster                                               |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                               |
| sympy_sum                  | 162 ms                                                       | 156 ms: 1.04x faster                                               |
| logging_simple             | 6.71 us                                                      | 6.46 us: 1.04x faster                                              |
| mdp                        | 2.57 sec                                                     | 2.49 sec: 1.03x faster                                             |
| scimark_monte_carlo        | 69.0 ms                                                      | 67.0 ms: 1.03x faster                                              |
| tornado_http               | 121 ms                                                       | 118 ms: 1.03x faster                                               |
| sympy_integrate            | 23.9 ms                                                      | 23.5 ms: 1.02x faster                                              |
| dulwich_log                | 65.4 ms                                                      | 64.2 ms: 1.02x faster                                              |
| xml_etree_parse            | 144 ms                                                       | 141 ms: 1.02x faster                                               |
| sympy_str                  | 302 ms                                                       | 298 ms: 1.02x faster                                               |
| json_loads                 | 24.4 us                                                      | 24.1 us: 1.01x faster                                              |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.57 sec: 1.01x faster                                             |
| regex_compile              | 144 ms                                                       | 143 ms: 1.01x faster                                               |
| asyncio_tcp                | 378 ms                                                       | 376 ms: 1.01x faster                                               |
| pickle_pure_python         | 318 us                                                       | 317 us: 1.00x faster                                               |
| nqueens                    | 89.9 ms                                                      | 90.4 ms: 1.01x slower                                              |
| meteor_contest             | 128 ms                                                       | 129 ms: 1.01x slower                                               |
| sqlglot_transpile          | 1.78 ms                                                      | 1.79 ms: 1.01x slower                                              |
| 2to3                       | 285 ms                                                       | 289 ms: 1.01x slower                                               |
| chameleon                  | 7.23 ms                                                      | 7.33 ms: 1.01x slower                                              |
| dask                       | 392 ms                                                       | 398 ms: 1.02x slower                                               |
| tomli_loads                | 2.16 sec                                                     | 2.19 sec: 1.02x slower                                             |
| unpickle_pure_python       | 210 us                                                       | 213 us: 1.02x slower                                               |
| json                       | 5.12 ms                                                      | 5.20 ms: 1.02x slower                                              |
| fannkuch                   | 350 ms                                                       | 356 ms: 1.02x slower                                               |
| pycparser                  | 1.23 sec                                                     | 1.26 sec: 1.02x slower                                             |
| pprint_pformat             | 1.65 sec                                                     | 1.69 sec: 1.02x slower                                             |
| sqlglot_parse              | 1.38 ms                                                      | 1.41 ms: 1.02x slower                                              |
| scimark_fft                | 301 ms                                                       | 308 ms: 1.02x slower                                               |
| regex_dna                  | 239 ms                                                       | 245 ms: 1.03x slower                                               |
| pprint_safe_repr           | 807 ms                                                       | 831 ms: 1.03x slower                                               |
| django_template            | 38.2 ms                                                      | 39.3 ms: 1.03x slower                                              |
| deltablue                  | 3.24 ms                                                      | 3.34 ms: 1.03x slower                                              |
| logging_silent             | 94.4 ns                                                      | 97.9 ns: 1.04x slower                                              |
| docutils                   | 2.87 sec                                                     | 2.97 sec: 1.04x slower                                             |
| deepcopy_reduce            | 3.37 us                                                      | 3.50 us: 1.04x slower                                              |
| sqlglot_optimize           | 57.5 ms                                                      | 59.7 ms: 1.04x slower                                              |
| python_startup_no_site     | 8.64 ms                                                      | 8.98 ms: 1.04x slower                                              |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.38 ms: 1.04x slower                                              |
| deepcopy_memo              | 36.8 us                                                      | 38.3 us: 1.04x slower                                              |
| xml_etree_process          | 58.4 ms                                                      | 61.0 ms: 1.04x slower                                              |
| nbody                      | 88.0 ms                                                      | 92.0 ms: 1.05x slower                                              |
| deepcopy                   | 368 us                                                       | 385 us: 1.05x slower                                               |
| mako                       | 10.0 ms                                                      | 10.5 ms: 1.05x slower                                              |
| float                      | 76.6 ms                                                      | 80.3 ms: 1.05x slower                                              |
| sqlglot_normalize          | 116 ms                                                       | 121 ms: 1.05x slower                                               |
| sympy_expand               | 484 ms                                                       | 508 ms: 1.05x slower                                               |
| go                         | 150 ms                                                       | 158 ms: 1.05x slower                                               |
| spectral_norm              | 91.6 ms                                                      | 97.6 ms: 1.07x slower                                              |
| pyflate                    | 439 ms                                                       | 469 ms: 1.07x slower                                               |
| hexiom                     | 5.96 ms                                                      | 6.40 ms: 1.07x slower                                              |
| json_dumps                 | 10.2 ms                                                      | 11.2 ms: 1.10x slower                                              |
| richards                   | 45.7 ms                                                      | 50.9 ms: 1.11x slower                                              |
| regex_v8                   | 23.6 ms                                                      | 26.4 ms: 1.12x slower                                              |
| richards_super             | 51.3 ms                                                      | 57.4 ms: 1.12x slower                                              |
| typing_runtime_protocols   | 152 us                                                       | 174 us: 1.15x slower                                               |
| python_startup             | 11.6 ms                                                      | 13.3 ms: 1.15x slower                                              |
| scimark_sor                | 109 ms                                                       | 127 ms: 1.17x slower                                               |
| coverage                   | 66.7 ms                                                      | 79.8 ms: 1.20x slower                                              |
| telco                      | 6.96 ms                                                      | 8.43 ms: 1.21x slower                                              |
| create_gc_cycles           | 1.59 ms                                                      | 2.01 ms: 1.26x slower                                              |
| gc_traversal               | 3.48 ms                                                      | 4.45 ms: 1.28x slower                                              |
| Geometric mean             | (ref)                                                        | 1.00x slower                                                       |

Benchmark hidden because not significant (5): bench_mp_pool, xml_etree_iterparse, xml_etree_generate, scimark_lu, asyncio_websockets
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, gunicorn, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240731-3.13.0rc1-e4a3e78/bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.000x slower
# HPT report

- Reliability score: 81.76% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.94x