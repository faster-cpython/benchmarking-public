# Results vs. 3.13.0b2

- fork: python
- ref: 498376d7a7d6f704f22a
- machine: windows-amd64
- commit hash: 498376d
- commit date: 2024-08-02
- overall geometric mean: 1.00x slower
- HPT reliability: 99.46%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 240 ms: 1.16x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.84 sec: 1.13x slower                                                     |
| html5lib       | 35.0 ms                                                         | 41.0 ms: 1.17x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 96.1 ms: 1.17x slower                                                      |
| Geometric mean | (ref)                                                           | 1.16x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg          | 605 ms                                                          | 537 ms: 1.13x faster                                                       |
| async_tree_none_tg        | 202 ms                                                          | 189 ms: 1.07x faster                                                       |
| async_tree_io             | 588 ms                                                          | 551 ms: 1.07x faster                                                       |
| async_tree_memoization_tg | 258 ms                                                          | 246 ms: 1.05x faster                                                       |
| async_tree_none           | 218 ms                                                          | 212 ms: 1.03x faster                                                       |
| Geometric mean            | (ref)                                                           | 1.05x faster                                                               |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 49.8 ms: 1.36x faster                                                      |
| float          | 49.7 ms                                                         | 44.9 ms: 1.11x faster                                                      |
| Geometric mean | (ref)                                                           | 1.15x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.62 ms: 1.02x slower                                                      |
| regex_dna      | 119 ms                                                          | 122 ms: 1.02x slower                                                       |
| regex_compile  | 78.0 ms                                                         | 89.4 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                           | 1.04x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.35 sec                                                        | 1.25 sec: 1.08x faster                                                     |
| xml_etree_iterparse  | 62.3 ms                                                         | 61.5 ms: 1.01x faster                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 52.6 ms: 1.01x faster                                                      |
| json_loads           | 14.2 us                                                         | 14.3 us: 1.01x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 92.9 ms: 1.02x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 37.5 ms: 1.03x slower                                                      |
| pickle_pure_python   | 175 us                                                          | 181 us: 1.03x slower                                                       |
| json_dumps           | 5.61 ms                                                         | 5.99 ms: 1.07x slower                                                      |
| unpickle_pure_python | 122 us                                                          | 136 us: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.0 ms: 1.08x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 18.2 ms: 1.12x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 4.96 ms: 1.28x faster                                                      |
| django_template | 21.7 ms                                                         | 24.7 ms: 1.14x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 39.0 ms: 1.23x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 17.9 ms: 1.24x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.08x slower                                                               |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                    | 8.11 ms                                                         | 519 us: 15.61x faster                                                      |
| spectral_norm             | 63.7 ms                                                         | 46.1 ms: 1.38x faster                                                      |
| deepcopy_memo             | 22.1 us                                                         | 16.2 us: 1.37x faster                                                      |
| nbody                     | 67.6 ms                                                         | 49.8 ms: 1.36x faster                                                      |
| mako                      | 6.36 ms                                                         | 4.96 ms: 1.28x faster                                                      |
| scimark_sor               | 75.3 ms                                                         | 59.9 ms: 1.26x faster                                                      |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 2.07 ms: 1.21x faster                                                      |
| deepcopy                  | 220 us                                                          | 183 us: 1.20x faster                                                       |
| scimark_fft               | 171 ms                                                          | 148 ms: 1.16x faster                                                       |
| crypto_pyaes              | 45.5 ms                                                         | 39.9 ms: 1.14x faster                                                      |
| async_tree_io_tg          | 605 ms                                                          | 537 ms: 1.13x faster                                                       |
| deepcopy_reduce           | 1.99 us                                                         | 1.78 us: 1.12x faster                                                      |
| float                     | 49.7 ms                                                         | 44.9 ms: 1.11x faster                                                      |
| fannkuch                  | 243 ms                                                          | 220 ms: 1.11x faster                                                       |
| pyflate                   | 279 ms                                                          | 257 ms: 1.08x faster                                                       |
| tomli_loads               | 1.35 sec                                                        | 1.25 sec: 1.08x faster                                                     |
| async_tree_none_tg        | 202 ms                                                          | 189 ms: 1.07x faster                                                       |
| async_tree_io             | 588 ms                                                          | 551 ms: 1.07x faster                                                       |
| json                      | 3.19 ms                                                         | 3.00 ms: 1.06x faster                                                      |
| async_tree_memoization_tg | 258 ms                                                          | 246 ms: 1.05x faster                                                       |
| scimark_monte_carlo       | 39.1 ms                                                         | 37.5 ms: 1.04x faster                                                      |
| async_tree_none           | 218 ms                                                          | 212 ms: 1.03x faster                                                       |
| telco                     | 4.67 ms                                                         | 4.54 ms: 1.03x faster                                                      |
| scimark_lu                | 56.6 ms                                                         | 55.6 ms: 1.02x faster                                                      |
| comprehensions            | 10.4 us                                                         | 10.2 us: 1.02x faster                                                      |
| xml_etree_iterparse       | 62.3 ms                                                         | 61.5 ms: 1.01x faster                                                      |
| xml_etree_generate        | 53.2 ms                                                         | 52.6 ms: 1.01x faster                                                      |
| meteor_contest            | 69.9 ms                                                         | 70.1 ms: 1.00x slower                                                      |
| json_loads                | 14.2 us                                                         | 14.3 us: 1.01x slower                                                      |
| gc_traversal              | 1.55 ms                                                         | 1.57 ms: 1.01x slower                                                      |
| pprint_pformat            | 966 ms                                                          | 983 ms: 1.02x slower                                                       |
| chaos                     | 38.4 ms                                                         | 39.0 ms: 1.02x slower                                                      |
| regex_effbot              | 1.58 ms                                                         | 1.62 ms: 1.02x slower                                                      |
| xml_etree_parse           | 90.9 ms                                                         | 92.9 ms: 1.02x slower                                                      |
| logging_format            | 6.22 us                                                         | 6.36 us: 1.02x slower                                                      |
| regex_dna                 | 119 ms                                                          | 122 ms: 1.02x slower                                                       |
| logging_simple            | 5.78 us                                                         | 5.95 us: 1.03x slower                                                      |
| xml_etree_process         | 36.4 ms                                                         | 37.5 ms: 1.03x slower                                                      |
| pickle_pure_python        | 175 us                                                          | 181 us: 1.03x slower                                                       |
| create_gc_cycles          | 888 us                                                          | 919 us: 1.04x slower                                                       |
| generators                | 19.6 ms                                                         | 20.8 ms: 1.06x slower                                                      |
| json_dumps                | 5.61 ms                                                         | 5.99 ms: 1.07x slower                                                      |
| logging_silent            | 52.9 ns                                                         | 56.5 ns: 1.07x slower                                                      |
| bench_thread_pool         | 768 us                                                          | 825 us: 1.07x slower                                                       |
| mdp                       | 1.31 sec                                                        | 1.41 sec: 1.08x slower                                                     |
| pathlib                   | 75.9 ms                                                         | 82.1 ms: 1.08x slower                                                      |
| python_startup            | 20.3 ms                                                         | 22.0 ms: 1.08x slower                                                      |
| nqueens                   | 56.7 ms                                                         | 61.9 ms: 1.09x slower                                                      |
| coroutines                | 12.8 ms                                                         | 14.1 ms: 1.11x slower                                                      |
| sqlglot_parse             | 748 us                                                          | 834 us: 1.11x slower                                                       |
| unpickle_pure_python      | 122 us                                                          | 136 us: 1.12x slower                                                       |
| coverage                  | 42.1 ms                                                         | 47.1 ms: 1.12x slower                                                      |
| python_startup_no_site    | 16.2 ms                                                         | 18.2 ms: 1.12x slower                                                      |
| sqlglot_normalize         | 173 ms                                                          | 195 ms: 1.13x slower                                                       |
| sqlglot_optimize          | 32.7 ms                                                         | 36.9 ms: 1.13x slower                                                      |
| docutils                  | 1.63 sec                                                        | 1.84 sec: 1.13x slower                                                     |
| sqlglot_transpile         | 955 us                                                          | 1.08 ms: 1.13x slower                                                      |
| dulwich_log               | 38.0 ms                                                         | 43.1 ms: 1.13x slower                                                      |
| bench_mp_pool             | 64.8 ms                                                         | 73.7 ms: 1.14x slower                                                      |
| django_template           | 21.7 ms                                                         | 24.7 ms: 1.14x slower                                                      |
| richards_super            | 30.2 ms                                                         | 34.5 ms: 1.14x slower                                                      |
| async_generators          | 223 ms                                                          | 256 ms: 1.15x slower                                                       |
| regex_compile             | 78.0 ms                                                         | 89.4 ms: 1.15x slower                                                      |
| richards                  | 26.7 ms                                                         | 30.6 ms: 1.15x slower                                                      |
| sympy_sum                 | 84.4 ms                                                         | 97.3 ms: 1.15x slower                                                      |
| raytrace                  | 162 ms                                                          | 188 ms: 1.16x slower                                                       |
| 2to3                      | 207 ms                                                          | 240 ms: 1.16x slower                                                       |
| html5lib                  | 35.0 ms                                                         | 41.0 ms: 1.17x slower                                                      |
| tornado_http              | 81.8 ms                                                         | 96.1 ms: 1.17x slower                                                      |
| sympy_str                 | 159 ms                                                          | 188 ms: 1.18x slower                                                       |
| typing_runtime_protocols  | 101 us                                                          | 121 us: 1.19x slower                                                       |
| sympy_integrate           | 12.2 ms                                                         | 14.7 ms: 1.20x slower                                                      |
| go                        | 82.1 ms                                                         | 101 ms: 1.22x slower                                                       |
| sympy_expand              | 271 ms                                                          | 332 ms: 1.23x slower                                                       |
| pylint                    | 205 ms                                                          | 252 ms: 1.23x slower                                                       |
| genshi_xml                | 31.6 ms                                                         | 39.0 ms: 1.23x slower                                                      |
| genshi_text               | 14.4 ms                                                         | 17.9 ms: 1.24x slower                                                      |
| deltablue                 | 1.88 ms                                                         | 2.36 ms: 1.25x slower                                                      |
| hexiom                    | 3.72 ms                                                         | 4.69 ms: 1.26x slower                                                      |
| asyncio_tcp               | 471 ms                                                          | 638 ms: 1.35x slower                                                       |
| Geometric mean            | (ref)                                                           | 1.00x slower                                                               |

Benchmark hidden because not significant (8): pycparser, regex_v8, async_tree_cpu_io_mixed_tg, async_tree_memoization, pidigits, pprint_safe_repr, async_tree_cpu_io_mixed, asyncio_tcp_ssl
Ignored benchmarks (10) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.46% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown