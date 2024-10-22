# Results vs. 3.13.0

- fork: python
- ref: db6f5e193315a3bbfa7b
- machine: linux-x86_64
- commit hash: db6f5e1
- commit date: 2024-08-13
- overall geometric mean: 1.45x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x slower
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 437 ms: 1.50x slower                                                        |
| docutils       | 2.81 sec                                                     | 3.51 sec: 1.25x slower                                                      |
| html5lib       | 71.9 ms                                                      | 109 ms: 1.52x slower                                                        |
| tornado_http   | 120 ms                                                       | 166 ms: 1.38x slower                                                        |
| Geometric mean | (ref)                                                        | 1.41x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 471 ms: 1.02x slower                                                        |
| async_tree_none_tg         | 340 ms                                                       | 366 ms: 1.08x slower                                                        |
| async_tree_io_tg           | 819 ms                                                       | 891 ms: 1.09x slower                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 632 ms: 1.10x slower                                                        |
| async_tree_io              | 847 ms                                                       | 948 ms: 1.12x slower                                                        |
| async_tree_none            | 372 ms                                                       | 419 ms: 1.12x slower                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 683 ms: 1.14x slower                                                        |
| async_tree_memoization     | 452 ms                                                       | 521 ms: 1.15x slower                                                        |
| asyncio_tcp                | 380 ms                                                       | 448 ms: 1.18x slower                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.90 sec: 1.20x slower                                                      |
| coroutines                 | 21.6 ms                                                      | 29.3 ms: 1.35x slower                                                       |
| async_generators           | 359 ms                                                       | 521 ms: 1.45x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.15x slower                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 253 ms                                                       | 251 ms: 1.01x faster                                                        |
| float          | 81.9 ms                                                      | 146 ms: 1.78x slower                                                        |
| nbody          | 88.0 ms                                                      | 201 ms: 2.28x slower                                                        |
| Geometric mean | (ref)                                                        | 1.59x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 244 ms                                                       | 237 ms: 1.03x faster                                                        |
| regex_v8       | 26.2 ms                                                      | 26.9 ms: 1.03x slower                                                       |
| regex_effbot   | 3.37 ms                                                      | 3.48 ms: 1.03x slower                                                       |
| regex_compile  | 144 ms                                                       | 233 ms: 1.61x slower                                                        |
| Geometric mean | (ref)                                                        | 1.14x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 145 ms                                                       | 136 ms: 1.06x faster                                                        |
| xml_etree_iterparse  | 100 ms                                                       | 109 ms: 1.09x slower                                                        |
| json_loads           | 24.0 us                                                      | 29.7 us: 1.24x slower                                                       |
| json_dumps           | 11.0 ms                                                      | 14.5 ms: 1.32x slower                                                       |
| xml_etree_generate   | 85.3 ms                                                      | 119 ms: 1.39x slower                                                        |
| tomli_loads          | 2.41 sec                                                     | 3.41 sec: 1.42x slower                                                      |
| xml_etree_process    | 60.9 ms                                                      | 97.6 ms: 1.60x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 598 us: 1.88x slower                                                        |
| unpickle_pure_python | 214 us                                                       | 406 us: 1.90x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.39x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 17.1 ms: 1.29x slower                                                       |
| python_startup_no_site | 8.94 ms                                                      | 11.8 ms: 1.32x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.30x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 57.3 ms                                                      | 85.5 ms: 1.49x slower                                                       |
| genshi_text     | 26.6 ms                                                      | 44.1 ms: 1.66x slower                                                       |
| django_template | 38.9 ms                                                      | 69.3 ms: 1.78x slower                                                       |
| mako            | 10.4 ms                                                      | 22.2 ms: 2.13x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.75x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-pythonperf2-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| gc_traversal               | 4.11 ms                                                      | 2.79 ms: 1.47x faster                                                       |
| create_gc_cycles           | 1.76 ms                                                      | 1.61 ms: 1.09x faster                                                       |
| xml_etree_parse            | 145 ms                                                       | 136 ms: 1.06x faster                                                        |
| regex_dna                  | 244 ms                                                       | 237 ms: 1.03x faster                                                        |
| pidigits                   | 253 ms                                                       | 251 ms: 1.01x faster                                                        |
| async_tree_memoization_tg  | 461 ms                                                       | 471 ms: 1.02x slower                                                        |
| regex_v8                   | 26.2 ms                                                      | 26.9 ms: 1.03x slower                                                       |
| regex_effbot               | 3.37 ms                                                      | 3.48 ms: 1.03x slower                                                       |
| bench_mp_pool              | 4.65 ms                                                      | 4.94 ms: 1.06x slower                                                       |
| async_tree_none_tg         | 340 ms                                                       | 366 ms: 1.08x slower                                                        |
| async_tree_io_tg           | 819 ms                                                       | 891 ms: 1.09x slower                                                        |
| xml_etree_iterparse        | 100 ms                                                       | 109 ms: 1.09x slower                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 632 ms: 1.10x slower                                                        |
| async_tree_io              | 847 ms                                                       | 948 ms: 1.12x slower                                                        |
| async_tree_none            | 372 ms                                                       | 419 ms: 1.12x slower                                                        |
| pathlib                    | 17.4 ms                                                      | 19.8 ms: 1.14x slower                                                       |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 683 ms: 1.14x slower                                                        |
| deepcopy                   | 397 us                                                       | 453 us: 1.14x slower                                                        |
| async_tree_memoization     | 452 ms                                                       | 521 ms: 1.15x slower                                                        |
| json                       | 5.22 ms                                                      | 6.16 ms: 1.18x slower                                                       |
| asyncio_tcp                | 380 ms                                                       | 448 ms: 1.18x slower                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.90 sec: 1.20x slower                                                      |
| telco                      | 8.58 ms                                                      | 10.6 ms: 1.23x slower                                                       |
| generators                 | 33.5 ms                                                      | 41.3 ms: 1.23x slower                                                       |
| json_loads                 | 24.0 us                                                      | 29.7 us: 1.24x slower                                                       |
| docutils                   | 2.81 sec                                                     | 3.51 sec: 1.25x slower                                                      |
| pylint                     | 346 ms                                                       | 435 ms: 1.26x slower                                                        |
| python_startup             | 13.3 ms                                                      | 17.1 ms: 1.29x slower                                                       |
| mdp                        | 2.52 sec                                                     | 3.25 sec: 1.29x slower                                                      |
| scimark_fft                | 314 ms                                                       | 413 ms: 1.31x slower                                                        |
| python_startup_no_site     | 8.94 ms                                                      | 11.8 ms: 1.32x slower                                                       |
| json_dumps                 | 11.0 ms                                                      | 14.5 ms: 1.32x slower                                                       |
| deepcopy_memo              | 39.5 us                                                      | 52.3 us: 1.33x slower                                                       |
| bpe_tokeniser              | 5.10 sec                                                     | 6.77 sec: 1.33x slower                                                      |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 5.72 ms: 1.33x slower                                                       |
| coverage                   | 81.1 ms                                                      | 109 ms: 1.34x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 29.3 ms: 1.35x slower                                                       |
| meteor_contest             | 128 ms                                                       | 176 ms: 1.37x slower                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 4.85 us: 1.37x slower                                                       |
| tornado_http               | 120 ms                                                       | 166 ms: 1.38x slower                                                        |
| xml_etree_generate         | 85.3 ms                                                      | 119 ms: 1.39x slower                                                        |
| sympy_integrate            | 23.3 ms                                                      | 32.6 ms: 1.40x slower                                                       |
| pycparser                  | 1.26 sec                                                     | 1.77 sec: 1.41x slower                                                      |
| tomli_loads                | 2.41 sec                                                     | 3.41 sec: 1.42x slower                                                      |
| async_generators           | 359 ms                                                       | 521 ms: 1.45x slower                                                        |
| genshi_xml                 | 57.3 ms                                                      | 85.5 ms: 1.49x slower                                                       |
| nqueens                    | 88.2 ms                                                      | 133 ms: 1.50x slower                                                        |
| 2to3                       | 291 ms                                                       | 437 ms: 1.50x slower                                                        |
| html5lib                   | 71.9 ms                                                      | 109 ms: 1.52x slower                                                        |
| sympy_str                  | 296 ms                                                       | 456 ms: 1.54x slower                                                        |
| richards                   | 52.7 ms                                                      | 82.7 ms: 1.57x slower                                                       |
| pyflate                    | 492 ms                                                       | 774 ms: 1.57x slower                                                        |
| thrift                     | 877 us                                                       | 1.38 ms: 1.58x slower                                                       |
| sqlglot_optimize           | 59.7 ms                                                      | 95.4 ms: 1.60x slower                                                       |
| sqlglot_normalize          | 118 ms                                                       | 189 ms: 1.60x slower                                                        |
| fannkuch                   | 365 ms                                                       | 583 ms: 1.60x slower                                                        |
| xml_etree_process          | 60.9 ms                                                      | 97.6 ms: 1.60x slower                                                       |
| regex_compile              | 144 ms                                                       | 233 ms: 1.61x slower                                                        |
| typing_runtime_protocols   | 174 us                                                       | 282 us: 1.62x slower                                                        |
| sympy_expand               | 505 ms                                                       | 823 ms: 1.63x slower                                                        |
| genshi_text                | 26.6 ms                                                      | 44.1 ms: 1.66x slower                                                       |
| richards_super             | 59.8 ms                                                      | 99.3 ms: 1.66x slower                                                       |
| crypto_pyaes               | 72.8 ms                                                      | 122 ms: 1.67x slower                                                        |
| sympy_sum                  | 154 ms                                                       | 265 ms: 1.72x slower                                                        |
| comprehensions             | 17.3 us                                                      | 30.2 us: 1.75x slower                                                       |
| spectral_norm              | 97.4 ms                                                      | 171 ms: 1.75x slower                                                        |
| float                      | 81.9 ms                                                      | 146 ms: 1.78x slower                                                        |
| logging_format             | 7.07 us                                                      | 12.6 us: 1.78x slower                                                       |
| pprint_safe_repr           | 812 ms                                                       | 1.45 sec: 1.78x slower                                                      |
| django_template            | 38.9 ms                                                      | 69.3 ms: 1.78x slower                                                       |
| logging_simple             | 6.40 us                                                      | 11.6 us: 1.82x slower                                                       |
| pprint_pformat             | 1.65 sec                                                     | 3.00 sec: 1.82x slower                                                      |
| pickle_pure_python         | 318 us                                                       | 598 us: 1.88x slower                                                        |
| hexiom                     | 6.33 ms                                                      | 11.9 ms: 1.89x slower                                                       |
| bench_thread_pool          | 901 us                                                       | 1.70 ms: 1.89x slower                                                       |
| unpickle_pure_python       | 214 us                                                       | 406 us: 1.90x slower                                                        |
| logging_silent             | 97.7 ns                                                      | 186 ns: 1.90x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 3.39 ms: 1.91x slower                                                       |
| scimark_sor                | 126 ms                                                       | 256 ms: 2.04x slower                                                        |
| chaos                      | 61.7 ms                                                      | 127 ms: 2.06x slower                                                        |
| scimark_monte_carlo        | 64.9 ms                                                      | 134 ms: 2.06x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 2.87 ms: 2.08x slower                                                       |
| go                         | 160 ms                                                       | 333 ms: 2.08x slower                                                        |
| raytrace                   | 289 ms                                                       | 610 ms: 2.11x slower                                                        |
| mako                       | 10.4 ms                                                      | 22.2 ms: 2.13x slower                                                       |
| nbody                      | 88.0 ms                                                      | 201 ms: 2.28x slower                                                        |
| deltablue                  | 3.41 ms                                                      | 8.31 ms: 2.44x slower                                                       |
| scimark_lu                 | 97.8 ms                                                      | 248 ms: 2.54x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.45x slower                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.35x
- 95% likely to have a slowdown of 1.33x
- 99% likely to have a slowdown of 1.31x

# Memory
- memory change: 1.17x