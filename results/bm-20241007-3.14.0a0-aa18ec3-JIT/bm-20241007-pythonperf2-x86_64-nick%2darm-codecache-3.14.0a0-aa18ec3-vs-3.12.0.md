# Results vs. 3.12.0

- fork: nick-arm
- ref: codecache
- machine: linux-x86_64
- commit hash: aa18ec3
- commit date: 2024-10-07
- overall geometric mean: 1.016x faster
- HPT reliability: 62.46%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 317 ms: 1.11x slower                                                 |
| docutils       | 2.87 sec                                                     | 3.19 sec: 1.11x slower                                               |
| Geometric mean | (ref)                                                        | 1.08x slower                                                         |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 310 ms: 1.39x faster                                                 |
| async_tree_memoization_tg  | 540 ms                                                       | 391 ms: 1.38x faster                                                 |
| async_tree_none            | 452 ms                                                       | 327 ms: 1.38x faster                                                 |
| async_tree_memoization     | 544 ms                                                       | 406 ms: 1.34x faster                                                 |
| async_tree_io_tg           | 1.05 sec                                                     | 792 ms: 1.33x faster                                                 |
| async_tree_io              | 1.04 sec                                                     | 804 ms: 1.30x faster                                                 |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 549 ms: 1.27x faster                                                 |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 580 ms: 1.20x faster                                                 |
| Geometric mean             | (ref)                                                        | 1.32x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 250 ms: 1.06x faster                                                 |
| nbody          | 88.0 ms                                                      | 84.2 ms: 1.04x faster                                                |
| float          | 76.6 ms                                                      | 75.8 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                        | 1.04x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.43 ms: 1.04x faster                                                |
| regex_dna      | 239 ms                                                       | 245 ms: 1.03x slower                                                 |
| regex_v8       | 23.6 ms                                                      | 24.7 ms: 1.05x slower                                                |
| regex_compile  | 144 ms                                                       | 152 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                        | 1.02x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 78.0 ms: 1.10x faster                                                |
| pickle_dict          | 32.5 us                                                      | 30.8 us: 1.06x faster                                                |
| pickle_list          | 4.43 us                                                      | 4.20 us: 1.05x faster                                                |
| xml_etree_iterparse  | 103 ms                                                       | 98.4 ms: 1.05x faster                                                |
| xml_etree_process    | 58.4 ms                                                      | 56.2 ms: 1.04x faster                                                |
| xml_etree_parse      | 144 ms                                                       | 140 ms: 1.03x faster                                                 |
| json_loads           | 24.4 us                                                      | 23.8 us: 1.02x faster                                                |
| pickle               | 10.5 us                                                      | 10.3 us: 1.02x faster                                                |
| tomli_loads          | 2.16 sec                                                     | 2.17 sec: 1.01x slower                                               |
| unpickle_list        | 4.66 us                                                      | 4.76 us: 1.02x slower                                                |
| json_dumps           | 10.2 ms                                                      | 10.5 ms: 1.02x slower                                                |
| unpickle_pure_python | 210 us                                                       | 215 us: 1.03x slower                                                 |
| pickle_pure_python   | 318 us                                                       | 329 us: 1.03x slower                                                 |
| unpickle             | 14.8 us                                                      | 15.6 us: 1.05x slower                                                |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.96 ms: 1.04x slower                                                |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.20 ms: 1.09x faster                                                |
| django_template | 38.2 ms                                                      | 43.2 ms: 1.13x slower                                                |
| Geometric mean  | (ref)                                                        | 1.02x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 310 ms: 1.39x faster                                                 |
| async_tree_memoization_tg  | 540 ms                                                       | 391 ms: 1.38x faster                                                 |
| async_tree_none            | 452 ms                                                       | 327 ms: 1.38x faster                                                 |
| async_tree_memoization     | 544 ms                                                       | 406 ms: 1.34x faster                                                 |
| async_tree_io_tg           | 1.05 sec                                                     | 792 ms: 1.33x faster                                                 |
| deepcopy_memo              | 36.8 us                                                      | 27.7 us: 1.33x faster                                                |
| async_tree_io              | 1.04 sec                                                     | 804 ms: 1.30x faster                                                 |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 549 ms: 1.27x faster                                                 |
| deepcopy                   | 368 us                                                       | 299 us: 1.23x faster                                                 |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 580 ms: 1.20x faster                                                 |
| pathlib                    | 18.9 ms                                                      | 15.8 ms: 1.20x faster                                                |
| comprehensions             | 21.9 us                                                      | 18.8 us: 1.17x faster                                                |
| deepcopy_reduce            | 3.37 us                                                      | 2.96 us: 1.14x faster                                                |
| crypto_pyaes               | 80.3 ms                                                      | 70.7 ms: 1.14x faster                                                |
| xml_etree_generate         | 86.1 ms                                                      | 78.0 ms: 1.10x faster                                                |
| spectral_norm              | 91.6 ms                                                      | 83.3 ms: 1.10x faster                                                |
| mako                       | 10.0 ms                                                      | 9.20 ms: 1.09x faster                                                |
| coroutines                 | 23.0 ms                                                      | 21.2 ms: 1.08x faster                                                |
| pprint_safe_repr           | 807 ms                                                       | 755 ms: 1.07x faster                                                 |
| scimark_fft                | 301 ms                                                       | 283 ms: 1.06x faster                                                 |
| pidigits                   | 265 ms                                                       | 250 ms: 1.06x faster                                                 |
| pickle_dict                | 32.5 us                                                      | 30.8 us: 1.06x faster                                                |
| pickle_list                | 4.43 us                                                      | 4.20 us: 1.05x faster                                                |
| pprint_pformat             | 1.65 sec                                                     | 1.58 sec: 1.05x faster                                               |
| xml_etree_iterparse        | 103 ms                                                       | 98.4 ms: 1.05x faster                                                |
| nbody                      | 88.0 ms                                                      | 84.2 ms: 1.04x faster                                                |
| logging_format             | 7.48 us                                                      | 7.18 us: 1.04x faster                                                |
| regex_effbot               | 3.57 ms                                                      | 3.43 ms: 1.04x faster                                                |
| xml_etree_process          | 58.4 ms                                                      | 56.2 ms: 1.04x faster                                                |
| richards                   | 45.7 ms                                                      | 44.2 ms: 1.04x faster                                                |
| xml_etree_parse            | 144 ms                                                       | 140 ms: 1.03x faster                                                 |
| asyncio_tcp                | 378 ms                                                       | 369 ms: 1.02x faster                                                 |
| json_loads                 | 24.4 us                                                      | 23.8 us: 1.02x faster                                                |
| sqlite_synth               | 2.77 us                                                      | 2.71 us: 1.02x faster                                                |
| scimark_sor                | 109 ms                                                       | 107 ms: 1.02x faster                                                 |
| dulwich_log                | 65.4 ms                                                      | 64.0 ms: 1.02x faster                                                |
| scimark_lu                 | 98.8 ms                                                      | 96.9 ms: 1.02x faster                                                |
| pickle                     | 10.5 us                                                      | 10.3 us: 1.02x faster                                                |
| async_generators           | 390 ms                                                       | 383 ms: 1.02x faster                                                 |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.14 ms: 1.02x faster                                                |
| logging_simple             | 6.71 us                                                      | 6.61 us: 1.01x faster                                                |
| richards_super             | 51.3 ms                                                      | 50.6 ms: 1.01x faster                                                |
| float                      | 76.6 ms                                                      | 75.8 ms: 1.01x faster                                                |
| deltablue                  | 3.24 ms                                                      | 3.21 ms: 1.01x faster                                                |
| scimark_monte_carlo        | 69.0 ms                                                      | 68.7 ms: 1.00x faster                                                |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.00x faster                                               |
| mdp                        | 2.57 sec                                                     | 2.56 sec: 1.00x faster                                               |
| tomli_loads                | 2.16 sec                                                     | 2.17 sec: 1.01x slower                                               |
| json                       | 5.12 ms                                                      | 5.20 ms: 1.02x slower                                                |
| fannkuch                   | 350 ms                                                       | 356 ms: 1.02x slower                                                 |
| unpickle_list              | 4.66 us                                                      | 4.76 us: 1.02x slower                                                |
| json_dumps                 | 10.2 ms                                                      | 10.5 ms: 1.02x slower                                                |
| go                         | 150 ms                                                       | 154 ms: 1.03x slower                                                 |
| unpickle_pure_python       | 210 us                                                       | 215 us: 1.03x slower                                                 |
| regex_dna                  | 239 ms                                                       | 245 ms: 1.03x slower                                                 |
| pyflate                    | 439 ms                                                       | 451 ms: 1.03x slower                                                 |
| pickle_pure_python         | 318 us                                                       | 329 us: 1.03x slower                                                 |
| meteor_contest             | 128 ms                                                       | 133 ms: 1.04x slower                                                 |
| python_startup_no_site     | 8.64 ms                                                      | 8.96 ms: 1.04x slower                                                |
| chaos                      | 64.0 ms                                                      | 66.8 ms: 1.04x slower                                                |
| regex_v8                   | 23.6 ms                                                      | 24.7 ms: 1.05x slower                                                |
| pycparser                  | 1.23 sec                                                     | 1.29 sec: 1.05x slower                                               |
| logging_silent             | 94.4 ns                                                      | 98.9 ns: 1.05x slower                                                |
| unpickle                   | 14.8 us                                                      | 15.6 us: 1.05x slower                                                |
| sympy_str                  | 302 ms                                                       | 318 ms: 1.05x slower                                                 |
| generators                 | 37.4 ms                                                      | 39.5 ms: 1.06x slower                                                |
| regex_compile              | 144 ms                                                       | 152 ms: 1.06x slower                                                 |
| sympy_sum                  | 162 ms                                                       | 173 ms: 1.07x slower                                                 |
| raytrace                   | 298 ms                                                       | 322 ms: 1.08x slower                                                 |
| sympy_expand               | 484 ms                                                       | 525 ms: 1.08x slower                                                 |
| sqlglot_parse              | 1.38 ms                                                      | 1.52 ms: 1.11x slower                                                |
| telco                      | 6.96 ms                                                      | 7.71 ms: 1.11x slower                                                |
| docutils                   | 2.87 sec                                                     | 3.19 sec: 1.11x slower                                               |
| 2to3                       | 285 ms                                                       | 317 ms: 1.11x slower                                                 |
| sqlglot_transpile          | 1.78 ms                                                      | 1.98 ms: 1.11x slower                                                |
| nqueens                    | 89.9 ms                                                      | 101 ms: 1.12x slower                                                 |
| sqlglot_normalize          | 116 ms                                                       | 130 ms: 1.13x slower                                                 |
| django_template            | 38.2 ms                                                      | 43.2 ms: 1.13x slower                                                |
| sympy_integrate            | 23.9 ms                                                      | 27.2 ms: 1.14x slower                                                |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                |
| create_gc_cycles           | 1.59 ms                                                      | 1.87 ms: 1.17x slower                                                |
| hexiom                     | 5.96 ms                                                      | 7.06 ms: 1.18x slower                                                |
| sqlglot_optimize           | 57.5 ms                                                      | 68.7 ms: 1.20x slower                                                |
| coverage                   | 66.7 ms                                                      | 80.7 ms: 1.21x slower                                                |
| gc_traversal               | 3.48 ms                                                      | 4.30 ms: 1.23x slower                                                |
| typing_runtime_protocols   | 152 us                                                       | 189 us: 1.24x slower                                                 |
| unpack_sequence            | 53.2 ns                                                      | 88.7 ns: 1.67x slower                                                |
| bench_mp_pool              | 4.76 ms                                                      | 4.58 sec: 962.42x slower                                             |
| Geometric mean             | (ref)                                                        | 1.07x slower                                                         |

Benchmark hidden because not significant (3): bench_thread_pool, asyncio_websockets, tornado_http
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241007-3.14.0a0-aa18ec3-JIT/bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.016x faster
# HPT report

- Reliability score: 62.46% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x