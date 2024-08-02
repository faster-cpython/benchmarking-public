# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: no_cold_exits
- machine: linux-x86_64
- commit hash: a1bdb94
- commit date: 2024-06-18
- overall geometric mean: 1.00x slower
- HPT reliability: 95.01%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 306 ms: 1.05x slower                                                       |
| docutils       | 2.98 sec                                                         | 3.12 sec: 1.05x slower                                                     |
| tornado_http   | 119 ms                                                           | 123 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                            | 1.03x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|-------------------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg        | 900 ms                                                           | 877 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed | 604 ms                                                           | 618 ms: 1.02x slower                                                       |
| async_tree_none         | 365 ms                                                           | 375 ms: 1.03x slower                                                       |
| async_tree_io           | 873 ms                                                           | 906 ms: 1.04x slower                                                       |
| Geometric mean          | (ref)                                                            | 1.01x slower                                                               |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_memoization_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 74.8 ms: 1.07x faster                                                      |
| nbody          | 87.8 ms                                                          | 83.5 ms: 1.05x faster                                                      |
| pidigits       | 254 ms                                                           | 250 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                            | 1.05x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 238 ms: 1.05x faster                                                       |
| regex_compile  | 144 ms                                                           | 138 ms: 1.04x faster                                                       |
| regex_v8       | 26.0 ms                                                          | 25.9 ms: 1.01x faster                                                      |
| regex_effbot   | 3.40 ms                                                          | 3.45 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                            | 1.02x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.11 sec: 1.14x faster                                                     |
| xml_etree_generate   | 85.7 ms                                                          | 80.8 ms: 1.06x faster                                                      |
| pickle_dict          | 32.8 us                                                          | 31.4 us: 1.05x faster                                                      |
| unpickle             | 15.7 us                                                          | 15.1 us: 1.04x faster                                                      |
| xml_etree_process    | 59.7 ms                                                          | 58.0 ms: 1.03x faster                                                      |
| xml_etree_iterparse  | 103 ms                                                           | 99.6 ms: 1.03x faster                                                      |
| unpickle_pure_python | 224 us                                                           | 220 us: 1.02x faster                                                       |
| pickle_list          | 4.44 us                                                          | 4.35 us: 1.02x faster                                                      |
| json_loads           | 25.0 us                                                          | 25.2 us: 1.01x slower                                                      |
| xml_etree_parse      | 144 ms                                                           | 145 ms: 1.01x slower                                                       |
| pickle_pure_python   | 307 us                                                           | 312 us: 1.01x slower                                                       |
| unpickle_list        | 4.70 us                                                          | 4.85 us: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                            | 1.02x faster                                                               |

