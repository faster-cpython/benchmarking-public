# Results vs. 3.13.0b2

- fork: mdboom
- ref: accelerate_DJBX33A_m
- machine: linux-x86_64
- commit hash: 04d5e93
- commit date: 2024-08-27
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240827-pythonperf2-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 283 ms: 1.03x faster                                                        |
| docutils       | 2.98 sec                                                         | 2.97 sec: 1.00x faster                                                      |
| html5lib       | 74.7 ms                                                          | 72.5 ms: 1.03x faster                                                       |
| tornado_http   | 119 ms                                                           | 117 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                            | 1.02x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240827-pythonperf2-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization     | 460 ms                                                           | 397 ms: 1.16x faster                                                        |
| async_tree_none            | 365 ms                                                           | 317 ms: 1.15x faster                                                        |
| async_tree_io_tg           | 900 ms                                                           | 794 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 306 ms: 1.11x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 387 ms: 1.09x faster                                                        |
| async_tree_io              | 873 ms                                                           | 814 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 568 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 543 ms: 1.05x faster                                                        |
| Geometric mean             | (ref)                                                            | 1.10x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240827-pythonperf2-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 78.4 ms: 1.02x faster                                                       |
| nbody          | 87.8 ms                                                          | 86.7 ms: 1.01x faster                                                       |
| pidigits       | 254 ms                                                           | 253 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240827-pythonperf2-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 233 ms: 1.07x faster                                                        |
| regex_compile  | 144 ms                                                           | 142 ms: 1.02x faster                                                        |
| regex_v8       | 26.0 ms                                                          | 25.7 ms: 1.01x faster                                                       |
| regex_effbot   | 3.40 ms                                                          | 3.53 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                            | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240827-pythonperf2-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 224 us                                                           | 212 us: 1.06x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                           | 101 ms: 1.02x faster                                                        |
| tomli_loads          | 2.40 sec                                                         | 2.37 sec: 1.01x faster                                                      |
| json_loads           | 25.0 us                                                          | 24.8 us: 1.01x faster                                                       |
| json_dumps           | 10.8 ms                                                          | 10.8 ms: 1.01x slower                                                       |
| xml_etree_process    | 59.7 ms                                                          | 60.1 ms: 1.01x slower                                                       |
| xml_etree_generate   | 85.7 ms                                                          | 86.7 ms: 1.01x slower                                                       |
| pickle_pure_python   | 307 us                                                           | 318 us: 1.04x slower                                                        |
| Geometric mean       | (ref)                                                            | 1.00x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240827-pythonperf2-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 9.08 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240827-pythonperf2-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 39.0 ms                                                          | 39.6 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.00x slower                                                                |

