# Results vs. 3.12.0

- fork: python
- ref: edb6883ef3f7a8ef0c83
- machine: linux-x86_64
- commit hash: edb6883
- commit date: 2024-06-01
- overall geometric mean: 1.00x slower
- HPT reliability: 89.59%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240601-pythonperf2-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 293 ms: 1.03x slower                                                         |
| chameleon      | 7.23 ms                                                      | 7.46 ms: 1.03x slower                                                        |
| docutils       | 2.87 sec                                                     | 2.98 sec: 1.04x slower                                                       |
| tornado_http   | 121 ms                                                       | 119 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240601-pythonperf2-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 428 ms: 1.26x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 345 ms: 1.25x faster                                                         |
| async_tree_none            | 452 ms                                                       | 368 ms: 1.23x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 581 ms: 1.20x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 885 ms: 1.18x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 464 ms: 1.17x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 906 ms: 1.16x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 612 ms: 1.14x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.20x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240601-pythonperf2-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                         |
| nbody          | 88.0 ms                                                      | 87.0 ms: 1.01x faster                                                        |
| float          | 76.6 ms                                                      | 79.2 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240601-pythonperf2-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 144 ms: 1.00x faster                                                         |
| regex_effbot   | 3.57 ms                                                      | 3.59 ms: 1.01x slower                                                        |
| regex_dna      | 239 ms                                                       | 251 ms: 1.05x slower                                                         |
| regex_v8       | 23.6 ms                                                      | 25.5 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240601-pythonperf2-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_dict          | 32.5 us                                                      | 31.1 us: 1.05x faster                                                        |
| pickle_pure_python   | 318 us                                                       | 310 us: 1.03x faster                                                         |
| pickle               | 10.5 us                                                      | 10.4 us: 1.01x faster                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 86.7 ms: 1.01x slower                                                        |
| json_loads           | 24.4 us                                                      | 24.8 us: 1.02x slower                                                        |
| unpickle             | 14.8 us                                                      | 15.2 us: 1.02x slower                                                        |
| unpickle_list        | 4.66 us                                                      | 4.79 us: 1.03x slower                                                        |
| xml_etree_process    | 58.4 ms                                                      | 60.5 ms: 1.04x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 10.7 ms: 1.05x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 224 us: 1.07x slower                                                         |
| tomli_loads          | 2.16 sec                                                     | 2.40 sec: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                                 |

