# Results vs. 3.13.0b2

- fork: python
- ref: 4ed7d1d6acc22807bfb5
- machine: linux-x86_64
- commit hash: 4ed7d1d
- commit date: 2024-09-12
- overall geometric mean: 1.01x faster
- HPT reliability: 80.88%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 309 ms: 1.06x slower                                                        |
| docutils       | 2.98 sec                                                         | 3.15 sec: 1.06x slower                                                      |
| html5lib       | 74.7 ms                                                          | 71.1 ms: 1.05x faster                                                       |
| tornado_http   | 119 ms                                                           | 122 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                            | 1.02x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization     | 460 ms                                                           | 404 ms: 1.14x faster                                                        |
| async_tree_none            | 365 ms                                                           | 323 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 311 ms: 1.09x faster                                                        |
| async_tree_io_tg           | 900 ms                                                           | 828 ms: 1.09x faster                                                        |
| async_tree_io              | 873 ms                                                           | 812 ms: 1.08x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 393 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 576 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 549 ms: 1.04x faster                                                        |
| Geometric mean             | (ref)                                                            | 1.09x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 74.6 ms: 1.08x faster                                                       |
| nbody          | 87.8 ms                                                          | 81.8 ms: 1.07x faster                                                       |
| pidigits       | 254 ms                                                           | 250 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                            | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 233 ms: 1.07x faster                                                        |
| regex_v8       | 26.0 ms                                                          | 25.7 ms: 1.01x faster                                                       |
| regex_compile  | 144 ms                                                           | 147 ms: 1.02x slower                                                        |
| regex_effbot   | 3.40 ms                                                          | 3.49 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.13 sec: 1.13x faster                                                      |
| pickle_dict          | 32.8 us                                                          | 29.5 us: 1.11x faster                                                       |
| xml_etree_generate   | 85.7 ms                                                          | 80.1 ms: 1.07x faster                                                       |
| xml_etree_process    | 59.7 ms                                                          | 55.9 ms: 1.07x faster                                                       |
| pickle_list          | 4.44 us                                                          | 4.18 us: 1.06x faster                                                       |
| json_loads           | 25.0 us                                                          | 23.9 us: 1.05x faster                                                       |
| unpickle             | 15.7 us                                                          | 15.1 us: 1.04x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                           | 98.9 ms: 1.04x faster                                                       |
| pickle               | 10.6 us                                                          | 10.4 us: 1.02x faster                                                       |
| unpickle_pure_python | 224 us                                                           | 220 us: 1.02x faster                                                        |
| json_dumps           | 10.8 ms                                                          | 10.6 ms: 1.01x faster                                                       |
| pickle_pure_python   | 307 us                                                           | 326 us: 1.06x slower                                                        |
| Geometric mean       | (ref)                                                            | 1.04x faster                                                                |

