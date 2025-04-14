# Results vs. 3.13.0

- fork: python
- ref: v3.12.0
- machine: linux-x86_64
- commit hash: 0fb18b0
- commit date: 2023-10-02
- overall geometric mean: 1.010x faster
- HPT reliability: 57.24%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 285 ms: 1.03x faster                                         |
| chameleon      | 7.49 ms                                                      | 7.23 ms: 1.04x faster                                        |
| docutils       | 2.81 sec                                                     | 2.87 sec: 1.02x slower                                       |
| tornado_http   | 119 ms                                                       | 121 ms: 1.02x slower                                         |
| Geometric mean | (ref)                                                        | 1.01x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| asyncio_websockets         | 395 ms                                                       | 387 ms: 1.02x faster                                         |
| coroutines                 | 21.6 ms                                                      | 23.0 ms: 1.07x slower                                        |
| async_generators           | 364 ms                                                       | 390 ms: 1.07x slower                                         |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 696 ms: 1.17x slower                                         |
| async_tree_memoization_tg  | 458 ms                                                       | 540 ms: 1.18x slower                                         |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 697 ms: 1.21x slower                                         |
| async_tree_memoization     | 447 ms                                                       | 544 ms: 1.22x slower                                         |
| async_tree_none            | 370 ms                                                       | 452 ms: 1.22x slower                                         |
| async_tree_io              | 832 ms                                                       | 1.04 sec: 1.25x slower                                       |
| async_tree_none_tg         | 342 ms                                                       | 431 ms: 1.26x slower                                         |
| async_tree_io_tg           | 823 ms                                                       | 1.05 sec: 1.28x slower                                       |
| Geometric mean             | (ref)                                                        | 1.17x slower                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 81.6 ms                                                      | 76.6 ms: 1.06x faster                                        |
| nbody          | 92.1 ms                                                      | 88.0 ms: 1.05x faster                                        |
| pidigits       | 252 ms                                                       | 265 ms: 1.05x slower                                         |
| Geometric mean | (ref)                                                        | 1.02x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_v8       | 24.9 ms                                                      | 23.6 ms: 1.06x faster                                        |
| regex_compile  | 143 ms                                                       | 144 ms: 1.01x slower                                         |
| regex_effbot   | 3.51 ms                                                      | 3.57 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                 |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads          | 2.43 sec                                                     | 2.16 sec: 1.13x faster                                       |
| json_dumps           | 10.8 ms                                                      | 10.2 ms: 1.06x faster                                        |
| xml_etree_process    | 60.7 ms                                                      | 58.4 ms: 1.04x faster                                        |
| unpickle_pure_python | 216 us                                                       | 210 us: 1.03x faster                                         |
| json_loads           | 24.7 us                                                      | 24.4 us: 1.01x faster                                        |
| pickle_pure_python   | 322 us                                                       | 318 us: 1.01x faster                                         |
| xml_etree_generate   | 85.2 ms                                                      | 86.1 ms: 1.01x slower                                        |
| xml_etree_iterparse  | 99.8 ms                                                      | 103 ms: 1.03x slower                                         |
| Geometric mean       | (ref)                                                        | 1.03x faster                                                 |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 11.6 ms: 1.35x faster                                        |
| python_startup_no_site | 8.93 ms                                                      | 8.64 ms: 1.03x faster                                        |
| Geometric mean         | (ref)                                                        | 1.18x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 10.3 ms                                                      | 10.0 ms: 1.03x faster                                        |
| django_template | 38.9 ms                                                      | 38.2 ms: 1.02x faster                                        |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| create_gc_cycles           | 2.65 ms                                                      | 1.59 ms: 1.67x faster                                        |
| python_startup             | 15.6 ms                                                      | 11.6 ms: 1.35x faster                                        |
| gc_traversal               | 4.48 ms                                                      | 3.48 ms: 1.29x faster                                        |
| coverage                   | 84.5 ms                                                      | 66.7 ms: 1.27x faster                                        |
| telco                      | 8.77 ms                                                      | 6.96 ms: 1.26x faster                                        |
| mypy2                      | 1.02 sec                                                     | 830 ms: 1.23x faster                                         |
| richards_super             | 60.2 ms                                                      | 51.3 ms: 1.17x faster                                        |
| typing_runtime_protocols   | 176 us                                                       | 152 us: 1.16x faster                                         |
| scimark_sor                | 125 ms                                                       | 109 ms: 1.15x faster                                         |
| richards                   | 52.5 ms                                                      | 45.7 ms: 1.15x faster                                        |
| tomli_loads                | 2.43 sec                                                     | 2.16 sec: 1.13x faster                                       |
| pyflate                    | 493 ms                                                       | 439 ms: 1.12x faster                                         |
| go                         | 167 ms                                                       | 150 ms: 1.12x faster                                         |
| fannkuch                   | 384 ms                                                       | 350 ms: 1.10x faster                                         |
| json                       | 5.62 ms                                                      | 5.12 ms: 1.10x faster                                        |
| hexiom                     | 6.47 ms                                                      | 5.96 ms: 1.09x faster                                        |
| float                      | 81.6 ms                                                      | 76.6 ms: 1.06x faster                                        |
| spectral_norm              | 97.4 ms                                                      | 91.6 ms: 1.06x faster                                        |
| json_dumps                 | 10.8 ms                                                      | 10.2 ms: 1.06x faster                                        |
| deepcopy_memo              | 38.9 us                                                      | 36.8 us: 1.06x faster                                        |
| regex_v8                   | 24.9 ms                                                      | 23.6 ms: 1.06x faster                                        |
| deepcopy                   | 388 us                                                       | 368 us: 1.05x faster                                         |
| nbody                      | 92.1 ms                                                      | 88.0 ms: 1.05x faster                                        |
| sympy_expand               | 506 ms                                                       | 484 ms: 1.05x faster                                         |
| deltablue                  | 3.38 ms                                                      | 3.24 ms: 1.05x faster                                        |
| xml_etree_process          | 60.7 ms                                                      | 58.4 ms: 1.04x faster                                        |
| pycparser                  | 1.28 sec                                                     | 1.23 sec: 1.04x faster                                       |
| chameleon                  | 7.49 ms                                                      | 7.23 ms: 1.04x faster                                        |
| deepcopy_reduce            | 3.49 us                                                      | 3.37 us: 1.04x faster                                        |
| pprint_safe_repr           | 835 ms                                                       | 807 ms: 1.03x faster                                         |
| python_startup_no_site     | 8.93 ms                                                      | 8.64 ms: 1.03x faster                                        |
| logging_silent             | 97.5 ns                                                      | 94.4 ns: 1.03x faster                                        |
| unpickle_pure_python       | 216 us                                                       | 210 us: 1.03x faster                                         |
| mako                       | 10.3 ms                                                      | 10.0 ms: 1.03x faster                                        |
| sqlglot_normalize          | 119 ms                                                       | 116 ms: 1.03x faster                                         |
| pprint_pformat             | 1.70 sec                                                     | 1.65 sec: 1.03x faster                                       |
| nqueens                    | 92.3 ms                                                      | 89.9 ms: 1.03x faster                                        |
| 2to3                       | 293 ms                                                       | 285 ms: 1.03x faster                                         |
| asyncio_websockets         | 395 ms                                                       | 387 ms: 1.02x faster                                         |
| sqlglot_optimize           | 58.7 ms                                                      | 57.5 ms: 1.02x faster                                        |
| django_template            | 38.9 ms                                                      | 38.2 ms: 1.02x faster                                        |
| meteor_contest             | 130 ms                                                       | 128 ms: 1.02x faster                                         |
| json_loads                 | 24.7 us                                                      | 24.4 us: 1.01x faster                                        |
| pickle_pure_python         | 322 us                                                       | 318 us: 1.01x faster                                         |
| sqlglot_transpile          | 1.76 ms                                                      | 1.78 ms: 1.01x slower                                        |
| sqlglot_parse              | 1.37 ms                                                      | 1.38 ms: 1.01x slower                                        |
| regex_compile              | 143 ms                                                       | 144 ms: 1.01x slower                                         |
| scimark_fft                | 298 ms                                                       | 301 ms: 1.01x slower                                         |
| xml_etree_generate         | 85.2 ms                                                      | 86.1 ms: 1.01x slower                                        |
| scimark_lu                 | 97.4 ms                                                      | 98.8 ms: 1.01x slower                                        |
| regex_effbot               | 3.51 ms                                                      | 3.57 ms: 1.02x slower                                        |
| mdp                        | 2.53 sec                                                     | 2.57 sec: 1.02x slower                                       |
| sympy_str                  | 297 ms                                                       | 302 ms: 1.02x slower                                         |
| tornado_http               | 119 ms                                                       | 121 ms: 1.02x slower                                         |
| docutils                   | 2.81 sec                                                     | 2.87 sec: 1.02x slower                                       |
| bench_thread_pool          | 929 us                                                       | 950 us: 1.02x slower                                         |
| sympy_integrate            | 23.4 ms                                                      | 23.9 ms: 1.02x slower                                        |
| xml_etree_iterparse        | 99.8 ms                                                      | 103 ms: 1.03x slower                                         |
| sqlalchemy_imperative      | 18.1 ms                                                      | 18.7 ms: 1.03x slower                                        |
| pidigits                   | 252 ms                                                       | 265 ms: 1.05x slower                                         |
| sympy_sum                  | 154 ms                                                       | 162 ms: 1.05x slower                                         |
| chaos                      | 60.6 ms                                                      | 64.0 ms: 1.06x slower                                        |
| scimark_monte_carlo        | 65.2 ms                                                      | 69.0 ms: 1.06x slower                                        |
| coroutines                 | 21.6 ms                                                      | 23.0 ms: 1.07x slower                                        |
| logging_simple             | 6.28 us                                                      | 6.71 us: 1.07x slower                                        |
| async_generators           | 364 ms                                                       | 390 ms: 1.07x slower                                         |
| sqlalchemy_declarative     | 148 ms                                                       | 159 ms: 1.08x slower                                         |
| logging_format             | 6.95 us                                                      | 7.48 us: 1.08x slower                                        |
| pathlib                    | 17.4 ms                                                      | 18.9 ms: 1.09x slower                                        |
| crypto_pyaes               | 73.5 ms                                                      | 80.3 ms: 1.09x slower                                        |
| generators                 | 33.9 ms                                                      | 37.4 ms: 1.10x slower                                        |
| raytrace                   | 267 ms                                                       | 298 ms: 1.11x slower                                         |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 696 ms: 1.17x slower                                         |
| async_tree_memoization_tg  | 458 ms                                                       | 540 ms: 1.18x slower                                         |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 697 ms: 1.21x slower                                         |
| async_tree_memoization     | 447 ms                                                       | 544 ms: 1.22x slower                                         |
| async_tree_none            | 370 ms                                                       | 452 ms: 1.22x slower                                         |
| async_tree_io              | 832 ms                                                       | 1.04 sec: 1.25x slower                                       |
| async_tree_none_tg         | 342 ms                                                       | 431 ms: 1.26x slower                                         |
| comprehensions             | 17.3 us                                                      | 21.9 us: 1.27x slower                                        |
| async_tree_io_tg           | 823 ms                                                       | 1.05 sec: 1.28x slower                                       |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                 |

Benchmark hidden because not significant (5): bench_mp_pool, dulwich_log, scimark_sparse_mat_mult, xml_etree_parse, regex_dna
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, pylint, shortest_path, sphinx, thrift
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.010x faster
# HPT report

- Reliability score: 57.24% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.98x