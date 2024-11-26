# Results vs. 3.12.0

- fork: python
- ref: v3.13.0
- machine: linux-x86_64
- commit hash: 60403a5
- commit date: 2024-10-07
- overall geometric mean: 1.007x slower
- HPT reliability: 57.24%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 293 ms: 1.03x slower                                         |
| chameleon      | 7.23 ms                                                      | 7.49 ms: 1.04x slower                                        |
| docutils       | 2.87 sec                                                     | 2.81 sec: 1.02x faster                                       |
| tornado_http   | 121 ms                                                       | 119 ms: 1.02x faster                                         |
| Geometric mean | (ref)                                                        | 1.01x slower                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 823 ms: 1.28x faster                                         |
| async_tree_none_tg         | 431 ms                                                       | 342 ms: 1.26x faster                                         |
| async_tree_io              | 1.04 sec                                                     | 832 ms: 1.25x faster                                         |
| async_tree_none            | 452 ms                                                       | 370 ms: 1.22x faster                                         |
| async_tree_memoization     | 544 ms                                                       | 447 ms: 1.22x faster                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 574 ms: 1.21x faster                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 458 ms: 1.18x faster                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 596 ms: 1.17x faster                                         |
| Geometric mean             | (ref)                                                        | 1.22x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 252 ms: 1.05x faster                                         |
| nbody          | 88.0 ms                                                      | 92.1 ms: 1.05x slower                                        |
| float          | 76.6 ms                                                      | 81.6 ms: 1.06x slower                                        |
| Geometric mean | (ref)                                                        | 1.02x slower                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.51 ms: 1.02x faster                                        |
| regex_compile  | 144 ms                                                       | 143 ms: 1.01x faster                                         |
| regex_v8       | 23.6 ms                                                      | 24.9 ms: 1.06x slower                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                 |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 99.8 ms: 1.03x faster                                        |
| xml_etree_generate   | 86.1 ms                                                      | 85.2 ms: 1.01x faster                                        |
| pickle_pure_python   | 318 us                                                       | 322 us: 1.01x slower                                         |
| json_loads           | 24.4 us                                                      | 24.7 us: 1.01x slower                                        |
| unpickle_pure_python | 210 us                                                       | 216 us: 1.03x slower                                         |
| xml_etree_process    | 58.4 ms                                                      | 60.7 ms: 1.04x slower                                        |
| json_dumps           | 10.2 ms                                                      | 10.8 ms: 1.06x slower                                        |
| tomli_loads          | 2.16 sec                                                     | 2.43 sec: 1.13x slower                                       |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                 |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.93 ms: 1.03x slower                                        |
| python_startup         | 11.6 ms                                                      | 15.6 ms: 1.35x slower                                        |
| Geometric mean         | (ref)                                                        | 1.18x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 38.9 ms: 1.02x slower                                        |
| mako            | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                        |
| Geometric mean  | (ref)                                                        | 1.02x slower                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 823 ms: 1.28x faster                                         |
| comprehensions             | 21.9 us                                                      | 17.3 us: 1.27x faster                                        |
| async_tree_none_tg         | 431 ms                                                       | 342 ms: 1.26x faster                                         |
| async_tree_io              | 1.04 sec                                                     | 832 ms: 1.25x faster                                         |
| async_tree_none            | 452 ms                                                       | 370 ms: 1.22x faster                                         |
| async_tree_memoization     | 544 ms                                                       | 447 ms: 1.22x faster                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 574 ms: 1.21x faster                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 458 ms: 1.18x faster                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 596 ms: 1.17x faster                                         |
| raytrace                   | 298 ms                                                       | 267 ms: 1.11x faster                                         |
| generators                 | 37.4 ms                                                      | 33.9 ms: 1.10x faster                                        |
| crypto_pyaes               | 80.3 ms                                                      | 73.5 ms: 1.09x faster                                        |
| pathlib                    | 18.9 ms                                                      | 17.4 ms: 1.09x faster                                        |
| logging_format             | 7.48 us                                                      | 6.95 us: 1.08x faster                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 148 ms: 1.08x faster                                         |
| async_generators           | 390 ms                                                       | 364 ms: 1.07x faster                                         |
| logging_simple             | 6.71 us                                                      | 6.28 us: 1.07x faster                                        |
| coroutines                 | 23.0 ms                                                      | 21.6 ms: 1.07x faster                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 65.2 ms: 1.06x faster                                        |
| chaos                      | 64.0 ms                                                      | 60.6 ms: 1.06x faster                                        |
| sympy_sum                  | 162 ms                                                       | 154 ms: 1.05x faster                                         |
| pidigits                   | 265 ms                                                       | 252 ms: 1.05x faster                                         |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.1 ms: 1.03x faster                                        |
| xml_etree_iterparse        | 103 ms                                                       | 99.8 ms: 1.03x faster                                        |
| sympy_integrate            | 23.9 ms                                                      | 23.4 ms: 1.02x faster                                        |
| bench_thread_pool          | 950 us                                                       | 929 us: 1.02x faster                                         |
| docutils                   | 2.87 sec                                                     | 2.81 sec: 1.02x faster                                       |
| tornado_http               | 121 ms                                                       | 119 ms: 1.02x faster                                         |
| sympy_str                  | 302 ms                                                       | 297 ms: 1.02x faster                                         |
| mdp                        | 2.57 sec                                                     | 2.53 sec: 1.02x faster                                       |
| regex_effbot               | 3.57 ms                                                      | 3.51 ms: 1.02x faster                                        |
| scimark_lu                 | 98.8 ms                                                      | 97.4 ms: 1.01x faster                                        |
| xml_etree_generate         | 86.1 ms                                                      | 85.2 ms: 1.01x faster                                        |
| scimark_fft                | 301 ms                                                       | 298 ms: 1.01x faster                                         |
| regex_compile              | 144 ms                                                       | 143 ms: 1.01x faster                                         |
| sqlglot_parse              | 1.38 ms                                                      | 1.37 ms: 1.01x faster                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.76 ms: 1.01x faster                                        |
| pickle_pure_python         | 318 us                                                       | 322 us: 1.01x slower                                         |
| json_loads                 | 24.4 us                                                      | 24.7 us: 1.01x slower                                        |
| meteor_contest             | 128 ms                                                       | 130 ms: 1.02x slower                                         |
| django_template            | 38.2 ms                                                      | 38.9 ms: 1.02x slower                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 58.7 ms: 1.02x slower                                        |
| asyncio_websockets         | 387 ms                                                       | 395 ms: 1.02x slower                                         |
| 2to3                       | 285 ms                                                       | 293 ms: 1.03x slower                                         |
| nqueens                    | 89.9 ms                                                      | 92.3 ms: 1.03x slower                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.70 sec: 1.03x slower                                       |
| sqlglot_normalize          | 116 ms                                                       | 119 ms: 1.03x slower                                         |
| mako                       | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                        |
| unpickle_pure_python       | 210 us                                                       | 216 us: 1.03x slower                                         |
| logging_silent             | 94.4 ns                                                      | 97.5 ns: 1.03x slower                                        |
| python_startup_no_site     | 8.64 ms                                                      | 8.93 ms: 1.03x slower                                        |
| pprint_safe_repr           | 807 ms                                                       | 835 ms: 1.03x slower                                         |
| deepcopy_reduce            | 3.37 us                                                      | 3.49 us: 1.04x slower                                        |
| chameleon                  | 7.23 ms                                                      | 7.49 ms: 1.04x slower                                        |
| pycparser                  | 1.23 sec                                                     | 1.28 sec: 1.04x slower                                       |
| xml_etree_process          | 58.4 ms                                                      | 60.7 ms: 1.04x slower                                        |
| deltablue                  | 3.24 ms                                                      | 3.38 ms: 1.05x slower                                        |
| sympy_expand               | 484 ms                                                       | 506 ms: 1.05x slower                                         |
| nbody                      | 88.0 ms                                                      | 92.1 ms: 1.05x slower                                        |
| deepcopy                   | 368 us                                                       | 388 us: 1.05x slower                                         |
| regex_v8                   | 23.6 ms                                                      | 24.9 ms: 1.06x slower                                        |
| deepcopy_memo              | 36.8 us                                                      | 38.9 us: 1.06x slower                                        |
| json_dumps                 | 10.2 ms                                                      | 10.8 ms: 1.06x slower                                        |
| spectral_norm              | 91.6 ms                                                      | 97.4 ms: 1.06x slower                                        |
| float                      | 76.6 ms                                                      | 81.6 ms: 1.06x slower                                        |
| hexiom                     | 5.96 ms                                                      | 6.47 ms: 1.09x slower                                        |
| json                       | 5.12 ms                                                      | 5.62 ms: 1.10x slower                                        |
| fannkuch                   | 350 ms                                                       | 384 ms: 1.10x slower                                         |
| go                         | 150 ms                                                       | 167 ms: 1.12x slower                                         |
| pyflate                    | 439 ms                                                       | 493 ms: 1.12x slower                                         |
| tomli_loads                | 2.16 sec                                                     | 2.43 sec: 1.13x slower                                       |
| richards                   | 45.7 ms                                                      | 52.5 ms: 1.15x slower                                        |
| scimark_sor                | 109 ms                                                       | 125 ms: 1.15x slower                                         |
| typing_runtime_protocols   | 152 us                                                       | 176 us: 1.16x slower                                         |
| richards_super             | 51.3 ms                                                      | 60.2 ms: 1.17x slower                                        |
| mypy2                      | 830 ms                                                       | 1.02 sec: 1.23x slower                                       |
| telco                      | 6.96 ms                                                      | 8.77 ms: 1.26x slower                                        |
| coverage                   | 66.7 ms                                                      | 84.5 ms: 1.27x slower                                        |
| gc_traversal               | 3.48 ms                                                      | 4.48 ms: 1.29x slower                                        |
| python_startup             | 11.6 ms                                                      | 15.6 ms: 1.35x slower                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.65 ms: 1.67x slower                                        |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                 |

Benchmark hidden because not significant (5): regex_dna, xml_etree_parse, scimark_sparse_mat_mult, dulwich_log, bench_mp_pool
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.007x slower
# HPT report

- Reliability score: 57.24% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x