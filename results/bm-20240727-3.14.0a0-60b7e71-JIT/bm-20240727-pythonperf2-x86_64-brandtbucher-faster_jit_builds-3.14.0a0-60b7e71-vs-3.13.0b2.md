# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: faster_jit_builds
- machine: linux-x86_64
- commit hash: 60b7e71
- commit date: 2024-07-27
- overall geometric mean: 1.01x faster
- HPT reliability: 93.66%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 303 ms: 1.04x slower                                                           |
| docutils       | 2.98 sec                                                         | 3.12 sec: 1.05x slower                                                         |
| html5lib       | 74.7 ms                                                          | 69.9 ms: 1.07x faster                                                          |
| Geometric mean | (ref)                                                            | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 764 ms: 1.18x faster                                                           |
| async_tree_memoization     | 460 ms                                                           | 400 ms: 1.15x faster                                                           |
| async_tree_none_tg         | 340 ms                                                           | 302 ms: 1.13x faster                                                           |
| async_tree_memoization_tg  | 421 ms                                                           | 379 ms: 1.11x faster                                                           |
| async_tree_io              | 873 ms                                                           | 795 ms: 1.10x faster                                                           |
| async_tree_none            | 365 ms                                                           | 333 ms: 1.10x faster                                                           |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 536 ms: 1.07x faster                                                           |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 571 ms: 1.06x faster                                                           |
| Geometric mean             | (ref)                                                            | 1.11x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 87.8 ms                                                          | 81.5 ms: 1.08x faster                                                          |
| float          | 80.2 ms                                                          | 74.6 ms: 1.07x faster                                                          |
| pidigits       | 254 ms                                                           | 251 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                            | 1.05x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 236 ms: 1.06x faster                                                           |
| regex_compile  | 144 ms                                                           | 137 ms: 1.05x faster                                                           |
| regex_v8       | 26.0 ms                                                          | 26.5 ms: 1.02x slower                                                          |
| regex_effbot   | 3.40 ms                                                          | 3.52 ms: 1.03x slower                                                          |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.09 sec: 1.15x faster                                                         |
| xml_etree_iterparse  | 103 ms                                                           | 96.7 ms: 1.06x faster                                                          |
| unpickle_pure_python | 224 us                                                           | 213 us: 1.05x faster                                                           |
| xml_etree_generate   | 85.7 ms                                                          | 81.4 ms: 1.05x faster                                                          |
| xml_etree_parse      | 144 ms                                                           | 140 ms: 1.03x faster                                                           |
| xml_etree_process    | 59.7 ms                                                          | 58.8 ms: 1.02x faster                                                          |
| json_loads           | 25.0 us                                                          | 25.5 us: 1.02x slower                                                          |
| pickle_pure_python   | 307 us                                                           | 317 us: 1.03x slower                                                           |
| Geometric mean       | (ref)                                                            | 1.03x faster                                                                   |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|------------------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                          |
| python_startup_no_site | 8.85 ms                                                          | 9.08 ms: 1.03x slower                                                          |
| Geometric mean         | (ref)                                                            | 1.02x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|-----------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                          | 9.26 ms: 1.12x faster                                                          |
| django_template | 39.0 ms                                                          | 41.2 ms: 1.06x slower                                                          |
| genshi_text     | 25.9 ms                                                          | 30.3 ms: 1.17x slower                                                          |
| genshi_xml      | 58.1 ms                                                          | 68.9 ms: 1.19x slower                                                          |
| Geometric mean  | (ref)                                                            | 1.07x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy_memo              | 37.3 us                                                          | 28.4 us: 1.31x faster                                                          |
| deepcopy                   | 377 us                                                           | 302 us: 1.25x faster                                                           |
| spectral_norm              | 97.3 ms                                                          | 81.0 ms: 1.20x faster                                                          |
| richards_super             | 61.2 ms                                                          | 51.2 ms: 1.20x faster                                                          |
| richards                   | 53.4 ms                                                          | 45.1 ms: 1.19x faster                                                          |
| async_tree_io_tg           | 900 ms                                                           | 764 ms: 1.18x faster                                                           |
| tomli_loads                | 2.40 sec                                                         | 2.09 sec: 1.15x faster                                                         |
| async_tree_memoization     | 460 ms                                                           | 400 ms: 1.15x faster                                                           |
| deepcopy_reduce            | 3.39 us                                                          | 3.00 us: 1.13x faster                                                          |
| async_tree_none_tg         | 340 ms                                                           | 302 ms: 1.13x faster                                                           |
| mako                       | 10.4 ms                                                          | 9.26 ms: 1.12x faster                                                          |
| async_tree_memoization_tg  | 421 ms                                                           | 379 ms: 1.11x faster                                                           |
| pyflate                    | 482 ms                                                           | 437 ms: 1.10x faster                                                           |
| async_tree_io              | 873 ms                                                           | 795 ms: 1.10x faster                                                           |
| async_tree_none            | 365 ms                                                           | 333 ms: 1.10x faster                                                           |
| gc_traversal               | 4.69 ms                                                          | 4.34 ms: 1.08x faster                                                          |
| nbody                      | 87.8 ms                                                          | 81.5 ms: 1.08x faster                                                          |
| float                      | 80.2 ms                                                          | 74.6 ms: 1.07x faster                                                          |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 536 ms: 1.07x faster                                                           |
| html5lib                   | 74.7 ms                                                          | 69.9 ms: 1.07x faster                                                          |
| scimark_fft                | 312 ms                                                           | 292 ms: 1.07x faster                                                           |
| pathlib                    | 17.1 ms                                                          | 16.1 ms: 1.07x faster                                                          |
| bpe_tokeniser              | 5.14 sec                                                         | 4.84 sec: 1.06x faster                                                         |
| telco                      | 8.40 ms                                                          | 7.92 ms: 1.06x faster                                                          |
| xml_etree_iterparse        | 103 ms                                                           | 96.7 ms: 1.06x faster                                                          |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 571 ms: 1.06x faster                                                           |
| regex_dna                  | 249 ms                                                           | 236 ms: 1.06x faster                                                           |
| crypto_pyaes               | 73.6 ms                                                          | 69.7 ms: 1.06x faster                                                          |
| unpickle_pure_python       | 224 us                                                           | 213 us: 1.05x faster                                                           |
| regex_compile              | 144 ms                                                           | 137 ms: 1.05x faster                                                           |
| xml_etree_generate         | 85.7 ms                                                          | 81.4 ms: 1.05x faster                                                          |
| create_gc_cycles           | 2.00 ms                                                          | 1.92 ms: 1.05x faster                                                          |
| coverage                   | 83.5 ms                                                          | 80.7 ms: 1.04x faster                                                          |
| coroutines                 | 22.0 ms                                                          | 21.3 ms: 1.03x faster                                                          |
| xml_etree_parse            | 144 ms                                                           | 140 ms: 1.03x faster                                                           |
| go                         | 165 ms                                                           | 162 ms: 1.02x faster                                                           |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.22 ms: 1.02x faster                                                          |
| xml_etree_process          | 59.7 ms                                                          | 58.8 ms: 1.02x faster                                                          |
| logging_format             | 7.11 us                                                          | 7.01 us: 1.01x faster                                                          |
| pprint_safe_repr           | 818 ms                                                           | 807 ms: 1.01x faster                                                           |
| asyncio_websockets         | 395 ms                                                           | 390 ms: 1.01x faster                                                           |
| pidigits                   | 254 ms                                                           | 251 ms: 1.01x faster                                                           |
| scimark_monte_carlo        | 65.5 ms                                                          | 64.8 ms: 1.01x faster                                                          |
| logging_simple             | 6.40 us                                                          | 6.37 us: 1.01x faster                                                          |
| meteor_contest             | 128 ms                                                           | 127 ms: 1.01x faster                                                           |
| sqlglot_parse              | 1.39 ms                                                          | 1.41 ms: 1.01x slower                                                          |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                          |
| regex_v8                   | 26.0 ms                                                          | 26.5 ms: 1.02x slower                                                          |
| generators                 | 33.5 ms                                                          | 34.2 ms: 1.02x slower                                                          |
| json_loads                 | 25.0 us                                                          | 25.5 us: 1.02x slower                                                          |
| json                       | 5.35 ms                                                          | 5.48 ms: 1.02x slower                                                          |
| python_startup_no_site     | 8.85 ms                                                          | 9.08 ms: 1.03x slower                                                          |
| pickle_pure_python         | 307 us                                                           | 317 us: 1.03x slower                                                           |
| regex_effbot               | 3.40 ms                                                          | 3.52 ms: 1.03x slower                                                          |
| fannkuch                   | 353 ms                                                           | 366 ms: 1.04x slower                                                           |
| sqlglot_transpile          | 1.76 ms                                                          | 1.83 ms: 1.04x slower                                                          |
| hexiom                     | 6.35 ms                                                          | 6.61 ms: 1.04x slower                                                          |
| 2to3                       | 291 ms                                                           | 303 ms: 1.04x slower                                                           |
| docutils                   | 2.98 sec                                                         | 3.12 sec: 1.05x slower                                                         |
| logging_silent             | 96.3 ns                                                          | 101 ns: 1.05x slower                                                           |
| sympy_expand               | 501 ms                                                           | 528 ms: 1.05x slower                                                           |
| mdp                        | 2.46 sec                                                         | 2.60 sec: 1.06x slower                                                         |
| sympy_str                  | 295 ms                                                           | 311 ms: 1.06x slower                                                           |
| django_template            | 39.0 ms                                                          | 41.2 ms: 1.06x slower                                                          |
| deltablue                  | 3.37 ms                                                          | 3.59 ms: 1.06x slower                                                          |
| sqlglot_optimize           | 59.5 ms                                                          | 63.6 ms: 1.07x slower                                                          |
| async_generators           | 363 ms                                                           | 388 ms: 1.07x slower                                                           |
| sympy_sum                  | 155 ms                                                           | 167 ms: 1.08x slower                                                           |
| nqueens                    | 88.4 ms                                                          | 95.5 ms: 1.08x slower                                                          |
| scimark_sor                | 119 ms                                                           | 128 ms: 1.08x slower                                                           |
| comprehensions             | 17.0 us                                                          | 18.4 us: 1.08x slower                                                          |
| typing_runtime_protocols   | 171 us                                                           | 185 us: 1.09x slower                                                           |
| sqlglot_normalize          | 120 ms                                                           | 133 ms: 1.11x slower                                                           |
| sympy_integrate            | 23.2 ms                                                          | 25.7 ms: 1.11x slower                                                          |
| chaos                      | 59.6 ms                                                          | 66.5 ms: 1.12x slower                                                          |
| raytrace                   | 260 ms                                                           | 294 ms: 1.13x slower                                                           |
| pylint                     | 339 ms                                                           | 386 ms: 1.14x slower                                                           |
| genshi_text                | 25.9 ms                                                          | 30.3 ms: 1.17x slower                                                          |
| scimark_lu                 | 97.5 ms                                                          | 116 ms: 1.19x slower                                                           |
| genshi_xml                 | 58.1 ms                                                          | 68.9 ms: 1.19x slower                                                          |
| Geometric mean             | (ref)                                                            | 1.01x faster                                                                   |

Benchmark hidden because not significant (10): bench_mp_pool, bench_thread_pool, dask, asyncio_tcp, pycparser, json_dumps, asyncio_tcp_ssl, tornado_http, thrift, pprint_pformat
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 93.66% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x