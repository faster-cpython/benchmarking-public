# Results vs. 3.13.0

- fork: faster-cpython
- ref: load_const_return_re
- machine: linux-x86_64
- commit hash: 031f320
- commit date: 2024-10-23
- overall geometric mean: 1.09x slower
- HPT reliability: 56.38%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 317 ms: 1.09x slower                                                                   |
| docutils       | 2.81 sec                                                     | 3.19 sec: 1.14x slower                                                                 |
| tornado_http   | 120 ms                                                       | 123 ms: 1.03x slower                                                                   |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                           |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 371 ms: 1.24x faster                                                                   |
| async_tree_memoization     | 452 ms                                                       | 409 ms: 1.11x faster                                                                   |
| async_tree_none            | 372 ms                                                       | 337 ms: 1.10x faster                                                                   |
| coroutines                 | 21.6 ms                                                      | 20.4 ms: 1.06x faster                                                                  |
| async_tree_none_tg         | 340 ms                                                       | 321 ms: 1.06x faster                                                                   |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 575 ms: 1.04x faster                                                                   |
| async_tree_io              | 847 ms                                                       | 819 ms: 1.03x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 560 ms: 1.03x faster                                                                   |
| async_tree_io_tg           | 819 ms                                                       | 861 ms: 1.05x slower                                                                   |
| async_generators           | 359 ms                                                       | 380 ms: 1.06x slower                                                                   |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 85.3 ms: 1.03x faster                                                                  |
| float          | 81.9 ms                                                      | 80.7 ms: 1.02x faster                                                                  |
| pidigits       | 253 ms                                                       | 251 ms: 1.01x faster                                                                   |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                      | 24.8 ms: 1.06x faster                                                                  |
| regex_dna      | 244 ms                                                       | 234 ms: 1.04x faster                                                                   |
| regex_compile  | 144 ms                                                       | 147 ms: 1.02x slower                                                                   |
| regex_effbot   | 3.37 ms                                                      | 3.60 ms: 1.07x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.13 sec: 1.13x faster                                                                 |
| xml_etree_process    | 60.9 ms                                                      | 56.9 ms: 1.07x faster                                                                  |
| xml_etree_generate   | 85.3 ms                                                      | 80.0 ms: 1.07x faster                                                                  |
| xml_etree_iterparse  | 100 ms                                                       | 101 ms: 1.01x slower                                                                   |
| xml_etree_parse      | 145 ms                                                       | 147 ms: 1.02x slower                                                                   |
| json_loads           | 24.0 us                                                      | 24.6 us: 1.02x slower                                                                  |
| unpickle_pure_python | 214 us                                                       | 222 us: 1.04x slower                                                                   |
| pickle_pure_python   | 318 us                                                       | 340 us: 1.07x slower                                                                   |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                           |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.94 ms                                                      | 9.11 ms: 1.02x slower                                                                  |
| python_startup         | 13.3 ms                                                      | 15.1 ms: 1.13x slower                                                                  |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                      | 9.44 ms: 1.10x faster                                                                  |
| genshi_text     | 26.6 ms                                                      | 29.9 ms: 1.12x slower                                                                  |
| django_template | 38.9 ms                                                      | 43.8 ms: 1.13x slower                                                                  |
| genshi_xml      | 57.3 ms                                                      | 66.9 ms: 1.17x slower                                                                  |
| Geometric mean  | (ref)                                                        | 1.08x slower                                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| deepcopy_memo              | 39.5 us                                                      | 30.3 us: 1.30x faster                                                                  |
| deepcopy                   | 397 us                                                       | 316 us: 1.26x faster                                                                   |
| async_tree_memoization_tg  | 461 ms                                                       | 371 ms: 1.24x faster                                                                   |
| scimark_sor                | 126 ms                                                       | 104 ms: 1.21x faster                                                                   |
| deepcopy_reduce            | 3.54 us                                                      | 3.04 us: 1.16x faster                                                                  |
| tomli_loads                | 2.41 sec                                                     | 2.13 sec: 1.13x faster                                                                 |
| telco                      | 8.58 ms                                                      | 7.69 ms: 1.12x faster                                                                  |
| async_tree_memoization     | 452 ms                                                       | 409 ms: 1.11x faster                                                                   |
| mako                       | 10.4 ms                                                      | 9.44 ms: 1.10x faster                                                                  |
| async_tree_none            | 372 ms                                                       | 337 ms: 1.10x faster                                                                   |
| richards_super             | 59.8 ms                                                      | 54.6 ms: 1.09x faster                                                                  |
| richards                   | 52.7 ms                                                      | 48.3 ms: 1.09x faster                                                                  |
| scimark_fft                | 314 ms                                                       | 288 ms: 1.09x faster                                                                   |
| pathlib                    | 17.4 ms                                                      | 16.0 ms: 1.09x faster                                                                  |
| pyflate                    | 492 ms                                                       | 456 ms: 1.08x faster                                                                   |
| xml_etree_process          | 60.9 ms                                                      | 56.9 ms: 1.07x faster                                                                  |
| bpe_tokeniser              | 5.10 sec                                                     | 4.77 sec: 1.07x faster                                                                 |
| xml_etree_generate         | 85.3 ms                                                      | 80.0 ms: 1.07x faster                                                                  |
| coroutines                 | 21.6 ms                                                      | 20.4 ms: 1.06x faster                                                                  |
| async_tree_none_tg         | 340 ms                                                       | 321 ms: 1.06x faster                                                                   |
| regex_v8                   | 26.2 ms                                                      | 24.8 ms: 1.06x faster                                                                  |
| spectral_norm              | 97.4 ms                                                      | 93.3 ms: 1.04x faster                                                                  |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 575 ms: 1.04x faster                                                                   |
| regex_dna                  | 244 ms                                                       | 234 ms: 1.04x faster                                                                   |
| deltablue                  | 3.41 ms                                                      | 3.29 ms: 1.04x faster                                                                  |
| pprint_safe_repr           | 812 ms                                                       | 784 ms: 1.03x faster                                                                   |
| async_tree_io              | 847 ms                                                       | 819 ms: 1.03x faster                                                                   |
| nbody                      | 88.0 ms                                                      | 85.3 ms: 1.03x faster                                                                  |
| dulwich_log                | 65.5 ms                                                      | 63.8 ms: 1.03x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 560 ms: 1.03x faster                                                                   |
| coverage                   | 81.1 ms                                                      | 79.3 ms: 1.02x faster                                                                  |
| go                         | 160 ms                                                       | 157 ms: 1.02x faster                                                                   |
| pprint_pformat             | 1.65 sec                                                     | 1.62 sec: 1.02x faster                                                                 |
| float                      | 81.9 ms                                                      | 80.7 ms: 1.02x faster                                                                  |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.25 ms: 1.01x faster                                                                  |
| scimark_lu                 | 97.8 ms                                                      | 97.2 ms: 1.01x faster                                                                  |
| pidigits                   | 253 ms                                                       | 251 ms: 1.01x faster                                                                   |
| crypto_pyaes               | 72.8 ms                                                      | 73.2 ms: 1.01x slower                                                                  |
| thrift                     | 877 us                                                       | 887 us: 1.01x slower                                                                   |
| xml_etree_iterparse        | 100 ms                                                       | 101 ms: 1.01x slower                                                                   |
| meteor_contest             | 128 ms                                                       | 130 ms: 1.01x slower                                                                   |
| logging_format             | 7.07 us                                                      | 7.18 us: 1.02x slower                                                                  |
| xml_etree_parse            | 145 ms                                                       | 147 ms: 1.02x slower                                                                   |
| regex_compile              | 144 ms                                                       | 147 ms: 1.02x slower                                                                   |
| python_startup_no_site     | 8.94 ms                                                      | 9.11 ms: 1.02x slower                                                                  |
| json_loads                 | 24.0 us                                                      | 24.6 us: 1.02x slower                                                                  |
| tornado_http               | 120 ms                                                       | 123 ms: 1.03x slower                                                                   |
| mdp                        | 2.52 sec                                                     | 2.60 sec: 1.03x slower                                                                 |
| fannkuch                   | 365 ms                                                       | 375 ms: 1.03x slower                                                                   |
| pycparser                  | 1.26 sec                                                     | 1.30 sec: 1.03x slower                                                                 |
| unpickle_pure_python       | 214 us                                                       | 222 us: 1.04x slower                                                                   |
| typing_runtime_protocols   | 174 us                                                       | 182 us: 1.04x slower                                                                   |
| logging_simple             | 6.40 us                                                      | 6.69 us: 1.05x slower                                                                  |
| async_tree_io_tg           | 819 ms                                                       | 861 ms: 1.05x slower                                                                   |
| sympy_expand               | 505 ms                                                       | 533 ms: 1.06x slower                                                                   |
| logging_silent             | 97.7 ns                                                      | 103 ns: 1.06x slower                                                                   |
| async_generators           | 359 ms                                                       | 380 ms: 1.06x slower                                                                   |
| bench_thread_pool          | 901 us                                                       | 954 us: 1.06x slower                                                                   |
| pickle_pure_python         | 318 us                                                       | 340 us: 1.07x slower                                                                   |
| regex_effbot               | 3.37 ms                                                      | 3.60 ms: 1.07x slower                                                                  |
| scimark_monte_carlo        | 64.9 ms                                                      | 70.3 ms: 1.08x slower                                                                  |
| sympy_str                  | 296 ms                                                       | 321 ms: 1.09x slower                                                                   |
| 2to3                       | 291 ms                                                       | 317 ms: 1.09x slower                                                                   |
| comprehensions             | 17.3 us                                                      | 18.9 us: 1.10x slower                                                                  |
| sqlglot_parse              | 1.38 ms                                                      | 1.52 ms: 1.10x slower                                                                  |
| chaos                      | 61.7 ms                                                      | 67.7 ms: 1.10x slower                                                                  |
| sqlglot_transpile          | 1.78 ms                                                      | 1.99 ms: 1.12x slower                                                                  |
| raytrace                   | 289 ms                                                       | 323 ms: 1.12x slower                                                                   |
| genshi_text                | 26.6 ms                                                      | 29.9 ms: 1.12x slower                                                                  |
| nqueens                    | 88.2 ms                                                      | 99.5 ms: 1.13x slower                                                                  |
| django_template            | 38.9 ms                                                      | 43.8 ms: 1.13x slower                                                                  |
| python_startup             | 13.3 ms                                                      | 15.1 ms: 1.13x slower                                                                  |
| docutils                   | 2.81 sec                                                     | 3.19 sec: 1.14x slower                                                                 |
| hexiom                     | 6.33 ms                                                      | 7.20 ms: 1.14x slower                                                                  |
| sqlglot_normalize          | 118 ms                                                       | 135 ms: 1.14x slower                                                                   |
| sympy_sum                  | 154 ms                                                       | 175 ms: 1.14x slower                                                                   |
| generators                 | 33.5 ms                                                      | 38.9 ms: 1.16x slower                                                                  |
| genshi_xml                 | 57.3 ms                                                      | 66.9 ms: 1.17x slower                                                                  |
| sqlglot_optimize           | 59.7 ms                                                      | 69.7 ms: 1.17x slower                                                                  |
| sympy_integrate            | 23.3 ms                                                      | 27.3 ms: 1.17x slower                                                                  |
| pylint                     | 346 ms                                                       | 415 ms: 1.20x slower                                                                   |
| gc_traversal               | 4.11 ms                                                      | 5.80 ms: 1.41x slower                                                                  |
| create_gc_cycles           | 1.76 ms                                                      | 2.92 ms: 1.66x slower                                                                  |
| bench_mp_pool              | 4.65 ms                                                      | 2.57 sec: 552.24x slower                                                               |
| Geometric mean             | (ref)                                                        | 1.09x slower                                                                           |

Benchmark hidden because not significant (4): json, html5lib, json_dumps, asyncio_websockets
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20241023-3.14.0a1+-031f320-JIT/bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320.json: sphinx

# HPT report

- Reliability score: 56.38% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.19x