Benchmark hidden because not significant (3): genshi_xml, mako, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240827-pythonperf2-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 377 us                                                           | 287 us: 1.31x faster                                                        |
| deepcopy_memo              | 37.3 us                                                          | 30.3 us: 1.23x faster                                                       |
| deepcopy_reduce            | 3.39 us                                                          | 2.91 us: 1.17x faster                                                       |
| async_tree_memoization     | 460 ms                                                           | 397 ms: 1.16x faster                                                        |
| async_tree_none            | 365 ms                                                           | 317 ms: 1.15x faster                                                        |
| generators                 | 33.5 ms                                                          | 29.5 ms: 1.14x faster                                                       |
| async_tree_io_tg           | 900 ms                                                           | 794 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 306 ms: 1.11x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 387 ms: 1.09x faster                                                        |
| richards_super             | 61.2 ms                                                          | 56.9 ms: 1.08x faster                                                       |
| async_tree_io              | 873 ms                                                           | 814 ms: 1.07x faster                                                        |
| pathlib                    | 17.1 ms                                                          | 16.0 ms: 1.07x faster                                                       |
| regex_dna                  | 249 ms                                                           | 233 ms: 1.07x faster                                                        |
| gc_traversal               | 4.69 ms                                                          | 4.38 ms: 1.07x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 568 ms: 1.06x faster                                                        |
| bench_thread_pool          | 908 us                                                           | 858 us: 1.06x faster                                                        |
| unpickle_pure_python       | 224 us                                                           | 212 us: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 543 ms: 1.05x faster                                                        |
| thrift                     | 880 us                                                           | 837 us: 1.05x faster                                                        |
| bpe_tokeniser              | 5.14 sec                                                         | 4.89 sec: 1.05x faster                                                      |
| richards                   | 53.4 ms                                                          | 51.0 ms: 1.05x faster                                                       |
| logging_format             | 7.11 us                                                          | 6.84 us: 1.04x faster                                                       |
| scimark_fft                | 312 ms                                                           | 303 ms: 1.03x faster                                                        |
| 2to3                       | 291 ms                                                           | 283 ms: 1.03x faster                                                        |
| scimark_lu                 | 97.5 ms                                                          | 94.6 ms: 1.03x faster                                                       |
| html5lib                   | 74.7 ms                                                          | 72.5 ms: 1.03x faster                                                       |
| asyncio_tcp                | 378 ms                                                           | 367 ms: 1.03x faster                                                        |
| asyncio_websockets         | 395 ms                                                           | 385 ms: 1.03x faster                                                        |
| sqlglot_optimize           | 59.5 ms                                                          | 58.1 ms: 1.02x faster                                                       |
| sympy_sum                  | 155 ms                                                           | 151 ms: 1.02x faster                                                        |
| float                      | 80.2 ms                                                          | 78.4 ms: 1.02x faster                                                       |
| tornado_http               | 119 ms                                                           | 117 ms: 1.02x faster                                                        |
| sqlglot_normalize          | 120 ms                                                           | 118 ms: 1.02x faster                                                        |
| hexiom                     | 6.35 ms                                                          | 6.23 ms: 1.02x faster                                                       |
| regex_compile              | 144 ms                                                           | 142 ms: 1.02x faster                                                        |
| logging_simple             | 6.40 us                                                          | 6.29 us: 1.02x faster                                                       |
| pprint_safe_repr           | 818 ms                                                           | 804 ms: 1.02x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                           | 101 ms: 1.02x faster                                                        |
| tomli_loads                | 2.40 sec                                                         | 2.37 sec: 1.01x faster                                                      |
| regex_v8                   | 26.0 ms                                                          | 25.7 ms: 1.01x faster                                                       |
| nbody                      | 87.8 ms                                                          | 86.7 ms: 1.01x faster                                                       |
| pprint_pformat             | 1.66 sec                                                         | 1.64 sec: 1.01x faster                                                      |
| coroutines                 | 22.0 ms                                                          | 21.7 ms: 1.01x faster                                                       |
| meteor_contest             | 128 ms                                                           | 127 ms: 1.01x faster                                                        |
| sympy_integrate            | 23.2 ms                                                          | 22.9 ms: 1.01x faster                                                       |
| coverage                   | 83.5 ms                                                          | 82.6 ms: 1.01x faster                                                       |
| sympy_str                  | 295 ms                                                           | 292 ms: 1.01x faster                                                        |
| crypto_pyaes               | 73.6 ms                                                          | 72.9 ms: 1.01x faster                                                       |
| json_loads                 | 25.0 us                                                          | 24.8 us: 1.01x faster                                                       |
| scimark_monte_carlo        | 65.5 ms                                                          | 65.1 ms: 1.01x faster                                                       |
| nqueens                    | 88.4 ms                                                          | 87.9 ms: 1.01x faster                                                       |
| pyflate                    | 482 ms                                                           | 479 ms: 1.01x faster                                                        |
| docutils                   | 2.98 sec                                                         | 2.97 sec: 1.00x faster                                                      |
| spectral_norm              | 97.3 ms                                                          | 97.0 ms: 1.00x faster                                                       |
| pidigits                   | 254 ms                                                           | 253 ms: 1.00x faster                                                        |
| fannkuch                   | 353 ms                                                           | 354 ms: 1.00x slower                                                        |
| deltablue                  | 3.37 ms                                                          | 3.39 ms: 1.01x slower                                                       |
| json_dumps                 | 10.8 ms                                                          | 10.8 ms: 1.01x slower                                                       |
| xml_etree_process          | 59.7 ms                                                          | 60.1 ms: 1.01x slower                                                       |
| logging_silent             | 96.3 ns                                                          | 97.3 ns: 1.01x slower                                                       |
| xml_etree_generate         | 85.7 ms                                                          | 86.7 ms: 1.01x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                          | 1.79 ms: 1.01x slower                                                       |
| sqlglot_parse              | 1.39 ms                                                          | 1.41 ms: 1.01x slower                                                       |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                       |
| django_template            | 39.0 ms                                                          | 39.6 ms: 1.02x slower                                                       |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.37 ms: 1.02x slower                                                       |
| mdp                        | 2.46 sec                                                         | 2.52 sec: 1.02x slower                                                      |
| python_startup_no_site     | 8.85 ms                                                          | 9.08 ms: 1.03x slower                                                       |
| chaos                      | 59.6 ms                                                          | 61.2 ms: 1.03x slower                                                       |
| pycparser                  | 1.22 sec                                                         | 1.26 sec: 1.03x slower                                                      |
| typing_runtime_protocols   | 171 us                                                           | 176 us: 1.03x slower                                                        |
| pickle_pure_python         | 307 us                                                           | 318 us: 1.04x slower                                                        |
| regex_effbot               | 3.40 ms                                                          | 3.53 ms: 1.04x slower                                                       |
| raytrace                   | 260 ms                                                           | 270 ms: 1.04x slower                                                        |
| go                         | 165 ms                                                           | 183 ms: 1.11x slower                                                        |
| Geometric mean             | (ref)                                                            | 1.03x faster                                                                |

Benchmark hidden because not significant (14): bench_mp_pool, create_gc_cycles, telco, json, genshi_xml, mako, xml_etree_parse, async_generators, asyncio_tcp_ssl, scimark_sor, comprehensions, sympy_expand, genshi_text, pylint
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x