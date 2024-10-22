# Results vs. 3.13.0

- fork: python
- ref: v3.14.0a1
- machine: linux-x86_64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.08x slower
- HPT reliability: 51.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 314 ms: 1.08x slower                                             |
| docutils       | 2.81 sec                                                     | 3.17 sec: 1.13x slower                                           |
| html5lib       | 71.9 ms                                                      | 69.2 ms: 1.04x faster                                            |
| tornado_http   | 120 ms                                                       | 123 ms: 1.03x slower                                             |
| Geometric mean | (ref)                                                        | 1.05x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 373 ms: 1.24x faster                                             |
| async_tree_none            | 372 ms                                                       | 333 ms: 1.12x faster                                             |
| async_tree_memoization     | 452 ms                                                       | 408 ms: 1.11x faster                                             |
| async_tree_none_tg         | 340 ms                                                       | 323 ms: 1.05x faster                                             |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 574 ms: 1.04x faster                                             |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 557 ms: 1.03x faster                                             |
| asyncio_tcp                | 380 ms                                                       | 377 ms: 1.01x faster                                             |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x slower                                           |
| async_generators           | 359 ms                                                       | 379 ms: 1.05x slower                                             |
| async_tree_io_tg           | 819 ms                                                       | 865 ms: 1.06x slower                                             |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                     |

