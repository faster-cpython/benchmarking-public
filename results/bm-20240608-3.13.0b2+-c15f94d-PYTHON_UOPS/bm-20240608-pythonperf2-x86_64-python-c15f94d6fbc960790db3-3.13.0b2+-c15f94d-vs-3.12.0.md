# Results vs. 3.12.0

- fork: python
- ref: c15f94d6fbc960790db3
- machine: linux-x86_64
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.17x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x slower
- Memory change: 0.94x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 345 ms: 1.21x slower                                                         |
| chameleon      | 7.23 ms                                                      | 8.61 ms: 1.19x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.47 sec: 1.21x slower                                                       |
| tornado_http   | 121 ms                                                       | 129 ms: 1.07x slower                                                         |
| Geometric mean | (ref)                                                        | 1.17x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 454 ms: 1.19x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 366 ms: 1.18x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 904 ms: 1.17x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 475 ms: 1.14x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 613 ms: 1.14x faster                                                         |
| async_tree_none            | 452 ms                                                       | 398 ms: 1.13x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 943 ms: 1.10x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 654 ms: 1.06x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.14x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                         |
| float          | 76.6 ms                                                      | 96.2 ms: 1.26x slower                                                        |
| nbody          | 88.0 ms                                                      | 125 ms: 1.42x slower                                                         |
| Geometric mean | (ref)                                                        | 1.20x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.56 ms: 1.00x faster                                                        |
| regex_dna      | 239 ms                                                       | 255 ms: 1.07x slower                                                         |
| regex_v8       | 23.6 ms                                                      | 26.0 ms: 1.10x slower                                                        |
| regex_compile  | 144 ms                                                       | 216 ms: 1.50x slower                                                         |
| Geometric mean | (ref)                                                        | 1.15x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_dict          | 32.5 us                                                      | 31.3 us: 1.04x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 145 ms: 1.01x slower                                                         |
| unpickle             | 14.8 us                                                      | 15.0 us: 1.01x slower                                                        |
| unpickle_list        | 4.66 us                                                      | 4.73 us: 1.01x slower                                                        |
| pickle_list          | 4.43 us                                                      | 4.56 us: 1.03x slower                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 113 ms: 1.10x slower                                                         |
| json_dumps           | 10.2 ms                                                      | 11.3 ms: 1.11x slower                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 97.0 ms: 1.13x slower                                                        |
| xml_etree_process    | 58.4 ms                                                      | 68.8 ms: 1.18x slower                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.91 sec: 1.35x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 434 us: 1.36x slower                                                         |
| unpickle_pure_python | 210 us                                                       | 307 us: 1.46x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.11x slower                                                                 |

