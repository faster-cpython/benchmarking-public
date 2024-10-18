# Results vs. 3.12.0

- fork: nick-arm
- ref: codecache
- machine: linux-x86_64
- commit hash: c2fad93
- commit date: 2024-10-17
- overall geometric mean: 1.08x slower
- HPT reliability: 74.06%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 316 ms: 1.11x slower                                                 |
| docutils       | 2.87 sec                                                     | 3.22 sec: 1.12x slower                                               |
| Geometric mean | (ref)                                                        | 1.08x slower                                                         |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 375 ms: 1.44x faster                                                 |
| async_tree_none_tg         | 431 ms                                                       | 306 ms: 1.41x faster                                                 |
| async_tree_none            | 452 ms                                                       | 322 ms: 1.40x faster                                                 |
| async_tree_memoization     | 544 ms                                                       | 411 ms: 1.32x faster                                                 |
| async_tree_io_tg           | 1.05 sec                                                     | 825 ms: 1.28x faster                                                 |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 557 ms: 1.25x faster                                                 |
| async_tree_io              | 1.04 sec                                                     | 837 ms: 1.25x faster                                                 |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 564 ms: 1.23x faster                                                 |
| Geometric mean             | (ref)                                                        | 1.32x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 80.3 ms: 1.10x faster                                                |
| pidigits       | 265 ms                                                       | 252 ms: 1.05x faster                                                 |
| float          | 76.6 ms                                                      | 78.1 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                        | 1.04x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.47 ms: 1.03x faster                                                |
| regex_compile  | 144 ms                                                       | 147 ms: 1.02x slower                                                 |
| regex_dna      | 239 ms                                                       | 247 ms: 1.03x slower                                                 |
| regex_v8       | 23.6 ms                                                      | 25.6 ms: 1.08x slower                                                |
| Geometric mean | (ref)                                                        | 1.03x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 79.4 ms: 1.09x faster                                                |
| pickle_dict          | 32.5 us                                                      | 30.2 us: 1.08x faster                                                |
| pickle_list          | 4.43 us                                                      | 4.25 us: 1.04x faster                                                |
| xml_etree_process    | 58.4 ms                                                      | 56.6 ms: 1.03x faster                                                |
| json_loads           | 24.4 us                                                      | 23.9 us: 1.02x faster                                                |
| pickle               | 10.5 us                                                      | 10.3 us: 1.02x faster                                                |
| tomli_loads          | 2.16 sec                                                     | 2.18 sec: 1.01x slower                                               |
| xml_etree_parse      | 144 ms                                                       | 145 ms: 1.01x slower                                                 |
| unpickle_list        | 4.66 us                                                      | 4.75 us: 1.02x slower                                                |
| json_dumps           | 10.2 ms                                                      | 10.5 ms: 1.02x slower                                                |
| unpickle_pure_python | 210 us                                                       | 220 us: 1.05x slower                                                 |
| pickle_pure_python   | 318 us                                                       | 335 us: 1.05x slower                                                 |
| unpickle             | 14.8 us                                                      | 15.7 us: 1.06x slower                                                |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                         |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.99 ms: 1.04x slower                                                |
| python_startup         | 11.6 ms                                                      | 14.9 ms: 1.29x slower                                                |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.15 ms: 1.09x faster                                                |
| django_template | 38.2 ms                                                      | 42.5 ms: 1.11x slower                                                |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 375 ms: 1.44x faster                                                 |
| async_tree_none_tg         | 431 ms                                                       | 306 ms: 1.41x faster                                                 |
| async_tree_none            | 452 ms                                                       | 322 ms: 1.40x faster                                                 |
| async_tree_memoization     | 544 ms                                                       | 411 ms: 1.32x faster                                                 |
| deepcopy_memo              | 36.8 us                                                      | 28.1 us: 1.31x faster                                                |
| async_tree_io_tg           | 1.05 sec                                                     | 825 ms: 1.28x faster                                                 |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 557 ms: 1.25x faster                                                 |
| async_tree_io              | 1.04 sec                                                     | 837 ms: 1.25x faster                                                 |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 564 ms: 1.23x faster                                                 |
| deepcopy                   | 368 us                                                       | 302 us: 1.22x faster                                                 |
| pathlib                    | 18.9 ms                                                      | 15.7 ms: 1.20x faster                                                |
| deepcopy_reduce            | 3.37 us                                                      | 2.98 us: 1.13x faster                                                |
| crypto_pyaes               | 80.3 ms                                                      | 71.1 ms: 1.13x faster                                                |
| comprehensions             | 21.9 us                                                      | 19.4 us: 1.13x faster                                                |
| nbody                      | 88.0 ms                                                      | 80.3 ms: 1.10x faster                                                |
| mako                       | 10.0 ms                                                      | 9.15 ms: 1.09x faster                                                |
| xml_etree_generate         | 86.1 ms                                                      | 79.4 ms: 1.09x faster                                                |
| scimark_fft                | 301 ms                                                       | 278 ms: 1.08x faster                                                 |
| pickle_dict                | 32.5 us                                                      | 30.2 us: 1.08x faster                                                |
| coroutines                 | 23.0 ms                                                      | 21.5 ms: 1.07x faster                                                |
| pidigits                   | 265 ms                                                       | 252 ms: 1.05x faster                                                 |
| logging_silent             | 94.4 ns                                                      | 90.2 ns: 1.05x faster                                                |
| pickle_list                | 4.43 us                                                      | 4.25 us: 1.04x faster                                                |
| scimark_sor                | 109 ms                                                       | 106 ms: 1.03x faster                                                 |
| xml_etree_process          | 58.4 ms                                                      | 56.6 ms: 1.03x faster                                                |
| regex_effbot               | 3.57 ms                                                      | 3.47 ms: 1.03x faster                                                |
| logging_format             | 7.48 us                                                      | 7.28 us: 1.03x faster                                                |
| sqlite_synth               | 2.77 us                                                      | 2.71 us: 1.02x faster                                                |
| pprint_pformat             | 1.65 sec                                                     | 1.62 sec: 1.02x faster                                               |
| json_loads                 | 24.4 us                                                      | 23.9 us: 1.02x faster                                                |
| pickle                     | 10.5 us                                                      | 10.3 us: 1.02x faster                                                |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.13 ms: 1.02x faster                                                |
| scimark_lu                 | 98.8 ms                                                      | 97.0 ms: 1.02x faster                                                |
| pprint_safe_repr           | 807 ms                                                       | 794 ms: 1.02x faster                                                 |
| spectral_norm              | 91.6 ms                                                      | 90.2 ms: 1.02x faster                                                |
| richards                   | 45.7 ms                                                      | 45.0 ms: 1.02x faster                                                |
| async_generators           | 390 ms                                                       | 386 ms: 1.01x faster                                                 |
| scimark_monte_carlo        | 69.0 ms                                                      | 68.3 ms: 1.01x faster                                                |
| asyncio_websockets         | 387 ms                                                       | 383 ms: 1.01x faster                                                 |
| asyncio_tcp                | 378 ms                                                       | 377 ms: 1.00x faster                                                 |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.00x faster                                               |
| dulwich_log                | 65.4 ms                                                      | 65.9 ms: 1.01x slower                                                |
| tomli_loads                | 2.16 sec                                                     | 2.18 sec: 1.01x slower                                               |
| json                       | 5.12 ms                                                      | 5.17 ms: 1.01x slower                                                |
| xml_etree_parse            | 144 ms                                                       | 145 ms: 1.01x slower                                                 |
| go                         | 150 ms                                                       | 152 ms: 1.01x slower                                                 |
| pycparser                  | 1.23 sec                                                     | 1.25 sec: 1.02x slower                                               |
| mdp                        | 2.57 sec                                                     | 2.62 sec: 1.02x slower                                               |
| float                      | 76.6 ms                                                      | 78.1 ms: 1.02x slower                                                |
| bench_thread_pool          | 950 us                                                       | 968 us: 1.02x slower                                                 |
| unpickle_list              | 4.66 us                                                      | 4.75 us: 1.02x slower                                                |
| regex_compile              | 144 ms                                                       | 147 ms: 1.02x slower                                                 |
| json_dumps                 | 10.2 ms                                                      | 10.5 ms: 1.02x slower                                                |
| pyflate                    | 439 ms                                                       | 450 ms: 1.03x slower                                                 |
| regex_dna                  | 239 ms                                                       | 247 ms: 1.03x slower                                                 |
| richards_super             | 51.3 ms                                                      | 53.3 ms: 1.04x slower                                                |
| python_startup_no_site     | 8.64 ms                                                      | 8.99 ms: 1.04x slower                                                |
| meteor_contest             | 128 ms                                                       | 134 ms: 1.04x slower                                                 |
| unpickle_pure_python       | 210 us                                                       | 220 us: 1.05x slower                                                 |
| fannkuch                   | 350 ms                                                       | 367 ms: 1.05x slower                                                 |
| pickle_pure_python         | 318 us                                                       | 335 us: 1.05x slower                                                 |
| sympy_str                  | 302 ms                                                       | 320 ms: 1.06x slower                                                 |
| unpickle                   | 14.8 us                                                      | 15.7 us: 1.06x slower                                                |
| generators                 | 37.4 ms                                                      | 39.8 ms: 1.06x slower                                                |
| chaos                      | 64.0 ms                                                      | 68.4 ms: 1.07x slower                                                |
| sympy_sum                  | 162 ms                                                       | 174 ms: 1.08x slower                                                 |
| regex_v8                   | 23.6 ms                                                      | 25.6 ms: 1.08x slower                                                |
| sympy_expand               | 484 ms                                                       | 526 ms: 1.09x slower                                                 |
| raytrace                   | 298 ms                                                       | 324 ms: 1.09x slower                                                 |
| sqlglot_parse              | 1.38 ms                                                      | 1.50 ms: 1.09x slower                                                |
| 2to3                       | 285 ms                                                       | 316 ms: 1.11x slower                                                 |
| sqlglot_transpile          | 1.78 ms                                                      | 1.97 ms: 1.11x slower                                                |
| django_template            | 38.2 ms                                                      | 42.5 ms: 1.11x slower                                                |
| telco                      | 6.96 ms                                                      | 7.76 ms: 1.11x slower                                                |
| docutils                   | 2.87 sec                                                     | 3.22 sec: 1.12x slower                                               |
| nqueens                    | 89.9 ms                                                      | 102 ms: 1.14x slower                                                 |
| sympy_integrate            | 23.9 ms                                                      | 27.3 ms: 1.14x slower                                                |
| sqlglot_normalize          | 116 ms                                                       | 135 ms: 1.17x slower                                                 |
| coverage                   | 66.7 ms                                                      | 78.4 ms: 1.18x slower                                                |
| typing_runtime_protocols   | 152 us                                                       | 181 us: 1.20x slower                                                 |
| hexiom                     | 5.96 ms                                                      | 7.13 ms: 1.20x slower                                                |
| sqlglot_optimize           | 57.5 ms                                                      | 69.3 ms: 1.21x slower                                                |
| python_startup             | 11.6 ms                                                      | 14.9 ms: 1.29x slower                                                |
| gc_traversal               | 3.48 ms                                                      | 5.17 ms: 1.49x slower                                                |
| unpack_sequence            | 53.2 ns                                                      | 88.6 ns: 1.67x slower                                                |
| create_gc_cycles           | 1.59 ms                                                      | 2.80 ms: 1.76x slower                                                |
| bench_mp_pool              | 4.76 ms                                                      | 2.97 sec: 623.86x slower                                             |
| Geometric mean             | (ref)                                                        | 1.08x slower                                                         |

Benchmark hidden because not significant (4): xml_etree_iterparse, logging_simple, deltablue, tornado_http
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (7) of results/bm-20241017-3.14.0a0-c2fad93-JIT/bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

# HPT report

- Reliability score: 74.06% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.10x