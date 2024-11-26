# Results vs. 3.12.0

- fork: python
- ref: ded105a62b9d78717f8d
- machine: linux-x86_64
- commit hash: ded105a
- commit date: 2024-10-21
- overall geometric mean: 1.011x slower
- HPT reliability: 71.91%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 317 ms: 1.11x slower                                                         |
| docutils       | 2.87 sec                                                     | 3.21 sec: 1.12x slower                                                       |
| tornado_http   | 121 ms                                                       | 123 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                        | 1.08x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 378 ms: 1.43x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 326 ms: 1.32x faster                                                         |
| async_tree_none            | 452 ms                                                       | 343 ms: 1.32x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 417 ms: 1.30x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 846 ms: 1.23x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 568 ms: 1.23x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 874 ms: 1.21x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 581 ms: 1.20x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.28x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 251 ms: 1.05x faster                                                         |
| nbody          | 88.0 ms                                                      | 85.2 ms: 1.03x faster                                                        |
| float          | 76.6 ms                                                      | 79.2 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 147 ms: 1.02x slower                                                         |
| regex_dna      | 239 ms                                                       | 244 ms: 1.02x slower                                                         |
| regex_v8       | 23.6 ms                                                      | 25.6 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                 |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 82.3 ms: 1.05x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 99.6 ms: 1.03x faster                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.09 sec: 1.03x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 141 ms: 1.02x faster                                                         |
| xml_etree_process    | 58.4 ms                                                      | 59.0 ms: 1.01x slower                                                        |
| json_loads           | 24.4 us                                                      | 24.8 us: 1.02x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 217 us: 1.04x slower                                                         |
| pickle_pure_python   | 318 us                                                       | 337 us: 1.06x slower                                                         |
| json_dumps           | 10.2 ms                                                      | 11.0 ms: 1.08x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.99 ms: 1.04x slower                                                        |
| python_startup         | 11.6 ms                                                      | 14.8 ms: 1.27x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.15x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.48 ms: 1.06x faster                                                        |
| django_template | 38.2 ms                                                      | 44.8 ms: 1.17x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.05x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 378 ms: 1.43x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 326 ms: 1.32x faster                                                         |
| async_tree_none            | 452 ms                                                       | 343 ms: 1.32x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 417 ms: 1.30x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 846 ms: 1.23x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 568 ms: 1.23x faster                                                         |
| deepcopy_memo              | 36.8 us                                                      | 30.0 us: 1.23x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 874 ms: 1.21x faster                                                         |
| deepcopy                   | 368 us                                                       | 307 us: 1.20x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 581 ms: 1.20x faster                                                         |
| pathlib                    | 18.9 ms                                                      | 16.0 ms: 1.18x faster                                                        |
| comprehensions             | 21.9 us                                                      | 18.7 us: 1.18x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 72.8 ms: 1.10x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 3.07 us: 1.10x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 21.1 ms: 1.09x faster                                                        |
| mako                       | 10.0 ms                                                      | 9.48 ms: 1.06x faster                                                        |
| pidigits                   | 265 ms                                                       | 251 ms: 1.05x faster                                                         |
| xml_etree_generate         | 86.1 ms                                                      | 82.3 ms: 1.05x faster                                                        |
| scimark_fft                | 301 ms                                                       | 288 ms: 1.05x faster                                                         |
| dulwich_log                | 65.4 ms                                                      | 63.1 ms: 1.04x faster                                                        |
| scimark_sor                | 109 ms                                                       | 105 ms: 1.03x faster                                                         |
| xml_etree_iterparse        | 103 ms                                                       | 99.6 ms: 1.03x faster                                                        |
| nbody                      | 88.0 ms                                                      | 85.2 ms: 1.03x faster                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.09 sec: 1.03x faster                                                       |
| logging_silent             | 94.4 ns                                                      | 92.0 ns: 1.03x faster                                                        |
| pprint_safe_repr           | 807 ms                                                       | 788 ms: 1.03x faster                                                         |
| scimark_lu                 | 98.8 ms                                                      | 96.5 ms: 1.02x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 141 ms: 1.02x faster                                                         |
| async_generators           | 390 ms                                                       | 382 ms: 1.02x faster                                                         |
| pprint_pformat             | 1.65 sec                                                     | 1.62 sec: 1.02x faster                                                       |
| asyncio_websockets         | 387 ms                                                       | 382 ms: 1.01x faster                                                         |
| mdp                        | 2.57 sec                                                     | 2.58 sec: 1.00x slower                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 69.3 ms: 1.00x slower                                                        |
| logging_format             | 7.48 us                                                      | 7.53 us: 1.01x slower                                                        |
| json                       | 5.12 ms                                                      | 5.15 ms: 1.01x slower                                                        |
| spectral_norm              | 91.6 ms                                                      | 92.5 ms: 1.01x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 59.0 ms: 1.01x slower                                                        |
| tornado_http               | 121 ms                                                       | 123 ms: 1.01x slower                                                         |
| meteor_contest             | 128 ms                                                       | 130 ms: 1.01x slower                                                         |
| richards                   | 45.7 ms                                                      | 46.4 ms: 1.01x slower                                                        |
| regex_compile              | 144 ms                                                       | 147 ms: 1.02x slower                                                         |
| logging_simple             | 6.71 us                                                      | 6.84 us: 1.02x slower                                                        |
| json_loads                 | 24.4 us                                                      | 24.8 us: 1.02x slower                                                        |
| regex_dna                  | 239 ms                                                       | 244 ms: 1.02x slower                                                         |
| deltablue                  | 3.24 ms                                                      | 3.33 ms: 1.03x slower                                                        |
| float                      | 76.6 ms                                                      | 79.2 ms: 1.03x slower                                                        |
| generators                 | 37.4 ms                                                      | 38.7 ms: 1.03x slower                                                        |
| go                         | 150 ms                                                       | 155 ms: 1.03x slower                                                         |
| unpickle_pure_python       | 210 us                                                       | 217 us: 1.04x slower                                                         |
| pyflate                    | 439 ms                                                       | 456 ms: 1.04x slower                                                         |
| python_startup_no_site     | 8.64 ms                                                      | 8.99 ms: 1.04x slower                                                        |
| raytrace                   | 298 ms                                                       | 310 ms: 1.04x slower                                                         |
| pycparser                  | 1.23 sec                                                     | 1.29 sec: 1.04x slower                                                       |
| fannkuch                   | 350 ms                                                       | 368 ms: 1.05x slower                                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.42 ms: 1.05x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 337 us: 1.06x slower                                                         |
| sympy_str                  | 302 ms                                                       | 321 ms: 1.06x slower                                                         |
| chaos                      | 64.0 ms                                                      | 68.1 ms: 1.06x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 11.0 ms: 1.08x slower                                                        |
| sympy_sum                  | 162 ms                                                       | 175 ms: 1.08x slower                                                         |
| richards_super             | 51.3 ms                                                      | 55.4 ms: 1.08x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 25.6 ms: 1.08x slower                                                        |
| sympy_expand               | 484 ms                                                       | 533 ms: 1.10x slower                                                         |
| sqlglot_parse              | 1.38 ms                                                      | 1.52 ms: 1.10x slower                                                        |
| 2to3                       | 285 ms                                                       | 317 ms: 1.11x slower                                                         |
| telco                      | 6.96 ms                                                      | 7.75 ms: 1.11x slower                                                        |
| docutils                   | 2.87 sec                                                     | 3.21 sec: 1.12x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.99 ms: 1.12x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 102 ms: 1.14x slower                                                         |
| sympy_integrate            | 23.9 ms                                                      | 27.3 ms: 1.14x slower                                                        |
| sqlglot_normalize          | 116 ms                                                       | 135 ms: 1.16x slower                                                         |
| django_template            | 38.2 ms                                                      | 44.8 ms: 1.17x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 7.19 ms: 1.21x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 183 us: 1.21x slower                                                         |
| coverage                   | 66.7 ms                                                      | 81.3 ms: 1.22x slower                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 70.2 ms: 1.22x slower                                                        |
| python_startup             | 11.6 ms                                                      | 14.8 ms: 1.27x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 5.21 ms: 1.50x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.89 ms: 1.82x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 1.74 sec: 366.07x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.09x slower                                                                 |

Benchmark hidden because not significant (2): bench_thread_pool, regex_effbot
Ignored benchmarks (16) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20241021-3.14.0a1+-ded105a-JIT/bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.011x slower
# HPT report

- Reliability score: 71.91% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.10x