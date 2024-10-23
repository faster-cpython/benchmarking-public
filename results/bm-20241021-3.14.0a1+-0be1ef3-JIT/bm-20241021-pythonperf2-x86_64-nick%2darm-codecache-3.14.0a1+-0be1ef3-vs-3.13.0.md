# Results vs. 3.13.0

- fork: nick-arm
- ref: codecache
- machine: linux-x86_64
- commit hash: 0be1ef3
- commit date: 2024-10-21
- overall geometric mean: 1.09x slower
- HPT reliability: 78.38%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 314 ms: 1.08x slower                                                  |
| docutils       | 2.81 sec                                                     | 3.18 sec: 1.13x slower                                                |
| html5lib       | 71.9 ms                                                      | 70.4 ms: 1.02x faster                                                 |
| tornado_http   | 120 ms                                                       | 123 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                        | 1.05x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 374 ms: 1.23x faster                                                  |
| async_tree_memoization     | 452 ms                                                       | 412 ms: 1.10x faster                                                  |
| async_tree_none            | 372 ms                                                       | 341 ms: 1.09x faster                                                  |
| async_tree_none_tg         | 340 ms                                                       | 323 ms: 1.05x faster                                                  |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 577 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 562 ms: 1.02x faster                                                  |
| async_tree_io              | 847 ms                                                       | 835 ms: 1.01x faster                                                  |
| coroutines                 | 21.6 ms                                                      | 22.3 ms: 1.03x slower                                                 |
| async_tree_io_tg           | 819 ms                                                       | 871 ms: 1.06x slower                                                  |
| async_generators           | 359 ms                                                       | 387 ms: 1.08x slower                                                  |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 79.6 ms: 1.03x faster                                                 |
| nbody          | 88.0 ms                                                      | 87.0 ms: 1.01x faster                                                 |
| pidigits       | 253 ms                                                       | 251 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                        | 1.01x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                      | 25.9 ms: 1.01x faster                                                 |
| regex_compile  | 144 ms                                                       | 147 ms: 1.02x slower                                                  |
| regex_dna      | 244 ms                                                       | 257 ms: 1.05x slower                                                  |
| regex_effbot   | 3.37 ms                                                      | 3.73 ms: 1.11x slower                                                 |
| Geometric mean | (ref)                                                        | 1.04x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.11 sec: 1.14x faster                                                |
| xml_etree_generate   | 85.3 ms                                                      | 81.1 ms: 1.05x faster                                                 |
| xml_etree_process    | 60.9 ms                                                      | 58.1 ms: 1.05x faster                                                 |
| json_dumps           | 11.0 ms                                                      | 11.1 ms: 1.01x slower                                                 |
| unpickle_pure_python | 214 us                                                       | 220 us: 1.02x slower                                                  |
| json_loads           | 24.0 us                                                      | 25.0 us: 1.04x slower                                                 |
| pickle_pure_python   | 318 us                                                       | 332 us: 1.04x slower                                                  |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                          |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 8.94 ms                                                      | 9.03 ms: 1.01x slower                                                 |
| python_startup         | 13.3 ms                                                      | 14.9 ms: 1.12x slower                                                 |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 10.4 ms                                                      | 9.62 ms: 1.08x faster                                                 |
| genshi_text     | 26.6 ms                                                      | 27.7 ms: 1.04x slower                                                 |
| genshi_xml      | 57.3 ms                                                      | 61.9 ms: 1.08x slower                                                 |
| django_template | 38.9 ms                                                      | 43.1 ms: 1.11x slower                                                 |
| Geometric mean  | (ref)                                                        | 1.04x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 39.5 us                                                      | 30.3 us: 1.30x faster                                                 |
| deepcopy                   | 397 us                                                       | 314 us: 1.27x faster                                                  |
| async_tree_memoization_tg  | 461 ms                                                       | 374 ms: 1.23x faster                                                  |
| scimark_sor                | 126 ms                                                       | 105 ms: 1.20x faster                                                  |
| richards                   | 52.7 ms                                                      | 45.1 ms: 1.17x faster                                                 |
| deepcopy_reduce            | 3.54 us                                                      | 3.04 us: 1.16x faster                                                 |
| tomli_loads                | 2.41 sec                                                     | 2.11 sec: 1.14x faster                                                |
| telco                      | 8.58 ms                                                      | 7.78 ms: 1.10x faster                                                 |
| scimark_fft                | 314 ms                                                       | 285 ms: 1.10x faster                                                  |
| pathlib                    | 17.4 ms                                                      | 15.8 ms: 1.10x faster                                                 |
| async_tree_memoization     | 452 ms                                                       | 412 ms: 1.10x faster                                                  |
| richards_super             | 59.8 ms                                                      | 54.7 ms: 1.09x faster                                                 |
| async_tree_none            | 372 ms                                                       | 341 ms: 1.09x faster                                                  |
| mako                       | 10.4 ms                                                      | 9.62 ms: 1.08x faster                                                 |
| bpe_tokeniser              | 5.10 sec                                                     | 4.76 sec: 1.07x faster                                                |
| logging_silent             | 97.7 ns                                                      | 92.3 ns: 1.06x faster                                                 |
| pyflate                    | 492 ms                                                       | 466 ms: 1.06x faster                                                  |
| xml_etree_generate         | 85.3 ms                                                      | 81.1 ms: 1.05x faster                                                 |
| async_tree_none_tg         | 340 ms                                                       | 323 ms: 1.05x faster                                                  |
| xml_etree_process          | 60.9 ms                                                      | 58.1 ms: 1.05x faster                                                 |
| coverage                   | 81.1 ms                                                      | 77.8 ms: 1.04x faster                                                 |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 577 ms: 1.04x faster                                                  |
| go                         | 160 ms                                                       | 155 ms: 1.03x faster                                                  |
| dulwich_log                | 65.5 ms                                                      | 63.5 ms: 1.03x faster                                                 |
| pprint_safe_repr           | 812 ms                                                       | 788 ms: 1.03x faster                                                  |
| float                      | 81.9 ms                                                      | 79.6 ms: 1.03x faster                                                 |
| spectral_norm              | 97.4 ms                                                      | 94.8 ms: 1.03x faster                                                 |
| scimark_lu                 | 97.8 ms                                                      | 95.4 ms: 1.03x faster                                                 |
| deltablue                  | 3.41 ms                                                      | 3.34 ms: 1.02x faster                                                 |
| html5lib                   | 71.9 ms                                                      | 70.4 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 562 ms: 1.02x faster                                                  |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.21 ms: 1.02x faster                                                 |
| async_tree_io              | 847 ms                                                       | 835 ms: 1.01x faster                                                  |
| regex_v8                   | 26.2 ms                                                      | 25.9 ms: 1.01x faster                                                 |
| nbody                      | 88.0 ms                                                      | 87.0 ms: 1.01x faster                                                 |
| pidigits                   | 253 ms                                                       | 251 ms: 1.01x faster                                                  |
| crypto_pyaes               | 72.8 ms                                                      | 73.0 ms: 1.00x slower                                                 |
| fannkuch                   | 365 ms                                                       | 367 ms: 1.01x slower                                                  |
| python_startup_no_site     | 8.94 ms                                                      | 9.03 ms: 1.01x slower                                                 |
| json_dumps                 | 11.0 ms                                                      | 11.1 ms: 1.01x slower                                                 |
| pycparser                  | 1.26 sec                                                     | 1.27 sec: 1.01x slower                                                |
| mdp                        | 2.52 sec                                                     | 2.57 sec: 1.02x slower                                                |
| regex_compile              | 144 ms                                                       | 147 ms: 1.02x slower                                                  |
| logging_format             | 7.07 us                                                      | 7.23 us: 1.02x slower                                                 |
| thrift                     | 877 us                                                       | 897 us: 1.02x slower                                                  |
| unpickle_pure_python       | 214 us                                                       | 220 us: 1.02x slower                                                  |
| tornado_http               | 120 ms                                                       | 123 ms: 1.03x slower                                                  |
| meteor_contest             | 128 ms                                                       | 132 ms: 1.03x slower                                                  |
| coroutines                 | 21.6 ms                                                      | 22.3 ms: 1.03x slower                                                 |
| json_loads                 | 24.0 us                                                      | 25.0 us: 1.04x slower                                                 |
| genshi_text                | 26.6 ms                                                      | 27.7 ms: 1.04x slower                                                 |
| pickle_pure_python         | 318 us                                                       | 332 us: 1.04x slower                                                  |
| bench_thread_pool          | 901 us                                                       | 940 us: 1.04x slower                                                  |
| sympy_expand               | 505 ms                                                       | 527 ms: 1.04x slower                                                  |
| typing_runtime_protocols   | 174 us                                                       | 183 us: 1.05x slower                                                  |
| regex_dna                  | 244 ms                                                       | 257 ms: 1.05x slower                                                  |
| logging_simple             | 6.40 us                                                      | 6.75 us: 1.06x slower                                                 |
| scimark_monte_carlo        | 64.9 ms                                                      | 68.8 ms: 1.06x slower                                                 |
| async_tree_io_tg           | 819 ms                                                       | 871 ms: 1.06x slower                                                  |
| sympy_str                  | 296 ms                                                       | 317 ms: 1.07x slower                                                  |
| async_generators           | 359 ms                                                       | 387 ms: 1.08x slower                                                  |
| genshi_xml                 | 57.3 ms                                                      | 61.9 ms: 1.08x slower                                                 |
| 2to3                       | 291 ms                                                       | 314 ms: 1.08x slower                                                  |
| sqlglot_parse              | 1.38 ms                                                      | 1.50 ms: 1.08x slower                                                 |
| comprehensions             | 17.3 us                                                      | 18.8 us: 1.09x slower                                                 |
| raytrace                   | 289 ms                                                       | 316 ms: 1.09x slower                                                  |
| sqlglot_transpile          | 1.78 ms                                                      | 1.96 ms: 1.10x slower                                                 |
| regex_effbot               | 3.37 ms                                                      | 3.73 ms: 1.11x slower                                                 |
| django_template            | 38.9 ms                                                      | 43.1 ms: 1.11x slower                                                 |
| chaos                      | 61.7 ms                                                      | 68.7 ms: 1.11x slower                                                 |
| sqlglot_normalize          | 118 ms                                                       | 133 ms: 1.12x slower                                                  |
| python_startup             | 13.3 ms                                                      | 14.9 ms: 1.12x slower                                                 |
| sympy_sum                  | 154 ms                                                       | 173 ms: 1.13x slower                                                  |
| docutils                   | 2.81 sec                                                     | 3.18 sec: 1.13x slower                                                |
| hexiom                     | 6.33 ms                                                      | 7.21 ms: 1.14x slower                                                 |
| sqlglot_optimize           | 59.7 ms                                                      | 68.8 ms: 1.15x slower                                                 |
| nqueens                    | 88.2 ms                                                      | 102 ms: 1.15x slower                                                  |
| generators                 | 33.5 ms                                                      | 38.7 ms: 1.16x slower                                                 |
| sympy_integrate            | 23.3 ms                                                      | 27.2 ms: 1.16x slower                                                 |
| pylint                     | 346 ms                                                       | 415 ms: 1.20x slower                                                  |
| gc_traversal               | 4.11 ms                                                      | 5.81 ms: 1.41x slower                                                 |
| create_gc_cycles           | 1.76 ms                                                      | 2.90 ms: 1.65x slower                                                 |
| bench_mp_pool              | 4.65 ms                                                      | 3.17 sec: 681.02x slower                                              |
| Geometric mean             | (ref)                                                        | 1.09x slower                                                          |

Benchmark hidden because not significant (5): pprint_pformat, json, asyncio_websockets, xml_etree_iterparse, xml_etree_parse
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20241021-3.14.0a1+-0be1ef3-JIT/bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3.json: sphinx

# HPT report

- Reliability score: 78.38% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.21x