Benchmark hidden because not significant (2): json_dumps, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|------------------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 8.85 ms                                                          | 8.94 ms: 1.01x slower                                                      |
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                      |
| Geometric mean         | (ref)                                                            | 1.01x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|-----------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                          | 9.24 ms: 1.12x faster                                                      |
| django_template | 39.0 ms                                                          | 41.5 ms: 1.07x slower                                                      |
| genshi_xml      | 58.1 ms                                                          | 63.6 ms: 1.09x slower                                                      |
| genshi_text     | 25.9 ms                                                          | 28.7 ms: 1.11x slower                                                      |
| Geometric mean  | (ref)                                                            | 1.04x slower                                                               |

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-pythonperf2-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|--------------------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo            | 37.3 us                                                          | 29.6 us: 1.26x faster                                                      |
| deepcopy                 | 377 us                                                           | 304 us: 1.24x faster                                                       |
| spectral_norm            | 97.3 ms                                                          | 82.9 ms: 1.17x faster                                                      |
| richards                 | 53.4 ms                                                          | 45.8 ms: 1.17x faster                                                      |
| tomli_loads              | 2.40 sec                                                         | 2.11 sec: 1.14x faster                                                     |
| richards_super           | 61.2 ms                                                          | 53.7 ms: 1.14x faster                                                      |
| mako                     | 10.4 ms                                                          | 9.24 ms: 1.12x faster                                                      |
| deepcopy_reduce          | 3.39 us                                                          | 3.05 us: 1.11x faster                                                      |
| scimark_sparse_mat_mult  | 4.28 ms                                                          | 3.92 ms: 1.09x faster                                                      |
| pyflate                  | 482 ms                                                           | 442 ms: 1.09x faster                                                       |
| float                    | 80.2 ms                                                          | 74.8 ms: 1.07x faster                                                      |
| scimark_fft              | 312 ms                                                           | 293 ms: 1.07x faster                                                       |
| xml_etree_generate       | 85.7 ms                                                          | 80.8 ms: 1.06x faster                                                      |
| gc_traversal             | 4.69 ms                                                          | 4.42 ms: 1.06x faster                                                      |
| nbody                    | 87.8 ms                                                          | 83.5 ms: 1.05x faster                                                      |
| regex_dna                | 249 ms                                                           | 238 ms: 1.05x faster                                                       |
| pathlib                  | 17.1 ms                                                          | 16.3 ms: 1.05x faster                                                      |
| pickle_dict              | 32.8 us                                                          | 31.4 us: 1.05x faster                                                      |
| pprint_safe_repr         | 818 ms                                                           | 781 ms: 1.05x faster                                                       |
| fannkuch                 | 353 ms                                                           | 337 ms: 1.05x faster                                                       |
| create_gc_cycles         | 2.00 ms                                                          | 1.92 ms: 1.05x faster                                                      |
| crypto_pyaes             | 73.6 ms                                                          | 70.4 ms: 1.04x faster                                                      |
| regex_compile            | 144 ms                                                           | 138 ms: 1.04x faster                                                       |
| unpickle                 | 15.7 us                                                          | 15.1 us: 1.04x faster                                                      |
| xml_etree_process        | 59.7 ms                                                          | 58.0 ms: 1.03x faster                                                      |
| xml_etree_iterparse      | 103 ms                                                           | 99.6 ms: 1.03x faster                                                      |
| telco                    | 8.40 ms                                                          | 8.17 ms: 1.03x faster                                                      |
| async_tree_io_tg         | 900 ms                                                           | 877 ms: 1.03x faster                                                       |
| pprint_pformat           | 1.66 sec                                                         | 1.62 sec: 1.02x faster                                                     |
| unpickle_pure_python     | 224 us                                                           | 220 us: 1.02x faster                                                       |
| pickle_list              | 4.44 us                                                          | 4.35 us: 1.02x faster                                                      |
| pidigits                 | 254 ms                                                           | 250 ms: 1.01x faster                                                       |
| logging_format           | 7.11 us                                                          | 7.02 us: 1.01x faster                                                      |
| asyncio_websockets       | 395 ms                                                           | 392 ms: 1.01x faster                                                       |
| bpe_tokeniser            | 5.14 sec                                                         | 5.11 sec: 1.01x faster                                                     |
| regex_v8                 | 26.0 ms                                                          | 25.9 ms: 1.01x faster                                                      |
| sqlite_synth             | 2.80 us                                                          | 2.79 us: 1.00x faster                                                      |
| scimark_monte_carlo      | 65.5 ms                                                          | 65.8 ms: 1.00x slower                                                      |
| asyncio_tcp              | 378 ms                                                           | 380 ms: 1.01x slower                                                       |
| json_loads               | 25.0 us                                                          | 25.2 us: 1.01x slower                                                      |
| go                       | 165 ms                                                           | 166 ms: 1.01x slower                                                       |
| xml_etree_parse          | 144 ms                                                           | 145 ms: 1.01x slower                                                       |
| json                     | 5.35 ms                                                          | 5.41 ms: 1.01x slower                                                      |
| python_startup_no_site   | 8.85 ms                                                          | 8.94 ms: 1.01x slower                                                      |
| python_startup           | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                      |
| regex_effbot             | 3.40 ms                                                          | 3.45 ms: 1.01x slower                                                      |
| pickle_pure_python       | 307 us                                                           | 312 us: 1.01x slower                                                       |
| meteor_contest           | 128 ms                                                           | 130 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed  | 604 ms                                                           | 618 ms: 1.02x slower                                                       |
| pycparser                | 1.22 sec                                                         | 1.25 sec: 1.02x slower                                                     |
| async_tree_none          | 365 ms                                                           | 375 ms: 1.03x slower                                                       |
| thrift                   | 880 us                                                           | 905 us: 1.03x slower                                                       |
| unpickle_list            | 4.70 us                                                          | 4.85 us: 1.03x slower                                                      |
| sqlglot_parse            | 1.39 ms                                                          | 1.44 ms: 1.03x slower                                                      |
| tornado_http             | 119 ms                                                           | 123 ms: 1.03x slower                                                       |
| coroutines               | 22.0 ms                                                          | 22.8 ms: 1.04x slower                                                      |
| async_tree_io            | 873 ms                                                           | 906 ms: 1.04x slower                                                       |
| dask                     | 391 ms                                                           | 405 ms: 1.04x slower                                                       |
| generators               | 33.5 ms                                                          | 34.9 ms: 1.04x slower                                                      |
| sqlglot_transpile        | 1.76 ms                                                          | 1.84 ms: 1.04x slower                                                      |
| mdp                      | 2.46 sec                                                         | 2.57 sec: 1.04x slower                                                     |
| docutils                 | 2.98 sec                                                         | 3.12 sec: 1.05x slower                                                     |
| hexiom                   | 6.35 ms                                                          | 6.66 ms: 1.05x slower                                                      |
| 2to3                     | 291 ms                                                           | 306 ms: 1.05x slower                                                       |
| sqlglot_optimize         | 59.5 ms                                                          | 62.5 ms: 1.05x slower                                                      |
| nqueens                  | 88.4 ms                                                          | 93.3 ms: 1.06x slower                                                      |
| sympy_expand             | 501 ms                                                           | 529 ms: 1.06x slower                                                       |
| async_generators         | 363 ms                                                           | 385 ms: 1.06x slower                                                       |
| sqlglot_normalize        | 120 ms                                                           | 128 ms: 1.06x slower                                                       |
| sympy_str                | 295 ms                                                           | 314 ms: 1.06x slower                                                       |
| django_template          | 39.0 ms                                                          | 41.5 ms: 1.07x slower                                                      |
| comprehensions           | 17.0 us                                                          | 18.2 us: 1.07x slower                                                      |
| sympy_sum                | 155 ms                                                           | 168 ms: 1.08x slower                                                       |
| typing_runtime_protocols | 171 us                                                           | 185 us: 1.08x slower                                                       |
| logging_silent           | 96.3 ns                                                          | 105 ns: 1.09x slower                                                       |
| deltablue                | 3.37 ms                                                          | 3.69 ms: 1.09x slower                                                      |
| genshi_xml               | 58.1 ms                                                          | 63.6 ms: 1.09x slower                                                      |
| sympy_integrate          | 23.2 ms                                                          | 25.7 ms: 1.11x slower                                                      |
| genshi_text              | 25.9 ms                                                          | 28.7 ms: 1.11x slower                                                      |
| chaos                    | 59.6 ms                                                          | 66.3 ms: 1.11x slower                                                      |
| raytrace                 | 260 ms                                                           | 291 ms: 1.12x slower                                                       |
| pylint                   | 339 ms                                                           | 380 ms: 1.12x slower                                                       |
| scimark_sor              | 119 ms                                                           | 136 ms: 1.15x slower                                                       |
| scimark_lu               | 97.5 ms                                                          | 116 ms: 1.19x slower                                                       |
| Geometric mean           | (ref)                                                            | 1.00x slower                                                               |

Benchmark hidden because not significant (13): bench_mp_pool, json_dumps, dulwich_log, html5lib, coverage, asyncio_tcp_ssl, logging_simple, pickle, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_memoization_tg, bench_thread_pool, async_tree_memoization
Ignored benchmarks (5) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 95.01% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.07x