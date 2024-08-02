# Results vs. 3.12.0

- fork: python
- ref: c15f94d6fbc960790db3
- machine: linux-x86_64
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.01x slower
- HPT reliability: 69.05%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 306 ms: 1.07x slower                                                         |
| chameleon      | 7.23 ms                                                      | 7.67 ms: 1.06x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.13 sec: 1.09x slower                                                       |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                 |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 843 ms: 1.25x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 438 ms: 1.23x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 350 ms: 1.23x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 447 ms: 1.22x faster                                                         |
| async_tree_none            | 452 ms                                                       | 376 ms: 1.20x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 586 ms: 1.19x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 883 ms: 1.18x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 627 ms: 1.11x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.20x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 250 ms: 1.06x faster                                                         |
| nbody          | 88.0 ms                                                      | 84.0 ms: 1.05x faster                                                        |
| float          | 76.6 ms                                                      | 73.3 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 140 ms: 1.03x faster                                                         |
| regex_effbot   | 3.57 ms                                                      | 3.62 ms: 1.01x slower                                                        |
| regex_dna      | 239 ms                                                       | 251 ms: 1.05x slower                                                         |
| regex_v8       | 23.6 ms                                                      | 25.2 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 82.9 ms: 1.04x faster                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.09 sec: 1.03x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 100 ms: 1.02x faster                                                         |
| pickle_pure_python   | 318 us                                                       | 316 us: 1.01x faster                                                         |
| xml_etree_parse      | 144 ms                                                       | 143 ms: 1.01x faster                                                         |
| unpickle_list        | 4.66 us                                                      | 4.70 us: 1.01x slower                                                        |
| json_loads           | 24.4 us                                                      | 24.7 us: 1.01x slower                                                        |
| pickle_list          | 4.43 us                                                      | 4.54 us: 1.02x slower                                                        |
| pickle               | 10.5 us                                                      | 10.9 us: 1.03x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 10.7 ms: 1.04x slower                                                        |
| pickle_dict          | 32.5 us                                                      | 34.0 us: 1.04x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 221 us: 1.05x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (2): xml_etree_process, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.44 ms: 1.09x slower                                                        |
| python_startup         | 11.6 ms                                                      | 13.8 ms: 1.19x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.14x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.15 ms: 1.09x faster                                                        |
| django_template | 38.2 ms                                                      | 41.9 ms: 1.10x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.00x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 843 ms: 1.25x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 438 ms: 1.23x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 350 ms: 1.23x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 447 ms: 1.22x faster                                                         |
| comprehensions             | 21.9 us                                                      | 18.1 us: 1.21x faster                                                        |
| async_tree_none            | 452 ms                                                       | 376 ms: 1.20x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 586 ms: 1.19x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 883 ms: 1.18x faster                                                         |
| crypto_pyaes               | 80.3 ms                                                      | 71.1 ms: 1.13x faster                                                        |
| spectral_norm              | 91.6 ms                                                      | 81.6 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 627 ms: 1.11x faster                                                         |
| mako                       | 10.0 ms                                                      | 9.15 ms: 1.09x faster                                                        |
| generators                 | 37.4 ms                                                      | 34.3 ms: 1.09x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 17.6 ms: 1.07x faster                                                        |
| logging_format             | 7.48 us                                                      | 7.02 us: 1.07x faster                                                        |
| pidigits                   | 265 ms                                                       | 250 ms: 1.06x faster                                                         |
| coroutines                 | 23.0 ms                                                      | 21.8 ms: 1.05x faster                                                        |
| nbody                      | 88.0 ms                                                      | 84.0 ms: 1.05x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.41 us: 1.05x faster                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.02 ms: 1.05x faster                                                        |
| float                      | 76.6 ms                                                      | 73.3 ms: 1.05x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 66.3 ms: 1.04x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 82.9 ms: 1.04x faster                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.09 sec: 1.03x faster                                                       |
| async_generators           | 390 ms                                                       | 378 ms: 1.03x faster                                                         |
| regex_compile              | 144 ms                                                       | 140 ms: 1.03x faster                                                         |
| xml_etree_iterparse        | 103 ms                                                       | 100 ms: 1.02x faster                                                         |
| scimark_fft                | 301 ms                                                       | 295 ms: 1.02x faster                                                         |
| fannkuch                   | 350 ms                                                       | 343 ms: 1.02x faster                                                         |
| richards                   | 45.7 ms                                                      | 45.4 ms: 1.01x faster                                                        |
| pickle_pure_python         | 318 us                                                       | 316 us: 1.01x faster                                                         |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                       |
| xml_etree_parse            | 144 ms                                                       | 143 ms: 1.01x faster                                                         |
| mdp                        | 2.57 sec                                                     | 2.56 sec: 1.00x faster                                                       |
| asyncio_tcp                | 378 ms                                                       | 380 ms: 1.00x slower                                                         |
| dulwich_log                | 65.4 ms                                                      | 65.9 ms: 1.01x slower                                                        |
| unpickle_list              | 4.66 us                                                      | 4.70 us: 1.01x slower                                                        |
| json_loads                 | 24.4 us                                                      | 24.7 us: 1.01x slower                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.62 ms: 1.01x slower                                                        |
| richards_super             | 51.3 ms                                                      | 52.4 ms: 1.02x slower                                                        |
| meteor_contest             | 128 ms                                                       | 131 ms: 1.02x slower                                                         |
| pickle_list                | 4.43 us                                                      | 4.54 us: 1.02x slower                                                        |
| chaos                      | 64.0 ms                                                      | 65.6 ms: 1.03x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.82 ms: 1.03x slower                                                        |
| dask                       | 392 ms                                                       | 403 ms: 1.03x slower                                                         |
| sympy_sum                  | 162 ms                                                       | 167 ms: 1.03x slower                                                         |
| sqlglot_parse              | 1.38 ms                                                      | 1.42 ms: 1.03x slower                                                        |
| sympy_str                  | 302 ms                                                       | 312 ms: 1.03x slower                                                         |
| pickle                     | 10.5 us                                                      | 10.9 us: 1.03x slower                                                        |
| json                       | 5.12 ms                                                      | 5.33 ms: 1.04x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 10.7 ms: 1.04x slower                                                        |
| pickle_dict                | 32.5 us                                                      | 34.0 us: 1.04x slower                                                        |
| regex_dna                  | 239 ms                                                       | 251 ms: 1.05x slower                                                         |
| unpickle_pure_python       | 210 us                                                       | 221 us: 1.05x slower                                                         |
| pyflate                    | 439 ms                                                       | 463 ms: 1.05x slower                                                         |
| chameleon                  | 7.23 ms                                                      | 7.67 ms: 1.06x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 25.2 ms: 1.07x slower                                                        |
| 2to3                       | 285 ms                                                       | 306 ms: 1.07x slower                                                         |
| sympy_integrate            | 23.9 ms                                                      | 25.7 ms: 1.07x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 96.9 ms: 1.08x slower                                                        |
| docutils                   | 2.87 sec                                                     | 3.13 sec: 1.09x slower                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 3.68 us: 1.09x slower                                                        |
| sympy_expand               | 484 ms                                                       | 529 ms: 1.09x slower                                                         |
| python_startup_no_site     | 8.64 ms                                                      | 9.44 ms: 1.09x slower                                                        |
| go                         | 150 ms                                                       | 164 ms: 1.10x slower                                                         |
| sqlglot_optimize           | 57.5 ms                                                      | 63.0 ms: 1.10x slower                                                        |
| django_template            | 38.2 ms                                                      | 41.9 ms: 1.10x slower                                                        |
| sqlglot_normalize          | 116 ms                                                       | 128 ms: 1.11x slower                                                         |
| hexiom                     | 5.96 ms                                                      | 6.65 ms: 1.12x slower                                                        |
| deepcopy                   | 368 us                                                       | 418 us: 1.13x slower                                                         |
| aiohttp                    | 1.02 ms                                                      | 1.17 ms: 1.15x slower                                                        |
| scimark_lu                 | 98.8 ms                                                      | 114 ms: 1.15x slower                                                         |
| deltablue                  | 3.24 ms                                                      | 3.74 ms: 1.16x slower                                                        |
| gunicorn                   | 1.00 ms                                                      | 1.16 ms: 1.16x slower                                                        |
| telco                      | 6.96 ms                                                      | 8.19 ms: 1.18x slower                                                        |
| python_startup             | 11.6 ms                                                      | 13.8 ms: 1.19x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 182 us: 1.20x slower                                                         |
| coverage                   | 66.7 ms                                                      | 80.5 ms: 1.21x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 1.94 ms: 1.22x slower                                                        |
| scimark_sor                | 109 ms                                                       | 138 ms: 1.27x slower                                                         |
| logging_silent             | 94.4 ns                                                      | 120 ns: 1.27x slower                                                         |
| gc_traversal               | 3.48 ms                                                      | 4.44 ms: 1.28x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (13): pprint_pformat, pycparser, raytrace, xml_etree_process, bench_mp_pool, deepcopy_memo, unpickle, sqlite_synth, bench_thread_pool, asyncio_websockets, pprint_safe_repr, tornado_http, mypy2
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240608-3.13.0b2+-c15f94d-JIT/bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 69.05% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x