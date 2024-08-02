# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: no_cold_exits
- machine: linux-x86_64
- commit hash: f837cc6
- commit date: 2024-06-10
- overall geometric mean: 1.01x slower
- HPT reliability: 95.74%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 304 ms: 1.04x slower                                                       |
| docutils       | 2.98 sec                                                         | 3.09 sec: 1.04x slower                                                     |
| html5lib       | 74.7 ms                                                          | 73.3 ms: 1.02x faster                                                      |
| tornado_http   | 119 ms                                                           | 122 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                            | 1.02x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|-------------------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg        | 900 ms                                                           | 914 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed | 604 ms                                                           | 620 ms: 1.03x slower                                                       |
| async_tree_none         | 365 ms                                                           | 377 ms: 1.03x slower                                                       |
| async_tree_memoization  | 460 ms                                                           | 476 ms: 1.03x slower                                                       |
| Geometric mean          | (ref)                                                            | 1.02x slower                                                               |

Benchmark hidden because not significant (4): async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 75.5 ms: 1.06x faster                                                      |
| nbody          | 87.8 ms                                                          | 84.1 ms: 1.04x faster                                                      |
| pidigits       | 254 ms                                                           | 250 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                            | 1.04x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                           | 136 ms: 1.06x faster                                                       |
| regex_dna      | 249 ms                                                           | 239 ms: 1.04x faster                                                       |
| regex_effbot   | 3.40 ms                                                          | 3.49 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                            | 1.02x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.10 sec: 1.14x faster                                                     |
| pickle_dict          | 32.8 us                                                          | 31.1 us: 1.06x faster                                                      |
| xml_etree_generate   | 85.7 ms                                                          | 81.8 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 103 ms                                                           | 99.0 ms: 1.04x faster                                                      |
| unpickle_pure_python | 224 us                                                           | 217 us: 1.04x faster                                                       |
| xml_etree_process    | 59.7 ms                                                          | 58.6 ms: 1.02x faster                                                      |
| pickle               | 10.6 us                                                          | 10.5 us: 1.01x faster                                                      |
| pickle_list          | 4.44 us                                                          | 4.48 us: 1.01x slower                                                      |
| unpickle             | 15.7 us                                                          | 16.0 us: 1.02x slower                                                      |
| pickle_pure_python   | 307 us                                                           | 315 us: 1.02x slower                                                       |
| unpickle_list        | 4.70 us                                                          | 4.93 us: 1.05x slower                                                      |
| Geometric mean       | (ref)                                                            | 1.02x faster                                                               |

