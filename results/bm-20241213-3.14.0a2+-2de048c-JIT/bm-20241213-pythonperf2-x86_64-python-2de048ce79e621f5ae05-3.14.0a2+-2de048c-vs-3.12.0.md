# Results vs. 3.12.0

- fork: python
- ref: 2de048ce79e621f5ae05
- machine: linux-x86_64
- commit hash: 2de048c
- commit date: 2024-12-13
- overall geometric mean: 1.014x faster
- HPT reliability: 67.52%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-pythonperf2-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 290 ms: 1.02x slower                                                         |
| docutils       | 2.87 sec                                                     | 2.99 sec: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-pythonperf2-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 637 ms: 1.65x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 334 ms: 1.62x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 653 ms: 1.60x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 275 ms: 1.57x faster                                                         |
| async_tree_none            | 452 ms                                                       | 293 ms: 1.54x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 361 ms: 1.51x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 508 ms: 1.37x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 524 ms: 1.33x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.52x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-pythonperf2-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 251 ms: 1.06x faster                                                         |
| float          | 76.6 ms                                                      | 72.8 ms: 1.05x faster                                                        |
| nbody          | 88.0 ms                                                      | 90.8 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-pythonperf2-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.24 ms: 1.10x faster                                                        |
| regex_compile  | 144 ms                                                       | 138 ms: 1.05x faster                                                         |
| regex_dna      | 239 ms                                                       | 234 ms: 1.02x faster                                                         |
| regex_v8       | 23.6 ms                                                      | 25.2 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-pythonperf2-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 94.0 ms: 1.09x faster                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 80.7 ms: 1.07x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 136 ms: 1.06x faster                                                         |
| tomli_loads          | 2.16 sec                                                     | 2.05 sec: 1.05x faster                                                       |
| unpickle_pure_python | 210 us                                                       | 202 us: 1.04x faster                                                         |
| xml_etree_process    | 58.4 ms                                                      | 56.9 ms: 1.03x faster                                                        |
| json_loads           | 24.4 us                                                      | 25.1 us: 1.03x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 341 us: 1.07x slower                                                         |
| json_dumps           | 10.2 ms                                                      | 11.2 ms: 1.09x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-pythonperf2-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.02 ms: 1.04x slower                                                        |
| python_startup         | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-pythonperf2-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.38 ms: 1.07x faster                                                        |
| django_template | 38.2 ms                                                      | 39.5 ms: 1.03x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-pythonperf2-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 637 ms: 1.65x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 334 ms: 1.62x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 653 ms: 1.60x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 275 ms: 1.57x faster                                                         |
| async_tree_none            | 452 ms                                                       | 293 ms: 1.54x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 361 ms: 1.51x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 508 ms: 1.37x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 524 ms: 1.33x faster                                                         |
| deepcopy_memo              | 36.8 us                                                      | 29.8 us: 1.23x faster                                                        |
| deepcopy                   | 368 us                                                       | 310 us: 1.19x faster                                                         |
| comprehensions             | 21.9 us                                                      | 19.0 us: 1.15x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 2.97 us: 1.13x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 16.7 ms: 1.13x faster                                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 143 ms: 1.12x faster                                                         |
| regex_effbot               | 3.57 ms                                                      | 3.24 ms: 1.10x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 62.9 ms: 1.10x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 21.0 ms: 1.09x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 94.0 ms: 1.09x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 75.3 ms: 1.07x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 80.7 ms: 1.07x faster                                                        |
| mako                       | 10.0 ms                                                      | 9.38 ms: 1.07x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 136 ms: 1.06x faster                                                         |
| pidigits                   | 265 ms                                                       | 251 ms: 1.06x faster                                                         |
| tomli_loads                | 2.16 sec                                                     | 2.05 sec: 1.05x faster                                                       |
| float                      | 76.6 ms                                                      | 72.8 ms: 1.05x faster                                                        |
| scimark_sor                | 109 ms                                                       | 104 ms: 1.05x faster                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                      | 17.9 ms: 1.05x faster                                                        |
| regex_compile              | 144 ms                                                       | 138 ms: 1.05x faster                                                         |
| unpickle_pure_python       | 210 us                                                       | 202 us: 1.04x faster                                                         |
| go                         | 150 ms                                                       | 145 ms: 1.04x faster                                                         |
| logging_format             | 7.48 us                                                      | 7.23 us: 1.03x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 158 ms: 1.03x faster                                                         |
| xml_etree_process          | 58.4 ms                                                      | 56.9 ms: 1.03x faster                                                        |
| regex_dna                  | 239 ms                                                       | 234 ms: 1.02x faster                                                         |
| logging_simple             | 6.71 us                                                      | 6.60 us: 1.02x faster                                                        |
| pprint_safe_repr           | 807 ms                                                       | 797 ms: 1.01x faster                                                         |
| sympy_integrate            | 23.9 ms                                                      | 24.0 ms: 1.00x slower                                                        |
| sympy_str                  | 302 ms                                                       | 305 ms: 1.01x slower                                                         |
| meteor_contest             | 128 ms                                                       | 130 ms: 1.01x slower                                                         |
| scimark_fft                | 301 ms                                                       | 305 ms: 1.01x slower                                                         |
| mdp                        | 2.57 sec                                                     | 2.60 sec: 1.01x slower                                                       |
| sqlite_synth               | 2.77 us                                                      | 2.82 us: 1.02x slower                                                        |
| 2to3                       | 285 ms                                                       | 290 ms: 1.02x slower                                                         |
| spectral_norm              | 91.6 ms                                                      | 93.6 ms: 1.02x slower                                                        |
| bench_thread_pool          | 950 us                                                       | 970 us: 1.02x slower                                                         |
| deltablue                  | 3.24 ms                                                      | 3.31 ms: 1.02x slower                                                        |
| json                       | 5.12 ms                                                      | 5.25 ms: 1.03x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.82 ms: 1.03x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.42 ms: 1.03x slower                                                        |
| pyflate                    | 439 ms                                                       | 451 ms: 1.03x slower                                                         |
| json_loads                 | 24.4 us                                                      | 25.1 us: 1.03x slower                                                        |
| nbody                      | 88.0 ms                                                      | 90.8 ms: 1.03x slower                                                        |
| django_template            | 38.2 ms                                                      | 39.5 ms: 1.03x slower                                                        |
| dulwich_log                | 65.4 ms                                                      | 67.7 ms: 1.04x slower                                                        |
| docutils                   | 2.87 sec                                                     | 2.99 sec: 1.04x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 9.02 ms: 1.04x slower                                                        |
| richards                   | 45.7 ms                                                      | 48.2 ms: 1.05x slower                                                        |
| chaos                      | 64.0 ms                                                      | 67.6 ms: 1.06x slower                                                        |
| generators                 | 37.4 ms                                                      | 39.8 ms: 1.06x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 101 ns: 1.07x slower                                                         |
| sqlglot_optimize           | 57.5 ms                                                      | 61.3 ms: 1.07x slower                                                        |
| richards_super             | 51.3 ms                                                      | 54.8 ms: 1.07x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 25.2 ms: 1.07x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 341 us: 1.07x slower                                                         |
| sympy_expand               | 484 ms                                                       | 521 ms: 1.08x slower                                                         |
| sqlglot_normalize          | 116 ms                                                       | 125 ms: 1.08x slower                                                         |
| fannkuch                   | 350 ms                                                       | 379 ms: 1.08x slower                                                         |
| json_dumps                 | 10.2 ms                                                      | 11.2 ms: 1.09x slower                                                        |
| telco                      | 6.96 ms                                                      | 7.65 ms: 1.10x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 101 ms: 1.13x slower                                                         |
| raytrace                   | 298 ms                                                       | 338 ms: 1.14x slower                                                         |
| hexiom                     | 5.96 ms                                                      | 7.08 ms: 1.19x slower                                                        |
| async_generators           | 390 ms                                                       | 465 ms: 1.19x slower                                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.02 ms: 1.19x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 183 us: 1.20x slower                                                         |
| coverage                   | 66.7 ms                                                      | 81.5 ms: 1.22x slower                                                        |
| mypy2                      | 830 ms                                                       | 1.04 sec: 1.26x slower                                                       |
| python_startup             | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.69 ms: 1.69x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 6.31 ms: 1.81x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 1.10 sec: 231.44x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.05x slower                                                                 |

Benchmark hidden because not significant (4): pycparser, pprint_pformat, scimark_lu, asyncio_websockets
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241213-3.14.0a2+-2de048c-JIT/bm-20241213-pythonperf2-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.014x faster

# HPT report

- Reliability score: 67.52% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x