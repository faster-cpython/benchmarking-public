# Results vs. base

- fork: brandtbucher
- ref: underflow_static_no_
- machine: linux-x86_64
- commit hash: bab095f
- commit date: 2024-08-26
- overall geometric mean: 1.02x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 276 ms                                                                | 283 ms: 1.03x slower                                                        |
| docutils       | 3.04 sec                                                              | 3.35 sec: 1.10x slower                                                      |
| html5lib       | 63.4 ms                                                               | 71.2 ms: 1.12x slower                                                       |
| tornado_http   | 94.7 ms                                                               | 102 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.08x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f |
|------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| coroutines       | 23.0 ms                                                               | 22.7 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl  | 1.81 sec                                                              | 1.81 sec: 1.00x faster                                                      |
| async_generators | 454 ms                                                                | 460 ms: 1.01x slower                                                        |
| async_tree_io    | 924 ms                                                                | 939 ms: 1.02x slower                                                        |
| async_tree_io_tg | 886 ms                                                                | 903 ms: 1.02x slower                                                        |
| asyncio_tcp      | 499 ms                                                                | 522 ms: 1.05x slower                                                        |
| Geometric mean   | (ref)                                                                 | 1.01x slower                                                                |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, async_tree_none, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                | 187 ms: 1.00x faster                                                        |
| float          | 70.4 ms                                                               | 70.9 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.9 ms                                                               | 24.5 ms: 1.02x slower                                                       |
| regex_effbot   | 3.51 ms                                                               | 3.61 ms: 1.03x slower                                                       |
| regex_dna      | 210 ms                                                                | 218 ms: 1.04x slower                                                        |
| regex_compile  | 142 ms                                                                | 151 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 213 us                                                                | 205 us: 1.04x faster                                                        |
| xml_etree_process    | 54.7 ms                                                               | 54.1 ms: 1.01x faster                                                       |
| xml_etree_generate   | 77.7 ms                                                               | 77.1 ms: 1.01x faster                                                       |
| json_loads           | 28.6 us                                                               | 28.4 us: 1.01x faster                                                       |
| xml_etree_iterparse  | 97.7 ms                                                               | 98.8 ms: 1.01x slower                                                       |
| tomli_loads          | 1.92 sec                                                              | 1.99 sec: 1.04x slower                                                      |
| pickle_pure_python   | 302 us                                                                | 314 us: 1.04x slower                                                        |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (2): json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.6 ms: 1.00x slower                                                       |
| python_startup_no_site | 7.14 ms                                                               | 7.18 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 25.7 ms                                                               | 24.8 ms: 1.04x faster                                                       |
| mako            | 9.79 ms                                                               | 9.60 ms: 1.02x faster                                                       |
| django_template | 35.6 ms                                                               | 37.2 ms: 1.05x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20240823-linux-x86_64-python-5fce482c9a9d18d36c81-3.14.0a0-5fce482 | bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo            | 27.0 us                                                               | 25.7 us: 1.05x faster                                                       |
| richards_super           | 45.0 ms                                                               | 43.2 ms: 1.04x faster                                                       |
| unpickle_pure_python     | 213 us                                                                | 205 us: 1.04x faster                                                        |
| genshi_text              | 25.7 ms                                                               | 24.8 ms: 1.04x faster                                                       |
| richards                 | 38.6 ms                                                               | 37.7 ms: 1.02x faster                                                       |
| pyflate                  | 450 ms                                                                | 442 ms: 1.02x faster                                                        |
| mako                     | 9.79 ms                                                               | 9.60 ms: 1.02x faster                                                       |
| spectral_norm            | 101 ms                                                                | 99.5 ms: 1.02x faster                                                       |
| crypto_pyaes             | 66.6 ms                                                               | 65.5 ms: 1.02x faster                                                       |
| nqueens                  | 85.7 ms                                                               | 84.4 ms: 1.02x faster                                                       |
| coroutines               | 23.0 ms                                                               | 22.7 ms: 1.01x faster                                                       |
| scimark_sparse_mat_mult  | 4.47 ms                                                               | 4.42 ms: 1.01x faster                                                       |
| thrift                   | 789 us                                                                | 779 us: 1.01x faster                                                        |
| typing_runtime_protocols | 165 us                                                                | 164 us: 1.01x faster                                                        |
| xml_etree_process        | 54.7 ms                                                               | 54.1 ms: 1.01x faster                                                       |
| comprehensions           | 16.7 us                                                               | 16.5 us: 1.01x faster                                                       |
| meteor_contest           | 106 ms                                                                | 105 ms: 1.01x faster                                                        |
| scimark_fft              | 314 ms                                                                | 311 ms: 1.01x faster                                                        |
| pathlib                  | 15.8 ms                                                               | 15.6 ms: 1.01x faster                                                       |
| xml_etree_generate       | 77.7 ms                                                               | 77.1 ms: 1.01x faster                                                       |
| json_loads               | 28.6 us                                                               | 28.4 us: 1.01x faster                                                       |
| bpe_tokeniser            | 4.43 sec                                                              | 4.42 sec: 1.00x faster                                                      |
| asyncio_tcp_ssl          | 1.81 sec                                                              | 1.81 sec: 1.00x faster                                                      |
| pidigits                 | 187 ms                                                                | 187 ms: 1.00x faster                                                        |
| python_startup           | 10.5 ms                                                               | 10.6 ms: 1.00x slower                                                       |
| hexiom                   | 6.89 ms                                                               | 6.92 ms: 1.01x slower                                                       |
| python_startup_no_site   | 7.14 ms                                                               | 7.18 ms: 1.01x slower                                                       |
| float                    | 70.4 ms                                                               | 70.9 ms: 1.01x slower                                                       |
| scimark_lu               | 109 ms                                                                | 110 ms: 1.01x slower                                                        |
| telco                    | 7.63 ms                                                               | 7.70 ms: 1.01x slower                                                       |
| xml_etree_iterparse      | 97.7 ms                                                               | 98.8 ms: 1.01x slower                                                       |
| async_generators         | 454 ms                                                                | 460 ms: 1.01x slower                                                        |
| pycparser                | 1.18 sec                                                              | 1.19 sec: 1.01x slower                                                      |
| raytrace                 | 276 ms                                                                | 280 ms: 1.02x slower                                                        |
| create_gc_cycles         | 1.75 ms                                                               | 1.78 ms: 1.02x slower                                                       |
| async_tree_io            | 924 ms                                                                | 939 ms: 1.02x slower                                                        |
| go                       | 170 ms                                                                | 173 ms: 1.02x slower                                                        |
| async_tree_io_tg         | 886 ms                                                                | 903 ms: 1.02x slower                                                        |
| pprint_pformat           | 1.49 sec                                                              | 1.52 sec: 1.02x slower                                                      |
| gc_traversal             | 3.58 ms                                                               | 3.66 ms: 1.02x slower                                                       |
| regex_v8                 | 23.9 ms                                                               | 24.5 ms: 1.02x slower                                                       |
| deltablue                | 3.18 ms                                                               | 3.26 ms: 1.03x slower                                                       |
| logging_format           | 6.04 us                                                               | 6.19 us: 1.03x slower                                                       |
| regex_effbot             | 3.51 ms                                                               | 3.61 ms: 1.03x slower                                                       |
| 2to3                     | 276 ms                                                                | 283 ms: 1.03x slower                                                        |
| bench_thread_pool        | 817 us                                                                | 844 us: 1.03x slower                                                        |
| tomli_loads              | 1.92 sec                                                              | 1.99 sec: 1.04x slower                                                      |
| sympy_expand             | 504 ms                                                                | 523 ms: 1.04x slower                                                        |
| regex_dna                | 210 ms                                                                | 218 ms: 1.04x slower                                                        |
| pickle_pure_python       | 302 us                                                                | 314 us: 1.04x slower                                                        |
| scimark_monte_carlo      | 62.5 ms                                                               | 65.2 ms: 1.04x slower                                                       |
| chaos                    | 58.6 ms                                                               | 61.2 ms: 1.04x slower                                                       |
| asyncio_tcp              | 499 ms                                                                | 522 ms: 1.05x slower                                                        |
| django_template          | 35.6 ms                                                               | 37.2 ms: 1.05x slower                                                       |
| deepcopy                 | 265 us                                                                | 278 us: 1.05x slower                                                        |
| sqlglot_optimize         | 58.1 ms                                                               | 61.1 ms: 1.05x slower                                                       |
| sqlglot_normalize        | 113 ms                                                                | 120 ms: 1.06x slower                                                        |
| regex_compile            | 142 ms                                                                | 151 ms: 1.06x slower                                                        |
| mdp                      | 2.56 sec                                                              | 2.73 sec: 1.06x slower                                                      |
| sympy_integrate          | 22.8 ms                                                               | 24.5 ms: 1.08x slower                                                       |
| tornado_http             | 94.7 ms                                                               | 102 ms: 1.08x slower                                                        |
| sympy_str                | 299 ms                                                                | 328 ms: 1.10x slower                                                        |
| docutils                 | 3.04 sec                                                              | 3.35 sec: 1.10x slower                                                      |
| pylint                   | 372 ms                                                                | 412 ms: 1.11x slower                                                        |
| sqlglot_transpile        | 1.69 ms                                                               | 1.88 ms: 1.12x slower                                                       |
| html5lib                 | 63.4 ms                                                               | 71.2 ms: 1.12x slower                                                       |
| sympy_sum                | 171 ms                                                                | 194 ms: 1.13x slower                                                        |
| sqlglot_parse            | 1.34 ms                                                               | 1.53 ms: 1.15x slower                                                       |
| generators               | 33.3 ms                                                               | 41.1 ms: 1.23x slower                                                       |
| Geometric mean           | (ref)                                                                 | 1.02x slower                                                                |

Benchmark hidden because not significant (20): async_tree_cpu_io_mixed, logging_silent, json, genshi_xml, nbody, json_dumps, xml_etree_parse, async_tree_none, logging_simple, asyncio_websockets, coverage, scimark_sor, bench_mp_pool, pprint_safe_repr, fannkuch, async_tree_cpu_io_mixed_tg, deepcopy_reduce, async_tree_memoization, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.03x