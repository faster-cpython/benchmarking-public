# Results vs. 3.12.0

- fork: python
- ref: f9a5a3a3ef34e63dc197
- machine: linux-x86_64
- commit hash: f9a5a3a
- commit date: 2024-12-28
- overall geometric mean: 1.045x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 281 ms: 1.01x faster                                                         |
| docutils       | 2.87 sec                                                     | 2.89 sec: 1.01x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 632 ms: 1.67x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 332 ms: 1.63x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 647 ms: 1.61x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 271 ms: 1.59x faster                                                         |
| async_tree_none            | 452 ms                                                       | 294 ms: 1.54x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 357 ms: 1.52x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 501 ms: 1.39x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 518 ms: 1.34x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.53x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 255 ms: 1.04x faster                                                         |
| float          | 76.6 ms                                                      | 75.2 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.28 ms: 1.09x faster                                                        |
| regex_compile  | 144 ms                                                       | 136 ms: 1.06x faster                                                         |
| regex_dna      | 239 ms                                                       | 246 ms: 1.03x slower                                                         |
| regex_v8       | 23.6 ms                                                      | 27.0 ms: 1.14x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 96.9 ms: 1.06x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 136 ms: 1.06x faster                                                         |
| tomli_loads          | 2.16 sec                                                     | 2.06 sec: 1.05x faster                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 83.1 ms: 1.04x faster                                                        |
| json_loads           | 24.4 us                                                      | 23.8 us: 1.02x faster                                                        |
| unpickle_pure_python | 210 us                                                       | 206 us: 1.02x faster                                                         |
| pickle_pure_python   | 318 us                                                       | 327 us: 1.03x slower                                                         |
| json_dumps           | 10.2 ms                                                      | 11.6 ms: 1.14x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.01 ms: 1.04x slower                                                        |
| python_startup         | 11.6 ms                                                      | 16.1 ms: 1.38x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.5 ms: 1.07x faster                                                        |
| mako            | 10.0 ms                                                      | 11.0 ms: 1.10x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 632 ms: 1.67x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 332 ms: 1.63x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 647 ms: 1.61x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 271 ms: 1.59x faster                                                         |
| async_tree_none            | 452 ms                                                       | 294 ms: 1.54x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 357 ms: 1.52x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 501 ms: 1.39x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 518 ms: 1.34x faster                                                         |
| generators                 | 37.4 ms                                                      | 28.5 ms: 1.31x faster                                                        |
| deepcopy                   | 368 us                                                       | 283 us: 1.30x faster                                                         |
| comprehensions             | 21.9 us                                                      | 17.5 us: 1.25x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 30.3 us: 1.21x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 15.8 ms: 1.19x faster                                                        |
| go                         | 150 ms                                                       | 126 ms: 1.18x faster                                                         |
| deepcopy_reduce            | 3.37 us                                                      | 2.88 us: 1.17x faster                                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 143 ms: 1.11x faster                                                         |
| coroutines                 | 23.0 ms                                                      | 20.7 ms: 1.11x faster                                                        |
| logging_format             | 7.48 us                                                      | 6.78 us: 1.10x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 72.9 ms: 1.10x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.28 ms: 1.09x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 63.5 ms: 1.09x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.18 us: 1.09x faster                                                        |
| django_template            | 38.2 ms                                                      | 35.5 ms: 1.07x faster                                                        |
| raytrace                   | 298 ms                                                       | 278 ms: 1.07x faster                                                         |
| xml_etree_iterparse        | 103 ms                                                       | 96.9 ms: 1.06x faster                                                        |
| regex_compile              | 144 ms                                                       | 136 ms: 1.06x faster                                                         |
| xml_etree_parse            | 144 ms                                                       | 136 ms: 1.06x faster                                                         |
| sympy_sum                  | 162 ms                                                       | 153 ms: 1.06x faster                                                         |
| async_generators           | 390 ms                                                       | 371 ms: 1.05x faster                                                         |
| pprint_pformat             | 1.65 sec                                                     | 1.58 sec: 1.05x faster                                                       |
| sqlalchemy_imperative      | 18.7 ms                                                      | 17.9 ms: 1.05x faster                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.06 sec: 1.05x faster                                                       |
| spectral_norm              | 91.6 ms                                                      | 87.8 ms: 1.04x faster                                                        |
| pidigits                   | 265 ms                                                       | 255 ms: 1.04x faster                                                         |
| mdp                        | 2.57 sec                                                     | 2.47 sec: 1.04x faster                                                       |
| pprint_safe_repr           | 807 ms                                                       | 777 ms: 1.04x faster                                                         |
| xml_etree_generate         | 86.1 ms                                                      | 83.1 ms: 1.04x faster                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.33 ms: 1.04x faster                                                        |
| sympy_str                  | 302 ms                                                       | 293 ms: 1.03x faster                                                         |
| sqlglot_transpile          | 1.78 ms                                                      | 1.72 ms: 1.03x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 23.3 ms: 1.03x faster                                                        |
| bench_thread_pool          | 950 us                                                       | 924 us: 1.03x faster                                                         |
| json_loads                 | 24.4 us                                                      | 23.8 us: 1.02x faster                                                        |
| sqlglot_normalize          | 116 ms                                                       | 113 ms: 1.02x faster                                                         |
| chaos                      | 64.0 ms                                                      | 62.7 ms: 1.02x faster                                                        |
| float                      | 76.6 ms                                                      | 75.2 ms: 1.02x faster                                                        |
| unpickle_pure_python       | 210 us                                                       | 206 us: 1.02x faster                                                         |
| nqueens                    | 89.9 ms                                                      | 88.5 ms: 1.02x faster                                                        |
| 2to3                       | 285 ms                                                       | 281 ms: 1.01x faster                                                         |
| pycparser                  | 1.23 sec                                                     | 1.22 sec: 1.01x faster                                                       |
| meteor_contest             | 128 ms                                                       | 127 ms: 1.01x faster                                                         |
| sqlglot_optimize           | 57.5 ms                                                      | 57.1 ms: 1.01x faster                                                        |
| pyflate                    | 439 ms                                                       | 436 ms: 1.01x faster                                                         |
| docutils                   | 2.87 sec                                                     | 2.89 sec: 1.01x slower                                                       |
| fannkuch                   | 350 ms                                                       | 353 ms: 1.01x slower                                                         |
| richards_super             | 51.3 ms                                                      | 51.8 ms: 1.01x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.02 ms: 1.01x slower                                                        |
| scimark_lu                 | 98.8 ms                                                      | 101 ms: 1.02x slower                                                         |
| sqlite_synth               | 2.77 us                                                      | 2.84 us: 1.02x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 327 us: 1.03x slower                                                         |
| scimark_sor                | 109 ms                                                       | 112 ms: 1.03x slower                                                         |
| regex_dna                  | 239 ms                                                       | 246 ms: 1.03x slower                                                         |
| dulwich_log                | 65.4 ms                                                      | 67.9 ms: 1.04x slower                                                        |
| scimark_fft                | 301 ms                                                       | 313 ms: 1.04x slower                                                         |
| sympy_expand               | 484 ms                                                       | 504 ms: 1.04x slower                                                         |
| python_startup_no_site     | 8.64 ms                                                      | 9.01 ms: 1.04x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 98.8 ns: 1.05x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 3.40 ms: 1.05x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.50 ms: 1.07x slower                                                        |
| mako                       | 10.0 ms                                                      | 11.0 ms: 1.10x slower                                                        |
| telco                      | 6.96 ms                                                      | 7.85 ms: 1.13x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 11.6 ms: 1.14x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 27.0 ms: 1.14x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 174 us: 1.15x slower                                                         |
| coverage                   | 66.7 ms                                                      | 79.9 ms: 1.20x slower                                                        |
| mypy2                      | 830 ms                                                       | 1.03 sec: 1.24x slower                                                       |
| python_startup             | 11.6 ms                                                      | 16.1 ms: 1.38x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.77 ms: 1.74x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 6.35 ms: 1.83x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 1.97 sec: 413.15x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                                 |

Benchmark hidden because not significant (5): nbody, richards, json, asyncio_websockets, xml_etree_process
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241228-3.14.0a3+-f9a5a3a/bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.045x faster

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x