Benchmark hidden because not significant (2): pickle, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.91 ms: 1.03x slower                                                        |
| python_startup         | 11.6 ms                                                      | 13.2 ms: 1.14x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.08x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 45.5 ms: 1.19x slower                                                        |
| mako            | 10.0 ms                                                      | 14.6 ms: 1.46x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.32x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 454 ms: 1.19x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 366 ms: 1.18x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 904 ms: 1.17x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 475 ms: 1.14x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 613 ms: 1.14x faster                                                         |
| async_tree_none            | 452 ms                                                       | 398 ms: 1.13x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 943 ms: 1.10x faster                                                         |
| generators                 | 37.4 ms                                                      | 34.1 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 654 ms: 1.06x faster                                                         |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                         |
| pickle_dict                | 32.5 us                                                      | 31.3 us: 1.04x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 18.3 ms: 1.03x faster                                                        |
| logging_format             | 7.48 us                                                      | 7.39 us: 1.01x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 22.8 ms: 1.01x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.56 ms: 1.00x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 145 ms: 1.01x slower                                                         |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.60 sec: 1.01x slower                                                       |
| async_generators           | 390 ms                                                       | 395 ms: 1.01x slower                                                         |
| unpickle                   | 14.8 us                                                      | 15.0 us: 1.01x slower                                                        |
| unpickle_list              | 4.66 us                                                      | 4.73 us: 1.01x slower                                                        |
| logging_simple             | 6.71 us                                                      | 6.82 us: 1.02x slower                                                        |
| asyncio_tcp                | 378 ms                                                       | 388 ms: 1.03x slower                                                         |
| pickle_list                | 4.43 us                                                      | 4.56 us: 1.03x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 8.91 ms: 1.03x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 4.97 ms: 1.04x slower                                                        |
| tornado_http               | 121 ms                                                       | 129 ms: 1.07x slower                                                         |
| regex_dna                  | 239 ms                                                       | 255 ms: 1.07x slower                                                         |
| json                       | 5.12 ms                                                      | 5.48 ms: 1.07x slower                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.97 us: 1.07x slower                                                        |
| mdp                        | 2.57 sec                                                     | 2.77 sec: 1.08x slower                                                       |
| bench_thread_pool          | 950 us                                                       | 1.02 ms: 1.08x slower                                                        |
| mypy2                      | 830 ms                                                       | 897 ms: 1.08x slower                                                         |
| dask                       | 392 ms                                                       | 427 ms: 1.09x slower                                                         |
| regex_v8                   | 23.6 ms                                                      | 26.0 ms: 1.10x slower                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 113 ms: 1.10x slower                                                         |
| json_dumps                 | 10.2 ms                                                      | 11.3 ms: 1.11x slower                                                        |
| meteor_contest             | 128 ms                                                       | 143 ms: 1.12x slower                                                         |
| xml_etree_generate         | 86.1 ms                                                      | 97.0 ms: 1.13x slower                                                        |
| raytrace                   | 298 ms                                                       | 338 ms: 1.13x slower                                                         |
| python_startup             | 11.6 ms                                                      | 13.2 ms: 1.14x slower                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 92.4 ms: 1.15x slower                                                        |
| gunicorn                   | 1.00 ms                                                      | 1.16 ms: 1.16x slower                                                        |
| sympy_sum                  | 162 ms                                                       | 189 ms: 1.16x slower                                                         |
| sympy_integrate            | 23.9 ms                                                      | 28.1 ms: 1.17x slower                                                        |
| aiohttp                    | 1.02 ms                                                      | 1.19 ms: 1.17x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.45 sec: 1.17x slower                                                       |
| xml_etree_process          | 58.4 ms                                                      | 68.8 ms: 1.18x slower                                                        |
| django_template            | 38.2 ms                                                      | 45.5 ms: 1.19x slower                                                        |
| chameleon                  | 7.23 ms                                                      | 8.61 ms: 1.19x slower                                                        |
| dulwich_log                | 65.4 ms                                                      | 78.3 ms: 1.20x slower                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 4.07 us: 1.21x slower                                                        |
| docutils                   | 2.87 sec                                                     | 3.47 sec: 1.21x slower                                                       |
| 2to3                       | 285 ms                                                       | 345 ms: 1.21x slower                                                         |
| sqlglot_normalize          | 116 ms                                                       | 141 ms: 1.22x slower                                                         |
| sympy_str                  | 302 ms                                                       | 371 ms: 1.23x slower                                                         |
| sqlglot_optimize           | 57.5 ms                                                      | 70.7 ms: 1.23x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 2.20 ms: 1.24x slower                                                        |
| coverage                   | 66.7 ms                                                      | 83.4 ms: 1.25x slower                                                        |
| float                      | 76.6 ms                                                      | 96.2 ms: 1.26x slower                                                        |
| comprehensions             | 21.9 us                                                      | 27.6 us: 1.26x slower                                                        |
| chaos                      | 64.0 ms                                                      | 80.7 ms: 1.26x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.74 ms: 1.26x slower                                                        |
| pprint_pformat             | 1.65 sec                                                     | 2.11 sec: 1.28x slower                                                       |
| pprint_safe_repr           | 807 ms                                                       | 1.04 sec: 1.29x slower                                                       |
| deepcopy                   | 368 us                                                       | 475 us: 1.29x slower                                                         |
| sympy_expand               | 484 ms                                                       | 628 ms: 1.30x slower                                                         |
| create_gc_cycles           | 1.59 ms                                                      | 2.06 ms: 1.30x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 197 us: 1.30x slower                                                         |
| nqueens                    | 89.9 ms                                                      | 117 ms: 1.30x slower                                                         |
| richards_super             | 51.3 ms                                                      | 68.3 ms: 1.33x slower                                                        |
| richards                   | 45.7 ms                                                      | 61.2 ms: 1.34x slower                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.91 sec: 1.35x slower                                                       |
| go                         | 150 ms                                                       | 202 ms: 1.35x slower                                                         |
| telco                      | 6.96 ms                                                      | 9.41 ms: 1.35x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 4.72 ms: 1.36x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 434 us: 1.36x slower                                                         |
| fannkuch                   | 350 ms                                                       | 479 ms: 1.37x slower                                                         |
| deltablue                  | 3.24 ms                                                      | 4.54 ms: 1.40x slower                                                        |
| nbody                      | 88.0 ms                                                      | 125 ms: 1.42x slower                                                         |
| scimark_fft                | 301 ms                                                       | 433 ms: 1.44x slower                                                         |
| scimark_monte_carlo        | 69.0 ms                                                      | 99.7 ms: 1.45x slower                                                        |
| pyflate                    | 439 ms                                                       | 637 ms: 1.45x slower                                                         |
| unpickle_pure_python       | 210 us                                                       | 307 us: 1.46x slower                                                         |
| mako                       | 10.0 ms                                                      | 14.6 ms: 1.46x slower                                                        |
| scimark_lu                 | 98.8 ms                                                      | 145 ms: 1.47x slower                                                         |
| scimark_sor                | 109 ms                                                       | 163 ms: 1.49x slower                                                         |
| regex_compile              | 144 ms                                                       | 216 ms: 1.50x slower                                                         |
| deepcopy_memo              | 36.8 us                                                      | 57.7 us: 1.57x slower                                                        |
| spectral_norm              | 91.6 ms                                                      | 147 ms: 1.60x slower                                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 6.80 ms: 1.62x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 157 ns: 1.66x slower                                                         |
| hexiom                     | 5.96 ms                                                      | 10.6 ms: 1.78x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.17x slower                                                                 |

Benchmark hidden because not significant (3): asyncio_websockets, pickle, json_loads
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240608-3.13.0b2+-c15f94d-PYTHON_UOPS/bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.13x
- 95% likely to have a slowdown of 1.12x
- 99% likely to have a slowdown of 1.09x

# Memory
- memory change: 0.94x