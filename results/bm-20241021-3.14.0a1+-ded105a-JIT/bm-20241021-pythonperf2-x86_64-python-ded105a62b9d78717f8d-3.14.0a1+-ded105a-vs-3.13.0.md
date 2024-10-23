# Results vs. 3.13.0

- fork: python
- ref: ded105a62b9d78717f8d
- machine: linux-x86_64
- commit hash: ded105a
- commit date: 2024-10-21
- overall geometric mean: 1.09x slower
- HPT reliability: 62.76%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 315 ms: 1.08x slower                                                         |
| docutils       | 2.81 sec                                                     | 3.20 sec: 1.14x slower                                                       |
| html5lib       | 71.9 ms                                                      | 71.1 ms: 1.01x faster                                                        |
| tornado_http   | 120 ms                                                       | 124 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 374 ms: 1.23x faster                                                         |
| async_tree_memoization     | 452 ms                                                       | 411 ms: 1.10x faster                                                         |
| async_tree_none            | 372 ms                                                       | 340 ms: 1.09x faster                                                         |
| async_tree_none_tg         | 340 ms                                                       | 322 ms: 1.05x faster                                                         |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 580 ms: 1.03x faster                                                         |
| async_tree_io              | 847 ms                                                       | 831 ms: 1.02x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 564 ms: 1.02x faster                                                         |
| async_tree_io_tg           | 819 ms                                                       | 864 ms: 1.06x slower                                                         |
| async_generators           | 359 ms                                                       | 388 ms: 1.08x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 84.7 ms: 1.04x faster                                                        |
| float          | 81.9 ms                                                      | 79.5 ms: 1.03x faster                                                        |
| pidigits       | 253 ms                                                       | 251 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                      | 26.0 ms: 1.01x faster                                                        |
| regex_compile  | 144 ms                                                       | 146 ms: 1.01x slower                                                         |
| regex_dna      | 244 ms                                                       | 257 ms: 1.05x slower                                                         |
| regex_effbot   | 3.37 ms                                                      | 3.62 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.07 sec: 1.16x faster                                                       |
| xml_etree_generate   | 85.3 ms                                                      | 80.7 ms: 1.06x faster                                                        |
| xml_etree_process    | 60.9 ms                                                      | 57.8 ms: 1.05x faster                                                        |
| xml_etree_parse      | 145 ms                                                       | 143 ms: 1.01x faster                                                         |
| json_dumps           | 11.0 ms                                                      | 11.1 ms: 1.01x slower                                                        |
| unpickle_pure_python | 214 us                                                       | 220 us: 1.02x slower                                                         |
| json_loads           | 24.0 us                                                      | 24.7 us: 1.03x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 332 us: 1.04x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                 |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.94 ms                                                      | 9.00 ms: 1.01x slower                                                        |
| python_startup         | 13.3 ms                                                      | 14.9 ms: 1.12x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                      | 9.58 ms: 1.09x faster                                                        |
| genshi_xml      | 57.3 ms                                                      | 62.4 ms: 1.09x slower                                                        |
| genshi_text     | 26.6 ms                                                      | 29.0 ms: 1.09x slower                                                        |
| django_template | 38.9 ms                                                      | 43.7 ms: 1.12x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.05x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy_memo              | 39.5 us                                                      | 30.5 us: 1.29x faster                                                        |
| deepcopy                   | 397 us                                                       | 313 us: 1.27x faster                                                         |
| async_tree_memoization_tg  | 461 ms                                                       | 374 ms: 1.23x faster                                                         |
| scimark_sor                | 126 ms                                                       | 103 ms: 1.22x faster                                                         |
| deepcopy_reduce            | 3.54 us                                                      | 3.03 us: 1.17x faster                                                        |
| richards                   | 52.7 ms                                                      | 45.2 ms: 1.17x faster                                                        |
| tomli_loads                | 2.41 sec                                                     | 2.07 sec: 1.16x faster                                                       |
| richards_super             | 59.8 ms                                                      | 52.9 ms: 1.13x faster                                                        |
| telco                      | 8.58 ms                                                      | 7.75 ms: 1.11x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 411 ms: 1.10x faster                                                         |
| pathlib                    | 17.4 ms                                                      | 15.9 ms: 1.09x faster                                                        |
| scimark_fft                | 314 ms                                                       | 287 ms: 1.09x faster                                                         |
| async_tree_none            | 372 ms                                                       | 340 ms: 1.09x faster                                                         |
| mako                       | 10.4 ms                                                      | 9.58 ms: 1.09x faster                                                        |
| bpe_tokeniser              | 5.10 sec                                                     | 4.69 sec: 1.09x faster                                                       |
| logging_silent             | 97.7 ns                                                      | 91.6 ns: 1.07x faster                                                        |
| go                         | 160 ms                                                       | 151 ms: 1.06x faster                                                         |
| xml_etree_generate         | 85.3 ms                                                      | 80.7 ms: 1.06x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 322 ms: 1.05x faster                                                         |
| xml_etree_process          | 60.9 ms                                                      | 57.8 ms: 1.05x faster                                                        |
| dulwich_log                | 65.5 ms                                                      | 62.9 ms: 1.04x faster                                                        |
| nbody                      | 88.0 ms                                                      | 84.7 ms: 1.04x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 93.8 ms: 1.04x faster                                                        |
| pyflate                    | 492 ms                                                       | 475 ms: 1.03x faster                                                         |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 580 ms: 1.03x faster                                                         |
| deltablue                  | 3.41 ms                                                      | 3.30 ms: 1.03x faster                                                        |
| float                      | 81.9 ms                                                      | 79.5 ms: 1.03x faster                                                        |
| scimark_lu                 | 97.8 ms                                                      | 95.3 ms: 1.03x faster                                                        |
| pprint_safe_repr           | 812 ms                                                       | 792 ms: 1.03x faster                                                         |
| pprint_pformat             | 1.65 sec                                                     | 1.61 sec: 1.02x faster                                                       |
| async_tree_io              | 847 ms                                                       | 831 ms: 1.02x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 564 ms: 1.02x faster                                                         |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.22 ms: 1.02x faster                                                        |
| xml_etree_parse            | 145 ms                                                       | 143 ms: 1.01x faster                                                         |
| html5lib                   | 71.9 ms                                                      | 71.1 ms: 1.01x faster                                                        |
| regex_v8                   | 26.2 ms                                                      | 26.0 ms: 1.01x faster                                                        |
| pidigits                   | 253 ms                                                       | 251 ms: 1.01x faster                                                         |
| fannkuch                   | 365 ms                                                       | 366 ms: 1.00x slower                                                         |
| python_startup_no_site     | 8.94 ms                                                      | 9.00 ms: 1.01x slower                                                        |
| regex_compile              | 144 ms                                                       | 146 ms: 1.01x slower                                                         |
| json_dumps                 | 11.0 ms                                                      | 11.1 ms: 1.01x slower                                                        |
| coverage                   | 81.1 ms                                                      | 82.5 ms: 1.02x slower                                                        |
| meteor_contest             | 128 ms                                                       | 131 ms: 1.02x slower                                                         |
| unpickle_pure_python       | 214 us                                                       | 220 us: 1.02x slower                                                         |
| mdp                        | 2.52 sec                                                     | 2.59 sec: 1.03x slower                                                       |
| json_loads                 | 24.0 us                                                      | 24.7 us: 1.03x slower                                                        |
| tornado_http               | 120 ms                                                       | 124 ms: 1.03x slower                                                         |
| thrift                     | 877 us                                                       | 909 us: 1.04x slower                                                         |
| pickle_pure_python         | 318 us                                                       | 332 us: 1.04x slower                                                         |
| sympy_expand               | 505 ms                                                       | 529 ms: 1.05x slower                                                         |
| bench_thread_pool          | 901 us                                                       | 948 us: 1.05x slower                                                         |
| regex_dna                  | 244 ms                                                       | 257 ms: 1.05x slower                                                         |
| async_tree_io_tg           | 819 ms                                                       | 864 ms: 1.06x slower                                                         |
| typing_runtime_protocols   | 174 us                                                       | 184 us: 1.06x slower                                                         |
| regex_effbot               | 3.37 ms                                                      | 3.62 ms: 1.08x slower                                                        |
| sympy_str                  | 296 ms                                                       | 318 ms: 1.08x slower                                                         |
| async_generators           | 359 ms                                                       | 388 ms: 1.08x slower                                                         |
| comprehensions             | 17.3 us                                                      | 18.7 us: 1.08x slower                                                        |
| 2to3                       | 291 ms                                                       | 315 ms: 1.08x slower                                                         |
| scimark_monte_carlo        | 64.9 ms                                                      | 70.4 ms: 1.08x slower                                                        |
| genshi_xml                 | 57.3 ms                                                      | 62.4 ms: 1.09x slower                                                        |
| genshi_text                | 26.6 ms                                                      | 29.0 ms: 1.09x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.52 ms: 1.10x slower                                                        |
| chaos                      | 61.7 ms                                                      | 68.0 ms: 1.10x slower                                                        |
| raytrace                   | 289 ms                                                       | 321 ms: 1.11x slower                                                         |
| sqlglot_transpile          | 1.78 ms                                                      | 1.99 ms: 1.12x slower                                                        |
| python_startup             | 13.3 ms                                                      | 14.9 ms: 1.12x slower                                                        |
| django_template            | 38.9 ms                                                      | 43.7 ms: 1.12x slower                                                        |
| sympy_sum                  | 154 ms                                                       | 174 ms: 1.13x slower                                                         |
| hexiom                     | 6.33 ms                                                      | 7.19 ms: 1.14x slower                                                        |
| docutils                   | 2.81 sec                                                     | 3.20 sec: 1.14x slower                                                       |
| sqlglot_normalize          | 118 ms                                                       | 135 ms: 1.14x slower                                                         |
| generators                 | 33.5 ms                                                      | 38.6 ms: 1.15x slower                                                        |
| nqueens                    | 88.2 ms                                                      | 102 ms: 1.16x slower                                                         |
| sqlglot_optimize           | 59.7 ms                                                      | 69.4 ms: 1.16x slower                                                        |
| sympy_integrate            | 23.3 ms                                                      | 27.2 ms: 1.17x slower                                                        |
| pylint                     | 346 ms                                                       | 420 ms: 1.21x slower                                                         |
| gc_traversal               | 4.11 ms                                                      | 5.20 ms: 1.27x slower                                                        |
| create_gc_cycles           | 1.76 ms                                                      | 2.92 ms: 1.66x slower                                                        |
| bench_mp_pool              | 4.65 ms                                                      | 2.28 sec: 490.83x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.09x slower                                                                 |

Benchmark hidden because not significant (7): json, xml_etree_iterparse, crypto_pyaes, asyncio_websockets, logging_format, pycparser, logging_simple
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20241021-3.14.0a1+-ded105a-JIT/bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a.json: sphinx

# HPT report

- Reliability score: 62.76% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.19x