# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_mcmodel
- machine: linux-x86_64
- commit hash: d19b26c
- commit date: 2024-07-14
- overall geometric mean: 1.02x faster
- HPT reliability: 84.16%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 298 ms: 1.03x slower                                                        |
| docutils       | 2.81 sec                                                     | 3.10 sec: 1.10x slower                                                      |
| html5lib       | 71.9 ms                                                      | 69.1 ms: 1.04x faster                                                       |
| tornado_http   | 120 ms                                                       | 121 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 383 ms: 1.20x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 304 ms: 1.12x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 405 ms: 1.12x faster                                                        |
| async_tree_none            | 372 ms                                                       | 338 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 540 ms: 1.06x faster                                                        |
| async_tree_io              | 847 ms                                                       | 811 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 579 ms: 1.04x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.0 ms: 1.03x faster                                                       |
| async_tree_io_tg           | 819 ms                                                       | 801 ms: 1.02x faster                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x faster                                                      |
| asyncio_websockets         | 382 ms                                                       | 391 ms: 1.02x slower                                                        |
| async_generators           | 359 ms                                                       | 376 ms: 1.05x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                                |

Benchmark hidden because not significant (1): asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 73.2 ms: 1.12x faster                                                       |
| nbody          | 88.0 ms                                                      | 81.1 ms: 1.09x faster                                                       |
| pidigits       | 253 ms                                                       | 251 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 133 ms: 1.08x faster                                                        |
| regex_v8       | 26.2 ms                                                      | 27.1 ms: 1.03x slower                                                       |
| regex_effbot   | 3.37 ms                                                      | 3.58 ms: 1.06x slower                                                       |
| regex_dna      | 244 ms                                                       | 262 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.04 sec: 1.18x faster                                                      |
| xml_etree_process    | 60.9 ms                                                      | 57.6 ms: 1.06x faster                                                       |
| xml_etree_generate   | 85.3 ms                                                      | 80.9 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 100 ms                                                       | 97.7 ms: 1.02x faster                                                       |
| pickle_pure_python   | 318 us                                                       | 312 us: 1.02x faster                                                        |
| xml_etree_parse      | 145 ms                                                       | 144 ms: 1.01x faster                                                        |
| unpickle_pure_python | 214 us                                                       | 217 us: 1.01x slower                                                        |
| json_loads           | 24.0 us                                                      | 25.4 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                       |
| python_startup_no_site | 8.94 ms                                                      | 9.04 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                      | 8.96 ms: 1.16x faster                                                       |
| genshi_text     | 26.6 ms                                                      | 26.5 ms: 1.01x faster                                                       |
| genshi_xml      | 57.3 ms                                                      | 58.8 ms: 1.03x slower                                                       |
| django_template | 38.9 ms                                                      | 40.8 ms: 1.05x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 39.5 us                                                      | 28.6 us: 1.38x faster                                                       |
| deepcopy                   | 397 us                                                       | 301 us: 1.32x faster                                                        |
| richards                   | 52.7 ms                                                      | 43.0 ms: 1.23x faster                                                       |
| richards_super             | 59.8 ms                                                      | 49.6 ms: 1.21x faster                                                       |
| async_tree_memoization_tg  | 461 ms                                                       | 383 ms: 1.20x faster                                                        |
| tomli_loads                | 2.41 sec                                                     | 2.04 sec: 1.18x faster                                                      |
| spectral_norm              | 97.4 ms                                                      | 82.9 ms: 1.17x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 3.02 us: 1.17x faster                                                       |
| mako                       | 10.4 ms                                                      | 8.96 ms: 1.16x faster                                                       |
| pyflate                    | 492 ms                                                       | 438 ms: 1.12x faster                                                        |
| float                      | 81.9 ms                                                      | 73.2 ms: 1.12x faster                                                       |
| async_tree_none_tg         | 340 ms                                                       | 304 ms: 1.12x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 405 ms: 1.12x faster                                                        |
| async_tree_none            | 372 ms                                                       | 338 ms: 1.10x faster                                                        |
| nbody                      | 88.0 ms                                                      | 81.1 ms: 1.09x faster                                                       |
| regex_compile              | 144 ms                                                       | 133 ms: 1.08x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 16.1 ms: 1.08x faster                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 540 ms: 1.06x faster                                                        |
| xml_etree_process          | 60.9 ms                                                      | 57.6 ms: 1.06x faster                                                       |
| xml_etree_generate         | 85.3 ms                                                      | 80.9 ms: 1.06x faster                                                       |
| fannkuch                   | 365 ms                                                       | 346 ms: 1.05x faster                                                        |
| raytrace                   | 289 ms                                                       | 275 ms: 1.05x faster                                                        |
| pycparser                  | 1.26 sec                                                     | 1.20 sec: 1.05x faster                                                      |
| async_tree_io              | 847 ms                                                       | 811 ms: 1.04x faster                                                        |
| html5lib                   | 71.9 ms                                                      | 69.1 ms: 1.04x faster                                                       |
| crypto_pyaes               | 72.8 ms                                                      | 70.1 ms: 1.04x faster                                                       |
| go                         | 160 ms                                                       | 155 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 579 ms: 1.04x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.60 sec: 1.03x faster                                                      |
| telco                      | 8.58 ms                                                      | 8.35 ms: 1.03x faster                                                       |
| coroutines                 | 21.6 ms                                                      | 21.0 ms: 1.03x faster                                                       |
| scimark_fft                | 314 ms                                                       | 306 ms: 1.03x faster                                                        |
| xml_etree_iterparse        | 100 ms                                                       | 97.7 ms: 1.02x faster                                                       |
| pprint_safe_repr           | 812 ms                                                       | 794 ms: 1.02x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 801 ms: 1.02x faster                                                        |
| logging_simple             | 6.40 us                                                      | 6.27 us: 1.02x faster                                                       |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.20 ms: 1.02x faster                                                       |
| pickle_pure_python         | 318 us                                                       | 312 us: 1.02x faster                                                        |
| scimark_sor                | 126 ms                                                       | 124 ms: 1.01x faster                                                        |
| logging_format             | 7.07 us                                                      | 7.00 us: 1.01x faster                                                       |
| xml_etree_parse            | 145 ms                                                       | 144 ms: 1.01x faster                                                        |
| pidigits                   | 253 ms                                                       | 251 ms: 1.01x faster                                                        |
| genshi_text                | 26.6 ms                                                      | 26.5 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x faster                                                      |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                       |
| dulwich_log                | 65.5 ms                                                      | 65.9 ms: 1.01x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.39 ms: 1.01x slower                                                       |
| meteor_contest             | 128 ms                                                       | 130 ms: 1.01x slower                                                        |
| python_startup_no_site     | 8.94 ms                                                      | 9.04 ms: 1.01x slower                                                       |
| tornado_http               | 120 ms                                                       | 121 ms: 1.01x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.80 ms: 1.01x slower                                                       |
| unpickle_pure_python       | 214 us                                                       | 217 us: 1.01x slower                                                        |
| sympy_expand               | 505 ms                                                       | 512 ms: 1.01x slower                                                        |
| coverage                   | 81.1 ms                                                      | 82.8 ms: 1.02x slower                                                       |
| bpe_tokeniser              | 5.10 sec                                                     | 5.21 sec: 1.02x slower                                                      |
| asyncio_websockets         | 382 ms                                                       | 391 ms: 1.02x slower                                                        |
| thrift                     | 877 us                                                       | 897 us: 1.02x slower                                                        |
| sympy_str                  | 296 ms                                                       | 303 ms: 1.02x slower                                                        |
| genshi_xml                 | 57.3 ms                                                      | 58.8 ms: 1.03x slower                                                       |
| bench_thread_pool          | 901 us                                                       | 924 us: 1.03x slower                                                        |
| 2to3                       | 291 ms                                                       | 298 ms: 1.03x slower                                                        |
| generators                 | 33.5 ms                                                      | 34.4 ms: 1.03x slower                                                       |
| bench_mp_pool              | 4.65 ms                                                      | 4.78 ms: 1.03x slower                                                       |
| scimark_monte_carlo        | 64.9 ms                                                      | 66.9 ms: 1.03x slower                                                       |
| regex_v8                   | 26.2 ms                                                      | 27.1 ms: 1.03x slower                                                       |
| hexiom                     | 6.33 ms                                                      | 6.57 ms: 1.04x slower                                                       |
| mdp                        | 2.52 sec                                                     | 2.62 sec: 1.04x slower                                                      |
| sqlglot_optimize           | 59.7 ms                                                      | 62.2 ms: 1.04x slower                                                       |
| chaos                      | 61.7 ms                                                      | 64.3 ms: 1.04x slower                                                       |
| deltablue                  | 3.41 ms                                                      | 3.57 ms: 1.05x slower                                                       |
| async_generators           | 359 ms                                                       | 376 ms: 1.05x slower                                                        |
| dask                       | 379 ms                                                       | 397 ms: 1.05x slower                                                        |
| comprehensions             | 17.3 us                                                      | 18.1 us: 1.05x slower                                                       |
| django_template            | 38.9 ms                                                      | 40.8 ms: 1.05x slower                                                       |
| json                       | 5.22 ms                                                      | 5.50 ms: 1.05x slower                                                       |
| json_loads                 | 24.0 us                                                      | 25.4 us: 1.06x slower                                                       |
| typing_runtime_protocols   | 174 us                                                       | 185 us: 1.06x slower                                                        |
| regex_effbot               | 3.37 ms                                                      | 3.58 ms: 1.06x slower                                                       |
| sympy_sum                  | 154 ms                                                       | 164 ms: 1.06x slower                                                        |
| logging_silent             | 97.7 ns                                                      | 105 ns: 1.07x slower                                                        |
| nqueens                    | 88.2 ms                                                      | 94.7 ms: 1.07x slower                                                       |
| regex_dna                  | 244 ms                                                       | 262 ms: 1.07x slower                                                        |
| pylint                     | 346 ms                                                       | 372 ms: 1.08x slower                                                        |
| gc_traversal               | 4.11 ms                                                      | 4.43 ms: 1.08x slower                                                       |
| sqlglot_normalize          | 118 ms                                                       | 128 ms: 1.08x slower                                                        |
| sympy_integrate            | 23.3 ms                                                      | 25.4 ms: 1.09x slower                                                       |
| create_gc_cycles           | 1.76 ms                                                      | 1.92 ms: 1.09x slower                                                       |
| docutils                   | 2.81 sec                                                     | 3.10 sec: 1.10x slower                                                      |
| scimark_lu                 | 97.8 ms                                                      | 123 ms: 1.26x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (2): asyncio_tcp, json_dumps
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 84.16% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x