# Results vs. 3.13.0

- fork: python
- ref: 759a54d28ffe7eac8c23
- machine: linux-x86_64
- commit hash: 759a54d
- commit date: 2024-10-22
- overall geometric mean: 1.09x slower
- HPT reliability: 90.36%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 314 ms: 1.08x slower                                                         |
| docutils       | 2.81 sec                                                     | 3.22 sec: 1.15x slower                                                       |
| html5lib       | 71.9 ms                                                      | 71.0 ms: 1.01x faster                                                        |
| tornado_http   | 120 ms                                                       | 124 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 377 ms: 1.22x faster                                                         |
| async_tree_memoization     | 452 ms                                                       | 412 ms: 1.10x faster                                                         |
| async_tree_none            | 372 ms                                                       | 342 ms: 1.09x faster                                                         |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 576 ms: 1.04x faster                                                         |
| async_tree_none_tg         | 340 ms                                                       | 328 ms: 1.04x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 564 ms: 1.02x faster                                                         |
| async_tree_io_tg           | 819 ms                                                       | 870 ms: 1.06x slower                                                         |
| async_generators           | 359 ms                                                       | 390 ms: 1.09x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                 |

Benchmark hidden because not significant (2): async_tree_io, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 79.4 ms: 1.03x faster                                                        |
| nbody          | 88.0 ms                                                      | 85.6 ms: 1.03x faster                                                        |
| pidigits       | 253 ms                                                       | 251 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                      | 25.5 ms: 1.03x faster                                                        |
| regex_dna      | 244 ms                                                       | 242 ms: 1.01x faster                                                         |
| regex_compile  | 144 ms                                                       | 147 ms: 1.02x slower                                                         |
| regex_effbot   | 3.37 ms                                                      | 3.65 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.10 sec: 1.14x faster                                                       |
| xml_etree_generate   | 85.3 ms                                                      | 84.5 ms: 1.01x faster                                                        |
| xml_etree_process    | 60.9 ms                                                      | 60.3 ms: 1.01x faster                                                        |
| json_dumps           | 11.0 ms                                                      | 11.0 ms: 1.00x slower                                                        |
| xml_etree_iterparse  | 100 ms                                                       | 101 ms: 1.00x slower                                                         |
| xml_etree_parse      | 145 ms                                                       | 147 ms: 1.02x slower                                                         |
| unpickle_pure_python | 214 us                                                       | 220 us: 1.03x slower                                                         |
| json_loads           | 24.0 us                                                      | 25.0 us: 1.04x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 333 us: 1.05x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.94 ms                                                      | 9.05 ms: 1.01x slower                                                        |
| python_startup         | 13.3 ms                                                      | 14.9 ms: 1.12x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                      | 9.42 ms: 1.11x faster                                                        |
| genshi_xml      | 57.3 ms                                                      | 63.6 ms: 1.11x slower                                                        |
| django_template | 38.9 ms                                                      | 43.4 ms: 1.12x slower                                                        |
| genshi_text     | 26.6 ms                                                      | 30.2 ms: 1.13x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.06x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy_memo              | 39.5 us                                                      | 30.0 us: 1.32x faster                                                        |
| deepcopy                   | 397 us                                                       | 309 us: 1.28x faster                                                         |
| async_tree_memoization_tg  | 461 ms                                                       | 377 ms: 1.22x faster                                                         |
| scimark_sor                | 126 ms                                                       | 106 ms: 1.18x faster                                                         |
| richards_super             | 59.8 ms                                                      | 51.0 ms: 1.17x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 3.03 us: 1.17x faster                                                        |
| richards                   | 52.7 ms                                                      | 46.1 ms: 1.14x faster                                                        |
| tomli_loads                | 2.41 sec                                                     | 2.10 sec: 1.14x faster                                                       |
| telco                      | 8.58 ms                                                      | 7.75 ms: 1.11x faster                                                        |
| mako                       | 10.4 ms                                                      | 9.42 ms: 1.11x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 412 ms: 1.10x faster                                                         |
| scimark_fft                | 314 ms                                                       | 287 ms: 1.10x faster                                                         |
| pyflate                    | 492 ms                                                       | 452 ms: 1.09x faster                                                         |
| async_tree_none            | 372 ms                                                       | 342 ms: 1.09x faster                                                         |
| pathlib                    | 17.4 ms                                                      | 16.1 ms: 1.08x faster                                                        |
| bpe_tokeniser              | 5.10 sec                                                     | 4.77 sec: 1.07x faster                                                       |
| go                         | 160 ms                                                       | 154 ms: 1.04x faster                                                         |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 576 ms: 1.04x faster                                                         |
| dulwich_log                | 65.5 ms                                                      | 63.1 ms: 1.04x faster                                                        |
| deltablue                  | 3.41 ms                                                      | 3.29 ms: 1.04x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 328 ms: 1.04x faster                                                         |
| float                      | 81.9 ms                                                      | 79.4 ms: 1.03x faster                                                        |
| nbody                      | 88.0 ms                                                      | 85.6 ms: 1.03x faster                                                        |
| regex_v8                   | 26.2 ms                                                      | 25.5 ms: 1.03x faster                                                        |
| pprint_safe_repr           | 812 ms                                                       | 794 ms: 1.02x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 564 ms: 1.02x faster                                                         |
| spectral_norm              | 97.4 ms                                                      | 95.7 ms: 1.02x faster                                                        |
| html5lib                   | 71.9 ms                                                      | 71.0 ms: 1.01x faster                                                        |
| xml_etree_generate         | 85.3 ms                                                      | 84.5 ms: 1.01x faster                                                        |
| xml_etree_process          | 60.9 ms                                                      | 60.3 ms: 1.01x faster                                                        |
| regex_dna                  | 244 ms                                                       | 242 ms: 1.01x faster                                                         |
| pidigits                   | 253 ms                                                       | 251 ms: 1.01x faster                                                         |
| scimark_lu                 | 97.8 ms                                                      | 97.3 ms: 1.01x faster                                                        |
| json_dumps                 | 11.0 ms                                                      | 11.0 ms: 1.00x slower                                                        |
| xml_etree_iterparse        | 100 ms                                                       | 101 ms: 1.00x slower                                                         |
| logging_silent             | 97.7 ns                                                      | 98.2 ns: 1.01x slower                                                        |
| pycparser                  | 1.26 sec                                                     | 1.27 sec: 1.01x slower                                                       |
| python_startup_no_site     | 8.94 ms                                                      | 9.05 ms: 1.01x slower                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.67 sec: 1.01x slower                                                       |
| regex_compile              | 144 ms                                                       | 147 ms: 1.02x slower                                                         |
| xml_etree_parse            | 145 ms                                                       | 147 ms: 1.02x slower                                                         |
| meteor_contest             | 128 ms                                                       | 131 ms: 1.02x slower                                                         |
| logging_simple             | 6.40 us                                                      | 6.54 us: 1.02x slower                                                        |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.40 ms: 1.03x slower                                                        |
| unpickle_pure_python       | 214 us                                                       | 220 us: 1.03x slower                                                         |
| tornado_http               | 120 ms                                                       | 124 ms: 1.03x slower                                                         |
| typing_runtime_protocols   | 174 us                                                       | 181 us: 1.04x slower                                                         |
| fannkuch                   | 365 ms                                                       | 380 ms: 1.04x slower                                                         |
| json_loads                 | 24.0 us                                                      | 25.0 us: 1.04x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 333 us: 1.05x slower                                                         |
| mdp                        | 2.52 sec                                                     | 2.66 sec: 1.05x slower                                                       |
| bench_thread_pool          | 901 us                                                       | 950 us: 1.05x slower                                                         |
| scimark_monte_carlo        | 64.9 ms                                                      | 68.6 ms: 1.06x slower                                                        |
| sympy_expand               | 505 ms                                                       | 534 ms: 1.06x slower                                                         |
| thrift                     | 877 us                                                       | 928 us: 1.06x slower                                                         |
| async_tree_io_tg           | 819 ms                                                       | 870 ms: 1.06x slower                                                         |
| coverage                   | 81.1 ms                                                      | 86.3 ms: 1.06x slower                                                        |
| 2to3                       | 291 ms                                                       | 314 ms: 1.08x slower                                                         |
| regex_effbot               | 3.37 ms                                                      | 3.65 ms: 1.08x slower                                                        |
| async_generators           | 359 ms                                                       | 390 ms: 1.09x slower                                                         |
| comprehensions             | 17.3 us                                                      | 18.8 us: 1.09x slower                                                        |
| sympy_str                  | 296 ms                                                       | 323 ms: 1.09x slower                                                         |
| sqlglot_parse              | 1.38 ms                                                      | 1.51 ms: 1.09x slower                                                        |
| genshi_xml                 | 57.3 ms                                                      | 63.6 ms: 1.11x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.98 ms: 1.11x slower                                                        |
| django_template            | 38.9 ms                                                      | 43.4 ms: 1.12x slower                                                        |
| python_startup             | 13.3 ms                                                      | 14.9 ms: 1.12x slower                                                        |
| sqlglot_normalize          | 118 ms                                                       | 133 ms: 1.13x slower                                                         |
| chaos                      | 61.7 ms                                                      | 69.5 ms: 1.13x slower                                                        |
| genshi_text                | 26.6 ms                                                      | 30.2 ms: 1.13x slower                                                        |
| hexiom                     | 6.33 ms                                                      | 7.21 ms: 1.14x slower                                                        |
| docutils                   | 2.81 sec                                                     | 3.22 sec: 1.15x slower                                                       |
| sympy_sum                  | 154 ms                                                       | 177 ms: 1.15x slower                                                         |
| raytrace                   | 289 ms                                                       | 336 ms: 1.16x slower                                                         |
| sqlglot_optimize           | 59.7 ms                                                      | 69.6 ms: 1.17x slower                                                        |
| nqueens                    | 88.2 ms                                                      | 103 ms: 1.17x slower                                                         |
| sympy_integrate            | 23.3 ms                                                      | 27.6 ms: 1.18x slower                                                        |
| generators                 | 33.5 ms                                                      | 39.7 ms: 1.19x slower                                                        |
| pylint                     | 346 ms                                                       | 424 ms: 1.22x slower                                                         |
| gc_traversal               | 4.11 ms                                                      | 5.53 ms: 1.34x slower                                                        |
| create_gc_cycles           | 1.76 ms                                                      | 2.89 ms: 1.64x slower                                                        |
| bench_mp_pool              | 4.65 ms                                                      | 2.18 sec: 468.76x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.09x slower                                                                 |

Benchmark hidden because not significant (5): async_tree_io, asyncio_websockets, logging_format, crypto_pyaes, json
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20241022-3.14.0a1+-759a54d-JIT/bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d.json: sphinx

# HPT report

- Reliability score: 90.36% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.19x