Benchmark hidden because not significant (3): asyncio_websockets, async_tree_io, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 83.7 ms: 1.05x faster                                            |
| float          | 81.9 ms                                                      | 79.3 ms: 1.03x faster                                            |
| pidigits       | 253 ms                                                       | 251 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                        | 1.03x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                      | 25.0 ms: 1.05x faster                                            |
| regex_dna      | 244 ms                                                       | 233 ms: 1.05x faster                                             |
| regex_compile  | 144 ms                                                       | 150 ms: 1.04x slower                                             |
| regex_effbot   | 3.37 ms                                                      | 3.57 ms: 1.06x slower                                            |
| Geometric mean | (ref)                                                        | 1.00x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.12 sec: 1.14x faster                                           |
| xml_etree_generate   | 85.3 ms                                                      | 80.6 ms: 1.06x faster                                            |
| xml_etree_process    | 60.9 ms                                                      | 57.7 ms: 1.06x faster                                            |
| unpickle             | 15.1 us                                                      | 14.9 us: 1.02x faster                                            |
| xml_etree_iterparse  | 100 ms                                                       | 99.5 ms: 1.01x faster                                            |
| unpickle_list        | 4.62 us                                                      | 4.67 us: 1.01x slower                                            |
| pickle_list          | 4.59 us                                                      | 4.66 us: 1.02x slower                                            |
| pickle               | 10.5 us                                                      | 10.7 us: 1.02x slower                                            |
| json_dumps           | 11.0 ms                                                      | 11.2 ms: 1.02x slower                                            |
| pickle_dict          | 32.1 us                                                      | 32.9 us: 1.03x slower                                            |
| json_loads           | 24.0 us                                                      | 24.6 us: 1.03x slower                                            |
| unpickle_pure_python | 214 us                                                       | 221 us: 1.03x slower                                             |
| pickle_pure_python   | 318 us                                                       | 333 us: 1.05x slower                                             |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                     |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 8.94 ms                                                      | 9.01 ms: 1.01x slower                                            |
| python_startup         | 13.3 ms                                                      | 14.9 ms: 1.12x slower                                            |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 10.4 ms                                                      | 9.52 ms: 1.09x faster                                            |
| genshi_text     | 26.6 ms                                                      | 28.0 ms: 1.05x slower                                            |
| genshi_xml      | 57.3 ms                                                      | 62.1 ms: 1.08x slower                                            |
| django_template | 38.9 ms                                                      | 42.9 ms: 1.10x slower                                            |
| Geometric mean  | (ref)                                                        | 1.04x slower                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| deepcopy_memo              | 39.5 us                                                      | 29.9 us: 1.32x faster                                            |
| deepcopy                   | 397 us                                                       | 309 us: 1.28x faster                                             |
| async_tree_memoization_tg  | 461 ms                                                       | 373 ms: 1.24x faster                                             |
| scimark_sor                | 126 ms                                                       | 103 ms: 1.22x faster                                             |
| deepcopy_reduce            | 3.54 us                                                      | 3.10 us: 1.14x faster                                            |
| tomli_loads                | 2.41 sec                                                     | 2.12 sec: 1.14x faster                                           |
| richards                   | 52.7 ms                                                      | 46.6 ms: 1.13x faster                                            |
| async_tree_none            | 372 ms                                                       | 333 ms: 1.12x faster                                             |
| richards_super             | 59.8 ms                                                      | 53.6 ms: 1.11x faster                                            |
| async_tree_memoization     | 452 ms                                                       | 408 ms: 1.11x faster                                             |
| telco                      | 8.58 ms                                                      | 7.80 ms: 1.10x faster                                            |
| mako                       | 10.4 ms                                                      | 9.52 ms: 1.09x faster                                            |
| pathlib                    | 17.4 ms                                                      | 15.9 ms: 1.09x faster                                            |
| scimark_fft                | 314 ms                                                       | 290 ms: 1.08x faster                                             |
| bpe_tokeniser              | 5.10 sec                                                     | 4.74 sec: 1.08x faster                                           |
| xml_etree_generate         | 85.3 ms                                                      | 80.6 ms: 1.06x faster                                            |
| xml_etree_process          | 60.9 ms                                                      | 57.7 ms: 1.06x faster                                            |
| go                         | 160 ms                                                       | 152 ms: 1.05x faster                                             |
| nbody                      | 88.0 ms                                                      | 83.7 ms: 1.05x faster                                            |
| async_tree_none_tg         | 340 ms                                                       | 323 ms: 1.05x faster                                             |
| regex_v8                   | 26.2 ms                                                      | 25.0 ms: 1.05x faster                                            |
| regex_dna                  | 244 ms                                                       | 233 ms: 1.05x faster                                             |
| spectral_norm              | 97.4 ms                                                      | 93.0 ms: 1.05x faster                                            |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 574 ms: 1.04x faster                                             |
| pyflate                    | 492 ms                                                       | 473 ms: 1.04x faster                                             |
| logging_silent             | 97.7 ns                                                      | 93.9 ns: 1.04x faster                                            |
| html5lib                   | 71.9 ms                                                      | 69.2 ms: 1.04x faster                                            |
| float                      | 81.9 ms                                                      | 79.3 ms: 1.03x faster                                            |
| deltablue                  | 3.41 ms                                                      | 3.30 ms: 1.03x faster                                            |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 557 ms: 1.03x faster                                             |
| json                       | 5.22 ms                                                      | 5.08 ms: 1.03x faster                                            |
| scimark_lu                 | 97.8 ms                                                      | 95.5 ms: 1.02x faster                                            |
| coverage                   | 81.1 ms                                                      | 79.2 ms: 1.02x faster                                            |
| sqlite_synth               | 2.79 us                                                      | 2.73 us: 1.02x faster                                            |
| unpickle                   | 15.1 us                                                      | 14.9 us: 1.02x faster                                            |
| pprint_safe_repr           | 812 ms                                                       | 798 ms: 1.02x faster                                             |
| dulwich_log                | 65.5 ms                                                      | 64.5 ms: 1.02x faster                                            |
| fannkuch                   | 365 ms                                                       | 361 ms: 1.01x faster                                             |
| asyncio_tcp                | 380 ms                                                       | 377 ms: 1.01x faster                                             |
| crypto_pyaes               | 72.8 ms                                                      | 72.2 ms: 1.01x faster                                            |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.26 ms: 1.01x faster                                            |
| xml_etree_iterparse        | 100 ms                                                       | 99.5 ms: 1.01x faster                                            |
| pidigits                   | 253 ms                                                       | 251 ms: 1.01x faster                                             |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x slower                                           |
| python_startup_no_site     | 8.94 ms                                                      | 9.01 ms: 1.01x slower                                            |
| unpickle_list              | 4.62 us                                                      | 4.67 us: 1.01x slower                                            |
| pickle_list                | 4.59 us                                                      | 4.66 us: 1.02x slower                                            |
| pickle                     | 10.5 us                                                      | 10.7 us: 1.02x slower                                            |
| thrift                     | 877 us                                                       | 894 us: 1.02x slower                                             |
| logging_format             | 7.07 us                                                      | 7.21 us: 1.02x slower                                            |
| json_dumps                 | 11.0 ms                                                      | 11.2 ms: 1.02x slower                                            |
| mdp                        | 2.52 sec                                                     | 2.59 sec: 1.03x slower                                           |
| pickle_dict                | 32.1 us                                                      | 32.9 us: 1.03x slower                                            |
| json_loads                 | 24.0 us                                                      | 24.6 us: 1.03x slower                                            |
| pycparser                  | 1.26 sec                                                     | 1.29 sec: 1.03x slower                                           |
| tornado_http               | 120 ms                                                       | 123 ms: 1.03x slower                                             |
| unpickle_pure_python       | 214 us                                                       | 221 us: 1.03x slower                                             |
| typing_runtime_protocols   | 174 us                                                       | 180 us: 1.03x slower                                             |
| logging_simple             | 6.40 us                                                      | 6.62 us: 1.03x slower                                            |
| meteor_contest             | 128 ms                                                       | 133 ms: 1.04x slower                                             |
| regex_compile              | 144 ms                                                       | 150 ms: 1.04x slower                                             |
| pickle_pure_python         | 318 us                                                       | 333 us: 1.05x slower                                             |
| sympy_expand               | 505 ms                                                       | 530 ms: 1.05x slower                                             |
| genshi_text                | 26.6 ms                                                      | 28.0 ms: 1.05x slower                                            |
| scimark_monte_carlo        | 64.9 ms                                                      | 68.4 ms: 1.05x slower                                            |
| async_generators           | 359 ms                                                       | 379 ms: 1.05x slower                                             |
| bench_thread_pool          | 901 us                                                       | 950 us: 1.05x slower                                             |
| async_tree_io_tg           | 819 ms                                                       | 865 ms: 1.06x slower                                             |
| regex_effbot               | 3.37 ms                                                      | 3.57 ms: 1.06x slower                                            |
| 2to3                       | 291 ms                                                       | 314 ms: 1.08x slower                                             |
| sympy_str                  | 296 ms                                                       | 319 ms: 1.08x slower                                             |
| chaos                      | 61.7 ms                                                      | 66.5 ms: 1.08x slower                                            |
| genshi_xml                 | 57.3 ms                                                      | 62.1 ms: 1.08x slower                                            |
| sqlglot_parse              | 1.38 ms                                                      | 1.50 ms: 1.09x slower                                            |
| raytrace                   | 289 ms                                                       | 315 ms: 1.09x slower                                             |
| comprehensions             | 17.3 us                                                      | 18.8 us: 1.09x slower                                            |
| django_template            | 38.9 ms                                                      | 42.9 ms: 1.10x slower                                            |
| sqlglot_transpile          | 1.78 ms                                                      | 1.98 ms: 1.11x slower                                            |
| sqlglot_normalize          | 118 ms                                                       | 132 ms: 1.12x slower                                             |
| python_startup             | 13.3 ms                                                      | 14.9 ms: 1.12x slower                                            |
| hexiom                     | 6.33 ms                                                      | 7.11 ms: 1.12x slower                                            |
| sympy_sum                  | 154 ms                                                       | 173 ms: 1.13x slower                                             |
| docutils                   | 2.81 sec                                                     | 3.17 sec: 1.13x slower                                           |
| sqlglot_optimize           | 59.7 ms                                                      | 69.7 ms: 1.17x slower                                            |
| sympy_integrate            | 23.3 ms                                                      | 27.3 ms: 1.17x slower                                            |
| nqueens                    | 88.2 ms                                                      | 104 ms: 1.17x slower                                             |
| generators                 | 33.5 ms                                                      | 39.4 ms: 1.18x slower                                            |
| pylint                     | 346 ms                                                       | 423 ms: 1.22x slower                                             |
| gc_traversal               | 4.11 ms                                                      | 5.21 ms: 1.27x slower                                            |
| unpack_sequence            | 56.8 ns                                                      | 89.6 ns: 1.58x slower                                            |
| create_gc_cycles           | 1.76 ms                                                      | 2.90 ms: 1.65x slower                                            |
| bench_mp_pool              | 4.65 ms                                                      | 2.28 sec: 490.77x slower                                         |
| Geometric mean             | (ref)                                                        | 1.08x slower                                                     |

Benchmark hidden because not significant (5): pprint_pformat, asyncio_websockets, xml_etree_parse, async_tree_io, coroutines
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: sphinx

# HPT report

- Reliability score: 51.96% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.19x