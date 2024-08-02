# Results vs. 3.12.0

- fork: python
- ref: c15f94d6fbc960790db3
- machine: linux-x86_64
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.00x slower
- HPT reliability: 83.74%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 291 ms: 1.02x slower                                                         |
| chameleon      | 7.23 ms                                                      | 7.40 ms: 1.02x slower                                                        |
| docutils       | 2.87 sec                                                     | 2.99 sec: 1.04x slower                                                       |
| tornado_http   | 121 ms                                                       | 119 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 432 ms: 1.25x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 345 ms: 1.25x faster                                                         |
| async_tree_none            | 452 ms                                                       | 371 ms: 1.22x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 580 ms: 1.20x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 884 ms: 1.18x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 465 ms: 1.17x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 904 ms: 1.17x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 614 ms: 1.13x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.20x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                         |
| nbody          | 88.0 ms                                                      | 89.4 ms: 1.02x slower                                                        |
| float          | 76.6 ms                                                      | 80.8 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 145 ms: 1.01x slower                                                         |
| regex_dna      | 239 ms                                                       | 248 ms: 1.04x slower                                                         |
| regex_effbot   | 3.57 ms                                                      | 3.72 ms: 1.04x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 26.4 ms: 1.12x slower                                                        |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 318 us                                                       | 309 us: 1.03x faster                                                         |
| xml_etree_generate   | 86.1 ms                                                      | 85.2 ms: 1.01x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 102 ms: 1.01x faster                                                         |
| pickle_list          | 4.43 us                                                      | 4.46 us: 1.01x slower                                                        |
| pickle               | 10.5 us                                                      | 10.6 us: 1.01x slower                                                        |
| xml_etree_process    | 58.4 ms                                                      | 59.3 ms: 1.02x slower                                                        |
| json_loads           | 24.4 us                                                      | 24.8 us: 1.02x slower                                                        |
| pickle_dict          | 32.5 us                                                      | 33.3 us: 1.02x slower                                                        |
| unpickle_list        | 4.66 us                                                      | 4.80 us: 1.03x slower                                                        |
| unpickle             | 14.8 us                                                      | 15.7 us: 1.06x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 226 us: 1.08x slower                                                         |
| json_dumps           | 10.2 ms                                                      | 11.1 ms: 1.08x slower                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.39 sec: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                                 |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.84 ms: 1.02x slower                                                        |
| python_startup         | 11.6 ms                                                      | 13.2 ms: 1.14x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.08x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 39.1 ms: 1.02x slower                                                        |
| mako            | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| comprehensions             | 21.9 us                                                      | 17.1 us: 1.28x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 432 ms: 1.25x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 345 ms: 1.25x faster                                                         |
| async_tree_none            | 452 ms                                                       | 371 ms: 1.22x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 580 ms: 1.20x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 884 ms: 1.18x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 465 ms: 1.17x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 904 ms: 1.17x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 614 ms: 1.13x faster                                                         |
| generators                 | 37.4 ms                                                      | 33.4 ms: 1.12x faster                                                        |
| raytrace                   | 298 ms                                                       | 268 ms: 1.11x faster                                                         |
| pathlib                    | 18.9 ms                                                      | 17.3 ms: 1.09x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 73.9 ms: 1.09x faster                                                        |
| mypy2                      | 830 ms                                                       | 764 ms: 1.09x faster                                                         |
| logging_format             | 7.48 us                                                      | 7.02 us: 1.07x faster                                                        |
| chaos                      | 64.0 ms                                                      | 60.5 ms: 1.06x faster                                                        |
| async_generators           | 390 ms                                                       | 370 ms: 1.05x faster                                                         |
| scimark_monte_carlo        | 69.0 ms                                                      | 65.5 ms: 1.05x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.40 us: 1.05x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 155 ms: 1.05x faster                                                         |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                         |
| coroutines                 | 23.0 ms                                                      | 22.0 ms: 1.04x faster                                                        |
| bench_thread_pool          | 950 us                                                       | 918 us: 1.03x faster                                                         |
| pickle_pure_python         | 318 us                                                       | 309 us: 1.03x faster                                                         |
| sympy_integrate            | 23.9 ms                                                      | 23.4 ms: 1.02x faster                                                        |
| sympy_str                  | 302 ms                                                       | 295 ms: 1.02x faster                                                         |
| tornado_http               | 121 ms                                                       | 119 ms: 1.02x faster                                                         |
| mdp                        | 2.57 sec                                                     | 2.53 sec: 1.01x faster                                                       |
| nqueens                    | 89.9 ms                                                      | 88.8 ms: 1.01x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 85.2 ms: 1.01x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 102 ms: 1.01x faster                                                         |
| scimark_lu                 | 98.8 ms                                                      | 97.9 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.66 sec: 1.00x slower                                                       |
| pickle_list                | 4.43 us                                                      | 4.46 us: 1.01x slower                                                        |
| regex_compile              | 144 ms                                                       | 145 ms: 1.01x slower                                                         |
| pickle                     | 10.5 us                                                      | 10.6 us: 1.01x slower                                                        |
| pprint_safe_repr           | 807 ms                                                       | 814 ms: 1.01x slower                                                         |
| asyncio_websockets         | 387 ms                                                       | 391 ms: 1.01x slower                                                         |
| dask                       | 392 ms                                                       | 396 ms: 1.01x slower                                                         |
| sqlite_synth               | 2.77 us                                                      | 2.80 us: 1.01x slower                                                        |
| nbody                      | 88.0 ms                                                      | 89.4 ms: 1.02x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 59.3 ms: 1.02x slower                                                        |
| json_loads                 | 24.4 us                                                      | 24.8 us: 1.02x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.40 ms: 1.02x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 96.3 ns: 1.02x slower                                                        |
| 2to3                       | 285 ms                                                       | 291 ms: 1.02x slower                                                         |
| scimark_fft                | 301 ms                                                       | 308 ms: 1.02x slower                                                         |
| fannkuch                   | 350 ms                                                       | 358 ms: 1.02x slower                                                         |
| chameleon                  | 7.23 ms                                                      | 7.40 ms: 1.02x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 8.84 ms: 1.02x slower                                                        |
| pickle_dict                | 32.5 us                                                      | 33.3 us: 1.02x slower                                                        |
| django_template            | 38.2 ms                                                      | 39.1 ms: 1.02x slower                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 59.0 ms: 1.03x slower                                                        |
| dulwich_log                | 65.4 ms                                                      | 67.2 ms: 1.03x slower                                                        |
| deepcopy_memo              | 36.8 us                                                      | 37.8 us: 1.03x slower                                                        |
| unpickle_list              | 4.66 us                                                      | 4.80 us: 1.03x slower                                                        |
| json                       | 5.12 ms                                                      | 5.28 ms: 1.03x slower                                                        |
| sqlglot_normalize          | 116 ms                                                       | 119 ms: 1.03x slower                                                         |
| mako                       | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                                        |
| deepcopy                   | 368 us                                                       | 381 us: 1.03x slower                                                         |
| sympy_expand               | 484 ms                                                       | 501 ms: 1.04x slower                                                         |
| deltablue                  | 3.24 ms                                                      | 3.36 ms: 1.04x slower                                                        |
| regex_dna                  | 239 ms                                                       | 248 ms: 1.04x slower                                                         |
| regex_effbot               | 3.57 ms                                                      | 3.72 ms: 1.04x slower                                                        |
| gunicorn                   | 1.00 ms                                                      | 1.04 ms: 1.04x slower                                                        |
| docutils                   | 2.87 sec                                                     | 2.99 sec: 1.04x slower                                                       |
| aiohttp                    | 1.02 ms                                                      | 1.07 ms: 1.05x slower                                                        |
| float                      | 76.6 ms                                                      | 80.8 ms: 1.05x slower                                                        |
| spectral_norm              | 91.6 ms                                                      | 97.2 ms: 1.06x slower                                                        |
| unpickle                   | 14.8 us                                                      | 15.7 us: 1.06x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.37 ms: 1.07x slower                                                        |
| scimark_sor                | 109 ms                                                       | 117 ms: 1.08x slower                                                         |
| unpickle_pure_python       | 210 us                                                       | 226 us: 1.08x slower                                                         |
| json_dumps                 | 10.2 ms                                                      | 11.1 ms: 1.08x slower                                                        |
| go                         | 150 ms                                                       | 163 ms: 1.09x slower                                                         |
| pyflate                    | 439 ms                                                       | 484 ms: 1.10x slower                                                         |
| tomli_loads                | 2.16 sec                                                     | 2.39 sec: 1.11x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 26.4 ms: 1.12x slower                                                        |
| python_startup             | 11.6 ms                                                      | 13.2 ms: 1.14x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 173 us: 1.14x slower                                                         |
| richards                   | 45.7 ms                                                      | 53.5 ms: 1.17x slower                                                        |
| richards_super             | 51.3 ms                                                      | 60.3 ms: 1.17x slower                                                        |
| telco                      | 6.96 ms                                                      | 8.41 ms: 1.21x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 4.38 ms: 1.26x slower                                                        |
| coverage                   | 66.7 ms                                                      | 84.1 ms: 1.26x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.04 ms: 1.28x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.00x slower                                                                 |

Benchmark hidden because not significant (8): bench_mp_pool, scimark_sparse_mat_mult, xml_etree_parse, pycparser, deepcopy_reduce, asyncio_tcp, meteor_contest, sqlglot_transpile
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 83.74% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.93x