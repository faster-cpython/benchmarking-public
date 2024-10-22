# Results vs. 3.13.0

- fork: python
- ref: a2bec77d25b11f50362a
- machine: linux-x86_64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.44x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x slower
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 433 ms: 1.49x slower                                                        |
| docutils       | 2.81 sec                                                     | 3.49 sec: 1.24x slower                                                      |
| html5lib       | 71.9 ms                                                      | 106 ms: 1.48x slower                                                        |
| tornado_http   | 120 ms                                                       | 163 ms: 1.36x slower                                                        |
| Geometric mean | (ref)                                                        | 1.39x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 478 ms: 1.04x slower                                                        |
| async_tree_none_tg         | 340 ms                                                       | 369 ms: 1.09x slower                                                        |
| async_tree_io_tg           | 819 ms                                                       | 903 ms: 1.10x slower                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 645 ms: 1.12x slower                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.79 sec: 1.13x slower                                                      |
| async_tree_io              | 847 ms                                                       | 968 ms: 1.14x slower                                                        |
| async_tree_none            | 372 ms                                                       | 429 ms: 1.15x slower                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 693 ms: 1.16x slower                                                        |
| asyncio_tcp                | 380 ms                                                       | 452 ms: 1.19x slower                                                        |
| async_tree_memoization     | 452 ms                                                       | 540 ms: 1.19x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 28.8 ms: 1.33x slower                                                       |
| async_generators           | 359 ms                                                       | 497 ms: 1.38x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.15x slower                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 253 ms                                                       | 256 ms: 1.01x slower                                                        |
| float          | 81.9 ms                                                      | 148 ms: 1.81x slower                                                        |
| nbody          | 88.0 ms                                                      | 204 ms: 2.32x slower                                                        |
| Geometric mean | (ref)                                                        | 1.62x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 244 ms                                                       | 234 ms: 1.04x faster                                                        |
| regex_effbot   | 3.37 ms                                                      | 3.33 ms: 1.01x faster                                                       |
| regex_v8       | 26.2 ms                                                      | 28.4 ms: 1.08x slower                                                       |
| regex_compile  | 144 ms                                                       | 231 ms: 1.60x slower                                                        |
| Geometric mean | (ref)                                                        | 1.13x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 145 ms                                                       | 137 ms: 1.06x faster                                                        |
| xml_etree_iterparse  | 100 ms                                                       | 110 ms: 1.10x slower                                                        |
| json_loads           | 24.0 us                                                      | 30.5 us: 1.27x slower                                                       |
| json_dumps           | 11.0 ms                                                      | 14.4 ms: 1.32x slower                                                       |
| xml_etree_generate   | 85.3 ms                                                      | 114 ms: 1.34x slower                                                        |
| tomli_loads          | 2.41 sec                                                     | 3.38 sec: 1.41x slower                                                      |
| xml_etree_process    | 60.9 ms                                                      | 94.4 ms: 1.55x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 589 us: 1.85x slower                                                        |
| unpickle_pure_python | 214 us                                                       | 418 us: 1.95x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.38x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 16.9 ms: 1.27x slower                                                       |
| python_startup_no_site | 8.94 ms                                                      | 11.5 ms: 1.29x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.28x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 57.3 ms                                                      | 83.1 ms: 1.45x slower                                                       |
| genshi_text     | 26.6 ms                                                      | 42.4 ms: 1.59x slower                                                       |
| django_template | 38.9 ms                                                      | 68.2 ms: 1.76x slower                                                       |
| mako            | 10.4 ms                                                      | 22.3 ms: 2.14x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.72x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| gc_traversal               | 4.11 ms                                                      | 3.10 ms: 1.33x faster                                                       |
| xml_etree_parse            | 145 ms                                                       | 137 ms: 1.06x faster                                                        |
| bench_mp_pool              | 4.65 ms                                                      | 4.44 ms: 1.05x faster                                                       |
| regex_dna                  | 244 ms                                                       | 234 ms: 1.04x faster                                                        |
| regex_effbot               | 3.37 ms                                                      | 3.33 ms: 1.01x faster                                                       |
| pidigits                   | 253 ms                                                       | 256 ms: 1.01x slower                                                        |
| async_tree_memoization_tg  | 461 ms                                                       | 478 ms: 1.04x slower                                                        |
| regex_v8                   | 26.2 ms                                                      | 28.4 ms: 1.08x slower                                                       |
| async_tree_none_tg         | 340 ms                                                       | 369 ms: 1.09x slower                                                        |
| async_tree_io_tg           | 819 ms                                                       | 903 ms: 1.10x slower                                                        |
| xml_etree_iterparse        | 100 ms                                                       | 110 ms: 1.10x slower                                                        |
| deepcopy                   | 397 us                                                       | 444 us: 1.12x slower                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 645 ms: 1.12x slower                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.79 sec: 1.13x slower                                                      |
| pathlib                    | 17.4 ms                                                      | 19.8 ms: 1.14x slower                                                       |
| async_tree_io              | 847 ms                                                       | 968 ms: 1.14x slower                                                        |
| async_tree_none            | 372 ms                                                       | 429 ms: 1.15x slower                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 693 ms: 1.16x slower                                                        |
| json                       | 5.22 ms                                                      | 6.18 ms: 1.18x slower                                                       |
| asyncio_tcp                | 380 ms                                                       | 452 ms: 1.19x slower                                                        |
| async_tree_memoization     | 452 ms                                                       | 540 ms: 1.19x slower                                                        |
| telco                      | 8.58 ms                                                      | 10.4 ms: 1.21x slower                                                       |
| pylint                     | 346 ms                                                       | 427 ms: 1.23x slower                                                        |
| docutils                   | 2.81 sec                                                     | 3.49 sec: 1.24x slower                                                      |
| python_startup             | 13.3 ms                                                      | 16.9 ms: 1.27x slower                                                       |
| json_loads                 | 24.0 us                                                      | 30.5 us: 1.27x slower                                                       |
| python_startup_no_site     | 8.94 ms                                                      | 11.5 ms: 1.29x slower                                                       |
| coverage                   | 81.1 ms                                                      | 105 ms: 1.29x slower                                                        |
| deepcopy_memo              | 39.5 us                                                      | 51.0 us: 1.29x slower                                                       |
| mdp                        | 2.52 sec                                                     | 3.29 sec: 1.30x slower                                                      |
| json_dumps                 | 11.0 ms                                                      | 14.4 ms: 1.32x slower                                                       |
| scimark_fft                | 314 ms                                                       | 415 ms: 1.32x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 28.8 ms: 1.33x slower                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 4.73 us: 1.34x slower                                                       |
| xml_etree_generate         | 85.3 ms                                                      | 114 ms: 1.34x slower                                                        |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 5.79 ms: 1.35x slower                                                       |
| meteor_contest             | 128 ms                                                       | 174 ms: 1.35x slower                                                        |
| tornado_http               | 120 ms                                                       | 163 ms: 1.36x slower                                                        |
| generators                 | 33.5 ms                                                      | 45.5 ms: 1.36x slower                                                       |
| bpe_tokeniser              | 5.10 sec                                                     | 6.98 sec: 1.37x slower                                                      |
| dulwich_log                | 65.5 ms                                                      | 90.2 ms: 1.38x slower                                                       |
| sympy_integrate            | 23.3 ms                                                      | 32.2 ms: 1.38x slower                                                       |
| async_generators           | 359 ms                                                       | 497 ms: 1.38x slower                                                        |
| tomli_loads                | 2.41 sec                                                     | 3.38 sec: 1.41x slower                                                      |
| pycparser                  | 1.26 sec                                                     | 1.77 sec: 1.41x slower                                                      |
| genshi_xml                 | 57.3 ms                                                      | 83.1 ms: 1.45x slower                                                       |
| html5lib                   | 71.9 ms                                                      | 106 ms: 1.48x slower                                                        |
| nqueens                    | 88.2 ms                                                      | 131 ms: 1.49x slower                                                        |
| 2to3                       | 291 ms                                                       | 433 ms: 1.49x slower                                                        |
| sympy_str                  | 296 ms                                                       | 455 ms: 1.54x slower                                                        |
| xml_etree_process          | 60.9 ms                                                      | 94.4 ms: 1.55x slower                                                       |
| typing_runtime_protocols   | 174 us                                                       | 271 us: 1.56x slower                                                        |
| pyflate                    | 492 ms                                                       | 774 ms: 1.57x slower                                                        |
| sqlglot_normalize          | 118 ms                                                       | 187 ms: 1.58x slower                                                        |
| richards                   | 52.7 ms                                                      | 83.5 ms: 1.58x slower                                                       |
| sqlglot_optimize           | 59.7 ms                                                      | 94.6 ms: 1.58x slower                                                       |
| genshi_text                | 26.6 ms                                                      | 42.4 ms: 1.59x slower                                                       |
| fannkuch                   | 365 ms                                                       | 582 ms: 1.60x slower                                                        |
| regex_compile              | 144 ms                                                       | 231 ms: 1.60x slower                                                        |
| thrift                     | 877 us                                                       | 1.42 ms: 1.62x slower                                                       |
| sympy_expand               | 505 ms                                                       | 827 ms: 1.64x slower                                                        |
| richards_super             | 59.8 ms                                                      | 100 ms: 1.68x slower                                                        |
| crypto_pyaes               | 72.8 ms                                                      | 124 ms: 1.70x slower                                                        |
| sympy_sum                  | 154 ms                                                       | 263 ms: 1.71x slower                                                        |
| bench_thread_pool          | 901 us                                                       | 1.56 ms: 1.73x slower                                                       |
| django_template            | 38.9 ms                                                      | 68.2 ms: 1.76x slower                                                       |
| comprehensions             | 17.3 us                                                      | 30.3 us: 1.76x slower                                                       |
| logging_format             | 7.07 us                                                      | 12.5 us: 1.76x slower                                                       |
| spectral_norm              | 97.4 ms                                                      | 172 ms: 1.77x slower                                                        |
| pprint_safe_repr           | 812 ms                                                       | 1.45 sec: 1.79x slower                                                      |
| logging_simple             | 6.40 us                                                      | 11.5 us: 1.80x slower                                                       |
| float                      | 81.9 ms                                                      | 148 ms: 1.81x slower                                                        |
| pprint_pformat             | 1.65 sec                                                     | 2.99 sec: 1.81x slower                                                      |
| pickle_pure_python         | 318 us                                                       | 589 us: 1.85x slower                                                        |
| logging_silent             | 97.7 ns                                                      | 183 ns: 1.87x slower                                                        |
| hexiom                     | 6.33 ms                                                      | 12.1 ms: 1.90x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 3.42 ms: 1.92x slower                                                       |
| unpickle_pure_python       | 214 us                                                       | 418 us: 1.95x slower                                                        |
| scimark_sor                | 126 ms                                                       | 251 ms: 2.00x slower                                                        |
| chaos                      | 61.7 ms                                                      | 127 ms: 2.05x slower                                                        |
| scimark_monte_carlo        | 64.9 ms                                                      | 134 ms: 2.07x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 2.91 ms: 2.11x slower                                                       |
| go                         | 160 ms                                                       | 342 ms: 2.13x slower                                                        |
| mako                       | 10.4 ms                                                      | 22.3 ms: 2.14x slower                                                       |
| raytrace                   | 289 ms                                                       | 623 ms: 2.15x slower                                                        |
| nbody                      | 88.0 ms                                                      | 204 ms: 2.32x slower                                                        |
| scimark_lu                 | 97.8 ms                                                      | 236 ms: 2.41x slower                                                        |
| deltablue                  | 3.41 ms                                                      | 8.39 ms: 2.46x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.44x slower                                                                |

Benchmark hidden because not significant (2): asyncio_websockets, create_gc_cycles
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.36x
- 95% likely to have a slowdown of 1.34x
- 99% likely to have a slowdown of 1.32x

# Memory
- memory change: 1.16x