Benchmark hidden because not significant (3): xml_etree_iterparse, pickle_list, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240601-pythonperf2-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.79 ms: 1.02x slower                                                        |
| python_startup         | 11.6 ms                                                      | 13.1 ms: 1.13x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240601-pythonperf2-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 39.4 ms: 1.03x slower                                                        |
| mako            | 10.0 ms                                                      | 10.7 ms: 1.07x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.05x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240601-pythonperf2-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| comprehensions             | 21.9 us                                                      | 17.0 us: 1.29x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 428 ms: 1.26x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 345 ms: 1.25x faster                                                         |
| async_tree_none            | 452 ms                                                       | 368 ms: 1.23x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 581 ms: 1.20x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 885 ms: 1.18x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 464 ms: 1.17x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 906 ms: 1.16x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 612 ms: 1.14x faster                                                         |
| raytrace                   | 298 ms                                                       | 265 ms: 1.12x faster                                                         |
| crypto_pyaes               | 80.3 ms                                                      | 72.7 ms: 1.10x faster                                                        |
| generators                 | 37.4 ms                                                      | 34.3 ms: 1.09x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 17.4 ms: 1.09x faster                                                        |
| async_generators           | 390 ms                                                       | 359 ms: 1.09x faster                                                         |
| mypy2                      | 830 ms                                                       | 770 ms: 1.08x faster                                                         |
| logging_format             | 7.48 us                                                      | 6.97 us: 1.07x faster                                                        |
| chaos                      | 64.0 ms                                                      | 60.7 ms: 1.05x faster                                                        |
| bench_thread_pool          | 950 us                                                       | 903 us: 1.05x faster                                                         |
| logging_simple             | 6.71 us                                                      | 6.39 us: 1.05x faster                                                        |
| pickle_dict                | 32.5 us                                                      | 31.1 us: 1.05x faster                                                        |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                         |
| sympy_sum                  | 162 ms                                                       | 155 ms: 1.05x faster                                                         |
| coroutines                 | 23.0 ms                                                      | 22.0 ms: 1.04x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 66.2 ms: 1.04x faster                                                        |
| pickle_pure_python         | 318 us                                                       | 310 us: 1.03x faster                                                         |
| mdp                        | 2.57 sec                                                     | 2.52 sec: 1.02x faster                                                       |
| sympy_integrate            | 23.9 ms                                                      | 23.5 ms: 1.02x faster                                                        |
| sympy_str                  | 302 ms                                                       | 297 ms: 1.02x faster                                                         |
| tornado_http               | 121 ms                                                       | 119 ms: 1.02x faster                                                         |
| scimark_lu                 | 98.8 ms                                                      | 97.4 ms: 1.01x faster                                                        |
| nbody                      | 88.0 ms                                                      | 87.0 ms: 1.01x faster                                                        |
| pickle                     | 10.5 us                                                      | 10.4 us: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.00x faster                                                       |
| regex_compile              | 144 ms                                                       | 144 ms: 1.00x faster                                                         |
| regex_effbot               | 3.57 ms                                                      | 3.59 ms: 1.01x slower                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 86.7 ms: 1.01x slower                                                        |
| scimark_fft                | 301 ms                                                       | 304 ms: 1.01x slower                                                         |
| meteor_contest             | 128 ms                                                       | 129 ms: 1.01x slower                                                         |
| nqueens                    | 89.9 ms                                                      | 91.1 ms: 1.01x slower                                                        |
| deepcopy_memo              | 36.8 us                                                      | 37.3 us: 1.01x slower                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.82 us: 1.02x slower                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 3.42 us: 1.02x slower                                                        |
| fannkuch                   | 350 ms                                                       | 355 ms: 1.02x slower                                                         |
| json_loads                 | 24.4 us                                                      | 24.8 us: 1.02x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 8.79 ms: 1.02x slower                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.69 sec: 1.02x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.41 ms: 1.02x slower                                                        |
| json                       | 5.12 ms                                                      | 5.23 ms: 1.02x slower                                                        |
| unpickle                   | 14.8 us                                                      | 15.2 us: 1.02x slower                                                        |
| pprint_safe_repr           | 807 ms                                                       | 826 ms: 1.02x slower                                                         |
| 2to3                       | 285 ms                                                       | 293 ms: 1.03x slower                                                         |
| pycparser                  | 1.23 sec                                                     | 1.27 sec: 1.03x slower                                                       |
| unpickle_list              | 4.66 us                                                      | 4.79 us: 1.03x slower                                                        |
| chameleon                  | 7.23 ms                                                      | 7.46 ms: 1.03x slower                                                        |
| deepcopy                   | 368 us                                                       | 380 us: 1.03x slower                                                         |
| logging_silent             | 94.4 ns                                                      | 97.5 ns: 1.03x slower                                                        |
| float                      | 76.6 ms                                                      | 79.2 ms: 1.03x slower                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 59.4 ms: 1.03x slower                                                        |
| dulwich_log                | 65.4 ms                                                      | 67.5 ms: 1.03x slower                                                        |
| django_template            | 38.2 ms                                                      | 39.4 ms: 1.03x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 60.5 ms: 1.04x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 3.36 ms: 1.04x slower                                                        |
| docutils                   | 2.87 sec                                                     | 2.98 sec: 1.04x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 10.7 ms: 1.05x slower                                                        |
| sympy_expand               | 484 ms                                                       | 506 ms: 1.05x slower                                                         |
| aiohttp                    | 1.02 ms                                                      | 1.07 ms: 1.05x slower                                                        |
| sqlglot_normalize          | 116 ms                                                       | 121 ms: 1.05x slower                                                         |
| gunicorn                   | 1.00 ms                                                      | 1.05 ms: 1.05x slower                                                        |
| scimark_sor                | 109 ms                                                       | 114 ms: 1.05x slower                                                         |
| regex_dna                  | 239 ms                                                       | 251 ms: 1.05x slower                                                         |
| spectral_norm              | 91.6 ms                                                      | 96.8 ms: 1.06x slower                                                        |
| mako                       | 10.0 ms                                                      | 10.7 ms: 1.07x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 224 us: 1.07x slower                                                         |
| go                         | 150 ms                                                       | 160 ms: 1.07x slower                                                         |
| regex_v8                   | 23.6 ms                                                      | 25.5 ms: 1.08x slower                                                        |
| pyflate                    | 439 ms                                                       | 482 ms: 1.10x slower                                                         |
| hexiom                     | 5.96 ms                                                      | 6.55 ms: 1.10x slower                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.40 sec: 1.11x slower                                                       |
| python_startup             | 11.6 ms                                                      | 13.1 ms: 1.13x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 174 us: 1.15x slower                                                         |
| richards_super             | 51.3 ms                                                      | 61.5 ms: 1.20x slower                                                        |
| richards                   | 45.7 ms                                                      | 55.3 ms: 1.21x slower                                                        |
| telco                      | 6.96 ms                                                      | 8.58 ms: 1.23x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 1.99 ms: 1.25x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 4.47 ms: 1.29x slower                                                        |
| coverage                   | 66.7 ms                                                      | 86.7 ms: 1.30x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.00x slower                                                                 |

Benchmark hidden because not significant (9): xml_etree_iterparse, scimark_sparse_mat_mult, asyncio_tcp, pickle_list, dask, sqlglot_transpile, xml_etree_parse, asyncio_websockets, bench_mp_pool
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240601-3.13.0b1+-edb6883/bm-20240601-pythonperf2-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 89.59% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.93x