Benchmark hidden because not significant (3): xml_etree_parse, json_dumps, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|------------------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 8.85 ms                                                          | 8.86 ms: 1.00x slower                                                      |
| Geometric mean         | (ref)                                                            | 1.00x slower                                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|-----------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                          | 9.15 ms: 1.13x faster                                                      |
| django_template | 39.0 ms                                                          | 41.0 ms: 1.05x slower                                                      |
| genshi_text     | 25.9 ms                                                          | 28.1 ms: 1.09x slower                                                      |
| genshi_xml      | 58.1 ms                                                          | 64.9 ms: 1.12x slower                                                      |
| Geometric mean  | (ref)                                                            | 1.03x slower                                                               |

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|--------------------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| richards                 | 53.4 ms                                                          | 43.2 ms: 1.24x faster                                                      |
| richards_super           | 61.2 ms                                                          | 51.3 ms: 1.19x faster                                                      |
| spectral_norm            | 97.3 ms                                                          | 83.0 ms: 1.17x faster                                                      |
| tomli_loads              | 2.40 sec                                                         | 2.10 sec: 1.14x faster                                                     |
| mako                     | 10.4 ms                                                          | 9.15 ms: 1.13x faster                                                      |
| scimark_fft              | 312 ms                                                           | 293 ms: 1.07x faster                                                       |
| regex_compile            | 144 ms                                                           | 136 ms: 1.06x faster                                                       |
| pyflate                  | 482 ms                                                           | 453 ms: 1.06x faster                                                       |
| float                    | 80.2 ms                                                          | 75.5 ms: 1.06x faster                                                      |
| pickle_dict              | 32.8 us                                                          | 31.1 us: 1.06x faster                                                      |
| pathlib                  | 17.1 ms                                                          | 16.2 ms: 1.06x faster                                                      |
| fannkuch                 | 353 ms                                                           | 336 ms: 1.05x faster                                                       |
| coverage                 | 83.5 ms                                                          | 79.6 ms: 1.05x faster                                                      |
| xml_etree_generate       | 85.7 ms                                                          | 81.8 ms: 1.05x faster                                                      |
| nbody                    | 87.8 ms                                                          | 84.1 ms: 1.04x faster                                                      |
| regex_dna                | 249 ms                                                           | 239 ms: 1.04x faster                                                       |
| crypto_pyaes             | 73.6 ms                                                          | 70.5 ms: 1.04x faster                                                      |
| pprint_safe_repr         | 818 ms                                                           | 787 ms: 1.04x faster                                                       |
| scimark_sparse_mat_mult  | 4.28 ms                                                          | 4.13 ms: 1.04x faster                                                      |
| xml_etree_iterparse      | 103 ms                                                           | 99.0 ms: 1.04x faster                                                      |
| unpickle_pure_python     | 224 us                                                           | 217 us: 1.04x faster                                                       |
| pprint_pformat           | 1.66 sec                                                         | 1.61 sec: 1.03x faster                                                     |
| dulwich_log              | 67.3 ms                                                          | 65.4 ms: 1.03x faster                                                      |
| go                       | 165 ms                                                           | 161 ms: 1.02x faster                                                       |
| deepcopy_memo            | 37.3 us                                                          | 36.5 us: 1.02x faster                                                      |
| telco                    | 8.40 ms                                                          | 8.23 ms: 1.02x faster                                                      |
| xml_etree_process        | 59.7 ms                                                          | 58.6 ms: 1.02x faster                                                      |
| html5lib                 | 74.7 ms                                                          | 73.3 ms: 1.02x faster                                                      |
| create_gc_cycles         | 2.00 ms                                                          | 1.97 ms: 1.02x faster                                                      |
| asyncio_websockets       | 395 ms                                                           | 389 ms: 1.02x faster                                                       |
| pidigits                 | 254 ms                                                           | 250 ms: 1.01x faster                                                       |
| logging_format           | 7.11 us                                                          | 7.02 us: 1.01x faster                                                      |
| pickle                   | 10.6 us                                                          | 10.5 us: 1.01x faster                                                      |
| sqlite_synth             | 2.80 us                                                          | 2.77 us: 1.01x faster                                                      |
| python_startup_no_site   | 8.85 ms                                                          | 8.86 ms: 1.00x slower                                                      |
| asyncio_tcp              | 378 ms                                                           | 381 ms: 1.01x slower                                                       |
| pickle_list              | 4.44 us                                                          | 4.48 us: 1.01x slower                                                      |
| async_tree_io_tg         | 900 ms                                                           | 914 ms: 1.02x slower                                                       |
| unpickle                 | 15.7 us                                                          | 16.0 us: 1.02x slower                                                      |
| sqlglot_parse            | 1.39 ms                                                          | 1.42 ms: 1.02x slower                                                      |
| tornado_http             | 119 ms                                                           | 122 ms: 1.02x slower                                                       |
| pickle_pure_python       | 307 us                                                           | 315 us: 1.02x slower                                                       |
| async_tree_cpu_io_mixed  | 604 ms                                                           | 620 ms: 1.03x slower                                                       |
| regex_effbot             | 3.40 ms                                                          | 3.49 ms: 1.03x slower                                                      |
| scimark_monte_carlo      | 65.5 ms                                                          | 67.3 ms: 1.03x slower                                                      |
| dask                     | 391 ms                                                           | 401 ms: 1.03x slower                                                       |
| async_tree_none          | 365 ms                                                           | 377 ms: 1.03x slower                                                       |
| sqlglot_transpile        | 1.76 ms                                                          | 1.82 ms: 1.03x slower                                                      |
| thrift                   | 880 us                                                           | 910 us: 1.03x slower                                                       |
| async_tree_memoization   | 460 ms                                                           | 476 ms: 1.03x slower                                                       |
| docutils                 | 2.98 sec                                                         | 3.09 sec: 1.04x slower                                                     |
| generators               | 33.5 ms                                                          | 34.8 ms: 1.04x slower                                                      |
| mdp                      | 2.46 sec                                                         | 2.56 sec: 1.04x slower                                                     |
| 2to3                     | 291 ms                                                           | 304 ms: 1.04x slower                                                       |
| gc_traversal             | 4.69 ms                                                          | 4.88 ms: 1.04x slower                                                      |
| sympy_expand             | 501 ms                                                           | 525 ms: 1.05x slower                                                       |
| unpickle_list            | 4.70 us                                                          | 4.93 us: 1.05x slower                                                      |
| pycparser                | 1.22 sec                                                         | 1.28 sec: 1.05x slower                                                     |
| hexiom                   | 6.35 ms                                                          | 6.68 ms: 1.05x slower                                                      |
| django_template          | 39.0 ms                                                          | 41.0 ms: 1.05x slower                                                      |
| sympy_str                | 295 ms                                                           | 310 ms: 1.05x slower                                                       |
| sympy_sum                | 155 ms                                                           | 164 ms: 1.06x slower                                                       |
| logging_silent           | 96.3 ns                                                          | 102 ns: 1.06x slower                                                       |
| bench_thread_pool        | 908 us                                                           | 965 us: 1.06x slower                                                       |
| comprehensions           | 17.0 us                                                          | 18.1 us: 1.07x slower                                                      |
| deepcopy_reduce          | 3.39 us                                                          | 3.64 us: 1.07x slower                                                      |
| nqueens                  | 88.4 ms                                                          | 94.9 ms: 1.07x slower                                                      |
| sqlglot_optimize         | 59.5 ms                                                          | 64.0 ms: 1.08x slower                                                      |
| async_generators         | 363 ms                                                           | 391 ms: 1.08x slower                                                       |
| sqlglot_normalize        | 120 ms                                                           | 130 ms: 1.08x slower                                                       |
| deepcopy                 | 377 us                                                           | 408 us: 1.08x slower                                                       |
| genshi_text              | 25.9 ms                                                          | 28.1 ms: 1.09x slower                                                      |
| typing_runtime_protocols | 171 us                                                           | 187 us: 1.09x slower                                                       |
| sympy_integrate          | 23.2 ms                                                          | 25.4 ms: 1.10x slower                                                      |
| raytrace                 | 260 ms                                                           | 286 ms: 1.10x slower                                                       |
| chaos                    | 59.6 ms                                                          | 65.7 ms: 1.10x slower                                                      |
| deltablue                | 3.37 ms                                                          | 3.74 ms: 1.11x slower                                                      |
| pylint                   | 339 ms                                                           | 377 ms: 1.11x slower                                                       |
| genshi_xml               | 58.1 ms                                                          | 64.9 ms: 1.12x slower                                                      |
| scimark_sor              | 119 ms                                                           | 137 ms: 1.15x slower                                                       |
| scimark_lu               | 97.5 ms                                                          | 117 ms: 1.20x slower                                                       |
| Geometric mean           | (ref)                                                            | 1.01x slower                                                               |

Benchmark hidden because not significant (15): bench_mp_pool, coroutines, xml_etree_parse, json_dumps, logging_simple, json, json_loads, meteor_contest, asyncio_tcp_ssl, python_startup, async_tree_io, async_tree_cpu_io_mixed_tg, regex_v8, async_tree_none_tg, async_tree_memoization_tg
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, chameleon, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 95.74% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.06x