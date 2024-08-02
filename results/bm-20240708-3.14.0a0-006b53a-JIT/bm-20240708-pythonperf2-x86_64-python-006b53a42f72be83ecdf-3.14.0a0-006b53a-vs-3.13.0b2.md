# Results vs. 3.13.0b2

- fork: python
- ref: 006b53a42f72be83ecdf
- machine: linux-x86_64
- commit hash: 006b53a
- commit date: 2024-07-08
- overall geometric mean: 1.01x faster
- HPT reliability: 67.29%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 305 ms: 1.05x slower                                                        |
| docutils       | 2.98 sec                                                         | 3.08 sec: 1.03x slower                                                      |
| html5lib       | 74.7 ms                                                          | 72.1 ms: 1.04x faster                                                       |
| tornado_http   | 119 ms                                                           | 121 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                            | 1.02x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 793 ms: 1.14x faster                                                        |
| async_tree_memoization     | 460 ms                                                           | 410 ms: 1.12x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 307 ms: 1.11x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 387 ms: 1.09x faster                                                        |
| async_tree_none            | 365 ms                                                           | 342 ms: 1.07x faster                                                        |
| async_tree_io              | 873 ms                                                           | 818 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 541 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 581 ms: 1.04x faster                                                        |
| Geometric mean             | (ref)                                                            | 1.09x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 87.8 ms                                                          | 81.8 ms: 1.07x faster                                                       |
| float          | 80.2 ms                                                          | 75.2 ms: 1.07x faster                                                       |
| pidigits       | 254 ms                                                           | 250 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                            | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 237 ms: 1.05x faster                                                        |
| regex_compile  | 144 ms                                                           | 138 ms: 1.04x faster                                                        |
| regex_v8       | 26.0 ms                                                          | 25.6 ms: 1.02x faster                                                       |
| regex_effbot   | 3.40 ms                                                          | 3.50 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                            | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.08 sec: 1.15x faster                                                      |
| xml_etree_generate   | 85.7 ms                                                          | 82.3 ms: 1.04x faster                                                       |
| unpickle_pure_python | 224 us                                                           | 216 us: 1.04x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                           | 99.4 ms: 1.03x faster                                                       |
| xml_etree_process    | 59.7 ms                                                          | 58.7 ms: 1.02x faster                                                       |
| json_dumps           | 10.8 ms                                                          | 10.8 ms: 1.01x slower                                                       |
| pickle_pure_python   | 307 us                                                           | 311 us: 1.01x slower                                                        |
| json_loads           | 25.0 us                                                          | 25.4 us: 1.02x slower                                                       |
| Geometric mean       | (ref)                                                            | 1.03x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.3 ms: 1.01x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 9.02 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                          | 9.22 ms: 1.13x faster                                                       |
| django_template | 39.0 ms                                                          | 42.1 ms: 1.08x slower                                                       |
| genshi_text     | 25.9 ms                                                          | 29.1 ms: 1.12x slower                                                       |
| genshi_xml      | 58.1 ms                                                          | 65.5 ms: 1.13x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.05x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 37.3 us                                                          | 28.6 us: 1.30x faster                                                       |
| deepcopy                   | 377 us                                                           | 307 us: 1.23x faster                                                        |
| richards                   | 53.4 ms                                                          | 45.8 ms: 1.17x faster                                                       |
| richards_super             | 61.2 ms                                                          | 52.7 ms: 1.16x faster                                                       |
| spectral_norm              | 97.3 ms                                                          | 84.0 ms: 1.16x faster                                                       |
| tomli_loads                | 2.40 sec                                                         | 2.08 sec: 1.15x faster                                                      |
| async_tree_io_tg           | 900 ms                                                           | 793 ms: 1.14x faster                                                        |
| deepcopy_reduce            | 3.39 us                                                          | 2.99 us: 1.13x faster                                                       |
| mako                       | 10.4 ms                                                          | 9.22 ms: 1.13x faster                                                       |
| async_tree_memoization     | 460 ms                                                           | 410 ms: 1.12x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 307 ms: 1.11x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 387 ms: 1.09x faster                                                        |
| scimark_fft                | 312 ms                                                           | 289 ms: 1.08x faster                                                        |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 3.97 ms: 1.08x faster                                                       |
| nbody                      | 87.8 ms                                                          | 81.8 ms: 1.07x faster                                                       |
| async_tree_none            | 365 ms                                                           | 342 ms: 1.07x faster                                                        |
| async_tree_io              | 873 ms                                                           | 818 ms: 1.07x faster                                                        |
| float                      | 80.2 ms                                                          | 75.2 ms: 1.07x faster                                                       |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 541 ms: 1.06x faster                                                        |
| pyflate                    | 482 ms                                                           | 455 ms: 1.06x faster                                                        |
| crypto_pyaes               | 73.6 ms                                                          | 69.8 ms: 1.05x faster                                                       |
| regex_dna                  | 249 ms                                                           | 237 ms: 1.05x faster                                                        |
| pathlib                    | 17.1 ms                                                          | 16.3 ms: 1.05x faster                                                       |
| fannkuch                   | 353 ms                                                           | 337 ms: 1.05x faster                                                        |
| regex_compile              | 144 ms                                                           | 138 ms: 1.04x faster                                                        |
| xml_etree_generate         | 85.7 ms                                                          | 82.3 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 581 ms: 1.04x faster                                                        |
| telco                      | 8.40 ms                                                          | 8.09 ms: 1.04x faster                                                       |
| unpickle_pure_python       | 224 us                                                           | 216 us: 1.04x faster                                                        |
| html5lib                   | 74.7 ms                                                          | 72.1 ms: 1.04x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                           | 99.4 ms: 1.03x faster                                                       |
| pprint_safe_repr           | 818 ms                                                           | 795 ms: 1.03x faster                                                        |
| create_gc_cycles           | 2.00 ms                                                          | 1.96 ms: 1.02x faster                                                       |
| pprint_pformat             | 1.66 sec                                                         | 1.63 sec: 1.02x faster                                                      |
| xml_etree_process          | 59.7 ms                                                          | 58.7 ms: 1.02x faster                                                       |
| dulwich_log                | 67.3 ms                                                          | 66.2 ms: 1.02x faster                                                       |
| scimark_monte_carlo        | 65.5 ms                                                          | 64.5 ms: 1.02x faster                                                       |
| regex_v8                   | 26.0 ms                                                          | 25.6 ms: 1.02x faster                                                       |
| pidigits                   | 254 ms                                                           | 250 ms: 1.01x faster                                                        |
| go                         | 165 ms                                                           | 163 ms: 1.01x faster                                                        |
| coroutines                 | 22.0 ms                                                          | 21.9 ms: 1.01x faster                                                       |
| bpe_tokeniser              | 5.14 sec                                                         | 5.12 sec: 1.00x faster                                                      |
| gc_traversal               | 4.69 ms                                                          | 4.67 ms: 1.00x faster                                                       |
| coverage                   | 83.5 ms                                                          | 83.8 ms: 1.00x slower                                                       |
| json_dumps                 | 10.8 ms                                                          | 10.8 ms: 1.01x slower                                                       |
| json                       | 5.35 ms                                                          | 5.39 ms: 1.01x slower                                                       |
| meteor_contest             | 128 ms                                                           | 129 ms: 1.01x slower                                                        |
| logging_simple             | 6.40 us                                                          | 6.45 us: 1.01x slower                                                       |
| sqlglot_parse              | 1.39 ms                                                          | 1.40 ms: 1.01x slower                                                       |
| python_startup             | 13.2 ms                                                          | 13.3 ms: 1.01x slower                                                       |
| logging_format             | 7.11 us                                                          | 7.19 us: 1.01x slower                                                       |
| pickle_pure_python         | 307 us                                                           | 311 us: 1.01x slower                                                        |
| dask                       | 391 ms                                                           | 396 ms: 1.01x slower                                                        |
| json_loads                 | 25.0 us                                                          | 25.4 us: 1.02x slower                                                       |
| tornado_http               | 119 ms                                                           | 121 ms: 1.02x slower                                                        |
| python_startup_no_site     | 8.85 ms                                                          | 9.02 ms: 1.02x slower                                                       |
| thrift                     | 880 us                                                           | 905 us: 1.03x slower                                                        |
| generators                 | 33.5 ms                                                          | 34.5 ms: 1.03x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                          | 1.82 ms: 1.03x slower                                                       |
| regex_effbot               | 3.40 ms                                                          | 3.50 ms: 1.03x slower                                                       |
| scimark_sor                | 119 ms                                                           | 123 ms: 1.03x slower                                                        |
| docutils                   | 2.98 sec                                                         | 3.08 sec: 1.03x slower                                                      |
| pycparser                  | 1.22 sec                                                         | 1.27 sec: 1.04x slower                                                      |
| mdp                        | 2.46 sec                                                         | 2.55 sec: 1.04x slower                                                      |
| logging_silent             | 96.3 ns                                                          | 100 ns: 1.04x slower                                                        |
| sympy_expand               | 501 ms                                                           | 523 ms: 1.04x slower                                                        |
| 2to3                       | 291 ms                                                           | 305 ms: 1.05x slower                                                        |
| hexiom                     | 6.35 ms                                                          | 6.68 ms: 1.05x slower                                                       |
| sympy_str                  | 295 ms                                                           | 310 ms: 1.05x slower                                                        |
| sqlglot_optimize           | 59.5 ms                                                          | 62.9 ms: 1.06x slower                                                       |
| nqueens                    | 88.4 ms                                                          | 93.5 ms: 1.06x slower                                                       |
| sympy_sum                  | 155 ms                                                           | 164 ms: 1.06x slower                                                        |
| async_generators           | 363 ms                                                           | 386 ms: 1.06x slower                                                        |
| comprehensions             | 17.0 us                                                          | 18.1 us: 1.07x slower                                                       |
| sqlglot_normalize          | 120 ms                                                           | 129 ms: 1.07x slower                                                        |
| typing_runtime_protocols   | 171 us                                                           | 183 us: 1.07x slower                                                        |
| django_template            | 39.0 ms                                                          | 42.1 ms: 1.08x slower                                                       |
| pylint                     | 339 ms                                                           | 369 ms: 1.09x slower                                                        |
| deltablue                  | 3.37 ms                                                          | 3.69 ms: 1.09x slower                                                       |
| chaos                      | 59.6 ms                                                          | 65.1 ms: 1.09x slower                                                       |
| sympy_integrate            | 23.2 ms                                                          | 25.5 ms: 1.10x slower                                                       |
| genshi_text                | 25.9 ms                                                          | 29.1 ms: 1.12x slower                                                       |
| genshi_xml                 | 58.1 ms                                                          | 65.5 ms: 1.13x slower                                                       |
| raytrace                   | 260 ms                                                           | 296 ms: 1.14x slower                                                        |
| scimark_lu                 | 97.5 ms                                                          | 114 ms: 1.17x slower                                                        |
| Geometric mean             | (ref)                                                            | 1.01x faster                                                                |

Benchmark hidden because not significant (6): bench_mp_pool, asyncio_websockets, asyncio_tcp_ssl, xml_etree_parse, asyncio_tcp, bench_thread_pool
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 67.29% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x