Benchmark hidden because not significant (2): xml_etree_parse, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 9.00 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                          | 9.23 ms: 1.12x faster                                                       |
| django_template | 39.0 ms                                                          | 42.8 ms: 1.10x slower                                                       |
| genshi_xml      | 58.1 ms                                                          | 66.0 ms: 1.14x slower                                                       |
| genshi_text     | 25.9 ms                                                          | 29.5 ms: 1.14x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.06x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 37.3 us                                                          | 27.1 us: 1.38x faster                                                       |
| deepcopy                   | 377 us                                                           | 289 us: 1.31x faster                                                        |
| richards                   | 53.4 ms                                                          | 44.5 ms: 1.20x faster                                                       |
| spectral_norm              | 97.3 ms                                                          | 81.6 ms: 1.19x faster                                                       |
| richards_super             | 61.2 ms                                                          | 52.1 ms: 1.17x faster                                                       |
| deepcopy_reduce            | 3.39 us                                                          | 2.92 us: 1.16x faster                                                       |
| async_tree_memoization     | 460 ms                                                           | 404 ms: 1.14x faster                                                        |
| scimark_sor                | 119 ms                                                           | 105 ms: 1.13x faster                                                        |
| async_tree_none            | 365 ms                                                           | 323 ms: 1.13x faster                                                        |
| tomli_loads                | 2.40 sec                                                         | 2.13 sec: 1.13x faster                                                      |
| mako                       | 10.4 ms                                                          | 9.23 ms: 1.12x faster                                                       |
| pickle_dict                | 32.8 us                                                          | 29.5 us: 1.11x faster                                                       |
| go                         | 165 ms                                                           | 149 ms: 1.11x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 311 ms: 1.09x faster                                                        |
| async_tree_io_tg           | 900 ms                                                           | 828 ms: 1.09x faster                                                        |
| bpe_tokeniser              | 5.14 sec                                                         | 4.75 sec: 1.08x faster                                                      |
| async_tree_io              | 873 ms                                                           | 812 ms: 1.08x faster                                                        |
| float                      | 80.2 ms                                                          | 74.6 ms: 1.08x faster                                                       |
| scimark_fft                | 312 ms                                                           | 290 ms: 1.08x faster                                                        |
| nbody                      | 87.8 ms                                                          | 81.8 ms: 1.07x faster                                                       |
| pyflate                    | 482 ms                                                           | 449 ms: 1.07x faster                                                        |
| regex_dna                  | 249 ms                                                           | 233 ms: 1.07x faster                                                        |
| pathlib                    | 17.1 ms                                                          | 16.0 ms: 1.07x faster                                                       |
| xml_etree_generate         | 85.7 ms                                                          | 80.1 ms: 1.07x faster                                                       |
| async_tree_memoization_tg  | 421 ms                                                           | 393 ms: 1.07x faster                                                        |
| xml_etree_process          | 59.7 ms                                                          | 55.9 ms: 1.07x faster                                                       |
| pickle_list                | 4.44 us                                                          | 4.18 us: 1.06x faster                                                       |
| crypto_pyaes               | 73.6 ms                                                          | 69.3 ms: 1.06x faster                                                       |
| deltablue                  | 3.37 ms                                                          | 3.21 ms: 1.05x faster                                                       |
| html5lib                   | 74.7 ms                                                          | 71.1 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 576 ms: 1.05x faster                                                        |
| json_loads                 | 25.0 us                                                          | 23.9 us: 1.05x faster                                                       |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.10 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 549 ms: 1.04x faster                                                        |
| json                       | 5.35 ms                                                          | 5.14 ms: 1.04x faster                                                       |
| dulwich_log                | 67.3 ms                                                          | 64.6 ms: 1.04x faster                                                       |
| sqlite_synth               | 2.80 us                                                          | 2.69 us: 1.04x faster                                                       |
| unpickle                   | 15.7 us                                                          | 15.1 us: 1.04x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                           | 98.9 ms: 1.04x faster                                                       |
| create_gc_cycles           | 2.00 ms                                                          | 1.94 ms: 1.03x faster                                                       |
| coverage                   | 83.5 ms                                                          | 81.3 ms: 1.03x faster                                                       |
| pprint_safe_repr           | 818 ms                                                           | 796 ms: 1.03x faster                                                        |
| coroutines                 | 22.0 ms                                                          | 21.5 ms: 1.02x faster                                                       |
| pickle                     | 10.6 us                                                          | 10.4 us: 1.02x faster                                                       |
| unpickle_pure_python       | 224 us                                                           | 220 us: 1.02x faster                                                        |
| pidigits                   | 254 ms                                                           | 250 ms: 1.01x faster                                                        |
| json_dumps                 | 10.8 ms                                                          | 10.6 ms: 1.01x faster                                                       |
| regex_v8                   | 26.0 ms                                                          | 25.7 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.58 sec: 1.00x slower                                                      |
| thrift                     | 880 us                                                           | 885 us: 1.01x slower                                                        |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                       |
| fannkuch                   | 353 ms                                                           | 358 ms: 1.01x slower                                                        |
| python_startup_no_site     | 8.85 ms                                                          | 9.00 ms: 1.02x slower                                                       |
| scimark_lu                 | 97.5 ms                                                          | 99.3 ms: 1.02x slower                                                       |
| meteor_contest             | 128 ms                                                           | 131 ms: 1.02x slower                                                        |
| regex_compile              | 144 ms                                                           | 147 ms: 1.02x slower                                                        |
| pycparser                  | 1.22 sec                                                         | 1.25 sec: 1.02x slower                                                      |
| tornado_http               | 119 ms                                                           | 122 ms: 1.02x slower                                                        |
| regex_effbot               | 3.40 ms                                                          | 3.49 ms: 1.03x slower                                                       |
| logging_simple             | 6.40 us                                                          | 6.62 us: 1.03x slower                                                       |
| gc_traversal               | 4.69 ms                                                          | 4.87 ms: 1.04x slower                                                       |
| logging_silent             | 96.3 ns                                                          | 100 ns: 1.04x slower                                                        |
| mdp                        | 2.46 sec                                                         | 2.57 sec: 1.04x slower                                                      |
| scimark_monte_carlo        | 65.5 ms                                                          | 68.9 ms: 1.05x slower                                                       |
| docutils                   | 2.98 sec                                                         | 3.15 sec: 1.06x slower                                                      |
| pickle_pure_python         | 307 us                                                           | 326 us: 1.06x slower                                                        |
| typing_runtime_protocols   | 171 us                                                           | 181 us: 1.06x slower                                                        |
| 2to3                       | 291 ms                                                           | 309 ms: 1.06x slower                                                        |
| sympy_str                  | 295 ms                                                           | 313 ms: 1.06x slower                                                        |
| sympy_expand               | 501 ms                                                           | 533 ms: 1.06x slower                                                        |
| sqlglot_normalize          | 120 ms                                                           | 129 ms: 1.07x slower                                                        |
| bench_mp_pool              | 4.91 ms                                                          | 5.25 ms: 1.07x slower                                                       |
| sqlglot_parse              | 1.39 ms                                                          | 1.49 ms: 1.07x slower                                                       |
| comprehensions             | 17.0 us                                                          | 18.2 us: 1.07x slower                                                       |
| async_generators           | 363 ms                                                           | 393 ms: 1.08x slower                                                        |
| sympy_sum                  | 155 ms                                                           | 169 ms: 1.09x slower                                                        |
| django_template            | 39.0 ms                                                          | 42.8 ms: 1.10x slower                                                       |
| hexiom                     | 6.35 ms                                                          | 6.98 ms: 1.10x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                          | 1.94 ms: 1.10x slower                                                       |
| chaos                      | 59.6 ms                                                          | 65.7 ms: 1.10x slower                                                       |
| sqlglot_optimize           | 59.5 ms                                                          | 65.7 ms: 1.10x slower                                                       |
| nqueens                    | 88.4 ms                                                          | 99.1 ms: 1.12x slower                                                       |
| generators                 | 33.5 ms                                                          | 37.6 ms: 1.12x slower                                                       |
| genshi_xml                 | 58.1 ms                                                          | 66.0 ms: 1.14x slower                                                       |
| genshi_text                | 25.9 ms                                                          | 29.5 ms: 1.14x slower                                                       |
| sympy_integrate            | 23.2 ms                                                          | 26.6 ms: 1.15x slower                                                       |
| raytrace                   | 260 ms                                                           | 310 ms: 1.19x slower                                                        |
| pylint                     | 339 ms                                                           | 410 ms: 1.21x slower                                                        |
| Geometric mean             | (ref)                                                            | 1.01x faster                                                                |

Benchmark hidden because not significant (8): telco, xml_etree_parse, pprint_pformat, asyncio_tcp, asyncio_websockets, unpickle_list, logging_format, bench_thread_pool
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240912-3.14.0a0-4ed7d1d-JIT/bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d.json: unpack_sequence

# HPT report

- Reliability score: 80.88% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x