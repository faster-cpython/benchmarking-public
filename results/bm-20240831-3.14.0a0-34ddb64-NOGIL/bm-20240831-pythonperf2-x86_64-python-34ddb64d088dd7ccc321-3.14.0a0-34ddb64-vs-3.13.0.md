# Results vs. 3.13.0

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: linux-x86_64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.44x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x slower
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 437 ms: 1.50x slower                                                        |
| docutils       | 2.81 sec                                                     | 3.44 sec: 1.22x slower                                                      |
| html5lib       | 71.9 ms                                                      | 107 ms: 1.49x slower                                                        |
| tornado_http   | 120 ms                                                       | 169 ms: 1.41x slower                                                        |
| Geometric mean | (ref)                                                        | 1.40x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets         | 382 ms                                                       | 385 ms: 1.01x slower                                                        |
| async_tree_memoization_tg  | 461 ms                                                       | 484 ms: 1.05x slower                                                        |
| async_tree_none_tg         | 340 ms                                                       | 373 ms: 1.10x slower                                                        |
| async_tree_io_tg           | 819 ms                                                       | 909 ms: 1.11x slower                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 645 ms: 1.12x slower                                                        |
| async_tree_none            | 372 ms                                                       | 421 ms: 1.13x slower                                                        |
| async_tree_io              | 847 ms                                                       | 963 ms: 1.14x slower                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 686 ms: 1.14x slower                                                        |
| async_tree_memoization     | 452 ms                                                       | 524 ms: 1.16x slower                                                        |
| asyncio_tcp                | 380 ms                                                       | 451 ms: 1.19x slower                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.90 sec: 1.20x slower                                                      |
| coroutines                 | 21.6 ms                                                      | 29.2 ms: 1.35x slower                                                       |
| async_generators           | 359 ms                                                       | 501 ms: 1.39x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.16x slower                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 253 ms                                                       | 250 ms: 1.01x faster                                                        |
| float          | 81.9 ms                                                      | 145 ms: 1.77x slower                                                        |
| nbody          | 88.0 ms                                                      | 195 ms: 2.22x slower                                                        |
| Geometric mean | (ref)                                                        | 1.57x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 244 ms                                                       | 241 ms: 1.01x faster                                                        |
| regex_v8       | 26.2 ms                                                      | 27.3 ms: 1.04x slower                                                       |
| regex_effbot   | 3.37 ms                                                      | 3.54 ms: 1.05x slower                                                       |
| regex_compile  | 144 ms                                                       | 231 ms: 1.60x slower                                                        |
| Geometric mean | (ref)                                                        | 1.15x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 145 ms                                                       | 137 ms: 1.05x faster                                                        |
| xml_etree_iterparse  | 100 ms                                                       | 110 ms: 1.10x slower                                                        |
| json_loads           | 24.0 us                                                      | 29.5 us: 1.23x slower                                                       |
| json_dumps           | 11.0 ms                                                      | 14.2 ms: 1.30x slower                                                       |
| xml_etree_generate   | 85.3 ms                                                      | 118 ms: 1.38x slower                                                        |
| tomli_loads          | 2.41 sec                                                     | 3.38 sec: 1.40x slower                                                      |
| xml_etree_process    | 60.9 ms                                                      | 96.7 ms: 1.59x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 593 us: 1.86x slower                                                        |
| unpickle_pure_python | 214 us                                                       | 417 us: 1.94x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.38x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 17.4 ms: 1.31x slower                                                       |
| python_startup_no_site | 8.94 ms                                                      | 12.0 ms: 1.34x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.32x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 57.3 ms                                                      | 83.9 ms: 1.46x slower                                                       |
| genshi_text     | 26.6 ms                                                      | 43.6 ms: 1.64x slower                                                       |
| django_template | 38.9 ms                                                      | 68.9 ms: 1.77x slower                                                       |
| mako            | 10.4 ms                                                      | 21.9 ms: 2.10x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.73x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| gc_traversal               | 4.11 ms                                                      | 2.99 ms: 1.37x faster                                                       |
| create_gc_cycles           | 1.76 ms                                                      | 1.67 ms: 1.06x faster                                                       |
| xml_etree_parse            | 145 ms                                                       | 137 ms: 1.05x faster                                                        |
| regex_dna                  | 244 ms                                                       | 241 ms: 1.01x faster                                                        |
| pidigits                   | 253 ms                                                       | 250 ms: 1.01x faster                                                        |
| asyncio_websockets         | 382 ms                                                       | 385 ms: 1.01x slower                                                        |
| regex_v8                   | 26.2 ms                                                      | 27.3 ms: 1.04x slower                                                       |
| async_tree_memoization_tg  | 461 ms                                                       | 484 ms: 1.05x slower                                                        |
| regex_effbot               | 3.37 ms                                                      | 3.54 ms: 1.05x slower                                                       |
| bench_mp_pool              | 4.65 ms                                                      | 5.06 ms: 1.09x slower                                                       |
| async_tree_none_tg         | 340 ms                                                       | 373 ms: 1.10x slower                                                        |
| xml_etree_iterparse        | 100 ms                                                       | 110 ms: 1.10x slower                                                        |
| async_tree_io_tg           | 819 ms                                                       | 909 ms: 1.11x slower                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 645 ms: 1.12x slower                                                        |
| async_tree_none            | 372 ms                                                       | 421 ms: 1.13x slower                                                        |
| async_tree_io              | 847 ms                                                       | 963 ms: 1.14x slower                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 686 ms: 1.14x slower                                                        |
| pathlib                    | 17.4 ms                                                      | 19.9 ms: 1.14x slower                                                       |
| deepcopy                   | 397 us                                                       | 455 us: 1.15x slower                                                        |
| async_tree_memoization     | 452 ms                                                       | 524 ms: 1.16x slower                                                        |
| json                       | 5.22 ms                                                      | 6.19 ms: 1.19x slower                                                       |
| asyncio_tcp                | 380 ms                                                       | 451 ms: 1.19x slower                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.90 sec: 1.20x slower                                                      |
| docutils                   | 2.81 sec                                                     | 3.44 sec: 1.22x slower                                                      |
| json_loads                 | 24.0 us                                                      | 29.5 us: 1.23x slower                                                       |
| generators                 | 33.5 ms                                                      | 41.3 ms: 1.23x slower                                                       |
| telco                      | 8.58 ms                                                      | 10.6 ms: 1.24x slower                                                       |
| scimark_fft                | 314 ms                                                       | 399 ms: 1.27x slower                                                        |
| pylint                     | 346 ms                                                       | 441 ms: 1.27x slower                                                        |
| mdp                        | 2.52 sec                                                     | 3.24 sec: 1.29x slower                                                      |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 5.57 ms: 1.30x slower                                                       |
| json_dumps                 | 11.0 ms                                                      | 14.2 ms: 1.30x slower                                                       |
| python_startup             | 13.3 ms                                                      | 17.4 ms: 1.31x slower                                                       |
| bpe_tokeniser              | 5.10 sec                                                     | 6.68 sec: 1.31x slower                                                      |
| python_startup_no_site     | 8.94 ms                                                      | 12.0 ms: 1.34x slower                                                       |
| meteor_contest             | 128 ms                                                       | 172 ms: 1.34x slower                                                        |
| coverage                   | 81.1 ms                                                      | 109 ms: 1.34x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 29.2 ms: 1.35x slower                                                       |
| deepcopy_memo              | 39.5 us                                                      | 53.4 us: 1.35x slower                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 4.83 us: 1.36x slower                                                       |
| sympy_integrate            | 23.3 ms                                                      | 32.1 ms: 1.38x slower                                                       |
| xml_etree_generate         | 85.3 ms                                                      | 118 ms: 1.38x slower                                                        |
| dulwich_log                | 65.5 ms                                                      | 90.5 ms: 1.38x slower                                                       |
| async_generators           | 359 ms                                                       | 501 ms: 1.39x slower                                                        |
| tomli_loads                | 2.41 sec                                                     | 3.38 sec: 1.40x slower                                                      |
| pycparser                  | 1.26 sec                                                     | 1.77 sec: 1.41x slower                                                      |
| tornado_http               | 120 ms                                                       | 169 ms: 1.41x slower                                                        |
| genshi_xml                 | 57.3 ms                                                      | 83.9 ms: 1.46x slower                                                       |
| html5lib                   | 71.9 ms                                                      | 107 ms: 1.49x slower                                                        |
| nqueens                    | 88.2 ms                                                      | 132 ms: 1.49x slower                                                        |
| 2to3                       | 291 ms                                                       | 437 ms: 1.50x slower                                                        |
| sympy_str                  | 296 ms                                                       | 455 ms: 1.54x slower                                                        |
| thrift                     | 877 us                                                       | 1.37 ms: 1.56x slower                                                       |
| fannkuch                   | 365 ms                                                       | 571 ms: 1.57x slower                                                        |
| pyflate                    | 492 ms                                                       | 771 ms: 1.57x slower                                                        |
| richards                   | 52.7 ms                                                      | 83.2 ms: 1.58x slower                                                       |
| xml_etree_process          | 60.9 ms                                                      | 96.7 ms: 1.59x slower                                                       |
| regex_compile              | 144 ms                                                       | 231 ms: 1.60x slower                                                        |
| typing_runtime_protocols   | 174 us                                                       | 279 us: 1.61x slower                                                        |
| sqlglot_optimize           | 59.7 ms                                                      | 95.9 ms: 1.61x slower                                                       |
| sqlglot_normalize          | 118 ms                                                       | 192 ms: 1.62x slower                                                        |
| sympy_expand               | 505 ms                                                       | 827 ms: 1.64x slower                                                        |
| genshi_text                | 26.6 ms                                                      | 43.6 ms: 1.64x slower                                                       |
| crypto_pyaes               | 72.8 ms                                                      | 120 ms: 1.65x slower                                                        |
| richards_super             | 59.8 ms                                                      | 101 ms: 1.69x slower                                                        |
| sympy_sum                  | 154 ms                                                       | 264 ms: 1.71x slower                                                        |
| comprehensions             | 17.3 us                                                      | 29.7 us: 1.72x slower                                                       |
| spectral_norm              | 97.4 ms                                                      | 170 ms: 1.75x slower                                                        |
| logging_format             | 7.07 us                                                      | 12.5 us: 1.76x slower                                                       |
| float                      | 81.9 ms                                                      | 145 ms: 1.77x slower                                                        |
| django_template            | 38.9 ms                                                      | 68.9 ms: 1.77x slower                                                       |
| pprint_safe_repr           | 812 ms                                                       | 1.44 sec: 1.78x slower                                                      |
| pprint_pformat             | 1.65 sec                                                     | 2.99 sec: 1.81x slower                                                      |
| logging_simple             | 6.40 us                                                      | 11.6 us: 1.81x slower                                                       |
| go                         | 160 ms                                                       | 291 ms: 1.81x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 593 us: 1.86x slower                                                        |
| hexiom                     | 6.33 ms                                                      | 11.9 ms: 1.87x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 3.39 ms: 1.91x slower                                                       |
| bench_thread_pool          | 901 us                                                       | 1.73 ms: 1.91x slower                                                       |
| unpickle_pure_python       | 214 us                                                       | 417 us: 1.94x slower                                                        |
| logging_silent             | 97.7 ns                                                      | 191 ns: 1.96x slower                                                        |
| scimark_sor                | 126 ms                                                       | 250 ms: 1.99x slower                                                        |
| chaos                      | 61.7 ms                                                      | 125 ms: 2.03x slower                                                        |
| scimark_monte_carlo        | 64.9 ms                                                      | 134 ms: 2.06x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 2.87 ms: 2.08x slower                                                       |
| mako                       | 10.4 ms                                                      | 21.9 ms: 2.10x slower                                                       |
| raytrace                   | 289 ms                                                       | 611 ms: 2.11x slower                                                        |
| nbody                      | 88.0 ms                                                      | 195 ms: 2.22x slower                                                        |
| scimark_lu                 | 97.8 ms                                                      | 237 ms: 2.42x slower                                                        |
| deltablue                  | 3.41 ms                                                      | 8.35 ms: 2.45x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.44x slower                                                                |
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.34x
- 95% likely to have a slowdown of 1.33x
- 99% likely to have a slowdown of 1.30x

# Memory
- memory change: 1.17x